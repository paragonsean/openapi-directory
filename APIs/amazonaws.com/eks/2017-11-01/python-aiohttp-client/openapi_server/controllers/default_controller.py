from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_encryption_config_request import AssociateEncryptionConfigRequest
from openapi_server.models.associate_encryption_config_response import AssociateEncryptionConfigResponse
from openapi_server.models.associate_identity_provider_config_request import AssociateIdentityProviderConfigRequest
from openapi_server.models.associate_identity_provider_config_response import AssociateIdentityProviderConfigResponse
from openapi_server.models.create_addon_request import CreateAddonRequest
from openapi_server.models.create_addon_response import CreateAddonResponse
from openapi_server.models.create_cluster_request import CreateClusterRequest
from openapi_server.models.create_cluster_response import CreateClusterResponse
from openapi_server.models.create_fargate_profile_request import CreateFargateProfileRequest
from openapi_server.models.create_fargate_profile_response import CreateFargateProfileResponse
from openapi_server.models.create_nodegroup_request import CreateNodegroupRequest
from openapi_server.models.create_nodegroup_response import CreateNodegroupResponse
from openapi_server.models.delete_addon_response import DeleteAddonResponse
from openapi_server.models.delete_cluster_response import DeleteClusterResponse
from openapi_server.models.delete_fargate_profile_response import DeleteFargateProfileResponse
from openapi_server.models.delete_nodegroup_response import DeleteNodegroupResponse
from openapi_server.models.deregister_cluster_response import DeregisterClusterResponse
from openapi_server.models.describe_addon_configuration_response import DescribeAddonConfigurationResponse
from openapi_server.models.describe_addon_response import DescribeAddonResponse
from openapi_server.models.describe_addon_versions_response import DescribeAddonVersionsResponse
from openapi_server.models.describe_cluster_response import DescribeClusterResponse
from openapi_server.models.describe_fargate_profile_response import DescribeFargateProfileResponse
from openapi_server.models.describe_identity_provider_config_request import DescribeIdentityProviderConfigRequest
from openapi_server.models.describe_identity_provider_config_response import DescribeIdentityProviderConfigResponse
from openapi_server.models.describe_nodegroup_response import DescribeNodegroupResponse
from openapi_server.models.describe_update_response import DescribeUpdateResponse
from openapi_server.models.disassociate_identity_provider_config_request import DisassociateIdentityProviderConfigRequest
from openapi_server.models.disassociate_identity_provider_config_response import DisassociateIdentityProviderConfigResponse
from openapi_server.models.list_addons_response import ListAddonsResponse
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_fargate_profiles_response import ListFargateProfilesResponse
from openapi_server.models.list_identity_provider_configs_response import ListIdentityProviderConfigsResponse
from openapi_server.models.list_nodegroups_response import ListNodegroupsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_updates_response import ListUpdatesResponse
from openapi_server.models.register_cluster_request import RegisterClusterRequest
from openapi_server.models.register_cluster_response import RegisterClusterResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_addon_request import UpdateAddonRequest
from openapi_server.models.update_addon_response import UpdateAddonResponse
from openapi_server.models.update_cluster_config_request import UpdateClusterConfigRequest
from openapi_server.models.update_cluster_config_response import UpdateClusterConfigResponse
from openapi_server.models.update_cluster_version_request import UpdateClusterVersionRequest
from openapi_server.models.update_cluster_version_response import UpdateClusterVersionResponse
from openapi_server.models.update_nodegroup_config_request import UpdateNodegroupConfigRequest
from openapi_server.models.update_nodegroup_config_response import UpdateNodegroupConfigResponse
from openapi_server.models.update_nodegroup_version_request import UpdateNodegroupVersionRequest
from openapi_server.models.update_nodegroup_version_response import UpdateNodegroupVersionResponse
from openapi_server import util


async def associate_encryption_config(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_encryption_config

    &lt;p&gt;Associate encryption configuration to an existing cluster.&lt;/p&gt; &lt;p&gt;You can use this API to enable encryption on existing clusters which do not have encryption already enabled. This allows you to implement a defense-in-depth security strategy without migrating applications to new Amazon EKS clusters.&lt;/p&gt;

    :param name: The name of the cluster that you are associating with encryption configuration.
    :type name: str
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
    body = AssociateEncryptionConfigRequest.from_dict(body)
    return web.Response(status=200)


async def associate_identity_provider_config(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_identity_provider_config

    &lt;p&gt;Associate an identity provider configuration to a cluster.&lt;/p&gt; &lt;p&gt;If you want to authenticate identities using an identity provider, you can create an identity provider configuration and associate it to your cluster. After configuring authentication to your cluster you can create Kubernetes &lt;code&gt;roles&lt;/code&gt; and &lt;code&gt;clusterroles&lt;/code&gt; to assign permissions to the roles, and then bind the roles to the identities using Kubernetes &lt;code&gt;rolebindings&lt;/code&gt; and &lt;code&gt;clusterrolebindings&lt;/code&gt;. For more information see &lt;a href&#x3D;\&quot;https://kubernetes.io/docs/reference/access-authn-authz/rbac/\&quot;&gt;Using RBAC Authorization&lt;/a&gt; in the Kubernetes documentation.&lt;/p&gt;

    :param name: The name of the cluster to associate the configuration to.
    :type name: str
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
    body = AssociateIdentityProviderConfigRequest.from_dict(body)
    return web.Response(status=200)


async def create_addon(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_addon

    &lt;p&gt;Creates an Amazon EKS add-on.&lt;/p&gt; &lt;p&gt;Amazon EKS add-ons help to automate the provisioning and lifecycle management of common operational software for Amazon EKS clusters. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html\&quot;&gt;Amazon EKS add-ons&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt;

    :param name: The name of the cluster to create the add-on for.
    :type name: str
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
    body = CreateAddonRequest.from_dict(body)
    return web.Response(status=200)


async def create_cluster(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cluster

    &lt;p&gt;Creates an Amazon EKS control plane. &lt;/p&gt; &lt;p&gt;The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, such as &lt;code&gt;etcd&lt;/code&gt; and the API server. The control plane runs in an account managed by Amazon Web Services, and the Kubernetes API is exposed by the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single tenant and unique. It runs on its own set of Amazon EC2 instances.&lt;/p&gt; &lt;p&gt;The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the nodes (for example, to support &lt;code&gt;kubectl exec&lt;/code&gt;, &lt;code&gt;logs&lt;/code&gt;, and &lt;code&gt;proxy&lt;/code&gt; data flows).&lt;/p&gt; &lt;p&gt;Amazon EKS nodes run in your Amazon Web Services account and connect to your cluster&#39;s control plane over the Kubernetes API server endpoint and a certificate file that is created for your cluster.&lt;/p&gt; &lt;p&gt;In most cases, it takes several minutes to create a cluster. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch nodes into your cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/managing-auth.html\&quot;&gt;Managing Cluster Authentication&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html\&quot;&gt;Launching Amazon EKS nodes&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateClusterRequest.from_dict(body)
    return web.Response(status=200)


async def create_fargate_profile(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_fargate_profile

    &lt;p&gt;Creates an Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to run pods on Fargate.&lt;/p&gt; &lt;p&gt;The Fargate profile allows an administrator to declare which pods run on Fargate and specify which pods run on which Fargate profile. This declaration is done through the profile’s selectors. Each profile can have up to five selectors that contain a namespace and labels. A namespace is required for every selector. The label field consists of multiple optional key-value pairs. Pods that match the selectors are scheduled on Fargate. If a to-be-scheduled pod matches any of the selectors in the Fargate profile, then that pod is run on Fargate.&lt;/p&gt; &lt;p&gt;When you create a Fargate profile, you must specify a pod execution role to use with the pods that are scheduled with the profile. This role is added to the cluster&#39;s Kubernetes &lt;a href&#x3D;\&quot;https://kubernetes.io/docs/admin/authorization/rbac/\&quot;&gt;Role Based Access Control&lt;/a&gt; (RBAC) for authorization so that the &lt;code&gt;kubelet&lt;/code&gt; that is running on the Fargate infrastructure can register with your Amazon EKS cluster so that it can appear in your cluster as a node. The pod execution role also provides IAM permissions to the Fargate infrastructure to allow read access to Amazon ECR image repositories. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html\&quot;&gt;Pod Execution Role&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Fargate profiles are immutable. However, you can create a new updated profile to replace an existing profile and then delete the original after the updated profile has finished creating.&lt;/p&gt; &lt;p&gt;If any Fargate profiles in a cluster are in the &lt;code&gt;DELETING&lt;/code&gt; status, you must wait for that Fargate profile to finish deleting before you can create any other profiles in that cluster.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html\&quot;&gt;Fargate Profile&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt;

    :param name: The name of the Amazon EKS cluster to apply the Fargate profile to.
    :type name: str
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
    body = CreateFargateProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_nodegroup(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_nodegroup

    &lt;p&gt;Creates a managed node group for an Amazon EKS cluster. You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster, unless you deploy a custom AMI using a launch template. For more information about using launch templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2 instances that are managed by Amazon Web Services for an Amazon EKS cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html\&quot;&gt;Managed node groups&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Windows AMI types are only supported for commercial Regions that support Windows Amazon EKS.&lt;/p&gt; &lt;/note&gt;

    :param name: The name of the cluster to create the node group in.
    :type name: str
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
    body = CreateNodegroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_addon(request: web.Request, name, addon_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, preserve=None) -> web.Response:
    """delete_addon

    &lt;p&gt;Delete an Amazon EKS add-on.&lt;/p&gt; &lt;p&gt;When you remove the add-on, it will also be deleted from the cluster. You can always manually start an add-on on the cluster using the Kubernetes API.&lt;/p&gt;

    :param name: The name of the cluster to delete the add-on from.
    :type name: str
    :param addon_name: The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;.
    :type addon_name: str
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
    :param preserve: Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn&#39;t removed.
    :type preserve: bool

    """
    return web.Response(status=200)


async def delete_cluster(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_cluster

    &lt;p&gt;Deletes the Amazon EKS cluster control plane.&lt;/p&gt; &lt;p&gt;If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html\&quot;&gt;Deleting a Cluster&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first. For more information, see &lt;a&gt;DeleteNodegroup&lt;/a&gt; and &lt;a&gt;DeleteFargateProfile&lt;/a&gt;.&lt;/p&gt;

    :param name: The name of the cluster to delete.
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


async def delete_fargate_profile(request: web.Request, name, fargate_profile_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_fargate_profile

    &lt;p&gt;Deletes an Fargate profile.&lt;/p&gt; &lt;p&gt;When you delete a Fargate profile, any pods running on Fargate that were created with the profile are deleted. If those pods match another Fargate profile, then they are scheduled on Fargate with that profile. If they no longer match any Fargate profiles, then they are not scheduled on Fargate and they may remain in a pending state.&lt;/p&gt; &lt;p&gt;Only one Fargate profile in a cluster can be in the &lt;code&gt;DELETING&lt;/code&gt; status at a time. You must wait for a Fargate profile to finish deleting before you can delete any other profiles in that cluster.&lt;/p&gt;

    :param name: The name of the Amazon EKS cluster associated with the Fargate profile to delete.
    :type name: str
    :param fargate_profile_name: The name of the Fargate profile to delete.
    :type fargate_profile_name: str
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


async def delete_nodegroup(request: web.Request, name, nodegroup_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_nodegroup

    Deletes an Amazon EKS node group for a cluster.

    :param name: The name of the Amazon EKS cluster that is associated with your node group.
    :type name: str
    :param nodegroup_name: The name of the node group to delete.
    :type nodegroup_name: str
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


async def deregister_cluster(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_cluster

    Deregisters a connected cluster to remove it from the Amazon EKS control plane.

    :param name: The name of the connected cluster to deregister.
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


async def describe_addon(request: web.Request, name, addon_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_addon

    Describes an Amazon EKS add-on.

    :param name: The name of the cluster.
    :type name: str
    :param addon_name: The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;.
    :type addon_name: str
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


async def describe_addon_configuration(request: web.Request, addon_name, addon_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_addon_configuration

    Returns configuration options.

    :param addon_name: The name of the add-on. The name must match one of the names that &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt; returns.
    :type addon_name: str
    :param addon_version: The version of the add-on. The version must match one of the versions returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt;.
    :type addon_version: str
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


async def describe_addon_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, kubernetes_version=None, max_results=None, next_token=None, addon_name=None, types=None, publishers=None, owners=None) -> web.Response:
    """describe_addon_versions

    Describes the versions for an add-on. Information such as the Kubernetes versions that you can use the add-on with, the &lt;code&gt;owner&lt;/code&gt;, &lt;code&gt;publisher&lt;/code&gt;, and the &lt;code&gt;type&lt;/code&gt; of the add-on are returned. 

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
    :param kubernetes_version: The Kubernetes versions that you can use the add-on with.
    :type kubernetes_version: str
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;DescribeAddonVersionsRequest&lt;/code&gt; where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str
    :param addon_name: The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;.
    :type addon_name: str
    :param types: The type of the add-on. For valid &lt;code&gt;types&lt;/code&gt;, don&#39;t specify a value for this property.
    :type types: List[str]
    :param publishers: The publisher of the add-on. For valid &lt;code&gt;publishers&lt;/code&gt;, don&#39;t specify a value for this property.
    :type publishers: List[str]
    :param owners: The owner of the add-on. For valid &lt;code&gt;owners&lt;/code&gt;, don&#39;t specify a value for this property.
    :type owners: List[str]

    """
    return web.Response(status=200)


async def describe_cluster(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cluster

    &lt;p&gt;Returns descriptive information about an Amazon EKS cluster.&lt;/p&gt; &lt;p&gt;The API server endpoint and certificate authority data returned by this operation are required for &lt;code&gt;kubelet&lt;/code&gt; and &lt;code&gt;kubectl&lt;/code&gt; to communicate with your Kubernetes API server. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html\&quot;&gt;Create a kubeconfig for Amazon EKS&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The API server endpoint and certificate authority data aren&#39;t available until the cluster reaches the &lt;code&gt;ACTIVE&lt;/code&gt; state.&lt;/p&gt; &lt;/note&gt;

    :param name: The name of the cluster to describe.
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


async def describe_fargate_profile(request: web.Request, name, fargate_profile_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_fargate_profile

    Returns descriptive information about an Fargate profile.

    :param name: The name of the Amazon EKS cluster associated with the Fargate profile.
    :type name: str
    :param fargate_profile_name: The name of the Fargate profile to describe.
    :type fargate_profile_name: str
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


async def describe_identity_provider_config(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_identity_provider_config

    Returns descriptive information about an identity provider configuration.

    :param name: The cluster name that the identity provider configuration is associated to.
    :type name: str
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
    body = DescribeIdentityProviderConfigRequest.from_dict(body)
    return web.Response(status=200)


async def describe_nodegroup(request: web.Request, name, nodegroup_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_nodegroup

    Returns descriptive information about an Amazon EKS node group.

    :param name: The name of the Amazon EKS cluster associated with the node group.
    :type name: str
    :param nodegroup_name: The name of the node group to describe.
    :type nodegroup_name: str
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


async def describe_update(request: web.Request, name, update_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, nodegroup_name=None, addon_name=None) -> web.Response:
    """describe_update

    &lt;p&gt;Returns descriptive information about an update against your Amazon EKS cluster or associated managed node group or Amazon EKS add-on.&lt;/p&gt; &lt;p&gt;When the status of the update is &lt;code&gt;Succeeded&lt;/code&gt;, the update is complete. If an update fails, the status is &lt;code&gt;Failed&lt;/code&gt;, and an error detail explains the reason for the failure.&lt;/p&gt;

    :param name: The name of the Amazon EKS cluster associated with the update.
    :type name: str
    :param update_id: The ID of the update to describe.
    :type update_id: str
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
    :param nodegroup_name: The name of the Amazon EKS node group associated with the update. This parameter is required if the update is a node group update.
    :type nodegroup_name: str
    :param addon_name: The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;. This parameter is required if the update is an add-on update.
    :type addon_name: str

    """
    return web.Response(status=200)


async def disassociate_identity_provider_config(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_identity_provider_config

    Disassociates an identity provider configuration from a cluster. If you disassociate an identity provider from your cluster, users included in the provider can no longer access the cluster. However, you can still access the cluster with Amazon Web Services IAM users.

    :param name: The name of the cluster to disassociate an identity provider from.
    :type name: str
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
    body = DisassociateIdentityProviderConfigRequest.from_dict(body)
    return web.Response(status=200)


async def list_addons(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_addons

    Lists the available add-ons.

    :param name: The name of the cluster.
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
    :param max_results: The maximum number of add-on results returned by &lt;code&gt;ListAddonsRequest&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListAddonsRequest&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListAddonsRequest&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListAddonsRequest&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value, if applicable.
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListAddonsRequest&lt;/code&gt; where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_clusters(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, include=None) -> web.Response:
    """list_clusters

    Lists the Amazon EKS clusters in your Amazon Web Services account in the specified Region.

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
    :param max_results: The maximum number of cluster results returned by &lt;code&gt;ListClusters&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListClusters&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListClusters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListClusters&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListClusters&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str
    :param include: Indicates whether external clusters are included in the returned list. Use &#39;&lt;code&gt;all&lt;/code&gt;&#39; to return connected clusters, or blank to return only Amazon EKS clusters. &#39;&lt;code&gt;all&lt;/code&gt;&#39; must be in lowercase otherwise an error occurs.
    :type include: List[str]

    """
    return web.Response(status=200)


async def list_fargate_profiles(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_fargate_profiles

    Lists the Fargate profiles associated with the specified cluster in your Amazon Web Services account in the specified Region.

    :param name: The name of the Amazon EKS cluster that you would like to list Fargate profiles in.
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
    :param max_results: The maximum number of Fargate profile results returned by &lt;code&gt;ListFargateProfiles&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListFargateProfiles&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListFargateProfiles&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListFargateProfiles&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type max_results: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListFargateProfiles&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_identity_provider_configs(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_identity_provider_configs

    A list of identity provider configurations.

    :param name: The cluster name that you want to list identity provider configurations for.
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
    :param max_results: The maximum number of identity provider configurations returned by &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value, if applicable.
    :type max_results: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;IdentityProviderConfigsRequest&lt;/code&gt; where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_nodegroups(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_nodegroups

    Lists the Amazon EKS managed node groups associated with the specified cluster in your Amazon Web Services account in the specified Region. Self-managed node groups are not listed.

    :param name: The name of the Amazon EKS cluster that you would like to list node groups in.
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
    :param max_results: The maximum number of node group results returned by &lt;code&gt;ListNodegroups&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListNodegroups&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListNodegroups&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListNodegroups&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type max_results: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListNodegroups&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    List the tags for an Amazon EKS resource.

    :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.
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


async def list_updates(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, nodegroup_name=None, addon_name=None, next_token=None, max_results=None) -> web.Response:
    """list_updates

    Lists the updates associated with an Amazon EKS cluster or managed node group in your Amazon Web Services account, in the specified Region.

    :param name: The name of the Amazon EKS cluster to list updates for.
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
    :param nodegroup_name: The name of the Amazon EKS managed node group to list updates for.
    :type nodegroup_name: str
    :param addon_name: The names of the installed add-ons that have available updates.
    :type addon_name: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListUpdates&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str
    :param max_results: The maximum number of update results returned by &lt;code&gt;ListUpdates&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListUpdates&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListUpdates&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListUpdates&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type max_results: int

    """
    return web.Response(status=200)


async def register_cluster(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_cluster

    &lt;p&gt;Connects a Kubernetes cluster to the Amazon EKS control plane. &lt;/p&gt; &lt;p&gt;Any Kubernetes cluster can be connected to the Amazon EKS control plane to view current information about the cluster and its nodes. &lt;/p&gt; &lt;p&gt;Cluster connection requires two steps. First, send a &lt;code&gt; &lt;a&gt;RegisterClusterRequest&lt;/a&gt; &lt;/code&gt; to add it to the Amazon EKS control plane.&lt;/p&gt; &lt;p&gt;Second, a &lt;a href&#x3D;\&quot;https://amazon-eks.s3.us-west-2.amazonaws.com/eks-connector/manifests/eks-connector/latest/eks-connector.yaml\&quot;&gt;Manifest&lt;/a&gt; containing the &lt;code&gt;activationID&lt;/code&gt; and &lt;code&gt;activationCode&lt;/code&gt; must be applied to the Kubernetes cluster through it&#39;s native provider to provide visibility.&lt;/p&gt; &lt;p&gt;After the Manifest is updated and applied, then the connected cluster is visible to the Amazon EKS control plane. If the Manifest is not applied within three days, then the connected cluster will no longer be visible and must be deregistered. See &lt;a&gt;DeregisterCluster&lt;/a&gt;.&lt;/p&gt;

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
    body = RegisterClusterRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well. Tags that you create for Amazon EKS resources do not propagate to any other resources associated with the cluster. For example, if you tag a cluster with this operation, that tag does not automatically propagate to the subnets and nodes associated with the cluster.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.
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

    Deletes specified tags from a resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.
    :type resource_arn: str
    :param tag_keys: The keys of the tags to be removed.
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


async def update_addon(request: web.Request, name, addon_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_addon

    Updates an Amazon EKS add-on.

    :param name: The name of the cluster.
    :type name: str
    :param addon_name: The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;.
    :type addon_name: str
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
    body = UpdateAddonRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster_config(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster_config

    &lt;p&gt;Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the &lt;a&gt;DescribeUpdate&lt;/a&gt; API operation.&lt;/p&gt; &lt;p&gt;You can use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren&#39;t exported to CloudWatch Logs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html\&quot;&gt;Amazon EKS Cluster Control Plane Logs&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon EKS User Guide&lt;/i&gt; &lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can also use this API operation to enable or disable public and private access to your cluster&#39;s Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html\&quot;&gt;Amazon EKS cluster endpoint access control&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon EKS User Guide&lt;/i&gt; &lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can&#39;t update the subnets or security group IDs for an existing cluster.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to &lt;code&gt;UPDATING&lt;/code&gt; (this status transition is eventually consistent). When the update is complete (either &lt;code&gt;Failed&lt;/code&gt; or &lt;code&gt;Successful&lt;/code&gt;), the cluster status moves to &lt;code&gt;Active&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the Amazon EKS cluster to update.
    :type name: str
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
    body = UpdateClusterConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster_version(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster_version

    &lt;p&gt;Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the &lt;a&gt;DescribeUpdate&lt;/a&gt; API operation.&lt;/p&gt; &lt;p&gt;Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to &lt;code&gt;UPDATING&lt;/code&gt; (this status transition is eventually consistent). When the update is complete (either &lt;code&gt;Failed&lt;/code&gt; or &lt;code&gt;Successful&lt;/code&gt;), the cluster status moves to &lt;code&gt;Active&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If your cluster has managed node groups attached to it, all of your node groups’ Kubernetes versions must match the cluster’s Kubernetes version in order to update the cluster to a new Kubernetes version.&lt;/p&gt;

    :param name: The name of the Amazon EKS cluster to update.
    :type name: str
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
    body = UpdateClusterVersionRequest.from_dict(body)
    return web.Response(status=200)


async def update_nodegroup_config(request: web.Request, name, nodegroup_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_nodegroup_config

    Updates an Amazon EKS managed node group configuration. Your node group continues to function during the update. The response output includes an update ID that you can use to track the status of your node group update with the &lt;a&gt;DescribeUpdate&lt;/a&gt; API operation. Currently you can update the Kubernetes labels for a node group or the scaling configuration.

    :param name: The name of the Amazon EKS cluster that the managed node group resides in.
    :type name: str
    :param nodegroup_name: The name of the managed node group to update.
    :type nodegroup_name: str
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
    body = UpdateNodegroupConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_nodegroup_version(request: web.Request, name, nodegroup_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_nodegroup_version

    &lt;p&gt;Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.&lt;/p&gt; &lt;p&gt;You can update a node group using a launch template only if the node group was originally deployed with a launch template. If you need to update a custom AMI in a node group that was deployed with a launch template, then update your custom AMI, specify the new ID in a new version of the launch template, and then update the node group to the new version of the launch template.&lt;/p&gt; &lt;p&gt;If you update without a launch template, then you can update to the latest available AMI version of a node group&#39;s current Kubernetes version by not specifying a Kubernetes version in the request. You can update to the latest AMI version of your cluster&#39;s current Kubernetes version by specifying your cluster&#39;s Kubernetes version in the request. For information about Linux versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html\&quot;&gt;Amazon EKS optimized Amazon Linux AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. For information about Windows versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html\&quot;&gt;Amazon EKS optimized Windows AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;You cannot roll back a node group to an earlier Kubernetes version or AMI version.&lt;/p&gt; &lt;p&gt;When a node in a managed node group is terminated due to a scaling action or update, the pods in that node are drained first. Amazon EKS attempts to drain the nodes gracefully and will fail if it is unable to do so. You can &lt;code&gt;force&lt;/code&gt; the update if Amazon EKS is unable to drain the nodes as a result of a pod disruption budget issue.&lt;/p&gt;

    :param name: The name of the Amazon EKS cluster that is associated with the managed node group to update.
    :type name: str
    :param nodegroup_name: The name of the managed node group to update.
    :type nodegroup_name: str
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
    body = UpdateNodegroupVersionRequest.from_dict(body)
    return web.Response(status=200)
