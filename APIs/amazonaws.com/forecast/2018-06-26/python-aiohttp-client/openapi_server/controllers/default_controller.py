from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_auto_predictor_request import CreateAutoPredictorRequest
from openapi_server.models.create_auto_predictor_response import CreateAutoPredictorResponse
from openapi_server.models.create_dataset_group_request import CreateDatasetGroupRequest
from openapi_server.models.create_dataset_group_response import CreateDatasetGroupResponse
from openapi_server.models.create_dataset_import_job_request import CreateDatasetImportJobRequest
from openapi_server.models.create_dataset_import_job_response import CreateDatasetImportJobResponse
from openapi_server.models.create_dataset_request import CreateDatasetRequest
from openapi_server.models.create_dataset_response import CreateDatasetResponse
from openapi_server.models.create_explainability_export_request import CreateExplainabilityExportRequest
from openapi_server.models.create_explainability_export_response import CreateExplainabilityExportResponse
from openapi_server.models.create_explainability_request import CreateExplainabilityRequest
from openapi_server.models.create_explainability_response import CreateExplainabilityResponse
from openapi_server.models.create_forecast_export_job_request import CreateForecastExportJobRequest
from openapi_server.models.create_forecast_export_job_response import CreateForecastExportJobResponse
from openapi_server.models.create_forecast_request import CreateForecastRequest
from openapi_server.models.create_forecast_response import CreateForecastResponse
from openapi_server.models.create_monitor_request import CreateMonitorRequest
from openapi_server.models.create_monitor_response import CreateMonitorResponse
from openapi_server.models.create_predictor_backtest_export_job_request import CreatePredictorBacktestExportJobRequest
from openapi_server.models.create_predictor_backtest_export_job_response import CreatePredictorBacktestExportJobResponse
from openapi_server.models.create_predictor_request import CreatePredictorRequest
from openapi_server.models.create_predictor_response import CreatePredictorResponse
from openapi_server.models.create_what_if_analysis_request import CreateWhatIfAnalysisRequest
from openapi_server.models.create_what_if_analysis_response import CreateWhatIfAnalysisResponse
from openapi_server.models.create_what_if_forecast_export_request import CreateWhatIfForecastExportRequest
from openapi_server.models.create_what_if_forecast_export_response import CreateWhatIfForecastExportResponse
from openapi_server.models.create_what_if_forecast_request import CreateWhatIfForecastRequest
from openapi_server.models.create_what_if_forecast_response import CreateWhatIfForecastResponse
from openapi_server.models.delete_dataset_group_request import DeleteDatasetGroupRequest
from openapi_server.models.delete_dataset_import_job_request import DeleteDatasetImportJobRequest
from openapi_server.models.delete_dataset_request import DeleteDatasetRequest
from openapi_server.models.delete_explainability_export_request import DeleteExplainabilityExportRequest
from openapi_server.models.delete_explainability_request import DeleteExplainabilityRequest
from openapi_server.models.delete_forecast_export_job_request import DeleteForecastExportJobRequest
from openapi_server.models.delete_forecast_request import DeleteForecastRequest
from openapi_server.models.delete_monitor_request import DeleteMonitorRequest
from openapi_server.models.delete_predictor_backtest_export_job_request import DeletePredictorBacktestExportJobRequest
from openapi_server.models.delete_predictor_request import DeletePredictorRequest
from openapi_server.models.delete_resource_tree_request import DeleteResourceTreeRequest
from openapi_server.models.delete_what_if_analysis_request import DeleteWhatIfAnalysisRequest
from openapi_server.models.delete_what_if_forecast_export_request import DeleteWhatIfForecastExportRequest
from openapi_server.models.delete_what_if_forecast_request import DeleteWhatIfForecastRequest
from openapi_server.models.describe_auto_predictor_request import DescribeAutoPredictorRequest
from openapi_server.models.describe_auto_predictor_response import DescribeAutoPredictorResponse
from openapi_server.models.describe_dataset_group_request import DescribeDatasetGroupRequest
from openapi_server.models.describe_dataset_group_response import DescribeDatasetGroupResponse
from openapi_server.models.describe_dataset_import_job_request import DescribeDatasetImportJobRequest
from openapi_server.models.describe_dataset_import_job_response import DescribeDatasetImportJobResponse
from openapi_server.models.describe_dataset_request import DescribeDatasetRequest
from openapi_server.models.describe_dataset_response import DescribeDatasetResponse
from openapi_server.models.describe_explainability_export_request import DescribeExplainabilityExportRequest
from openapi_server.models.describe_explainability_export_response import DescribeExplainabilityExportResponse
from openapi_server.models.describe_explainability_request import DescribeExplainabilityRequest
from openapi_server.models.describe_explainability_response import DescribeExplainabilityResponse
from openapi_server.models.describe_forecast_export_job_request import DescribeForecastExportJobRequest
from openapi_server.models.describe_forecast_export_job_response import DescribeForecastExportJobResponse
from openapi_server.models.describe_forecast_request import DescribeForecastRequest
from openapi_server.models.describe_forecast_response import DescribeForecastResponse
from openapi_server.models.describe_monitor_request import DescribeMonitorRequest
from openapi_server.models.describe_monitor_response import DescribeMonitorResponse
from openapi_server.models.describe_predictor_backtest_export_job_request import DescribePredictorBacktestExportJobRequest
from openapi_server.models.describe_predictor_backtest_export_job_response import DescribePredictorBacktestExportJobResponse
from openapi_server.models.describe_predictor_request import DescribePredictorRequest
from openapi_server.models.describe_predictor_response import DescribePredictorResponse
from openapi_server.models.describe_what_if_analysis_request import DescribeWhatIfAnalysisRequest
from openapi_server.models.describe_what_if_analysis_response import DescribeWhatIfAnalysisResponse
from openapi_server.models.describe_what_if_forecast_export_request import DescribeWhatIfForecastExportRequest
from openapi_server.models.describe_what_if_forecast_export_response import DescribeWhatIfForecastExportResponse
from openapi_server.models.describe_what_if_forecast_request import DescribeWhatIfForecastRequest
from openapi_server.models.describe_what_if_forecast_response import DescribeWhatIfForecastResponse
from openapi_server.models.get_accuracy_metrics_request import GetAccuracyMetricsRequest
from openapi_server.models.get_accuracy_metrics_response import GetAccuracyMetricsResponse
from openapi_server.models.list_dataset_groups_request import ListDatasetGroupsRequest
from openapi_server.models.list_dataset_groups_response import ListDatasetGroupsResponse
from openapi_server.models.list_dataset_import_jobs_request import ListDatasetImportJobsRequest
from openapi_server.models.list_dataset_import_jobs_response import ListDatasetImportJobsResponse
from openapi_server.models.list_datasets_request import ListDatasetsRequest
from openapi_server.models.list_datasets_response import ListDatasetsResponse
from openapi_server.models.list_explainabilities_request import ListExplainabilitiesRequest
from openapi_server.models.list_explainabilities_response import ListExplainabilitiesResponse
from openapi_server.models.list_explainability_exports_request import ListExplainabilityExportsRequest
from openapi_server.models.list_explainability_exports_response import ListExplainabilityExportsResponse
from openapi_server.models.list_forecast_export_jobs_request import ListForecastExportJobsRequest
from openapi_server.models.list_forecast_export_jobs_response import ListForecastExportJobsResponse
from openapi_server.models.list_forecasts_request import ListForecastsRequest
from openapi_server.models.list_forecasts_response import ListForecastsResponse
from openapi_server.models.list_monitor_evaluations_request import ListMonitorEvaluationsRequest
from openapi_server.models.list_monitor_evaluations_response import ListMonitorEvaluationsResponse
from openapi_server.models.list_monitors_request import ListMonitorsRequest
from openapi_server.models.list_monitors_response import ListMonitorsResponse
from openapi_server.models.list_predictor_backtest_export_jobs_request import ListPredictorBacktestExportJobsRequest
from openapi_server.models.list_predictor_backtest_export_jobs_response import ListPredictorBacktestExportJobsResponse
from openapi_server.models.list_predictors_request import ListPredictorsRequest
from openapi_server.models.list_predictors_response import ListPredictorsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_what_if_analyses_request import ListWhatIfAnalysesRequest
from openapi_server.models.list_what_if_analyses_response import ListWhatIfAnalysesResponse
from openapi_server.models.list_what_if_forecast_exports_request import ListWhatIfForecastExportsRequest
from openapi_server.models.list_what_if_forecast_exports_response import ListWhatIfForecastExportsResponse
from openapi_server.models.list_what_if_forecasts_request import ListWhatIfForecastsRequest
from openapi_server.models.list_what_if_forecasts_response import ListWhatIfForecastsResponse
from openapi_server.models.resume_resource_request import ResumeResourceRequest
from openapi_server.models.stop_resource_request import StopResourceRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_dataset_group_request import UpdateDatasetGroupRequest
from openapi_server import util


async def create_auto_predictor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_auto_predictor

    &lt;p&gt;Creates an Amazon Forecast predictor.&lt;/p&gt; &lt;p&gt;Amazon Forecast creates predictors with AutoPredictor, which involves applying the optimal combination of algorithms to each time series in your datasets. You can use &lt;a&gt;CreateAutoPredictor&lt;/a&gt; to create new predictors or upgrade/retrain existing predictors.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Creating new predictors&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The following parameters are required when creating a new predictor:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PredictorName&lt;/code&gt; - A unique name for the predictor.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DatasetGroupArn&lt;/code&gt; - The ARN of the dataset group used to train the predictor.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ForecastFrequency&lt;/code&gt; - The granularity of your forecasts (hourly, daily, weekly, etc).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ForecastHorizon&lt;/code&gt; - The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When creating a new predictor, do not specify a value for &lt;code&gt;ReferencePredictorArn&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Upgrading and retraining predictors&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The following parameters are required when retraining or upgrading a predictor:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PredictorName&lt;/code&gt; - A unique name for the predictor.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ReferencePredictorArn&lt;/code&gt; - The ARN of the predictor to retrain or upgrade.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When upgrading or retraining a predictor, only specify values for the &lt;code&gt;ReferencePredictorArn&lt;/code&gt; and &lt;code&gt;PredictorName&lt;/code&gt;. &lt;/p&gt;

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
    body = CreateAutoPredictorRequest.from_dict(body)
    return web.Response(status=200)


async def create_dataset(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_dataset

    &lt;p&gt;Creates an Amazon Forecast dataset. The information about the dataset that you provide helps Forecast understand how to consume the data for model training. This includes the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt; &lt;code&gt;DataFrequency&lt;/code&gt; &lt;/i&gt; - How frequently your historical time-series data is collected.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt; &lt;code&gt;Domain&lt;/code&gt; &lt;/i&gt; and &lt;i&gt; &lt;code&gt;DatasetType&lt;/code&gt; &lt;/i&gt; - Each dataset has an associated dataset domain and a type within the domain. Amazon Forecast provides a list of predefined domains and types within each domain. For each unique dataset domain and type within the domain, Amazon Forecast requires your data to include a minimum set of predefined fields.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt; &lt;code&gt;Schema&lt;/code&gt; &lt;/i&gt; - A schema specifies the fields in the dataset, including the field name and data type.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After creating a dataset, you import your training data into it and add the dataset to a dataset group. You use the dataset group to create a predictor. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html\&quot;&gt;Importing datasets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To get a list of all your datasets, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasets.html\&quot;&gt;ListDatasets&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;For example Forecast datasets, see the &lt;a href&#x3D;\&quot;https://github.com/aws-samples/amazon-forecast-samples\&quot;&gt;Amazon Forecast Sample GitHub repository&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of a dataset must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can import training data. Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html\&quot;&gt;DescribeDataset&lt;/a&gt; operation to get the status.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateDatasetRequest.from_dict(body)
    return web.Response(status=200)


async def create_dataset_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_dataset_group

    &lt;p&gt;Creates a dataset group, which holds a collection of related datasets. You can add datasets to the dataset group when you create the dataset group, or later by using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html\&quot;&gt;UpdateDatasetGroup&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;After creating a dataset group and adding datasets, you use the dataset group when you create a predictor. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html\&quot;&gt;Dataset groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To get a list of all your datasets groups, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetGroups.html\&quot;&gt;ListDatasetGroups&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of a dataset group must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can use the dataset group to create a predictor. To get the status, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html\&quot;&gt;DescribeDatasetGroup&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateDatasetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_dataset_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_dataset_import_job

    &lt;p&gt;Imports your training data to an Amazon Forecast dataset. You provide the location of your training data in an Amazon Simple Storage Service (Amazon S3) bucket and the Amazon Resource Name (ARN) of the dataset that you want to import the data to.&lt;/p&gt; &lt;p&gt;You must specify a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DataSource.html\&quot;&gt;DataSource&lt;/a&gt; object that includes an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data, as Amazon Forecast makes a copy of your data and processes it in an internal Amazon Web Services system. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-iam-roles.html\&quot;&gt;Set up permissions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The training data must be in CSV or Parquet format. The delimiter must be a comma (,).&lt;/p&gt; &lt;p&gt;You can specify the path to a specific file, the S3 bucket, or to a folder in the S3 bucket. For the latter two cases, Amazon Forecast imports all files up to the limit of 10,000 files.&lt;/p&gt; &lt;p&gt;Because dataset imports are not aggregated, your most recent dataset import is the one that is used when training a predictor or generating a forecast. Make sure that your most recent dataset import contains all of the data you want to model off of, and not just the new data collected since the previous import.&lt;/p&gt; &lt;p&gt;To get a list of all your dataset import jobs, filtered by specified criteria, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetImportJobs.html\&quot;&gt;ListDatasetImportJobs&lt;/a&gt; operation.&lt;/p&gt;

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
    body = CreateDatasetImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_explainability(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_explainability

    &lt;note&gt; &lt;p&gt;Explainability is only available for Forecasts and Predictors generated from an AutoPredictor (&lt;a&gt;CreateAutoPredictor&lt;/a&gt;)&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates an Amazon Forecast Explainability.&lt;/p&gt; &lt;p&gt;Explainability helps you better understand how the attributes in your datasets impact forecast. Amazon Forecast uses a metric called Impact scores to quantify the relative impact of each attribute and determine whether they increase or decrease forecast values.&lt;/p&gt; &lt;p&gt;To enable Forecast Explainability, your predictor must include at least one of the following: related time series, item metadata, or additional datasets like Holidays and the Weather Index.&lt;/p&gt; &lt;p&gt;CreateExplainability accepts either a Predictor ARN or Forecast ARN. To receive aggregated Impact scores for all time series and time points in your datasets, provide a Predictor ARN. To receive Impact scores for specific time series and time points, provide a Forecast ARN.&lt;/p&gt; &lt;p&gt; &lt;b&gt;CreateExplainability with a Predictor ARN&lt;/b&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can only have one Explainability resource per predictor. If you already enabled &lt;code&gt;ExplainPredictor&lt;/code&gt; in &lt;a&gt;CreateAutoPredictor&lt;/a&gt;, that predictor already has an Explainability resource.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The following parameters are required when providing a Predictor ARN:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ExplainabilityName&lt;/code&gt; - A unique name for the Explainability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ResourceArn&lt;/code&gt; - The Arn of the predictor.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TimePointGranularity&lt;/code&gt; - Must be set to “ALL”.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TimeSeriesGranularity&lt;/code&gt; - Must be set to “ALL”.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Do not specify a value for the following parameters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DataSource&lt;/code&gt; - Only valid when TimeSeriesGranularity is “SPECIFIC”.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Schema&lt;/code&gt; - Only valid when TimeSeriesGranularity is “SPECIFIC”.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StartDateTime&lt;/code&gt; - Only valid when TimePointGranularity is “SPECIFIC”.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EndDateTime&lt;/code&gt; - Only valid when TimePointGranularity is “SPECIFIC”.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;CreateExplainability with a Forecast ARN&lt;/b&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can specify a maximum of 50 time series and 500 time points.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The following parameters are required when providing a Predictor ARN:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ExplainabilityName&lt;/code&gt; - A unique name for the Explainability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ResourceArn&lt;/code&gt; - The Arn of the forecast.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TimePointGranularity&lt;/code&gt; - Either “ALL” or “SPECIFIC”.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TimeSeriesGranularity&lt;/code&gt; - Either “ALL” or “SPECIFIC”.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you set TimeSeriesGranularity to “SPECIFIC”, you must also provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DataSource&lt;/code&gt; - The S3 location of the CSV file specifying your time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Schema&lt;/code&gt; - The Schema defines the attributes and attribute types listed in the Data Source.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you set TimePointGranularity to “SPECIFIC”, you must also provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StartDateTime&lt;/code&gt; - The first timestamp in the range of time points.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EndDateTime&lt;/code&gt; - The last timestamp in the range of time points.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateExplainabilityRequest.from_dict(body)
    return web.Response(status=200)


async def create_explainability_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_explainability_export

    &lt;p&gt;Exports an Explainability resource created by the &lt;a&gt;CreateExplainability&lt;/a&gt; operation. Exported files are exported to an Amazon Simple Storage Service (Amazon S3) bucket.&lt;/p&gt; &lt;p&gt;You must specify a &lt;a&gt;DataDestination&lt;/a&gt; object that includes an Amazon S3 bucket and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see &lt;a&gt;aws-forecast-iam-roles&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of the export job must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can access the export in your Amazon S3 bucket. To get the status, use the &lt;a&gt;DescribeExplainabilityExport&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateExplainabilityExportRequest.from_dict(body)
    return web.Response(status=200)


async def create_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_forecast

    &lt;p&gt;Creates a forecast for each item in the &lt;code&gt;TARGET_TIME_SERIES&lt;/code&gt; dataset that was used to train the predictor. This is known as inference. To retrieve the forecast for a single item at low latency, use the operation. To export the complete forecast into your Amazon Simple Storage Service (Amazon S3) bucket, use the &lt;a&gt;CreateForecastExportJob&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;The range of the forecast is determined by the &lt;code&gt;ForecastHorizon&lt;/code&gt; value, which you specify in the &lt;a&gt;CreatePredictor&lt;/a&gt; request. When you query a forecast, you can request a specific date range within the forecast.&lt;/p&gt; &lt;p&gt;To get a list of all your forecasts, use the &lt;a&gt;ListForecasts&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The forecasts generated by Amazon Forecast are in the same time zone as the dataset that was used to create the predictor.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;a&gt;howitworks-forecast&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of the forecast must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can query or export the forecast. Use the &lt;a&gt;DescribeForecast&lt;/a&gt; operation to get the status.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;By default, a forecast includes predictions for every item (&lt;code&gt;item_id&lt;/code&gt;) in the dataset group that was used to train the predictor. However, you can use the &lt;code&gt;TimeSeriesSelector&lt;/code&gt; object to generate a forecast on a subset of time series. Forecast creation is skipped for any time series that you specify that are not in the input dataset. The forecast export file will not contain these time series or their forecasted values.&lt;/p&gt;

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
    body = CreateForecastRequest.from_dict(body)
    return web.Response(status=200)


async def create_forecast_export_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_forecast_export_job

    &lt;p&gt;Exports a forecast created by the &lt;a&gt;CreateForecast&lt;/a&gt; operation to your Amazon Simple Storage Service (Amazon S3) bucket. The forecast file name will match the following conventions:&lt;/p&gt; &lt;p&gt;&amp;lt;ForecastExportJobName&amp;gt;_&amp;lt;ExportTimestamp&amp;gt;_&amp;lt;PartNumber&amp;gt;&lt;/p&gt; &lt;p&gt;where the &amp;lt;ExportTimestamp&amp;gt; component is in Java SimpleDateFormat (yyyy-MM-ddTHH-mm-ssZ).&lt;/p&gt; &lt;p&gt;You must specify a &lt;a&gt;DataDestination&lt;/a&gt; object that includes an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see &lt;a&gt;aws-forecast-iam-roles&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a&gt;howitworks-forecast&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To get a list of all your forecast export jobs, use the &lt;a&gt;ListForecastExportJobs&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of the forecast export job must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can access the forecast in your Amazon S3 bucket. To get the status, use the &lt;a&gt;DescribeForecastExportJob&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateForecastExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_monitor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_monitor

    Creates a predictor monitor resource for an existing auto predictor. Predictor monitoring allows you to see how your predictor&#39;s performance changes over time. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html\&quot;&gt;Predictor Monitoring&lt;/a&gt;. 

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
    body = CreateMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def create_predictor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_predictor

    &lt;note&gt; &lt;p&gt; This operation creates a legacy predictor that does not include all the predictor functionalities provided by Amazon Forecast. To create a predictor that is compatible with all aspects of Forecast, use &lt;a&gt;CreateAutoPredictor&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates an Amazon Forecast predictor.&lt;/p&gt; &lt;p&gt;In the request, provide a dataset group and either specify an algorithm or let Amazon Forecast choose an algorithm for you using AutoML. If you specify an algorithm, you also can override algorithm-specific hyperparameters.&lt;/p&gt; &lt;p&gt;Amazon Forecast uses the algorithm to train a predictor using the latest version of the datasets in the specified dataset group. You can then generate a forecast using the &lt;a&gt;CreateForecast&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; To see the evaluation metrics, use the &lt;a&gt;GetAccuracyMetrics&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;You can specify a featurization configuration to fill and aggregate the data fields in the &lt;code&gt;TARGET_TIME_SERIES&lt;/code&gt; dataset to improve model training. For more information, see &lt;a&gt;FeaturizationConfig&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For RELATED_TIME_SERIES datasets, &lt;code&gt;CreatePredictor&lt;/code&gt; verifies that the &lt;code&gt;DataFrequency&lt;/code&gt; specified when the dataset was created matches the &lt;code&gt;ForecastFrequency&lt;/code&gt;. TARGET_TIME_SERIES datasets don&#39;t have this restriction. Amazon Forecast also verifies the delimiter and timestamp format. For more information, see &lt;a&gt;howitworks-datasets-groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;By default, predictors are trained and evaluated at the 0.1 (P10), 0.5 (P50), and 0.9 (P90) quantiles. You can choose custom forecast types to train and evaluate your predictor by setting the &lt;code&gt;ForecastTypes&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;AutoML&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If you want Amazon Forecast to evaluate each algorithm and choose the one that minimizes the &lt;code&gt;objective function&lt;/code&gt;, set &lt;code&gt;PerformAutoML&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;. The &lt;code&gt;objective function&lt;/code&gt; is defined as the mean of the weighted losses over the forecast types. By default, these are the p10, p50, and p90 quantile losses. For more information, see &lt;a&gt;EvaluationResult&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When AutoML is enabled, the following properties are disallowed:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AlgorithmArn&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HPOConfig&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PerformHPO&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TrainingParameters&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get a list of all of your predictors, use the &lt;a&gt;ListPredictors&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can use the predictor to create a forecast, the &lt;code&gt;Status&lt;/code&gt; of the predictor must be &lt;code&gt;ACTIVE&lt;/code&gt;, signifying that training has completed. To get the status, use the &lt;a&gt;DescribePredictor&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreatePredictorRequest.from_dict(body)
    return web.Response(status=200)


async def create_predictor_backtest_export_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_predictor_backtest_export_job

    &lt;p&gt;Exports backtest forecasts and accuracy metrics generated by the &lt;a&gt;CreateAutoPredictor&lt;/a&gt; or &lt;a&gt;CreatePredictor&lt;/a&gt; operations. Two folders containing CSV or Parquet files are exported to your specified S3 bucket.&lt;/p&gt; &lt;p&gt; The export file names will match the following conventions:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&amp;lt;ExportJobName&amp;gt;_&amp;lt;ExportTimestamp&amp;gt;_&amp;lt;PartNumber&amp;gt;.csv&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The &amp;lt;ExportTimestamp&amp;gt; component is in Java SimpleDate format (yyyy-MM-ddTHH-mm-ssZ).&lt;/p&gt; &lt;p&gt;You must specify a &lt;a&gt;DataDestination&lt;/a&gt; object that includes an Amazon S3 bucket and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see &lt;a&gt;aws-forecast-iam-roles&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of the export job must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can access the export in your Amazon S3 bucket. To get the status, use the &lt;a&gt;DescribePredictorBacktestExportJob&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreatePredictorBacktestExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_what_if_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_what_if_analysis

    &lt;p&gt;What-if analysis is a scenario modeling technique where you make a hypothetical change to a time series and compare the forecasts generated by these changes against the baseline, unchanged time series. It is important to remember that the purpose of a what-if analysis is to understand how a forecast can change given different modifications to the baseline time series.&lt;/p&gt; &lt;p&gt;For example, imagine you are a clothing retailer who is considering an end of season sale to clear space for new styles. After creating a baseline forecast, you can use a what-if analysis to investigate how different sales tactics might affect your goals.&lt;/p&gt; &lt;p&gt;You could create a scenario where everything is given a 25% markdown, and another where everything is given a fixed dollar markdown. You could create a scenario where the sale lasts for one week and another where the sale lasts for one month. With a what-if analysis, you can compare many different scenarios against each other.&lt;/p&gt; &lt;p&gt;Note that a what-if analysis is meant to display what the forecasting model has learned and how it will behave in the scenarios that you are evaluating. Do not blindly use the results of the what-if analysis to make business decisions. For instance, forecasts might not be accurate for novel scenarios where there is no reference available to determine whether a forecast is good.&lt;/p&gt; &lt;p&gt;The &lt;a&gt;TimeSeriesSelector&lt;/a&gt; object defines the items that you want in the what-if analysis.&lt;/p&gt;

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
    body = CreateWhatIfAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def create_what_if_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_what_if_forecast

    A what-if forecast is a forecast that is created from a modified version of the baseline forecast. Each what-if forecast incorporates either a replacement dataset or a set of transformations to the original dataset. 

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
    body = CreateWhatIfForecastRequest.from_dict(body)
    return web.Response(status=200)


async def create_what_if_forecast_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_what_if_forecast_export

    &lt;p&gt;Exports a forecast created by the &lt;a&gt;CreateWhatIfForecast&lt;/a&gt; operation to your Amazon Simple Storage Service (Amazon S3) bucket. The forecast file name will match the following conventions:&lt;/p&gt; &lt;p&gt; &lt;code&gt;≈&amp;lt;ForecastExportJobName&amp;gt;_&amp;lt;ExportTimestamp&amp;gt;_&amp;lt;PartNumber&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The &amp;lt;ExportTimestamp&amp;gt; component is in Java SimpleDateFormat (yyyy-MM-ddTHH-mm-ssZ).&lt;/p&gt; &lt;p&gt;You must specify a &lt;a&gt;DataDestination&lt;/a&gt; object that includes an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see &lt;a&gt;aws-forecast-iam-roles&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a&gt;howitworks-forecast&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To get a list of all your what-if forecast export jobs, use the &lt;a&gt;ListWhatIfForecastExports&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of the forecast export job must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can access the forecast in your Amazon S3 bucket. To get the status, use the &lt;a&gt;DescribeWhatIfForecastExport&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateWhatIfForecastExportRequest.from_dict(body)
    return web.Response(status=200)


async def delete_dataset(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_dataset

    &lt;p&gt;Deletes an Amazon Forecast dataset that was created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html\&quot;&gt;CreateDataset&lt;/a&gt; operation. You can only delete datasets that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html\&quot;&gt;DescribeDataset&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Forecast does not automatically update any dataset groups that contain the deleted dataset. In order to update the dataset group, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html\&quot;&gt;UpdateDatasetGroup&lt;/a&gt; operation, omitting the deleted dataset&#39;s ARN.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteDatasetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_dataset_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_dataset_group

    &lt;p&gt;Deletes a dataset group created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html\&quot;&gt;CreateDatasetGroup&lt;/a&gt; operation. You can only delete dataset groups that have a status of &lt;code&gt;ACTIVE&lt;/code&gt;, &lt;code&gt;CREATE_FAILED&lt;/code&gt;, or &lt;code&gt;UPDATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html\&quot;&gt;DescribeDatasetGroup&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This operation deletes only the dataset group, not the datasets in the group.&lt;/p&gt;

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
    body = DeleteDatasetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_dataset_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_dataset_import_job

    Deletes a dataset import job created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html\&quot;&gt;CreateDatasetImportJob&lt;/a&gt; operation. You can delete only dataset import jobs that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html\&quot;&gt;DescribeDatasetImportJob&lt;/a&gt; operation.

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
    body = DeleteDatasetImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def delete_explainability(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_explainability

    &lt;p&gt;Deletes an Explainability resource.&lt;/p&gt; &lt;p&gt;You can delete only predictor that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribeExplainability&lt;/a&gt; operation.&lt;/p&gt;

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
    body = DeleteExplainabilityRequest.from_dict(body)
    return web.Response(status=200)


async def delete_explainability_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_explainability_export

    Deletes an Explainability export.

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
    body = DeleteExplainabilityExportRequest.from_dict(body)
    return web.Response(status=200)


async def delete_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_forecast

    &lt;p&gt;Deletes a forecast created using the &lt;a&gt;CreateForecast&lt;/a&gt; operation. You can delete only forecasts that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribeForecast&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a forecast while it is being exported. After a forecast is deleted, you can no longer query the forecast.&lt;/p&gt;

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
    body = DeleteForecastRequest.from_dict(body)
    return web.Response(status=200)


async def delete_forecast_export_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_forecast_export_job

    Deletes a forecast export job created using the &lt;a&gt;CreateForecastExportJob&lt;/a&gt; operation. You can delete only export jobs that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribeForecastExportJob&lt;/a&gt; operation.

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
    body = DeleteForecastExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def delete_monitor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_monitor

    Deletes a monitor resource. You can only delete a monitor resource with a status of &lt;code&gt;ACTIVE&lt;/code&gt;, &lt;code&gt;ACTIVE_STOPPED&lt;/code&gt;, &lt;code&gt;CREATE_FAILED&lt;/code&gt;, or &lt;code&gt;CREATE_STOPPED&lt;/code&gt;.

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
    body = DeleteMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_predictor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_predictor

    Deletes a predictor created using the &lt;a&gt;DescribePredictor&lt;/a&gt; or &lt;a&gt;CreatePredictor&lt;/a&gt; operations. You can delete only predictor that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribePredictor&lt;/a&gt; operation.

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
    body = DeletePredictorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_predictor_backtest_export_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_predictor_backtest_export_job

    Deletes a predictor backtest export job.

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
    body = DeletePredictorBacktestExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_tree(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_tree

    &lt;p&gt;Deletes an entire resource tree. This operation will delete the parent resource and its child resources.&lt;/p&gt; &lt;p&gt;Child resources are resources that were created from another resource. For example, when a forecast is generated from a predictor, the forecast is the child resource and the predictor is the parent resource.&lt;/p&gt; &lt;p&gt;Amazon Forecast resources possess the following parent-child resource hierarchies:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Dataset&lt;/b&gt;: dataset import jobs&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Dataset Group&lt;/b&gt;: predictors, predictor backtest export jobs, forecasts, forecast export jobs&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Predictor&lt;/b&gt;: predictor backtest export jobs, forecasts, forecast export jobs&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Forecast&lt;/b&gt;: forecast export jobs&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;DeleteResourceTree&lt;/code&gt; will only delete Amazon Forecast resources, and will not delete datasets or exported files stored in Amazon S3. &lt;/p&gt; &lt;/note&gt;

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
    body = DeleteResourceTreeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_what_if_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_what_if_analysis

    &lt;p&gt;Deletes a what-if analysis created using the &lt;a&gt;CreateWhatIfAnalysis&lt;/a&gt; operation. You can delete only what-if analyses that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribeWhatIfAnalysis&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;You can&#39;t delete a what-if analysis while any of its forecasts are being exported.&lt;/p&gt;

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
    body = DeleteWhatIfAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def delete_what_if_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_what_if_forecast

    &lt;p&gt;Deletes a what-if forecast created using the &lt;a&gt;CreateWhatIfForecast&lt;/a&gt; operation. You can delete only what-if forecasts that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribeWhatIfForecast&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;You can&#39;t delete a what-if forecast while it is being exported. After a what-if forecast is deleted, you can no longer query the what-if analysis.&lt;/p&gt;

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
    body = DeleteWhatIfForecastRequest.from_dict(body)
    return web.Response(status=200)


async def delete_what_if_forecast_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_what_if_forecast_export

    Deletes a what-if forecast export created using the &lt;a&gt;CreateWhatIfForecastExport&lt;/a&gt; operation. You can delete only what-if forecast exports that have a status of &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;CREATE_FAILED&lt;/code&gt;. To get the status, use the &lt;a&gt;DescribeWhatIfForecastExport&lt;/a&gt; operation. 

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
    body = DeleteWhatIfForecastExportRequest.from_dict(body)
    return web.Response(status=200)


async def describe_auto_predictor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_auto_predictor

    Describes a predictor created using the CreateAutoPredictor operation.

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
    body = DescribeAutoPredictorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_dataset(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_dataset

    &lt;p&gt;Describes an Amazon Forecast dataset created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html\&quot;&gt;CreateDataset&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the parameters specified in the &lt;code&gt;CreateDataset&lt;/code&gt; request, this operation includes the following dataset properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeDatasetRequest.from_dict(body)
    return web.Response(status=200)


async def describe_dataset_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_dataset_group

    &lt;p&gt;Describes a dataset group created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html\&quot;&gt;CreateDatasetGroup&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the parameters provided in the &lt;code&gt;CreateDatasetGroup&lt;/code&gt; request, this operation includes the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DatasetArns&lt;/code&gt; - The datasets belonging to the group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeDatasetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def describe_dataset_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_dataset_import_job

    &lt;p&gt;Describes a dataset import job created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html\&quot;&gt;CreateDatasetImportJob&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the parameters provided in the &lt;code&gt;CreateDatasetImportJob&lt;/code&gt; request, this operation includes the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DataSize&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FieldStatistics&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeDatasetImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_explainability(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_explainability

    Describes an Explainability resource created using the &lt;a&gt;CreateExplainability&lt;/a&gt; operation.

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
    body = DescribeExplainabilityRequest.from_dict(body)
    return web.Response(status=200)


async def describe_explainability_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_explainability_export

    Describes an Explainability export created using the &lt;a&gt;CreateExplainabilityExport&lt;/a&gt; operation.

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
    body = DescribeExplainabilityExportRequest.from_dict(body)
    return web.Response(status=200)


async def describe_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_forecast

    &lt;p&gt;Describes a forecast created using the &lt;a&gt;CreateForecast&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided in the &lt;code&gt;CreateForecast&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DatasetGroupArn&lt;/code&gt; - The dataset group that provided the training data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeForecastRequest.from_dict(body)
    return web.Response(status=200)


async def describe_forecast_export_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_forecast_export_job

    &lt;p&gt;Describes a forecast export job created using the &lt;a&gt;CreateForecastExportJob&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided by the user in the &lt;code&gt;CreateForecastExportJob&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeForecastExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_monitor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_monitor

    &lt;p&gt;Describes a monitor resource. In addition to listing the properties provided in the &lt;a&gt;CreateMonitor&lt;/a&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Baseline&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastEvaluationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastEvaluationState&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_predictor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_predictor

    &lt;note&gt; &lt;p&gt; This operation is only valid for legacy predictors created with CreatePredictor. If you are not using a legacy predictor, use &lt;a&gt;DescribeAutoPredictor&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Describes a predictor created using the &lt;a&gt;CreatePredictor&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided in the &lt;code&gt;CreatePredictor&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DatasetImportJobArns&lt;/code&gt; - The dataset import jobs used to import training data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AutoMLAlgorithmArns&lt;/code&gt; - If AutoML is performed, the algorithms that were evaluated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribePredictorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_predictor_backtest_export_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_predictor_backtest_export_job

    &lt;p&gt;Describes a predictor backtest export job created using the &lt;a&gt;CreatePredictorBacktestExportJob&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided by the user in the &lt;code&gt;CreatePredictorBacktestExportJob&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; (if an error occurred)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribePredictorBacktestExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_what_if_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_what_if_analysis

    &lt;p&gt;Describes the what-if analysis created using the &lt;a&gt;CreateWhatIfAnalysis&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided in the &lt;code&gt;CreateWhatIfAnalysis&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeWhatIfAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def describe_what_if_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_what_if_forecast

    &lt;p&gt;Describes the what-if forecast created using the &lt;a&gt;CreateWhatIfForecast&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided in the &lt;code&gt;CreateWhatIfForecast&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeWhatIfForecastRequest.from_dict(body)
    return web.Response(status=200)


async def describe_what_if_forecast_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_what_if_forecast_export

    &lt;p&gt;Describes the what-if forecast export created using the &lt;a&gt;CreateWhatIfForecastExport&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;In addition to listing the properties provided in the &lt;code&gt;CreateWhatIfForecastExport&lt;/code&gt; request, this operation lists the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastModificationTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Message&lt;/code&gt; - If an error occurred, information about the error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Status&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeWhatIfForecastExportRequest.from_dict(body)
    return web.Response(status=200)


async def get_accuracy_metrics(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_accuracy_metrics

    &lt;p&gt;Provides metrics on the accuracy of the models that were trained by the &lt;a&gt;CreatePredictor&lt;/a&gt; operation. Use metrics to see how well the model performed and to decide whether to use the predictor to generate a forecast. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/metrics.html\&quot;&gt;Predictor Metrics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation generates metrics for each backtest window that was evaluated. The number of backtest windows (&lt;code&gt;NumberOfBacktestWindows&lt;/code&gt;) is specified using the &lt;a&gt;EvaluationParameters&lt;/a&gt; object, which is optionally included in the &lt;code&gt;CreatePredictor&lt;/code&gt; request. If &lt;code&gt;NumberOfBacktestWindows&lt;/code&gt; isn&#39;t specified, the number defaults to one.&lt;/p&gt; &lt;p&gt;The parameters of the &lt;code&gt;filling&lt;/code&gt; method determine which items contribute to the metrics. If you want all items to contribute, specify &lt;code&gt;zero&lt;/code&gt;. If you want only those items that have complete data in the range being evaluated to contribute, specify &lt;code&gt;nan&lt;/code&gt;. For more information, see &lt;a&gt;FeaturizationMethod&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can get accuracy metrics, the &lt;code&gt;Status&lt;/code&gt; of the predictor must be &lt;code&gt;ACTIVE&lt;/code&gt;, signifying that training has completed. To get the status, use the &lt;a&gt;DescribePredictor&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = GetAccuracyMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def list_dataset_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_dataset_groups

    Returns a list of dataset groups created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html\&quot;&gt;CreateDatasetGroup&lt;/a&gt; operation. For each dataset group, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the dataset group ARN with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html\&quot;&gt;DescribeDatasetGroup&lt;/a&gt; operation.

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
    body = ListDatasetGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_dataset_import_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_dataset_import_jobs

    Returns a list of dataset import jobs created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html\&quot;&gt;CreateDatasetImportJob&lt;/a&gt; operation. For each import job, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the ARN with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html\&quot;&gt;DescribeDatasetImportJob&lt;/a&gt; operation. You can filter the list by providing an array of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_Filter.html\&quot;&gt;Filter&lt;/a&gt; objects.

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
    body = ListDatasetImportJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_datasets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_datasets

    Returns a list of datasets created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html\&quot;&gt;CreateDataset&lt;/a&gt; operation. For each dataset, a summary of its properties, including its Amazon Resource Name (ARN), is returned. To retrieve the complete set of properties, use the ARN with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html\&quot;&gt;DescribeDataset&lt;/a&gt; operation.

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
    body = ListDatasetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_explainabilities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_explainabilities

    &lt;p&gt;Returns a list of Explainability resources created using the &lt;a&gt;CreateExplainability&lt;/a&gt; operation. This operation returns a summary for each Explainability. You can filter the list using an array of &lt;a&gt;Filter&lt;/a&gt; objects.&lt;/p&gt; &lt;p&gt;To retrieve the complete set of properties for a particular Explainability resource, use the ARN with the &lt;a&gt;DescribeExplainability&lt;/a&gt; operation.&lt;/p&gt;

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
    body = ListExplainabilitiesRequest.from_dict(body)
    return web.Response(status=200)


async def list_explainability_exports(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_explainability_exports

    &lt;p&gt;Returns a list of Explainability exports created using the &lt;a&gt;CreateExplainabilityExport&lt;/a&gt; operation. This operation returns a summary for each Explainability export. You can filter the list using an array of &lt;a&gt;Filter&lt;/a&gt; objects.&lt;/p&gt; &lt;p&gt;To retrieve the complete set of properties for a particular Explainability export, use the ARN with the &lt;a&gt;DescribeExplainability&lt;/a&gt; operation.&lt;/p&gt;

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
    body = ListExplainabilityExportsRequest.from_dict(body)
    return web.Response(status=200)


async def list_forecast_export_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_forecast_export_jobs

    Returns a list of forecast export jobs created using the &lt;a&gt;CreateForecastExportJob&lt;/a&gt; operation. For each forecast export job, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). To retrieve the complete set of properties, use the ARN with the &lt;a&gt;DescribeForecastExportJob&lt;/a&gt; operation. You can filter the list using an array of &lt;a&gt;Filter&lt;/a&gt; objects.

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
    body = ListForecastExportJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_forecasts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_forecasts

    Returns a list of forecasts created using the &lt;a&gt;CreateForecast&lt;/a&gt; operation. For each forecast, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). To retrieve the complete set of properties, specify the ARN with the &lt;a&gt;DescribeForecast&lt;/a&gt; operation. You can filter the list using an array of &lt;a&gt;Filter&lt;/a&gt; objects.

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
    body = ListForecastsRequest.from_dict(body)
    return web.Response(status=200)


async def list_monitor_evaluations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_monitor_evaluations

    &lt;p&gt;Returns a list of the monitoring evaluation results and predictor events collected by the monitor resource during different windows of time.&lt;/p&gt; &lt;p&gt;For information about monitoring see &lt;a&gt;predictor-monitoring&lt;/a&gt;. For more information about retrieving monitoring results see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html\&quot;&gt;Viewing Monitoring Results&lt;/a&gt;.&lt;/p&gt;

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
    body = ListMonitorEvaluationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_monitors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_monitors

    Returns a list of monitors created with the &lt;a&gt;CreateMonitor&lt;/a&gt; operation and &lt;a&gt;CreateAutoPredictor&lt;/a&gt; operation. For each monitor resource, this operation returns of a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve a complete set of properties of a monitor resource by specify the monitor&#39;s ARN in the &lt;a&gt;DescribeMonitor&lt;/a&gt; operation.

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
    body = ListMonitorsRequest.from_dict(body)
    return web.Response(status=200)


async def list_predictor_backtest_export_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_predictor_backtest_export_jobs

    &lt;p&gt;Returns a list of predictor backtest export jobs created using the &lt;a&gt;CreatePredictorBacktestExportJob&lt;/a&gt; operation. This operation returns a summary for each backtest export job. You can filter the list using an array of &lt;a&gt;Filter&lt;/a&gt; objects.&lt;/p&gt; &lt;p&gt;To retrieve the complete set of properties for a particular backtest export job, use the ARN with the &lt;a&gt;DescribePredictorBacktestExportJob&lt;/a&gt; operation.&lt;/p&gt;

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
    body = ListPredictorBacktestExportJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_predictors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_predictors

    &lt;p&gt;Returns a list of predictors created using the &lt;a&gt;CreateAutoPredictor&lt;/a&gt; or &lt;a&gt;CreatePredictor&lt;/a&gt; operations. For each predictor, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). &lt;/p&gt; &lt;p&gt;You can retrieve the complete set of properties by using the ARN with the &lt;a&gt;DescribeAutoPredictor&lt;/a&gt; and &lt;a&gt;DescribePredictor&lt;/a&gt; operations. You can filter the list using an array of &lt;a&gt;Filter&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListPredictorsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags for an Amazon Forecast resource.

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


async def list_what_if_analyses(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_what_if_analyses

    Returns a list of what-if analyses created using the &lt;a&gt;CreateWhatIfAnalysis&lt;/a&gt; operation. For each what-if analysis, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the what-if analysis ARN with the &lt;a&gt;DescribeWhatIfAnalysis&lt;/a&gt; operation.

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
    body = ListWhatIfAnalysesRequest.from_dict(body)
    return web.Response(status=200)


async def list_what_if_forecast_exports(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_what_if_forecast_exports

    Returns a list of what-if forecast exports created using the &lt;a&gt;CreateWhatIfForecastExport&lt;/a&gt; operation. For each what-if forecast export, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the what-if forecast export ARN with the &lt;a&gt;DescribeWhatIfForecastExport&lt;/a&gt; operation.

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
    body = ListWhatIfForecastExportsRequest.from_dict(body)
    return web.Response(status=200)


async def list_what_if_forecasts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_what_if_forecasts

    Returns a list of what-if forecasts created using the &lt;a&gt;CreateWhatIfForecast&lt;/a&gt; operation. For each what-if forecast, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the what-if forecast ARN with the &lt;a&gt;DescribeWhatIfForecast&lt;/a&gt; operation.

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
    body = ListWhatIfForecastsRequest.from_dict(body)
    return web.Response(status=200)


async def resume_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resume_resource

    Resumes a stopped monitor resource.

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
    body = ResumeResourceRequest.from_dict(body)
    return web.Response(status=200)


async def stop_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_resource

    &lt;p&gt;Stops a resource.&lt;/p&gt; &lt;p&gt;The resource undergoes the following states: &lt;code&gt;CREATE_STOPPING&lt;/code&gt; and &lt;code&gt;CREATE_STOPPED&lt;/code&gt;. You cannot resume a resource once it has been stopped.&lt;/p&gt; &lt;p&gt;This operation can be applied to the following resources (and their corresponding child resources):&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Dataset Import Job&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Predictor Job&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Forecast Job&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Forecast Export Job&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Predictor Backtest Export Job&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Explainability Job&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Explainability Export Job&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = StopResourceRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.

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

    Deletes the specified tags from a resource.

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


async def update_dataset_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_dataset_group

    &lt;p&gt;Replaces the datasets in a dataset group with the specified datasets.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; of the dataset group must be &lt;code&gt;ACTIVE&lt;/code&gt; before you can use the dataset group to create a predictor. Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html\&quot;&gt;DescribeDatasetGroup&lt;/a&gt; operation to get the status.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateDatasetGroupRequest.from_dict(body)
    return web.Response(status=200)
