from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def names_changes_get_0(request: web.Request, output_format, from_date, to_date, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search for names with metadata changes in a given period

    Search for information about geographical names which have changed most recently within a specified time window.  Changes may include status cupdates and metadata corrections.

    :param output_format: The format of the output.
    :type output_format: str
    :param from_date: Defines the earliest date (YYYY-MM-DD format) of the change time window for the search
    :type from_date: int
    :param to_date: Defines the latest date (YYYY-MM-DD format) of the change time window for the search
    :type to_date: int
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_decisions_recent_get_0(request: web.Request, output_format, days, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search for names affected by recent naming decision

    Search for information about geographical names affected by naming &#39;decisions&#39; made by the BC Geographical Names Office (naming authority) within the last X days.

    :param output_format: The format of the output.
    :type output_format: str
    :param days: The number of days used to define the time window of naming decisions to search.  The number is interpreted as searching for &#39;names affected by decisions within the last X days&#39;.
    :type days: int
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_decisions_year_get_0(request: web.Request, output_format, year, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search for names affected by naming decisions in a given year

    Search for information about geographical names affected by naming &#39;decisions&#39; made by the BC Geographical Names Office (naming authority) in a given year.

    :param output_format: The format of the output.
    :type output_format: str
    :param year: The year in which to search for names affected by naming decisions&#39;.
    :type year: int
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_inside_get_0(request: web.Request, output_format, bbox, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search in a geographic area

    Search for information about geographical names that correspond to features within a geographic bounding box.  Various options and filter parameters are available to refine the search.

    :param output_format: The format of the output.
    :type output_format: str
    :param bbox: A geographic bounding box defining the search area.  Must be specified as a string of the form &#39;minLongitude,minLatitude,maxLongitude,maxLatitude&#39; (WGS84). e.g. -119,49,-118,50
    :type bbox: str
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_name_id_output_format_get(request: web.Request, name_id, output_format) -> web.Response:
    """Get a name by its nameId

    Get information about the geographical name with the specified nameId.

    :param name_id: The unique identifier for a name
    :type name_id: int
    :param output_format: The format of the output.
    :type output_format: str

    """
    return web.Response(status=200)


async def names_near_get_0(request: web.Request, output_format, feature_point, distance, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search near to a geographic point

    Search for information about geographical names that correspond to features within a geographic area defined by a centre point and a radius.  Various options and filter parameters are available to refine the search.

    :param output_format: The format of the output.
    :type output_format: str
    :param feature_point: A geographic coordinate specifying the centre point of the search area.  Must be specified as a string of the form &#39;longitude,latitude&#39; (WGS84).  e.g. -120,51
    :type feature_point: str
    :param distance: A radius (in kilometres) around the centre point.
    :type distance: str
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_not_official_search_get_0(request: web.Request, output_format, name, exact_spelling=None, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search by name, limit to unofficial names only

    Search for information about unofficial geographical names by the text of the name itself.  Various options and filter parameters are available to refine the search.

    :param output_format: The format of the output.
    :type output_format: str
    :param name: A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39;
    :type name: str
    :param exact_spelling: If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0)
    :type exact_spelling: int
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_official_search_get_0(request: web.Request, output_format, name, exact_spelling=None, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search by name, limit to official names only

    Search for information about official geographical names by the text of the name itself.  Various options and filter parameters are available to refine the search.

    :param output_format: The format of the output.
    :type output_format: str
    :param name: A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39;
    :type name: str
    :param exact_spelling: If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0)
    :type exact_spelling: int
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)


async def names_search_get_0(request: web.Request, output_format, name, exact_spelling=None, feature_class=None, feature_category=None, feature_type=None, sort_by=None, output_srs=None, embed=None, output_style=None, items_per_page=None, start_index=None) -> web.Response:
    """Search by name

    Search for information about geographical names by the text of the name itself.  The response will include both official and unofficial names.  Various options and filter parameters are available to refine the search.

    :param output_format: The format of the output.
    :type output_format: str
    :param name: A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39;
    :type name: str
    :param exact_spelling: If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0)
    :type exact_spelling: int
    :param feature_class: A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    :type feature_class: str
    :param feature_category: A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    :type feature_category: str
    :param feature_type: A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    :type feature_type: str
    :param sort_by: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type sort_by: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries.
    :type output_srs: int
    :param embed: A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name
    :type embed: int
    :param output_style: A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    :type output_style: str
    :param items_per_page: The number of search results to return (1-200)
    :type items_per_page: int
    :param start_index: The index of the first record to be returned (&gt;&#x3D; 1)
    :type start_index: int

    """
    return web.Response(status=200)
