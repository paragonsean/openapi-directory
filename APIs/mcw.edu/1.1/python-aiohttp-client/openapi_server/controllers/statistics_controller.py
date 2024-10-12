from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_active_object_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of active objects by type, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_active_object_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of active objects, by type, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_gene_type_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of gene types, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_gene_type_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of gene types, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_object_status_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of objects with given status, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_object_status_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of objects with given status, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_objects_with_ref_seq_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of objects with reference sequence(s), by object type, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_objects_with_ref_seq_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of objects with reference sequence(s), by object type, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_objects_with_reference_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of objects with reference, by object type, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_objects_with_reference_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of objects with reference, by object type, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_objects_with_xdbs_count_using_get(request: web.Request, species_type_key, object_key, date_yyyymmdd) -> web.Response:
    """Count of objects with external database ids, by database id, for specified species, object type and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param object_key: objectKey
    :type object_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_objects_with_xdbs_diff_using_get(request: web.Request, species_type_key, object_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of objects with external database ids, by database id, for specified species, object type and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param object_key: objectKey
    :type object_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_protein_interaction_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of protein interactions, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_protein_interaction_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of protein interactions, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_qtl_inheritance_type_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of strains, by qtl inheritance type, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_qtl_inheritance_type_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of strains, by qtl inheritance type, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_retired_object_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of retired objects by type, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_retired_object_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of retired objects, by type, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_strain_type_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of strain types, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_strain_type_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of strain types, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_term_stats_using_get(request: web.Request, acc_id, filter_acc_id) -> web.Response:
    """getTermStats

    

    :param acc_id: accId
    :type acc_id: str
    :param filter_acc_id: filterAccId
    :type filter_acc_id: str

    """
    return web.Response(status=200)


async def get_withdrawn_object_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of withdrawn objects by type, for specified species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_withdrawn_object_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of withdrawn objects, by type, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_xdbs_count_using_get(request: web.Request, species_type_key, date_yyyymmdd) -> web.Response:
    """Count of external database ids, for specied species and date

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_yyyymmdd: dateYYYYMMDD
    :type date_yyyymmdd: str

    """
    return web.Response(status=200)


async def get_xdbs_diff_using_get(request: web.Request, species_type_key, date_from_yyyymmdd, date_to_yyyymmdd) -> web.Response:
    """Count difference of external database ids, for specified species and date range

    

    :param species_type_key: speciesTypeKey
    :type species_type_key: int
    :param date_from_yyyymmdd: dateFromYYYYMMDD
    :type date_from_yyyymmdd: str
    :param date_to_yyyymmdd: dateToYYYYMMDD
    :type date_to_yyyymmdd: str

    """
    return web.Response(status=200)
