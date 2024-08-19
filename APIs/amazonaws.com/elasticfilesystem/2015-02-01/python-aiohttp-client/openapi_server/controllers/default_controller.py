from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_point_description import AccessPointDescription
from openapi_server.models.backup_policy_description import BackupPolicyDescription
from openapi_server.models.create_access_point_request import CreateAccessPointRequest
from openapi_server.models.create_file_system_request import CreateFileSystemRequest
from openapi_server.models.create_mount_target_request import CreateMountTargetRequest
from openapi_server.models.create_replication_configuration_request import CreateReplicationConfigurationRequest
from openapi_server.models.create_tags_request import CreateTagsRequest
from openapi_server.models.delete_tags_request import DeleteTagsRequest
from openapi_server.models.describe_access_points_response import DescribeAccessPointsResponse
from openapi_server.models.describe_account_preferences_request import DescribeAccountPreferencesRequest
from openapi_server.models.describe_account_preferences_response import DescribeAccountPreferencesResponse
from openapi_server.models.describe_file_systems_response import DescribeFileSystemsResponse
from openapi_server.models.describe_mount_target_security_groups_response import DescribeMountTargetSecurityGroupsResponse
from openapi_server.models.describe_mount_targets_response import DescribeMountTargetsResponse
from openapi_server.models.describe_replication_configurations_response import DescribeReplicationConfigurationsResponse
from openapi_server.models.describe_tags_response import DescribeTagsResponse
from openapi_server.models.file_system_description import FileSystemDescription
from openapi_server.models.file_system_policy_description import FileSystemPolicyDescription
from openapi_server.models.lifecycle_configuration_description import LifecycleConfigurationDescription
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.modify_mount_target_security_groups_request import ModifyMountTargetSecurityGroupsRequest
from openapi_server.models.mount_target_description import MountTargetDescription
from openapi_server.models.put_account_preferences_request import PutAccountPreferencesRequest
from openapi_server.models.put_account_preferences_response import PutAccountPreferencesResponse
from openapi_server.models.put_backup_policy_request import PutBackupPolicyRequest
from openapi_server.models.put_file_system_policy_request import PutFileSystemPolicyRequest
from openapi_server.models.put_lifecycle_configuration_request import PutLifecycleConfigurationRequest
from openapi_server.models.replication_configuration_description import ReplicationConfigurationDescription
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_file_system_request import UpdateFileSystemRequest
from openapi_server import util


async def create_access_point(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_access_point

    &lt;p&gt;Creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point&#39;s root directory. Applications using the access point can only access data in the application&#39;s own directory and any subdirectories. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html\&quot;&gt;Mounting a file system using EFS access points&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If multiple requests to create access points on the same file system are sent in quick succession, and the file system is near the limit of 1,000 access points, you may experience a throttling response for these requests. This is to ensure that the file system does not exceed the stated access point limit.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:CreateAccessPoint&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;Access points can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the &lt;code&gt;elasticfilesystem:TagResource&lt;/code&gt; action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the &lt;code&gt;elasticfilesystem:TagResource&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html\&quot;&gt;Granting permissions to tag resources during creation&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateAccessPointRequest.from_dict(body)
    return web.Response(status=200)


async def create_file_system(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_file_system

    &lt;p&gt;Creates a new, empty file system. The operation requires a creation token in the request that Amazon EFS uses to ensure idempotent creation (calling the operation with same creation token has no effect). If a file system does not currently exist that is owned by the caller&#39;s Amazon Web Services account with the specified creation token, this operation does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new, empty file system. The file system will have an Amazon EFS assigned ID, and an initial lifecycle state &lt;code&gt;creating&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returns with the description of the created file system.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Otherwise, this operation returns a &lt;code&gt;FileSystemAlreadyExists&lt;/code&gt; error with the ID of the existing file system.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For basic use cases, you can use a randomly generated UUID for the creation token.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; The idempotent operation allows you to retry a &lt;code&gt;CreateFileSystem&lt;/code&gt; call without risk of creating an extra file system. This can happen when an initial call fails in a way that leaves it uncertain whether or not a file system was actually created. An example might be that a transport level timeout occurred or your connection was reset. As long as you use the same creation token, if the initial call had succeeded in creating a file system, the client can learn of its existence from the &lt;code&gt;FileSystemAlreadyExists&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#creating-using-create-fs-part1\&quot;&gt;Creating a file system&lt;/a&gt; in the &lt;i&gt;Amazon EFS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;CreateFileSystem&lt;/code&gt; call returns while the file system&#39;s lifecycle state is still &lt;code&gt;creating&lt;/code&gt;. You can check the file system creation status by calling the &lt;a&gt;DescribeFileSystems&lt;/a&gt; operation, which among other things returns the file system state.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation accepts an optional &lt;code&gt;PerformanceMode&lt;/code&gt; parameter that you choose for your file system. We recommend &lt;code&gt;generalPurpose&lt;/code&gt; performance mode for most file systems. File systems using the &lt;code&gt;maxIO&lt;/code&gt; performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can&#39;t be changed after the file system has been created. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes.html\&quot;&gt;Amazon EFS performance modes&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can set the throughput mode for the file system using the &lt;code&gt;ThroughputMode&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;After the file system is fully created, Amazon EFS sets its lifecycle state to &lt;code&gt;available&lt;/code&gt;, at which point you can create one or more mount targets for the file system in your VPC. For more information, see &lt;a&gt;CreateMountTarget&lt;/a&gt;. You mount your Amazon EFS file system on an EC2 instances in your VPC by using the mount target. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html\&quot;&gt;Amazon EFS: How it Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:CreateFileSystem&lt;/code&gt; action. &lt;/p&gt; &lt;p&gt;File systems can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the &lt;code&gt;elasticfilesystem:TagResource&lt;/code&gt; action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the &lt;code&gt;elasticfilesystem:TagResource&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html\&quot;&gt;Granting permissions to tag resources during creation&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateFileSystemRequest.from_dict(body)
    return web.Response(status=200)


async def create_mount_target(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_mount_target

    &lt;p&gt;Creates a mount target for a file system. You can then mount the file system on EC2 instances by using the mount target.&lt;/p&gt; &lt;p&gt;You can create one mount target in each Availability Zone in your VPC. All EC2 instances in a VPC within a given Availability Zone share a single mount target for a given file system. If you have multiple subnets in an Availability Zone, you create a mount target in one of the subnets. EC2 instances do not need to be in the same subnet as the mount target in order to access their file system.&lt;/p&gt; &lt;p&gt;You can create only one mount target for an EFS file system using One Zone storage classes. You must create that mount target in the same Availability Zone in which the file system is located. Use the &lt;code&gt;AvailabilityZoneName&lt;/code&gt; and &lt;code&gt;AvailabiltyZoneId&lt;/code&gt; properties in the &lt;a&gt;DescribeFileSystems&lt;/a&gt; response object to get this information. Use the &lt;code&gt;subnetId&lt;/code&gt; associated with the file system&#39;s Availability Zone when creating the mount target.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html\&quot;&gt;Amazon EFS: How it Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;To create a mount target for a file system, the file system&#39;s lifecycle state must be &lt;code&gt;available&lt;/code&gt;. For more information, see &lt;a&gt;DescribeFileSystems&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In the request, provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The file system ID for which you are creating the mount target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A subnet ID, which determines the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The VPC in which Amazon EFS creates the mount target&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Availability Zone in which Amazon EFS creates the mount target&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The IP address range from which Amazon EFS selects the IP address of the mount target (if you don&#39;t specify an IP address in the request)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After creating the mount target, Amazon EFS returns a response that includes, a &lt;code&gt;MountTargetId&lt;/code&gt; and an &lt;code&gt;IpAddress&lt;/code&gt;. You use this IP address when mounting the file system in an EC2 instance. You can also use the mount target&#39;s DNS name when mounting the file system. The EC2 instance on which you mount the file system by using the mount target can resolve the mount target&#39;s DNS name to its IP address. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-implementation\&quot;&gt;How it Works: Implementation Overview&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Note that you can create mount targets for a file system in only one VPC, and there can be only one mount target per Availability Zone. That is, if the file system already has one or more mount targets created for it, the subnet specified in the request to add another mount target must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must belong to the same VPC as the subnets of the existing mount targets&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not be in the same Availability Zone as any of the subnets of the existing mount targets&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the request satisfies the requirements, Amazon EFS does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new mount target in the specified subnet.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Also creates a new network interface in the subnet as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the request provides an &lt;code&gt;IpAddress&lt;/code&gt;, Amazon EFS assigns that IP address to the network interface. Otherwise, Amazon EFS assigns a free address in the subnet (in the same way that the Amazon EC2 &lt;code&gt;CreateNetworkInterface&lt;/code&gt; call does when a request does not specify a primary private IP address).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the request provides &lt;code&gt;SecurityGroups&lt;/code&gt;, this network interface is associated with those security groups. Otherwise, it belongs to the default security group for the subnet&#39;s VPC.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Assigns the description &lt;code&gt;Mount target &lt;i&gt;fsmt-id&lt;/i&gt; for file system &lt;i&gt;fs-id&lt;/i&gt; &lt;/code&gt; where &lt;code&gt; &lt;i&gt;fsmt-id&lt;/i&gt; &lt;/code&gt; is the mount target ID, and &lt;code&gt; &lt;i&gt;fs-id&lt;/i&gt; &lt;/code&gt; is the &lt;code&gt;FileSystemId&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sets the &lt;code&gt;requesterManaged&lt;/code&gt; property of the network interface to &lt;code&gt;true&lt;/code&gt;, and the &lt;code&gt;requesterId&lt;/code&gt; value to &lt;code&gt;EFS&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Each Amazon EFS mount target has one corresponding requester-managed EC2 network interface. After the network interface is created, Amazon EFS sets the &lt;code&gt;NetworkInterfaceId&lt;/code&gt; field in the mount target&#39;s description to the network interface ID, and the &lt;code&gt;IpAddress&lt;/code&gt; field to its address. If network interface creation fails, the entire &lt;code&gt;CreateMountTarget&lt;/code&gt; operation fails.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;CreateMountTarget&lt;/code&gt; call returns only after creating the network interface, but while the mount target state is still &lt;code&gt;creating&lt;/code&gt;, you can check the mount target creation status by calling the &lt;a&gt;DescribeMountTargets&lt;/a&gt; operation, which among other things returns the mount target state.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;We recommend that you create a mount target in each of the Availability Zones. There are cost considerations for using a file system in an Availability Zone through a mount target created in another Availability Zone. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/efs/\&quot;&gt;Amazon EFS&lt;/a&gt;. In addition, by always using a mount target local to the instance&#39;s Availability Zone, you eliminate a partial failure scenario. If the Availability Zone in which your mount target is created goes down, then you can&#39;t access your file system through that mount target. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the following action on the file system:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;elasticfilesystem:CreateMountTarget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation also requires permissions for the following Amazon EC2 actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:DescribeSubnets&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:DescribeNetworkInterfaces&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:CreateNetworkInterface&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateMountTargetRequest.from_dict(body)
    return web.Response(status=200)


async def create_replication_configuration(request: web.Request, source_file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_replication_configuration

    &lt;p&gt;Creates a replication configuration that replicates an existing EFS file system to a new, read-only file system. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html\&quot;&gt;Amazon EFS replication&lt;/a&gt; in the &lt;i&gt;Amazon EFS User Guide&lt;/i&gt;. The replication configuration specifies the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Source file system&lt;/b&gt; - An existing EFS file system that you want replicated. The source file system cannot be a destination file system in an existing replication configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Destination file system configuration&lt;/b&gt; - The configuration of the destination file system to which the source file system will be replicated. There can only be one destination file system in a replication configuration. The destination file system configuration consists of the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Amazon Web Services Region&lt;/b&gt; - The Amazon Web Services Region in which the destination file system is created. Amazon EFS replication is available in all Amazon Web Services Regions that Amazon EFS is available in, except Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Europe (Milan), and Middle East (Bahrain).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Availability Zone&lt;/b&gt; - If you want the destination file system to use EFS One Zone availability and durability, you must specify the Availability Zone to create the file system in. For more information about EFS storage classes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html\&quot;&gt; Amazon EFS storage classes&lt;/a&gt; in the &lt;i&gt;Amazon EFS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Encryption&lt;/b&gt; - All destination file systems are created with encryption at rest enabled. You can specify the Key Management Service (KMS) key that is used to encrypt the destination file system. If you don&#39;t specify a KMS key, your service-managed KMS key for Amazon EFS is used. &lt;/p&gt; &lt;note&gt; &lt;p&gt;After the file system is created, you cannot change the KMS key.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following properties are set by default:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Performance mode&lt;/b&gt; - The destination file system&#39;s performance mode matches that of the source file system, unless the destination file system uses EFS One Zone storage. In that case, the General Purpose performance mode is used. The performance mode cannot be changed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Throughput mode&lt;/b&gt; - The destination file system&#39;s throughput mode matches that of the source file system. After the file system is created, you can modify the throughput mode.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following properties are turned off by default:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Lifecycle management&lt;/b&gt; - EFS lifecycle management and EFS Intelligent-Tiering are not enabled on the destination file system. After the destination file system is created, you can enable EFS lifecycle management and EFS Intelligent-Tiering.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Automatic backups&lt;/b&gt; - Automatic daily backups not enabled on the destination file system. After the file system is created, you can change this setting.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html\&quot;&gt;Amazon EFS replication&lt;/a&gt; in the &lt;i&gt;Amazon EFS User Guide&lt;/i&gt;.&lt;/p&gt;

    :param source_file_system_id: Specifies the Amazon EFS file system that you want to replicate. This file system cannot already be a source or destination file system in another replication configuration.
    :type source_file_system_id: str
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
    body = CreateReplicationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_tags(request: web.Request, file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tags

    &lt;note&gt; &lt;p&gt;DEPRECATED - &lt;code&gt;CreateTags&lt;/code&gt; is deprecated and not maintained. To create tags for EFS resources, use the API action.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates or overwrites tags associated with a file system. Each tag is a key-value pair. If a tag key specified in the request already exists on the file system, this operation overwrites its value with the value provided in the request. If you add the &lt;code&gt;Name&lt;/code&gt; tag to your file system, Amazon EFS returns it in the response to the &lt;a&gt;DescribeFileSystems&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;elasticfilesystem:CreateTags&lt;/code&gt; action.&lt;/p&gt;

    :param file_system_id: The ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.
    :type file_system_id: str
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
    body = CreateTagsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_access_point(request: web.Request, access_point_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_access_point

    &lt;p&gt;Deletes the specified access point. After deletion is complete, new clients can no longer connect to the access points. Clients connected to the access point at the time of deletion will continue to function until they terminate their connection.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DeleteAccessPoint&lt;/code&gt; action.&lt;/p&gt;

    :param access_point_id: The ID of the access point that you want to delete.
    :type access_point_id: str
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


async def delete_file_system(request: web.Request, file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_file_system

    &lt;p&gt;Deletes a file system, permanently severing access to its contents. Upon return, the file system no longer exists and you can&#39;t access any contents of the deleted file system.&lt;/p&gt; &lt;p&gt;You need to manually delete mount targets attached to a file system before you can delete an EFS file system. This step is performed for you when you use the Amazon Web Services console to delete a file system.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete a file system that is part of an EFS Replication configuration. You need to delete the replication configuration first.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; You can&#39;t delete a file system that is in use. That is, if the file system has any mount targets, you must first delete them. For more information, see &lt;a&gt;DescribeMountTargets&lt;/a&gt; and &lt;a&gt;DeleteMountTarget&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;DeleteFileSystem&lt;/code&gt; call returns while the file system state is still &lt;code&gt;deleting&lt;/code&gt;. You can check the file system deletion status by calling the &lt;a&gt;DescribeFileSystems&lt;/a&gt; operation, which returns a list of file systems in your account. If you pass file system ID or creation token for the deleted file system, the &lt;a&gt;DescribeFileSystems&lt;/a&gt; returns a &lt;code&gt;404 FileSystemNotFound&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DeleteFileSystem&lt;/code&gt; action.&lt;/p&gt;

    :param file_system_id: The ID of the file system you want to delete.
    :type file_system_id: str
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


async def delete_file_system_policy(request: web.Request, file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_file_system_policy

    &lt;p&gt;Deletes the &lt;code&gt;FileSystemPolicy&lt;/code&gt; for the specified file system. The default &lt;code&gt;FileSystemPolicy&lt;/code&gt; goes into effect once the existing policy is deleted. For more information about the default file system policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/res-based-policies-efs.html\&quot;&gt;Using Resource-based Policies with EFS&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DeleteFileSystemPolicy&lt;/code&gt; action.&lt;/p&gt;

    :param file_system_id: Specifies the EFS file system for which to delete the &lt;code&gt;FileSystemPolicy&lt;/code&gt;.
    :type file_system_id: str
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


async def delete_mount_target(request: web.Request, mount_target_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_mount_target

    &lt;p&gt;Deletes the specified mount target.&lt;/p&gt; &lt;p&gt;This operation forcibly breaks any mounts of the file system by using the mount target that is being deleted, which might disrupt instances or applications using those mounts. To avoid applications getting cut off abruptly, you might consider unmounting any mounts of the mount target, if feasible. The operation also deletes the associated network interface. Uncommitted writes might be lost, but breaking a mount target using this operation does not corrupt the file system itself. The file system you created remains. You can mount an EC2 instance in your VPC by using another mount target.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the following action on the file system:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;elasticfilesystem:DeleteMountTarget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;DeleteMountTarget&lt;/code&gt; call returns while the mount target state is still &lt;code&gt;deleting&lt;/code&gt;. You can check the mount target deletion by calling the &lt;a&gt;DescribeMountTargets&lt;/a&gt; operation, which returns a list of mount target descriptions for the given file system. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;The operation also requires permissions for the following Amazon EC2 action on the mount target&#39;s network interface:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:DeleteNetworkInterface&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param mount_target_id: The ID of the mount target to delete (String).
    :type mount_target_id: str
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


async def delete_replication_configuration(request: web.Request, source_file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_replication_configuration

    Deletes an existing replication configuration. To delete a replication configuration, you must make the request from the Amazon Web Services Region in which the destination file system is located. Deleting a replication configuration ends the replication process. After a replication configuration is deleted, the destination file system is no longer read-only. You can write to the destination file system after its status becomes &lt;code&gt;Writeable&lt;/code&gt;.

    :param source_file_system_id: The ID of the source file system in the replication configuration.
    :type source_file_system_id: str
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


async def delete_tags(request: web.Request, file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tags

    &lt;note&gt; &lt;p&gt;DEPRECATED - &lt;code&gt;DeleteTags&lt;/code&gt; is deprecated and not maintained. To remove tags from EFS resources, use the API action.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the specified tags from a file system. If the &lt;code&gt;DeleteTags&lt;/code&gt; request includes a tag key that doesn&#39;t exist, Amazon EFS ignores it and doesn&#39;t cause an error. For more information about tags and related restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Tag restrictions&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DeleteTags&lt;/code&gt; action.&lt;/p&gt;

    :param file_system_id: The ID of the file system whose tags you want to delete (String).
    :type file_system_id: str
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
    body = DeleteTagsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_access_points(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, access_point_id=None, file_system_id=None) -> web.Response:
    """describe_access_points

    &lt;p&gt;Returns the description of a specific Amazon EFS access point if the &lt;code&gt;AccessPointId&lt;/code&gt; is provided. If you provide an EFS &lt;code&gt;FileSystemId&lt;/code&gt;, it returns descriptions of all access points for that file system. You can provide either an &lt;code&gt;AccessPointId&lt;/code&gt; or a &lt;code&gt;FileSystemId&lt;/code&gt; in the request, but not both. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeAccessPoints&lt;/code&gt; action.&lt;/p&gt;

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
    :param max_results: (Optional) When retrieving all access points for a file system, you can optionally specify the &lt;code&gt;MaxItems&lt;/code&gt; parameter to limit the number of objects returned in a response. The default value is 100. 
    :type max_results: int
    :param next_token:  &lt;code&gt;NextToken&lt;/code&gt; is present if the response is paginated. You can use &lt;code&gt;NextMarker&lt;/code&gt; in the subsequent request to fetch the next page of access point descriptions.
    :type next_token: str
    :param access_point_id: (Optional) Specifies an EFS access point to describe in the response; mutually exclusive with &lt;code&gt;FileSystemId&lt;/code&gt;.
    :type access_point_id: str
    :param file_system_id: (Optional) If you provide a &lt;code&gt;FileSystemId&lt;/code&gt;, EFS returns all access points for that file system; mutually exclusive with &lt;code&gt;AccessPointId&lt;/code&gt;.
    :type file_system_id: str

    """
    return web.Response(status=200)


async def describe_account_preferences(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account_preferences

    Returns the account preferences settings for the Amazon Web Services account associated with the user making the request, in the current Amazon Web Services Region. For more information, see &lt;a href&#x3D;\&quot;efs/latest/ug/manage-efs-resource-ids.html\&quot;&gt;Managing Amazon EFS resource IDs&lt;/a&gt;.

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
    body = DescribeAccountPreferencesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_backup_policy(request: web.Request, file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_backup_policy

    Returns the backup policy for the specified EFS file system.

    :param file_system_id: Specifies which EFS file system to retrieve the &lt;code&gt;BackupPolicy&lt;/code&gt; for.
    :type file_system_id: str
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


async def describe_file_system_policy(request: web.Request, file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_file_system_policy

    &lt;p&gt;Returns the &lt;code&gt;FileSystemPolicy&lt;/code&gt; for the specified EFS file system.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeFileSystemPolicy&lt;/code&gt; action.&lt;/p&gt;

    :param file_system_id: Specifies which EFS file system to retrieve the &lt;code&gt;FileSystemPolicy&lt;/code&gt; for.
    :type file_system_id: str
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


async def describe_file_systems(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None, creation_token=None, file_system_id=None) -> web.Response:
    """describe_file_systems

    &lt;p&gt;Returns the description of a specific Amazon EFS file system if either the file system &lt;code&gt;CreationToken&lt;/code&gt; or the &lt;code&gt;FileSystemId&lt;/code&gt; is provided. Otherwise, it returns descriptions of all file systems owned by the caller&#39;s Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all file system descriptions, you can optionally specify the &lt;code&gt;MaxItems&lt;/code&gt; parameter to limit the number of descriptions in a response. This number is automatically set to 100. If more file system descriptions remain, Amazon EFS returns a &lt;code&gt;NextMarker&lt;/code&gt;, an opaque token, in the response. In this case, you should send a subsequent request with the &lt;code&gt;Marker&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextMarker&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To retrieve a list of your file system descriptions, this operation is used in an iterative process, where &lt;code&gt;DescribeFileSystems&lt;/code&gt; is called first without the &lt;code&gt;Marker&lt;/code&gt; and then the operation continues to call it with the &lt;code&gt;Marker&lt;/code&gt; parameter set to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the previous response until the response has no &lt;code&gt;NextMarker&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; The order of file systems returned in the response of one &lt;code&gt;DescribeFileSystems&lt;/code&gt; call and the order of file systems returned across the responses of a multi-call iteration is unspecified. &lt;/p&gt; &lt;p&gt; This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeFileSystems&lt;/code&gt; action. &lt;/p&gt;

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
    :param max_items: (Optional) Specifies the maximum number of file systems to return in the response (integer). This number is automatically set to 100. The response is paginated at 100 per page if you have more than 100 file systems. 
    :type max_items: int
    :param marker: (Optional) Opaque pagination token returned from a previous &lt;code&gt;DescribeFileSystems&lt;/code&gt; operation (String). If present, specifies to continue the list from where the returning call had left off. 
    :type marker: str
    :param creation_token: (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.
    :type creation_token: str
    :param file_system_id: (Optional) ID of the file system whose description you want to retrieve (String).
    :type file_system_id: str

    """
    return web.Response(status=200)


async def describe_lifecycle_configuration(request: web.Request, file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_lifecycle_configuration

    &lt;p&gt;Returns the current &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object for the specified Amazon EFS file system. EFS lifecycle management uses the &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object to identify which files to move to the EFS Infrequent Access (IA) storage class. For a file system without a &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object, the call returns an empty array in the response.&lt;/p&gt; &lt;p&gt;When EFS Intelligent-Tiering is enabled, &lt;code&gt;TransitionToPrimaryStorageClass&lt;/code&gt; has a value of &lt;code&gt;AFTER_1_ACCESS&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeLifecycleConfiguration&lt;/code&gt; operation.&lt;/p&gt;

    :param file_system_id: The ID of the file system whose &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object you want to retrieve (String).
    :type file_system_id: str
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


async def describe_mount_target_security_groups(request: web.Request, mount_target_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_mount_target_security_groups

    &lt;p&gt;Returns the security groups currently in effect for a mount target. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not &lt;code&gt;deleted&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;elasticfilesystem:DescribeMountTargetSecurityGroups&lt;/code&gt; action on the mount target&#39;s file system. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:DescribeNetworkInterfaceAttribute&lt;/code&gt; action on the mount target&#39;s network interface. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param mount_target_id: The ID of the mount target whose security groups you want to retrieve.
    :type mount_target_id: str
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


async def describe_mount_targets(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None, file_system_id=None, mount_target_id=None, access_point_id=None) -> web.Response:
    """describe_mount_targets

    &lt;p&gt;Returns the descriptions of all the current mount targets, or a specific mount target, for a file system. When requesting all of the current mount targets, the order of mount targets returned in the response is unspecified.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeMountTargets&lt;/code&gt; action, on either the file system ID that you specify in &lt;code&gt;FileSystemId&lt;/code&gt;, or on the file system of the mount target that you specify in &lt;code&gt;MountTargetId&lt;/code&gt;.&lt;/p&gt;

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
    :param max_items: (Optional) Maximum number of mount targets to return in the response. Currently, this number is automatically set to 10, and other values are ignored. The response is paginated at 100 per page if you have more than 100 mount targets.
    :type max_items: int
    :param marker: (Optional) Opaque pagination token returned from a previous &lt;code&gt;DescribeMountTargets&lt;/code&gt; operation (String). If present, it specifies to continue the list from where the previous returning call left off.
    :type marker: str
    :param file_system_id: (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if an &lt;code&gt;AccessPointId&lt;/code&gt; or &lt;code&gt;MountTargetId&lt;/code&gt; is not included. Accepts either a file system ID or ARN as input.
    :type file_system_id: str
    :param mount_target_id: (Optional) ID of the mount target that you want to have described (String). It must be included in your request if &lt;code&gt;FileSystemId&lt;/code&gt; is not included. Accepts either a mount target ID or ARN as input.
    :type mount_target_id: str
    :param access_point_id: (Optional) The ID of the access point whose mount targets that you want to list. It must be included in your request if a &lt;code&gt;FileSystemId&lt;/code&gt; or &lt;code&gt;MountTargetId&lt;/code&gt; is not included in your request. Accepts either an access point ID or ARN as input.
    :type access_point_id: str

    """
    return web.Response(status=200)


async def describe_replication_configurations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, file_system_id=None, next_token=None, max_results=None) -> web.Response:
    """describe_replication_configurations

    Retrieves the replication configuration for a specific file system. If a file system is not specified, all of the replication configurations for the Amazon Web Services account in an Amazon Web Services Region are retrieved.

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
    :param file_system_id: You can retrieve the replication configuration for a specific file system by providing its file system ID.
    :type file_system_id: str
    :param next_token:  &lt;code&gt;NextToken&lt;/code&gt; is present if the response is paginated. You can use &lt;code&gt;NextToken&lt;/code&gt; in a subsequent request to fetch the next page of output.
    :type next_token: str
    :param max_results: (Optional) To limit the number of objects returned in a response, you can specify the &lt;code&gt;MaxItems&lt;/code&gt; parameter. The default value is 100. 
    :type max_results: int

    """
    return web.Response(status=200)


async def describe_tags(request: web.Request, file_system_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None) -> web.Response:
    """describe_tags

    &lt;note&gt; &lt;p&gt;DEPRECATED - The &lt;code&gt;DescribeTags&lt;/code&gt; action is deprecated and not maintained. To view tags associated with EFS resources, use the &lt;code&gt;ListTagsForResource&lt;/code&gt; API action.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the tags associated with a file system. The order of tags returned in the response of one &lt;code&gt;DescribeTags&lt;/code&gt; call and the order of tags returned across the responses of a multiple-call iteration (when using pagination) is unspecified. &lt;/p&gt; &lt;p&gt; This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeTags&lt;/code&gt; action. &lt;/p&gt;

    :param file_system_id: The ID of the file system whose tag set you want to retrieve.
    :type file_system_id: str
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
    :param max_items: (Optional) The maximum number of file system tags to return in the response. Currently, this number is automatically set to 100, and other values are ignored. The response is paginated at 100 per page if you have more than 100 tags.
    :type max_items: int
    :param marker: (Optional) An opaque pagination token returned from a previous &lt;code&gt;DescribeTags&lt;/code&gt; operation (String). If present, it specifies to continue the list from where the previous call left off.
    :type marker: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists all tags for a top-level EFS resource. You must provide the ID of the resource that you want to retrieve the tags for.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:DescribeAccessPoints&lt;/code&gt; action.&lt;/p&gt;

    :param resource_id: Specifies the EFS resource you want to retrieve tags for. You can retrieve tags for EFS file systems and access points using this API endpoint.
    :type resource_id: str
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
    :param max_results: (Optional) Specifies the maximum number of tag objects to return in the response. The default value is 100.
    :type max_results: int
    :param next_token: (Optional) You can use &lt;code&gt;NextToken&lt;/code&gt; in a subsequent request to fetch the next page of access point descriptions if the response payload was paginated.
    :type next_token: str

    """
    return web.Response(status=200)


async def modify_mount_target_security_groups(request: web.Request, mount_target_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_mount_target_security_groups

    &lt;p&gt;Modifies the set of security groups in effect for a mount target.&lt;/p&gt; &lt;p&gt;When you create a mount target, Amazon EFS also creates a new network interface. For more information, see &lt;a&gt;CreateMountTarget&lt;/a&gt;. This operation replaces the security groups in effect for the network interface associated with a mount target, with the &lt;code&gt;SecurityGroups&lt;/code&gt; provided in the request. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not &lt;code&gt;deleted&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;The operation requires permissions for the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;elasticfilesystem:ModifyMountTargetSecurityGroups&lt;/code&gt; action on the mount target&#39;s file system. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:ModifyNetworkInterfaceAttribute&lt;/code&gt; action on the mount target&#39;s network interface. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param mount_target_id: The ID of the mount target whose security groups you want to modify.
    :type mount_target_id: str
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
    body = ModifyMountTargetSecurityGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_preferences(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_preferences

    &lt;p&gt;Use this operation to set the account preference in the current Amazon Web Services Region to use long 17 character (63 bit) or short 8 character (32 bit) resource IDs for new EFS file system and mount target resources. All existing resource IDs are not affected by any changes you make. You can set the ID preference during the opt-in period as EFS transitions to long resource IDs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/manage-efs-resource-ids.html\&quot;&gt;Managing Amazon EFS resource IDs&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Starting in October, 2021, you will receive an error if you try to set the account preference to use the short 8 character format resource ID. Contact Amazon Web Services support if you receive an error and must use short IDs for file system and mount target resources.&lt;/p&gt; &lt;/note&gt;

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
    body = PutAccountPreferencesRequest.from_dict(body)
    return web.Response(status=200)


async def put_backup_policy(request: web.Request, file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_backup_policy

    Updates the file system&#39;s backup policy. Use this action to start or stop automatic backups of the file system. 

    :param file_system_id: Specifies which EFS file system to update the backup policy for.
    :type file_system_id: str
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
    body = PutBackupPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_file_system_policy(request: web.Request, file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_file_system_policy

    &lt;p&gt;Applies an Amazon EFS &lt;code&gt;FileSystemPolicy&lt;/code&gt; to an Amazon EFS file system. A file system policy is an IAM resource-based policy and can contain multiple policy statements. A file system always has exactly one file system policy, which can be the default policy or an explicit policy set or updated using this API operation. EFS file system policies have a 20,000 character limit. When an explicit policy is set, it overrides the default policy. For more information about the default file system policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html#default-filesystempolicy\&quot;&gt;Default EFS File System Policy&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;EFS file system policies have a 20,000 character limit.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:PutFileSystemPolicy&lt;/code&gt; action.&lt;/p&gt;

    :param file_system_id: The ID of the EFS file system that you want to create or update the &lt;code&gt;FileSystemPolicy&lt;/code&gt; for.
    :type file_system_id: str
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
    body = PutFileSystemPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_lifecycle_configuration(request: web.Request, file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_lifecycle_configuration

    &lt;p&gt;Use this action to manage EFS lifecycle management and EFS Intelligent-Tiering. A &lt;code&gt;LifecycleConfiguration&lt;/code&gt; consists of one or more &lt;code&gt;LifecyclePolicy&lt;/code&gt; objects that define the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;EFS Lifecycle management&lt;/b&gt; - When Amazon EFS automatically transitions files in a file system into the lower-cost EFS Infrequent Access (IA) storage class.&lt;/p&gt; &lt;p&gt;To enable EFS Lifecycle management, set the value of &lt;code&gt;TransitionToIA&lt;/code&gt; to one of the available options.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;EFS Intelligent-Tiering&lt;/b&gt; - When Amazon EFS automatically transitions files from IA back into the file system&#39;s primary storage class (EFS Standard or EFS One Zone Standard).&lt;/p&gt; &lt;p&gt;To enable EFS Intelligent-Tiering, set the value of &lt;code&gt;TransitionToPrimaryStorageClass&lt;/code&gt; to &lt;code&gt;AFTER_1_ACCESS&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html\&quot;&gt;EFS Lifecycle Management&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each Amazon EFS file system supports one lifecycle configuration, which applies to all files in the file system. If a &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object already exists for the specified file system, a &lt;code&gt;PutLifecycleConfiguration&lt;/code&gt; call modifies the existing configuration. A &lt;code&gt;PutLifecycleConfiguration&lt;/code&gt; call with an empty &lt;code&gt;LifecyclePolicies&lt;/code&gt; array in the request body deletes any existing &lt;code&gt;LifecycleConfiguration&lt;/code&gt; and turns off lifecycle management and EFS Intelligent-Tiering for the file system.&lt;/p&gt; &lt;p&gt;In the request, specify the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The ID for the file system for which you are enabling, disabling, or modifying lifecycle management and EFS Intelligent-Tiering.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;LifecyclePolicies&lt;/code&gt; array of &lt;code&gt;LifecyclePolicy&lt;/code&gt; objects that define when files are moved into IA storage, and when they are moved back to Standard storage.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon EFS requires that each &lt;code&gt;LifecyclePolicy&lt;/code&gt; object have only have a single transition, so the &lt;code&gt;LifecyclePolicies&lt;/code&gt; array needs to be structured with separate &lt;code&gt;LifecyclePolicy&lt;/code&gt; objects. See the example requests in the following section for more information.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:PutLifecycleConfiguration&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;To apply a &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object to an encrypted file system, you need the same Key Management Service permissions as when you created the encrypted file system.&lt;/p&gt;

    :param file_system_id: The ID of the file system for which you are creating the &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object (String).
    :type file_system_id: str
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
    body = PutLifecycleConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Creates a tag for an EFS resource. You can create tags for EFS file systems and access points using this API operation.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:TagResource&lt;/code&gt; action.&lt;/p&gt;

    :param resource_id: The ID specifying the EFS resource that you want to create a tag for.
    :type resource_id: str
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


async def untag_resource(request: web.Request, resource_id, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Removes tags from an EFS resource. You can remove tags from EFS file systems and access points using this API operation.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;elasticfilesystem:UntagResource&lt;/code&gt; action.&lt;/p&gt;

    :param resource_id: Specifies the EFS resource that you want to remove tags from.
    :type resource_id: str
    :param tag_keys: The keys of the key-value tag pairs that you want to remove from the specified EFS resource.
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


async def update_file_system(request: web.Request, file_system_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_file_system

    Updates the throughput mode or the amount of provisioned throughput of an existing file system.

    :param file_system_id: The ID of the file system that you want to update.
    :type file_system_id: str
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
    body = UpdateFileSystemRequest.from_dict(body)
    return web.Response(status=200)
