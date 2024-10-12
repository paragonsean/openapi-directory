from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_scaling_policy_request import DeleteScalingPolicyRequest
from openapi_server.models.delete_scheduled_action_request import DeleteScheduledActionRequest
from openapi_server.models.deregister_scalable_target_request import DeregisterScalableTargetRequest
from openapi_server.models.describe_scalable_targets_request import DescribeScalableTargetsRequest
from openapi_server.models.describe_scalable_targets_response import DescribeScalableTargetsResponse
from openapi_server.models.describe_scaling_activities_request import DescribeScalingActivitiesRequest
from openapi_server.models.describe_scaling_activities_response import DescribeScalingActivitiesResponse
from openapi_server.models.describe_scaling_policies_request import DescribeScalingPoliciesRequest
from openapi_server.models.describe_scaling_policies_response import DescribeScalingPoliciesResponse
from openapi_server.models.describe_scheduled_actions_request import DescribeScheduledActionsRequest
from openapi_server.models.describe_scheduled_actions_response import DescribeScheduledActionsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_scaling_policy_request import PutScalingPolicyRequest
from openapi_server.models.put_scaling_policy_response import PutScalingPolicyResponse
from openapi_server.models.put_scheduled_action_request import PutScheduledActionRequest
from openapi_server.models.register_scalable_target_request import RegisterScalableTargetRequest
from openapi_server.models.register_scalable_target_response import RegisterScalableTargetResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server import util


async def delete_scaling_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_scaling_policy

    &lt;p&gt;Deletes the specified scaling policy for an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;Deleting a step scaling policy deletes the underlying alarm action, but does not delete the CloudWatch alarm associated with the scaling policy, even if it no longer has an associated action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html#delete-step-scaling-policy\&quot;&gt;Delete a step scaling policy&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html#delete-target-tracking-policy\&quot;&gt;Delete a target tracking scaling policy&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeleteScalingPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_scheduled_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_scheduled_action

    &lt;p&gt;Deletes the specified scheduled action for an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-additional-cli-commands.html#delete-scheduled-action\&quot;&gt;Delete a scheduled action&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeleteScheduledActionRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_scalable_target(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_scalable_target

    &lt;p&gt;Deregisters an Application Auto Scaling scalable target when you have finished using it. To see which resources have been registered, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html\&quot;&gt;DescribeScalableTargets&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Deregistering a scalable target deletes the scaling policies and the scheduled actions that are associated with it.&lt;/p&gt; &lt;/note&gt;

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
    body = DeregisterScalableTargetRequest.from_dict(body)
    return web.Response(status=200)


async def describe_scalable_targets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_scalable_targets

    &lt;p&gt;Gets information about the scalable targets in the specified namespace.&lt;/p&gt; &lt;p&gt;You can filter the results using &lt;code&gt;ResourceIds&lt;/code&gt; and &lt;code&gt;ScalableDimension&lt;/code&gt;.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeScalableTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_scaling_activities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_scaling_activities

    &lt;p&gt;Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.&lt;/p&gt; &lt;p&gt;You can filter the results using &lt;code&gt;ResourceId&lt;/code&gt; and &lt;code&gt;ScalableDimension&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For information about viewing scaling activities using the Amazon Web Services CLI, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html\&quot;&gt;Scaling activities for Application Auto Scaling&lt;/a&gt;.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeScalingActivitiesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_scaling_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_scaling_policies

    &lt;p&gt;Describes the Application Auto Scaling scaling policies for the specified service namespace.&lt;/p&gt; &lt;p&gt;You can filter the results using &lt;code&gt;ResourceId&lt;/code&gt;, &lt;code&gt;ScalableDimension&lt;/code&gt;, and &lt;code&gt;PolicyNames&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html\&quot;&gt;Target tracking scaling policies&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html\&quot;&gt;Step scaling policies&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeScalingPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_scheduled_actions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_scheduled_actions

    &lt;p&gt;Describes the Application Auto Scaling scheduled actions for the specified service namespace.&lt;/p&gt; &lt;p&gt;You can filter the results using the &lt;code&gt;ResourceId&lt;/code&gt;, &lt;code&gt;ScalableDimension&lt;/code&gt;, and &lt;code&gt;ScheduledActionNames&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html\&quot;&gt;Scheduled scaling&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-additional-cli-commands.html\&quot;&gt;Managing scheduled scaling&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeScheduledActionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Returns all the tags on the specified Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;For general information about tags, including the format and syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt;

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


async def put_scaling_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_scaling_policy

    &lt;p&gt;Creates or updates a scaling policy for an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scaling policy applies to the scalable target identified by those three attributes. You cannot create a scaling policy until you have registered the resource as a scalable target.&lt;/p&gt; &lt;p&gt;Multiple scaling policies can be in force at the same time for the same scalable target. You can have one or more target tracking scaling policies, one or more step scaling policies, or both. However, there is a chance that multiple policies could conflict, instructing the scalable target to scale out or in at the same time. Application Auto Scaling gives precedence to the policy that provides the largest capacity for both scale out and scale in. For example, if one policy increases capacity by 3, another policy increases capacity by 200 percent, and the current capacity is 10, Application Auto Scaling uses the policy with the highest calculated capacity (200% of 10 &#x3D; 20) and scales out to 30. &lt;/p&gt; &lt;p&gt;We recommend caution, however, when using target tracking scaling policies with step scaling policies because conflicts between these policies can cause undesirable behavior. For example, if the step scaling policy initiates a scale-in activity before the target tracking policy is ready to scale in, the scale-in activity will not be blocked. After the scale-in activity completes, the target tracking policy could instruct the scalable target to scale out again. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html\&quot;&gt;Target tracking scaling policies&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html\&quot;&gt;Step scaling policies&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a scalable target is deregistered, the scalable target is no longer available to use scaling policies. Any scaling policies that were specified for the scalable target are deleted.&lt;/p&gt; &lt;/note&gt;

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
    body = PutScalingPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_scheduled_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_scheduled_action

    &lt;p&gt;Creates or updates a scheduled action for an Application Auto Scaling scalable target. &lt;/p&gt; &lt;p&gt;Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scheduled action applies to the scalable target identified by those three attributes. You cannot create a scheduled action until you have registered the resource as a scalable target.&lt;/p&gt; &lt;p&gt;When you specify start and end times with a recurring schedule using a cron expression or rates, they form the boundaries for when the recurring action starts and stops.&lt;/p&gt; &lt;p&gt;To update a scheduled action, specify the parameters that you want to change. If you don&#39;t specify start and end times, the old values are deleted.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html\&quot;&gt;Scheduled scaling&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a scalable target is deregistered, the scalable target is no longer available to run scheduled actions. Any scheduled actions that were specified for the scalable target are deleted.&lt;/p&gt; &lt;/note&gt;

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
    body = PutScheduledActionRequest.from_dict(body)
    return web.Response(status=200)


async def register_scalable_target(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_scalable_target

    &lt;p&gt;Registers or updates a scalable target, which is the resource that you want to scale.&lt;/p&gt; &lt;p&gt;Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace, which represents some capacity dimension of the underlying service.&lt;/p&gt; &lt;p&gt;When you register a new scalable target, you must specify values for the minimum and maximum capacity. If the specified resource is not active in the target service, this operation does not change the resource&#39;s current capacity. Otherwise, it changes the resource&#39;s current capacity to a value that is inside of this range.&lt;/p&gt; &lt;p&gt;If you add a scaling policy, current capacity is adjustable within the specified range when scaling starts. Application Auto Scaling scaling policies will not scale capacity to values that are outside of the minimum and maximum range.&lt;/p&gt; &lt;p&gt;After you register a scalable target, you do not need to register it again to use other Application Auto Scaling operations. To see which resources have been registered, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html\&quot;&gt;DescribeScalableTargets&lt;/a&gt;. You can also view the scaling policies for a service namespace by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html\&quot;&gt;DescribeScalableTargets&lt;/a&gt;. If you no longer need a scalable target, you can deregister it by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html\&quot;&gt;DeregisterScalableTarget&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To update a scalable target, specify the parameters that you want to change. Include the parameters that identify the scalable target: resource ID, scalable dimension, and namespace. Any parameters that you don&#39;t specify are not changed by this update request. &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you call the &lt;code&gt;RegisterScalableTarget&lt;/code&gt; API operation to create a scalable target, there might be a brief delay until the operation achieves &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Eventual_consistency\&quot;&gt;eventual consistency&lt;/a&gt;. You might become aware of this brief delay if you get unexpected errors when performing sequential operations. The typical strategy is to retry the request, and some Amazon Web Services SDKs include automatic backoff and retry logic.&lt;/p&gt; &lt;p&gt;If you call the &lt;code&gt;RegisterScalableTarget&lt;/code&gt; API operation to update an existing scalable target, Application Auto Scaling retrieves the current capacity of the resource. If it&#39;s below the minimum capacity or above the maximum capacity, Application Auto Scaling adjusts the capacity of the scalable target to place it within these bounds, even if you don&#39;t include the &lt;code&gt;MinCapacity&lt;/code&gt; or &lt;code&gt;MaxCapacity&lt;/code&gt; request parameters.&lt;/p&gt; &lt;/note&gt;

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
    body = RegisterScalableTargetRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds or edits tags on an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;Each tag consists of a tag key and a tag value, which are both case-sensitive strings. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value.&lt;/p&gt; &lt;p&gt;You can use this operation to tag an Application Auto Scaling scalable target, but you cannot tag a scaling policy or scheduled action.&lt;/p&gt; &lt;p&gt;You can also add tags to an Application Auto Scaling scalable target while creating it (&lt;code&gt;RegisterScalableTarget&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;For general information about tags, including the format and syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Use tags to control access to a scalable target. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html\&quot;&gt;Tagging support for Application Auto Scaling&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Deletes tags from an Application Auto Scaling scalable target. To delete a tag, specify the tag key and the Application Auto Scaling scalable target.

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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)
