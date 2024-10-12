from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_annotation_result import EntityAnnotationResult
from openapi_server import util


async def get_annotate(request: web.Request, content=None, include_category=None, exclude_category=None, min_length=None, longest_only=None, include_abbreviation=None, include_acronym=None, include_numbers=None) -> web.Response:
    """Annotate a given text using SciGraph annotator

    

    :param content: The text content to annotate
    :type content: str
    :param include_category: Categories to include for annotation
    :type include_category: List[str]
    :param exclude_category: Categories to exclude for annotation
    :type exclude_category: List[str]
    :param min_length: The minimum number of characters in the annotated entity
    :type min_length: str
    :param longest_only: Should only the longest entity be returned for an overlapping group
    :type longest_only: bool
    :param include_abbreviation: Should abbreviations be included
    :type include_abbreviation: bool
    :param include_acronym: Should acronyms be included
    :type include_acronym: bool
    :param include_numbers: Should numbers be included
    :type include_numbers: bool

    """
    return web.Response(status=200)


async def get_annotate_entities(request: web.Request, content=None, include_category=None, exclude_category=None, min_length=None, longest_only=None, include_abbreviation=None, include_acronym=None, include_numbers=None) -> web.Response:
    """Annotate a given content using SciGraph annotator and get all entities from content

    

    :param content: The text content to annotate
    :type content: str
    :param include_category: Categories to include for annotation
    :type include_category: List[str]
    :param exclude_category: Categories to exclude for annotation
    :type exclude_category: List[str]
    :param min_length: The minimum number of characters in the annotated entity
    :type min_length: str
    :param longest_only: Should only the longest entity be returned for an overlapping group
    :type longest_only: bool
    :param include_abbreviation: Should abbreviations be included
    :type include_abbreviation: bool
    :param include_acronym: Should acronyms be included
    :type include_acronym: bool
    :param include_numbers: Should numbers be included
    :type include_numbers: bool

    """
    return web.Response(status=200)


async def post_annotate(request: web.Request, content=None, include_category=None, exclude_category=None, min_length=None, longest_only=None, include_abbreviation=None, include_acronym=None, include_numbers=None) -> web.Response:
    """Annotate a given text using SciGraph annotator

    

    :param content: The text content to annotate
    :type content: str
    :param include_category: Categories to include for annotation
    :type include_category: List[str]
    :param exclude_category: Categories to exclude for annotation
    :type exclude_category: List[str]
    :param min_length: The minimum number of characters in the annotated entity
    :type min_length: str
    :param longest_only: Should only the longest entity be returned for an overlapping group
    :type longest_only: bool
    :param include_abbreviation: Should abbreviations be included
    :type include_abbreviation: bool
    :param include_acronym: Should acronyms be included
    :type include_acronym: bool
    :param include_numbers: Should numbers be included
    :type include_numbers: bool

    """
    return web.Response(status=200)


async def post_annotate_entities(request: web.Request, content=None, include_category=None, exclude_category=None, min_length=None, longest_only=None, include_abbreviation=None, include_acronym=None, include_numbers=None) -> web.Response:
    """Annotate a given content using SciGraph annotator and get all entities from content

    

    :param content: The text content to annotate
    :type content: str
    :param include_category: Categories to include for annotation
    :type include_category: List[str]
    :param exclude_category: Categories to exclude for annotation
    :type exclude_category: List[str]
    :param min_length: The minimum number of characters in the annotated entity
    :type min_length: str
    :param longest_only: Should only the longest entity be returned for an overlapping group
    :type longest_only: bool
    :param include_abbreviation: Should abbreviations be included
    :type include_abbreviation: bool
    :param include_acronym: Should acronyms be included
    :type include_acronym: bool
    :param include_numbers: Should numbers be included
    :type include_numbers: bool

    """
    return web.Response(status=200)
