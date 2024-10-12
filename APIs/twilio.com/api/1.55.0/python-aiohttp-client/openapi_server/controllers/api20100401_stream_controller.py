from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_call_stream import ApiV2010AccountCallStream
from openapi_server.models.stream_enum_track import StreamEnumTrack
from openapi_server.models.stream_enum_update_status import StreamEnumUpdateStatus
from openapi_server import util


async def create_stream(request: web.Request, account_sid, call_sid, url, name=None, parameter1_name=None, parameter1_value=None, parameter10_name=None, parameter10_value=None, parameter11_name=None, parameter11_value=None, parameter12_name=None, parameter12_value=None, parameter13_name=None, parameter13_value=None, parameter14_name=None, parameter14_value=None, parameter15_name=None, parameter15_value=None, parameter16_name=None, parameter16_value=None, parameter17_name=None, parameter17_value=None, parameter18_name=None, parameter18_value=None, parameter19_name=None, parameter19_value=None, parameter2_name=None, parameter2_value=None, parameter20_name=None, parameter20_value=None, parameter21_name=None, parameter21_value=None, parameter22_name=None, parameter22_value=None, parameter23_name=None, parameter23_value=None, parameter24_name=None, parameter24_value=None, parameter25_name=None, parameter25_value=None, parameter26_name=None, parameter26_value=None, parameter27_name=None, parameter27_value=None, parameter28_name=None, parameter28_value=None, parameter29_name=None, parameter29_value=None, parameter3_name=None, parameter3_value=None, parameter30_name=None, parameter30_value=None, parameter31_name=None, parameter31_value=None, parameter32_name=None, parameter32_value=None, parameter33_name=None, parameter33_value=None, parameter34_name=None, parameter34_value=None, parameter35_name=None, parameter35_value=None, parameter36_name=None, parameter36_value=None, parameter37_name=None, parameter37_value=None, parameter38_name=None, parameter38_value=None, parameter39_name=None, parameter39_value=None, parameter4_name=None, parameter4_value=None, parameter40_name=None, parameter40_value=None, parameter41_name=None, parameter41_value=None, parameter42_name=None, parameter42_value=None, parameter43_name=None, parameter43_value=None, parameter44_name=None, parameter44_value=None, parameter45_name=None, parameter45_value=None, parameter46_name=None, parameter46_value=None, parameter47_name=None, parameter47_value=None, parameter48_name=None, parameter48_value=None, parameter49_name=None, parameter49_value=None, parameter5_name=None, parameter5_value=None, parameter50_name=None, parameter50_value=None, parameter51_name=None, parameter51_value=None, parameter52_name=None, parameter52_value=None, parameter53_name=None, parameter53_value=None, parameter54_name=None, parameter54_value=None, parameter55_name=None, parameter55_value=None, parameter56_name=None, parameter56_value=None, parameter57_name=None, parameter57_value=None, parameter58_name=None, parameter58_value=None, parameter59_name=None, parameter59_value=None, parameter6_name=None, parameter6_value=None, parameter60_name=None, parameter60_value=None, parameter61_name=None, parameter61_value=None, parameter62_name=None, parameter62_value=None, parameter63_name=None, parameter63_value=None, parameter64_name=None, parameter64_value=None, parameter65_name=None, parameter65_value=None, parameter66_name=None, parameter66_value=None, parameter67_name=None, parameter67_value=None, parameter68_name=None, parameter68_value=None, parameter69_name=None, parameter69_value=None, parameter7_name=None, parameter7_value=None, parameter70_name=None, parameter70_value=None, parameter71_name=None, parameter71_value=None, parameter72_name=None, parameter72_value=None, parameter73_name=None, parameter73_value=None, parameter74_name=None, parameter74_value=None, parameter75_name=None, parameter75_value=None, parameter76_name=None, parameter76_value=None, parameter77_name=None, parameter77_value=None, parameter78_name=None, parameter78_value=None, parameter79_name=None, parameter79_value=None, parameter8_name=None, parameter8_value=None, parameter80_name=None, parameter80_value=None, parameter81_name=None, parameter81_value=None, parameter82_name=None, parameter82_value=None, parameter83_name=None, parameter83_value=None, parameter84_name=None, parameter84_value=None, parameter85_name=None, parameter85_value=None, parameter86_name=None, parameter86_value=None, parameter87_name=None, parameter87_value=None, parameter88_name=None, parameter88_value=None, parameter89_name=None, parameter89_value=None, parameter9_name=None, parameter9_value=None, parameter90_name=None, parameter90_value=None, parameter91_name=None, parameter91_value=None, parameter92_name=None, parameter92_value=None, parameter93_name=None, parameter93_value=None, parameter94_name=None, parameter94_value=None, parameter95_name=None, parameter95_value=None, parameter96_name=None, parameter96_value=None, parameter97_name=None, parameter97_value=None, parameter98_name=None, parameter98_value=None, parameter99_name=None, parameter99_value=None, status_callback=None, status_callback_method=None, track=None) -> web.Response:
    """create_stream

    Create a Stream

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Stream resource.
    :type account_sid: str
    :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Stream resource is associated with.
    :type call_sid: str
    :param url: Relative or absolute url where WebSocket connection will be established.
    :type url: str
    :param name: The user-specified name of this Stream, if one was given when the Stream was created. This may be used to stop the Stream.
    :type name: str
    :param parameter1_name: Parameter name
    :type parameter1_name: str
    :param parameter1_value: Parameter value
    :type parameter1_value: str
    :param parameter10_name: Parameter name
    :type parameter10_name: str
    :param parameter10_value: Parameter value
    :type parameter10_value: str
    :param parameter11_name: Parameter name
    :type parameter11_name: str
    :param parameter11_value: Parameter value
    :type parameter11_value: str
    :param parameter12_name: Parameter name
    :type parameter12_name: str
    :param parameter12_value: Parameter value
    :type parameter12_value: str
    :param parameter13_name: Parameter name
    :type parameter13_name: str
    :param parameter13_value: Parameter value
    :type parameter13_value: str
    :param parameter14_name: Parameter name
    :type parameter14_name: str
    :param parameter14_value: Parameter value
    :type parameter14_value: str
    :param parameter15_name: Parameter name
    :type parameter15_name: str
    :param parameter15_value: Parameter value
    :type parameter15_value: str
    :param parameter16_name: Parameter name
    :type parameter16_name: str
    :param parameter16_value: Parameter value
    :type parameter16_value: str
    :param parameter17_name: Parameter name
    :type parameter17_name: str
    :param parameter17_value: Parameter value
    :type parameter17_value: str
    :param parameter18_name: Parameter name
    :type parameter18_name: str
    :param parameter18_value: Parameter value
    :type parameter18_value: str
    :param parameter19_name: Parameter name
    :type parameter19_name: str
    :param parameter19_value: Parameter value
    :type parameter19_value: str
    :param parameter2_name: Parameter name
    :type parameter2_name: str
    :param parameter2_value: Parameter value
    :type parameter2_value: str
    :param parameter20_name: Parameter name
    :type parameter20_name: str
    :param parameter20_value: Parameter value
    :type parameter20_value: str
    :param parameter21_name: Parameter name
    :type parameter21_name: str
    :param parameter21_value: Parameter value
    :type parameter21_value: str
    :param parameter22_name: Parameter name
    :type parameter22_name: str
    :param parameter22_value: Parameter value
    :type parameter22_value: str
    :param parameter23_name: Parameter name
    :type parameter23_name: str
    :param parameter23_value: Parameter value
    :type parameter23_value: str
    :param parameter24_name: Parameter name
    :type parameter24_name: str
    :param parameter24_value: Parameter value
    :type parameter24_value: str
    :param parameter25_name: Parameter name
    :type parameter25_name: str
    :param parameter25_value: Parameter value
    :type parameter25_value: str
    :param parameter26_name: Parameter name
    :type parameter26_name: str
    :param parameter26_value: Parameter value
    :type parameter26_value: str
    :param parameter27_name: Parameter name
    :type parameter27_name: str
    :param parameter27_value: Parameter value
    :type parameter27_value: str
    :param parameter28_name: Parameter name
    :type parameter28_name: str
    :param parameter28_value: Parameter value
    :type parameter28_value: str
    :param parameter29_name: Parameter name
    :type parameter29_name: str
    :param parameter29_value: Parameter value
    :type parameter29_value: str
    :param parameter3_name: Parameter name
    :type parameter3_name: str
    :param parameter3_value: Parameter value
    :type parameter3_value: str
    :param parameter30_name: Parameter name
    :type parameter30_name: str
    :param parameter30_value: Parameter value
    :type parameter30_value: str
    :param parameter31_name: Parameter name
    :type parameter31_name: str
    :param parameter31_value: Parameter value
    :type parameter31_value: str
    :param parameter32_name: Parameter name
    :type parameter32_name: str
    :param parameter32_value: Parameter value
    :type parameter32_value: str
    :param parameter33_name: Parameter name
    :type parameter33_name: str
    :param parameter33_value: Parameter value
    :type parameter33_value: str
    :param parameter34_name: Parameter name
    :type parameter34_name: str
    :param parameter34_value: Parameter value
    :type parameter34_value: str
    :param parameter35_name: Parameter name
    :type parameter35_name: str
    :param parameter35_value: Parameter value
    :type parameter35_value: str
    :param parameter36_name: Parameter name
    :type parameter36_name: str
    :param parameter36_value: Parameter value
    :type parameter36_value: str
    :param parameter37_name: Parameter name
    :type parameter37_name: str
    :param parameter37_value: Parameter value
    :type parameter37_value: str
    :param parameter38_name: Parameter name
    :type parameter38_name: str
    :param parameter38_value: Parameter value
    :type parameter38_value: str
    :param parameter39_name: Parameter name
    :type parameter39_name: str
    :param parameter39_value: Parameter value
    :type parameter39_value: str
    :param parameter4_name: Parameter name
    :type parameter4_name: str
    :param parameter4_value: Parameter value
    :type parameter4_value: str
    :param parameter40_name: Parameter name
    :type parameter40_name: str
    :param parameter40_value: Parameter value
    :type parameter40_value: str
    :param parameter41_name: Parameter name
    :type parameter41_name: str
    :param parameter41_value: Parameter value
    :type parameter41_value: str
    :param parameter42_name: Parameter name
    :type parameter42_name: str
    :param parameter42_value: Parameter value
    :type parameter42_value: str
    :param parameter43_name: Parameter name
    :type parameter43_name: str
    :param parameter43_value: Parameter value
    :type parameter43_value: str
    :param parameter44_name: Parameter name
    :type parameter44_name: str
    :param parameter44_value: Parameter value
    :type parameter44_value: str
    :param parameter45_name: Parameter name
    :type parameter45_name: str
    :param parameter45_value: Parameter value
    :type parameter45_value: str
    :param parameter46_name: Parameter name
    :type parameter46_name: str
    :param parameter46_value: Parameter value
    :type parameter46_value: str
    :param parameter47_name: Parameter name
    :type parameter47_name: str
    :param parameter47_value: Parameter value
    :type parameter47_value: str
    :param parameter48_name: Parameter name
    :type parameter48_name: str
    :param parameter48_value: Parameter value
    :type parameter48_value: str
    :param parameter49_name: Parameter name
    :type parameter49_name: str
    :param parameter49_value: Parameter value
    :type parameter49_value: str
    :param parameter5_name: Parameter name
    :type parameter5_name: str
    :param parameter5_value: Parameter value
    :type parameter5_value: str
    :param parameter50_name: Parameter name
    :type parameter50_name: str
    :param parameter50_value: Parameter value
    :type parameter50_value: str
    :param parameter51_name: Parameter name
    :type parameter51_name: str
    :param parameter51_value: Parameter value
    :type parameter51_value: str
    :param parameter52_name: Parameter name
    :type parameter52_name: str
    :param parameter52_value: Parameter value
    :type parameter52_value: str
    :param parameter53_name: Parameter name
    :type parameter53_name: str
    :param parameter53_value: Parameter value
    :type parameter53_value: str
    :param parameter54_name: Parameter name
    :type parameter54_name: str
    :param parameter54_value: Parameter value
    :type parameter54_value: str
    :param parameter55_name: Parameter name
    :type parameter55_name: str
    :param parameter55_value: Parameter value
    :type parameter55_value: str
    :param parameter56_name: Parameter name
    :type parameter56_name: str
    :param parameter56_value: Parameter value
    :type parameter56_value: str
    :param parameter57_name: Parameter name
    :type parameter57_name: str
    :param parameter57_value: Parameter value
    :type parameter57_value: str
    :param parameter58_name: Parameter name
    :type parameter58_name: str
    :param parameter58_value: Parameter value
    :type parameter58_value: str
    :param parameter59_name: Parameter name
    :type parameter59_name: str
    :param parameter59_value: Parameter value
    :type parameter59_value: str
    :param parameter6_name: Parameter name
    :type parameter6_name: str
    :param parameter6_value: Parameter value
    :type parameter6_value: str
    :param parameter60_name: Parameter name
    :type parameter60_name: str
    :param parameter60_value: Parameter value
    :type parameter60_value: str
    :param parameter61_name: Parameter name
    :type parameter61_name: str
    :param parameter61_value: Parameter value
    :type parameter61_value: str
    :param parameter62_name: Parameter name
    :type parameter62_name: str
    :param parameter62_value: Parameter value
    :type parameter62_value: str
    :param parameter63_name: Parameter name
    :type parameter63_name: str
    :param parameter63_value: Parameter value
    :type parameter63_value: str
    :param parameter64_name: Parameter name
    :type parameter64_name: str
    :param parameter64_value: Parameter value
    :type parameter64_value: str
    :param parameter65_name: Parameter name
    :type parameter65_name: str
    :param parameter65_value: Parameter value
    :type parameter65_value: str
    :param parameter66_name: Parameter name
    :type parameter66_name: str
    :param parameter66_value: Parameter value
    :type parameter66_value: str
    :param parameter67_name: Parameter name
    :type parameter67_name: str
    :param parameter67_value: Parameter value
    :type parameter67_value: str
    :param parameter68_name: Parameter name
    :type parameter68_name: str
    :param parameter68_value: Parameter value
    :type parameter68_value: str
    :param parameter69_name: Parameter name
    :type parameter69_name: str
    :param parameter69_value: Parameter value
    :type parameter69_value: str
    :param parameter7_name: Parameter name
    :type parameter7_name: str
    :param parameter7_value: Parameter value
    :type parameter7_value: str
    :param parameter70_name: Parameter name
    :type parameter70_name: str
    :param parameter70_value: Parameter value
    :type parameter70_value: str
    :param parameter71_name: Parameter name
    :type parameter71_name: str
    :param parameter71_value: Parameter value
    :type parameter71_value: str
    :param parameter72_name: Parameter name
    :type parameter72_name: str
    :param parameter72_value: Parameter value
    :type parameter72_value: str
    :param parameter73_name: Parameter name
    :type parameter73_name: str
    :param parameter73_value: Parameter value
    :type parameter73_value: str
    :param parameter74_name: Parameter name
    :type parameter74_name: str
    :param parameter74_value: Parameter value
    :type parameter74_value: str
    :param parameter75_name: Parameter name
    :type parameter75_name: str
    :param parameter75_value: Parameter value
    :type parameter75_value: str
    :param parameter76_name: Parameter name
    :type parameter76_name: str
    :param parameter76_value: Parameter value
    :type parameter76_value: str
    :param parameter77_name: Parameter name
    :type parameter77_name: str
    :param parameter77_value: Parameter value
    :type parameter77_value: str
    :param parameter78_name: Parameter name
    :type parameter78_name: str
    :param parameter78_value: Parameter value
    :type parameter78_value: str
    :param parameter79_name: Parameter name
    :type parameter79_name: str
    :param parameter79_value: Parameter value
    :type parameter79_value: str
    :param parameter8_name: Parameter name
    :type parameter8_name: str
    :param parameter8_value: Parameter value
    :type parameter8_value: str
    :param parameter80_name: Parameter name
    :type parameter80_name: str
    :param parameter80_value: Parameter value
    :type parameter80_value: str
    :param parameter81_name: Parameter name
    :type parameter81_name: str
    :param parameter81_value: Parameter value
    :type parameter81_value: str
    :param parameter82_name: Parameter name
    :type parameter82_name: str
    :param parameter82_value: Parameter value
    :type parameter82_value: str
    :param parameter83_name: Parameter name
    :type parameter83_name: str
    :param parameter83_value: Parameter value
    :type parameter83_value: str
    :param parameter84_name: Parameter name
    :type parameter84_name: str
    :param parameter84_value: Parameter value
    :type parameter84_value: str
    :param parameter85_name: Parameter name
    :type parameter85_name: str
    :param parameter85_value: Parameter value
    :type parameter85_value: str
    :param parameter86_name: Parameter name
    :type parameter86_name: str
    :param parameter86_value: Parameter value
    :type parameter86_value: str
    :param parameter87_name: Parameter name
    :type parameter87_name: str
    :param parameter87_value: Parameter value
    :type parameter87_value: str
    :param parameter88_name: Parameter name
    :type parameter88_name: str
    :param parameter88_value: Parameter value
    :type parameter88_value: str
    :param parameter89_name: Parameter name
    :type parameter89_name: str
    :param parameter89_value: Parameter value
    :type parameter89_value: str
    :param parameter9_name: Parameter name
    :type parameter9_name: str
    :param parameter9_value: Parameter value
    :type parameter9_value: str
    :param parameter90_name: Parameter name
    :type parameter90_name: str
    :param parameter90_value: Parameter value
    :type parameter90_value: str
    :param parameter91_name: Parameter name
    :type parameter91_name: str
    :param parameter91_value: Parameter value
    :type parameter91_value: str
    :param parameter92_name: Parameter name
    :type parameter92_name: str
    :param parameter92_value: Parameter value
    :type parameter92_value: str
    :param parameter93_name: Parameter name
    :type parameter93_name: str
    :param parameter93_value: Parameter value
    :type parameter93_value: str
    :param parameter94_name: Parameter name
    :type parameter94_name: str
    :param parameter94_value: Parameter value
    :type parameter94_value: str
    :param parameter95_name: Parameter name
    :type parameter95_name: str
    :param parameter95_value: Parameter value
    :type parameter95_value: str
    :param parameter96_name: Parameter name
    :type parameter96_name: str
    :param parameter96_value: Parameter value
    :type parameter96_value: str
    :param parameter97_name: Parameter name
    :type parameter97_name: str
    :param parameter97_value: Parameter value
    :type parameter97_value: str
    :param parameter98_name: Parameter name
    :type parameter98_name: str
    :param parameter98_value: Parameter value
    :type parameter98_value: str
    :param parameter99_name: Parameter name
    :type parameter99_name: str
    :param parameter99_value: Parameter value
    :type parameter99_value: str
    :param status_callback: Absolute URL of the status callback.
    :type status_callback: str
    :param status_callback_method: The http method for the status_callback (one of GET, POST).
    :type status_callback_method: str
    :param track: 
    :type track: str

    """
    return web.Response(status=200)


async def update_stream(request: web.Request, account_sid, call_sid, sid, status) -> web.Response:
    """update_stream

    Stop a Stream using either the SID of the Stream resource or the &#x60;name&#x60; used when creating the resource

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Stream resource.
    :type account_sid: str
    :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Stream resource is associated with.
    :type call_sid: str
    :param sid: The SID of the Stream resource, or the &#x60;name&#x60; used when creating the resource
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
