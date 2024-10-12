from typing import List, Dict
from aiohttp import web

from openapi_server.models.record import Record
from openapi_server.models.records_format_get200_response import RecordsFormatGet200Response
from openapi_server.models.records_record_id_more_like_this_format_get200_response import RecordsRecordIdMoreLikeThisFormatGet200Response
from openapi_server import util


async def records_format_get(request: web.Request, format, authentication_token=None, text=None, and_category=None, and_content_partner=None, and_primary_collection=None, and_collection=None, and_usage=None, and_subject=None, and_dc_type=None, and_format=None, and_placename=None, and_creator=None, and_title=None, and_date=None, and_year=None, and_decade=None, and_century=None, without_filter_field=None, and_or_filter_field=None, and_is_commercial_use=None, and_has_large_thumbnail_url=None, and_has_lat_lng=None, geo_bbox=None, fields=None, sort=None, direction=None, page=None, per_page=None, facets=None, facets_page=None, facets_per_page=None, exclude_filters_from_facets=None) -> web.Response:
    """Run queries against DigitalNZ metadata search service.

    This is the main search endpoint allowing queries against the records database.

    :param format: Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \&quot;content_partner\&quot;, whereas XML uses a hyphenated naming convention, eg. \&quot;content-partner\&quot;. 
    :type format: str
    :param authentication_token: The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \&quot;[my API key](https://digitalnz.org/api_keys/edit)\&quot; from your username drop-down menu (on the right hand side)&#39;. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you&#39;ll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  &#x60;curl -H \&quot;Authentication-Token:{YOUR_API_KEY}\&quot; http://api.digitalnz.org/v3/records.json?text&#x3D;kiwi&#x60; 
    :type authentication_token: str
    :param text: This field enables queries based on one or more search terms and provides the functionality of the main search box on [digitalnz.org](https://digitalnz.org). Search terms can be combined with boolean operators (AND, OR).   A minus sign excludes certain terms, eg. \&quot;-horse\&quot;.   An asterisk (\\*) acts as a wildcard, eg. \&quot;ted*\&quot;.   Multiple search terms are combined with an AND by default.   Examples: &#x60;\&quot;moustache\&quot;&#x60;, &#x60;\&quot;Wanganui OR Whanganui\&quot;&#x60;,  &#x60;\&quot;-paperspast\&quot;&#x60;, &#x60;\&quot;ted*\&quot;&#x60; 
    :type text: str
    :param and_category: These are the same categories that are used across the tabs in [digitalnz.org](https://digitalnz.org/records?text&#x3D;&amp;tab&#x3D;Videos)
    :type and_category: str
    :param and_content_partner: Allows filtering for records from a particular Content Partner.   Examples: &#x60;\&quot;Ministry for Culture and Heritage\&quot;&#x60; &#x60;\&quot;Trove\&quot;&#x60; &#x60;\&quot;V.C. Browne &amp; Son\&quot;&#x60;    *Tip* - To see a list of Content Partners available for filtering use the *facets* parameter, eg. *\&quot;&amp;facets&#x3D;content_partner\&quot;*.   
    :type and_content_partner: str
    :param and_primary_collection: Allows filtering for records from a particular *primary_collection*.   Examples: &#x60;\&quot;Puke Ariki\&quot;&#x60; &#x60;\&quot;NZHistory\&quot;&#x60; &#x60;\&quot;TAPUHI\&quot;&#x60;      *Tip* - To see a list of Primary_Collections available for filtering use the *facets* parameter, eg. *\&quot;&amp;facets&#x3D;primary_collection\&quot;*.    
    :type and_primary_collection: str
    :param and_collection: Allows filtering for records from a particular Collection. Collections can be thought of as sub-collections or groupings under Primary_Collections.   Examples: &#x60;\&quot;Music 101\&quot;&#x60; &#x60;\&quot;Mollusks\&quot;&#x60; &#x60;\&quot;Wairarapa Daily Times\&quot;&#x60;    *Tip* - To see a list of Collections available for filtering use the *facets* parameter, eg. *\&quot;&amp;facets&#x3D;collection\&quot;*.  
    :type and_collection: str
    :param and_usage: 
    :type and_usage: str
    :param and_subject: Examples: &#x60;\&quot;Cats\&quot;&#x60; &#x60;\&quot;Weddings\&quot;&#x60; &#x60;\&quot;climb*\&quot;&#x60; 
    :type and_subject: str
    :param and_dc_type: Examples: &#x60;\&quot;Conference item\&quot;&#x60; &#x60;\&quot;Magazines\&quot;&#x60; 
    :type and_dc_type: str
    :param and_format: Examples: &#x60;\&quot;Photolithographs\&quot;&#x60; &#x60;\&quot;Glass*\&quot;&#x60; 
    :type and_format: str
    :param and_placename: This field can be used for text-based location search. For a more advanced coordinate-based search, see the \&quot;geo_bbox\&quot; field below.   Examples: &#x60;\&quot;Scott Base\&quot;&#x60; &#x60;\&quot;Wainuiomata\&quot;&#x60; &#x60;\&quot;castle*\&quot;&#x60; 
    :type and_placename: str
    :param and_creator: Examples: &#x60;\&quot;Revelle Jackson\&quot;&#x60; &#x60;\&quot;Nicholas Chevalier\&quot;&#x60; &#x60;\&quot;Rita Angus\&quot;&#x60; 
    :type and_creator: str
    :param and_title: Examples: &#x60;\&quot;Pukeko\&quot;&#x60; &#x60;\&quot;Club\&quot;&#x60; &#x60;\&quot;Break*\&quot;&#x60;\&quot; 
    :type and_title: str
    :param and_date: This field can be useful for querying and sorting (see the &#39;sort&#39; param further down). But it should be noted that, as with some other fields, **not all records have date metadata associated**. There is good coverage of date metadata within certain collections, but there are plenty with no date information at all. So, if you query for records from a specific date you may get some matching results, but might also be missing other potentially relevant records that don&#39;t have date metadata available.   Example: &#x60;\&quot;1970-12-25\&quot;&#x60;  *Tip* - There is a related (but not searchable) field that is returned on each record (where available), that often has a more human readable version of the date information, called &#39;display_date&#39;. 
    :type and_date: str
    :param and_year: This field allows searching specifically by year. The metadata is derived from the same date information that is searchable and returned in the date field. It is possible to search across a range using syntax the following syntax &#x60;[{start year} TO {end year}]&#x60;.   Example: &#x60;\&quot;1893\&quot;&#x60; &#x60;\&quot;[1982 TO 1987]\&quot;&#x60; 
    :type and_year: str
    :param and_decade: This field allows searching specifically by decade. The metadata is derived from the same date information that is searchable and returned in the date field.   Example: &#x60;\&quot;1850\&quot;&#x60; &#x60;\&quot;1990\&quot;&#x60; 
    :type and_decade: str
    :param and_century: This field allows searching specifically by century. The metadata is derived from the same date information that is searchable and returned in the date field.   Example: &#x60;\&quot;1900\&quot;&#x60; &#x60;\&quot;2000\&quot;&#x60; 
    :type and_century: str
    :param without_filter_field: All of the above &#x60;and[___][]&#x60; filters in this document are also able to be used with this syntax to exclude specific matches. For example to exclude Papers Past content &#x60;&amp;without[primary_collection]&#x3D;Papers+Past&#x60; 
    :type without_filter_field: str
    :param and_or_filter_field: All of the above &#x60;and[___][]&#x60; filters in this document are also able to be used with the &#x60;and[or][___][]&#x60; syntax to allow multi-select *OR* queries within one field.   Basic example:  - To filter your results to only those with a category or Audio or Videos:    &#x60;&amp;and[or][category][]&#x3D;Audio&amp;and[or][category][]&#x3D;Videos&#x60;     In order to combine *OR* filters across multiple fields the syntax needs to be nested as follows   Nested examples:   - To search for *(year is 2014 OR 2015) AND (primary_collection is TAPUHI OR Public Address)*    &#x60;&amp;and[or][year][]&#x3D;2015&amp;and[or][year][]&#x3D;2014&amp;and[and][or][primary_collection][]&#x3D;TAPUHI&amp;and[and][or][primary_collection][]&#x3D;Public+Address&#x60;    - To search for *(category is Images OR Video) AND (subject is cat OR cats)*    &#x60;&amp;and[or][category][]&#x3D;Images&amp;and[or][category][]&#x3D;Videos&amp;and[and][or][subject][]&#x3D;cat&amp;and[and][or][subject][]&#x3D;cats&#x60;   
    :type and_or_filter_field: str
    :param and_is_commercial_use: Some DigitalNZ partners offer their metadata for use in commercial applications. This content can be identified through the *is_commercial_use* flag. Only API results where the *is_commercial_use* field set to True can be used for commercial purposes. Check out the [terms of use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use#commercial_use_terms) for more information. 
    :type and_is_commercial_use: bool
    :param and_has_large_thumbnail_url: Filters results to only those records that have an image available in the *large_thumbnail_url* field.   **Note:** There is an issue with this field where, in order to get results, it needs to be specified with \&quot;Y\&quot; or not specified at all. 
    :type and_has_large_thumbnail_url: str
    :param and_has_lat_lng: Filters results to only those records that have latitude and longitude coordinates present in the metadata.    *Tip* - To see the location metadata you&#39;ll need to specifically request that field using the *fields* parameter - *\&quot;&amp;fields&#x3D;verbose,locations\&quot;*  as it is not part of the default, or verbose field sets. 
    :type and_has_lat_lng: bool
    :param geo_bbox: A geographic bounding box scoping a search to a geographic region. Order of latitude-longitude coordinates is north, west, south, east.   For example, filtering the Wellington region would be *\&quot;&amp;geo_bbox&#x3D;-41,174,-42,175\&quot;* 
    :type geo_bbox: str
    :param fields: Comma-separated whitelist of fields to be returned. The syntax *\&quot;&amp;fields&#x3D;verbose\&quot;* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\&quot;&amp;fields&#x3D;id,title,subject,collection,landing_url,locations\&quot;*. 
    :type fields: str
    :param sort: Used to control the order of the results in conjunction with the *direction* field.   - *syndication_date* - is the creation date of the record within DigitalNZ, ie. when DigitalNZ first harvested the record.   - *date* - is the date metadata (if present) associated with the record.        To sort the search results with newest records at the top use: \&quot;&amp;sort&#x3D;syndication_date&amp;direction&#x3D;desc\&quot; 
    :type sort: str
    :param direction: Used in conjunction with *sort* to order the results  - *asc* - Ascending, oldest first.  - *desc* - Descending, newest first. 
    :type direction: str
    :param page: Specify which page of results to return.
    :type page: int
    :param per_page: The number of records to return per page of search results.
    :type per_page: int
    :param facets: Shows a breakdown of record counts for the specified facets based on the current result set. In the [DigitalNZ search interface](https://digitalnz.org/records) these facets are used to list the values filterable for each field. A comma-separated list will return multiple facets in one call. 
    :type facets: List[str]
    :param facets_page: This value specifies which page of facet results to return. Allowing pagination through large lists of facet values.
    :type facets_page: int
    :param facets_per_page: The number of facets to return per page of facet results.
    :type facets_per_page: int
    :param exclude_filters_from_facets: This field can be used when filtering into some facets, to maintain the context of the wider facet values. A common use case is to allow the results of a search to be filtered down into a specific category (eg Audio), while still showing the other possible filter options as facet counts (eg. Images, Audio, Video, etc). Setting this to &#39;true&#39; will not effect the search results returned but will ignore all search filters (eg. \&quot;and[category]&#x3D;Audio\&quot;) when calculating the facet counts.  
    :type exclude_filters_from_facets: bool

    """
    return web.Response(status=200)


async def records_record_id_format_get(request: web.Request, record_id, format, authentication_token=None, fields=None) -> web.Response:
    """View metadata associated with a single record.

    If you know its &#x60;record_id&#x60; you can use this endpoint to view all metadata associated with that specific record. 

    :param record_id: Every record has a unique, persistent *record_id*.
    :type record_id: int
    :param format: Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \&quot;content_partner\&quot;, whereas XML uses a hyphenated naming convention, eg. \&quot;content-partner\&quot;. 
    :type format: str
    :param authentication_token: The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \&quot;[my API key](https://digitalnz.org/api_keys/edit)\&quot; from your username drop-down menu (on the right hand side)&#39;. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you&#39;ll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  &#x60;curl -H \&quot;Authentication-Token:{YOUR_API_KEY}\&quot; http://api.digitalnz.org/v3/records.json?text&#x3D;kiwi&#x60; 
    :type authentication_token: str
    :param fields: Comma-separated whitelist of fields to be returned. The syntax *\&quot;&amp;fields&#x3D;verbose\&quot;* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\&quot;&amp;fields&#x3D;id,title,subject,collection,landing_url,locations\&quot;*. 
    :type fields: str

    """
    return web.Response(status=200)


async def records_record_id_more_like_this_format_get(request: web.Request, record_id, format, authentication_token=None, fields=None, mlt_fields=None, filtering=None) -> web.Response:
    """The \&quot;More Like This\&quot; call returns similar records to the specified ID. 

    This feature returns a set of search results that are similar (ie have similar metadata) to a specific record. 

    :param record_id: Every record has a unique, persistent *record_id*.
    :type record_id: int
    :param format: Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \&quot;content_partner\&quot;, whereas XML uses a hyphenated naming convention, eg. \&quot;content-partner\&quot;. 
    :type format: str
    :param authentication_token: The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \&quot;[my API key](https://digitalnz.org/api_keys/edit)\&quot; from your username drop-down menu (on the right hand side)&#39;. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you&#39;ll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  &#x60;curl -H \&quot;Authentication-Token:{YOUR_API_KEY}\&quot; http://api.digitalnz.org/v3/records.json?text&#x3D;kiwi&#x60; 
    :type authentication_token: str
    :param fields: Comma-separated whitelist of fields to be returned. The syntax *\&quot;&amp;fields&#x3D;verbose\&quot;* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\&quot;&amp;fields&#x3D;id,title,subject,collection,landing_url,locations\&quot;*. 
    :type fields: str
    :param mlt_fields: Comma-separated list of fields used to evaluate relatedness. Available fields to compare are *title* and *subject*, eg *&amp;mlt_fields&#x3D;title,subject* or *&amp;mlt_fields&#x3D;title*. 
    :type mlt_fields: str
    :param filtering: More Like This (MLT) queries can be filtered in the same ways as regular searches, using the same syntax outined in the GET /records call above. This enables things like scoping the related records to only return Images eg *&amp;and[category]&#x3D;Images*, or to only show related records from a specific content partner eg *&amp;and[content_partner]&#x3D;Puke+Ariki*. 
    :type filtering: str

    """
    return web.Response(status=200)
