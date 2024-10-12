from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_snapshot_request import CreateSnapshotRequest
from openapi_server.models.describe_app_output import DescribeAppOutput
from openapi_server.models.describe_simulation_output import DescribeSimulationOutput
from openapi_server.models.list_apps_output import ListAppsOutput
from openapi_server.models.list_simulations_output import ListSimulationsOutput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.start_app_output import StartAppOutput
from openapi_server.models.start_app_request import StartAppRequest
from openapi_server.models.start_clock_request import StartClockRequest
from openapi_server.models.start_simulation_output import StartSimulationOutput
from openapi_server.models.start_simulation_request import StartSimulationRequest
from openapi_server.models.stop_app_request import StopAppRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server import util


async def create_snapshot(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_snapshot

    &lt;p&gt;Creates a snapshot of the specified simulation. A snapshot is a file that contains simulation state data at a specific time. The state data saved in a snapshot includes entity data from the State Fabric, the simulation configuration specified in the schema, and the clock tick number. You can use the snapshot to initialize a new simulation. For more information about snapshots, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html\&quot;&gt;Snapshots&lt;/a&gt; in the &lt;i&gt;SimSpace Weaver User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;You specify a &lt;code&gt;Destination&lt;/code&gt; when you create a snapshot. The &lt;code&gt;Destination&lt;/code&gt; is the name of an Amazon S3 bucket and an optional &lt;code&gt;ObjectKeyPrefix&lt;/code&gt;. The &lt;code&gt;ObjectKeyPrefix&lt;/code&gt; is usually the name of a folder in the bucket. SimSpace Weaver creates a &lt;code&gt;snapshot&lt;/code&gt; folder inside the &lt;code&gt;Destination&lt;/code&gt; and places the snapshot file there.&lt;/p&gt; &lt;p&gt;The snapshot file is an Amazon S3 object. It has an object key with the form: &lt;code&gt; &lt;i&gt;object-key-prefix&lt;/i&gt;/snapshot/&lt;i&gt;simulation-name&lt;/i&gt;-&lt;i&gt;YYMMdd&lt;/i&gt;-&lt;i&gt;HHmm&lt;/i&gt;-&lt;i&gt;ss&lt;/i&gt;.zip&lt;/code&gt;, where: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;YY&lt;/i&gt; &lt;/code&gt; is the 2-digit year&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;MM&lt;/i&gt; &lt;/code&gt; is the 2-digit month&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;dd&lt;/i&gt; &lt;/code&gt; is the 2-digit day of the month&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;HH&lt;/i&gt; &lt;/code&gt; is the 2-digit hour (24-hour clock)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;mm&lt;/i&gt; &lt;/code&gt; is the 2-digit minutes&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;ss&lt;/i&gt; &lt;/code&gt; is the 2-digit seconds&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app(request: web.Request, app, domain, simulation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app

    Deletes the instance of the given custom app.

    :param app: The name of the app.
    :type app: str
    :param domain: The name of the domain of the app.
    :type domain: str
    :param simulation: The name of the simulation of the app.
    :type simulation: str
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


async def delete_simulation(request: web.Request, simulation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_simulation

    &lt;p&gt;Deletes all SimSpace Weaver resources assigned to the given simulation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Your simulation uses resources in other Amazon Web Services. This API operation doesn&#39;t delete resources in other Amazon Web Services.&lt;/p&gt; &lt;/note&gt;

    :param simulation: The name of the simulation.
    :type simulation: str
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


async def describe_app(request: web.Request, app, domain, simulation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app

    Returns the state of the given custom app.

    :param app: The name of the app.
    :type app: str
    :param domain: The name of the domain of the app.
    :type domain: str
    :param simulation: The name of the simulation of the app.
    :type simulation: str
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


async def describe_simulation(request: web.Request, simulation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_simulation

    Returns the current state of the given simulation.

    :param simulation: The name of the simulation.
    :type simulation: str
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


async def list_apps(request: web.Request, simulation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_apps

    Lists all custom apps or service apps for the given simulation and domain.

    :param simulation: The name of the simulation that you want to list apps for.
    :type simulation: str
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
    :param domain: The name of the domain that you want to list apps for.
    :type domain: str
    :param max_results: The maximum number of apps to list.
    :type max_results: int
    :param next_token: If SimSpace Weaver returns &lt;code&gt;nextToken&lt;/code&gt;, then there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then &lt;code&gt;nextToken&lt;/code&gt; is set to &lt;code&gt;null&lt;/code&gt;. Each pagination token expires after 24 hours. If you provide a token that isn&#39;t valid, then you receive an &lt;i&gt;HTTP 400 ValidationException&lt;/i&gt; error.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_simulations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_simulations

    Lists the SimSpace Weaver simulations in the Amazon Web Services account used to make the API call.

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
    :param max_results: The maximum number of simulations to list.
    :type max_results: int
    :param next_token: If SimSpace Weaver returns &lt;code&gt;nextToken&lt;/code&gt;, then there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then &lt;code&gt;nextToken&lt;/code&gt; is set to &lt;code&gt;null&lt;/code&gt;. Each pagination token expires after 24 hours. If you provide a token that isn&#39;t valid, then you receive an &lt;i&gt;HTTP 400 ValidationException&lt;/i&gt; error.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists all tags on a SimSpace Weaver resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.
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


async def start_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_app

    Starts a custom app with the configuration specified in the simulation schema.

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
    body = StartAppRequest.from_dict(body)
    return web.Response(status=200)


async def start_clock(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_clock

    Starts the simulation clock.

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
    body = StartClockRequest.from_dict(body)
    return web.Response(status=200)


async def start_simulation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_simulation

    Starts a simulation with the given name. You must choose to start your simulation from a schema or from a snapshot. For more information about the schema, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference.html\&quot;&gt;schema reference&lt;/a&gt; in the &lt;i&gt;SimSpace Weaver User Guide&lt;/i&gt;. For more information about snapshots, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html\&quot;&gt;Snapshots&lt;/a&gt; in the &lt;i&gt;SimSpace Weaver User Guide&lt;/i&gt;.

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
    body = StartSimulationRequest.from_dict(body)
    return web.Response(status=200)


async def stop_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_app

    Stops the given custom app and shuts down all of its allocated compute resources.

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
    body = StopAppRequest.from_dict(body)
    return web.Response(status=200)


async def stop_clock(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_clock

    Stops the simulation clock.

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
    body = StartClockRequest.from_dict(body)
    return web.Response(status=200)


async def stop_simulation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_simulation

    &lt;p&gt;Stops the given simulation.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can&#39;t restart a simulation after you stop it. If you want to restart a simulation, then you must stop it, delete it, and start a new instance of it.&lt;/p&gt; &lt;/important&gt;

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
    body = StartClockRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds tags to a SimSpace Weaver resource. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to add tags to. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.
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

    Removes tags from a SimSpace Weaver resource. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to remove tags from. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.
    :type resource_arn: str
    :param tag_keys: A list of tag keys to remove from the resource.
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
