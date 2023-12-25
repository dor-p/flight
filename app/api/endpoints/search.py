# api/endpoints/search.py
import os
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from pydantic import BaseModel


if os.environ.get("RUNNING_IN_DOCKER"):
    from app.db.sessions import get_db_session
else:
    from db.sessions import get_db_session

from fastapi import APIRouter, Response
from pydantic import BaseModel
from fastapi import Request


router = APIRouter()


class SearchPayload(BaseModel):
    gene_name: str
    protein_variant: str


@router.options("/search")
def options_handler(request: Request):
    return Response(status_code=204)


@router.post("/search")
async def search_variants_by_gene_and_protein(request: Request, conn=Depends(get_db_session)):
    data = await request.json()
    gene_name = data.get('gene_name')
    gene_name = gene_name.upper()
    protein_variant = data.get('protein_variant')
    print("Got gene name and protein variant")
    print(gene_name, protein_variant)
    if "c." in protein_variant:
        last_letter = protein_variant.split(">")[1].capitalize()
        first_letter = protein_variant.split(">")[0][-1].capitalize()
        protein_variant = protein_variant[:-3]+first_letter+">"+last_letter
        rows = await conn.fetch("SELECT * FROM variants WHERE gene_name = $1 AND c_dot = $2 LIMIT 1", gene_name, protein_variant)
    elif "p." in protein_variant:
        protein_variant = protein_variant.replace("p.", "")
        rows = await conn.fetch("SELECT * FROM variants WHERE gene_name = $1 AND protein_variant = $2 LIMIT 1", gene_name, protein_variant)
    else:
        raise HTTPException(status_code=400, detail="Invalid protein variant")
    return rows
