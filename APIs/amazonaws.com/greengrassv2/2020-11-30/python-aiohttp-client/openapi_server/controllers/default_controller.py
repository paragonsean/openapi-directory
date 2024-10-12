from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_service_role_to_account_request import AssociateServiceRoleToAccountRequest
from openapi_server.models.associate_service_role_to_account_response import AssociateServiceRoleToAccountResponse
from openapi_server.models.batch_associate_client_device_with_core_device_request import BatchAssociateClientDeviceWithCoreDeviceRequest
from openapi_server.models.batch_associate_client_device_with_core_device_response import BatchAssociateClientDeviceWithCoreDeviceResponse
from openapi_server.models.batch_disassociate_client_device_from_core_device_request import BatchDisassociateClientDeviceFromCoreDeviceRequest
from openapi_server.models.batch_disassociate_client_device_from_core_device_response import BatchDisassociateClientDeviceFromCoreDeviceResponse
from openapi_server.models.cancel_deployment_response import CancelDeploymentResponse
from openapi_server.models.create_component_version_request import CreateComponentVersionRequest
from openapi_server.models.create_component_version_response import CreateComponentVersionResponse
from openapi_server.models.create_deployment_request import CreateDeploymentRequest
from openapi_server.models.create_deployment_response import CreateDeploymentResponse
from openapi_server.models.describe_component_response import DescribeComponentResponse
from openapi_server.models.disassociate_service_role_from_account_response import DisassociateServiceRoleFromAccountResponse
from openapi_server.models.get_component_response import GetComponentResponse
from openapi_server.models.get_component_version_artifact_response import GetComponentVersionArtifactResponse
from openapi_server.models.get_connectivity_info_response import GetConnectivityInfoResponse
from openapi_server.models.get_core_device_response import GetCoreDeviceResponse
from openapi_server.models.get_deployment_response import GetDeploymentResponse
from openapi_server.models.get_service_role_for_account_response import GetServiceRoleForAccountResponse
from openapi_server.models.list_client_devices_associated_with_core_device_response import ListClientDevicesAssociatedWithCoreDeviceResponse
from openapi_server.models.list_component_versions_response import ListComponentVersionsResponse
from openapi_server.models.list_components_response import ListComponentsResponse
from openapi_server.models.list_core_devices_response import ListCoreDevicesResponse
from openapi_server.models.list_deployments_response import ListDeploymentsResponse
from openapi_server.models.list_effective_deployments_response import ListEffectiveDeploymentsResponse
from openapi_server.models.list_installed_components_response import ListInstalledComponentsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.resolve_component_candidates_request import ResolveComponentCandidatesRequest
from openapi_server.models.resolve_component_candidates_response import ResolveComponentCandidatesResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_connectivity_info_request import UpdateConnectivityInfoRequest
from openapi_server.models.update_connectivity_info_response import UpdateConnectivityInfoResponse
from openapi_server import util


async def associate_service_role_to_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_service_role_to_account

    Associates a Greengrass service role with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. The role must include the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/iam/home#/policies/arn:awsiam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy\&quot;&gt;AWSGreengrassResourceAccessRolePolicy&lt;/a&gt; managed policy or a custom policy that defines equivalent permissions for the IoT Greengrass features that you use. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html\&quot;&gt;Greengrass service role&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.

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
    body = AssociateServiceRoleToAccountRequest.from_dict(body)
    return web.Response(status=200)


async def batch_associate_client_device_with_core_device(request: web.Request, core_device_thing_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_associate_client_device_with_core_device

    &lt;p&gt;Associates a list of client devices with a core device. Use this API operation to specify which client devices can discover a core device through cloud discovery. With cloud discovery, client devices connect to IoT Greengrass to retrieve associated core devices&#39; connectivity information and certificates. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-cloud-discovery.html\&quot;&gt;Configure cloud discovery&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Client devices are local IoT devices that connect to and communicate with an IoT Greengrass core device over MQTT. You can connect client devices to a core device to sync MQTT messages and data to Amazon Web Services IoT Core and interact with client devices in Greengrass components. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html\&quot;&gt;Interact with local IoT devices&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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
    body = BatchAssociateClientDeviceWithCoreDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def batch_disassociate_client_device_from_core_device(request: web.Request, core_device_thing_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_disassociate_client_device_from_core_device

    Disassociates a list of client devices from a core device. After you disassociate a client device from a core device, the client device won&#39;t be able to use cloud discovery to retrieve the core device&#39;s connectivity information and certificates.

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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
    body = BatchDisassociateClientDeviceFromCoreDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_deployment(request: web.Request, deployment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_deployment

    Cancels a deployment. This operation cancels the deployment for devices that haven&#39;t yet received it. If a device already received the deployment, this operation doesn&#39;t change anything for that device.

    :param deployment_id: The ID of the deployment.
    :type deployment_id: str
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


async def create_component_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_component_version

    &lt;p&gt;Creates a component. Components are software that run on Greengrass core devices. After you develop and test a component on your core device, you can use this operation to upload your component to IoT Greengrass. Then, you can deploy the component to other core devices.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Create components from recipes&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Create a component from a recipe, which is a file that defines the component&#39;s metadata, parameters, dependencies, lifecycle, artifacts, and platform capability. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html\&quot;&gt;IoT Greengrass component recipe reference&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To create a component from a recipe, specify &lt;code&gt;inlineRecipe&lt;/code&gt; when you call this operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Create components from Lambda functions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Create a component from an Lambda function that runs on IoT Greengrass. This creates a recipe and artifacts from the Lambda function&#39;s deployment package. You can use this operation to migrate Lambda functions from IoT Greengrass V1 to IoT Greengrass V2.&lt;/p&gt; &lt;p&gt;This function only accepts Lambda functions that use the following runtimes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Python 2.7 – &lt;code&gt;python2.7&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Python 3.7 – &lt;code&gt;python3.7&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Python 3.8 – &lt;code&gt;python3.8&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Python 3.9 – &lt;code&gt;python3.9&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Java 8 – &lt;code&gt;java8&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Java 11 – &lt;code&gt;java11&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Node.js 10 – &lt;code&gt;nodejs10.x&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Node.js 12 – &lt;code&gt;nodejs12.x&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Node.js 14 – &lt;code&gt;nodejs14.x&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To create a component from a Lambda function, specify &lt;code&gt;lambdaFunction&lt;/code&gt; when you call this operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass currently supports Lambda functions on only Linux core devices.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateComponentVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_deployment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_deployment

    &lt;p&gt;Creates a continuous deployment for a target, which is a Greengrass core device or group of core devices. When you add a new core device to a group of core devices that has a deployment, IoT Greengrass deploys that group&#39;s deployment to the new device.&lt;/p&gt; &lt;p&gt;You can define one deployment for each target. When you create a new deployment for a target that has an existing deployment, you replace the previous deployment. IoT Greengrass applies the new deployment to the target devices.&lt;/p&gt; &lt;p&gt;Every deployment has a revision number that indicates how many deployment revisions you define for a target. Use this operation to create a new revision of an existing deployment.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html\&quot;&gt;Create deployments&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateDeploymentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_component(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_component

    &lt;p&gt;Deletes a version of a component from IoT Greengrass.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the component&#39;s recipe and artifacts. As a result, deployments that refer to this component version will fail. If you have deployments that use this component version, you can remove the component from the deployment or update the deployment to use a valid version.&lt;/p&gt; &lt;/note&gt;

    :param arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version.
    :type arn: str
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


async def delete_core_device(request: web.Request, core_device_thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_core_device

    Deletes a Greengrass core device, which is an IoT thing. This operation removes the core device from the list of core devices. This operation doesn&#39;t delete the IoT thing. For more information about how to delete the IoT thing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html\&quot;&gt;DeleteThing&lt;/a&gt; in the &lt;i&gt;IoT API Reference&lt;/i&gt;.

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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


async def delete_deployment(request: web.Request, deployment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_deployment

    &lt;p&gt;Deletes a deployment. To delete an active deployment, you must first cancel it. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDeployment.html\&quot;&gt;CancelDeployment&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deleting a deployment doesn&#39;t affect core devices that run that deployment, because core devices store the deployment&#39;s configuration on the device. Additionally, core devices can roll back to a previous deployment that has been deleted.&lt;/p&gt;

    :param deployment_id: The ID of the deployment.
    :type deployment_id: str
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


async def describe_component(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_component

    Retrieves metadata for a version of a component.

    :param arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version.
    :type arn: str
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


async def disassociate_service_role_from_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_service_role_from_account

    Disassociates the Greengrass service role from IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. Without a service role, IoT Greengrass can&#39;t verify the identity of client devices or manage core device connectivity information. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html\&quot;&gt;Greengrass service role&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.

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


async def get_component(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, recipe_output_format=None) -> web.Response:
    """get_component

    Gets the recipe for a version of a component.

    :param arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version.
    :type arn: str
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
    :param recipe_output_format: The format of the recipe.
    :type recipe_output_format: str

    """
    return web.Response(status=200)


async def get_component_version_artifact(request: web.Request, arn, artifact_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_component_version_artifact

    Gets the pre-signed URL to download a public or a Lambda component artifact. Core devices call this operation to identify the URL that they can use to download an artifact to install.

    :param arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version. Specify the ARN of a public or a Lambda component version.
    :type arn: str
    :param artifact_name: &lt;p&gt;The name of the artifact.&lt;/p&gt; &lt;p&gt;You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html\&quot;&gt;GetComponent&lt;/a&gt; operation to download the component recipe, which includes the URI of the artifact. The artifact name is the section of the URI after the scheme. For example, in the artifact URI &lt;code&gt;greengrass:SomeArtifact.zip&lt;/code&gt;, the artifact name is &lt;code&gt;SomeArtifact.zip&lt;/code&gt;.&lt;/p&gt;
    :type artifact_name: str
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


async def get_connectivity_info(request: web.Request, thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_connectivity_info

    &lt;p&gt;Retrieves connectivity information for a Greengrass core device.&lt;/p&gt; &lt;p&gt;Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html\&quot;&gt;IoT Greengrass discovery API&lt;/a&gt;, IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html\&quot;&gt;Connect client devices to core devices&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param thing_name: The name of the core device. This is also the name of the IoT thing.
    :type thing_name: str
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


async def get_core_device(request: web.Request, core_device_thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_core_device

    &lt;p&gt;Retrieves metadata for a Greengrass core device.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn&#39;t running on the device, or if device isn&#39;t connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.&lt;/p&gt; &lt;p&gt;Core devices send status updates at the following times:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When the IoT Greengrass Core software starts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the core device receives a deployment from the Amazon Web Services Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the status of any component on the core device becomes &lt;code&gt;BROKEN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;At a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss\&quot;&gt;regular interval that you can configure&lt;/a&gt;, which defaults to 24 hours&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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


async def get_deployment(request: web.Request, deployment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deployment

    Gets a deployment. Deployments define the components that run on Greengrass core devices.

    :param deployment_id: The ID of the deployment.
    :type deployment_id: str
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


async def get_service_role_for_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_role_for_account

    Gets the service role associated with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html\&quot;&gt;Greengrass service role&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.

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


async def list_client_devices_associated_with_core_device(request: web.Request, core_device_thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_client_devices_associated_with_core_device

    Retrieves a paginated list of client devices that are associated with a core device.

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_component_versions(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_component_versions

    Retrieves a paginated list of all versions for a component. Greater versions are listed first.

    :param arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component.
    :type arn: str
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
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_components(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, scope=None, max_results=None, next_token=None) -> web.Response:
    """list_components

    Retrieves a paginated list of component summaries. This list includes components that you have permission to view.

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
    :param scope: &lt;p&gt;The scope of the components to list.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;PRIVATE&lt;/code&gt; &lt;/p&gt;
    :type scope: str
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_core_devices(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, thing_group_arn=None, status=None, max_results=None, next_token=None) -> web.Response:
    """list_core_devices

    &lt;p&gt;Retrieves a paginated list of Greengrass core devices.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn&#39;t running on the device, or if device isn&#39;t connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.&lt;/p&gt; &lt;p&gt;Core devices send status updates at the following times:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When the IoT Greengrass Core software starts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the core device receives a deployment from the Amazon Web Services Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the status of any component on the core device becomes &lt;code&gt;BROKEN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;At a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss\&quot;&gt;regular interval that you can configure&lt;/a&gt;, which defaults to 24 hours&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param thing_group_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device.
    :type thing_group_arn: str
    :param status: &lt;p&gt;The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HEALTHY&lt;/code&gt; – The IoT Greengrass Core software and all components run on the core device without issue.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UNHEALTHY&lt;/code&gt; – The IoT Greengrass Core software or a component is in a failed state on the core device.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type status: str
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_deployments(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, target_arn=None, history_filter=None, parent_target_arn=None, max_results=None, next_token=None) -> web.Response:
    """list_deployments

    Retrieves a paginated list of deployments.

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
    :param target_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the target IoT thing or thing group.
    :type target_arn: str
    :param history_filter: &lt;p&gt;The filter for the list of deployments. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all deployments.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LATEST_ONLY&lt;/code&gt; – The list includes only the latest revision of each deployment.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;LATEST_ONLY&lt;/code&gt; &lt;/p&gt;
    :type history_filter: str
    :param parent_target_arn: The parent deployment&#39;s target &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; within a subdeployment.
    :type parent_target_arn: str
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_effective_deployments(request: web.Request, core_device_thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_effective_deployments

    Retrieves a paginated list of deployment jobs that IoT Greengrass sends to Greengrass core devices.

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_installed_components(request: web.Request, core_device_thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, topology_filter=None) -> web.Response:
    """list_installed_components

    &lt;p&gt;Retrieves a paginated list of the components that a Greengrass core device runs. By default, this list doesn&#39;t include components that are deployed as dependencies of other components. To include dependencies in the response, set the &lt;code&gt;topologyFilter&lt;/code&gt; parameter to &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn&#39;t running on the device, or if device isn&#39;t connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.&lt;/p&gt; &lt;p&gt;Core devices send status updates at the following times:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When the IoT Greengrass Core software starts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the core device receives a deployment from the Amazon Web Services Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the status of any component on the core device becomes &lt;code&gt;BROKEN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;At a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss\&quot;&gt;regular interval that you can configure&lt;/a&gt;, which defaults to 24 hours&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param core_device_thing_name: The name of the core device. This is also the name of the IoT thing.
    :type core_device_thing_name: str
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
    :param max_results: The maximum number of results to be returned per paginated request.
    :type max_results: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param topology_filter: &lt;p&gt;The filter for the list of components. Choose from the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all components installed on the core device.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ROOT&lt;/code&gt; – The list includes only &lt;i&gt;root&lt;/i&gt; components, which are components that you specify in a deployment. When you choose this option, the list doesn&#39;t include components that the core device installs as dependencies of other components.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;ROOT&lt;/code&gt; &lt;/p&gt;
    :type topology_filter: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieves the list of tags for an IoT Greengrass resource.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource.
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


async def resolve_component_candidates(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resolve_component_candidates

    &lt;p&gt;Retrieves a list of components that meet the component, version, and platform requirements of a deployment. Greengrass core devices call this operation when they receive a deployment to identify the components to install.&lt;/p&gt; &lt;p&gt;This operation identifies components that meet all dependency requirements for a deployment. If the requirements conflict, then this operation returns an error and the deployment fails. For example, this occurs if component &lt;code&gt;A&lt;/code&gt; requires version &lt;code&gt;&amp;gt;2.0.0&lt;/code&gt; and component &lt;code&gt;B&lt;/code&gt; requires version &lt;code&gt;&amp;lt;2.0.0&lt;/code&gt; of a component dependency.&lt;/p&gt; &lt;p&gt;When you specify the component candidates to resolve, IoT Greengrass compares each component&#39;s digest from the core device with the component&#39;s digest in the Amazon Web Services Cloud. If the digests don&#39;t match, then IoT Greengrass specifies to use the version from the Amazon Web Services Cloud.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To use this operation, you must use the data plane API endpoint and authenticate with an IoT device certificate. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/greengrass.html\&quot;&gt;IoT Greengrass endpoints and quotas&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

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
    body = ResolveComponentCandidatesRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds tags to an IoT Greengrass resource. If a tag already exists for the resource, this operation updates the tag&#39;s value.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to tag.
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

    Removes a tag from an IoT Greengrass resource.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to untag.
    :type resource_arn: str
    :param tag_keys: A list of keys for tags to remove from the resource.
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


async def update_connectivity_info(request: web.Request, thing_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_connectivity_info

    &lt;p&gt;Updates connectivity information for a Greengrass core device.&lt;/p&gt; &lt;p&gt;Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html\&quot;&gt;IoT Greengrass discovery API&lt;/a&gt;, IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html\&quot;&gt;Connect client devices to core devices&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param thing_name: The name of the core device. This is also the name of the IoT thing.
    :type thing_name: str
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
    body = UpdateConnectivityInfoRequest.from_dict(body)
    return web.Response(status=200)
