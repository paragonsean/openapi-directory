from typing import List, Dict
from aiohttp import web

from openapi_server.models.contribution import Contribution
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.export import Export
from openapi_server.models.export_summary import ExportSummary
from openapi_server.models.flag import Flag
from openapi_server.models.moderation_history_item_submission import ModerationHistoryItemSubmission
from openapi_server import util


async def contribution_refinement_types_get(request: web.Request, ) -> web.Response:
    """List valid contribution refinement types

    


    """
    return web.Response(status=200)


async def contribution_refinements_get(request: web.Request, assignment=None, country=None, created_before=None, created_after=None, geohash=None, has_location=None, lat_long=None, radius=None, media_type=None, owned_by=None, q=None, url_words=None, user=None, refinements=None, refinement_size=None) -> web.Response:
    """List contribution refinement options

    Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

    :param assignment: Restrict results to contributions submitted to this assignment.
    :type assignment: str
    :param country: Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    :type country: str
    :param created_before: Limit results to contributions created before this date time.
    :type created_before: str
    :param created_after: Limit results to contributions created after this date time.
    :type created_after: str
    :param geohash: Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    :type geohash: str
    :param has_location: Restrict results to contributions which have a publicly visible location.
    :type has_location: bool
    :param lat_long: Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    :type lat_long: str
    :param radius: When limiting result by location with the latLong parameter, specify the radius in kilometers.
    :type radius: float
    :param media_type: Restrict results to contributions which include a media file of the given type (ie. image / video)
    :type media_type: str
    :param owned_by: Restrict results to contributions which are fall under the jurisdiction by this user.
    :type owned_by: str
    :param q: Restrict results to contributions whose headline text matches this keyword.
    :type q: str
    :param url_words: Locate a specific contribution by URL words
    :type url_words: str
    :param user: Restrict results to contributions by this user identified by id.
    :type user: str
    :param refinements: Comma seperated list of refinement names.
    :type refinements: str
    :param refinement_size: Number of refinement options to return.
    :type refinement_size: 

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    return web.Response(status=200)


async def contributions_get(request: web.Request, assignment=None, country=None, created_before=None, created_after=None, created_day=None, created_month=None, geohash=None, has_location=None, lat_long=None, radius=None, media_type=None, owned_by=None, q=None, url_words=None, user=None, ids=None, format=None) -> web.Response:
    """List contributions

    Retrieve contributions.

    :param assignment: Restrict results to contributions submitted to this assignment.
    :type assignment: str
    :param country: Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    :type country: str
    :param created_before: Limit results to contributions created before this date time.
    :type created_before: str
    :param created_after: Limit results to contributions created after this date time.
    :type created_after: str
    :param created_day: Limit results to contributions created on this day.
    :type created_day: str
    :param created_month: Limit results to contributions created during this month.
    :type created_month: str
    :param geohash: Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    :type geohash: str
    :param has_location: Restrict results to contributions which have a publicly visible location.
    :type has_location: bool
    :param lat_long: Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    :type lat_long: str
    :param radius: When limiting result by location with the latLong parameter, specify the radius in kilometers.
    :type radius: float
    :param media_type: Restrict results to contributions which include a media file of the given type (ie. image / video)
    :type media_type: str
    :param owned_by: Restrict results to contributions which are fall under the jurisdiction by this user.
    :type owned_by: str
    :param q: Restrict results to contributions whose headline text matches this keyword.
    :type q: str
    :param url_words: Locate a specific contribution by URL words
    :type url_words: str
    :param user: Restrict results to contributions by this user identified by id.
    :type user: str
    :param ids: Restrict results to a list of specific contributions identified by a comma seperated list of ids.
    :type ids: str
    :param format: Select output format. &#39;json&#39; or &#39;rss&#39;. Defaults to JSON.
    :type format: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    created_day = util.deserialize_date(created_day)
    return web.Response(status=200)


async def contributions_id_delete(request: web.Request, id) -> web.Response:
    """Delete this contribution

    

    :param id: Id of the contribution to delete
    :type id: str

    """
    return web.Response(status=200)


async def contributions_id_flag_post(request: web.Request, id, body) -> web.Response:
    """Raise a flag against this contribution

    Allows end users to bring potential issues with publicly visible content to the attention of moderators.

    :param id: Id of the contribution to flag
    :type id: str
    :param body: Flag to be created
    :type body: dict | bytes

    """
    body = Flag.from_dict(body)
    return web.Response(status=200)


async def contributions_id_get(request: web.Request, id) -> web.Response:
    """Get a single contribution by id

    

    :param id: Id of the contribution to return
    :type id: str

    """
    return web.Response(status=200)


async def contributions_id_like_post(request: web.Request, id) -> web.Response:
    """Allows a user to mark a contribution as liked

    

    :param id: Id of the contribution
    :type id: str

    """
    return web.Response(status=200)


async def contributions_id_likes_get(request: web.Request, id) -> web.Response:
    """List users who have liked this contributions

    Returns a list of user ids of users who have liked this conribution

    :param id: Id of the contribution
    :type id: str

    """
    return web.Response(status=200)


async def contributions_id_moderate_post(request: web.Request, id, body) -> web.Response:
    """Perform a moderation action on this contribution

    Allows the contribution to approved of rejected.

    :param id: Id of the contribution to moderate
    :type id: str
    :param body: A moderation action
    :type body: dict | bytes

    """
    body = ModerationHistoryItemSubmission.from_dict(body)
    return web.Response(status=200)


async def contributions_post(request: web.Request, body) -> web.Response:
    """Create a new contribution

    

    :param body: Contribution object to be created
    :type body: dict | bytes

    """
    body = Contribution.from_dict(body)
    return web.Response(status=200)


async def export_post(request: web.Request, assignment=None, country=None, created_before=None, created_after=None, geohash=None, has_location=None, lat_long=None, radius=None, media_type=None, owned_by=None, q=None, url_words=None, user=None, tagged=None, combined=None, individual=None, format=None, _json=None) -> web.Response:
    """Export contributions.

    Begin an export job. Returns a export job which can be polled to follow the progress of an export.

    :param assignment: Restrict results to contributions submitted to this assignment.
    :type assignment: str
    :param country: Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    :type country: str
    :param created_before: Limit results to contributions created before this date time.
    :type created_before: str
    :param created_after: Limit results to contributions created after this date time.
    :type created_after: str
    :param geohash: Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    :type geohash: str
    :param has_location: Restrict results to contributions which have a publicly visible location.
    :type has_location: bool
    :param lat_long: Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    :type lat_long: str
    :param radius: When limiting result by location with the latLong parameter, specify the radius in kilometers.
    :type radius: float
    :param media_type: Restrict results to contributions which include a media file of the given type (ie. image / video)
    :type media_type: str
    :param owned_by: Restrict results to contributions which are fall under the jurisdiction by this user.
    :type owned_by: str
    :param q: Restrict results to contributions whose headline text matches this keyword.
    :type q: str
    :param url_words: Locate a specific contribution by URL words
    :type url_words: str
    :param user: Restrict results to contributions by this user identified by id.
    :type user: str
    :param tagged: Should exported media files be tagged with metadata. Deprecated; use format instead.
    :type tagged: bool
    :param combined: Included a combined file with all contribution text.
    :type combined: bool
    :param individual: Include individual text files for each contribution.
    :type individual: bool
    :param format: Media format to export; none, fullsize, tagged or original.
    :type format: str
    :param _json: Include raw JSON for each contribution.
    :type _json: bool

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    return web.Response(status=200)


async def export_summary_post(request: web.Request, assignment=None, country=None, created_before=None, created_after=None, geohash=None, has_location=None, lat_long=None, radius=None, media_type=None, owned_by=None, q=None, url_words=None, user=None) -> web.Response:
    """Export contributions preflight summary.

    Provide a preflight summary of an export request.

    :param assignment: Restrict results to contributions submitted to this assignment.
    :type assignment: str
    :param country: Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    :type country: str
    :param created_before: Limit results to contributions created before this date time.
    :type created_before: str
    :param created_after: Limit results to contributions created after this date time.
    :type created_after: str
    :param geohash: Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    :type geohash: str
    :param has_location: Restrict results to contributions which have a publicly visible location.
    :type has_location: bool
    :param lat_long: Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    :type lat_long: str
    :param radius: When limiting result by location with the latLong parameter, specify the radius in kilometers.
    :type radius: float
    :param media_type: Restrict results to contributions which include a media file of the given type (ie. image / video)
    :type media_type: str
    :param owned_by: Restrict results to contributions which are fall under the jurisdiction by this user.
    :type owned_by: str
    :param q: Restrict results to contributions whose headline text matches this keyword.
    :type q: str
    :param url_words: Locate a specific contribution by URL words
    :type url_words: str
    :param user: Restrict results to contributions by this user identified by id.
    :type user: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    return web.Response(status=200)


async def exports_id_get(request: web.Request, id) -> web.Response:
    """Get a single export job; poll to follow export progress.

    

    :param id: Id of the export job to return
    :type id: str

    """
    return web.Response(status=200)
