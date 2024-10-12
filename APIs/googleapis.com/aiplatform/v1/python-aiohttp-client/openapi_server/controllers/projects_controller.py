from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_api_http_body import GoogleApiHttpBody
from openapi_server.models.google_cloud_aiplatform_v1_add_context_artifacts_and_executions_request import GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest
from openapi_server.models.google_cloud_aiplatform_v1_add_context_children_request import GoogleCloudAiplatformV1AddContextChildrenRequest
from openapi_server.models.google_cloud_aiplatform_v1_add_execution_events_request import GoogleCloudAiplatformV1AddExecutionEventsRequest
from openapi_server.models.google_cloud_aiplatform_v1_add_trial_measurement_request import GoogleCloudAiplatformV1AddTrialMeasurementRequest
from openapi_server.models.google_cloud_aiplatform_v1_artifact import GoogleCloudAiplatformV1Artifact
from openapi_server.models.google_cloud_aiplatform_v1_assign_notebook_runtime_request import GoogleCloudAiplatformV1AssignNotebookRuntimeRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_create_features_request import GoogleCloudAiplatformV1BatchCreateFeaturesRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_create_tensorboard_runs_request import GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_create_tensorboard_runs_response import GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse
from openapi_server.models.google_cloud_aiplatform_v1_batch_create_tensorboard_time_series_request import GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_create_tensorboard_time_series_response import GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse
from openapi_server.models.google_cloud_aiplatform_v1_batch_import_evaluated_annotations_request import GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_import_evaluated_annotations_response import GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse
from openapi_server.models.google_cloud_aiplatform_v1_batch_migrate_resources_request import GoogleCloudAiplatformV1BatchMigrateResourcesRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_prediction_job import GoogleCloudAiplatformV1BatchPredictionJob
from openapi_server.models.google_cloud_aiplatform_v1_batch_read_feature_values_request import GoogleCloudAiplatformV1BatchReadFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_batch_read_tensorboard_time_series_data_response import GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse
from openapi_server.models.google_cloud_aiplatform_v1_complete_trial_request import GoogleCloudAiplatformV1CompleteTrialRequest
from openapi_server.models.google_cloud_aiplatform_v1_compute_tokens_request import GoogleCloudAiplatformV1ComputeTokensRequest
from openapi_server.models.google_cloud_aiplatform_v1_compute_tokens_response import GoogleCloudAiplatformV1ComputeTokensResponse
from openapi_server.models.google_cloud_aiplatform_v1_context import GoogleCloudAiplatformV1Context
from openapi_server.models.google_cloud_aiplatform_v1_copy_model_request import GoogleCloudAiplatformV1CopyModelRequest
from openapi_server.models.google_cloud_aiplatform_v1_count_tokens_request import GoogleCloudAiplatformV1CountTokensRequest
from openapi_server.models.google_cloud_aiplatform_v1_count_tokens_response import GoogleCloudAiplatformV1CountTokensResponse
from openapi_server.models.google_cloud_aiplatform_v1_create_deployment_resource_pool_request import GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest
from openapi_server.models.google_cloud_aiplatform_v1_custom_job import GoogleCloudAiplatformV1CustomJob
from openapi_server.models.google_cloud_aiplatform_v1_data_labeling_job import GoogleCloudAiplatformV1DataLabelingJob
from openapi_server.models.google_cloud_aiplatform_v1_dataset import GoogleCloudAiplatformV1Dataset
from openapi_server.models.google_cloud_aiplatform_v1_dataset_version import GoogleCloudAiplatformV1DatasetVersion
from openapi_server.models.google_cloud_aiplatform_v1_delete_feature_values_request import GoogleCloudAiplatformV1DeleteFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_deploy_index_request import GoogleCloudAiplatformV1DeployIndexRequest
from openapi_server.models.google_cloud_aiplatform_v1_deploy_model_request import GoogleCloudAiplatformV1DeployModelRequest
from openapi_server.models.google_cloud_aiplatform_v1_deployed_index import GoogleCloudAiplatformV1DeployedIndex
from openapi_server.models.google_cloud_aiplatform_v1_direct_predict_request import GoogleCloudAiplatformV1DirectPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1_direct_predict_response import GoogleCloudAiplatformV1DirectPredictResponse
from openapi_server.models.google_cloud_aiplatform_v1_direct_raw_predict_request import GoogleCloudAiplatformV1DirectRawPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1_direct_raw_predict_response import GoogleCloudAiplatformV1DirectRawPredictResponse
from openapi_server.models.google_cloud_aiplatform_v1_endpoint import GoogleCloudAiplatformV1Endpoint
from openapi_server.models.google_cloud_aiplatform_v1_entity_type import GoogleCloudAiplatformV1EntityType
from openapi_server.models.google_cloud_aiplatform_v1_execution import GoogleCloudAiplatformV1Execution
from openapi_server.models.google_cloud_aiplatform_v1_explain_request import GoogleCloudAiplatformV1ExplainRequest
from openapi_server.models.google_cloud_aiplatform_v1_explain_response import GoogleCloudAiplatformV1ExplainResponse
from openapi_server.models.google_cloud_aiplatform_v1_export_feature_values_request import GoogleCloudAiplatformV1ExportFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_export_model_request import GoogleCloudAiplatformV1ExportModelRequest
from openapi_server.models.google_cloud_aiplatform_v1_export_tensorboard_time_series_data_request import GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest
from openapi_server.models.google_cloud_aiplatform_v1_export_tensorboard_time_series_data_response import GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse
from openapi_server.models.google_cloud_aiplatform_v1_feature import GoogleCloudAiplatformV1Feature
from openapi_server.models.google_cloud_aiplatform_v1_feature_group import GoogleCloudAiplatformV1FeatureGroup
from openapi_server.models.google_cloud_aiplatform_v1_feature_online_store import GoogleCloudAiplatformV1FeatureOnlineStore
from openapi_server.models.google_cloud_aiplatform_v1_feature_view import GoogleCloudAiplatformV1FeatureView
from openapi_server.models.google_cloud_aiplatform_v1_featurestore import GoogleCloudAiplatformV1Featurestore
from openapi_server.models.google_cloud_aiplatform_v1_fetch_feature_values_request import GoogleCloudAiplatformV1FetchFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_fetch_feature_values_response import GoogleCloudAiplatformV1FetchFeatureValuesResponse
from openapi_server.models.google_cloud_aiplatform_v1_find_neighbors_request import GoogleCloudAiplatformV1FindNeighborsRequest
from openapi_server.models.google_cloud_aiplatform_v1_find_neighbors_response import GoogleCloudAiplatformV1FindNeighborsResponse
from openapi_server.models.google_cloud_aiplatform_v1_generate_content_request import GoogleCloudAiplatformV1GenerateContentRequest
from openapi_server.models.google_cloud_aiplatform_v1_generate_content_response import GoogleCloudAiplatformV1GenerateContentResponse
from openapi_server.models.google_cloud_aiplatform_v1_hyperparameter_tuning_job import GoogleCloudAiplatformV1HyperparameterTuningJob
from openapi_server.models.google_cloud_aiplatform_v1_import_data_request import GoogleCloudAiplatformV1ImportDataRequest
from openapi_server.models.google_cloud_aiplatform_v1_import_feature_values_request import GoogleCloudAiplatformV1ImportFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_import_model_evaluation_request import GoogleCloudAiplatformV1ImportModelEvaluationRequest
from openapi_server.models.google_cloud_aiplatform_v1_index import GoogleCloudAiplatformV1Index
from openapi_server.models.google_cloud_aiplatform_v1_index_endpoint import GoogleCloudAiplatformV1IndexEndpoint
from openapi_server.models.google_cloud_aiplatform_v1_lineage_subgraph import GoogleCloudAiplatformV1LineageSubgraph
from openapi_server.models.google_cloud_aiplatform_v1_list_annotations_response import GoogleCloudAiplatformV1ListAnnotationsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_artifacts_response import GoogleCloudAiplatformV1ListArtifactsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_batch_prediction_jobs_response import GoogleCloudAiplatformV1ListBatchPredictionJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_contexts_response import GoogleCloudAiplatformV1ListContextsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_custom_jobs_response import GoogleCloudAiplatformV1ListCustomJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_data_items_response import GoogleCloudAiplatformV1ListDataItemsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_data_labeling_jobs_response import GoogleCloudAiplatformV1ListDataLabelingJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_dataset_versions_response import GoogleCloudAiplatformV1ListDatasetVersionsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_datasets_response import GoogleCloudAiplatformV1ListDatasetsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_deployment_resource_pools_response import GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_endpoints_response import GoogleCloudAiplatformV1ListEndpointsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_entity_types_response import GoogleCloudAiplatformV1ListEntityTypesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_executions_response import GoogleCloudAiplatformV1ListExecutionsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_feature_groups_response import GoogleCloudAiplatformV1ListFeatureGroupsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_feature_online_stores_response import GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_feature_view_syncs_response import GoogleCloudAiplatformV1ListFeatureViewSyncsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_feature_views_response import GoogleCloudAiplatformV1ListFeatureViewsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_features_response import GoogleCloudAiplatformV1ListFeaturesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_featurestores_response import GoogleCloudAiplatformV1ListFeaturestoresResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_hyperparameter_tuning_jobs_response import GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_index_endpoints_response import GoogleCloudAiplatformV1ListIndexEndpointsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_indexes_response import GoogleCloudAiplatformV1ListIndexesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_metadata_schemas_response import GoogleCloudAiplatformV1ListMetadataSchemasResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_metadata_stores_response import GoogleCloudAiplatformV1ListMetadataStoresResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_model_deployment_monitoring_jobs_response import GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_model_evaluation_slices_response import GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_model_evaluations_response import GoogleCloudAiplatformV1ListModelEvaluationsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_model_versions_response import GoogleCloudAiplatformV1ListModelVersionsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_models_response import GoogleCloudAiplatformV1ListModelsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_nas_jobs_response import GoogleCloudAiplatformV1ListNasJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_nas_trial_details_response import GoogleCloudAiplatformV1ListNasTrialDetailsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_notebook_runtime_templates_response import GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_notebook_runtimes_response import GoogleCloudAiplatformV1ListNotebookRuntimesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_optimal_trials_response import GoogleCloudAiplatformV1ListOptimalTrialsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_pipeline_jobs_response import GoogleCloudAiplatformV1ListPipelineJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_saved_queries_response import GoogleCloudAiplatformV1ListSavedQueriesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_schedules_response import GoogleCloudAiplatformV1ListSchedulesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_specialist_pools_response import GoogleCloudAiplatformV1ListSpecialistPoolsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_studies_response import GoogleCloudAiplatformV1ListStudiesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_tensorboard_experiments_response import GoogleCloudAiplatformV1ListTensorboardExperimentsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_tensorboard_runs_response import GoogleCloudAiplatformV1ListTensorboardRunsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_tensorboard_time_series_response import GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_tensorboards_response import GoogleCloudAiplatformV1ListTensorboardsResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_training_pipelines_response import GoogleCloudAiplatformV1ListTrainingPipelinesResponse
from openapi_server.models.google_cloud_aiplatform_v1_list_trials_response import GoogleCloudAiplatformV1ListTrialsResponse
from openapi_server.models.google_cloud_aiplatform_v1_lookup_study_request import GoogleCloudAiplatformV1LookupStudyRequest
from openapi_server.models.google_cloud_aiplatform_v1_merge_version_aliases_request import GoogleCloudAiplatformV1MergeVersionAliasesRequest
from openapi_server.models.google_cloud_aiplatform_v1_metadata_schema import GoogleCloudAiplatformV1MetadataSchema
from openapi_server.models.google_cloud_aiplatform_v1_metadata_store import GoogleCloudAiplatformV1MetadataStore
from openapi_server.models.google_cloud_aiplatform_v1_model import GoogleCloudAiplatformV1Model
from openapi_server.models.google_cloud_aiplatform_v1_model_deployment_monitoring_job import GoogleCloudAiplatformV1ModelDeploymentMonitoringJob
from openapi_server.models.google_cloud_aiplatform_v1_model_evaluation import GoogleCloudAiplatformV1ModelEvaluation
from openapi_server.models.google_cloud_aiplatform_v1_mutate_deployed_model_request import GoogleCloudAiplatformV1MutateDeployedModelRequest
from openapi_server.models.google_cloud_aiplatform_v1_nas_job import GoogleCloudAiplatformV1NasJob
from openapi_server.models.google_cloud_aiplatform_v1_notebook_runtime_template import GoogleCloudAiplatformV1NotebookRuntimeTemplate
from openapi_server.models.google_cloud_aiplatform_v1_pipeline_job import GoogleCloudAiplatformV1PipelineJob
from openapi_server.models.google_cloud_aiplatform_v1_predict_request import GoogleCloudAiplatformV1PredictRequest
from openapi_server.models.google_cloud_aiplatform_v1_predict_response import GoogleCloudAiplatformV1PredictResponse
from openapi_server.models.google_cloud_aiplatform_v1_purge_artifacts_request import GoogleCloudAiplatformV1PurgeArtifactsRequest
from openapi_server.models.google_cloud_aiplatform_v1_purge_contexts_request import GoogleCloudAiplatformV1PurgeContextsRequest
from openapi_server.models.google_cloud_aiplatform_v1_purge_executions_request import GoogleCloudAiplatformV1PurgeExecutionsRequest
from openapi_server.models.google_cloud_aiplatform_v1_query_deployed_models_response import GoogleCloudAiplatformV1QueryDeployedModelsResponse
from openapi_server.models.google_cloud_aiplatform_v1_raw_predict_request import GoogleCloudAiplatformV1RawPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1_read_feature_values_request import GoogleCloudAiplatformV1ReadFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_read_feature_values_response import GoogleCloudAiplatformV1ReadFeatureValuesResponse
from openapi_server.models.google_cloud_aiplatform_v1_read_index_datapoints_request import GoogleCloudAiplatformV1ReadIndexDatapointsRequest
from openapi_server.models.google_cloud_aiplatform_v1_read_index_datapoints_response import GoogleCloudAiplatformV1ReadIndexDatapointsResponse
from openapi_server.models.google_cloud_aiplatform_v1_read_tensorboard_blob_data_response import GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse
from openapi_server.models.google_cloud_aiplatform_v1_read_tensorboard_size_response import GoogleCloudAiplatformV1ReadTensorboardSizeResponse
from openapi_server.models.google_cloud_aiplatform_v1_read_tensorboard_time_series_data_response import GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse
from openapi_server.models.google_cloud_aiplatform_v1_read_tensorboard_usage_response import GoogleCloudAiplatformV1ReadTensorboardUsageResponse
from openapi_server.models.google_cloud_aiplatform_v1_remove_context_children_request import GoogleCloudAiplatformV1RemoveContextChildrenRequest
from openapi_server.models.google_cloud_aiplatform_v1_remove_datapoints_request import GoogleCloudAiplatformV1RemoveDatapointsRequest
from openapi_server.models.google_cloud_aiplatform_v1_resume_schedule_request import GoogleCloudAiplatformV1ResumeScheduleRequest
from openapi_server.models.google_cloud_aiplatform_v1_schedule import GoogleCloudAiplatformV1Schedule
from openapi_server.models.google_cloud_aiplatform_v1_search_data_items_response import GoogleCloudAiplatformV1SearchDataItemsResponse
from openapi_server.models.google_cloud_aiplatform_v1_search_features_response import GoogleCloudAiplatformV1SearchFeaturesResponse
from openapi_server.models.google_cloud_aiplatform_v1_search_migratable_resources_request import GoogleCloudAiplatformV1SearchMigratableResourcesRequest
from openapi_server.models.google_cloud_aiplatform_v1_search_migratable_resources_response import GoogleCloudAiplatformV1SearchMigratableResourcesResponse
from openapi_server.models.google_cloud_aiplatform_v1_search_model_deployment_monitoring_stats_anomalies_request import GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest
from openapi_server.models.google_cloud_aiplatform_v1_search_model_deployment_monitoring_stats_anomalies_response import GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse
from openapi_server.models.google_cloud_aiplatform_v1_search_nearest_entities_request import GoogleCloudAiplatformV1SearchNearestEntitiesRequest
from openapi_server.models.google_cloud_aiplatform_v1_search_nearest_entities_response import GoogleCloudAiplatformV1SearchNearestEntitiesResponse
from openapi_server.models.google_cloud_aiplatform_v1_specialist_pool import GoogleCloudAiplatformV1SpecialistPool
from openapi_server.models.google_cloud_aiplatform_v1_stream_raw_predict_request import GoogleCloudAiplatformV1StreamRawPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1_streaming_predict_request import GoogleCloudAiplatformV1StreamingPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1_streaming_predict_response import GoogleCloudAiplatformV1StreamingPredictResponse
from openapi_server.models.google_cloud_aiplatform_v1_streaming_read_feature_values_request import GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_study import GoogleCloudAiplatformV1Study
from openapi_server.models.google_cloud_aiplatform_v1_suggest_trials_request import GoogleCloudAiplatformV1SuggestTrialsRequest
from openapi_server.models.google_cloud_aiplatform_v1_sync_feature_view_response import GoogleCloudAiplatformV1SyncFeatureViewResponse
from openapi_server.models.google_cloud_aiplatform_v1_tensorboard import GoogleCloudAiplatformV1Tensorboard
from openapi_server.models.google_cloud_aiplatform_v1_tensorboard_experiment import GoogleCloudAiplatformV1TensorboardExperiment
from openapi_server.models.google_cloud_aiplatform_v1_tensorboard_run import GoogleCloudAiplatformV1TensorboardRun
from openapi_server.models.google_cloud_aiplatform_v1_tensorboard_time_series import GoogleCloudAiplatformV1TensorboardTimeSeries
from openapi_server.models.google_cloud_aiplatform_v1_training_pipeline import GoogleCloudAiplatformV1TrainingPipeline
from openapi_server.models.google_cloud_aiplatform_v1_trial import GoogleCloudAiplatformV1Trial
from openapi_server.models.google_cloud_aiplatform_v1_undeploy_index_request import GoogleCloudAiplatformV1UndeployIndexRequest
from openapi_server.models.google_cloud_aiplatform_v1_undeploy_model_request import GoogleCloudAiplatformV1UndeployModelRequest
from openapi_server.models.google_cloud_aiplatform_v1_update_explanation_dataset_request import GoogleCloudAiplatformV1UpdateExplanationDatasetRequest
from openapi_server.models.google_cloud_aiplatform_v1_upload_model_request import GoogleCloudAiplatformV1UploadModelRequest
from openapi_server.models.google_cloud_aiplatform_v1_upsert_datapoints_request import GoogleCloudAiplatformV1UpsertDatapointsRequest
from openapi_server.models.google_cloud_aiplatform_v1_write_feature_values_request import GoogleCloudAiplatformV1WriteFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1_write_tensorboard_experiment_data_request import GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest
from openapi_server.models.google_cloud_aiplatform_v1_write_tensorboard_run_data_request import GoogleCloudAiplatformV1WriteTensorboardRunDataRequest
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def aiplatform_projects_locations_batch_prediction_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_batch_prediction_jobs_create

    Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

    :param parent: Required. The resource name of the Location to create the BatchPredictionJob in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchPredictionJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_batch_prediction_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_batch_prediction_jobs_list

    Lists BatchPredictionJobs in a Location.

    :param parent: Required. The resource name of the Location to list the BatchPredictionJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;model_display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60;
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListBatchPredictionJobsResponse.next_page_token of the previous JobService.ListBatchPredictionJobs call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_custom_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_custom_jobs_create

    Creates a CustomJob. A created CustomJob right away will be attempted to be run.

    :param parent: Required. The resource name of the Location to create the CustomJob in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1CustomJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_custom_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_custom_jobs_list

    Lists CustomJobs in a Location.

    :param parent: Required. The resource name of the Location to list the CustomJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60;
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListCustomJobsResponse.next_page_token of the previous JobService.ListCustomJobs call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_data_labeling_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_data_labeling_jobs_create

    Creates a DataLabelingJob.

    :param parent: Required. The parent of the DataLabelingJob. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DataLabelingJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_data_labeling_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_data_labeling_jobs_list

    Lists DataLabelingJobs in a Location.

    :param parent: Required. The parent of the DataLabelingJob. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60;
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order by default. Use &#x60;desc&#x60; after a field name for descending.
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read. FieldMask represents a set of symbolic field paths. For example, the mask can be &#x60;paths: \&quot;name\&quot;&#x60;. The \&quot;name\&quot; here is a field in DataLabelingJob. If this field is not set, all fields of the DataLabelingJob are returned.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_datasets_create

    Creates a Dataset.

    :param parent: Required. The resource name of the Location to create the Dataset in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Dataset.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_data_items_annotations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_datasets_data_items_annotations_list

    Lists Annotations belongs to a dataitem

    :param parent: Required. The resource name of the DataItem to list Annotations from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending.
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_data_items_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_datasets_data_items_list

    Lists DataItems in a Dataset.

    :param parent: Required. The resource name of the Dataset to list DataItems from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending.
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_dataset_versions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_datasets_dataset_versions_create

    Create a version from a Dataset.

    :param parent: Required. The name of the Dataset resource. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DatasetVersion.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_dataset_versions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_datasets_dataset_versions_list

    Lists DatasetVersions in a Dataset.

    :param parent: Required. The resource name of the Dataset to list DatasetVersions from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. The standard list filter.
    :type filter: str
    :param order_by: Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending.
    :type order_by: str
    :param page_size: Optional. The standard list page size.
    :type page_size: int
    :param page_token: Optional. The standard list page token.
    :type page_token: str
    :param read_mask: Optional. Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_dataset_versions_restore(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """aiplatform_projects_locations_datasets_dataset_versions_restore

    Restores a dataset version.

    :param name: Required. The name of the DatasetVersion resource. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_import(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_datasets_import

    Imports data into a Dataset.

    :param name: Required. The name of the Dataset resource. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ImportDataRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_datasets_list

    Lists Datasets in a Location.

    :param parent: Required. The name of the Dataset&#39;s parent resource. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;display_name&#x60;: supports &#x3D; and !&#x3D; * &#x60;metadata_schema_uri&#x60;: supports &#x3D; and !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60;
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60;
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_saved_queries_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_datasets_saved_queries_list

    Lists SavedQueries in a Dataset.

    :param parent: Required. The resource name of the Dataset to list SavedQueries from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending.
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_datasets_search_data_items(request: web.Request, dataset, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, annotation_filters=None, annotations_filter=None, annotations_limit=None, data_item_filter=None, data_labeling_job=None, field_mask=None, order_by=None, order_by_annotation_order_by=None, order_by_annotation_saved_query=None, order_by_data_item=None, page_size=None, page_token=None, saved_query=None) -> web.Response:
    """aiplatform_projects_locations_datasets_search_data_items

    Searches DataItems in a Dataset.

    :param dataset: Required. The resource name of the Dataset from which to search DataItems. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60;
    :type dataset: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param annotation_filters: An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned. * &#x60;annotation_spec_id&#x60; - for &#x3D; or !&#x3D;. Must specify &#x60;saved_query_id&#x3D;&#x60; - saved query id that annotations should belong to.
    :type annotation_filters: List[str]
    :param annotations_filter: An expression for filtering the Annotations that will be returned per DataItem. * &#x60;annotation_spec_id&#x60; - for &#x3D; or !&#x3D;.
    :type annotations_filter: str
    :param annotations_limit: If set, only up to this many of Annotations will be returned per DataItemView. The maximum value is 1000. If not set, the maximum value will be used.
    :type annotations_limit: int
    :param data_item_filter: An expression for filtering the DataItem that will be returned. * &#x60;data_item_id&#x60; - for &#x3D; or !&#x3D;. * &#x60;labeled&#x60; - for &#x3D; or !&#x3D;. * &#x60;has_annotation(ANNOTATION_SPEC_ID)&#x60; - true only for DataItem that have at least one annotation with annotation_spec_id &#x3D; &#x60;ANNOTATION_SPEC_ID&#x60; in the context of SavedQuery or DataLabelingJob. For example: * &#x60;data_item&#x3D;1&#x60; * &#x60;has_annotation(5)&#x60;
    :type data_item_filter: str
    :param data_labeling_job: The resource name of a DataLabelingJob. Format: &#x60;projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}&#x60; If this field is set, all of the search will be done in the context of this DataLabelingJob.
    :type data_labeling_job: str
    :param field_mask: Mask specifying which fields of DataItemView to read.
    :type field_mask: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending.
    :type order_by: str
    :param order_by_annotation_order_by: A comma-separated list of annotation fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Must also specify saved_query.
    :type order_by_annotation_order_by: str
    :param order_by_annotation_saved_query: Required. Saved query of the Annotation. Only Annotations belong to this saved query will be considered for ordering.
    :type order_by_annotation_saved_query: str
    :param order_by_data_item: A comma-separated list of data item fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending.
    :type order_by_data_item: str
    :param page_size: Requested page size. Server may return fewer results than requested. Default and maximum page size is 100.
    :type page_size: int
    :param page_token: A token identifying a page of results for the server to return Typically obtained via SearchDataItemsResponse.next_page_token of the previous DatasetService.SearchDataItems call.
    :type page_token: str
    :param saved_query: The resource name of a SavedQuery(annotation set in UI). Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}&#x60; All of the search will be done in the context of this SavedQuery.
    :type saved_query: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_deployment_resource_pools_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_deployment_resource_pools_create

    Create a DeploymentResourcePool.

    :param parent: Required. The parent location resource where this DeploymentResourcePool will be created. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_deployment_resource_pools_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_deployment_resource_pools_list

    List DeploymentResourcePools in a location.

    :param parent: Required. The parent Location which owns this collection of DeploymentResourcePools. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of DeploymentResourcePools to return. The service may return fewer than this value.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListDeploymentResourcePools&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListDeploymentResourcePools&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_deployment_resource_pools_query_deployed_models(request: web.Request, deployment_resource_pool, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_deployment_resource_pools_query_deployed_models

    List DeployedModels that have been deployed on this DeploymentResourcePool.

    :param deployment_resource_pool: Required. The name of the target DeploymentResourcePool to query. Format: &#x60;projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}&#x60;
    :type deployment_resource_pool: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of DeployedModels to return. The service may return fewer than this value.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;QueryDeployedModels&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;QueryDeployedModels&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, endpoint_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_create

    Creates an Endpoint.

    :param parent: Required. The resource name of the Location to create the Endpoint in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param endpoint_id: Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are &#x60;[a-z0-9-]&#x60;. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are &#x60;[0-9]&#x60; with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as &#x60;?endpoint_id&#x3D;12345&#x60;. This is the fallback for fields that are not included in either the URI or the body.
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Endpoint.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_deploy_model(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_deploy_model

    Deploys a Model into this Endpoint, creating a DeployedModel within it.

    :param endpoint: Required. The name of the Endpoint resource into which to deploy a Model. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DeployModelRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_direct_predict(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_direct_predict

    Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks.

    :param endpoint: Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DirectPredictRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_direct_raw_predict(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_direct_raw_predict

    Perform an unary online prediction request to a gRPC model server for custom containers.

    :param endpoint: Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DirectRawPredictRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_explain(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_explain

    Perform an online explanation. If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated.

    :param endpoint: Required. The name of the Endpoint requested to serve the explanation. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ExplainRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_list

    Lists Endpoints in a Location.

    :param parent: Required. The resource name of the Location from which to list the Endpoints. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;endpoint&#x60; supports &#x3D; and !&#x3D;. &#x60;endpoint&#x60; represents the Endpoint ID, i.e. the last segment of the Endpoint&#39;s resource name. * &#x60;display_name&#x60; supports &#x3D; and, !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;endpoint&#x3D;1&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60;
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;.
    :type order_by: str
    :param page_size: Optional. The standard list page size.
    :type page_size: int
    :param page_token: Optional. The standard list page token. Typically obtained via ListEndpointsResponse.next_page_token of the previous EndpointService.ListEndpoints call.
    :type page_token: str
    :param read_mask: Optional. Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_mutate_deployed_model(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_mutate_deployed_model

    Updates an existing deployed model. Updatable fields include &#x60;min_replica_count&#x60;, &#x60;max_replica_count&#x60;, &#x60;autoscaling_metric_specs&#x60;, &#x60;disable_container_logging&#x60; (v1 only), and &#x60;enable_container_logging&#x60; (v1beta1 only).

    :param endpoint: Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1MutateDeployedModelRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_endpoints_undeploy_model(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_endpoints_undeploy_model

    Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it&#39;s using.

    :param endpoint: Required. The name of the Endpoint resource from which to undeploy a Model. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1UndeployModelRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_groups_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, feature_group_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_feature_groups_create

    Creates a new FeatureGroup in a given project and location.

    :param parent: Required. The resource name of the Location to create FeatureGroups. Format: &#x60;projects/{project}/locations/{location}&#39;&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param feature_group_id: Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within the project and location.
    :type feature_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1FeatureGroup.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_groups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_feature_groups_list

    Lists FeatureGroups in a given project and location.

    :param parent: Required. The resource name of the Location to list FeatureGroups. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the FeatureGroups that match the filter expression. The following fields are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality and key presence. Examples: * &#x60;create_time &gt; \&quot;2020-01-01\&quot; OR update_time &gt; \&quot;2020-01-01\&quot;&#x60; FeatureGroups created or updated after 2020-01-01. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; FeatureGroups with label \&quot;env\&quot; set to \&quot;prod\&quot;.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported Fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60;
    :type order_by: str
    :param page_size: The maximum number of FeatureGroups to return. The service may return fewer than this value. If unspecified, at most 100 FeatureGroups will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous FeatureGroupAdminService.ListFeatureGroups call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureGroupAdminService.ListFeatureGroups must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, feature_online_store_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_create

    Creates a new FeatureOnlineStore in a given project and location.

    :param parent: Required. The resource name of the Location to create FeatureOnlineStores. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param feature_online_store_id: Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within the project and location.
    :type feature_online_store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1FeatureOnlineStore.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_feature_views_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, feature_view_id=None, run_sync_immediately=None, body=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_feature_views_create

    Creates a new FeatureView in a given FeatureOnlineStore.

    :param parent: Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param feature_view_id: Required. The ID to use for the FeatureView, which will become the final component of the FeatureView&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.
    :type feature_view_id: str
    :param run_sync_immediately: Immutable. If set to true, one on demand sync will be run immediately, regardless whether the FeatureView.sync_config is configured or not.
    :type run_sync_immediately: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1FeatureView.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_feature_views_feature_view_syncs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_feature_views_feature_view_syncs_list

    Lists FeatureViewSyncs in a given FeatureView.

    :param parent: Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the FeatureViewSyncs that match the filter expression. The following filters are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. Examples: * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; FeatureViewSyncs created after 2020-01-31T15:30:00.000000Z.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;create_time&#x60;
    :type order_by: str
    :param page_size: The maximum number of FeatureViewSyncs to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViewSyncs will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViewSyncs call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViewSyncs must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_feature_views_fetch_feature_values(request: web.Request, feature_view, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_feature_views_fetch_feature_values

    Fetch feature values under a FeatureView.

    :param feature_view: Required. FeatureView resource format &#x60;projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}&#x60;
    :type feature_view: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1FetchFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_feature_views_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_feature_views_list

    Lists FeatureViews in a given FeatureOnlineStore.

    :param parent: Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the FeatureViews that match the filter expression. The following filters are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. Examples: * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot; OR update_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; FeatureViews created or updated after 2020-01-31T15:30:00.000000Z. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; FeatureViews having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any FeatureView which has a label with &#39;env&#39; as the key.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;feature_view_id&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60;
    :type order_by: str
    :param page_size: The maximum number of FeatureViews to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViews will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViews call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViews must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_feature_views_search_nearest_entities(request: web.Request, feature_view, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_feature_views_search_nearest_entities

    Search the nearest entities under a FeatureView. Search only works for indexable feature view; if a feature view isn&#39;t indexable, returns Invalid argument response.

    :param feature_view: Required. FeatureView resource format &#x60;projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}&#x60;
    :type feature_view: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1SearchNearestEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_feature_views_sync(request: web.Request, feature_view, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_feature_views_sync

    Triggers on-demand sync for the FeatureView.

    :param feature_view: Required. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}&#x60;
    :type feature_view: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_list

    Lists FeatureOnlineStores in a given project and location.

    :param parent: Required. The resource name of the Location to list FeatureOnlineStores. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the FeatureOnlineStores that match the filter expression. The following fields are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality and key presence. Examples: * &#x60;create_time &gt; \&quot;2020-01-01\&quot; OR update_time &gt; \&quot;2020-01-01\&quot;&#x60; FeatureOnlineStores created or updated after 2020-01-01. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; FeatureOnlineStores with label \&quot;env\&quot; set to \&quot;prod\&quot;.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported Fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60;
    :type order_by: str
    :param page_size: The maximum number of FeatureOnlineStores to return. The service may return fewer than this value. If unspecified, at most 100 FeatureOnlineStores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureOnlineStores call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureOnlineStores must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_feature_online_stores_operations_list_wait(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_feature_online_stores_operations_list_wait

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

    :param name: The name of the operation&#39;s parent resource.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_batch_read_feature_values(request: web.Request, featurestore, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_batch_read_feature_values

    Batch reads Feature values from a Featurestore. This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance&#39;s read timestamp.

    :param featurestore: Required. The resource name of the Featurestore from which to query Feature values. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60;
    :type featurestore: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchReadFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, featurestore_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_create

    Creates a new Featurestore in a given project and location.

    :param parent: Required. The resource name of the Location to create Featurestores. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param featurestore_id: Required. The ID to use for this Featurestore, which will become the final component of the Featurestore&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within the project and location.
    :type featurestore_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Featurestore.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, entity_type_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_create

    Creates a new EntityType in a given Featurestore.

    :param parent: Required. The resource name of the Featurestore to create EntityTypes. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param entity_type_id: Required. The ID to use for the EntityType, which will become the final component of the EntityType&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within a featurestore.
    :type entity_type_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1EntityType.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_delete_feature_values(request: web.Request, entity_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_delete_feature_values

    Delete Feature values from Featurestore. The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done. If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

    :param entity_type: Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;
    :type entity_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DeleteFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_export_feature_values(request: web.Request, entity_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_export_feature_values

    Exports Feature values from all the entities of a target EntityType.

    :param entity_type: Required. The resource name of the EntityType from which to export Feature values. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60;
    :type entity_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ExportFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_features_batch_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_features_batch_create

    Creates a batch of Features in a given EntityType.

    :param parent: Required. The resource name of the EntityType to create the batch of Features under. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchCreateFeaturesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_features_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, feature_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_features_create

    Creates a new Feature in a given EntityType.

    :param parent: Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; Format for feature_group as parent: &#x60;projects/{project}/locations/{location}/featureGroups/{feature_group}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param feature_id: Required. The ID to use for the Feature, which will become the final component of the Feature&#39;s resource name. This value may be up to 128 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.
    :type feature_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Feature.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_features_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, latest_stats_count=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_features_list

    Lists Features in a given EntityType.

    :param parent: Required. The resource name of the Location to list Features. Format for entity_type as parent: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; Format for feature_group as parent: &#x60;projects/{project}/locations/{location}/featureGroups/{feature_group}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the Features that match the filter expression. The following filters are supported: * &#x60;value_type&#x60;: Supports &#x3D; and !&#x3D; comparisons. * &#x60;create_time&#x60;: Supports &#x3D;, !&#x3D;, &lt;, &gt;, &gt;&#x3D;, and &lt;&#x3D; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x3D;, !&#x3D;, &lt;, &gt;, &gt;&#x3D;, and &lt;&#x3D; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. Examples: * &#x60;value_type &#x3D; DOUBLE&#x60; --&gt; Features whose type is DOUBLE. * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot; OR update_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; Features having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any Feature which has a label with &#39;env&#39; as the key.
    :type filter: str
    :param latest_stats_count: Only applicable for Vertex AI Feature Store (Legacy). If set, return the most recent ListFeaturesRequest.latest_stats_count of stats for each Feature in response. Valid value is [0, 10]. If number of stats exists &lt; ListFeaturesRequest.latest_stats_count, return all existing stats.
    :type latest_stats_count: int
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;feature_id&#x60; * &#x60;value_type&#x60; (Not supported for FeatureRegistry Feature) * &#x60;create_time&#x60; * &#x60;update_time&#x60;
    :type order_by: str
    :param page_size: The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 1000 Features will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous FeaturestoreService.ListFeatures call or FeatureRegistryService.ListFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListFeatures or FeatureRegistryService.ListFeatures must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_import_feature_values(request: web.Request, entity_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_import_feature_values

    Imports Feature values into the Featurestore from a source storage. The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done. If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done. There are also scenarios where the caller can cause inconsistency. - Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

    :param entity_type: Required. The resource name of the EntityType grouping the Features for which values are being imported. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;
    :type entity_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ImportFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_list

    Lists EntityTypes in a given Featurestore.

    :param parent: Required. The resource name of the Featurestore to list EntityTypes. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the EntityTypes that match the filter expression. The following filters are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. Examples: * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot; OR update_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; EntityTypes having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any EntityType which has a label with &#39;env&#39; as the key.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;entity_type_id&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60;
    :type order_by: str
    :param page_size: The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous FeaturestoreService.ListEntityTypes call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListEntityTypes must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_read_feature_values(request: web.Request, entity_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_read_feature_values

    Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues.

    :param entity_type: Required. The resource name of the EntityType for the entity being read. Value format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be &#x60;user&#x60;.
    :type entity_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ReadFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_streaming_read_feature_values(request: web.Request, entity_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_streaming_read_feature_values

    Reads Feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses.

    :param entity_type: Required. The resource name of the entities&#39; type. Value format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be &#x60;user&#x60;.
    :type entity_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_entity_types_write_feature_values(request: web.Request, entity_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_entity_types_write_feature_values

    Writes Feature values of one or more entities of an EntityType. The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention.

    :param entity_type: Required. The resource name of the EntityType for the entities being written. Value format: &#x60;projects/{project}/locations/{location}/featurestores/ {featurestore}/entityTypes/{entityType}&#x60;. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be &#x60;user&#x60;.
    :type entity_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1WriteFeatureValuesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_list

    Lists Featurestores in a given project and location.

    :param parent: Required. The resource name of the Location to list Featurestores. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the featurestores that match the filter expression. The following fields are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;online_serving_config.fixed_node_count&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. * &#x60;labels&#x60;: Supports key-value equality and key presence. Examples: * &#x60;create_time &gt; \&quot;2020-01-01\&quot; OR update_time &gt; \&quot;2020-01-01\&quot;&#x60; Featurestores created or updated after 2020-01-01. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; Featurestores with label \&quot;env\&quot; set to \&quot;prod\&quot;.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported Fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; * &#x60;online_serving_config.fixed_node_count&#x60;
    :type order_by: str
    :param page_size: The maximum number of Featurestores to return. The service may return fewer than this value. If unspecified, at most 100 Featurestores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous FeaturestoreService.ListFeaturestores call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListFeaturestores must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_featurestores_search_features(request: web.Request, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """aiplatform_projects_locations_featurestores_search_features

    Searches Features matching a query in a given project.

    :param location: Required. The resource name of the Location to search Features. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type location: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous FeaturestoreService.SearchFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.SearchFeatures, except &#x60;page_size&#x60;, must match the call that provided the page token.
    :type page_token: str
    :param query: Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using &#x60;AND&#x60; to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature&#39;s FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric &#x60;[a-zA-Z0-9]&#x60;, underscore &#x60;_&#x60;, or asterisk &#x60;*&#x60; are treated as delimiters for tokens. &#x60;*&#x60; is treated as a wildcard that matches characters within a token. * Ignoring case. * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks (\&quot;). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: * &#x60;feature_id&#x60; * &#x60;description&#x60; * &#x60;entity_type_id&#x60; Examples: * &#x60;feature_id: foo&#x60; --&gt; Matches a Feature with ID containing the substring &#x60;foo&#x60; (eg. &#x60;foo&#x60;, &#x60;foofeature&#x60;, &#x60;barfoo&#x60;). * &#x60;feature_id: foo*feature&#x60; --&gt; Matches a Feature with ID containing the substring &#x60;foo*feature&#x60; (eg. &#x60;foobarfeature&#x60;). * &#x60;feature_id: foo AND description: bar&#x60; --&gt; Matches a Feature with ID containing the substring &#x60;foo&#x60; and description containing the substring &#x60;bar&#x60;. Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. * &#x60;feature_id&#x60;: Supports &#x3D; comparisons. * &#x60;description&#x60;: Supports &#x3D; comparisons. Multi-token filters should be enclosed in quotes. * &#x60;entity_type_id&#x60;: Supports &#x3D; comparisons. * &#x60;value_type&#x60;: Supports &#x3D; and !&#x3D; comparisons. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. * &#x60;featurestore_id&#x60;: Supports &#x3D; comparisons. Examples: * &#x60;description &#x3D; \&quot;foo bar\&quot;&#x60; --&gt; Any Feature with description exactly equal to &#x60;foo bar&#x60; * &#x60;value_type &#x3D; DOUBLE&#x60; --&gt; Features whose type is DOUBLE. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; Features having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any Feature which has a label with &#x60;env&#x60; as the key.
    :type query: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_hyperparameter_tuning_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_hyperparameter_tuning_jobs_create

    Creates a HyperparameterTuningJob

    :param parent: Required. The resource name of the Location to create the HyperparameterTuningJob in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1HyperparameterTuningJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_hyperparameter_tuning_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_hyperparameter_tuning_jobs_list

    Lists HyperparameterTuningJobs in a Location.

    :param parent: Required. The resource name of the Location to list the HyperparameterTuningJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60;
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListHyperparameterTuningJobsResponse.next_page_token of the previous JobService.ListHyperparameterTuningJobs call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_create

    Creates an IndexEndpoint.

    :param parent: Required. The resource name of the Location to create the IndexEndpoint in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1IndexEndpoint.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_deploy_index(request: web.Request, index_endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_deploy_index

    Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

    :param index_endpoint: Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60;
    :type index_endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DeployIndexRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_find_neighbors(request: web.Request, index_endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_find_neighbors

    Finds the nearest neighbors of each vector within the request.

    :param index_endpoint: Required. The name of the index endpoint. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60;
    :type index_endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1FindNeighborsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_list

    Lists IndexEndpoints in a Location.

    :param parent: Required. The resource name of the Location from which to list the IndexEndpoints. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;index_endpoint&#x60; supports &#x3D; and !&#x3D;. &#x60;index_endpoint&#x60; represents the IndexEndpoint ID, ie. the last segment of the IndexEndpoint&#39;s resourcename. * &#x60;display_name&#x60; supports &#x3D;, !&#x3D; and regex() (uses [re2](https://github.com/google/re2/wiki/Syntax) syntax) * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* or labels:key - key existence A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;index_endpoint&#x3D;\&quot;1\&quot;&#x60; * &#x60;display_name&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;regex(display_name, \&quot;^A\&quot;) -&gt; The display name starts with an A. * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60;
    :type filter: str
    :param page_size: Optional. The standard list page size.
    :type page_size: int
    :param page_token: Optional. The standard list page token. Typically obtained via ListIndexEndpointsResponse.next_page_token of the previous IndexEndpointService.ListIndexEndpoints call.
    :type page_token: str
    :param read_mask: Optional. Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_mutate_deployed_index(request: web.Request, index_endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_mutate_deployed_index

    Update an existing DeployedIndex under an IndexEndpoint.

    :param index_endpoint: Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60;
    :type index_endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1DeployedIndex.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_read_index_datapoints(request: web.Request, index_endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_read_index_datapoints

    Reads the datapoints/vectors of the given IDs. A maximum of 1000 datapoints can be retrieved in a batch.

    :param index_endpoint: Required. The name of the index endpoint. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60;
    :type index_endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ReadIndexDatapointsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_index_endpoints_undeploy_index(request: web.Request, index_endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_index_endpoints_undeploy_index

    Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it&#39;s using.

    :param index_endpoint: Required. The name of the IndexEndpoint resource from which to undeploy an Index. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60;
    :type index_endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1UndeployIndexRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_indexes_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_indexes_create

    Creates an Index.

    :param parent: Required. The resource name of the Location to create the Index in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Index.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_indexes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_indexes_list

    Lists Indexes in a Location.

    :param parent: Required. The resource name of the Location from which to list the Indexes. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListIndexesResponse.next_page_token of the previous IndexService.ListIndexes call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_indexes_remove_datapoints(request: web.Request, index, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_indexes_remove_datapoints

    Remove Datapoints from an Index.

    :param index: Required. The name of the Index resource to be updated. Format: &#x60;projects/{project}/locations/{location}/indexes/{index}&#x60;
    :type index: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1RemoveDatapointsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_indexes_upsert_datapoints(request: web.Request, index, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_indexes_upsert_datapoints

    Add/update Datapoints into an Index.

    :param index: Required. The name of the Index resource to be updated. Format: &#x60;projects/{project}/locations/{location}/indexes/{index}&#x60;
    :type index: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1UpsertDatapointsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_list

    Lists information about the supported locations for this service.

    :param name: The resource that owns the locations collection, if applicable.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
    :type filter: str
    :param page_size: The maximum number of results to return. If not set, the service selects a default.
    :type page_size: int
    :param page_token: A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_artifacts_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, artifact_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_artifacts_create

    Creates an Artifact associated with a MetadataStore.

    :param parent: Required. The resource name of the MetadataStore where the Artifact should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param artifact_id: The {artifact} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}&#x60; If not provided, the Artifact&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all Artifacts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting Artifact.)
    :type artifact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Artifact.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_artifacts_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_artifacts_list

    Lists Artifacts in the MetadataStore.

    :param parent: Required. The MetadataStore whose Artifacts should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60;. Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;uri&#x60;, &#x60;state&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60; * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60;. For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60; In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; * **Context based filtering**: To filter Artifacts based on the contexts to which they belong, use the function operator with the full resource name &#x60;in_context()&#x60;. For example: &#x60;in_context(\&quot;projects//locations//metadataStores//contexts/\&quot;)&#x60; Each of the above supported filter types can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;.
    :type filter: str
    :param order_by: How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \&quot; desc\&quot; suffix; for example: \&quot;foo desc, bar\&quot;. Subfields are specified with a &#x60;.&#x60; character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.
    :type order_by: str
    :param page_size: The maximum number of Artifacts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous MetadataService.ListArtifacts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_artifacts_purge(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_artifacts_purge

    Purges Artifacts.

    :param parent: Required. The metadata store to purge Artifacts from. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1PurgeArtifactsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_artifacts_query_artifact_lineage_subgraph(request: web.Request, artifact, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, max_hops=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_artifacts_query_artifact_lineage_subgraph

    Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

    :param artifact: Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}&#x60; The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.
    :type artifact: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the Lineage Subgraph. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60; Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;uri&#x60;, &#x60;state&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60; * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60;. For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60; In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; Each of the above supported filter types can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;.
    :type filter: str
    :param max_hops: Specifies the size of the lineage graph in terms of number of hops from the specified artifact. Negative Value: INVALID_ARGUMENT error is returned 0: Only input artifact is returned. No value: Transitive closure is performed to return the complete graph.
    :type max_hops: int

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_add_context_artifacts_and_executions(request: web.Request, context, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_add_context_artifacts_and_executions

    Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

    :param context: Required. The resource name of the Context that the Artifacts and Executions belong to. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60;
    :type context: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_add_context_children(request: web.Request, context, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_add_context_children

    Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

    :param context: Required. The resource name of the parent Context. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60;
    :type context: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1AddContextChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, context_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_create

    Creates a Context associated with a MetadataStore.

    :param parent: Required. The resource name of the MetadataStore where the Context should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param context_id: The {context} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60;. If not provided, the Context&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all Contexts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting Context.)
    :type context_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Context.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_list

    Lists Contexts on the MetadataStore.

    :param parent: Required. The MetadataStore whose Contexts should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Filter specifying the boolean condition for the Contexts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60;. Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60;. * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60;. For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60;. In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; * **Parent Child filtering**: To filter Contexts based on parent-child relationship use the HAS operator as follows: &#x60;&#x60;&#x60; parent_contexts: \&quot;projects//locations//metadataStores//contexts/\&quot; child_contexts: \&quot;projects//locations//metadataStores//contexts/\&quot; &#x60;&#x60;&#x60; Each of the above supported filters can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;.
    :type filter: str
    :param order_by: How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \&quot; desc\&quot; suffix; for example: \&quot;foo desc, bar\&quot;. Subfields are specified with a &#x60;.&#x60; character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.
    :type order_by: str
    :param page_size: The maximum number of Contexts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous MetadataService.ListContexts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_purge(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_purge

    Purges Contexts.

    :param parent: Required. The metadata store to purge Contexts from. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1PurgeContextsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_query_context_lineage_subgraph(request: web.Request, context, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_query_context_lineage_subgraph

    Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

    :param context: Required. The resource name of the Context whose Artifacts and Executions should be retrieved as a LineageSubgraph. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60; The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.
    :type context: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_contexts_remove_context_children(request: web.Request, context, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_contexts_remove_context_children

    Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

    :param context: Required. The resource name of the parent Context. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60;
    :type context: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1RemoveContextChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, metadata_store_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_create

    Initializes a MetadataStore, including allocation of resources.

    :param parent: Required. The resource name of the Location where the MetadataStore should be created. Format: &#x60;projects/{project}/locations/{location}/&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param metadata_store_id: The {metadatastore} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; If not provided, the MetadataStore&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting MetadataStore.)
    :type metadata_store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1MetadataStore.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_executions_add_execution_events(request: web.Request, execution, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_executions_add_execution_events

    Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

    :param execution: Required. The resource name of the Execution that the Events connect Artifacts with. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60;
    :type execution: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1AddExecutionEventsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_executions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, execution_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_executions_create

    Creates an Execution associated with a MetadataStore.

    :param parent: Required. The resource name of the MetadataStore where the Execution should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param execution_id: The {execution} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60; If not provided, the Execution&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting Execution.)
    :type execution_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Execution.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_executions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_executions_list

    Lists Executions in the MetadataStore.

    :param parent: Required. The MetadataStore whose Executions should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Filter specifying the boolean condition for the Executions to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60;. Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;state&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60;. * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60; For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60; In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; * **Context based filtering**: To filter Executions based on the contexts to which they belong use the function operator with the full resource name: &#x60;in_context()&#x60;. For example: &#x60;in_context(\&quot;projects//locations//metadataStores//contexts/\&quot;)&#x60; Each of the above supported filters can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;.
    :type filter: str
    :param order_by: How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \&quot; desc\&quot; suffix; for example: \&quot;foo desc, bar\&quot;. Subfields are specified with a &#x60;.&#x60; character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.
    :type order_by: str
    :param page_size: The maximum number of Executions to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous MetadataService.ListExecutions call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with an INVALID_ARGUMENT error.)
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_executions_purge(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_executions_purge

    Purges Executions.

    :param parent: Required. The metadata store to purge Executions from. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1PurgeExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_executions_query_execution_inputs_and_outputs(request: web.Request, execution, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_executions_query_execution_inputs_and_outputs

    Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

    :param execution: Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60;
    :type execution: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_list

    Lists MetadataStores for a Location.

    :param parent: Required. The Location whose MetadataStores should be listed. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of Metadata Stores to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous MetadataService.ListMetadataStores call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_metadata_schemas_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, metadata_schema_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_metadata_schemas_create

    Creates a MetadataSchema.

    :param parent: Required. The resource name of the MetadataStore where the MetadataSchema should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param metadata_schema_id: The {metadata_schema} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}&#x60; If not provided, the MetadataStore&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all MetadataSchemas in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting MetadataSchema.)
    :type metadata_schema_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1MetadataSchema.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_metadata_stores_metadata_schemas_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_metadata_stores_metadata_schemas_list

    Lists MetadataSchemas.

    :param parent: Required. The MetadataStore whose MetadataSchemas should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: A query to filter available MetadataSchemas for matching results.
    :type filter: str
    :param page_size: The maximum number of MetadataSchemas to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous MetadataService.ListMetadataSchemas call. Provide this to retrieve the next page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_migratable_resources_batch_migrate(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_migratable_resources_batch_migrate

    Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

    :param parent: Required. The location of the migrated resource will live in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchMigrateResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_migratable_resources_search(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_migratable_resources_search

    Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI&#39;s given location.

    :param parent: Required. The location that the migratable resources should be searched from. It&#39;s the Vertex AI location that the resources can be migrated to, not the resources&#39; original location. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1SearchMigratableResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_model_deployment_monitoring_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_model_deployment_monitoring_jobs_create

    Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

    :param parent: Required. The parent of the ModelDeploymentMonitoringJob. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ModelDeploymentMonitoringJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_model_deployment_monitoring_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_model_deployment_monitoring_jobs_list

    Lists ModelDeploymentMonitoringJobs in a Location.

    :param parent: Required. The parent of the ModelDeploymentMonitoringJob. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60;
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_model_deployment_monitoring_jobs_search_model_deployment_monitoring_stats_anomalies(request: web.Request, model_deployment_monitoring_job, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_model_deployment_monitoring_jobs_search_model_deployment_monitoring_stats_anomalies

    Searches Model Monitoring Statistics generated within a given time window.

    :param model_deployment_monitoring_job: Required. ModelDeploymentMonitoring Job resource name. Format: &#x60;projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}&#x60;
    :type model_deployment_monitoring_job: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_copy(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_copy

    Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

    :param parent: Required. The resource name of the Location into which to copy the Model. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1CopyModelRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_delete_version(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """aiplatform_projects_locations_models_delete_version

    Deletes a Model version. Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

    :param name: Required. The name of the model version to be deleted, with a version ID explicitly included. Example: &#x60;projects/{project}/locations/{location}/models/{model}@1234&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_models_evaluations_import(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_evaluations_import

    Imports an externally generated ModelEvaluation.

    :param parent: Required. The name of the parent model resource. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ImportModelEvaluationRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_evaluations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_models_evaluations_list

    Lists ModelEvaluations in a Model.

    :param parent: Required. The resource name of the Model to list the ModelEvaluations from. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListModelEvaluationsResponse.next_page_token of the previous ModelService.ListModelEvaluations call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_models_evaluations_slices_batch_import(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_evaluations_slices_batch_import

    Imports a list of externally generated EvaluatedAnnotations.

    :param parent: Required. The name of the parent ModelEvaluationSlice resource. Format: &#x60;projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_evaluations_slices_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_models_evaluations_slices_list

    Lists ModelEvaluationSlices in a ModelEvaluation.

    :param parent: Required. The resource name of the ModelEvaluation to list the ModelEvaluationSlices from. Format: &#x60;projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. * &#x60;slice.dimension&#x60; - for &#x3D;.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListModelEvaluationSlicesResponse.next_page_token of the previous ModelService.ListModelEvaluationSlices call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_models_export(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_export

    Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

    :param name: Required. The resource name of the Model to export. The resource name may contain version id or version alias to specify the version, if no version is specified, the default version will be exported.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ExportModelRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_models_list

    Lists Models in a Location.

    :param parent: Required. The resource name of the Location to list the Models from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;model&#x60; supports &#x3D; and !&#x3D;. &#x60;model&#x60; represents the Model ID, i.e. the last segment of the Model&#39;s resource name. * &#x60;display_name&#x60; supports &#x3D; and !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;model&#x3D;1234&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60;
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;.
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListModelsResponse.next_page_token of the previous ModelService.ListModels call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_models_list_versions(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_models_list_versions

    Lists versions of the specified model.

    :param name: Required. The name of the model to list versions for.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60;
    :type filter: str
    :param order_by: A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;update_time asc, create_time desc&#x60;.
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via next_page_token of the previous ListModelVersions call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_models_merge_version_aliases(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_merge_version_aliases

    Merges a set of aliases for a Model version.

    :param name: Required. The name of the model version to merge aliases, with a version ID explicitly included. Example: &#x60;projects/{project}/locations/{location}/models/{model}@1234&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1MergeVersionAliasesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_update_explanation_dataset(request: web.Request, model, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_update_explanation_dataset

    Incrementally update the dataset used for an examples model.

    :param model: Required. The resource name of the Model to update. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60;
    :type model: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1UpdateExplanationDatasetRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_models_upload(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_models_upload

    Uploads a Model artifact into Vertex AI.

    :param parent: Required. The resource name of the Location into which to upload the Model. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1UploadModelRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_nas_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_nas_jobs_create

    Creates a NasJob

    :param parent: Required. The resource name of the Location to create the NasJob in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1NasJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_nas_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_nas_jobs_list

    Lists NasJobs in a Location.

    :param parent: Required. The resource name of the Location to list the NasJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60;
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListNasJobsResponse.next_page_token of the previous JobService.ListNasJobs call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_nas_jobs_nas_trial_details_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_nas_jobs_nas_trial_details_list

    List top NasTrialDetails of a NasJob.

    :param parent: Required. The name of the NasJob resource. Format: &#x60;projects/{project}/locations/{location}/nasJobs/{nas_job}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListNasTrialDetailsResponse.next_page_token of the previous JobService.ListNasTrialDetails call.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtime_templates_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, notebook_runtime_template_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtime_templates_create

    Creates a NotebookRuntimeTemplate.

    :param parent: Required. The resource name of the Location to create the NotebookRuntimeTemplate. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param notebook_runtime_template_id: Optional. User specified ID for the notebook runtime template.
    :type notebook_runtime_template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1NotebookRuntimeTemplate.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtime_templates_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, options_requested_policy_version=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtime_templates_get_iam_policy

    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

    :param resource: REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param options_requested_policy_version: Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtime_templates_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtime_templates_list

    Lists NotebookRuntimeTemplates in a Location.

    :param parent: Required. The resource name of the Location from which to list the NotebookRuntimeTemplates. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;notebookRuntimeTemplate&#x60; supports &#x3D; and !&#x3D;. &#x60;notebookRuntimeTemplate&#x60; represents the NotebookRuntimeTemplate ID, i.e. the last segment of the NotebookRuntimeTemplate&#39;s resource name. * &#x60;display_name&#x60; supports &#x3D; and !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. * &#x60;notebookRuntimeType&#x60; supports &#x3D; and !&#x3D;. notebookRuntimeType enum: [USER_DEFINED, ONE_CLICK]. Some examples: * &#x60;notebookRuntimeTemplate&#x3D;notebookRuntimeTemplate123&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; * &#x60;notebookRuntimeType&#x3D;USER_DEFINED&#x60;
    :type filter: str
    :param order_by: Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;.
    :type order_by: str
    :param page_size: Optional. The standard list page size.
    :type page_size: int
    :param page_token: Optional. The standard list page token. Typically obtained via ListNotebookRuntimeTemplatesResponse.next_page_token of the previous NotebookService.ListNotebookRuntimeTemplates call.
    :type page_token: str
    :param read_mask: Optional. Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtime_templates_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtime_templates_set_iam_policy

    Sets the access control policy on the specified resource. Replaces any existing policy. Can return &#x60;NOT_FOUND&#x60;, &#x60;INVALID_ARGUMENT&#x60;, and &#x60;PERMISSION_DENIED&#x60; errors.

    :param resource: REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleIamV1SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtime_templates_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, permissions=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtime_templates_test_iam_permissions

    Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a &#x60;NOT_FOUND&#x60; error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param permissions: The set of permissions to check for the &#x60;resource&#x60;. Permissions with wildcards (such as &#x60;*&#x60; or &#x60;storage.*&#x60;) are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).
    :type permissions: List[str]

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtimes_assign(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtimes_assign

    Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

    :param parent: Required. The resource name of the Location to get the NotebookRuntime assignment. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1AssignNotebookRuntimeRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtimes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtimes_list

    Lists NotebookRuntimes in a Location.

    :param parent: Required. The resource name of the Location from which to list the NotebookRuntimes. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;notebookRuntime&#x60; supports &#x3D; and !&#x3D;. &#x60;notebookRuntime&#x60; represents the NotebookRuntime ID, i.e. the last segment of the NotebookRuntime&#39;s resource name. * &#x60;displayName&#x60; supports &#x3D; and !&#x3D; and regex. * &#x60;notebookRuntimeTemplate&#x60; supports &#x3D; and !&#x3D;. &#x60;notebookRuntimeTemplate&#x60; represents the NotebookRuntimeTemplate ID, i.e. the last segment of the NotebookRuntimeTemplate&#39;s resource name. * &#x60;healthState&#x60; supports &#x3D; and !&#x3D;. healthState enum: [HEALTHY, UNHEALTHY, HEALTH_STATE_UNSPECIFIED]. * &#x60;runtimeState&#x60; supports &#x3D; and !&#x3D;. runtimeState enum: [RUNTIME_STATE_UNSPECIFIED, RUNNING, BEING_STARTED, BEING_STOPPED, STOPPED, BEING_UPGRADED]. * &#x60;runtimeUser&#x60; supports &#x3D; and !&#x3D;. * API version is UI only: &#x60;uiState&#x60; supports &#x3D; and !&#x3D;. uiState enum: [UI_RESOURCE_STATE_UNSPECIFIED, UI_RESOURCE_STATE_BEING_CREATED, UI_RESOURCE_STATE_ACTIVE, UI_RESOURCE_STATE_BEING_DELETED, UI_RESOURCE_STATE_CREATION_FAILED]. * &#x60;notebookRuntimeType&#x60; supports &#x3D; and !&#x3D;. notebookRuntimeType enum: [USER_DEFINED, ONE_CLICK]. Some examples: * &#x60;notebookRuntime&#x3D;\&quot;notebookRuntime123\&quot;&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; and &#x60;displayName&#x3D;~\&quot;myDisplayNameRegex\&quot;&#x60; * &#x60;notebookRuntimeTemplate&#x3D;\&quot;notebookRuntimeTemplate321\&quot;&#x60; * &#x60;healthState&#x3D;HEALTHY&#x60; * &#x60;runtimeState&#x3D;RUNNING&#x60; * &#x60;runtimeUser&#x3D;\&quot;test@google.com\&quot;&#x60; * &#x60;uiState&#x3D;UI_RESOURCE_STATE_BEING_DELETED&#x60; * &#x60;notebookRuntimeType&#x3D;USER_DEFINED&#x60;
    :type filter: str
    :param order_by: Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;.
    :type order_by: str
    :param page_size: Optional. The standard list page size.
    :type page_size: int
    :param page_token: Optional. The standard list page token. Typically obtained via ListNotebookRuntimesResponse.next_page_token of the previous NotebookService.ListNotebookRuntimes call.
    :type page_token: str
    :param read_mask: Optional. Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtimes_start(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtimes_start

    Starts a NotebookRuntime.

    :param name: Required. The name of the NotebookRuntime resource to be started. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_notebook_runtimes_upgrade(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_notebook_runtimes_upgrade

    Upgrades a NotebookRuntime.

    :param name: Required. The name of the NotebookRuntime resource to be upgrade. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_pipeline_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, pipeline_job_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_pipeline_jobs_create

    Creates a PipelineJob. A PipelineJob will run immediately when created.

    :param parent: Required. The resource name of the Location to create the PipelineJob in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param pipeline_job_id: The ID to use for the PipelineJob, which will become the final component of the PipelineJob name. If not provided, an ID will be automatically generated. This value should be less than 128 characters, and valid characters are &#x60;/a-z-/&#x60;.
    :type pipeline_job_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1PipelineJob.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_pipeline_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_pipeline_jobs_list

    Lists PipelineJobs in a Location.

    :param parent: Required. The resource name of the Location to list the PipelineJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the PipelineJobs that match the filter expression. The following fields are supported: * &#x60;pipeline_name&#x60;: Supports &#x60;&#x3D;&#x60; and &#x60;!&#x3D;&#x60; comparisons. * &#x60;display_name&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;pipeline_job_user_id&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. for example, can check if pipeline&#39;s display_name contains *step* by doing display_name:\\\&quot;*step*\\\&quot; * &#x60;state&#x60;: Supports &#x60;&#x3D;&#x60; and &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;end_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality and key presence. * &#x60;template_uri&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;template_metadata.version&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. Filter expressions can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). For example: &#x60;pipeline_name&#x3D;\&quot;test\&quot; AND create_time&gt;\&quot;2020-05-18T13:30:00Z\&quot;&#x60;. The syntax to define filter expression is based on https://google.aip.dev/160. Examples: * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot; OR update_time&gt;\&quot;2020-05-18T00:00:00Z\&quot;&#x60; PipelineJobs created or updated after 2020-05-18 00:00:00 UTC. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; PipelineJobs with label \&quot;env\&quot; set to \&quot;prod\&quot;.
    :type filter: str
    :param order_by: A comma-separated list of fields to order by. The default sort order is in ascending order. Use \&quot;desc\&quot; after a field name for descending. You can have multiple order_by fields provided e.g. \&quot;create_time desc, end_time\&quot;, \&quot;end_time, start_time, update_time\&quot; For example, using \&quot;create_time desc, end_time\&quot; will order results by create time in descending order, and if there are multiple jobs having the same create time, order them by the end time in ascending order. if order_by is not specified, it will order by default order is create time in descending order. Supported fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; * &#x60;end_time&#x60; * &#x60;start_time&#x60;
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListPipelineJobsResponse.next_page_token of the previous PipelineService.ListPipelineJobs call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_compute_tokens(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_compute_tokens

    Return a list of tokens based on the input text.

    :param endpoint: Required. The name of the Endpoint requested to get lists of tokens and token ids.
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ComputeTokensRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_count_tokens(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_count_tokens

    Perform a token counting.

    :param endpoint: Required. The name of the Endpoint requested to perform token counting. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1CountTokensRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_generate_content(request: web.Request, model, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_generate_content

    Generate content with multimodal inputs.

    :param model: Required. The name of the publisher model requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/publishers/*/models/*&#x60;
    :type model: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1GenerateContentRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_predict(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_predict

    Perform an online prediction.

    :param endpoint: Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1PredictRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_raw_predict(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_raw_predict

    Perform an online prediction with an arbitrary HTTP payload. The response includes the following HTTP headers: * &#x60;X-Vertex-AI-Endpoint-Id&#x60;: ID of the Endpoint that served this prediction. * &#x60;X-Vertex-AI-Deployed-Model-Id&#x60;: ID of the Endpoint&#39;s DeployedModel that served this prediction.

    :param endpoint: Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1RawPredictRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_server_streaming_predict(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_server_streaming_predict

    Perform a server-side streaming online prediction request for Vertex LLM streaming.

    :param endpoint: Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1StreamingPredictRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_stream_generate_content(request: web.Request, model, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_stream_generate_content

    Generate content with multimodal inputs with streaming support.

    :param model: Required. The name of the publisher model requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/publishers/*/models/*&#x60;
    :type model: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1GenerateContentRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_publishers_models_stream_raw_predict(request: web.Request, endpoint, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_publishers_models_stream_raw_predict

    Perform a streaming online prediction with an arbitrary HTTP payload.

    :param endpoint: Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60;
    :type endpoint: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1StreamRawPredictRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_schedules_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_schedules_create

    Creates a Schedule.

    :param parent: Required. The resource name of the Location to create the Schedule in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Schedule.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_schedules_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_schedules_list

    Lists Schedules in a Location.

    :param parent: Required. The resource name of the Location to list the Schedules from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the Schedules that match the filter expression. The following fields are supported: * &#x60;display_name&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60;: Supports &#x60;&#x3D;&#x60; and &#x60;!&#x3D;&#x60; comparisons. * &#x60;request&#x60;: Supports existence of the check. (e.g. &#x60;create_pipeline_job_request:*&#x60; --&gt; Schedule has create_pipeline_job_request). * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;start_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;end_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons and &#x60;:*&#x60; existence check. Values must be in RFC 3339 format. * &#x60;next_run_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. Filter expressions can be combined together using logical operators (&#x60;NOT&#x60;, &#x60;AND&#x60; &amp; &#x60;OR&#x60;). The syntax to define filter expression is based on https://google.aip.dev/160. Examples: * &#x60;state&#x3D;\&quot;ACTIVE\&quot; AND display_name:\&quot;my_schedule_*\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_schedule\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;end_time&gt;\&quot;2021-05-18T00:00:00Z\&quot; OR NOT end_time:*&#x60; * &#x60;create_pipeline_job_request:*&#x60;
    :type filter: str
    :param order_by: A comma-separated list of fields to order by. The default sort order is in ascending order. Use \&quot;desc\&quot; after a field name for descending. You can have multiple order_by fields provided. For example, using \&quot;create_time desc, end_time\&quot; will order results by create time in descending order, and if there are multiple schedules having the same create time, order them by the end time in ascending order. If order_by is not specified, it will order by default with create_time in descending order. Supported fields: * &#x60;create_time&#x60; * &#x60;start_time&#x60; * &#x60;end_time&#x60; * &#x60;next_run_time&#x60;
    :type order_by: str
    :param page_size: The standard list page size. Default to 100 if not specified.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListSchedulesResponse.next_page_token of the previous ScheduleService.ListSchedules call.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_schedules_pause(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_schedules_pause

    Pauses a Schedule. Will mark Schedule.state to &#39;PAUSED&#39;. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

    :param name: Required. The name of the Schedule resource to be paused. Format: &#x60;projects/{project}/locations/{location}/schedules/{schedule}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_schedules_resume(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_schedules_resume

    Resumes a paused Schedule to start scheduling new runs. Will mark Schedule.state to &#39;ACTIVE&#39;. Only paused Schedule can be resumed. When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If Schedule.catchUp is set up true, all missed runs will be scheduled for backfill first.

    :param name: Required. The name of the Schedule resource to be resumed. Format: &#x60;projects/{project}/locations/{location}/schedules/{schedule}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ResumeScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_specialist_pools_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_specialist_pools_create

    Creates a SpecialistPool.

    :param parent: Required. The parent Project name for the new SpecialistPool. The form is &#x60;projects/{project}/locations/{location}&#x60;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1SpecialistPool.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_specialist_pools_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_specialist_pools_list

    Lists SpecialistPools in a Location.

    :param parent: Required. The name of the SpecialistPool&#39;s parent resource. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained by ListSpecialistPoolsResponse.next_page_token of the previous SpecialistPoolService.ListSpecialistPools call. Return first page if empty.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read. FieldMask represents a set of
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_create

    Creates a Study. A resource name will be generated after creation of the Study.

    :param parent: Required. The resource name of the Location to create the CustomJob in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Study.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_studies_list

    Lists all the studies in a region for an associated project.

    :param parent: Required. The resource name of the Location to list the Study from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Optional. The maximum number of studies to return per \&quot;page\&quot; of results. If unspecified, service will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_lookup(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_lookup

    Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

    :param parent: Required. The resource name of the Location to get the Study from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1LookupStudyRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_add_trial_measurement(request: web.Request, trial_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_add_trial_measurement

    Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete.

    :param trial_name: Required. The name of the trial to add measurement. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60;
    :type trial_name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1AddTrialMeasurementRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_check_trial_early_stopping_state(request: web.Request, trial_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_check_trial_early_stopping_state

    Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse.

    :param trial_name: Required. The Trial&#39;s name. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60;
    :type trial_name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_complete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_complete

    Marks a Trial as complete.

    :param name: Required. The Trial&#39;s name. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1CompleteTrialRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_create

    Adds a user provided Trial to a Study.

    :param parent: Required. The resource name of the Study to create the Trial in. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Trial.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_list

    Lists the Trials associated with a Study.

    :param parent: Required. The resource name of the Study to list the Trial from. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Optional. The number of Trials to retrieve per \&quot;page\&quot; of results. If unspecified, the service will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_list_optimal_trials(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_list_optimal_trials

    Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency

    :param parent: Required. The name of the Study that the optimal Trial belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_stop(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_stop

    Stops a Trial.

    :param name: Required. The Trial&#39;s name. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_studies_trials_suggest(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_studies_trials_suggest

    Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse.

    :param parent: Required. The project and location that the Study belongs to. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1SuggestTrialsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_batch_read(request: web.Request, tensorboard, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, time_series=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_batch_read

    Reads multiple TensorboardTimeSeries&#39; data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

    :param tensorboard: Required. The resource name of the Tensorboard containing TensorboardTimeSeries to read data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60;. The TensorboardTimeSeries referenced by time_series must be sub resources of this Tensorboard.
    :type tensorboard: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param time_series: Required. The resource names of the TensorboardTimeSeries to read data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60;
    :type time_series: List[str]

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_create

    Creates a Tensorboard.

    :param parent: Required. The resource name of the Location to create the Tensorboard in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1Tensorboard.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_batch_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_batch_create

    Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

    :param parent: Required. The resource name of the TensorboardExperiment to create the TensorboardTimeSeries in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; The TensorboardRuns referenced by the parent fields in the CreateTensorboardTimeSeriesRequest messages must be sub resources of this TensorboardExperiment.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, tensorboard_experiment_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_create

    Creates a TensorboardExperiment.

    :param parent: Required. The resource name of the Tensorboard to create the TensorboardExperiment in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param tensorboard_experiment_id: Required. The ID to use for the Tensorboard experiment, which becomes the final component of the Tensorboard experiment&#39;s resource name. This value should be 1-128 characters, and valid characters are &#x60;/a-z-/&#x60;.
    :type tensorboard_experiment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1TensorboardExperiment.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_list

    Lists TensorboardExperiments in a Location.

    :param parent: Required. The resource name of the Tensorboard to list TensorboardExperiments. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the TensorboardExperiments that match the filter expression.
    :type filter: str
    :param order_by: Field to use to sort the list.
    :type order_by: str
    :param page_size: The maximum number of TensorboardExperiments to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardExperiments are returned. The maximum value is 1000; values above 1000 are coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous TensorboardService.ListTensorboardExperiments call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardExperiments must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_batch_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_batch_create

    Batch create TensorboardRuns.

    :param parent: Required. The resource name of the TensorboardExperiment to create the TensorboardRuns in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; The parent field in the CreateTensorboardRunRequest messages must match this field.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, tensorboard_run_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_create

    Creates a TensorboardRun.

    :param parent: Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param tensorboard_run_id: Required. The ID to use for the Tensorboard run, which becomes the final component of the Tensorboard run&#39;s resource name. This value should be 1-128 characters, and valid characters are &#x60;/a-z-/&#x60;.
    :type tensorboard_run_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1TensorboardRun.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_list

    Lists TensorboardRuns in a Location.

    :param parent: Required. The resource name of the TensorboardExperiment to list TensorboardRuns. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the TensorboardRuns that match the filter expression.
    :type filter: str
    :param order_by: Field to use to sort the list.
    :type order_by: str
    :param page_size: The maximum number of TensorboardRuns to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardRuns are returned. The maximum value is 1000; values above 1000 are coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous TensorboardService.ListTensorboardRuns call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardRuns must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_time_series_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, tensorboard_time_series_id=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_time_series_create

    Creates a TensorboardTimeSeries.

    :param parent: Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param tensorboard_time_series_id: Optional. The user specified unique ID to use for the TensorboardTimeSeries, which becomes the final component of the TensorboardTimeSeries&#39;s resource name. This value should match \&quot;a-z0-9{0, 127}\&quot;
    :type tensorboard_time_series_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1TensorboardTimeSeries.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_time_series_export_tensorboard_time_series(request: web.Request, tensorboard_time_series, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_time_series_export_tensorboard_time_series

    Exports a TensorboardTimeSeries&#39; data. Data is returned in paginated responses.

    :param tensorboard_time_series: Required. The resource name of the TensorboardTimeSeries to export data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60;
    :type tensorboard_time_series: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_time_series_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_time_series_list

    Lists TensorboardTimeSeries in a Location.

    :param parent: Required. The resource name of the TensorboardRun to list TensorboardTimeSeries. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the TensorboardTimeSeries that match the filter expression.
    :type filter: str
    :param order_by: Field to use to sort the list.
    :type order_by: str
    :param page_size: The maximum number of TensorboardTimeSeries to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardTimeSeries are returned. The maximum value is 1000; values above 1000 are coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous TensorboardService.ListTensorboardTimeSeries call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardTimeSeries must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_time_series_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_time_series_patch

    Updates a TensorboardTimeSeries.

    :param name: Output only. Name of the TensorboardTimeSeries.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Required. Field mask is used to specify the fields to be overwritten in the TensorboardTimeSeries resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it&#39;s in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1TensorboardTimeSeries.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read(request: web.Request, tensorboard_time_series, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, max_data_points=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read

    Reads a TensorboardTimeSeries&#39; data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can&#39;t be greater than 10k.

    :param tensorboard_time_series: Required. The resource name of the TensorboardTimeSeries to read data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60;
    :type tensorboard_time_series: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Reads the TensorboardTimeSeries&#39; data that match the filter expression.
    :type filter: str
    :param max_data_points: The maximum number of TensorboardTimeSeries&#39; data to return. This value should be a positive integer. This value can be set to -1 to return all data.
    :type max_data_points: int

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read_blob_data(request: web.Request, time_series, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, blob_ids=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read_blob_data

    Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project&#39;s Cloud Storage bucket without users having to obtain Cloud Storage access permission.

    :param time_series: Required. The resource name of the TensorboardTimeSeries to list Blobs. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60;
    :type time_series: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param blob_ids: IDs of the blobs to read.
    :type blob_ids: List[str]

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_runs_write(request: web.Request, tensorboard_run, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_runs_write

    Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

    :param tensorboard_run: Required. The resource name of the TensorboardRun to write data to. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60;
    :type tensorboard_run: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1WriteTensorboardRunDataRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_experiments_write(request: web.Request, tensorboard_experiment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_experiments_write

    Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun&#39;s. If any data fail to be ingested, an error is returned.

    :param tensorboard_experiment: Required. The resource name of the TensorboardExperiment to write data to. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60;
    :type tensorboard_experiment: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_list

    Lists Tensorboards in a Location.

    :param parent: Required. The resource name of the Location to list Tensorboards. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Lists the Tensorboards that match the filter expression.
    :type filter: str
    :param order_by: Field to use to sort the list.
    :type order_by: str
    :param page_size: The maximum number of Tensorboards to return. The service may return fewer than this value. If unspecified, at most 100 Tensorboards are returned. The maximum value is 100; values above 100 are coerced to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous TensorboardService.ListTensorboards call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboards must match the call that provided the page token.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_read_size(request: web.Request, tensorboard, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_read_size

    Returns the storage size for a given TensorBoard instance.

    :param tensorboard: Required. The name of the Tensorboard resource. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60;
    :type tensorboard: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_tensorboards_read_usage(request: web.Request, tensorboard, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """aiplatform_projects_locations_tensorboards_read_usage

    Returns a list of monthly active users for a given TensorBoard instance.

    :param tensorboard: Required. The name of the Tensorboard resource. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60;
    :type tensorboard: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_training_pipelines_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_training_pipelines_create

    Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

    :param parent: Required. The resource name of the Location to create the TrainingPipeline in. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAiplatformV1TrainingPipeline.from_dict(body)
    return web.Response(status=200)


async def aiplatform_projects_locations_training_pipelines_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """aiplatform_projects_locations_training_pipelines_list

    Lists TrainingPipelines in a Location.

    :param parent: Required. The resource name of the Location to list the TrainingPipelines from. Format: &#x60;projects/{project}/locations/{location}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;training_task_definition&#x60; &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;PIPELINE_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_pipeline_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;PIPELINE_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_pipeline\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_pipeline\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;training_task_definition:\&quot;*automl_text_classification*\&quot;&#x60;
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token. Typically obtained via ListTrainingPipelinesResponse.next_page_token of the previous PipelineService.ListTrainingPipelines call.
    :type page_token: str
    :param read_mask: Mask specifying which fields to read.
    :type read_mask: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_training_pipelines_operations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """aiplatform_projects_locations_training_pipelines_operations_cancel

    Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

    :param name: The name of the operation resource to be cancelled.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_training_pipelines_operations_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, force=None) -> web.Response:
    """aiplatform_projects_locations_training_pipelines_operations_delete

    Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;.

    :param name: The name of the operation resource to be deleted.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param force: If set to true, any specialist managers in this SpecialistPool will also be deleted. (Otherwise, the request will only work if the SpecialistPool has no specialist managers.)
    :type force: bool

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_training_pipelines_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """aiplatform_projects_locations_training_pipelines_operations_list

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

    :param name: The name of the operation&#39;s parent resource.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def aiplatform_projects_locations_training_pipelines_operations_wait(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, timeout=None) -> web.Response:
    """aiplatform_projects_locations_training_pipelines_operations_wait

    Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. If the operation is already done, the latest state is immediately returned. If the timeout specified is greater than the default HTTP/RPC timeout, the HTTP/RPC timeout is used. If the server does not support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Note that this method is on a best-effort basis. It may return the latest state before the specified timeout (including immediately), meaning even an immediate response is no guarantee that the operation is done.

    :param name: The name of the operation resource to wait on.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param timeout: The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used.
    :type timeout: str

    """
    return web.Response(status=200)
