from typing import List, Dict
from aiohttp import web

from openapi_server.models.card_resume import CardResume
from openapi_server.models.serie import Serie
from openapi_server.models.serie_resume import SerieResume
from openapi_server.models.set import Set
from openapi_server.models.set_resume import SetResume
from openapi_server.models.string_endpoint import StringEndpoint
from openapi_server import util


async def categories_category_get(request: web.Request, category) -> web.Response:
    """categories_category_get

    

    :param category: 
    :type category: str

    """
    return web.Response(status=200)


async def categories_get(request: web.Request, ) -> web.Response:
    """categories_get

    


    """
    return web.Response(status=200)


async def dex_ids_dex_id_get(request: web.Request, dex_id) -> web.Response:
    """dex_ids_dex_id_get

    

    :param dex_id: 
    :type dex_id: str

    """
    return web.Response(status=200)


async def dex_ids_get(request: web.Request, ) -> web.Response:
    """dex_ids_get

    


    """
    return web.Response(status=200)


async def energy_types_energy_type_get(request: web.Request, energy_type) -> web.Response:
    """energy_types_energy_type_get

    

    :param energy_type: 
    :type energy_type: str

    """
    return web.Response(status=200)


async def energy_types_get(request: web.Request, ) -> web.Response:
    """energy_types_get

    


    """
    return web.Response(status=200)


async def hp_get(request: web.Request, ) -> web.Response:
    """hp_get

    


    """
    return web.Response(status=200)


async def hp_hp_get(request: web.Request, hp) -> web.Response:
    """hp_hp_get

    

    :param hp: 
    :type hp: str

    """
    return web.Response(status=200)


async def illustrators_get(request: web.Request, ) -> web.Response:
    """illustrators_get

    


    """
    return web.Response(status=200)


async def illustrators_illustrator_get(request: web.Request, illustrator) -> web.Response:
    """illustrators_illustrator_get

    

    :param illustrator: 
    :type illustrator: str

    """
    return web.Response(status=200)


async def rarities_get(request: web.Request, ) -> web.Response:
    """rarities_get

    


    """
    return web.Response(status=200)


async def rarities_rarity_get(request: web.Request, rarity) -> web.Response:
    """rarities_rarity_get

    

    :param rarity: 
    :type rarity: str

    """
    return web.Response(status=200)


async def regulation_marks_get(request: web.Request, ) -> web.Response:
    """regulation_marks_get

    


    """
    return web.Response(status=200)


async def regulation_marks_regulation_mark_get(request: web.Request, regulation_mark) -> web.Response:
    """regulation_marks_regulation_mark_get

    

    :param regulation_mark: 
    :type regulation_mark: str

    """
    return web.Response(status=200)


async def retreats_get(request: web.Request, ) -> web.Response:
    """retreats_get

    


    """
    return web.Response(status=200)


async def retreats_retreat_get(request: web.Request, retreat) -> web.Response:
    """retreats_retreat_get

    

    :param retreat: 
    :type retreat: str

    """
    return web.Response(status=200)


async def series_get(request: web.Request, ) -> web.Response:
    """series_get

    


    """
    return web.Response(status=200)


async def series_serie_get(request: web.Request, serie) -> web.Response:
    """series_serie_get

    

    :param serie: the serie ID or name
    :type serie: str

    """
    return web.Response(status=200)


async def sets_get(request: web.Request, ) -> web.Response:
    """sets_get

    


    """
    return web.Response(status=200)


async def sets_set_get(request: web.Request, set) -> web.Response:
    """sets_set_get

    

    :param set: the set ID or the set name
    :type set: str

    """
    return web.Response(status=200)


async def stages_get(request: web.Request, ) -> web.Response:
    """stages_get

    


    """
    return web.Response(status=200)


async def stages_stage_get(request: web.Request, stage) -> web.Response:
    """stages_stage_get

    

    :param stage: 
    :type stage: str

    """
    return web.Response(status=200)


async def suffixes_get(request: web.Request, ) -> web.Response:
    """suffixes_get

    


    """
    return web.Response(status=200)


async def suffixes_suffix_get(request: web.Request, suffix) -> web.Response:
    """suffixes_suffix_get

    

    :param suffix: 
    :type suffix: str

    """
    return web.Response(status=200)


async def trainer_types_get(request: web.Request, ) -> web.Response:
    """trainer_types_get

    


    """
    return web.Response(status=200)


async def trainer_types_trainer_type_get(request: web.Request, trainer_type) -> web.Response:
    """trainer_types_trainer_type_get

    

    :param trainer_type: 
    :type trainer_type: str

    """
    return web.Response(status=200)


async def types_get(request: web.Request, ) -> web.Response:
    """types_get

    


    """
    return web.Response(status=200)


async def types_type_get(request: web.Request, type) -> web.Response:
    """types_type_get

    

    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def variants_get(request: web.Request, ) -> web.Response:
    """variants_get

    


    """
    return web.Response(status=200)


async def variants_variant_get(request: web.Request, variant) -> web.Response:
    """variants_variant_get

    

    :param variant: 
    :type variant: str

    """
    return web.Response(status=200)
