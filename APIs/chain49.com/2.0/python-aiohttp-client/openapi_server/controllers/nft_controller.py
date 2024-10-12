from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_nft_meta_v2200_response import GetNFTMetaV2200Response
from openapi_server import util


async def get_nft_meta_v2(request: web.Request, blockchain, nft_contract, nft_token_id) -> web.Response:
    """Get NFT metadata V2

    Only works on Ethereum-like blockchains (currently ethereum and bsc)  Get metadata like name or description for a specified contract and token ID. The resulting data contains a link which can then be used to request the IPFS link for the actual image to display in a block explorer for example.  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.

    :param blockchain: NFT-compatible blockchain name
    :type blockchain: str
    :param nft_contract: Address of NFT contract
    :type nft_contract: str
    :param nft_token_id: Unique token ID of NFT
    :type nft_token_id: str

    """
    return web.Response(status=200)
