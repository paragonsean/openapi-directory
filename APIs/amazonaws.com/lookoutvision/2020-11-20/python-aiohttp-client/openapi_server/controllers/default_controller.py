from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_dataset_request import CreateDatasetRequest
from openapi_server.models.create_dataset_response import CreateDatasetResponse
from openapi_server.models.create_model_request import CreateModelRequest
from openapi_server.models.create_model_response import CreateModelResponse
from openapi_server.models.create_project_request import CreateProjectRequest
from openapi_server.models.create_project_response import CreateProjectResponse
from openapi_server.models.delete_model_response import DeleteModelResponse
from openapi_server.models.delete_project_response import DeleteProjectResponse
from openapi_server.models.describe_dataset_response import DescribeDatasetResponse
from openapi_server.models.describe_model_packaging_job_response import DescribeModelPackagingJobResponse
from openapi_server.models.describe_model_response import DescribeModelResponse
from openapi_server.models.describe_project_response import DescribeProjectResponse
from openapi_server.models.detect_anomalies_request import DetectAnomaliesRequest
from openapi_server.models.detect_anomalies_response import DetectAnomaliesResponse
from openapi_server.models.list_dataset_entries_response import ListDatasetEntriesResponse
from openapi_server.models.list_model_packaging_jobs_response import ListModelPackagingJobsResponse
from openapi_server.models.list_models_response import ListModelsResponse
from openapi_server.models.list_projects_response import ListProjectsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.start_model_packaging_job_request import StartModelPackagingJobRequest
from openapi_server.models.start_model_packaging_job_response import StartModelPackagingJobResponse
from openapi_server.models.start_model_request import StartModelRequest
from openapi_server.models.start_model_response import StartModelResponse
from openapi_server.models.stop_model_response import StopModelResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_dataset_entries_request import UpdateDatasetEntriesRequest
from openapi_server.models.update_dataset_entries_response import UpdateDatasetEntriesResponse
from openapi_server import util


async def create_dataset(request: web.Request, project_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """create_dataset

    &lt;p&gt;Creates a new dataset in an Amazon Lookout for Vision project. &lt;code&gt;CreateDataset&lt;/code&gt; can create a training or a test dataset from a valid dataset source (&lt;code&gt;DatasetSource&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;If you want a single dataset project, specify &lt;code&gt;train&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To have a project with separate training and test datasets, call &lt;code&gt;CreateDataset&lt;/code&gt; twice. On the first call, specify &lt;code&gt;train&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;. On the second call, specify &lt;code&gt;test&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:CreateDataset&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project in which you want to create a dataset.
    :type project_name: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;CreateDataset&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;CreateDataset&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;CreateDataset&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;CreateDataset&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt;
    :type x_amzn_client_token: str

    """
    body = CreateDatasetRequest.from_dict(body)
    return web.Response(status=200)


async def create_model(request: web.Request, project_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """create_model

    &lt;p&gt;Creates a new version of a model within an an Amazon Lookout for Vision project. &lt;code&gt;CreateModel&lt;/code&gt; is an asynchronous operation in which Amazon Lookout for Vision trains, tests, and evaluates a new version of a model. &lt;/p&gt; &lt;p&gt;To get the current status, check the &lt;code&gt;Status&lt;/code&gt; field returned in the response from &lt;a&gt;DescribeModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the project has a single dataset, Amazon Lookout for Vision internally splits the dataset to create a training and a test dataset. If the project has a training and a test dataset, Lookout for Vision uses the respective datasets to train and test the model. &lt;/p&gt; &lt;p&gt;After training completes, the evaluation metrics are stored at the location specified in &lt;code&gt;OutputConfig&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:CreateModel&lt;/code&gt; operation. If you want to tag your model, you also require permission to the &lt;code&gt;lookoutvision:TagResource&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project in which you want to create a model version.
    :type project_name: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;CreateModel&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;CreateModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;CreateModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from starting multiple training jobs. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;CreateModel&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt;
    :type x_amzn_client_token: str

    """
    body = CreateModelRequest.from_dict(body)
    return web.Response(status=200)


async def create_project(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """create_project

    &lt;p&gt;Creates an empty Amazon Lookout for Vision project. After you create the project, add a dataset by calling &lt;a&gt;CreateDataset&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:CreateProject&lt;/code&gt; operation.&lt;/p&gt;

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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;CreateProject&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;CreateProject&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;CreateProject&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple project creation requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;CreateProject&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt;
    :type x_amzn_client_token: str

    """
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_dataset(request: web.Request, project_name, dataset_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """delete_dataset

    &lt;p&gt;Deletes an existing Amazon Lookout for Vision &lt;code&gt;dataset&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;If your the project has a single dataset, you must create a new dataset before you can create a model.&lt;/p&gt; &lt;p&gt;If you project has a training dataset and a test dataset consider the following. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you delete the test dataset, your project reverts to a single dataset project. If you then train the model, Amazon Lookout for Vision internally splits the remaining dataset into a training and test dataset.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you delete the training dataset, you must create a training dataset before you can create a model.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DeleteDataset&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the dataset that you want to delete.
    :type project_name: str
    :param dataset_type: The type of the dataset to delete. Specify &lt;code&gt;train&lt;/code&gt; to delete the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to delete the test dataset. To delete the dataset in a single dataset project, specify &lt;code&gt;train&lt;/code&gt;.
    :type dataset_type: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;DeleteDataset&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;DeleteDataset&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;DeleteDataset&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple deletetion requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;DeleteDataset&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt;
    :type x_amzn_client_token: str

    """
    return web.Response(status=200)


async def delete_model(request: web.Request, project_name, model_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """delete_model

    &lt;p&gt;Deletes an Amazon Lookout for Vision model. You can&#39;t delete a running model. To stop a running model, use the &lt;a&gt;StopModel&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;It might take a few seconds to delete a model. To determine if a model has been deleted, call &lt;a&gt;ListModels&lt;/a&gt; and check if the version of the model (&lt;code&gt;ModelVersion&lt;/code&gt;) is in the &lt;code&gt;Models&lt;/code&gt; array. &lt;/p&gt; &lt;p/&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DeleteModel&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the model that you want to delete.
    :type project_name: str
    :param model_version: The version of the model that you want to delete.
    :type model_version: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;DeleteModel&lt;/code&gt; completes only once. You choose the value to pass. For example, an issue might prevent you from getting a response from &lt;code&gt;DeleteModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;DeleteModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for ClientToken, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple model deletion requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;DeleteModel&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt;
    :type x_amzn_client_token: str

    """
    return web.Response(status=200)


async def delete_project(request: web.Request, project_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """delete_project

    &lt;p&gt;Deletes an Amazon Lookout for Vision project.&lt;/p&gt; &lt;p&gt;To delete a project, you must first delete each version of the model associated with the project. To delete a model use the &lt;a&gt;DeleteModel&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;You also have to delete the dataset(s) associated with the model. For more information, see &lt;a&gt;DeleteDataset&lt;/a&gt;. The images referenced by the training and test datasets aren&#39;t deleted. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DeleteProject&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project to delete.
    :type project_name: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;DeleteProject&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;DeleteProject&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;DeleteProject&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple project deletion requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;DeleteProject&lt;/code&gt;. An idempotency token is active for 8 hours.&lt;/p&gt;
    :type x_amzn_client_token: str

    """
    return web.Response(status=200)


async def describe_dataset(request: web.Request, project_name, dataset_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_dataset

    &lt;p&gt;Describe an Amazon Lookout for Vision dataset.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeDataset&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the dataset that you want to describe.
    :type project_name: str
    :param dataset_type: The type of the dataset to describe. Specify &lt;code&gt;train&lt;/code&gt; to describe the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to describe the test dataset. If you have a single dataset project, specify &lt;code&gt;train&lt;/code&gt; 
    :type dataset_type: str
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


async def describe_model(request: web.Request, project_name, model_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_model

    &lt;p&gt;Describes a version of an Amazon Lookout for Vision model.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeModel&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The project that contains the version of a model that you want to describe.
    :type project_name: str
    :param model_version: The version of the model that you want to describe.
    :type model_version: str
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


async def describe_model_packaging_job(request: web.Request, project_name, job_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_model_packaging_job

    &lt;p&gt;Describes an Amazon Lookout for Vision model packaging job. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeModelPackagingJob&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Using your Amazon Lookout for Vision model on an edge device&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt;

    :param project_name: The name of the project that contains the model packaging job that you want to describe. 
    :type project_name: str
    :param job_name: The job name for the model packaging job. 
    :type job_name: str
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


async def describe_project(request: web.Request, project_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_project

    &lt;p&gt;Describes an Amazon Lookout for Vision project.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DescribeProject&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that you want to describe.
    :type project_name: str
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


async def detect_anomalies(request: web.Request, project_name, model_version, content_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detect_anomalies

    &lt;p&gt;Detects anomalies in an image that you supply. &lt;/p&gt; &lt;p&gt;The response from &lt;code&gt;DetectAnomalies&lt;/code&gt; includes a boolean prediction that the image contains one or more anomalies and a confidence value for the prediction. If the model is an image segmentation model, the response also includes segmentation information for each type of anomaly found in the image.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before calling &lt;code&gt;DetectAnomalies&lt;/code&gt;, you must first start your model with the &lt;a&gt;StartModel&lt;/a&gt; operation. You are charged for the amount of time, in minutes, that a model runs and for the number of anomaly detection units that your model uses. If you are not using a model, use the &lt;a&gt;StopModel&lt;/a&gt; operation to stop your model. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;i&gt;Detecting anomalies in an image&lt;/i&gt; in the Amazon Lookout for Vision developer guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:DetectAnomalies&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the model version that you want to use.
    :type project_name: str
    :param model_version: The version of the model that you want to use.
    :type model_version: str
    :param content_type: The type of the image passed in &lt;code&gt;Body&lt;/code&gt;. Valid values are &lt;code&gt;image/png&lt;/code&gt; (PNG format images) and &lt;code&gt;image/jpeg&lt;/code&gt; (JPG format images). 
    :type content_type: str
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
    body = DetectAnomaliesRequest.from_dict(body)
    return web.Response(status=200)


async def list_dataset_entries(request: web.Request, project_name, dataset_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, labeled=None, anomaly_class=None, created_before=None, created_after=None, next_token=None, max_results=None, source_ref_contains=None, max_results2=None, next_token2=None) -> web.Response:
    """list_dataset_entries

    &lt;p&gt;Lists the JSON Lines within a dataset. An Amazon Lookout for Vision JSON Line contains the anomaly information for a single image, including the image location and the assigned label.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListDatasetEntries&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the dataset that you want to list.
    :type project_name: str
    :param dataset_type: The type of the dataset that you want to list. Specify &lt;code&gt;train&lt;/code&gt; to list the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to list the test dataset. If you have a single dataset project, specify &lt;code&gt;train&lt;/code&gt;.
    :type dataset_type: str
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
    :param labeled: Specify &lt;code&gt;true&lt;/code&gt; to include labeled entries, otherwise specify &lt;code&gt;false&lt;/code&gt;. If you don&#39;t specify a value, Lookout for Vision returns all entries.
    :type labeled: bool
    :param anomaly_class: Specify &lt;code&gt;normal&lt;/code&gt; to include only normal images. Specify &lt;code&gt;anomaly&lt;/code&gt; to only include anomalous entries. If you don&#39;t specify a value, Amazon Lookout for Vision returns normal and anomalous images.
    :type anomaly_class: str
    :param created_before: Only includes entries before the specified date in the response. For example, &lt;code&gt;2020-06-23T00:00:00&lt;/code&gt;.
    :type created_before: str
    :param created_after: Only includes entries after the specified date in the response. For example, &lt;code&gt;2020-06-23T00:00:00&lt;/code&gt;.
    :type created_after: str
    :param next_token: If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of dataset entries.
    :type next_token: str
    :param max_results: The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.
    :type max_results: int
    :param source_ref_contains: Perform a \&quot;contains\&quot; search on the values of the &lt;code&gt;source-ref&lt;/code&gt; key within the dataset. For example a value of \&quot;IMG_17\&quot; returns all JSON Lines where the &lt;code&gt;source-ref&lt;/code&gt; key value matches &lt;i&gt;*IMG_17*&lt;/i&gt;.
    :type source_ref_contains: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    return web.Response(status=200)


async def list_model_packaging_jobs(request: web.Request, project_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_model_packaging_jobs

    &lt;p&gt; Lists the model packaging jobs created for an Amazon Lookout for Vision project. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListModelPackagingJobs&lt;/code&gt; operation. &lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Using your Amazon Lookout for Vision model on an edge device&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt;

    :param project_name:  The name of the project for which you want to list the model packaging jobs. 
    :type project_name: str
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
    :param next_token: If the previous response was incomplete (because there is more results to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. 
    :type next_token: str
    :param max_results: The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. 
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_models(request: web.Request, project_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_models

    &lt;p&gt;Lists the versions of a model in an Amazon Lookout for Vision project.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListModels&lt;/code&gt; operation is eventually consistent. Recent calls to &lt;code&gt;CreateModel&lt;/code&gt; might take a while to appear in the response from &lt;code&gt;ListProjects&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListModels&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the model versions that you want to list.
    :type project_name: str
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
    :param next_token: If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of models.
    :type next_token: str
    :param max_results: The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_projects(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_projects

    &lt;p&gt;Lists the Amazon Lookout for Vision projects in your AWS account that are in the AWS Region in which you call &lt;code&gt;ListProjects&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListProjects&lt;/code&gt; operation is eventually consistent. Recent calls to &lt;code&gt;CreateProject&lt;/code&gt; and &lt;code&gt;DeleteProject&lt;/code&gt; might take a while to appear in the response from &lt;code&gt;ListProjects&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListProjects&lt;/code&gt; operation.&lt;/p&gt;

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
    :param next_token: If the previous response was incomplete (because there is more data to retrieve), Amazon Lookout for Vision returns a pagination token in the response. You can use this pagination token to retrieve the next set of projects.
    :type next_token: str
    :param max_results: The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Returns a list of tags attached to the specified Amazon Lookout for Vision model.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:ListTagsForResource&lt;/code&gt; operation.&lt;/p&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the model for which you want to list tags. 
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


async def start_model(request: web.Request, project_name, model_version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """start_model

    &lt;p&gt;Starts the running of the version of an Amazon Lookout for Vision model. Starting a model takes a while to complete. To check the current state of the model, use &lt;a&gt;DescribeModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A model is ready to use when its status is &lt;code&gt;HOSTED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Once the model is running, you can detect custom labels in new images by calling &lt;a&gt;DetectAnomalies&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You are charged for the amount of time that the model is running. To stop a running model, call &lt;a&gt;StopModel&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:StartModel&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the model that you want to start.
    :type project_name: str
    :param model_version: The version of the model that you want to start.
    :type model_version: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;StartModel&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;StartModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;StartModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value. &lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple start requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;StartModel&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt;
    :type x_amzn_client_token: str

    """
    body = StartModelRequest.from_dict(body)
    return web.Response(status=200)


async def start_model_packaging_job(request: web.Request, project_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """start_model_packaging_job

    &lt;p&gt;Starts an Amazon Lookout for Vision model packaging job. A model packaging job creates an AWS IoT Greengrass component for a Lookout for Vision model. You can use the component to deploy your model to an edge device managed by Greengrass. &lt;/p&gt; &lt;p&gt;Use the &lt;a&gt;DescribeModelPackagingJob&lt;/a&gt; API to determine the current status of the job. The model packaging job is complete if the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;SUCCEEDED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To deploy the component to the target device, use the component name and component version with the AWS IoT Greengrass &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html\&quot;&gt;CreateDeployment&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;This operation requires the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;lookoutvision:StartModelPackagingJob&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:PutObject&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:GetBucketLocation&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;kms:GenerateDataKey&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;greengrass:CreateComponentVersion&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;greengrass:DescribeComponent&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) &lt;code&gt;greengrass:TagResource&lt;/code&gt;. Only required if you want to tag the component.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;i&gt;Using your Amazon Lookout for Vision model on an edge device&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt;

    :param project_name:  The name of the project which contains the version of the model that you want to package. 
    :type project_name: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;StartModelPackagingJob&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;StartModelPackagingJob&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;StartModelPackagingJob&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;StartModelPackagingJob&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt;
    :type x_amzn_client_token: str

    """
    body = StartModelPackagingJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_model(request: web.Request, project_name, model_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """stop_model

    &lt;p&gt;Stops the hosting of a running model. The operation might take a while to complete. To check the current status, call &lt;a&gt;DescribeModel&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;After the model hosting stops, the &lt;code&gt;Status&lt;/code&gt; of the model is &lt;code&gt;TRAINED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:StopModel&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the model that you want to stop.
    :type project_name: str
    :param model_version: The version of the model that you want to stop.
    :type model_version: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;StopModel&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;StopModel&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;StopModel&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple stop requests. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;StopModel&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt;
    :type x_amzn_client_token: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds one or more key-value tags to an Amazon Lookout for Vision model. For more information, see &lt;i&gt;Tagging a model&lt;/i&gt; in the &lt;i&gt;Amazon Lookout for Vision Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:TagResource&lt;/code&gt; operation.&lt;/p&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the model to assign the tags.
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

    &lt;p&gt;Removes one or more tags from an Amazon Lookout for Vision model. For more information, see &lt;i&gt;Tagging a model&lt;/i&gt; in the &lt;i&gt;Amazon Lookout for Vision Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:UntagResource&lt;/code&gt; operation.&lt;/p&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the model from which you want to remove tags. 
    :type resource_arn: str
    :param tag_keys: A list of the keys of the tags that you want to remove.
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


async def update_dataset_entries(request: web.Request, project_name, dataset_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """update_dataset_entries

    &lt;p&gt;Adds or updates one or more JSON Line entries in a dataset. A JSON Line includes information about an image used for training or testing an Amazon Lookout for Vision model.&lt;/p&gt; &lt;p&gt;To update an existing JSON Line, use the &lt;code&gt;source-ref&lt;/code&gt; field to identify the JSON Line. The JSON line that you supply replaces the existing JSON line. Any existing annotations that are not in the new JSON line are removed from the dataset. &lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Defining JSON lines for anomaly classification&lt;/i&gt; in the Amazon Lookout for Vision Developer Guide. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The images you reference in the &lt;code&gt;source-ref&lt;/code&gt; field of a JSON line, must be in the same S3 bucket as the existing images in the dataset. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updating a dataset might take a while to complete. To check the current status, call &lt;a&gt;DescribeDataset&lt;/a&gt; and check the &lt;code&gt;Status&lt;/code&gt; field in the response.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lookoutvision:UpdateDatasetEntries&lt;/code&gt; operation.&lt;/p&gt;

    :param project_name: The name of the project that contains the dataset that you want to update.
    :type project_name: str
    :param dataset_type: The type of the dataset that you want to update. Specify &lt;code&gt;train&lt;/code&gt; to update the training dataset. Specify &lt;code&gt;test&lt;/code&gt; to update the test dataset. If you have a single dataset project, specify &lt;code&gt;train&lt;/code&gt;.
    :type dataset_type: str
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
    :param x_amzn_client_token: &lt;p&gt;ClientToken is an idempotency token that ensures a call to &lt;code&gt;UpdateDatasetEntries&lt;/code&gt; completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from &lt;code&gt;UpdateDatasetEntries&lt;/code&gt;. In this case, safely retry your call to &lt;code&gt;UpdateDatasetEntries&lt;/code&gt; by using the same &lt;code&gt;ClientToken&lt;/code&gt; parameter value.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a value for &lt;code&gt;ClientToken&lt;/code&gt;, the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple updates with the same dataset entries. You&#39;ll need to provide your own value for other use cases. &lt;/p&gt; &lt;p&gt;An error occurs if the other input parameters are not the same as in the first request. Using a different value for &lt;code&gt;ClientToken&lt;/code&gt; is considered a new call to &lt;code&gt;UpdateDatasetEntries&lt;/code&gt;. An idempotency token is active for 8 hours. &lt;/p&gt;
    :type x_amzn_client_token: str

    """
    body = UpdateDatasetEntriesRequest.from_dict(body)
    return web.Response(status=200)
