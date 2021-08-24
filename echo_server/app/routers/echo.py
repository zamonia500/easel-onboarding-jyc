from typing import List

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/echo/", tags=["users"])
async def echo_query_parameter(request: Request):

    result = dict(argo="sync!")

    for key in request.query_params.keys():
        param_list: List = request.query_params.getlist(key)
        result[key] = param_list if len(param_list) > 1 else param_list[0]

    return result
