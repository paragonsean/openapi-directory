from typing import List, Dict
from aiohttp import web

from openapi_server.models.chaos_parameters import ChaosParameters
from openapi_server.models.chaos_report import ChaosReport
from openapi_server.models.fabric_error import FabricError
from openapi_server import util


async def get_chaos_report(request: web.Request, api_version, continuation_token=None, start_time_utc=None, end_time_utc=None, timeout=None) -> web.Response:
    """Gets the next segment of the Chaos report based on the passed-in continuation token or the passed-in time-range.

    You can either specify the ContinuationToken to get the next segment of the Chaos report or you can specify the time-range through StartTimeUtc and EndTimeUtc, but you cannot specify both the ContinuationToken and the time-range in the same call. When there are more than 100 Chaos events, the Chaos report is returned in segments where a segment contains no more than 100 Chaos events. 

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param start_time_utc: The Windows file time representing the start time of the time range for which a Chaos report is to be generated. Please consult [DateTime.ToFileTimeUtc Method](https://msdn.microsoft.com/en-us/library/system.datetime.tofiletimeutc(v&#x3D;vs.110).aspx) for details.
    :type start_time_utc: str
    :param end_time_utc: The Windows file time representing the end time of the time range for which a Chaos report is to be generated. Please consult [DateTime.ToFileTimeUtc Method](https://msdn.microsoft.com/en-us/library/system.datetime.tofiletimeutc(v&#x3D;vs.110).aspx) for details.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_chaos(request: web.Request, api_version, chaos_parameters, timeout=None) -> web.Response:
    """Starts Chaos in the cluster.

    If Chaos is not already running in the cluster, it starts Chaos with the passed in Chaos parameters. If Chaos is already running when this call is made, the call fails with the error code FABRIC_E_CHAOS_ALREADY_RUNNING. Please refer to the article [Induce controlled Chaos in Service Fabric clusters](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-controlled-chaos) for more details. 

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param chaos_parameters: Describes all the parameters to configure a Chaos run.
    :type chaos_parameters: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    chaos_parameters = ChaosParameters.from_dict(chaos_parameters)
    return web.Response(status=200)


async def stop_chaos(request: web.Request, api_version, timeout=None) -> web.Response:
    """Stops Chaos in the cluster if it is already running, otherwise it does nothing.

    Stops Chaos from scheduling further faults; but, the in-flight faults are not affected.

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)
