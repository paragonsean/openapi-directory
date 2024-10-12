from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_board_assets_result import AddBoardAssetsResult
from openapi_server.models.board_asset import BoardAsset
from openapi_server.models.board_created import BoardCreated
from openapi_server.models.board_detail import BoardDetail
from openapi_server.models.board_info import BoardInfo
from openapi_server.models.board_list import BoardList
from openapi_server.models.board_relationship import BoardRelationship
from openapi_server.models.board_sort_order import BoardSortOrder
from openapi_server.models.comment_created import CommentCreated
from openapi_server.models.comment_request import CommentRequest
from openapi_server.models.comments_list import CommentsList
from openapi_server import util


async def v3_boards_board_id_assets_asset_id_delete(request: web.Request, board_id, asset_id, accept_language=None) -> web.Response:
    """Remove an asset from a board

    

    :param board_id: Specify the board to remove an asset from.
    :type board_id: str
    :param asset_id: Specify the asset to remove from the board.
    :type asset_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)


async def v3_boards_board_id_assets_asset_id_put(request: web.Request, board_id, asset_id, accept_language=None) -> web.Response:
    """Add an asset to a board

    

    :param board_id: Specify the board to add an asset to.
    :type board_id: str
    :param asset_id: Specify the asset to add to the board. If it is already in the board&#39;s asset collection, no action is taken.
    :type asset_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)


async def v3_boards_board_id_assets_delete(request: web.Request, board_id, accept_language=None, asset_ids=None) -> web.Response:
    """Remove assets from a board

    

    :param board_id: Specify the board to remove assets from.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param asset_ids: List the assets to be removed from the board.
    :type asset_ids: List[str]

    """
    return web.Response(status=200)


async def v3_boards_board_id_assets_put(request: web.Request, board_id, accept_language=None, body=None) -> web.Response:
    """Add assets to a board

    

    :param board_id: Specify the board to add assets to.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param body: List assets to add to the board.
    :type body: list | bytes

    """
    body = [BoardAsset.from_dict(d) for d in body]
    return web.Response(status=200)


async def v3_boards_board_id_comments_comment_id_delete(request: web.Request, board_id, comment_id, accept_language=None) -> web.Response:
    """Delete a comment from a board

    

    :param board_id: Specify the board containing the comment to delete.
    :type board_id: str
    :param comment_id: Specify the comment to delete.
    :type comment_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)


async def v3_boards_board_id_comments_get(request: web.Request, board_id, accept_language=None) -> web.Response:
    """Get comments from a board

    

    :param board_id: Specify the board to retrieve comments from.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)


async def v3_boards_board_id_comments_post(request: web.Request, board_id, accept_language=None, body=None) -> web.Response:
    """Add a comment to a board

    

    :param board_id: Specify the board to add a comment to.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param body: Comment to be added to the board.
    :type body: dict | bytes

    """
    body = CommentRequest.from_dict(body)
    return web.Response(status=200)


async def v3_boards_board_id_delete(request: web.Request, board_id, accept_language=None) -> web.Response:
    """Delete a board

    

    :param board_id: Specify the board to delete.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)


async def v3_boards_board_id_get(request: web.Request, board_id, accept_language=None) -> web.Response:
    """Get assets and metadata for a specific board

    

    :param board_id: Retrieve details for a specific board.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)


async def v3_boards_board_id_put(request: web.Request, board_id, accept_language=None, body=None) -> web.Response:
    """Update a board

    

    :param board_id: Specify the board to update.
    :type board_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param body: Specify a new name and description for the board (name is required).
    :type body: dict | bytes

    """
    body = BoardInfo.from_dict(body)
    return web.Response(status=200)


async def v3_boards_get(request: web.Request, accept_language=None, page=None, board_relationship=None, sort_order=None, page_size=None) -> web.Response:
    """Get all boards that the user participates in

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param page: Request results starting at a page number (default is 1).
    :type page: int
    :param board_relationship: Search for boards the user owns or has been invited to as an editor.
    :type board_relationship: dict | bytes
    :param sort_order: Sort the list of boards by last update date or name. Defaults to date_last_updated_descending.
    :type sort_order: dict | bytes
    :param page_size: Request number of boards to return in each page. (default is 30).
    :type page_size: int

    """
    board_relationship = .from_dict(board_relationship)
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)


async def v3_boards_post(request: web.Request, accept_language=None, body=None) -> web.Response:
    """Create a new board

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param body: Specify a name and description of the board to create (name is required).
    :type body: dict | bytes

    """
    body = BoardInfo.from_dict(body)
    return web.Response(status=200)
