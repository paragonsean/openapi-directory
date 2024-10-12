from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def canvas_data_analytics_summary_0(request: web.Request, canvas_id=None, ending_at=None, starting_at=None, length=None, include_variant_breakdown=None, include_step_breakdown=None, include_deleted_step_data=None) -> web.Response:
    """Canvas Data Analytics Summary

    This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas&#39; results.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;data\&quot;: {     \&quot;name\&quot;: (string) Canvas name,     \&quot;total_stats\&quot;: {       \&quot;revenue\&quot;: (float),       \&quot;conversions\&quot;: (int),       \&quot;conversions_by_entry_time\&quot;: (int),       \&quot;entries\&quot;: (int)     },     \&quot;variant_stats\&quot;: (optional) {       \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for variant) {         \&quot;name\&quot;: (string) name of variant,         \&quot;revenue\&quot;: (float),         \&quot;conversions\&quot;: (int),         \&quot;entries\&quot;: (int)       },       ... (more variants)     },     \&quot;step_stats\&quot;: (optional) {       \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for step) {         \&quot;name\&quot;: (string) name of step,         \&quot;revenue\&quot;: (float),         \&quot;conversions\&quot;: (int),         \&quot;conversions_by_entry_time\&quot;: (int),         \&quot;messages\&quot;: {           \&quot;android_push\&quot;: (name of channel) [             {               \&quot;sent\&quot;: (int),               \&quot;opens\&quot;: (int),               \&quot;influenced_opens\&quot;: (int),               \&quot;bounces\&quot;: (int)               ... (more stats for channel)             }           ],           ... (more channels)         }       },       ... (more steps)     }   },   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

    :param canvas_id: (Required) String   Canvas API identifier
    :type canvas_id: str
    :param ending_at: (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request
    :type ending_at: str
    :param starting_at: (Optional) DateTime (ISO 8601 string)  Date on which the data export should begin (either length or starting_at required)
    :type starting_at: str
    :param length: (Optional) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)
    :type length: str
    :param include_variant_breakdown: (Optional) Boolean  Whether or not to include variant stats (defaults to false)
    :type include_variant_breakdown: str
    :param include_step_breakdown: (Optional) Boolean  Whether or not to include step stats (defaults to false)
    :type include_step_breakdown: str
    :param include_deleted_step_data: (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false)
    :type include_deleted_step_data: str

    """
    return web.Response(status=200)


async def canvas_data_series_analytics_0(request: web.Request, canvas_id=None, ending_at=None, starting_at=None, length=None, include_variant_breakdown=None, include_step_breakdown=None, include_deleted_step_data=None) -> web.Response:
    """Canvas Data Series Analytics

    This endpoint allows you to export time series data for a Canvas.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;data\&quot;: {     \&quot;name\&quot;: (string) Canvas name,     \&quot;stats\&quot;: [       {         \&quot;time\&quot;: (string) date as ISO 8601 date,         \&quot;total_stats\&quot;: {           \&quot;revenue\&quot;: (float),           \&quot;conversions\&quot;: (int),           \&quot;conversions_by_entry_time\&quot;: (int),           \&quot;entries\&quot;: (int)         },         \&quot;variant_stats\&quot;: (optional) {           \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for variant) {             \&quot;name\&quot;: (string) name of variant,             \&quot;revenue\&quot;: (int),             \&quot;conversions\&quot;: (int),             \&quot;conversions_by_entry_time\&quot;: (int),             \&quot;entries\&quot;: (int)           },           ... (more variants)         },         \&quot;step_stats\&quot;: (optional) {           \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for step) {             \&quot;name\&quot;: (string) name of step,             \&quot;revenue\&quot;: (float),             \&quot;conversions\&quot;: (int),             \&quot;conversions_by_entry_time\&quot;: (int),             \&quot;messages\&quot;: {               \&quot;email\&quot;: [                 {                   \&quot;sent\&quot;: (int),                   \&quot;opens\&quot;: (int),                   \&quot;unique_opens\&quot;: (int),                   \&quot;clicks\&quot;: (int),                   ... (more stats)                 }               ],               ... (more channels)             }           },           ... (more steps)         }       },       ... (more stats by time)     ]   },   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

    :param canvas_id: (Required) String  Canvas API Identifier
    :type canvas_id: str
    :param ending_at: (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request
    :type ending_at: str
    :param starting_at: (Optional) DateTime (ISO 8601 string)   Date on which the data export should begin (either length or starting_at are required)
    :type starting_at: str
    :param length: (Optional) DateTime (ISO 8601 string)  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)
    :type length: str
    :param include_variant_breakdown: (Optional) Boolean  Whether or not to include variant stats (defaults to false)
    :type include_variant_breakdown: str
    :param include_step_breakdown: (Optional) Boolean  Whether or not to include step stats (defaults to false)
    :type include_step_breakdown: str
    :param include_deleted_step_data: (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false)
    :type include_deleted_step_data: str

    """
    return web.Response(status=200)


async def canvas_details_0(request: web.Request, canvas_id=None) -> web.Response:
    """Canvas Details

    This endpoint allows you to export metadata about a Canvas, such as its name, when it was created, its current status, and more.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;created_at\&quot;: (string) date created as ISO 8601 date,   \&quot;updated_at\&quot;: (string) date updated as ISO 8601 date,   \&quot;name\&quot;: (string) Canvas name,   \&quot;description\&quot;: (string) Canvas description,   \&quot;archived\&quot;: (boolean) whether this Canvas is archived,   \&quot;draft\&quot;: (boolean) whether this Canvas is a draft,   \&quot;schedule_type\&quot;: (string) type of scheduling action,   \&quot;first_entry\&quot;: (string) date of first entry as ISO 8601 date,   \&quot;last_entry\&quot;: (string) date of last entry as ISO 8601 date,   \&quot;channels\&quot;: (array of strings) step channels used with Canvas,   \&quot;variants\&quot;: [     {       \&quot;name\&quot;: (string) name of variant,       \&quot;id\&quot;: (string) API identifier of the variant,       \&quot;first_step_ids\&quot;: (array of strings) API identifiers for first steps in variant,       \&quot;first_step_id\&quot;: (string) API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)     },     ... (more variations)   ],   \&quot;tags\&quot;: (array of strings) tag names associated with the Canvas,   \&quot;steps\&quot;: [     {       \&quot;name\&quot;: (string) name of step,       \&quot;id\&quot;: (string) API identifier of the step,       \&quot;next_step_ids\&quot;: (array of strings) API identifiers of steps following step,       \&quot;channels\&quot;: (array of strings) channels used in step,       \&quot;messages\&quot;: {           \&quot;message_variation_id\&quot;: (string) {  // &lt;&#x3D;This is the actual id               \&quot;channel\&quot;: (string) channel type of the message (eg., \&quot;email\&quot;),               ... channel-specific fields for this message, see Campaign Details Endpoint API Response for example message responses ...           }       }     },     ... (more steps)   ],   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

    :param canvas_id: (Required) String  Canvas API Identifier 
    :type canvas_id: str

    """
    return web.Response(status=200)


async def canvas_list_0(request: web.Request, page=None, include_archived=None, sort_direction=None, last_edit_time_gt=None) -> web.Response:
    """Canvas List

    This endpoint allows you to export a list of Canvases, including the name, Canvas API Identifier and associated Tags. The Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).  &gt; Archived Canvases will not be included in the API response unless the &#x60;include_archived&#x60; field is specified. Canvases that are stopped but not archived, however, will be returned by default.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;canvases\&quot; : [    {     \&quot;id\&quot; : (string) Canvas API Identifier,     \&quot;last_edited\&quot;: (ISO 8601 string) the last edited time for the message,     \&quot;name\&quot; : (string) Canvas name,     \&quot;tags\&quot; : (array) tag names associated with the Canvas,    },     ... (more Canvases)   ],   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

    :param page: (Optional) Integer  The page of Canvases to return, defaults to &#x60;0&#x60; (returns the first set of up to 100)
    :type page: str
    :param include_archived: (Optional) Boolean  Whether or not to include archived Canvases, defaults to &#x60;false&#x60;.
    :type include_archived: str
    :param sort_direction: (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
    :type sort_direction: str
    :param last_edit_time_gt: (Optional) DateTime (ISO 8601 string)  Filters the results and only returns Canvases that were edited greater than the time provided till now.
    :type last_edit_time_gt: str

    """
    return web.Response(status=200)
