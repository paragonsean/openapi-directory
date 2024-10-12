from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_activities import ApplicationActivities
from openapi_server.models.application_activity_contents import ApplicationActivityContents
from openapi_server.models.error import Error
from openapi_server.models.harvest_activities import HarvestActivities
from openapi_server.models.harvest_activity_contents import HarvestActivityContents
from openapi_server.models.planting_activities import PlantingActivities
from openapi_server.models.planting_activity_contents import PlantingActivityContents
from openapi_server.models.scouting_observation import ScoutingObservation
from openapi_server.models.scouting_observation_attachment_contents import ScoutingObservationAttachmentContents
from openapi_server.models.scouting_observation_attachments import ScoutingObservationAttachments
from openapi_server.models.scouting_observations import ScoutingObservations
from openapi_server import util


async def v4_layers_as_applied_activity_id_contents_get(request: web.Request, accept, activity_id, range) -> web.Response:
    """Retrieve the raw application activity

    Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param activity_id: Unique identifier of the Application Activity.
    :type activity_id: str
    :type activity_id: str
    :param range: Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    :type range: str

    """
    return web.Response(status=200)


async def v4_layers_as_applied_get(request: web.Request, accept, x_next_token=None, x_limit=None, resource_owner_id=None, occurred_after=None, occurred_before=None, updated_after=None) -> web.Response:
    """Retrieve a list of application activities

    Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int
    :param resource_owner_id: Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
    :type resource_owner_id: str
    :type resource_owner_id: str
    :param occurred_after: Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_after: str
    :param occurred_before: Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_before: str
    :param updated_after: Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
    :type updated_after: str

    """
    occurred_after = util.deserialize_datetime(occurred_after)
    occurred_before = util.deserialize_datetime(occurred_before)
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def v4_layers_as_harvested_activity_id_contents_get(request: web.Request, accept, activity_id, range) -> web.Response:
    """Retrieve the raw harvest activity

    Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param activity_id: Unique identifier of the Harvest Activity.
    :type activity_id: str
    :type activity_id: str
    :param range: Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    :type range: str

    """
    return web.Response(status=200)


async def v4_layers_as_harvested_get(request: web.Request, accept, x_next_token=None, x_limit=None, resource_owner_id=None, occurred_after=None, occurred_before=None, updated_after=None) -> web.Response:
    """Retrieve a list of harvest activities

    Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int
    :param resource_owner_id: Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
    :type resource_owner_id: str
    :type resource_owner_id: str
    :param occurred_after: Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_after: str
    :param occurred_before: Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_before: str
    :param updated_after: Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
    :type updated_after: str

    """
    occurred_after = util.deserialize_datetime(occurred_after)
    occurred_before = util.deserialize_datetime(occurred_before)
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def v4_layers_as_planted_activity_id_contents_get(request: web.Request, accept, activity_id, range) -> web.Response:
    """Retrieve the raw planting activity

    Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).  The data is compressed using .zip format.

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param activity_id: Unique identifier of the Planting Activity.
    :type activity_id: str
    :type activity_id: str
    :param range: Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    :type range: str

    """
    return web.Response(status=200)


async def v4_layers_as_planted_get(request: web.Request, accept, x_next_token=None, x_limit=None, resource_owner_id=None, occurred_after=None, occurred_before=None, updated_after=None) -> web.Response:
    """Retrieve a list of planting activities

    Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int
    :param resource_owner_id: Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
    :type resource_owner_id: str
    :type resource_owner_id: str
    :param occurred_after: Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_after: str
    :param occurred_before: Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_before: str
    :param updated_after: Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
    :type updated_after: str

    """
    occurred_after = util.deserialize_datetime(occurred_after)
    occurred_before = util.deserialize_datetime(occurred_before)
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def v4_layers_scouting_observations_get(request: web.Request, x_next_token=None, x_limit=None, occurred_after=None, occurred_before=None) -> web.Response:
    """Retrieve a list of scouting observations

    Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.

    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int
    :param occurred_after: Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_after: str
    :param occurred_before: Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore.
    :type occurred_before: str

    """
    occurred_after = util.deserialize_datetime(occurred_after)
    occurred_before = util.deserialize_datetime(occurred_before)
    return web.Response(status=200)


async def v4_layers_scouting_observations_scouting_observation_id_attachments_attachment_id_contents_get(request: web.Request, accept, scouting_observation_id, attachment_id, range) -> web.Response:
    """Retrieve the binary contents of a scouting observation’s attachment.

    Photos added to scouting notes in the FieldView app are capped to &#x60;20MiB&#x60; (&#x60;20971520 bytes&#x60;), and we won’t store photos larger than that in a scouting note. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param scouting_observation_id: Unique identifier of the Scouting Observation.
    :type scouting_observation_id: str
    :type scouting_observation_id: str
    :param attachment_id: Unique identifier of the attachment.
    :type attachment_id: str
    :type attachment_id: str
    :param range: Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    :type range: str

    """
    return web.Response(status=200)


async def v4_layers_scouting_observations_scouting_observation_id_attachments_get(request: web.Request, scouting_observation_id, x_next_token=None, x_limit=None) -> web.Response:
    """Retrieve attachments associated with a given scouting observation.

    Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.

    :param scouting_observation_id: Unique identifier of the Scouting Observation.
    :type scouting_observation_id: str
    :type scouting_observation_id: str
    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int

    """
    return web.Response(status=200)


async def v4_layers_scouting_observations_scouting_observation_id_get(request: web.Request, scouting_observation_id) -> web.Response:
    """Retrieve individual scouting observation

    Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.

    :param scouting_observation_id: Unique identifier of the Scouting Observation.
    :type scouting_observation_id: str
    :type scouting_observation_id: str

    """
    return web.Response(status=200)
