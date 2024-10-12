from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_stream_target_to_transcoder_output200_response import AddStreamTargetToTranscoderOutput200Response
from openapi_server.models.create_transcoder200_response import CreateTranscoder200Response
from openapi_server.models.create_transcoder_output200_response import CreateTranscoderOutput200Response
from openapi_server.models.create_transcoder_property200_response import CreateTranscoderProperty200Response
from openapi_server.models.disable_all_stream_targets_transcoder200_response import DisableAllStreamTargetsTranscoder200Response
from openapi_server.models.disable_transcoder_output_output_stream_target200_response import DisableTranscoderOutputOutputStreamTarget200Response
from openapi_server.models.enable_transcoder_output_output_stream_target200_response import EnableTranscoderOutputOutputStreamTarget200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.list_transcoder_recordings200_response import ListTranscoderRecordings200Response
from openapi_server.models.list_transcoder_schedules200_response import ListTranscoderSchedules200Response
from openapi_server.models.output_add_stream_target_input import OutputAddStreamTargetInput
from openapi_server.models.output_create_input import OutputCreateInput
from openapi_server.models.output_remove_stream_target_input import OutputRemoveStreamTargetInput
from openapi_server.models.output_stream_target import OutputStreamTarget
from openapi_server.models.output_stream_target_create_input import OutputStreamTargetCreateInput
from openapi_server.models.output_stream_target_update_input import OutputStreamTargetUpdateInput
from openapi_server.models.output_update_input import OutputUpdateInput
from openapi_server.models.outputs import Outputs
from openapi_server.models.reset_transcoder200_response import ResetTranscoder200Response
from openapi_server.models.restart_transcoder_output_output_stream_target200_response import RestartTranscoderOutputOutputStreamTarget200Response
from openapi_server.models.show_transcoder_state200_response import ShowTranscoderState200Response
from openapi_server.models.show_transcoder_stats200_response import ShowTranscoderStats200Response
from openapi_server.models.show_transcoder_thumbnail_url200_response import ShowTranscoderThumbnailUrl200Response
from openapi_server.models.show_uptime_metrics_current200_response import ShowUptimeMetricsCurrent200Response
from openapi_server.models.show_uptime_metrics_historic200_response import ShowUptimeMetricsHistoric200Response
from openapi_server.models.start_transcoder200_response import StartTranscoder200Response
from openapi_server.models.transcoder_create_input import TranscoderCreateInput
from openapi_server.models.transcoder_properties import TranscoderProperties
from openapi_server.models.transcoder_property_create_input import TranscoderPropertyCreateInput
from openapi_server.models.transcoder_update_input import TranscoderUpdateInput
from openapi_server.models.transcoders import Transcoders
from openapi_server.models.uptime import Uptime
from openapi_server.models.uptimes import Uptimes
from openapi_server import util


async def add_stream_target_to_transcoder_output(request: web.Request, transcoder_id, id, output_stream_target) -> web.Response:
    """Deprecated operation

    The operation POST /transcoders/{transcoder_id}/outputs/{id}/add_stream_target is deprecated. Use POST /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets to add an existing stream target to an output.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the output rendition.
    :type id: str
    :param output_stream_target: Provide the details of the stream target to add in the body of the request.
    :type output_stream_target: dict | bytes

    """
    output_stream_target = OutputAddStreamTargetInput.from_dict(output_stream_target)
    return web.Response(status=200)


async def create_transcoder(request: web.Request, transcoder) -> web.Response:
    """Create a transcoder

    This operation creates a transcoder.

    :param transcoder: Provide the details of the transcoder to create in the body of the request.
    :type transcoder: dict | bytes

    """
    transcoder = TranscoderCreateInput.from_dict(transcoder)
    return web.Response(status=200)


async def create_transcoder_output(request: web.Request, transcoder_id, output) -> web.Response:
    """Create an output

    This operation creates an output rendition for a specific transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output: Provide the details of the output rendition to create in the body of the request.
    :type output: dict | bytes

    """
    output = OutputCreateInput.from_dict(output)
    return web.Response(status=200)


async def create_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, output_stream_target) -> web.Response:
    """Create an output stream target

    This operation creates an output stream target. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param output_stream_target: Provide the details of the output stream target to create in the body of the request. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions.
    :type output_stream_target: dict | bytes

    """
    output_stream_target = OutputStreamTargetCreateInput.from_dict(output_stream_target)
    return web.Response(status=200)


async def create_transcoder_property(request: web.Request, transcoder_id, _property) -> web.Response:
    """Create a property for a transcoder

    This operation creates a property for a transcoder. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param _property: Provide the details of the property to create in the body of the request.
    :type _property: dict | bytes

    """
    _property = TranscoderPropertyCreateInput.from_dict(_property)
    return web.Response(status=200)


async def delete_transcoder(request: web.Request, id) -> web.Response:
    """Delete a transcoder

    This operation deletes a transcoder, including all of its assigned output renditions and stream targets.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def delete_transcoder_output(request: web.Request, transcoder_id, id) -> web.Response:
    """Delete an output

    This operation deletes an output, including all of its assigned targets.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the output rendition.
    :type id: str

    """
    return web.Response(status=200)


async def delete_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, stream_target_id) -> web.Response:
    """Delete an output stream target

    This operation deletes an output stream target, including all of its assigned targets.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def delete_transcoder_property(request: web.Request, transcoder_id, id) -> web.Response:
    """Delete a transcoder&#39;s property

    This operation deletes a specific property from a specific transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset.
    :type id: str

    """
    return web.Response(status=200)


async def disable_all_stream_targets_transcoder(request: web.Request, id) -> web.Response:
    """Disable a transcoder&#39;s stream targets

    This operation disables all of the stream targets assigned to a specific transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def disable_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, stream_target_id) -> web.Response:
    """Disable an output stream target

    This operation disables an output stream target.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def enable_all_stream_targets_transcoder(request: web.Request, id) -> web.Response:
    """Enable a transcoder&#39;s stream targets

    This operation enables all of the stream targets assigned to a specific transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def enable_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, stream_target_id) -> web.Response:
    """Enable an output stream target

    This operation enables an output stream target.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def index_uptimes(request: web.Request, transcoder_id, page=None, per_page=None) -> web.Response:
    """Fetch all uptime records for a transcoder

    This operation shows all of the uptime records for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a specific transcoding session.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def list_transcoder_output_output_stream_targets(request: web.Request, transcoder_id, output_id) -> web.Response:
    """Fetch all output stream targets of an output of a transcoder

    This operation shows the details of all of the output stream targets of an output of a transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str

    """
    return web.Response(status=200)


async def list_transcoder_outputs(request: web.Request, transcoder_id) -> web.Response:
    """Fetch all outputs of a transcoder

    This operation shows the details of all of the output renditions of a specific transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str

    """
    return web.Response(status=200)


async def list_transcoder_properties(request: web.Request, transcoder_id) -> web.Response:
    """Fetch a transcoder&#39;s properties

    This operation shows all of the properties of a specific transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str

    """
    return web.Response(status=200)


async def list_transcoder_recordings(request: web.Request, id) -> web.Response:
    """Fetch a transcoder&#39;s recordings

    This operation shows the details of all of the recordings for a specific transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def list_transcoder_schedules(request: web.Request, id) -> web.Response:
    """Fetch transcoder&#39;s schedules

    This operation shows the details of all of the schedules for a specific transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def list_transcoders(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all transcoders

    This operation shows the details of all of your transcoders.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def remove_stream_target_to_transcoder_output(request: web.Request, transcoder_id, id, output_stream_target) -> web.Response:
    """Deprecated operation

    The operation DELETE /transcoders/{transcoder_id}/outputs/{id}/remove_stream_target is deprecated. Use DELETE /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{id} to remove a stream target from an output.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the output rendition.
    :type id: str
    :param output_stream_target: Provide the details of the stream target to remove in the body of the request.
    :type output_stream_target: dict | bytes

    """
    output_stream_target = OutputRemoveStreamTargetInput.from_dict(output_stream_target)
    return web.Response(status=200)


async def reset_transcoder(request: web.Request, id) -> web.Response:
    """Reset a transcoder

    This operation resets a transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def restart_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, stream_target_id) -> web.Response:
    """Restart an output stream target

    This operation restarts an output stream target.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def show_transcoder(request: web.Request, id) -> web.Response:
    """Fetch a transcoder

    This operation shows the details of a specific transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def show_transcoder_output(request: web.Request, transcoder_id, id) -> web.Response:
    """Fetch an output

    This operation shows the details of a specific output rendition for a specific transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the output rendition.
    :type id: str

    """
    return web.Response(status=200)


async def show_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, stream_target_id) -> web.Response:
    """Fetch an output stream target

    This operation shows the details of an output stream target.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def show_transcoder_property(request: web.Request, transcoder_id, id) -> web.Response:
    """Fetch a property for a transcoder

    This operation shows the details of a specific property for a specific transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset.
    :type id: str

    """
    return web.Response(status=200)


async def show_transcoder_state(request: web.Request, id) -> web.Response:
    """Fetch the state and uptime ID of a transcoder

    This operation shows the current state and uptime ID of a transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def show_transcoder_stats(request: web.Request, id) -> web.Response:
    """Fetch statistics for a current transcoder

    This operation responds with a hash of metrics (keys) for a currently running transcoder. Each key has a &lt;strong&gt;status&lt;/strong&gt;, &lt;strong&gt;text&lt;/strong&gt; (description), &lt;strong&gt;units&lt;/strong&gt;, and &lt;strong&gt;value&lt;/strong&gt;.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def show_transcoder_thumbnail_url(request: web.Request, id) -> web.Response:
    """Fetch the thumbnail URL of a transcoder

    This operation shows the thumbnail URL of a started transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def show_uptime(request: web.Request, transcoder_id, id) -> web.Response:
    """Fetch an uptime record

    This operation shows the details of a specific uptime record for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a transcoding session.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the uptime record.
    :type id: str

    """
    return web.Response(status=200)


async def show_uptime_metrics_current(request: web.Request, transcoder_id, id, fields=None) -> web.Response:
    """Fetch current stream health metrics for an active transcoder

    This operation returns a snapshot of the current source connection and processing details of an active (running) transcoder.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the uptime record.
    :type id: str
    :param fields: A comma-separated list of fields to return.
    :type fields: str

    """
    return web.Response(status=200)


async def show_uptime_metrics_historic(request: web.Request, transcoder_id, id, fields=None, _from=None, to=None) -> web.Response:
    """Fetch historic stream health metrics for a transcoder

    This operation shows the historic source connection and processing details for a transcoding session (uptime record). The transcoder can be running or stopped. Metrics are recorded every 20 seconds.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the uptime record.
    :type id: str
    :param fields: A comma-separated list of fields to return.
    :type fields: str
    :param _from: The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC.
    :type _from: str
    :param to: The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC.
    :type to: str

    """
    return web.Response(status=200)


async def start_transcoder(request: web.Request, id) -> web.Response:
    """Start a transcoder

    This operation starts a transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def stop_transcoder(request: web.Request, id) -> web.Response:
    """Stop a transcoder

    This operation stops a transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str

    """
    return web.Response(status=200)


async def update_transcoder(request: web.Request, id, transcoder) -> web.Response:
    """Update a transcoder

    This operation updates a transcoder.

    :param id: The unique alphanumeric string that identifies the transcoder.
    :type id: str
    :param transcoder: Provide the details of the transcoder to update in the body of the request.
    :type transcoder: dict | bytes

    """
    transcoder = TranscoderUpdateInput.from_dict(transcoder)
    return web.Response(status=200)


async def update_transcoder_output(request: web.Request, transcoder_id, id, output) -> web.Response:
    """Update an output

    This operation updates an output rendition.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param id: The unique alphanumeric string that identifies the output rendition.
    :type id: str
    :param output: Provide the details of the output rendition to update in the body of the request.
    :type output: dict | bytes

    """
    output = OutputUpdateInput.from_dict(output)
    return web.Response(status=200)


async def update_transcoder_output_output_stream_target(request: web.Request, transcoder_id, output_id, stream_target_id, output_stream_target) -> web.Response:
    """Update an output stream target

    This operation updates an output stream target.

    :param transcoder_id: The unique alphanumeric string that identifies the transcoder.
    :type transcoder_id: str
    :param output_id: The unique alphanumeric string that identifies the output rendition.
    :type output_id: str
    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param output_stream_target: Provide the details of the output stream target to update in the body of the request.
    :type output_stream_target: dict | bytes

    """
    output_stream_target = OutputStreamTargetUpdateInput.from_dict(output_stream_target)
    return web.Response(status=200)
