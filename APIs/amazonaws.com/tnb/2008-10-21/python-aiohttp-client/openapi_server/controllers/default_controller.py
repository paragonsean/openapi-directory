from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_sol_function_package_output import CreateSolFunctionPackageOutput
from openapi_server.models.create_sol_function_package_request import CreateSolFunctionPackageRequest
from openapi_server.models.create_sol_network_instance_output import CreateSolNetworkInstanceOutput
from openapi_server.models.create_sol_network_instance_request import CreateSolNetworkInstanceRequest
from openapi_server.models.create_sol_network_package_output import CreateSolNetworkPackageOutput
from openapi_server.models.get_sol_function_instance_output import GetSolFunctionInstanceOutput
from openapi_server.models.get_sol_function_package_content_output import GetSolFunctionPackageContentOutput
from openapi_server.models.get_sol_function_package_descriptor_output import GetSolFunctionPackageDescriptorOutput
from openapi_server.models.get_sol_function_package_output import GetSolFunctionPackageOutput
from openapi_server.models.get_sol_network_instance_output import GetSolNetworkInstanceOutput
from openapi_server.models.get_sol_network_operation_output import GetSolNetworkOperationOutput
from openapi_server.models.get_sol_network_package_content_output import GetSolNetworkPackageContentOutput
from openapi_server.models.get_sol_network_package_descriptor_output import GetSolNetworkPackageDescriptorOutput
from openapi_server.models.get_sol_network_package_output import GetSolNetworkPackageOutput
from openapi_server.models.instantiate_sol_network_instance_output import InstantiateSolNetworkInstanceOutput
from openapi_server.models.instantiate_sol_network_instance_request import InstantiateSolNetworkInstanceRequest
from openapi_server.models.list_sol_function_instances_output import ListSolFunctionInstancesOutput
from openapi_server.models.list_sol_function_packages_output import ListSolFunctionPackagesOutput
from openapi_server.models.list_sol_network_instances_output import ListSolNetworkInstancesOutput
from openapi_server.models.list_sol_network_operations_output import ListSolNetworkOperationsOutput
from openapi_server.models.list_sol_network_packages_output import ListSolNetworkPackagesOutput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.put_sol_function_package_content_output import PutSolFunctionPackageContentOutput
from openapi_server.models.put_sol_function_package_content_request import PutSolFunctionPackageContentRequest
from openapi_server.models.put_sol_network_package_content_output import PutSolNetworkPackageContentOutput
from openapi_server.models.put_sol_network_package_content_request import PutSolNetworkPackageContentRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.terminate_sol_network_instance_output import TerminateSolNetworkInstanceOutput
from openapi_server.models.terminate_sol_network_instance_request import TerminateSolNetworkInstanceRequest
from openapi_server.models.update_sol_function_package_output import UpdateSolFunctionPackageOutput
from openapi_server.models.update_sol_function_package_request import UpdateSolFunctionPackageRequest
from openapi_server.models.update_sol_network_instance_output import UpdateSolNetworkInstanceOutput
from openapi_server.models.update_sol_network_instance_request import UpdateSolNetworkInstanceRequest
from openapi_server.models.update_sol_network_package_output import UpdateSolNetworkPackageOutput
from openapi_server.models.update_sol_network_package_request import UpdateSolNetworkPackageRequest
from openapi_server.models.validate_sol_function_package_content_output import ValidateSolFunctionPackageContentOutput
from openapi_server.models.validate_sol_network_package_content_output import ValidateSolNetworkPackageContentOutput
from openapi_server import util


async def cancel_sol_network_operation(request: web.Request, ns_lcm_op_occ_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_sol_network_operation

    &lt;p&gt;Cancels a network operation.&lt;/p&gt; &lt;p&gt;A network operation is any operation that is done to your network, such as network instance instantiation or termination.&lt;/p&gt;

    :param ns_lcm_op_occ_id: The identifier of the network operation.
    :type ns_lcm_op_occ_id: str
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


async def create_sol_function_package(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sol_function_package

    &lt;p&gt;Creates a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html\&quot;&gt;Function packages&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Telco Network Builder User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Creating a function package is the first step for creating a network in AWS TNB. This request creates an empty container with an ID. The next step is to upload the actual CSAR zip file into that empty container. To upload function package content, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html\&quot;&gt;PutSolFunctionPackageContent&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateSolFunctionPackageRequest.from_dict(body)
    return web.Response(status=200)


async def create_sol_network_instance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sol_network_instance

    &lt;p&gt;Creates a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed. Creating a network instance is the third step after creating a network package. For more information about network instances, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html\&quot;&gt;Network instances&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Telco Network Builder User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Once you create a network instance, you can instantiate it. To instantiate a network, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateSolNetworkInstance.html\&quot;&gt;InstantiateSolNetworkInstance&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateSolNetworkInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def create_sol_network_package(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sol_network_package

    &lt;p&gt;Creates a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html\&quot;&gt;Network instances&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Telco Network Builder User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;A network package consists of a network service descriptor (NSD) file (required) and any additional files (optional), such as scripts specific to your needs. For example, if you have multiple function packages in your network package, you can use the NSD to define which network functions should run in certain VPCs, subnets, or EKS clusters.&lt;/p&gt; &lt;p&gt;This request creates an empty network package container with an ID. Once you create a network package, you can upload the network package content using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html\&quot;&gt;PutSolNetworkPackageContent&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateSolFunctionPackageRequest.from_dict(body)
    return web.Response(status=200)


async def delete_sol_function_package(request: web.Request, vnf_pkg_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sol_function_package

    &lt;p&gt;Deletes a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt; &lt;p&gt;To delete a function package, the package must be in a disabled state. To disable a function package, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html\&quot;&gt;UpdateSolFunctionPackage&lt;/a&gt;. &lt;/p&gt;

    :param vnf_pkg_id: ID of the function package.
    :type vnf_pkg_id: str
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


async def delete_sol_network_instance(request: web.Request, ns_instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sol_network_instance

    &lt;p&gt;Deletes a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt; &lt;p&gt;To delete a network instance, the instance must be in a stopped or terminated state. To terminate a network instance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html\&quot;&gt;TerminateSolNetworkInstance&lt;/a&gt;.&lt;/p&gt;

    :param ns_instance_id: Network instance ID.
    :type ns_instance_id: str
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


async def delete_sol_network_package(request: web.Request, nsd_info_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sol_network_package

    &lt;p&gt;Deletes network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt; &lt;p&gt;To delete a network package, the package must be in a disable state. To disable a network package, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html\&quot;&gt;UpdateSolNetworkPackage&lt;/a&gt;.&lt;/p&gt;

    :param nsd_info_id: ID of the network service descriptor in the network package.
    :type nsd_info_id: str
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


async def get_sol_function_instance(request: web.Request, vnf_instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_function_instance

    &lt;p&gt;Gets the details of a network function instance, including the instantation state and metadata from the function package descriptor in the network function package.&lt;/p&gt; &lt;p&gt;A network function instance is a function in a function package .&lt;/p&gt;

    :param vnf_instance_id: ID of the network function.
    :type vnf_instance_id: str
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


async def get_sol_function_package(request: web.Request, vnf_pkg_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_function_package

    &lt;p&gt;Gets the details of an individual function package, such as the operational state and whether the package is in use.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network..&lt;/p&gt;

    :param vnf_pkg_id: ID of the function package.
    :type vnf_pkg_id: str
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


async def get_sol_function_package_content(request: web.Request, accept, vnf_pkg_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_function_package_content

    &lt;p&gt;Gets the contents of a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

    :param accept: The format of the package that you want to download from the function packages.
    :type accept: str
    :param vnf_pkg_id: ID of the function package.
    :type vnf_pkg_id: str
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


async def get_sol_function_package_descriptor(request: web.Request, accept, vnf_pkg_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_function_package_descriptor

    &lt;p&gt;Gets a function package descriptor in a function package.&lt;/p&gt; &lt;p&gt;A function package descriptor is a .yaml file in a function package that uses the TOSCA standard to describe how the network function in the function package should run on your network.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

    :param accept: Indicates which content types, expressed as MIME types, the client is able to understand.
    :type accept: str
    :param vnf_pkg_id: ID of the function package.
    :type vnf_pkg_id: str
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


async def get_sol_network_instance(request: web.Request, ns_instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_network_instance

    &lt;p&gt;Gets the details of the network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt;

    :param ns_instance_id: ID of the network instance.
    :type ns_instance_id: str
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


async def get_sol_network_operation(request: web.Request, ns_lcm_op_occ_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_network_operation

    &lt;p&gt;Gets the details of a network operation, including the tasks involved in the network operation and the status of the tasks.&lt;/p&gt; &lt;p&gt;A network operation is any operation that is done to your network, such as network instance instantiation or termination.&lt;/p&gt;

    :param ns_lcm_op_occ_id: The identifier of the network operation.
    :type ns_lcm_op_occ_id: str
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


async def get_sol_network_package(request: web.Request, nsd_info_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_network_package

    &lt;p&gt;Gets the details of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

    :param nsd_info_id: ID of the network service descriptor in the network package.
    :type nsd_info_id: str
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


async def get_sol_network_package_content(request: web.Request, accept, nsd_info_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_network_package_content

    &lt;p&gt;Gets the contents of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

    :param accept: The format of the package you want to download from the network package.
    :type accept: str
    :param nsd_info_id: ID of the network service descriptor in the network package.
    :type nsd_info_id: str
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


async def get_sol_network_package_descriptor(request: web.Request, nsd_info_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sol_network_package_descriptor

    &lt;p&gt;Gets the content of the network service descriptor.&lt;/p&gt; &lt;p&gt;A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the Amazon Web Services infrastructure you want to deploy the network functions on.&lt;/p&gt;

    :param nsd_info_id: ID of the network service descriptor in the network package.
    :type nsd_info_id: str
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


async def instantiate_sol_network_instance(request: web.Request, ns_instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, dry_run=None) -> web.Response:
    """instantiate_sol_network_instance

    &lt;p&gt;Instantiates a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt; &lt;p&gt;Before you can instantiate a network instance, you have to create a network instance. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkInstance.html\&quot;&gt;CreateSolNetworkInstance&lt;/a&gt;.&lt;/p&gt;

    :param ns_instance_id: ID of the network instance.
    :type ns_instance_id: str
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
    :param dry_run: A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is &lt;code&gt;DryRunOperation&lt;/code&gt;. Otherwise, it is &lt;code&gt;UnauthorizedOperation&lt;/code&gt;.
    :type dry_run: bool

    """
    body = InstantiateSolNetworkInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def list_sol_function_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, nextpage_opaque_marker=None, max_results2=None, next_token=None) -> web.Response:
    """list_sol_function_instances

    &lt;p&gt;Lists network function instances.&lt;/p&gt; &lt;p&gt;A network function instance is a function in a function package .&lt;/p&gt;

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
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param nextpage_opaque_marker: The token for the next page of results.
    :type nextpage_opaque_marker: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_sol_function_packages(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, nextpage_opaque_marker=None, max_results2=None, next_token=None) -> web.Response:
    """list_sol_function_packages

    &lt;p&gt;Lists information about function packages.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

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
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param nextpage_opaque_marker: The token for the next page of results.
    :type nextpage_opaque_marker: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_sol_network_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, nextpage_opaque_marker=None, max_results2=None, next_token=None) -> web.Response:
    """list_sol_network_instances

    &lt;p&gt;Lists your network instances.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt;

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
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param nextpage_opaque_marker: The token for the next page of results.
    :type nextpage_opaque_marker: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_sol_network_operations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, nextpage_opaque_marker=None, max_results2=None, next_token=None) -> web.Response:
    """list_sol_network_operations

    &lt;p&gt;Lists details for a network operation, including when the operation started and the status of the operation.&lt;/p&gt; &lt;p&gt;A network operation is any operation that is done to your network, such as network instance instantiation or termination.&lt;/p&gt;

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
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param nextpage_opaque_marker: The token for the next page of results.
    :type nextpage_opaque_marker: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_sol_network_packages(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, nextpage_opaque_marker=None, max_results2=None, next_token=None) -> web.Response:
    """list_sol_network_packages

    &lt;p&gt;Lists network packages.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

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
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param nextpage_opaque_marker: The token for the next page of results.
    :type nextpage_opaque_marker: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists tags for AWS TNB resources.

    :param resource_arn: Resource ARN.
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


async def put_sol_function_package_content(request: web.Request, vnf_pkg_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, content_type=None) -> web.Response:
    """put_sol_function_package_content

    &lt;p&gt;Uploads the contents of a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

    :param vnf_pkg_id: Function package ID.
    :type vnf_pkg_id: str
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
    :param content_type: Function package content type.
    :type content_type: str

    """
    body = PutSolFunctionPackageContentRequest.from_dict(body)
    return web.Response(status=200)


async def put_sol_network_package_content(request: web.Request, nsd_info_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, content_type=None) -> web.Response:
    """put_sol_network_package_content

    &lt;p&gt;Uploads the contents of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

    :param nsd_info_id: Network service descriptor info ID.
    :type nsd_info_id: str
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
    :param content_type: Network package content type.
    :type content_type: str

    """
    body = PutSolNetworkPackageContentRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Tags an AWS TNB resource.&lt;/p&gt; &lt;p&gt;A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.&lt;/p&gt;

    :param resource_arn: Resource ARN.
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


async def terminate_sol_network_instance(request: web.Request, ns_instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """terminate_sol_network_instance

    &lt;p&gt;Terminates a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt; &lt;p&gt;You must terminate a network instance before you can delete it.&lt;/p&gt;

    :param ns_instance_id: ID of the network instance.
    :type ns_instance_id: str
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
    body = TerminateSolNetworkInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Untags an AWS TNB resource.&lt;/p&gt; &lt;p&gt;A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.&lt;/p&gt;

    :param resource_arn: Resource ARN.
    :type resource_arn: str
    :param tag_keys: Tag keys.
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


async def update_sol_function_package(request: web.Request, vnf_pkg_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sol_function_package

    &lt;p&gt;Updates the operational state of function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

    :param vnf_pkg_id: ID of the function package.
    :type vnf_pkg_id: str
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
    body = UpdateSolFunctionPackageRequest.from_dict(body)
    return web.Response(status=200)


async def update_sol_network_instance(request: web.Request, ns_instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sol_network_instance

    &lt;p&gt;Update a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt;

    :param ns_instance_id: ID of the network instance.
    :type ns_instance_id: str
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
    body = UpdateSolNetworkInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def update_sol_network_package(request: web.Request, nsd_info_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sol_network_package

    &lt;p&gt;Updates the operational state of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt; &lt;p&gt;A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the Amazon Web Services infrastructure you want to deploy the network functions on.&lt;/p&gt;

    :param nsd_info_id: ID of the network service descriptor in the network package.
    :type nsd_info_id: str
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
    body = UpdateSolNetworkPackageRequest.from_dict(body)
    return web.Response(status=200)


async def validate_sol_function_package_content(request: web.Request, vnf_pkg_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, content_type=None) -> web.Response:
    """validate_sol_function_package_content

    &lt;p&gt;Validates function package content. This can be used as a dry run before uploading function package content with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html\&quot;&gt;PutSolFunctionPackageContent&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

    :param vnf_pkg_id: Function package ID.
    :type vnf_pkg_id: str
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
    :param content_type: Function package content type.
    :type content_type: str

    """
    body = PutSolFunctionPackageContentRequest.from_dict(body)
    return web.Response(status=200)


async def validate_sol_network_package_content(request: web.Request, nsd_info_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, content_type=None) -> web.Response:
    """validate_sol_network_package_content

    &lt;p&gt;Validates network package content. This can be used as a dry run before uploading network package content with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html\&quot;&gt;PutSolNetworkPackageContent&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

    :param nsd_info_id: Network service descriptor file.
    :type nsd_info_id: str
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
    :param content_type: Network package content type.
    :type content_type: str

    """
    body = PutSolNetworkPackageContentRequest.from_dict(body)
    return web.Response(status=200)
