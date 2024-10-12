from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tags_to_resource_request import AddTagsToResourceRequest
from openapi_server.models.add_tags_to_resource_response import AddTagsToResourceResponse
from openapi_server.models.create_hapg_request import CreateHapgRequest
from openapi_server.models.create_hapg_response import CreateHapgResponse
from openapi_server.models.create_hsm_request import CreateHsmRequest
from openapi_server.models.create_hsm_response import CreateHsmResponse
from openapi_server.models.create_luna_client_request import CreateLunaClientRequest
from openapi_server.models.create_luna_client_response import CreateLunaClientResponse
from openapi_server.models.delete_hapg_request import DeleteHapgRequest
from openapi_server.models.delete_hapg_response import DeleteHapgResponse
from openapi_server.models.delete_hsm_request import DeleteHsmRequest
from openapi_server.models.delete_hsm_response import DeleteHsmResponse
from openapi_server.models.delete_luna_client_request import DeleteLunaClientRequest
from openapi_server.models.delete_luna_client_response import DeleteLunaClientResponse
from openapi_server.models.describe_hapg_request import DescribeHapgRequest
from openapi_server.models.describe_hapg_response import DescribeHapgResponse
from openapi_server.models.describe_hsm_request import DescribeHsmRequest
from openapi_server.models.describe_hsm_response import DescribeHsmResponse
from openapi_server.models.describe_luna_client_request import DescribeLunaClientRequest
from openapi_server.models.describe_luna_client_response import DescribeLunaClientResponse
from openapi_server.models.get_config_request import GetConfigRequest
from openapi_server.models.get_config_response import GetConfigResponse
from openapi_server.models.list_available_zones_response import ListAvailableZonesResponse
from openapi_server.models.list_hapgs_request import ListHapgsRequest
from openapi_server.models.list_hapgs_response import ListHapgsResponse
from openapi_server.models.list_hsms_request import ListHsmsRequest
from openapi_server.models.list_hsms_response import ListHsmsResponse
from openapi_server.models.list_luna_clients_request import ListLunaClientsRequest
from openapi_server.models.list_luna_clients_response import ListLunaClientsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.modify_hapg_request import ModifyHapgRequest
from openapi_server.models.modify_hapg_response import ModifyHapgResponse
from openapi_server.models.modify_hsm_request import ModifyHsmRequest
from openapi_server.models.modify_hsm_response import ModifyHsmResponse
from openapi_server.models.modify_luna_client_request import ModifyLunaClientRequest
from openapi_server.models.modify_luna_client_response import ModifyLunaClientResponse
from openapi_server.models.remove_tags_from_resource_request import RemoveTagsFromResourceRequest
from openapi_server.models.remove_tags_from_resource_response import RemoveTagsFromResourceResponse
from openapi_server import util


async def add_tags_to_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags_to_resource

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Adds or overwrites one or more tags for the specified AWS CloudHSM resource.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and a value. Tag keys must be unique to each resource.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AddTagsToResourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_hapg(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hapg

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateHapgRequest.from_dict(body)
    return web.Response(status=200)


async def create_hsm(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hsm

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates an uninitialized HSM instance.&lt;/p&gt; &lt;p&gt;There is an upfront fee charged for each HSM instance that you create with the &lt;code&gt;CreateHsm&lt;/code&gt; operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the &lt;a&gt;DeleteHsm&lt;/a&gt; operation, go to the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home\&quot;&gt;AWS Support Center&lt;/a&gt;, create a new case, and select &lt;b&gt;Account and Billing Support&lt;/b&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It can take up to 20 minutes to create and provision an HSM. You can monitor the status of the HSM with the &lt;a&gt;DescribeHsm&lt;/a&gt; operation. The HSM is ready to be initialized when the status changes to &lt;code&gt;RUNNING&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateHsmRequest.from_dict(body)
    return web.Response(status=200)


async def create_luna_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_luna_client

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates an HSM client.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateLunaClientRequest.from_dict(body)
    return web.Response(status=200)


async def delete_hapg(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_hapg

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes a high-availability partition group.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteHapgRequest.from_dict(body)
    return web.Response(status=200)


async def delete_hsm(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_hsm

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteHsmRequest.from_dict(body)
    return web.Response(status=200)


async def delete_luna_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_luna_client

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes a client.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteLunaClientRequest.from_dict(body)
    return web.Response(status=200)


async def describe_hapg(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_hapg

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about a high-availability partition group.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeHapgRequest.from_dict(body)
    return web.Response(status=200)


async def describe_hsm(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_hsm

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeHsmRequest.from_dict(body)
    return web.Response(status=200)


async def describe_luna_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_luna_client

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about an HSM client.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeLunaClientRequest.from_dict(body)
    return web.Response(status=200)


async def get_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_config

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetConfigRequest.from_dict(body)
    return web.Response(status=200)


async def list_available_zones(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_available_zones

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists the Availability Zones that have available AWS CloudHSM capacity.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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


async def list_hapgs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_hapgs

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists the high-availability partition groups for the account.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListHapgs&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListHapgsRequest.from_dict(body)
    return web.Response(status=200)


async def list_hsms(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_hsms

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves the identifiers of all of the HSMs provisioned for the current customer.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListHsms&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListHsmsRequest.from_dict(body)
    return web.Response(status=200)


async def list_luna_clients(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_luna_clients

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists all of the clients.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListLunaClients&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListLunaClientsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Returns a list of all tags for the specified AWS CloudHSM resource.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def modify_hapg(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_hapg

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies an existing high-availability partition group.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ModifyHapgRequest.from_dict(body)
    return web.Response(status=200)


async def modify_hsm(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_hsm

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies an HSM.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation can result in the HSM being offline for up to 15 minutes while the AWS CloudHSM service is reconfigured. If you are modifying a production HSM, you should ensure that your AWS CloudHSM service is configured for high availability, and consider executing this operation during a maintenance window.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ModifyHsmRequest.from_dict(body)
    return web.Response(status=200)


async def modify_luna_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_luna_client

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies the certificate used by the client.&lt;/p&gt; &lt;p&gt;This action can potentially start a workflow to install the new certificate on the client&#39;s HSMs.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ModifyLunaClientRequest.from_dict(body)
    return web.Response(status=200)


async def remove_tags_from_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags_from_resource

    &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Removes one or more tags from the specified AWS CloudHSM resource.&lt;/p&gt; &lt;p&gt;To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use &lt;a&gt;AddTagsToResource&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RemoveTagsFromResourceRequest.from_dict(body)
    return web.Response(status=200)
