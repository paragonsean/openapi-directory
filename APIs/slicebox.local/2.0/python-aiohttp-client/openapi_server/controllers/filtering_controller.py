from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter import Filter
from openapi_server.models.source_tag_filter import SourceTagFilter
from openapi_server.models.tag_path_tag import TagPathTag
from openapi_server import util


async def filtering_associations_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """filtering_associations_get

    Get a list of source to filter associations.

    :param startindex: start index of returned slice of source &lt;-&gt; filter associations
    :type startindex: int
    :param count: size of returned slice of source &lt;-&gt; filter associations
    :type count: int

    """
    return web.Response(status=200)


async def filtering_associations_id_delete(request: web.Request, id) -> web.Response:
    """filtering_associations_id_delete

    remove the source &lt;-&gt; filter association corresponding to the supplied ID

    :param id: id of source &lt;-&gt; filter association to remove
    :type id: int

    """
    return web.Response(status=200)


async def filtering_associations_post(request: web.Request, sourcetagfilter) -> web.Response:
    """filtering_associations_post

    Inserts or updates a source &lt;-&gt; filter associations. If the specified Source already  has an association this is updated, otherwise a new is inserted.

    :param sourcetagfilter: Source to Filter association
    :type sourcetagfilter: dict | bytes

    """
    sourcetagfilter = SourceTagFilter.from_dict(sourcetagfilter)
    return web.Response(status=200)


async def filtering_filters_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """filtering_filters_get

    List defined filters

    :param startindex: start index of returned slice of filters
    :type startindex: int
    :param count: size of returned slice of filters
    :type count: int

    """
    return web.Response(status=200)


async def filtering_filters_id_delete(request: web.Request, id) -> web.Response:
    """filtering_filters_id_delete

    remove the filter corresponding to the supplied ID

    :param id: id of filter to remove
    :type id: int

    """
    return web.Response(status=200)


async def filtering_filters_id_tagpaths_get(request: web.Request, id) -> web.Response:
    """filtering_filters_id_tagpaths_get

    List tagpaths for the selected filter

    :param id: id of filter
    :type id: int

    """
    return web.Response(status=200)


async def filtering_filters_id_tagpaths_post(request: web.Request, id, tagpath) -> web.Response:
    """filtering_filters_id_tagpaths_post

    add a tagpath to a filter

    :param id: id of filter to remove
    :type id: int
    :param tagpath: id of filter to remove
    :type tagpath: dict | bytes

    """
    tagpath = TagPathTag.from_dict(tagpath)
    return web.Response(status=200)


async def filtering_filters_id_tagpaths_tagpathid_delete(request: web.Request, id, tagpathid) -> web.Response:
    """filtering_filters_id_tagpaths_tagpathid_delete

    remove the tagpath corresponding to the supplied ID

    :param id: id of filter
    :type id: int
    :param tagpathid: id of TagPath to remove
    :type tagpathid: int

    """
    return web.Response(status=200)


async def filtering_filters_post(request: web.Request, tag_filter) -> web.Response:
    """filtering_filters_post

    Inserts or updates a filter. If a filter with same name as supplied filter exists this filter is updated, otherwise a new filter is inserted.

    :param tag_filter: Filter
    :type tag_filter: dict | bytes

    """
    tag_filter = Filter.from_dict(tag_filter)
    return web.Response(status=200)
