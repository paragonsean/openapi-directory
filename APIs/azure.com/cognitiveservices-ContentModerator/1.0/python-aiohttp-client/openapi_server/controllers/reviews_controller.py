from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.frames import Frames
from openapi_server.models.job import Job
from openapi_server.models.job_id import JobId
from openapi_server.models.review import Review
from openapi_server.models.reviews_add_video_transcript_moderation_result_request_inner import ReviewsAddVideoTranscriptModerationResultRequestInner
from openapi_server.models.reviews_create_job_request import ReviewsCreateJobRequest
from openapi_server.models.reviews_create_reviews_request_inner import ReviewsCreateReviewsRequestInner
from openapi_server import util


async def reviews_add_video_frame(request: web.Request, team_name, review_id, timescale=None) -> web.Response:
    """reviews_add_video_frame

    The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

    :param team_name: Your team name.
    :type team_name: str
    :param review_id: Id of the review.
    :type review_id: str
    :param timescale: Timescale of the video you are adding frames to.
    :type timescale: int

    """
    return web.Response(status=200)


async def reviews_add_video_transcript(request: web.Request, team_name, review_id, content_type, vtt_file) -> web.Response:
    """reviews_add_video_transcript

    This API adds a transcript file (text version of all the words spoken in a video) to a video review. The file should be a valid WebVTT format.

    :param team_name: Your team name.
    :type team_name: str
    :param review_id: Id of the review.
    :type review_id: str
    :param content_type: The content type.
    :type content_type: str
    :param vtt_file: Transcript file of the video.
    :type vtt_file: 

    """
    return web.Response(status=200)


async def reviews_add_video_transcript_moderation_result(request: web.Request, content_type, team_name, review_id, transcript_moderation_body) -> web.Response:
    """reviews_add_video_transcript_moderation_result

    This API adds a transcript screen text result file for a video review. Transcript screen text result file is a result of Screen Text API . In order to generate transcript screen text result file , a transcript file has to be screened for profanity using Screen Text API.

    :param content_type: The content type.
    :type content_type: str
    :param team_name: Your team name.
    :type team_name: str
    :param review_id: Id of the review.
    :type review_id: str
    :param transcript_moderation_body: Body for add video transcript moderation result API
    :type transcript_moderation_body: list | bytes

    """
    transcript_moderation_body = [ReviewsAddVideoTranscriptModerationResultRequestInner.from_dict(d) for d in transcript_moderation_body]
    return web.Response(status=200)


async def reviews_create_job(request: web.Request, team_name, content_type, content_id, workflow_name, content_type2, content, call_back_endpoint=None) -> web.Response:
    """reviews_create_job

    A job Id will be returned for the content posted on this endpoint.     Once the content is evaluated against the Workflow provided the review will be created or ignored based on the workflow expression.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;    &lt;p&gt;  &lt;h4&gt;Job Completion CallBack Sample&lt;/h4&gt;&lt;br/&gt;    {&lt;br/&gt;    \&quot;JobId\&quot;: \&quot;&lt;Job Id&gt;,&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id, if the Job resulted in a Review to be created&gt;\&quot;,&lt;br/&gt;    \&quot;WorkFlowId\&quot;: \&quot;default\&quot;,&lt;br/&gt;    \&quot;Status\&quot;: \&quot;&lt;This will be one of Complete, InProgress, Error&gt;\&quot;,&lt;br/&gt;    \&quot;ContentType\&quot;: \&quot;Image\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;This is the ContentId that was specified on input&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Job\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;  &lt;p&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;&lt;br/&gt;    {    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

    :param team_name: Your team name.
    :type team_name: str
    :param content_type: Image, Text or Video.
    :type content_type: str
    :param content_id: Id/Name to identify the content submitted.
    :type content_id: str
    :param workflow_name: Workflow Name that you want to invoke.
    :type workflow_name: str
    :param content_type2: The content type.
    :type content_type2: str
    :param content: Content to evaluate.
    :type content: dict | bytes
    :param call_back_endpoint: Callback endpoint for posting the create job result.
    :type call_back_endpoint: str

    """
    content = ReviewsCreateJobRequest.from_dict(content)
    return web.Response(status=200)


async def reviews_create_reviews(request: web.Request, url_content_type, team_name, create_review_body, sub_team=None) -> web.Response:
    """reviews_create_reviews

    The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

    :param url_content_type: The content type.
    :type url_content_type: str
    :param team_name: Your team name.
    :type team_name: str
    :param create_review_body: Body for create reviews API
    :type create_review_body: list | bytes
    :param sub_team: SubTeam of your team, you want to assign the created review to.
    :type sub_team: str

    """
    create_review_body = [ReviewsCreateReviewsRequestInner.from_dict(d) for d in create_review_body]
    return web.Response(status=200)


async def reviews_get_job_details(request: web.Request, team_name, job_id) -> web.Response:
    """reviews_get_job_details

    Get the Job Details for a Job Id.

    :param team_name: Your Team Name.
    :type team_name: str
    :param job_id: Id of the job.
    :type job_id: str

    """
    return web.Response(status=200)


async def reviews_get_review(request: web.Request, team_name, review_id) -> web.Response:
    """reviews_get_review

    Returns review details for the review Id passed.

    :param team_name: Your Team Name.
    :type team_name: str
    :param review_id: Id of the review.
    :type review_id: str

    """
    return web.Response(status=200)


async def reviews_get_video_frames(request: web.Request, team_name, review_id, start_seed=None, no_of_records=None, filter=None) -> web.Response:
    """reviews_get_video_frames

    The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

    :param team_name: Your team name.
    :type team_name: str
    :param review_id: Id of the review.
    :type review_id: str
    :param start_seed: Time stamp of the frame from where you want to start fetching the frames.
    :type start_seed: int
    :param no_of_records: Number of frames to fetch.
    :type no_of_records: int
    :param filter: Get frames filtered by tags.
    :type filter: str

    """
    return web.Response(status=200)


async def reviews_publish_video_review(request: web.Request, team_name, review_id) -> web.Response:
    """reviews_publish_video_review

    Publish video review to make it available for review.

    :param team_name: Your team name.
    :type team_name: str
    :param review_id: Id of the review.
    :type review_id: str

    """
    return web.Response(status=200)
