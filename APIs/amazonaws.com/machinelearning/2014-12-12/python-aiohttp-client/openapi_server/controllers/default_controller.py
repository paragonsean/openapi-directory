from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tags_input import AddTagsInput
from openapi_server.models.add_tags_output import AddTagsOutput
from openapi_server.models.create_batch_prediction_input import CreateBatchPredictionInput
from openapi_server.models.create_batch_prediction_output import CreateBatchPredictionOutput
from openapi_server.models.create_data_source_from_rds_input import CreateDataSourceFromRDSInput
from openapi_server.models.create_data_source_from_rds_output import CreateDataSourceFromRDSOutput
from openapi_server.models.create_data_source_from_redshift_input import CreateDataSourceFromRedshiftInput
from openapi_server.models.create_data_source_from_redshift_output import CreateDataSourceFromRedshiftOutput
from openapi_server.models.create_data_source_from_s3_input import CreateDataSourceFromS3Input
from openapi_server.models.create_data_source_from_s3_output import CreateDataSourceFromS3Output
from openapi_server.models.create_evaluation_input import CreateEvaluationInput
from openapi_server.models.create_evaluation_output import CreateEvaluationOutput
from openapi_server.models.create_ml_model_input import CreateMLModelInput
from openapi_server.models.create_ml_model_output import CreateMLModelOutput
from openapi_server.models.create_realtime_endpoint_input import CreateRealtimeEndpointInput
from openapi_server.models.create_realtime_endpoint_output import CreateRealtimeEndpointOutput
from openapi_server.models.delete_batch_prediction_input import DeleteBatchPredictionInput
from openapi_server.models.delete_batch_prediction_output import DeleteBatchPredictionOutput
from openapi_server.models.delete_data_source_input import DeleteDataSourceInput
from openapi_server.models.delete_data_source_output import DeleteDataSourceOutput
from openapi_server.models.delete_evaluation_input import DeleteEvaluationInput
from openapi_server.models.delete_evaluation_output import DeleteEvaluationOutput
from openapi_server.models.delete_ml_model_input import DeleteMLModelInput
from openapi_server.models.delete_ml_model_output import DeleteMLModelOutput
from openapi_server.models.delete_realtime_endpoint_input import DeleteRealtimeEndpointInput
from openapi_server.models.delete_realtime_endpoint_output import DeleteRealtimeEndpointOutput
from openapi_server.models.delete_tags_input import DeleteTagsInput
from openapi_server.models.delete_tags_output import DeleteTagsOutput
from openapi_server.models.describe_batch_predictions_input import DescribeBatchPredictionsInput
from openapi_server.models.describe_batch_predictions_output import DescribeBatchPredictionsOutput
from openapi_server.models.describe_data_sources_input import DescribeDataSourcesInput
from openapi_server.models.describe_data_sources_output import DescribeDataSourcesOutput
from openapi_server.models.describe_evaluations_input import DescribeEvaluationsInput
from openapi_server.models.describe_evaluations_output import DescribeEvaluationsOutput
from openapi_server.models.describe_ml_models_input import DescribeMLModelsInput
from openapi_server.models.describe_ml_models_output import DescribeMLModelsOutput
from openapi_server.models.describe_tags_input import DescribeTagsInput
from openapi_server.models.describe_tags_output import DescribeTagsOutput
from openapi_server.models.get_batch_prediction_input import GetBatchPredictionInput
from openapi_server.models.get_batch_prediction_output import GetBatchPredictionOutput
from openapi_server.models.get_data_source_input import GetDataSourceInput
from openapi_server.models.get_data_source_output import GetDataSourceOutput
from openapi_server.models.get_evaluation_input import GetEvaluationInput
from openapi_server.models.get_evaluation_output import GetEvaluationOutput
from openapi_server.models.get_ml_model_input import GetMLModelInput
from openapi_server.models.get_ml_model_output import GetMLModelOutput
from openapi_server.models.predict_input import PredictInput
from openapi_server.models.predict_output import PredictOutput
from openapi_server.models.update_batch_prediction_input import UpdateBatchPredictionInput
from openapi_server.models.update_batch_prediction_output import UpdateBatchPredictionOutput
from openapi_server.models.update_data_source_input import UpdateDataSourceInput
from openapi_server.models.update_data_source_output import UpdateDataSourceOutput
from openapi_server.models.update_evaluation_input import UpdateEvaluationInput
from openapi_server.models.update_evaluation_output import UpdateEvaluationOutput
from openapi_server.models.update_ml_model_input import UpdateMLModelInput
from openapi_server.models.update_ml_model_output import UpdateMLModelOutput
from openapi_server import util


async def add_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags

    Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, &lt;code&gt;AddTags&lt;/code&gt; updates the tag&#39;s value.

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
    body = AddTagsInput.from_dict(body)
    return web.Response(status=200)


async def create_batch_prediction(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_batch_prediction

    &lt;p&gt;Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a &lt;code&gt;DataSource&lt;/code&gt;. This operation creates a new &lt;code&gt;BatchPrediction&lt;/code&gt;, and uses an &lt;code&gt;MLModel&lt;/code&gt; and the data files referenced by the &lt;code&gt;DataSource&lt;/code&gt; as information sources. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateBatchPrediction&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateBatchPrediction&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;BatchPrediction&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;BatchPrediction&lt;/code&gt; completes, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can poll for status updates by using the &lt;a&gt;GetBatchPrediction&lt;/a&gt; operation and checking the &lt;code&gt;Status&lt;/code&gt; parameter of the result. After the &lt;code&gt;COMPLETED&lt;/code&gt; status appears, the results are available in the location specified by the &lt;code&gt;OutputUri&lt;/code&gt; parameter.&lt;/p&gt;

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
    body = CreateBatchPredictionInput.from_dict(body)
    return web.Response(status=200)


async def create_data_source_from_rds(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_source_from_rds

    &lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; object from an &lt;a href&#x3D;\&quot;http://aws.amazon.com/rds/\&quot;&gt; Amazon Relational Database Service&lt;/a&gt; (Amazon RDS). A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; is created and ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in the &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state can be used only to perform &lt;code&gt;&amp;gt;CreateMLModel&lt;/code&gt;&amp;gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML cannot accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt;

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
    body = CreateDataSourceFromRDSInput.from_dict(body)
    return web.Response(status=200)


async def create_data_source_from_redshift(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_source_from_redshift

    &lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; from a database hosted on an Amazon Redshift cluster. A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform either &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; is created and ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; states can be used to perform only &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML can&#39;t accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt; &lt;p&gt;The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a &lt;code&gt;SelectSqlQuery&lt;/code&gt; query. Amazon ML executes an &lt;code&gt;Unload&lt;/code&gt; command in Amazon Redshift to transfer the result set of the &lt;code&gt;SelectSqlQuery&lt;/code&gt; query to &lt;code&gt;S3StagingLocation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After the &lt;code&gt;DataSource&lt;/code&gt; has been created, it&#39;s ready for use in evaluations and batch predictions. If you plan to use the &lt;code&gt;DataSource&lt;/code&gt; to train an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; also requires a recipe. A recipe describes how each input variable will be used in training an &lt;code&gt;MLModel&lt;/code&gt;. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.&lt;/p&gt; &lt;p&gt;You can&#39;t change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call &lt;code&gt;GetDataSource&lt;/code&gt; for an existing datasource and copy the values to a &lt;code&gt;CreateDataSource&lt;/code&gt; call. Change the settings that you want to change and make sure that all required fields have the appropriate values.&lt;/p&gt;

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
    body = CreateDataSourceFromRedshiftInput.from_dict(body)
    return web.Response(status=200)


async def create_data_source_from_s3(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_source_from_s3

    &lt;p&gt;Creates a &lt;code&gt;DataSource&lt;/code&gt; object. A &lt;code&gt;DataSource&lt;/code&gt; references data that can be used to perform &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt;, or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;DataSource&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;DataSource&lt;/code&gt; has been created and is ready for use, Amazon ML sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;code&gt;DataSource&lt;/code&gt; in the &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state can be used to perform only &lt;code&gt;CreateMLModel&lt;/code&gt;, &lt;code&gt;CreateEvaluation&lt;/code&gt; or &lt;code&gt;CreateBatchPrediction&lt;/code&gt; operations. &lt;/p&gt; &lt;p&gt; If Amazon ML can&#39;t accept the input source, it sets the &lt;code&gt;Status&lt;/code&gt; parameter to &lt;code&gt;FAILED&lt;/code&gt; and includes an error message in the &lt;code&gt;Message&lt;/code&gt; attribute of the &lt;code&gt;GetDataSource&lt;/code&gt; operation response. &lt;/p&gt; &lt;p&gt;The observation data used in a &lt;code&gt;DataSource&lt;/code&gt; should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the &lt;code&gt;DataSource&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;After the &lt;code&gt;DataSource&lt;/code&gt; has been created, it&#39;s ready to use in evaluations and batch predictions. If you plan to use the &lt;code&gt;DataSource&lt;/code&gt; to train an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; also needs a recipe. A recipe describes how each input variable will be used in training an &lt;code&gt;MLModel&lt;/code&gt;. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.&lt;/p&gt;

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
    body = CreateDataSourceFromS3Input.from_dict(body)
    return web.Response(status=200)


async def create_evaluation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_evaluation

    &lt;p&gt;Creates a new &lt;code&gt;Evaluation&lt;/code&gt; of an &lt;code&gt;MLModel&lt;/code&gt;. An &lt;code&gt;MLModel&lt;/code&gt; is evaluated on a set of observations associated to a &lt;code&gt;DataSource&lt;/code&gt;. Like a &lt;code&gt;DataSource&lt;/code&gt; for an &lt;code&gt;MLModel&lt;/code&gt;, the &lt;code&gt;DataSource&lt;/code&gt; for an &lt;code&gt;Evaluation&lt;/code&gt; contains values for the &lt;code&gt;Target Variable&lt;/code&gt;. The &lt;code&gt;Evaluation&lt;/code&gt; compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the &lt;code&gt;MLModel&lt;/code&gt; functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding &lt;code&gt;MLModelType&lt;/code&gt;: &lt;code&gt;BINARY&lt;/code&gt;, &lt;code&gt;REGRESSION&lt;/code&gt; or &lt;code&gt;MULTICLASS&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateEvaluation&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateEvaluation&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;Evaluation&lt;/code&gt; is created and ready for use, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to check progress of the evaluation during the creation operation.&lt;/p&gt;

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
    body = CreateEvaluationInput.from_dict(body)
    return web.Response(status=200)


async def create_ml_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_ml_model

    &lt;p&gt;Creates a new &lt;code&gt;MLModel&lt;/code&gt; using the &lt;code&gt;DataSource&lt;/code&gt; and the recipe as information sources. &lt;/p&gt; &lt;p&gt;An &lt;code&gt;MLModel&lt;/code&gt; is nearly immutable. Users can update only the &lt;code&gt;MLModelName&lt;/code&gt; and the &lt;code&gt;ScoreThreshold&lt;/code&gt; in an &lt;code&gt;MLModel&lt;/code&gt; without creating a new &lt;code&gt;MLModel&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMLModel&lt;/code&gt; is an asynchronous operation. In response to &lt;code&gt;CreateMLModel&lt;/code&gt;, Amazon Machine Learning (Amazon ML) immediately returns and sets the &lt;code&gt;MLModel&lt;/code&gt; status to &lt;code&gt;PENDING&lt;/code&gt;. After the &lt;code&gt;MLModel&lt;/code&gt; has been created and ready is for use, Amazon ML sets the status to &lt;code&gt;COMPLETED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to check the progress of the &lt;code&gt;MLModel&lt;/code&gt; during the creation operation.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMLModel&lt;/code&gt; requires a &lt;code&gt;DataSource&lt;/code&gt; with computed statistics, which can be created by setting &lt;code&gt;ComputeStatistics&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt; in &lt;code&gt;CreateDataSourceFromRDS&lt;/code&gt;, &lt;code&gt;CreateDataSourceFromS3&lt;/code&gt;, or &lt;code&gt;CreateDataSourceFromRedshift&lt;/code&gt; operations. &lt;/p&gt;

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
    body = CreateMLModelInput.from_dict(body)
    return web.Response(status=200)


async def create_realtime_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_realtime_endpoint

    Creates a real-time endpoint for the &lt;code&gt;MLModel&lt;/code&gt;. The endpoint contains the URI of the &lt;code&gt;MLModel&lt;/code&gt;; that is, the location to send real-time prediction requests for the specified &lt;code&gt;MLModel&lt;/code&gt;.

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
    body = CreateRealtimeEndpointInput.from_dict(body)
    return web.Response(status=200)


async def delete_batch_prediction(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_batch_prediction

    &lt;p&gt;Assigns the DELETED status to a &lt;code&gt;BatchPrediction&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteBatchPrediction&lt;/code&gt; operation, you can use the &lt;a&gt;GetBatchPrediction&lt;/a&gt; operation to verify that the status of the &lt;code&gt;BatchPrediction&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The result of the &lt;code&gt;DeleteBatchPrediction&lt;/code&gt; operation is irreversible.&lt;/p&gt;

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
    body = DeleteBatchPredictionInput.from_dict(body)
    return web.Response(status=200)


async def delete_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_data_source

    &lt;p&gt;Assigns the DELETED status to a &lt;code&gt;DataSource&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteDataSource&lt;/code&gt; operation, you can use the &lt;a&gt;GetDataSource&lt;/a&gt; operation to verify that the status of the &lt;code&gt;DataSource&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The results of the &lt;code&gt;DeleteDataSource&lt;/code&gt; operation are irreversible.&lt;/p&gt;

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
    body = DeleteDataSourceInput.from_dict(body)
    return web.Response(status=200)


async def delete_evaluation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_evaluation

    &lt;p&gt;Assigns the &lt;code&gt;DELETED&lt;/code&gt; status to an &lt;code&gt;Evaluation&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After invoking the &lt;code&gt;DeleteEvaluation&lt;/code&gt; operation, you can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to verify that the status of the &lt;code&gt;Evaluation&lt;/code&gt; changed to &lt;code&gt;DELETED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The results of the &lt;code&gt;DeleteEvaluation&lt;/code&gt; operation are irreversible.&lt;/p&gt;

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
    body = DeleteEvaluationInput.from_dict(body)
    return web.Response(status=200)


async def delete_ml_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_ml_model

    &lt;p&gt;Assigns the &lt;code&gt;DELETED&lt;/code&gt; status to an &lt;code&gt;MLModel&lt;/code&gt;, rendering it unusable.&lt;/p&gt; &lt;p&gt;After using the &lt;code&gt;DeleteMLModel&lt;/code&gt; operation, you can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to verify that the status of the &lt;code&gt;MLModel&lt;/code&gt; changed to DELETED.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Caution:&lt;/b&gt; The result of the &lt;code&gt;DeleteMLModel&lt;/code&gt; operation is irreversible.&lt;/p&gt;

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
    body = DeleteMLModelInput.from_dict(body)
    return web.Response(status=200)


async def delete_realtime_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_realtime_endpoint

    Deletes a real time endpoint of an &lt;code&gt;MLModel&lt;/code&gt;.

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
    body = DeleteRealtimeEndpointInput.from_dict(body)
    return web.Response(status=200)


async def delete_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tags

    &lt;p&gt;Deletes the specified tags associated with an ML object. After this operation is complete, you can&#39;t recover deleted tags.&lt;/p&gt; &lt;p&gt;If you specify a tag that doesn&#39;t exist, Amazon ML ignores it.&lt;/p&gt;

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
    body = DeleteTagsInput.from_dict(body)
    return web.Response(status=200)


async def describe_batch_predictions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_batch_predictions

    Returns a list of &lt;code&gt;BatchPrediction&lt;/code&gt; operations that match the search criteria in the request.

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
    :param limit: Pagination limit
    :type limit: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeBatchPredictionsInput.from_dict(body)
    return web.Response(status=200)


async def describe_data_sources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_data_sources

    Returns a list of &lt;code&gt;DataSource&lt;/code&gt; that match the search criteria in the request.

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
    :param limit: Pagination limit
    :type limit: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeDataSourcesInput.from_dict(body)
    return web.Response(status=200)


async def describe_evaluations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_evaluations

    Returns a list of &lt;code&gt;DescribeEvaluations&lt;/code&gt; that match the search criteria in the request.

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
    :param limit: Pagination limit
    :type limit: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeEvaluationsInput.from_dict(body)
    return web.Response(status=200)


async def describe_ml_models(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_ml_models

    Returns a list of &lt;code&gt;MLModel&lt;/code&gt; that match the search criteria in the request.

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
    :param limit: Pagination limit
    :type limit: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeMLModelsInput.from_dict(body)
    return web.Response(status=200)


async def describe_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tags

    Describes one or more of the tags for your Amazon ML object.

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
    body = DescribeTagsInput.from_dict(body)
    return web.Response(status=200)


async def get_batch_prediction(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_batch_prediction

    Returns a &lt;code&gt;BatchPrediction&lt;/code&gt; that includes detailed metadata, status, and data file information for a &lt;code&gt;Batch Prediction&lt;/code&gt; request.

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
    body = GetBatchPredictionInput.from_dict(body)
    return web.Response(status=200)


async def get_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_data_source

    &lt;p&gt;Returns a &lt;code&gt;DataSource&lt;/code&gt; that includes metadata and data file information, as well as the current status of the &lt;code&gt;DataSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDataSource&lt;/code&gt; provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.&lt;/p&gt;

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
    body = GetDataSourceInput.from_dict(body)
    return web.Response(status=200)


async def get_evaluation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_evaluation

    Returns an &lt;code&gt;Evaluation&lt;/code&gt; that includes metadata as well as the current status of the &lt;code&gt;Evaluation&lt;/code&gt;.

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
    body = GetEvaluationInput.from_dict(body)
    return web.Response(status=200)


async def get_ml_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_ml_model

    &lt;p&gt;Returns an &lt;code&gt;MLModel&lt;/code&gt; that includes detailed metadata, data source information, and the current status of the &lt;code&gt;MLModel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetMLModel&lt;/code&gt; provides results in normal or verbose format. &lt;/p&gt;

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
    body = GetMLModelInput.from_dict(body)
    return web.Response(status=200)


async def predict(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """predict

    &lt;p&gt;Generates a prediction for the observation using the specified &lt;code&gt;ML Model&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Note:&lt;/b&gt; Not all response parameters will be populated. Whether a response parameter is populated depends on the type of model requested.&lt;/p&gt;

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
    body = PredictInput.from_dict(body)
    return web.Response(status=200)


async def update_batch_prediction(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_batch_prediction

    &lt;p&gt;Updates the &lt;code&gt;BatchPredictionName&lt;/code&gt; of a &lt;code&gt;BatchPrediction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetBatchPrediction&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    body = UpdateBatchPredictionInput.from_dict(body)
    return web.Response(status=200)


async def update_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_data_source

    &lt;p&gt;Updates the &lt;code&gt;DataSourceName&lt;/code&gt; of a &lt;code&gt;DataSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetDataSource&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    body = UpdateDataSourceInput.from_dict(body)
    return web.Response(status=200)


async def update_evaluation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_evaluation

    &lt;p&gt;Updates the &lt;code&gt;EvaluationName&lt;/code&gt; of an &lt;code&gt;Evaluation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetEvaluation&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    body = UpdateEvaluationInput.from_dict(body)
    return web.Response(status=200)


async def update_ml_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_ml_model

    &lt;p&gt;Updates the &lt;code&gt;MLModelName&lt;/code&gt; and the &lt;code&gt;ScoreThreshold&lt;/code&gt; of an &lt;code&gt;MLModel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetMLModel&lt;/code&gt; operation to view the contents of the updated data element.&lt;/p&gt;

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
    body = UpdateMLModelInput.from_dict(body)
    return web.Response(status=200)
