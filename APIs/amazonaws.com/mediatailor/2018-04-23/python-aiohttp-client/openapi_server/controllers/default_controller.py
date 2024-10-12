from typing import List, Dict
from aiohttp import web

from openapi_server.models.configure_logs_for_channel_request import ConfigureLogsForChannelRequest
from openapi_server.models.configure_logs_for_channel_response import ConfigureLogsForChannelResponse
from openapi_server.models.configure_logs_for_playback_configuration_request import ConfigureLogsForPlaybackConfigurationRequest
from openapi_server.models.configure_logs_for_playback_configuration_response import ConfigureLogsForPlaybackConfigurationResponse
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.create_channel_response import CreateChannelResponse
from openapi_server.models.create_live_source_request import CreateLiveSourceRequest
from openapi_server.models.create_live_source_response import CreateLiveSourceResponse
from openapi_server.models.create_prefetch_schedule_request import CreatePrefetchScheduleRequest
from openapi_server.models.create_prefetch_schedule_response import CreatePrefetchScheduleResponse
from openapi_server.models.create_program_request import CreateProgramRequest
from openapi_server.models.create_program_response import CreateProgramResponse
from openapi_server.models.create_source_location_request import CreateSourceLocationRequest
from openapi_server.models.create_source_location_response import CreateSourceLocationResponse
from openapi_server.models.create_vod_source_request import CreateVodSourceRequest
from openapi_server.models.create_vod_source_response import CreateVodSourceResponse
from openapi_server.models.describe_channel_response import DescribeChannelResponse
from openapi_server.models.describe_live_source_response import DescribeLiveSourceResponse
from openapi_server.models.describe_program_response import DescribeProgramResponse
from openapi_server.models.describe_source_location_response import DescribeSourceLocationResponse
from openapi_server.models.describe_vod_source_response import DescribeVodSourceResponse
from openapi_server.models.get_channel_policy_response import GetChannelPolicyResponse
from openapi_server.models.get_channel_schedule_response import GetChannelScheduleResponse
from openapi_server.models.get_playback_configuration_response import GetPlaybackConfigurationResponse
from openapi_server.models.get_prefetch_schedule_response import GetPrefetchScheduleResponse
from openapi_server.models.list_alerts_response import ListAlertsResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_live_sources_response import ListLiveSourcesResponse
from openapi_server.models.list_playback_configurations_response import ListPlaybackConfigurationsResponse
from openapi_server.models.list_prefetch_schedules_request import ListPrefetchSchedulesRequest
from openapi_server.models.list_prefetch_schedules_response import ListPrefetchSchedulesResponse
from openapi_server.models.list_source_locations_response import ListSourceLocationsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_vod_sources_response import ListVodSourcesResponse
from openapi_server.models.put_channel_policy_request import PutChannelPolicyRequest
from openapi_server.models.put_playback_configuration_request import PutPlaybackConfigurationRequest
from openapi_server.models.put_playback_configuration_response import PutPlaybackConfigurationResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse
from openapi_server.models.update_live_source_request import UpdateLiveSourceRequest
from openapi_server.models.update_live_source_response import UpdateLiveSourceResponse
from openapi_server.models.update_program_request import UpdateProgramRequest
from openapi_server.models.update_program_response import UpdateProgramResponse
from openapi_server.models.update_source_location_request import UpdateSourceLocationRequest
from openapi_server.models.update_source_location_response import UpdateSourceLocationResponse
from openapi_server.models.update_vod_source_response import UpdateVodSourceResponse
from openapi_server import util


async def configure_logs_for_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """configure_logs_for_channel

    Configures Amazon CloudWatch log settings for a channel.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ConfigureLogsForChannelRequest.from_dict(body)
    return web.Response(status=200)


async def configure_logs_for_playback_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """configure_logs_for_playback_configuration

    Amazon CloudWatch log settings for a playback configuration.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ConfigureLogsForPlaybackConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel(request: web.Request, channel_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel

    Creates a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def create_live_source(request: web.Request, live_source_name, source_location_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_live_source

    The live source configuration.

    :param live_source_name: The name of the live source.
    :type live_source_name: str
    :param source_location_name: The name of the source location.
    :type source_location_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateLiveSourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_prefetch_schedule(request: web.Request, name, playback_configuration_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_prefetch_schedule

    Creates a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\&quot;&gt;Using ad prefetching&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param name: The name to assign to the schedule request.
    :type name: str
    :param playback_configuration_name: The name to assign to the playback configuration.
    :type playback_configuration_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePrefetchScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def create_program(request: web.Request, channel_name, program_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_program

    Creates a program within a channel. For information about programs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html\&quot;&gt;Working with programs&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel for this Program.
    :type channel_name: str
    :param program_name: The name of the Program.
    :type program_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateProgramRequest.from_dict(body)
    return web.Response(status=200)


async def create_source_location(request: web.Request, source_location_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_source_location

    Creates a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param source_location_name: The name associated with the source location.
    :type source_location_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSourceLocationRequest.from_dict(body)
    return web.Response(status=200)


async def create_vod_source(request: web.Request, source_location_name, vod_source_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vod_source

    The VOD source configuration parameters.

    :param source_location_name: The name of the source location for this VOD source.
    :type source_location_name: str
    :param vod_source_name: The name associated with the VOD source.&amp;gt;
    :type vod_source_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateVodSourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel

    Deletes a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_channel_policy(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel_policy

    The channel policy to delete.

    :param channel_name: The name of the channel associated with this channel policy.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_live_source(request: web.Request, live_source_name, source_location_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_live_source

    The live source to delete.

    :param live_source_name: The name of the live source.
    :type live_source_name: str
    :param source_location_name: The name of the source location associated with this Live Source.
    :type source_location_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_playback_configuration(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_playback_configuration

    Deletes a playback configuration. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with configurations in AWS Elemental MediaTailor&lt;/a&gt;.

    :param name: The name of the playback configuration.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_prefetch_schedule(request: web.Request, name, playback_configuration_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_prefetch_schedule

    Deletes a prefetch schedule for a specific playback configuration. If you call &lt;code&gt;DeletePrefetchSchedule&lt;/code&gt; on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. For more information about ad prefetching, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\&quot;&gt;Using ad prefetching&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param name: The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.
    :type name: str
    :param playback_configuration_name: The name of the playback configuration for this prefetch schedule.
    :type playback_configuration_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_program(request: web.Request, channel_name, program_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_program

    Deletes a program within a channel. For information about programs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html\&quot;&gt;Working with programs&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param program_name: The name of the program.
    :type program_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_source_location(request: web.Request, source_location_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_source_location

    Deletes a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param source_location_name: The name of the source location.
    :type source_location_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_vod_source(request: web.Request, source_location_name, vod_source_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vod_source

    The video on demand (VOD) source to delete.

    :param source_location_name: The name of the source location associated with this VOD Source.
    :type source_location_name: str
    :param vod_source_name: The name of the VOD source.
    :type vod_source_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_channel(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel

    Describes a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_live_source(request: web.Request, live_source_name, source_location_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_live_source

    The live source to describe.

    :param live_source_name: The name of the live source.
    :type live_source_name: str
    :param source_location_name: The name of the source location associated with this Live Source.
    :type source_location_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_program(request: web.Request, channel_name, program_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_program

    Describes a program within a channel. For information about programs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html\&quot;&gt;Working with programs&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel associated with this Program.
    :type channel_name: str
    :param program_name: The name of the program.
    :type program_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_source_location(request: web.Request, source_location_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_source_location

    Describes a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param source_location_name: The name of the source location.
    :type source_location_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_vod_source(request: web.Request, source_location_name, vod_source_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_vod_source

    Provides details about a specific video on demand (VOD) source in a specific source location.

    :param source_location_name: The name of the source location associated with this VOD Source.
    :type source_location_name: str
    :param vod_source_name: The name of the VOD Source.
    :type vod_source_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_channel_policy(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channel_policy

    Returns the channel&#39;s IAM policy. IAM policies are used to control access to your channel.

    :param channel_name: The name of the channel associated with this Channel Policy.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_channel_schedule(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, duration_minutes=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """get_channel_schedule

    Retrieves information about your channel&#39;s schedule.

    :param channel_name: The name of the channel associated with this Channel Schedule.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param duration_minutes: The duration in minutes of the channel schedule.
    :type duration_minutes: str
    :param max_results: The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; channel schedules, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: &lt;p&gt;(Optional) If the playback configuration has more than &lt;code&gt;MaxResults&lt;/code&gt; channel schedules, use &lt;code&gt;NextToken&lt;/code&gt; to get the second and subsequent pages of results.&lt;/p&gt; &lt;p&gt;For the first &lt;code&gt;GetChannelScheduleRequest&lt;/code&gt; request, omit this value.&lt;/p&gt; &lt;p&gt;For the second and subsequent requests, get the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response and specify that value for &lt;code&gt;NextToken&lt;/code&gt; in the request.&lt;/p&gt; &lt;p&gt;If the previous response didn&#39;t include a &lt;code&gt;NextToken&lt;/code&gt; element, there are no more channel schedules to get.&lt;/p&gt;
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def get_playback_configuration(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_playback_configuration

    Retrieves a playback configuration. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with configurations in AWS Elemental MediaTailor&lt;/a&gt;.

    :param name: The identifier for the playback configuration.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_prefetch_schedule(request: web.Request, name, playback_configuration_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_prefetch_schedule

    Retrieves a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\&quot;&gt;Using ad prefetching&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param name: The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.
    :type name: str
    :param playback_configuration_name: Returns information about the prefetch schedule for a specific playback configuration. If you call &lt;code&gt;GetPrefetchSchedule&lt;/code&gt; on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.
    :type playback_configuration_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_alerts(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_alerts

    Lists the alerts that are associated with a MediaTailor channel assembly resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of alerts that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; alerts, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels

    Retrieves information about the channels that are associated with the current AWS account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; channels, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_live_sources(request: web.Request, source_location_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_live_sources

    Lists the live sources contained in a source location. A source represents a piece of content.

    :param source_location_name: The name of the source location associated with this Live Sources list.
    :type source_location_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; live sources, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_playback_configurations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_playback_configurations

    Retrieves existing playback configurations. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with Configurations in AWS Elemental MediaTailor&lt;/a&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of playback configurations that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; playback configurations, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_prefetch_schedules(request: web.Request, playback_configuration_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_prefetch_schedules

    Lists the prefetch schedules for a playback configuration.

    :param playback_configuration_name: Retrieves the prefetch schedule(s) for a specific playback configuration.
    :type playback_configuration_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPrefetchSchedulesRequest.from_dict(body)
    return web.Response(status=200)


async def list_source_locations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_source_locations

    Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results:  The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; source locations, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    A list of tags that are associated with this resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\&quot;&gt;Tagging AWS Elemental MediaTailor Resources&lt;/a&gt;.

    :param resource_arn: The Amazon Resource Name (ARN) associated with this resource.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_vod_sources(request: web.Request, source_location_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_vod_sources

    Lists the VOD sources contained in a source location. A source represents a piece of content.

    :param source_location_name: The name of the source location associated with this VOD Source list.
    :type source_location_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results:  The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; VOD sources, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results.
    :type max_results: int
    :param next_token: Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def put_channel_policy(request: web.Request, channel_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_channel_policy

    Creates an IAM policy for the channel. IAM policies are used to control access to your channel.

    :param channel_name: The channel name associated with this Channel Policy.
    :type channel_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutChannelPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_playback_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_playback_configuration

    Creates a playback configuration. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with configurations in AWS Elemental MediaTailor&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutPlaybackConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def start_channel(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_channel

    Starts a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def stop_channel(request: web.Request, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_channel

    Stops a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    The resource to tag. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\&quot;&gt;Tagging AWS Elemental MediaTailor Resources&lt;/a&gt;.

    :param resource_arn: The Amazon Resource Name (ARN) associated with the resource.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    The resource to untag.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to untag.
    :type resource_arn: str
    :param tag_keys: The tag keys associated with the resource.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_channel(request: web.Request, channel_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel

    Updates a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param channel_name: The name of the channel.
    :type channel_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_live_source(request: web.Request, live_source_name, source_location_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_live_source

    Updates a live source&#39;s configuration.

    :param live_source_name: The name of the live source.
    :type live_source_name: str
    :param source_location_name: The name of the source location associated with this Live Source.
    :type source_location_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateLiveSourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_program(request: web.Request, channel_name, program_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_program

    Updates a program within a channel.

    :param channel_name: The name of the channel for this Program.
    :type channel_name: str
    :param program_name: The name of the Program.
    :type program_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProgramRequest.from_dict(body)
    return web.Response(status=200)


async def update_source_location(request: web.Request, source_location_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_source_location

    Updates a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

    :param source_location_name: The name of the source location.
    :type source_location_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSourceLocationRequest.from_dict(body)
    return web.Response(status=200)


async def update_vod_source(request: web.Request, source_location_name, vod_source_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_vod_source

    Updates a VOD source&#39;s configuration.

    :param source_location_name: The name of the source location associated with this VOD Source.
    :type source_location_name: str
    :param vod_source_name: The name of the VOD source.
    :type vod_source_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateLiveSourceRequest.from_dict(body)
    return web.Response(status=200)
