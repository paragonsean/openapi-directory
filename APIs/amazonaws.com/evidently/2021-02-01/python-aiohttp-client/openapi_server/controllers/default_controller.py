from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_evaluate_feature_request import BatchEvaluateFeatureRequest
from openapi_server.models.batch_evaluate_feature_response import BatchEvaluateFeatureResponse
from openapi_server.models.create_experiment_request import CreateExperimentRequest
from openapi_server.models.create_experiment_response import CreateExperimentResponse
from openapi_server.models.create_feature_request import CreateFeatureRequest
from openapi_server.models.create_feature_response import CreateFeatureResponse
from openapi_server.models.create_launch_request import CreateLaunchRequest
from openapi_server.models.create_launch_response import CreateLaunchResponse
from openapi_server.models.create_project_request import CreateProjectRequest
from openapi_server.models.create_project_response import CreateProjectResponse
from openapi_server.models.create_segment_request import CreateSegmentRequest
from openapi_server.models.create_segment_response import CreateSegmentResponse
from openapi_server.models.evaluate_feature_request import EvaluateFeatureRequest
from openapi_server.models.evaluate_feature_response import EvaluateFeatureResponse
from openapi_server.models.get_experiment_response import GetExperimentResponse
from openapi_server.models.get_experiment_results_request import GetExperimentResultsRequest
from openapi_server.models.get_experiment_results_response import GetExperimentResultsResponse
from openapi_server.models.get_feature_response import GetFeatureResponse
from openapi_server.models.get_launch_response import GetLaunchResponse
from openapi_server.models.get_project_response import GetProjectResponse
from openapi_server.models.get_segment_response import GetSegmentResponse
from openapi_server.models.list_experiments_response import ListExperimentsResponse
from openapi_server.models.list_features_response import ListFeaturesResponse
from openapi_server.models.list_launches_response import ListLaunchesResponse
from openapi_server.models.list_projects_response import ListProjectsResponse
from openapi_server.models.list_segment_references_response import ListSegmentReferencesResponse
from openapi_server.models.list_segments_response import ListSegmentsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_project_events_request import PutProjectEventsRequest
from openapi_server.models.put_project_events_response import PutProjectEventsResponse
from openapi_server.models.start_experiment_request import StartExperimentRequest
from openapi_server.models.start_experiment_response import StartExperimentResponse
from openapi_server.models.start_launch_response import StartLaunchResponse
from openapi_server.models.stop_experiment_request import StopExperimentRequest
from openapi_server.models.stop_experiment_response import StopExperimentResponse
from openapi_server.models.stop_launch_request import StopLaunchRequest
from openapi_server.models.stop_launch_response import StopLaunchResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.test_segment_pattern_request import TestSegmentPatternRequest
from openapi_server.models.test_segment_pattern_response import TestSegmentPatternResponse
from openapi_server.models.update_experiment_request import UpdateExperimentRequest
from openapi_server.models.update_experiment_response import UpdateExperimentResponse
from openapi_server.models.update_feature_request import UpdateFeatureRequest
from openapi_server.models.update_feature_response import UpdateFeatureResponse
from openapi_server.models.update_launch_request import UpdateLaunchRequest
from openapi_server.models.update_launch_response import UpdateLaunchResponse
from openapi_server.models.update_project_data_delivery_request import UpdateProjectDataDeliveryRequest
from openapi_server.models.update_project_data_delivery_response import UpdateProjectDataDeliveryResponse
from openapi_server.models.update_project_request import UpdateProjectRequest
from openapi_server.models.update_project_response import UpdateProjectResponse
from openapi_server import util


async def batch_evaluate_feature(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_evaluate_feature

    &lt;p&gt;This operation assigns feature variation to user sessions. For each user session, you pass in an &lt;code&gt;entityID&lt;/code&gt; that represents the user. Evidently then checks the evaluation rules and assigns the variation.&lt;/p&gt; &lt;p&gt;The first rules that are evaluated are the override rules. If the user&#39;s &lt;code&gt;entityID&lt;/code&gt; matches an override rule, the user is served the variation specified by that rule.&lt;/p&gt; &lt;p&gt;Next, if there is a launch of the feature, the user might be assigned to a variation in the launch. The chance of this depends on the percentage of users that are allocated to that launch. If the user is enrolled in the launch, the variation they are served depends on the allocation of the various feature variations used for the launch.&lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch, and there is an ongoing experiment for this feature, the user might be assigned to a variation in the experiment. The chance of this depends on the percentage of users that are allocated to that experiment. If the user is enrolled in the experiment, the variation they are served depends on the allocation of the various feature variations used for the experiment. &lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch or experiment, they are served the default variation.&lt;/p&gt;

    :param project: The name or ARN of the project that contains the feature being evaluated.
    :type project: str
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
    body = BatchEvaluateFeatureRequest.from_dict(body)
    return web.Response(status=200)


async def create_experiment(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_experiment

    &lt;p&gt;Creates an Evidently &lt;i&gt;experiment&lt;/i&gt;. Before you create an experiment, you must create the feature to use for the experiment.&lt;/p&gt; &lt;p&gt;An experiment helps you make feature design decisions based on evidence and data. An experiment can test as many as five variations at once. Evidently collects experiment data and analyzes it by statistical methods, and provides clear recommendations about which variations perform better.&lt;/p&gt; &lt;p&gt;You can optionally specify a &lt;code&gt;segment&lt;/code&gt; to have the experiment consider only certain audience types in the experiment, such as using only user sessions from a certain location or who use a certain internet browser.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an existing experiment. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateExperiment.html\&quot;&gt;UpdateExperiment&lt;/a&gt;. &lt;/p&gt;

    :param project: The name or ARN of the project that you want to create the new experiment in.
    :type project: str
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
    body = CreateExperimentRequest.from_dict(body)
    return web.Response(status=200)


async def create_feature(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_feature

    &lt;p&gt;Creates an Evidently &lt;i&gt;feature&lt;/i&gt; that you want to launch or test. You can define up to five variations of a feature, and use these variations in your launches and experiments. A feature must be created in a project. For information about creating a project, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html\&quot;&gt;CreateProject&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an existing feature. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateFeature.html\&quot;&gt;UpdateFeature&lt;/a&gt;. &lt;/p&gt;

    :param project: The name or ARN of the project that is to contain the new feature.
    :type project: str
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
    body = CreateFeatureRequest.from_dict(body)
    return web.Response(status=200)


async def create_launch(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_launch

    &lt;p&gt;Creates a &lt;i&gt;launch&lt;/i&gt; of a given feature. Before you create a launch, you must create the feature to use for the launch.&lt;/p&gt; &lt;p&gt;You can use a launch to safely validate new features by serving them to a specified percentage of your users while you roll out the feature. You can monitor the performance of the new feature to help you decide when to ramp up traffic to more users. This helps you reduce risk and identify unintended consequences before you fully launch the feature.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an existing launch. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateLaunch.html\&quot;&gt;UpdateLaunch&lt;/a&gt;. &lt;/p&gt;

    :param project: The name or ARN of the project that you want to create the launch in.
    :type project: str
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
    body = CreateLaunchRequest.from_dict(body)
    return web.Response(status=200)


async def create_project(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_project

    &lt;p&gt;Creates a project, which is the logical object in Evidently that can contain features, launches, and experiments. Use projects to group similar features together.&lt;/p&gt; &lt;p&gt;To update an existing project, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProject.html\&quot;&gt;UpdateProject&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_segment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_segment

    &lt;p&gt;Use this operation to define a &lt;i&gt;segment&lt;/i&gt; of your audience. A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age.&lt;/p&gt; &lt;p&gt;Using a segment in an experiment limits that experiment to evaluate only the users who match the segment criteria. Using one or more segments in a launch allows you to define different traffic splits for the different audience segments.&lt;/p&gt; &lt;p&gt;For more information about segment pattern syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax.html\&quot;&gt; Segment rule pattern syntax&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The pattern that you define for a segment is matched against the value of &lt;code&gt;evaluationContext&lt;/code&gt;, which is passed into Evidently in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html\&quot;&gt;EvaluateFeature&lt;/a&gt; operation, when Evidently assigns a feature variation to a user.&lt;/p&gt;

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
    body = CreateSegmentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_experiment(request: web.Request, experiment, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_experiment

    &lt;p&gt;Deletes an Evidently experiment. The feature used for the experiment is not deleted.&lt;/p&gt; &lt;p&gt;To stop an experiment without deleting it, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StopExperiment.html\&quot;&gt;StopExperiment&lt;/a&gt;. &lt;/p&gt;

    :param experiment: The name of the experiment to delete.
    :type experiment: str
    :param project: The name or ARN of the project that contains the experiment to delete.
    :type project: str
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


async def delete_feature(request: web.Request, feature, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_feature

    Deletes an Evidently feature.

    :param feature: The name of the feature to delete.
    :type feature: str
    :param project: The name or ARN of the project that contains the feature to delete.
    :type project: str
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


async def delete_launch(request: web.Request, launch, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_launch

    &lt;p&gt;Deletes an Evidently launch. The feature used for the launch is not deleted.&lt;/p&gt; &lt;p&gt;To stop a launch without deleting it, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StopLaunch.html\&quot;&gt;StopLaunch&lt;/a&gt;. &lt;/p&gt;

    :param launch: The name of the launch to delete.
    :type launch: str
    :param project: The name or ARN of the project that contains the launch to delete.
    :type project: str
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


async def delete_project(request: web.Request, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_project

    Deletes an Evidently project. Before you can delete a project, you must delete all the features that the project contains. To delete a feature, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteFeature.html\&quot;&gt;DeleteFeature&lt;/a&gt;.

    :param project: The name or ARN of the project to delete.
    :type project: str
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


async def delete_segment(request: web.Request, segment, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_segment

    Deletes a segment. You can&#39;t delete a segment that is being used in a launch or experiment, even if that launch or experiment is not currently running.

    :param segment: Specifies the segment to delete.
    :type segment: str
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


async def evaluate_feature(request: web.Request, feature, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """evaluate_feature

    &lt;p&gt;This operation assigns a feature variation to one given user session. You pass in an &lt;code&gt;entityID&lt;/code&gt; that represents the user. Evidently then checks the evaluation rules and assigns the variation.&lt;/p&gt; &lt;p&gt;The first rules that are evaluated are the override rules. If the user&#39;s &lt;code&gt;entityID&lt;/code&gt; matches an override rule, the user is served the variation specified by that rule.&lt;/p&gt; &lt;p&gt;If there is a current launch with this feature that uses segment overrides, and if the user session&#39;s &lt;code&gt;evaluationContext&lt;/code&gt; matches a segment rule defined in a segment override, the configuration in the segment overrides is used. For more information about segments, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateSegment.html\&quot;&gt;CreateSegment&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html\&quot;&gt;Use segments to focus your audience&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If there is a launch with no segment overrides, the user might be assigned to a variation in the launch. The chance of this depends on the percentage of users that are allocated to that launch. If the user is enrolled in the launch, the variation they are served depends on the allocation of the various feature variations used for the launch.&lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch, and there is an ongoing experiment for this feature, the user might be assigned to a variation in the experiment. The chance of this depends on the percentage of users that are allocated to that experiment.&lt;/p&gt; &lt;p&gt;If the experiment uses a segment, then only user sessions with &lt;code&gt;evaluationContext&lt;/code&gt; values that match the segment rule are used in the experiment.&lt;/p&gt; &lt;p&gt;If the user is enrolled in the experiment, the variation they are served depends on the allocation of the various feature variations used for the experiment. &lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch or experiment, they are served the default variation.&lt;/p&gt;

    :param feature: The name of the feature being evaluated.
    :type feature: str
    :param project: The name or ARN of the project that contains this feature.
    :type project: str
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
    body = EvaluateFeatureRequest.from_dict(body)
    return web.Response(status=200)


async def get_experiment(request: web.Request, experiment, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_experiment

    Returns the details about one experiment. You must already know the experiment name. To retrieve a list of experiments in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html\&quot;&gt;ListExperiments&lt;/a&gt;.

    :param experiment: The name of the experiment that you want to see the details of.
    :type experiment: str
    :param project: The name or ARN of the project that contains the experiment.
    :type project: str
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


async def get_experiment_results(request: web.Request, experiment, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_experiment_results

    &lt;p&gt;Retrieves the results of a running or completed experiment. No results are available until there have been 100 events for each variation and at least 10 minutes have passed since the start of the experiment. To increase the statistical power, Evidently performs an additional offline p-value analysis at the end of the experiment. Offline p-value analysis can detect statistical significance in some cases where the anytime p-values used during the experiment do not find statistical significance.&lt;/p&gt; &lt;p&gt;Experiment results are available up to 63 days after the start of the experiment. They are not available after that because of CloudWatch data retention policies.&lt;/p&gt;

    :param experiment: The name of the experiment to retrieve the results of.
    :type experiment: str
    :param project: The name or ARN of the project that contains the experiment that you want to see the results of.
    :type project: str
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
    body = GetExperimentResultsRequest.from_dict(body)
    return web.Response(status=200)


async def get_feature(request: web.Request, feature, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_feature

    Returns the details about one feature. You must already know the feature name. To retrieve a list of features in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeatures.html\&quot;&gt;ListFeatures&lt;/a&gt;.

    :param feature: The name of the feature that you want to retrieve information for.
    :type feature: str
    :param project: The name or ARN of the project that contains the feature.
    :type project: str
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


async def get_launch(request: web.Request, launch, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_launch

    Returns the details about one launch. You must already know the launch name. To retrieve a list of launches in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListLaunches.html\&quot;&gt;ListLaunches&lt;/a&gt;.

    :param launch: The name of the launch that you want to see the details of.
    :type launch: str
    :param project: The name or ARN of the project that contains the launch.
    :type project: str
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


async def get_project(request: web.Request, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_project

    Returns the details about one launch. You must already know the project name. To retrieve a list of projects in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListProjects.html\&quot;&gt;ListProjects&lt;/a&gt;.

    :param project: The name or ARN of the project that you want to see the details of.
    :type project: str
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


async def get_segment(request: web.Request, segment, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_segment

    Returns information about the specified segment. Specify the segment you want to view by specifying its ARN.

    :param segment: The ARN of the segment to return information for.
    :type segment: str
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


async def list_experiments(request: web.Request, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, status=None) -> web.Response:
    """list_experiments

    Returns configuration details about all the experiments in the specified project.

    :param project: The name or ARN of the project to return the experiment list from.
    :type project: str
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
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListExperiments&lt;/code&gt; operation.
    :type next_token: str
    :param status: Use this optional parameter to limit the returned results to only the experiments with the status that you specify here.
    :type status: str

    """
    return web.Response(status=200)


async def list_features(request: web.Request, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_features

    Returns configuration details about all the features in the specified project.

    :param project: The name or ARN of the project to return the feature list from.
    :type project: str
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
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListFeatures&lt;/code&gt; operation.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_launches(request: web.Request, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, status=None) -> web.Response:
    """list_launches

    Returns configuration details about all the launches in the specified project.

    :param project: The name or ARN of the project to return the launch list from.
    :type project: str
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
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListLaunches&lt;/code&gt; operation.
    :type next_token: str
    :param status: Use this optional parameter to limit the returned results to only the launches with the status that you specify here.
    :type status: str

    """
    return web.Response(status=200)


async def list_projects(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_projects

    Returns configuration details about all the projects in the current Region in your account.

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
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListProjects&lt;/code&gt; operation.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_segment_references(request: web.Request, segment, type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_segment_references

    Use this operation to find which experiments or launches are using a specified segment.

    :param segment: The ARN of the segment that you want to view information for.
    :type segment: str
    :param type: Specifies whether to return information about launches or experiments that use this segment.
    :type type: str
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
    :param max_results: The maximum number of results to include in the response. If you omit this, the default of 50 is used.
    :type max_results: int
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListSegmentReferences&lt;/code&gt; operation.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_segments(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_segments

    Returns a list of audience segments that you have created in your account in this Region.

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
    :param max_results: The maximum number of results to include in the response. If you omit this, the default of 50 is used.
    :type max_results: int
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListSegments&lt;/code&gt; operation.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with an Evidently resource.

    :param resource_arn: The ARN of the resource that you want to see the tags of.
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


async def put_project_events(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_project_events

    Sends performance events to Evidently. These events can be used to evaluate a launch or an experiment.

    :param project: The name or ARN of the project to write the events to.
    :type project: str
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
    body = PutProjectEventsRequest.from_dict(body)
    return web.Response(status=200)


async def start_experiment(request: web.Request, experiment, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_experiment

    Starts an existing experiment. To create an experiment, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateExperiment.html\&quot;&gt;CreateExperiment&lt;/a&gt;.

    :param experiment: The name of the experiment to start.
    :type experiment: str
    :param project: The name or ARN of the project that contains the experiment to start.
    :type project: str
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
    body = StartExperimentRequest.from_dict(body)
    return web.Response(status=200)


async def start_launch(request: web.Request, launch, project, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_launch

    Starts an existing launch. To create a launch, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateLaunch.html\&quot;&gt;CreateLaunch&lt;/a&gt;.

    :param launch: The name of the launch to start.
    :type launch: str
    :param project: The name or ARN of the project that contains the launch to start.
    :type project: str
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


async def stop_experiment(request: web.Request, experiment, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_experiment

    Stops an experiment that is currently running. If you stop an experiment, you can&#39;t resume it or restart it.

    :param experiment: The name of the experiment to stop.
    :type experiment: str
    :param project: The name or ARN of the project that contains the experiment to stop.
    :type project: str
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
    body = StopExperimentRequest.from_dict(body)
    return web.Response(status=200)


async def stop_launch(request: web.Request, launch, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_launch

    Stops a launch that is currently running. After you stop a launch, you will not be able to resume it or restart it. Also, it will not be evaluated as a rule for traffic allocation, and the traffic that was allocated to the launch will instead be available to the feature&#39;s experiment, if there is one. Otherwise, all traffic will be served the default variation after the launch is stopped.

    :param launch: The name of the launch to stop.
    :type launch: str
    :param project: The name or ARN of the project that contains the launch that you want to stop.
    :type project: str
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
    body = StopLaunchRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch Evidently resource. Projects, features, launches, and experiments can be tagged.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt;

    :param resource_arn: The ARN of the CloudWatch Evidently resource that you&#39;re adding tags to.
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


async def test_segment_pattern(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_segment_pattern

    Use this operation to test a rules pattern that you plan to use to create an audience segment. For more information about segments, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateSegment.html\&quot;&gt;CreateSegment&lt;/a&gt;.

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
    body = TestSegmentPatternRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from the specified resource.

    :param resource_arn: The ARN of the CloudWatch Evidently resource that you&#39;re removing tags from.
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
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


async def update_experiment(request: web.Request, experiment, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_experiment

    &lt;p&gt;Updates an Evidently experiment. &lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an experiment&#39;s tag. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

    :param experiment: The name of the experiment to update.
    :type experiment: str
    :param project: The name or ARN of the project that contains the experiment that you want to update.
    :type project: str
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
    body = UpdateExperimentRequest.from_dict(body)
    return web.Response(status=200)


async def update_feature(request: web.Request, feature, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_feature

    &lt;p&gt;Updates an existing feature.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to update the tags of an existing feature. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

    :param feature: The name of the feature to be updated.
    :type feature: str
    :param project: The name or ARN of the project that contains the feature to be updated.
    :type project: str
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
    body = UpdateFeatureRequest.from_dict(body)
    return web.Response(status=200)


async def update_launch(request: web.Request, launch, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_launch

    &lt;p&gt;Updates a launch of a given feature. &lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update the tags of an existing launch. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

    :param launch: The name of the launch that is to be updated.
    :type launch: str
    :param project: The name or ARN of the project that contains the launch that you want to update.
    :type project: str
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
    body = UpdateLaunchRequest.from_dict(body)
    return web.Response(status=200)


async def update_project(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_project

    &lt;p&gt;Updates the description of an existing project.&lt;/p&gt; &lt;p&gt;To create a new project, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html\&quot;&gt;CreateProject&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update the data storage options of a project. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProjectDataDelivery.html\&quot;&gt;UpdateProjectDataDelivery&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update the tags of a project. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

    :param project: The name or ARN of the project to update.
    :type project: str
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
    body = UpdateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def update_project_data_delivery(request: web.Request, project, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_project_data_delivery

    &lt;p&gt;Updates the data storage options for this project. If you store evaluation events, you an keep them and analyze them on your own. If you choose not to store evaluation events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.&lt;/p&gt; &lt;p&gt;You can&#39;t specify both &lt;code&gt;cloudWatchLogs&lt;/code&gt; and &lt;code&gt;s3Destination&lt;/code&gt; in the same operation.&lt;/p&gt;

    :param project: The name or ARN of the project that you want to modify the data storage options for.
    :type project: str
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
    body = UpdateProjectDataDeliveryRequest.from_dict(body)
    return web.Response(status=200)
