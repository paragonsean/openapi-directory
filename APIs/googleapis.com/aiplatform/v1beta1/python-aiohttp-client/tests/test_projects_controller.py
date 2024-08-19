# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_api_http_body import GoogleApiHttpBody
from openapi_server.models.google_cloud_aiplatform_v1beta1_add_context_artifacts_and_executions_request import GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_add_context_children_request import GoogleCloudAiplatformV1beta1AddContextChildrenRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_add_execution_events_request import GoogleCloudAiplatformV1beta1AddExecutionEventsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_add_trial_measurement_request import GoogleCloudAiplatformV1beta1AddTrialMeasurementRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_artifact import GoogleCloudAiplatformV1beta1Artifact
from openapi_server.models.google_cloud_aiplatform_v1beta1_assign_notebook_runtime_request import GoogleCloudAiplatformV1beta1AssignNotebookRuntimeRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_cancel_pipeline_jobs_request import GoogleCloudAiplatformV1beta1BatchCancelPipelineJobsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_create_features_request import GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_create_tensorboard_runs_request import GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_create_tensorboard_runs_response import GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_create_tensorboard_time_series_request import GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_create_tensorboard_time_series_response import GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_delete_pipeline_jobs_request import GoogleCloudAiplatformV1beta1BatchDeletePipelineJobsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_import_evaluated_annotations_request import GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_import_evaluated_annotations_response import GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_migrate_resources_request import GoogleCloudAiplatformV1beta1BatchMigrateResourcesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_prediction_job import GoogleCloudAiplatformV1beta1BatchPredictionJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_read_feature_values_request import GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_batch_read_tensorboard_time_series_data_response import GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_complete_trial_request import GoogleCloudAiplatformV1beta1CompleteTrialRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_compute_tokens_request import GoogleCloudAiplatformV1beta1ComputeTokensRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_compute_tokens_response import GoogleCloudAiplatformV1beta1ComputeTokensResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_context import GoogleCloudAiplatformV1beta1Context
from openapi_server.models.google_cloud_aiplatform_v1beta1_copy_model_request import GoogleCloudAiplatformV1beta1CopyModelRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_count_tokens_request import GoogleCloudAiplatformV1beta1CountTokensRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_count_tokens_response import GoogleCloudAiplatformV1beta1CountTokensResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_create_deployment_resource_pool_request import GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_custom_job import GoogleCloudAiplatformV1beta1CustomJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_data_labeling_job import GoogleCloudAiplatformV1beta1DataLabelingJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_dataset import GoogleCloudAiplatformV1beta1Dataset
from openapi_server.models.google_cloud_aiplatform_v1beta1_dataset_version import GoogleCloudAiplatformV1beta1DatasetVersion
from openapi_server.models.google_cloud_aiplatform_v1beta1_delete_feature_values_request import GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_deploy_index_request import GoogleCloudAiplatformV1beta1DeployIndexRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_deploy_model_request import GoogleCloudAiplatformV1beta1DeployModelRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_deployed_index import GoogleCloudAiplatformV1beta1DeployedIndex
from openapi_server.models.google_cloud_aiplatform_v1beta1_direct_predict_request import GoogleCloudAiplatformV1beta1DirectPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_direct_predict_response import GoogleCloudAiplatformV1beta1DirectPredictResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_direct_raw_predict_request import GoogleCloudAiplatformV1beta1DirectRawPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_direct_raw_predict_response import GoogleCloudAiplatformV1beta1DirectRawPredictResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_endpoint import GoogleCloudAiplatformV1beta1Endpoint
from openapi_server.models.google_cloud_aiplatform_v1beta1_entity_type import GoogleCloudAiplatformV1beta1EntityType
from openapi_server.models.google_cloud_aiplatform_v1beta1_execution import GoogleCloudAiplatformV1beta1Execution
from openapi_server.models.google_cloud_aiplatform_v1beta1_explain_request import GoogleCloudAiplatformV1beta1ExplainRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_explain_response import GoogleCloudAiplatformV1beta1ExplainResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_export_feature_values_request import GoogleCloudAiplatformV1beta1ExportFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_export_model_request import GoogleCloudAiplatformV1beta1ExportModelRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_export_tensorboard_time_series_data_request import GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_export_tensorboard_time_series_data_response import GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_feature import GoogleCloudAiplatformV1beta1Feature
from openapi_server.models.google_cloud_aiplatform_v1beta1_feature_group import GoogleCloudAiplatformV1beta1FeatureGroup
from openapi_server.models.google_cloud_aiplatform_v1beta1_feature_online_store import GoogleCloudAiplatformV1beta1FeatureOnlineStore
from openapi_server.models.google_cloud_aiplatform_v1beta1_feature_view import GoogleCloudAiplatformV1beta1FeatureView
from openapi_server.models.google_cloud_aiplatform_v1beta1_featurestore import GoogleCloudAiplatformV1beta1Featurestore
from openapi_server.models.google_cloud_aiplatform_v1beta1_fetch_feature_values_request import GoogleCloudAiplatformV1beta1FetchFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_fetch_feature_values_response import GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_find_neighbors_request import GoogleCloudAiplatformV1beta1FindNeighborsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_find_neighbors_response import GoogleCloudAiplatformV1beta1FindNeighborsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_generate_access_token_request import GoogleCloudAiplatformV1beta1GenerateAccessTokenRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_generate_access_token_response import GoogleCloudAiplatformV1beta1GenerateAccessTokenResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_generate_content_request import GoogleCloudAiplatformV1beta1GenerateContentRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_generate_content_response import GoogleCloudAiplatformV1beta1GenerateContentResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_hyperparameter_tuning_job import GoogleCloudAiplatformV1beta1HyperparameterTuningJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_import_data_request import GoogleCloudAiplatformV1beta1ImportDataRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_import_feature_values_request import GoogleCloudAiplatformV1beta1ImportFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_import_model_evaluation_request import GoogleCloudAiplatformV1beta1ImportModelEvaluationRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_index import GoogleCloudAiplatformV1beta1Index
from openapi_server.models.google_cloud_aiplatform_v1beta1_index_endpoint import GoogleCloudAiplatformV1beta1IndexEndpoint
from openapi_server.models.google_cloud_aiplatform_v1beta1_lineage_subgraph import GoogleCloudAiplatformV1beta1LineageSubgraph
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_annotations_response import GoogleCloudAiplatformV1beta1ListAnnotationsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_artifacts_response import GoogleCloudAiplatformV1beta1ListArtifactsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_batch_prediction_jobs_response import GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_contexts_response import GoogleCloudAiplatformV1beta1ListContextsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_custom_jobs_response import GoogleCloudAiplatformV1beta1ListCustomJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_data_items_response import GoogleCloudAiplatformV1beta1ListDataItemsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_data_labeling_jobs_response import GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_dataset_versions_response import GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_datasets_response import GoogleCloudAiplatformV1beta1ListDatasetsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_deployment_resource_pools_response import GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_endpoints_response import GoogleCloudAiplatformV1beta1ListEndpointsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_entity_types_response import GoogleCloudAiplatformV1beta1ListEntityTypesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_executions_response import GoogleCloudAiplatformV1beta1ListExecutionsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_feature_groups_response import GoogleCloudAiplatformV1beta1ListFeatureGroupsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_feature_online_stores_response import GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_feature_view_syncs_response import GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_feature_views_response import GoogleCloudAiplatformV1beta1ListFeatureViewsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_features_response import GoogleCloudAiplatformV1beta1ListFeaturesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_featurestores_response import GoogleCloudAiplatformV1beta1ListFeaturestoresResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_hyperparameter_tuning_jobs_response import GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_index_endpoints_response import GoogleCloudAiplatformV1beta1ListIndexEndpointsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_indexes_response import GoogleCloudAiplatformV1beta1ListIndexesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_metadata_schemas_response import GoogleCloudAiplatformV1beta1ListMetadataSchemasResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_metadata_stores_response import GoogleCloudAiplatformV1beta1ListMetadataStoresResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_model_deployment_monitoring_jobs_response import GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_model_evaluation_slices_response import GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_model_evaluations_response import GoogleCloudAiplatformV1beta1ListModelEvaluationsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_model_versions_response import GoogleCloudAiplatformV1beta1ListModelVersionsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_nas_jobs_response import GoogleCloudAiplatformV1beta1ListNasJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_nas_trial_details_response import GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_notebook_runtime_templates_response import GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_notebook_runtimes_response import GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_optimal_trials_response import GoogleCloudAiplatformV1beta1ListOptimalTrialsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_persistent_resources_response import GoogleCloudAiplatformV1beta1ListPersistentResourcesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_pipeline_jobs_response import GoogleCloudAiplatformV1beta1ListPipelineJobsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_saved_queries_response import GoogleCloudAiplatformV1beta1ListSavedQueriesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_schedules_response import GoogleCloudAiplatformV1beta1ListSchedulesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_specialist_pools_response import GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_studies_response import GoogleCloudAiplatformV1beta1ListStudiesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_tensorboard_experiments_response import GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_tensorboard_runs_response import GoogleCloudAiplatformV1beta1ListTensorboardRunsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_tensorboard_time_series_response import GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_tensorboards_response import GoogleCloudAiplatformV1beta1ListTensorboardsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_training_pipelines_response import GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_list_trials_response import GoogleCloudAiplatformV1beta1ListTrialsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_lookup_study_request import GoogleCloudAiplatformV1beta1LookupStudyRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_merge_version_aliases_request import GoogleCloudAiplatformV1beta1MergeVersionAliasesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_metadata_schema import GoogleCloudAiplatformV1beta1MetadataSchema
from openapi_server.models.google_cloud_aiplatform_v1beta1_metadata_store import GoogleCloudAiplatformV1beta1MetadataStore
from openapi_server.models.google_cloud_aiplatform_v1beta1_model import GoogleCloudAiplatformV1beta1Model
from openapi_server.models.google_cloud_aiplatform_v1beta1_model_deployment_monitoring_job import GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_model_evaluation import GoogleCloudAiplatformV1beta1ModelEvaluation
from openapi_server.models.google_cloud_aiplatform_v1beta1_mutate_deployed_model_request import GoogleCloudAiplatformV1beta1MutateDeployedModelRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_nas_job import GoogleCloudAiplatformV1beta1NasJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_notebook_runtime_template import GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate
from openapi_server.models.google_cloud_aiplatform_v1beta1_persistent_resource import GoogleCloudAiplatformV1beta1PersistentResource
from openapi_server.models.google_cloud_aiplatform_v1beta1_pipeline_job import GoogleCloudAiplatformV1beta1PipelineJob
from openapi_server.models.google_cloud_aiplatform_v1beta1_predict_request import GoogleCloudAiplatformV1beta1PredictRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_predict_response import GoogleCloudAiplatformV1beta1PredictResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_purge_artifacts_request import GoogleCloudAiplatformV1beta1PurgeArtifactsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_purge_contexts_request import GoogleCloudAiplatformV1beta1PurgeContextsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_purge_executions_request import GoogleCloudAiplatformV1beta1PurgeExecutionsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_query_deployed_models_response import GoogleCloudAiplatformV1beta1QueryDeployedModelsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_raw_predict_request import GoogleCloudAiplatformV1beta1RawPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_feature_values_request import GoogleCloudAiplatformV1beta1ReadFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_feature_values_response import GoogleCloudAiplatformV1beta1ReadFeatureValuesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_index_datapoints_request import GoogleCloudAiplatformV1beta1ReadIndexDatapointsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_index_datapoints_response import GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_tensorboard_blob_data_response import GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_tensorboard_size_response import GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_tensorboard_time_series_data_response import GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_read_tensorboard_usage_response import GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_remove_context_children_request import GoogleCloudAiplatformV1beta1RemoveContextChildrenRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_remove_datapoints_request import GoogleCloudAiplatformV1beta1RemoveDatapointsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_report_runtime_event_request import GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_report_runtime_event_response import GoogleCloudAiplatformV1beta1ReportRuntimeEventResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_resume_schedule_request import GoogleCloudAiplatformV1beta1ResumeScheduleRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_schedule import GoogleCloudAiplatformV1beta1Schedule
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_data_items_response import GoogleCloudAiplatformV1beta1SearchDataItemsResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_features_response import GoogleCloudAiplatformV1beta1SearchFeaturesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_migratable_resources_request import GoogleCloudAiplatformV1beta1SearchMigratableResourcesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_migratable_resources_response import GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_model_deployment_monitoring_stats_anomalies_request import GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_model_deployment_monitoring_stats_anomalies_response import GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_nearest_entities_request import GoogleCloudAiplatformV1beta1SearchNearestEntitiesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_search_nearest_entities_response import GoogleCloudAiplatformV1beta1SearchNearestEntitiesResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_specialist_pool import GoogleCloudAiplatformV1beta1SpecialistPool
from openapi_server.models.google_cloud_aiplatform_v1beta1_streaming_predict_request import GoogleCloudAiplatformV1beta1StreamingPredictRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_streaming_predict_response import GoogleCloudAiplatformV1beta1StreamingPredictResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_streaming_read_feature_values_request import GoogleCloudAiplatformV1beta1StreamingReadFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_study import GoogleCloudAiplatformV1beta1Study
from openapi_server.models.google_cloud_aiplatform_v1beta1_suggest_trials_request import GoogleCloudAiplatformV1beta1SuggestTrialsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_sync_feature_view_response import GoogleCloudAiplatformV1beta1SyncFeatureViewResponse
from openapi_server.models.google_cloud_aiplatform_v1beta1_tensorboard import GoogleCloudAiplatformV1beta1Tensorboard
from openapi_server.models.google_cloud_aiplatform_v1beta1_tensorboard_experiment import GoogleCloudAiplatformV1beta1TensorboardExperiment
from openapi_server.models.google_cloud_aiplatform_v1beta1_tensorboard_run import GoogleCloudAiplatformV1beta1TensorboardRun
from openapi_server.models.google_cloud_aiplatform_v1beta1_tensorboard_time_series import GoogleCloudAiplatformV1beta1TensorboardTimeSeries
from openapi_server.models.google_cloud_aiplatform_v1beta1_training_pipeline import GoogleCloudAiplatformV1beta1TrainingPipeline
from openapi_server.models.google_cloud_aiplatform_v1beta1_trial import GoogleCloudAiplatformV1beta1Trial
from openapi_server.models.google_cloud_aiplatform_v1beta1_undeploy_index_request import GoogleCloudAiplatformV1beta1UndeployIndexRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_undeploy_model_request import GoogleCloudAiplatformV1beta1UndeployModelRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_update_explanation_dataset_request import GoogleCloudAiplatformV1beta1UpdateExplanationDatasetRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_upload_model_request import GoogleCloudAiplatformV1beta1UploadModelRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_upsert_datapoints_request import GoogleCloudAiplatformV1beta1UpsertDatapointsRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_write_feature_values_request import GoogleCloudAiplatformV1beta1WriteFeatureValuesRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_write_tensorboard_experiment_data_request import GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataRequest
from openapi_server.models.google_cloud_aiplatform_v1beta1_write_tensorboard_run_data_request import GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.google_iam_v1_get_iam_policy_request import GoogleIamV1GetIamPolicyRequest
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_batch_prediction_jobs_create(client):
    """Test case for aiplatform_projects_locations_batch_prediction_jobs_create

    
    """
    body = {"modelMonitoringStatus":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"inputConfig":{"bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"uris":["uris","uris"]},"instancesFormat":"instancesFormat"},"outputInfo":{"bigqueryOutputTable":"bigqueryOutputTable","bigqueryOutputDataset":"bigqueryOutputDataset","gcsOutputDirectory":"gcsOutputDirectory"},"displayName":"displayName","modelVersionId":"modelVersionId","outputConfig":{"predictionsFormat":"predictionsFormat","gcsDestination":{"outputUriPrefix":"outputUriPrefix"},"bigqueryDestination":{"outputUri":"outputUri"}},"completionStats":{"successfulForecastPointCount":"successfulForecastPointCount","failedCount":"failedCount","incompleteCount":"incompleteCount","successfulCount":"successfulCount"},"encryptionSpec":{"kmsKeyName":"kmsKeyName"},"instanceConfig":{"keyField":"keyField","excludedFields":["excludedFields","excludedFields"],"instanceType":"instanceType","includedFields":["includedFields","includedFields"]},"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"partialFailures":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"model":"model","startTime":"startTime","state":"JOB_STATE_UNSPECIFIED","unmanagedContainerModel":{"containerSpec":{"args":["args","args"],"healthProbe":{"periodSeconds":6,"timeoutSeconds":1,"exec":{"command":["command","command"]}},"imageUri":"imageUri","deploymentTimeout":"deploymentTimeout","predictRoute":"predictRoute","sharedMemorySizeMb":"sharedMemorySizeMb","grpcPorts":[{"containerPort":0},{"containerPort":0}],"startupProbe":{"periodSeconds":6,"timeoutSeconds":1,"exec":{"command":["command","command"]}},"env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"healthRoute":"healthRoute","ports":[{"containerPort":0},{"containerPort":0}],"command":["command","command"]},"predictSchemata":{"instanceSchemaUri":"instanceSchemaUri","parametersSchemaUri":"parametersSchemaUri","predictionSchemaUri":"predictionSchemaUri"},"artifactUri":"artifactUri"},"modelMonitoringConfig":{"statsAnomaliesBaseDirectory":{"outputUriPrefix":"outputUriPrefix"},"analysisInstanceSchemaUri":"analysisInstanceSchemaUri","objectiveConfigs":[{"predictionDriftDetectionConfig":{"attributionScoreDriftThresholds":{"key":{"value":6.027456183070403}},"defaultDriftThreshold":{"value":6.027456183070403},"driftThresholds":{"key":{"value":6.027456183070403}}},"trainingPredictionSkewDetectionConfig":{"defaultSkewThreshold":{"value":6.027456183070403},"skewThresholds":{"key":{"value":6.027456183070403}},"attributionScoreSkewThresholds":{"key":{"value":6.027456183070403}}},"explanationConfig":{"explanationBaseline":{"gcs":{"outputUriPrefix":"outputUriPrefix"},"predictionFormat":"PREDICTION_FORMAT_UNSPECIFIED","bigquery":{"outputUri":"outputUri"}},"enableFeatureAttributes":True},"trainingDataset":{"loggingSamplingStrategy":{"randomSampleConfig":{"sampleRate":5.962133916683182}},"targetField":"targetField","dataFormat":"dataFormat","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"uris":["uris","uris"]},"dataset":"dataset"}},{"predictionDriftDetectionConfig":{"attributionScoreDriftThresholds":{"key":{"value":6.027456183070403}},"defaultDriftThreshold":{"value":6.027456183070403},"driftThresholds":{"key":{"value":6.027456183070403}}},"trainingPredictionSkewDetectionConfig":{"defaultSkewThreshold":{"value":6.027456183070403},"skewThresholds":{"key":{"value":6.027456183070403}},"attributionScoreSkewThresholds":{"key":{"value":6.027456183070403}}},"explanationConfig":{"explanationBaseline":{"gcs":{"outputUriPrefix":"outputUriPrefix"},"predictionFormat":"PREDICTION_FORMAT_UNSPECIFIED","bigquery":{"outputUri":"outputUri"}},"enableFeatureAttributes":True},"trainingDataset":{"loggingSamplingStrategy":{"randomSampleConfig":{"sampleRate":5.962133916683182}},"targetField":"targetField","dataFormat":"dataFormat","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"uris":["uris","uris"]},"dataset":"dataset"}}],"alertConfig":{"emailAlertConfig":{"userEmails":["userEmails","userEmails"]},"notificationChannels":["notificationChannels","notificationChannels"],"enableLogging":True}},"serviceAccount":"serviceAccount","updateTime":"updateTime","manualBatchTuningParameters":{"batchSize":1},"modelMonitoringStatsAnomalies":[{"featureStats":[{"featureDisplayName":"featureDisplayName","trainingStats":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"predictionStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"threshold":{"value":6.027456183070403}},{"featureDisplayName":"featureDisplayName","trainingStats":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"predictionStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"threshold":{"value":6.027456183070403}}],"deployedModelId":"deployedModelId","anomalyCount":0,"objective":"MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED"},{"featureStats":[{"featureDisplayName":"featureDisplayName","trainingStats":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"predictionStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"threshold":{"value":6.027456183070403}},{"featureDisplayName":"featureDisplayName","trainingStats":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"predictionStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"threshold":{"value":6.027456183070403}}],"deployedModelId":"deployedModelId","anomalyCount":0,"objective":"MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED"}],"labels":{"key":"labels"},"disableContainerLogging":True,"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"modelParameters":"","createTime":"createTime","name":"name","resourcesConsumed":{"replicaHours":5.637376656633329},"dedicatedResources":{"startingReplicaCount":6,"maxReplicaCount":0,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"endTime":"endTime","generateExplanation":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/batchPredictionJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_batch_prediction_jobs_list(client):
    """Test case for aiplatform_projects_locations_batch_prediction_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/batchPredictionJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_custom_jobs_create(client):
    """Test case for aiplatform_projects_locations_custom_jobs_create

    
    """
    body = {"jobSpec":{"models":["models","models"],"workerPoolSpecs":[{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}}],"protectedArtifactLocationId":"protectedArtifactLocationId","serviceAccount":"serviceAccount","network":"network","tensorboard":"tensorboard","enableWebAccess":True,"experiment":"experiment","persistentResourceId":"persistentResourceId","experimentRun":"experimentRun","enableDashboardAccess":True,"scheduling":{"restartJobOnWorkerRestart":True,"disableRetries":True,"timeout":"timeout"},"reservedIpRanges":["reservedIpRanges","reservedIpRanges"],"baseOutputDirectory":{"outputUriPrefix":"outputUriPrefix"}},"webAccessUris":{"key":"webAccessUris"},"createTime":"createTime","displayName":"displayName","name":"name","startTime":"startTime","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"endTime":"endTime","state":"JOB_STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/customJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_custom_jobs_list(client):
    """Test case for aiplatform_projects_locations_custom_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/customJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_data_labeling_jobs_create(client):
    """Test case for aiplatform_projects_locations_data_labeling_jobs_create

    
    """
    body = {"inputsSchemaUri":"inputsSchemaUri","annotationLabels":{"key":"annotationLabels"},"activeLearningConfig":{"trainingConfig":{"timeoutTrainingMilliHours":"timeoutTrainingMilliHours"},"maxDataItemCount":"maxDataItemCount","maxDataItemPercentage":0,"sampleConfig":{"sampleStrategy":"SAMPLE_STRATEGY_UNSPECIFIED","initialBatchSamplePercentage":1,"followingBatchSamplePercentage":6}},"displayName":"displayName","inputs":"","currentSpend":{"nanos":5,"units":"units","currencyCode":"currencyCode"},"updateTime":"updateTime","datasets":["datasets","datasets"],"encryptionSpec":{"kmsKeyName":"kmsKeyName"},"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"instructionUri":"instructionUri","labels":{"key":"labels"},"labelingProgress":2,"createTime":"createTime","specialistPools":["specialistPools","specialistPools"],"name":"name","labelerCount":5,"state":"JOB_STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/dataLabelingJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_data_labeling_jobs_list(client):
    """Test case for aiplatform_projects_locations_data_labeling_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/dataLabelingJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_create(client):
    """Test case for aiplatform_projects_locations_datasets_create

    
    """
    body = {"metadata":"","displayName":"displayName","metadataSchemaUri":"metadataSchemaUri","description":"description","updateTime":"updateTime","dataItemCount":"dataItemCount","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"metadataArtifact":"metadataArtifact","labels":{"key":"labels"},"createTime":"createTime","savedQueries":[{"annotationFilter":"annotationFilter","metadata":"","annotationSpecCount":0,"createTime":"createTime","displayName":"displayName","name":"name","etag":"etag","updateTime":"updateTime","supportAutomlTraining":True,"problemType":"problemType"},{"annotationFilter":"annotationFilter","metadata":"","annotationSpecCount":0,"createTime":"createTime","displayName":"displayName","name":"name","etag":"etag","updateTime":"updateTime","supportAutomlTraining":True,"problemType":"problemType"}],"name":"name","etag":"etag"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_data_items_annotations_list(client):
    """Test case for aiplatform_projects_locations_datasets_data_items_annotations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/annotations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_data_items_list(client):
    """Test case for aiplatform_projects_locations_datasets_data_items_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/dataItems'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_dataset_versions_create(client):
    """Test case for aiplatform_projects_locations_datasets_dataset_versions_create

    
    """
    body = {"metadata":"","createTime":"createTime","displayName":"displayName","bigQueryDatasetName":"bigQueryDatasetName","name":"name","etag":"etag","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/datasetVersions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_dataset_versions_list(client):
    """Test case for aiplatform_projects_locations_datasets_dataset_versions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/datasetVersions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_dataset_versions_restore(client):
    """Test case for aiplatform_projects_locations_datasets_dataset_versions_restore

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{namerestor}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_import(client):
    """Test case for aiplatform_projects_locations_datasets_import

    
    """
    body = {"importConfigs":[{"annotationLabels":{"key":"annotationLabels"},"dataItemLabels":{"key":"dataItemLabels"},"gcsSource":{"uris":["uris","uris"]},"importSchemaUri":"importSchemaUri"},{"annotationLabels":{"key":"annotationLabels"},"dataItemLabels":{"key":"dataItemLabels"},"gcsSource":{"uris":["uris","uris"]},"importSchemaUri":"importSchemaUri"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameimpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_list(client):
    """Test case for aiplatform_projects_locations_datasets_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_saved_queries_list(client):
    """Test case for aiplatform_projects_locations_datasets_saved_queries_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/savedQueries'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_datasets_search_data_items(client):
    """Test case for aiplatform_projects_locations_datasets_search_data_items

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('annotationFilters', ['annotation_filters_example']),
                    ('annotationsFilter', 'annotations_filter_example'),
                    ('annotationsLimit', 56),
                    ('dataItemFilter', 'data_item_filter_example'),
                    ('dataLabelingJob', 'data_labeling_job_example'),
                    ('fieldMask', 'field_mask_example'),
                    ('orderBy', 'order_by_example'),
                    ('orderByAnnotation.orderBy', 'order_by_annotation_order_by_example'),
                    ('orderByAnnotation.savedQuery', 'order_by_annotation_saved_query_example'),
                    ('orderByDataItem', 'order_by_data_item_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('savedQuery', 'saved_query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{datasetsearch_data_item}'.format(dataset='dataset_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_deployment_resource_pools_create(client):
    """Test case for aiplatform_projects_locations_deployment_resource_pools_create

    
    """
    body = {"deploymentResourcePool":{"createTime":"createTime","name":"name","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}}},"deploymentResourcePoolId":"deploymentResourcePoolId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/deploymentResourcePools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_deployment_resource_pools_list(client):
    """Test case for aiplatform_projects_locations_deployment_resource_pools_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/deploymentResourcePools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_deployment_resource_pools_query_deployed_models(client):
    """Test case for aiplatform_projects_locations_deployment_resource_pools_query_deployed_models

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{deployment_resource_poolquery_deployed_model}'.format(deployment_resource_pool='deployment_resource_pool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_create(client):
    """Test case for aiplatform_projects_locations_endpoints_create

    
    """
    body = {"modelDeploymentMonitoringJob":"modelDeploymentMonitoringJob","enablePrivateServiceConnect":True,"displayName":"displayName","description":"description","predictRequestResponseLoggingConfig":{"bigqueryDestination":{"outputUri":"outputUri"},"samplingRate":0.8008281904610115,"enabled":True},"updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"labels":{"key":"labels"},"network":"network","privateServiceConnectConfig":{"enablePrivateServiceConnect":True,"projectAllowlist":["projectAllowlist","projectAllowlist"]},"createTime":"createTime","trafficSplit":{"key":6},"name":"name","etag":"etag","deployedModels":[{"enableContainerLogging":True,"displayName":"displayName","modelVersionId":"modelVersionId","privateEndpoints":{"explainHttpUri":"explainHttpUri","healthHttpUri":"healthHttpUri","serviceAttachment":"serviceAttachment","predictHttpUri":"predictHttpUri"},"disableExplanations":True,"serviceAccount":"serviceAccount","enableAccessLogging":True,"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"createTime":"createTime","sharedResources":"sharedResources","model":"model","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"id":"id"},{"enableContainerLogging":True,"displayName":"displayName","modelVersionId":"modelVersionId","privateEndpoints":{"explainHttpUri":"explainHttpUri","healthHttpUri":"healthHttpUri","serviceAttachment":"serviceAttachment","predictHttpUri":"predictHttpUri"},"disableExplanations":True,"serviceAccount":"serviceAccount","enableAccessLogging":True,"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"createTime":"createTime","sharedResources":"sharedResources","model":"model","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"id":"id"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('endpointId', 'endpoint_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/endpoints'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_deploy_model(client):
    """Test case for aiplatform_projects_locations_endpoints_deploy_model

    
    """
    body = {"deployedModel":{"enableContainerLogging":True,"displayName":"displayName","modelVersionId":"modelVersionId","privateEndpoints":{"explainHttpUri":"explainHttpUri","healthHttpUri":"healthHttpUri","serviceAttachment":"serviceAttachment","predictHttpUri":"predictHttpUri"},"disableExplanations":True,"serviceAccount":"serviceAccount","enableAccessLogging":True,"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"createTime":"createTime","sharedResources":"sharedResources","model":"model","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"id":"id"},"trafficSplit":{"key":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointdeploy_mode}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_direct_predict(client):
    """Test case for aiplatform_projects_locations_endpoints_direct_predict

    
    """
    body = {"inputs":[{"doubleVal":[0.8008281904610115,0.8008281904610115],"intVal":[1,1],"shape":["shape","shape"],"stringVal":["stringVal","stringVal"],"dtype":"DATA_TYPE_UNSPECIFIED","bytesVal":["bytesVal","bytesVal"],"floatVal":[6.0274563,6.0274563],"boolVal":[True,True],"uintVal":[5,5],"structVal":{},"int64Val":["int64Val","int64Val"],"uint64Val":["uint64Val","uint64Val"],"listVal":[null,null],"tensorVal":"tensorVal"},{"doubleVal":[0.8008281904610115,0.8008281904610115],"intVal":[1,1],"shape":["shape","shape"],"stringVal":["stringVal","stringVal"],"dtype":"DATA_TYPE_UNSPECIFIED","bytesVal":["bytesVal","bytesVal"],"floatVal":[6.0274563,6.0274563],"boolVal":[True,True],"uintVal":[5,5],"structVal":{},"int64Val":["int64Val","int64Val"],"uint64Val":["uint64Val","uint64Val"],"listVal":[null,null],"tensorVal":"tensorVal"}],"parameters":{"doubleVal":[0.8008281904610115,0.8008281904610115],"intVal":[1,1],"shape":["shape","shape"],"stringVal":["stringVal","stringVal"],"dtype":"DATA_TYPE_UNSPECIFIED","bytesVal":["bytesVal","bytesVal"],"floatVal":[6.0274563,6.0274563],"boolVal":[True,True],"uintVal":[5,5],"structVal":{},"int64Val":["int64Val","int64Val"],"uint64Val":["uint64Val","uint64Val"],"listVal":[null,null],"tensorVal":"tensorVal"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointdirect_predic}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_direct_raw_predict(client):
    """Test case for aiplatform_projects_locations_endpoints_direct_raw_predict

    
    """
    body = {"input":"input","methodName":"methodName"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointdirect_raw_predic}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_explain(client):
    """Test case for aiplatform_projects_locations_endpoints_explain

    
    """
    body = {"concurrentExplanationSpecOverride":{"key":{"metadata":{"inputs":{"key":{"inputBaselines":["",""]}}},"examplesOverride":{"neighborCount":6,"dataFormat":"DATA_FORMAT_UNSPECIFIED","restrictions":[{"allow":["allow","allow"],"deny":["deny","deny"],"namespaceName":"namespaceName"},{"allow":["allow","allow"],"deny":["deny","deny"],"namespaceName":"namespaceName"}],"crowdingCount":0,"returnEmbeddings":True},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}}},"deployedModelId":"deployedModelId","explanationSpecOverride":{"metadata":{"inputs":{"key":{"inputBaselines":["",""]}}},"examplesOverride":{"neighborCount":6,"dataFormat":"DATA_FORMAT_UNSPECIFIED","restrictions":[{"allow":["allow","allow"],"deny":["deny","deny"],"namespaceName":"namespaceName"},{"allow":["allow","allow"],"deny":["deny","deny"],"namespaceName":"namespaceName"}],"crowdingCount":0,"returnEmbeddings":True},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"instances":["",""],"parameters":""}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointexplai}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_list(client):
    """Test case for aiplatform_projects_locations_endpoints_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/endpoints'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_mutate_deployed_model(client):
    """Test case for aiplatform_projects_locations_endpoints_mutate_deployed_model

    
    """
    body = {"deployedModel":{"enableContainerLogging":True,"displayName":"displayName","modelVersionId":"modelVersionId","privateEndpoints":{"explainHttpUri":"explainHttpUri","healthHttpUri":"healthHttpUri","serviceAttachment":"serviceAttachment","predictHttpUri":"predictHttpUri"},"disableExplanations":True,"serviceAccount":"serviceAccount","enableAccessLogging":True,"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"createTime":"createTime","sharedResources":"sharedResources","model":"model","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"id":"id"},"updateMask":"updateMask"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointmutate_deployed_mode}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_endpoints_undeploy_model(client):
    """Test case for aiplatform_projects_locations_endpoints_undeploy_model

    
    """
    body = {"deployedModelId":"deployedModelId","trafficSplit":{"key":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointundeploy_mode}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_groups_create(client):
    """Test case for aiplatform_projects_locations_feature_groups_create

    
    """
    body = {"createTime":"createTime","bigQuery":{"entityIdColumns":["entityIdColumns","entityIdColumns"],"bigQuerySource":{"inputUri":"inputUri"}},"name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('featureGroupId', 'feature_group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/featureGroups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_groups_list(client):
    """Test case for aiplatform_projects_locations_feature_groups_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/featureGroups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_create(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_create

    
    """
    body = {"createTime":"createTime","optimized":"{}","dedicatedServingEndpoint":{"publicEndpointDomainName":"publicEndpointDomainName","serviceAttachment":"serviceAttachment","privateServiceConnectConfig":{"enablePrivateServiceConnect":True,"projectAllowlist":["projectAllowlist","projectAllowlist"]}},"name":"name","bigtable":{"autoScaling":{"minNodeCount":1,"maxNodeCount":6,"cpuUtilizationTarget":0}},"embeddingManagement":{"enabled":True},"etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('featureOnlineStoreId', 'feature_online_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/featureOnlineStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_feature_views_create(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_feature_views_create

    
    """
    body = {"serviceAccountEmail":"serviceAccountEmail","vectorSearchConfig":{"bruteForceConfig":"{}","embeddingColumn":"embeddingColumn","crowdingColumn":"crowdingColumn","embeddingDimension":0,"filterColumns":["filterColumns","filterColumns"],"distanceMeasureType":"DISTANCE_MEASURE_TYPE_UNSPECIFIED","treeAhConfig":{"leafNodeEmbeddingCount":"leafNodeEmbeddingCount"}},"featureRegistrySource":{"featureGroups":[{"featureGroupId":"featureGroupId","featureIds":["featureIds","featureIds"]},{"featureGroupId":"featureGroupId","featureIds":["featureIds","featureIds"]}],"projectNumber":"projectNumber"},"createTime":"createTime","name":"name","syncConfig":{"cron":"cron"},"etag":"etag","updateTime":"updateTime","bigQuerySource":{"entityIdColumns":["entityIdColumns","entityIdColumns"],"uri":"uri"},"serviceAgentType":"SERVICE_AGENT_TYPE_UNSPECIFIED","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('featureViewId', 'feature_view_id_example'),
                    ('runSyncImmediately', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/featureViews'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_feature_views_feature_view_syncs_list(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_feature_views_feature_view_syncs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/featureViewSyncs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_feature_views_fetch_feature_values(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_feature_views_fetch_feature_values

    
    """
    body = {"dataKey":{"compositeKey":{"parts":["parts","parts"]},"key":"key"},"dataFormat":"FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED","format":"FORMAT_UNSPECIFIED","id":"id"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{feature_viewfetch_feature_value}'.format(feature_view='feature_view_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_feature_views_list(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_feature_views_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/featureViews'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_feature_views_search_nearest_entities(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_feature_views_search_nearest_entities

    
    """
    body = {"query":{"neighborCount":6,"stringFilters":[{"name":"name","allowTokens":["allowTokens","allowTokens"],"denyTokens":["denyTokens","denyTokens"]},{"name":"name","allowTokens":["allowTokens","allowTokens"],"denyTokens":["denyTokens","denyTokens"]}],"perCrowdingAttributeNeighborCount":5,"entityId":"entityId","embedding":{"value":[0.8008282,0.8008282]},"parameters":{"leafNodesSearchFraction":5.962133916683182,"approximateNeighborCandidates":1}},"returnFullEntity":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{feature_viewsearch_nearest_entitie}'.format(feature_view='feature_view_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_feature_views_sync(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_feature_views_sync

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{feature_viewsyn}'.format(feature_view='feature_view_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_feature_online_stores_list(client):
    """Test case for aiplatform_projects_locations_feature_online_stores_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/featureOnlineStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_batch_read_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_batch_read_feature_values

    
    """
    body = {"entityTypeSpecs":[{"settings":[{"featureId":"featureId","destinationField":"destinationField"},{"featureId":"featureId","destinationField":"destinationField"}],"entityTypeId":"entityTypeId","featureSelector":{"idMatcher":{"ids":["ids","ids"]}}},{"settings":[{"featureId":"featureId","destinationField":"destinationField"},{"featureId":"featureId","destinationField":"destinationField"}],"entityTypeId":"entityTypeId","featureSelector":{"idMatcher":{"ids":["ids","ids"]}}}],"destination":{"bigqueryDestination":{"outputUri":"outputUri"},"csvDestination":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"}},"tfrecordDestination":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"}}},"csvReadInstances":{"gcsSource":{"uris":["uris","uris"]}},"startTime":"startTime","bigqueryReadInstances":{"inputUri":"inputUri"},"passThroughFields":[{"fieldName":"fieldName"},{"fieldName":"fieldName"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{featurestorebatch_read_feature_value}'.format(featurestore='featurestore_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_create(client):
    """Test case for aiplatform_projects_locations_featurestores_create

    
    """
    body = {"createTime":"createTime","name":"name","etag":"etag","onlineServingConfig":{"scaling":{"minNodeCount":5,"maxNodeCount":1,"cpuUtilizationTarget":6},"fixedNodeCount":0},"updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"onlineStorageTtlDays":5,"state":"STATE_UNSPECIFIED","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('featurestoreId', 'featurestore_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/featurestores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_create(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_create

    
    """
    body = {"monitoringConfig":{"categoricalThresholdConfig":{"value":0.8008281904610115},"importFeaturesAnalysis":{"anomalyDetectionBaseline":"BASELINE_UNSPECIFIED","state":"STATE_UNSPECIFIED"},"snapshotAnalysis":{"stalenessDays":1,"monitoringInterval":"monitoringInterval","disabled":True,"monitoringIntervalDays":6},"numericalThresholdConfig":{"value":0.8008281904610115}},"offlineStorageTtlDays":0,"createTime":"createTime","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('entityTypeId', 'entity_type_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/entityTypes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_delete_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_delete_feature_values

    
    """
    body = {"selectEntity":{"entityIdSelector":{"entityIdField":"entityIdField","csvSource":{"gcsSource":{"uris":["uris","uris"]}}}},"selectTimeRangeAndFeature":{"skipOnlineStorageDelete":True,"featureSelector":{"idMatcher":{"ids":["ids","ids"]}},"timeRange":{"startTime":"startTime","endTime":"endTime"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{entity_typedelete_feature_value}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_export_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_export_feature_values

    
    """
    body = {"settings":[{"featureId":"featureId","destinationField":"destinationField"},{"featureId":"featureId","destinationField":"destinationField"}],"snapshotExport":{"startTime":"startTime","snapshotTime":"snapshotTime"},"fullExport":{"startTime":"startTime","endTime":"endTime"},"destination":{"bigqueryDestination":{"outputUri":"outputUri"},"csvDestination":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"}},"tfrecordDestination":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"}}},"featureSelector":{"idMatcher":{"ids":["ids","ids"]}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{entity_typeexport_feature_value}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_features_batch_create(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_features_batch_create

    
    """
    body = {"requests":[{"parent":"parent","feature":{"disableMonitoring":True,"description":"description","monitoringStatsAnomalies":[{"featureStatsAnomaly":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"objective":"OBJECTIVE_UNSPECIFIED"},{"featureStatsAnomaly":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"objective":"OBJECTIVE_UNSPECIFIED"}],"updateTime":"updateTime","labels":{"key":"labels"},"monitoringStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"versionColumnName":"versionColumnName","monitoringConfig":{"categoricalThresholdConfig":{"value":0.8008281904610115},"importFeaturesAnalysis":{"anomalyDetectionBaseline":"BASELINE_UNSPECIFIED","state":"STATE_UNSPECIFIED"},"snapshotAnalysis":{"stalenessDays":1,"monitoringInterval":"monitoringInterval","disabled":True,"monitoringIntervalDays":6},"numericalThresholdConfig":{"value":0.8008281904610115}},"createTime":"createTime","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","etag":"etag","pointOfContact":"pointOfContact"},"featureId":"featureId"},{"parent":"parent","feature":{"disableMonitoring":True,"description":"description","monitoringStatsAnomalies":[{"featureStatsAnomaly":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"objective":"OBJECTIVE_UNSPECIFIED"},{"featureStatsAnomaly":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"objective":"OBJECTIVE_UNSPECIFIED"}],"updateTime":"updateTime","labels":{"key":"labels"},"monitoringStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"versionColumnName":"versionColumnName","monitoringConfig":{"categoricalThresholdConfig":{"value":0.8008281904610115},"importFeaturesAnalysis":{"anomalyDetectionBaseline":"BASELINE_UNSPECIFIED","state":"STATE_UNSPECIFIED"},"snapshotAnalysis":{"stalenessDays":1,"monitoringInterval":"monitoringInterval","disabled":True,"monitoringIntervalDays":6},"numericalThresholdConfig":{"value":0.8008281904610115}},"createTime":"createTime","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","etag":"etag","pointOfContact":"pointOfContact"},"featureId":"featureId"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/features:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_features_create(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_features_create

    
    """
    body = {"disableMonitoring":True,"description":"description","monitoringStatsAnomalies":[{"featureStatsAnomaly":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"objective":"OBJECTIVE_UNSPECIFIED"},{"featureStatsAnomaly":{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},"objective":"OBJECTIVE_UNSPECIFIED"}],"updateTime":"updateTime","labels":{"key":"labels"},"monitoringStats":[{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"},{"anomalyDetectionThreshold":5.962133916683182,"score":2.3021358869347655,"statsUri":"statsUri","distributionDeviation":5.637376656633329,"startTime":"startTime","endTime":"endTime","anomalyUri":"anomalyUri"}],"versionColumnName":"versionColumnName","monitoringConfig":{"categoricalThresholdConfig":{"value":0.8008281904610115},"importFeaturesAnalysis":{"anomalyDetectionBaseline":"BASELINE_UNSPECIFIED","state":"STATE_UNSPECIFIED"},"snapshotAnalysis":{"stalenessDays":1,"monitoringInterval":"monitoringInterval","disabled":True,"monitoringIntervalDays":6},"numericalThresholdConfig":{"value":0.8008281904610115}},"createTime":"createTime","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","etag":"etag","pointOfContact":"pointOfContact"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('featureId', 'feature_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/features'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_features_list(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_features_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('latestStatsCount', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/features'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_import_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_import_feature_values

    
    """
    body = {"disableOnlineServing":True,"workerCount":0,"entityIdField":"entityIdField","featureTimeField":"featureTimeField","avroSource":{"gcsSource":{"uris":["uris","uris"]}},"csvSource":{"gcsSource":{"uris":["uris","uris"]}},"featureTime":"featureTime","featureSpecs":[{"sourceField":"sourceField","id":"id"},{"sourceField":"sourceField","id":"id"}],"bigquerySource":{"inputUri":"inputUri"},"disableIngestionAnalysis":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{entity_typeimport_feature_value}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_list(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/entityTypes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_read_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_read_feature_values

    
    """
    body = {"entityId":"entityId","featureSelector":{"idMatcher":{"ids":["ids","ids"]}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{entity_typeread_feature_value}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_streaming_read_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_streaming_read_feature_values

    
    """
    body = {"entityIds":["entityIds","entityIds"],"featureSelector":{"idMatcher":{"ids":["ids","ids"]}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{entity_typestreaming_read_feature_value}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_entity_types_write_feature_values(client):
    """Test case for aiplatform_projects_locations_featurestores_entity_types_write_feature_values

    
    """
    body = {"payloads":[{"entityId":"entityId","featureValues":{"key":{"int64Value":"int64Value","metadata":{"generateTime":"generateTime"},"stringValue":"stringValue","int64ArrayValue":{"values":["values","values"]},"boolValue":True,"doubleValue":6.027456183070403,"stringArrayValue":{"values":["values","values"]},"boolArrayValue":{"values":[True,True]},"bytesValue":"bytesValue","doubleArrayValue":{"values":[0.8008281904610115,0.8008281904610115]}}}},{"entityId":"entityId","featureValues":{"key":{"int64Value":"int64Value","metadata":{"generateTime":"generateTime"},"stringValue":"stringValue","int64ArrayValue":{"values":["values","values"]},"boolValue":True,"doubleValue":6.027456183070403,"stringArrayValue":{"values":["values","values"]},"boolArrayValue":{"values":[True,True]},"bytesValue":"bytesValue","doubleArrayValue":{"values":[0.8008281904610115,0.8008281904610115]}}}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{entity_typewrite_feature_value}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_list(client):
    """Test case for aiplatform_projects_locations_featurestores_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/featurestores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_featurestores_search_features(client):
    """Test case for aiplatform_projects_locations_featurestores_search_features

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{location}/featurestores:searchFeatures'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_hyperparameter_tuning_jobs_create(client):
    """Test case for aiplatform_projects_locations_hyperparameter_tuning_jobs_create

    
    """
    body = {"trialJobSpec":{"models":["models","models"],"workerPoolSpecs":[{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}}],"protectedArtifactLocationId":"protectedArtifactLocationId","serviceAccount":"serviceAccount","network":"network","tensorboard":"tensorboard","enableWebAccess":True,"experiment":"experiment","persistentResourceId":"persistentResourceId","experimentRun":"experimentRun","enableDashboardAccess":True,"scheduling":{"restartJobOnWorkerRestart":True,"disableRetries":True,"timeout":"timeout"},"reservedIpRanges":["reservedIpRanges","reservedIpRanges"],"baseOutputDirectory":{"outputUriPrefix":"outputUriPrefix"}},"displayName":"displayName","maxFailedTrialCount":0,"updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"parallelTrialCount":1,"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"studySpec":{"convexStopConfig":{"maxNumSteps":"maxNumSteps","useSeconds":True,"learningRateParameterName":"learningRateParameterName","minNumSteps":"minNumSteps","autoregressiveOrder":"autoregressiveOrder"},"medianAutomatedStoppingSpec":{"useElapsedDuration":True},"studyStoppingConfig":{"minimumRuntimeConstraint":{"endTime":"endTime","maxDuration":"maxDuration"},"maximumRuntimeConstraint":{"endTime":"endTime","maxDuration":"maxDuration"},"shouldStopAsap":True,"maxDurationNoProgress":"maxDurationNoProgress","maxNumTrialsNoProgress":1,"minNumTrials":1,"maxNumTrials":7},"transferLearningConfig":{"disableTransferLearning":True,"priorStudyNames":["priorStudyNames","priorStudyNames"]},"measurementSelectionType":"MEASUREMENT_SELECTION_TYPE_UNSPECIFIED","convexAutomatedStoppingSpec":{"minMeasurementCount":"minMeasurementCount","minStepCount":"minStepCount","useElapsedDuration":True,"learningRateParameterName":"learningRateParameterName","maxStepCount":"maxStepCount","updateAllStoppedTrials":True},"decayCurveStoppingSpec":{"useElapsedDuration":True},"metrics":[{"safetyConfig":{"safetyThreshold":5.637376656633329,"desiredMinSafeTrialsFraction":5.962133916683182},"goal":"GOAL_TYPE_UNSPECIFIED","metricId":"metricId"},{"safetyConfig":{"safetyThreshold":5.637376656633329,"desiredMinSafeTrialsFraction":5.962133916683182},"goal":"GOAL_TYPE_UNSPECIFIED","metricId":"metricId"}],"parameters":[{"categoricalValueSpec":{"defaultValue":"defaultValue","values":["values","values"]},"parameterId":"parameterId","scaleType":"SCALE_TYPE_UNSPECIFIED","conditionalParameterSpecs":[{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}},{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}}],"doubleValueSpec":{"minValue":4.145608029883936,"defaultValue":3.616076749251911,"maxValue":2.027123023002322},"integerValueSpec":{"minValue":"minValue","defaultValue":"defaultValue","maxValue":"maxValue"},"discreteValueSpec":{"defaultValue":7.061401241503109,"values":[9.301444243932576,9.301444243932576]}},{"categoricalValueSpec":{"defaultValue":"defaultValue","values":["values","values"]},"parameterId":"parameterId","scaleType":"SCALE_TYPE_UNSPECIFIED","conditionalParameterSpecs":[{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}},{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}}],"doubleValueSpec":{"minValue":4.145608029883936,"defaultValue":3.616076749251911,"maxValue":2.027123023002322},"integerValueSpec":{"minValue":"minValue","defaultValue":"defaultValue","maxValue":"maxValue"},"discreteValueSpec":{"defaultValue":7.061401241503109,"values":[9.301444243932576,9.301444243932576]}}],"observationNoise":"OBSERVATION_NOISE_UNSPECIFIED","algorithm":"ALGORITHM_UNSPECIFIED"},"trials":[{"customJob":"customJob","clientId":"clientId","infeasibleReason":"infeasibleReason","webAccessUris":{"key":"webAccessUris"},"name":"name","startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED","parameters":[{"parameterId":"parameterId","value":""},{"parameterId":"parameterId","value":""}],"measurements":[{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"}]},{"customJob":"customJob","clientId":"clientId","infeasibleReason":"infeasibleReason","webAccessUris":{"key":"webAccessUris"},"name":"name","startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED","parameters":[{"parameterId":"parameterId","value":""},{"parameterId":"parameterId","value":""}],"measurements":[{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"}]}],"createTime":"createTime","name":"name","maxTrialCount":6,"startTime":"startTime","endTime":"endTime","state":"JOB_STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/hyperparameterTuningJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_hyperparameter_tuning_jobs_list(client):
    """Test case for aiplatform_projects_locations_hyperparameter_tuning_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/hyperparameterTuningJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_create(client):
    """Test case for aiplatform_projects_locations_index_endpoints_create

    
    """
    body = {"enablePrivateServiceConnect":True,"publicEndpointDomainName":"publicEndpointDomainName","deployedIndexes":[{"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"indexSyncTime":"indexSyncTime","createTime":"createTime","displayName":"displayName","privateEndpoints":{"serviceAttachment":"serviceAttachment","pscAutomatedEndpoints":[{"matchAddress":"matchAddress","projectId":"projectId","network":"network"},{"matchAddress":"matchAddress","projectId":"projectId","network":"network"}],"matchGrpcAddress":"matchGrpcAddress"},"deploymentGroup":"deploymentGroup","deployedIndexAuthConfig":{"authProvider":{"allowedIssuers":["allowedIssuers","allowedIssuers"],"audiences":["audiences","audiences"]}},"index":"index","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"enableAccessLogging":True,"id":"id","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]},{"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"indexSyncTime":"indexSyncTime","createTime":"createTime","displayName":"displayName","privateEndpoints":{"serviceAttachment":"serviceAttachment","pscAutomatedEndpoints":[{"matchAddress":"matchAddress","projectId":"projectId","network":"network"},{"matchAddress":"matchAddress","projectId":"projectId","network":"network"}],"matchGrpcAddress":"matchGrpcAddress"},"deploymentGroup":"deploymentGroup","deployedIndexAuthConfig":{"authProvider":{"allowedIssuers":["allowedIssuers","allowedIssuers"],"audiences":["audiences","audiences"]}},"index":"index","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"enableAccessLogging":True,"id":"id","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]}],"displayName":"displayName","description":"description","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"labels":{"key":"labels"},"network":"network","privateServiceConnectConfig":{"enablePrivateServiceConnect":True,"projectAllowlist":["projectAllowlist","projectAllowlist"]},"createTime":"createTime","publicEndpointEnabled":True,"name":"name","etag":"etag"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/indexEndpoints'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_deploy_index(client):
    """Test case for aiplatform_projects_locations_index_endpoints_deploy_index

    
    """
    body = {"deployedIndex":{"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"indexSyncTime":"indexSyncTime","createTime":"createTime","displayName":"displayName","privateEndpoints":{"serviceAttachment":"serviceAttachment","pscAutomatedEndpoints":[{"matchAddress":"matchAddress","projectId":"projectId","network":"network"},{"matchAddress":"matchAddress","projectId":"projectId","network":"network"}],"matchGrpcAddress":"matchGrpcAddress"},"deploymentGroup":"deploymentGroup","deployedIndexAuthConfig":{"authProvider":{"allowedIssuers":["allowedIssuers","allowedIssuers"],"audiences":["audiences","audiences"]}},"index":"index","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"enableAccessLogging":True,"id":"id","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{index_endpointdeploy_inde}'.format(index_endpoint='index_endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_find_neighbors(client):
    """Test case for aiplatform_projects_locations_index_endpoints_find_neighbors

    
    """
    body = {"returnFullDatapoint":True,"deployedIndexId":"deployedIndexId","queries":[{"neighborCount":1,"datapoint":{"restricts":[{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]},{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]}],"crowdingTag":{"crowdingAttribute":"crowdingAttribute"},"featureVector":[0.8008282,0.8008282],"numericRestricts":[{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129},{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129}],"datapointId":"datapointId"},"approximateNeighborCount":0,"fractionLeafNodesToSearchOverride":6.027456183070403,"perCrowdingAttributeNeighborCount":5},{"neighborCount":1,"datapoint":{"restricts":[{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]},{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]}],"crowdingTag":{"crowdingAttribute":"crowdingAttribute"},"featureVector":[0.8008282,0.8008282],"numericRestricts":[{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129},{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129}],"datapointId":"datapointId"},"approximateNeighborCount":0,"fractionLeafNodesToSearchOverride":6.027456183070403,"perCrowdingAttributeNeighborCount":5}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{index_endpointfind_neighbor}'.format(index_endpoint='index_endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_list(client):
    """Test case for aiplatform_projects_locations_index_endpoints_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/indexEndpoints'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_mutate_deployed_index(client):
    """Test case for aiplatform_projects_locations_index_endpoints_mutate_deployed_index

    
    """
    body = {"automaticResources":{"minReplicaCount":6,"maxReplicaCount":0},"indexSyncTime":"indexSyncTime","createTime":"createTime","displayName":"displayName","privateEndpoints":{"serviceAttachment":"serviceAttachment","pscAutomatedEndpoints":[{"matchAddress":"matchAddress","projectId":"projectId","network":"network"},{"matchAddress":"matchAddress","projectId":"projectId","network":"network"}],"matchGrpcAddress":"matchGrpcAddress"},"deploymentGroup":"deploymentGroup","deployedIndexAuthConfig":{"authProvider":{"allowedIssuers":["allowedIssuers","allowedIssuers"],"audiences":["audiences","audiences"]}},"index":"index","dedicatedResources":{"autoscalingMetricSpecs":[{"metricName":"metricName","target":1},{"metricName":"metricName","target":1}],"minReplicaCount":2,"maxReplicaCount":5,"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},"enableAccessLogging":True,"id":"id","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{index_endpointmutate_deployed_inde}'.format(index_endpoint='index_endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_read_index_datapoints(client):
    """Test case for aiplatform_projects_locations_index_endpoints_read_index_datapoints

    
    """
    body = {"ids":["ids","ids"],"deployedIndexId":"deployedIndexId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{index_endpointread_index_datapoint}'.format(index_endpoint='index_endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_index_endpoints_undeploy_index(client):
    """Test case for aiplatform_projects_locations_index_endpoints_undeploy_index

    
    """
    body = {"deployedIndexId":"deployedIndexId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{index_endpointundeploy_inde}'.format(index_endpoint='index_endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_indexes_create(client):
    """Test case for aiplatform_projects_locations_indexes_create

    
    """
    body = {"metadata":"","deployedIndexes":[{"indexEndpoint":"indexEndpoint","displayName":"displayName","deployedIndexId":"deployedIndexId"},{"indexEndpoint":"indexEndpoint","displayName":"displayName","deployedIndexId":"deployedIndexId"}],"displayName":"displayName","metadataSchemaUri":"metadataSchemaUri","description":"description","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"labels":{"key":"labels"},"indexStats":{"shardsCount":0,"vectorsCount":"vectorsCount"},"createTime":"createTime","indexUpdateMethod":"INDEX_UPDATE_METHOD_UNSPECIFIED","name":"name","etag":"etag"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/indexes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_indexes_list(client):
    """Test case for aiplatform_projects_locations_indexes_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/indexes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_indexes_remove_datapoints(client):
    """Test case for aiplatform_projects_locations_indexes_remove_datapoints

    
    """
    body = {"datapointIds":["datapointIds","datapointIds"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{indexremove_datapoint}'.format(index='index_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_indexes_upsert_datapoints(client):
    """Test case for aiplatform_projects_locations_indexes_upsert_datapoints

    
    """
    body = {"datapoints":[{"restricts":[{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]},{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]}],"crowdingTag":{"crowdingAttribute":"crowdingAttribute"},"featureVector":[0.8008282,0.8008282],"numericRestricts":[{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129},{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129}],"datapointId":"datapointId"},{"restricts":[{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]},{"denyList":["denyList","denyList"],"namespace":"namespace","allowList":["allowList","allowList"]}],"crowdingTag":{"crowdingAttribute":"crowdingAttribute"},"featureVector":[0.8008282,0.8008282],"numericRestricts":[{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129},{"op":"OPERATOR_UNSPECIFIED","namespace":"namespace","valueDouble":6.027456183070403,"valueInt":"valueInt","valueFloat":1.4658129}],"datapointId":"datapointId"}],"updateMask":"updateMask"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{indexupsert_datapoint}'.format(index='index_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_list(client):
    """Test case for aiplatform_projects_locations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_artifacts_create(client):
    """Test case for aiplatform_projects_locations_metadata_stores_artifacts_create

    
    """
    body = {"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('artifactId', 'artifact_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/artifacts'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_artifacts_list(client):
    """Test case for aiplatform_projects_locations_metadata_stores_artifacts_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/artifacts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_artifacts_purge(client):
    """Test case for aiplatform_projects_locations_metadata_stores_artifacts_purge

    
    """
    body = {"filter":"filter","force":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/artifacts:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_artifacts_query_artifact_lineage_subgraph(client):
    """Test case for aiplatform_projects_locations_metadata_stores_artifacts_query_artifact_lineage_subgraph

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('maxHops', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{artifactquery_artifact_lineage_subgrap}'.format(artifact='artifact_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_add_context_artifacts_and_executions(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_add_context_artifacts_and_executions

    
    """
    body = {"executions":["executions","executions"],"artifacts":["artifacts","artifacts"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{contextadd_context_artifacts_and_execution}'.format(context='context_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_add_context_children(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_add_context_children

    
    """
    body = {"childContexts":["childContexts","childContexts"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{contextadd_context_childre}'.format(context='context_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_create(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_create

    
    """
    body = {"parentContexts":["parentContexts","parentContexts"],"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('contextId', 'context_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/contexts'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_list(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/contexts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_purge(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_purge

    
    """
    body = {"filter":"filter","force":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/contexts:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_query_context_lineage_subgraph(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_query_context_lineage_subgraph

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{contextquery_context_lineage_subgrap}'.format(context='context_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_contexts_remove_context_children(client):
    """Test case for aiplatform_projects_locations_metadata_stores_contexts_remove_context_children

    
    """
    body = {"childContexts":["childContexts","childContexts"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{contextremove_context_childre}'.format(context='context_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_create(client):
    """Test case for aiplatform_projects_locations_metadata_stores_create

    
    """
    body = {"createTime":"createTime","name":"name","description":"description","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"state":{"diskUtilizationBytes":"diskUtilizationBytes"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('metadataStoreId', 'metadata_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/metadataStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_executions_add_execution_events(client):
    """Test case for aiplatform_projects_locations_metadata_stores_executions_add_execution_events

    
    """
    body = {"events":[{"artifact":"artifact","execution":"execution","eventTime":"eventTime","type":"TYPE_UNSPECIFIED","labels":{"key":"labels"}},{"artifact":"artifact","execution":"execution","eventTime":"eventTime","type":"TYPE_UNSPECIFIED","labels":{"key":"labels"}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{executionadd_execution_event}'.format(execution='execution_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_executions_create(client):
    """Test case for aiplatform_projects_locations_metadata_stores_executions_create

    
    """
    body = {"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('executionId', 'execution_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/executions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_executions_list(client):
    """Test case for aiplatform_projects_locations_metadata_stores_executions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/executions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_executions_purge(client):
    """Test case for aiplatform_projects_locations_metadata_stores_executions_purge

    
    """
    body = {"filter":"filter","force":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/executions:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_executions_query_execution_inputs_and_outputs(client):
    """Test case for aiplatform_projects_locations_metadata_stores_executions_query_execution_inputs_and_outputs

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{executionquery_execution_inputs_and_output}'.format(execution='execution_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_list(client):
    """Test case for aiplatform_projects_locations_metadata_stores_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/metadataStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_metadata_schemas_create(client):
    """Test case for aiplatform_projects_locations_metadata_stores_metadata_schemas_create

    
    """
    body = {"schema":"schema","schemaVersion":"schemaVersion","createTime":"createTime","name":"name","schemaType":"METADATA_SCHEMA_TYPE_UNSPECIFIED","description":"description"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('metadataSchemaId', 'metadata_schema_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/metadataSchemas'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_metadata_stores_metadata_schemas_list(client):
    """Test case for aiplatform_projects_locations_metadata_stores_metadata_schemas_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/metadataSchemas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_migratable_resources_batch_migrate(client):
    """Test case for aiplatform_projects_locations_migratable_resources_batch_migrate

    
    """
    body = {"migrateResourceRequests":[{"migrateMlEngineModelVersionConfig":{"endpoint":"endpoint","modelVersion":"modelVersion","modelDisplayName":"modelDisplayName"},"migrateAutomlDatasetConfig":{"datasetDisplayName":"datasetDisplayName","dataset":"dataset"},"migrateDataLabelingDatasetConfig":{"migrateDataLabelingAnnotatedDatasetConfigs":[{"annotatedDataset":"annotatedDataset"},{"annotatedDataset":"annotatedDataset"}],"datasetDisplayName":"datasetDisplayName","dataset":"dataset"},"migrateAutomlModelConfig":{"model":"model","modelDisplayName":"modelDisplayName"}},{"migrateMlEngineModelVersionConfig":{"endpoint":"endpoint","modelVersion":"modelVersion","modelDisplayName":"modelDisplayName"},"migrateAutomlDatasetConfig":{"datasetDisplayName":"datasetDisplayName","dataset":"dataset"},"migrateDataLabelingDatasetConfig":{"migrateDataLabelingAnnotatedDatasetConfigs":[{"annotatedDataset":"annotatedDataset"},{"annotatedDataset":"annotatedDataset"}],"datasetDisplayName":"datasetDisplayName","dataset":"dataset"},"migrateAutomlModelConfig":{"model":"model","modelDisplayName":"modelDisplayName"}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/migratableResources:batchMigrate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_migratable_resources_search(client):
    """Test case for aiplatform_projects_locations_migratable_resources_search

    
    """
    body = {"filter":"filter","pageSize":0,"pageToken":"pageToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/migratableResources:search'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_model_deployment_monitoring_jobs_create(client):
    """Test case for aiplatform_projects_locations_model_deployment_monitoring_jobs_create

    
    """
    body = {"modelDeploymentMonitoringScheduleConfig":{"monitorInterval":"monitorInterval","monitorWindow":"monitorWindow"},"scheduleState":"MONITORING_SCHEDULE_STATE_UNSPECIFIED","analysisInstanceSchemaUri":"analysisInstanceSchemaUri","displayName":"displayName","enableMonitoringPipelineLogs":True,"updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"samplePredictInstance":"","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"modelMonitoringAlertConfig":{"emailAlertConfig":{"userEmails":["userEmails","userEmails"]},"notificationChannels":["notificationChannels","notificationChannels"],"enableLogging":True},"labels":{"key":"labels"},"latestMonitoringPipelineMetadata":{"runTime":"runTime","status":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},"predictInstanceSchemaUri":"predictInstanceSchemaUri","endpoint":"endpoint","loggingSamplingStrategy":{"randomSampleConfig":{"sampleRate":5.962133916683182}},"nextScheduleTime":"nextScheduleTime","statsAnomaliesBaseDirectory":{"outputUriPrefix":"outputUriPrefix"},"createTime":"createTime","bigqueryTables":[{"logType":"LOG_TYPE_UNSPECIFIED","bigqueryTablePath":"bigqueryTablePath","requestResponseLoggingSchemaVersion":"requestResponseLoggingSchemaVersion","logSource":"LOG_SOURCE_UNSPECIFIED"},{"logType":"LOG_TYPE_UNSPECIFIED","bigqueryTablePath":"bigqueryTablePath","requestResponseLoggingSchemaVersion":"requestResponseLoggingSchemaVersion","logSource":"LOG_SOURCE_UNSPECIFIED"}],"name":"name","modelDeploymentMonitoringObjectiveConfigs":[{"deployedModelId":"deployedModelId","objectiveConfig":{"predictionDriftDetectionConfig":{"attributionScoreDriftThresholds":{"key":{"value":6.027456183070403}},"defaultDriftThreshold":{"value":6.027456183070403},"driftThresholds":{"key":{"value":6.027456183070403}}},"trainingPredictionSkewDetectionConfig":{"defaultSkewThreshold":{"value":6.027456183070403},"skewThresholds":{"key":{"value":6.027456183070403}},"attributionScoreSkewThresholds":{"key":{"value":6.027456183070403}}},"explanationConfig":{"explanationBaseline":{"gcs":{"outputUriPrefix":"outputUriPrefix"},"predictionFormat":"PREDICTION_FORMAT_UNSPECIFIED","bigquery":{"outputUri":"outputUri"}},"enableFeatureAttributes":True},"trainingDataset":{"loggingSamplingStrategy":{"randomSampleConfig":{"sampleRate":5.962133916683182}},"targetField":"targetField","dataFormat":"dataFormat","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"uris":["uris","uris"]},"dataset":"dataset"}}},{"deployedModelId":"deployedModelId","objectiveConfig":{"predictionDriftDetectionConfig":{"attributionScoreDriftThresholds":{"key":{"value":6.027456183070403}},"defaultDriftThreshold":{"value":6.027456183070403},"driftThresholds":{"key":{"value":6.027456183070403}}},"trainingPredictionSkewDetectionConfig":{"defaultSkewThreshold":{"value":6.027456183070403},"skewThresholds":{"key":{"value":6.027456183070403}},"attributionScoreSkewThresholds":{"key":{"value":6.027456183070403}}},"explanationConfig":{"explanationBaseline":{"gcs":{"outputUriPrefix":"outputUriPrefix"},"predictionFormat":"PREDICTION_FORMAT_UNSPECIFIED","bigquery":{"outputUri":"outputUri"}},"enableFeatureAttributes":True},"trainingDataset":{"loggingSamplingStrategy":{"randomSampleConfig":{"sampleRate":5.962133916683182}},"targetField":"targetField","dataFormat":"dataFormat","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"uris":["uris","uris"]},"dataset":"dataset"}}}],"state":"JOB_STATE_UNSPECIFIED","logTtl":"logTtl"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/modelDeploymentMonitoringJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_model_deployment_monitoring_jobs_list(client):
    """Test case for aiplatform_projects_locations_model_deployment_monitoring_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/modelDeploymentMonitoringJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_model_deployment_monitoring_jobs_search_model_deployment_monitoring_stats_anomalies(client):
    """Test case for aiplatform_projects_locations_model_deployment_monitoring_jobs_search_model_deployment_monitoring_stats_anomalies

    
    """
    body = {"featureDisplayName":"featureDisplayName","deployedModelId":"deployedModelId","pageSize":6,"objectives":[{"topFeatureCount":0,"type":"MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED"},{"topFeatureCount":0,"type":"MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED"}],"startTime":"startTime","endTime":"endTime","pageToken":"pageToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{model_deployment_monitoring_jobsearch_model_deployment_monitoring_stats_anomalie}'.format(model_deployment_monitoring_job='model_deployment_monitoring_job_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_copy(client):
    """Test case for aiplatform_projects_locations_models_copy

    
    """
    body = {"modelId":"modelId","sourceModel":"sourceModel","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"parentModel":"parentModel"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/models:copy'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_delete_version(client):
    """Test case for aiplatform_projects_locations_models_delete_version

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{namedelete_versio}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_evaluations_import(client):
    """Test case for aiplatform_projects_locations_models_evaluations_import

    
    """
    body = {"modelEvaluation":{"biasConfigs":{"biasSlices":{"configs":{"key":{"range":{"high":0.8008282,"low":6.0274563},"allValues":True,"value":{"stringValue":"stringValue","floatValue":1.4658129}}}},"labels":["labels","labels"]},"metadata":"","modelExplanation":{"meanAttributions":[{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403},{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403}]},"createTime":"createTime","explanationSpecs":[{"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"explanationType":"explanationType"},{"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"explanationType":"explanationType"}],"displayName":"displayName","name":"name","metrics":"","metricsSchemaUri":"metricsSchemaUri","sliceDimensions":["sliceDimensions","sliceDimensions"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/evaluations:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_evaluations_list(client):
    """Test case for aiplatform_projects_locations_models_evaluations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/evaluations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_evaluations_slices_batch_import(client):
    """Test case for aiplatform_projects_locations_models_evaluations_slices_batch_import

    
    """
    body = {"evaluatedAnnotations":[{"dataItemPayload":"","errorAnalysisAnnotations":[{"attributedItems":[{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"},{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"}],"outlierScore":6.027456183070403,"outlierThreshold":1.4658129805029452,"queryType":"QUERY_TYPE_UNSPECIFIED"},{"attributedItems":[{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"},{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"}],"outlierScore":6.027456183070403,"outlierThreshold":1.4658129805029452,"queryType":"QUERY_TYPE_UNSPECIFIED"}],"evaluatedDataItemViewId":"evaluatedDataItemViewId","explanations":[{"explanationType":"explanationType","explanation":{"neighbors":[{"neighborId":"neighborId","neighborDistance":5.637376656633329},{"neighborId":"neighborId","neighborDistance":5.637376656633329}],"attributions":[{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403},{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403}]}},{"explanationType":"explanationType","explanation":{"neighbors":[{"neighborId":"neighborId","neighborDistance":5.637376656633329},{"neighborId":"neighborId","neighborDistance":5.637376656633329}],"attributions":[{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403},{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403}]}}],"groundTruths":["",""],"type":"EVALUATED_ANNOTATION_TYPE_UNSPECIFIED","predictions":["",""]},{"dataItemPayload":"","errorAnalysisAnnotations":[{"attributedItems":[{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"},{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"}],"outlierScore":6.027456183070403,"outlierThreshold":1.4658129805029452,"queryType":"QUERY_TYPE_UNSPECIFIED"},{"attributedItems":[{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"},{"distance":0.8008281904610115,"annotationResourceName":"annotationResourceName"}],"outlierScore":6.027456183070403,"outlierThreshold":1.4658129805029452,"queryType":"QUERY_TYPE_UNSPECIFIED"}],"evaluatedDataItemViewId":"evaluatedDataItemViewId","explanations":[{"explanationType":"explanationType","explanation":{"neighbors":[{"neighborId":"neighborId","neighborDistance":5.637376656633329},{"neighborId":"neighborId","neighborDistance":5.637376656633329}],"attributions":[{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403},{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403}]}},{"explanationType":"explanationType","explanation":{"neighbors":[{"neighborId":"neighborId","neighborDistance":5.637376656633329},{"neighborId":"neighborId","neighborDistance":5.637376656633329}],"attributions":[{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403},{"outputDisplayName":"outputDisplayName","outputIndex":[5,5],"featureAttributions":"","instanceOutputValue":1.4658129805029452,"outputName":"outputName","approximationError":0.8008281904610115,"baselineOutputValue":6.027456183070403}]}}],"groundTruths":["",""],"type":"EVALUATED_ANNOTATION_TYPE_UNSPECIFIED","predictions":["",""]}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parentbatch_impor}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_evaluations_slices_list(client):
    """Test case for aiplatform_projects_locations_models_evaluations_slices_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/slices'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_export(client):
    """Test case for aiplatform_projects_locations_models_export

    
    """
    body = {"outputConfig":{"imageDestination":{"outputUri":"outputUri"},"exportFormatId":"exportFormatId","artifactDestination":{"outputUriPrefix":"outputUriPrefix"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameexpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_list_versions(client):
    """Test case for aiplatform_projects_locations_models_list_versions

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{namelist_version}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_merge_version_aliases(client):
    """Test case for aiplatform_projects_locations_models_merge_version_aliases

    
    """
    body = {"versionAliases":["versionAliases","versionAliases"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namemerge_version_aliase}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_update_explanation_dataset(client):
    """Test case for aiplatform_projects_locations_models_update_explanation_dataset

    
    """
    body = {"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{modelupdate_explanation_datase}'.format(model='model_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_models_upload(client):
    """Test case for aiplatform_projects_locations_models_upload

    
    """
    body = {"modelId":"modelId","model":{"versionDescription":"versionDescription","versionAliases":["versionAliases","versionAliases"],"metadata":"","originalModelInfo":{"model":"model"},"displayName":"displayName","versionCreateTime":"versionCreateTime","metadataSchemaUri":"metadataSchemaUri","description":"description","supportedOutputStorageFormats":["supportedOutputStorageFormats","supportedOutputStorageFormats"],"versionUpdateTime":"versionUpdateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"metadataArtifact":"metadataArtifact","supportedInputStorageFormats":["supportedInputStorageFormats","supportedInputStorageFormats"],"predictSchemata":{"instanceSchemaUri":"instanceSchemaUri","parametersSchemaUri":"parametersSchemaUri","predictionSchemaUri":"predictionSchemaUri"},"modelSourceInfo":{"sourceType":"MODEL_SOURCE_TYPE_UNSPECIFIED","copy":True},"baseModelSource":{"genieSource":{"baseModelUri":"baseModelUri"},"modelGardenSource":{"publicModelName":"publicModelName"}},"supportedDeploymentResourcesTypes":["DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED","DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED"],"artifactUri":"artifactUri","containerSpec":{"args":["args","args"],"healthProbe":{"periodSeconds":6,"timeoutSeconds":1,"exec":{"command":["command","command"]}},"imageUri":"imageUri","deploymentTimeout":"deploymentTimeout","predictRoute":"predictRoute","sharedMemorySizeMb":"sharedMemorySizeMb","grpcPorts":[{"containerPort":0},{"containerPort":0}],"startupProbe":{"periodSeconds":6,"timeoutSeconds":1,"exec":{"command":["command","command"]}},"env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"healthRoute":"healthRoute","ports":[{"containerPort":0},{"containerPort":0}],"command":["command","command"]},"supportedExportFormats":[{"id":"id","exportableContents":["EXPORTABLE_CONTENT_UNSPECIFIED","EXPORTABLE_CONTENT_UNSPECIFIED"]},{"id":"id","exportableContents":["EXPORTABLE_CONTENT_UNSPECIFIED","EXPORTABLE_CONTENT_UNSPECIFIED"]}],"trainingPipeline":"trainingPipeline","updateTime":"updateTime","labels":{"key":"labels"},"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"versionId":"versionId","createTime":"createTime","name":"name","etag":"etag","deployedModels":[{"endpoint":"endpoint","deployedModelId":"deployedModelId"},{"endpoint":"endpoint","deployedModelId":"deployedModelId"}]},"serviceAccount":"serviceAccount","parentModel":"parentModel"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/models:upload'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_nas_jobs_create(client):
    """Test case for aiplatform_projects_locations_nas_jobs_create

    
    """
    body = {"nasJobOutput":{"multiTrialJobOutput":{"searchTrials":[{"startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED"},{"startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED"}],"trainTrials":[{"startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED"},{"startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED"}]}},"displayName":"displayName","enableRestrictedImageTraining":True,"updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"createTime":"createTime","name":"name","startTime":"startTime","endTime":"endTime","state":"JOB_STATE_UNSPECIFIED","nasJobSpec":{"searchSpaceSpec":"searchSpaceSpec","resumeNasJobId":"resumeNasJobId","multiTrialAlgorithmSpec":{"trainTrialSpec":{"maxParallelTrialCount":5,"trainTrialJobSpec":{"models":["models","models"],"workerPoolSpecs":[{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}}],"protectedArtifactLocationId":"protectedArtifactLocationId","serviceAccount":"serviceAccount","network":"network","tensorboard":"tensorboard","enableWebAccess":True,"experiment":"experiment","persistentResourceId":"persistentResourceId","experimentRun":"experimentRun","enableDashboardAccess":True,"scheduling":{"restartJobOnWorkerRestart":True,"disableRetries":True,"timeout":"timeout"},"reservedIpRanges":["reservedIpRanges","reservedIpRanges"],"baseOutputDirectory":{"outputUriPrefix":"outputUriPrefix"}},"frequency":5},"metric":{"goal":"GOAL_TYPE_UNSPECIFIED","metricId":"metricId"},"multiTrialAlgorithm":"MULTI_TRIAL_ALGORITHM_UNSPECIFIED","searchTrialSpec":{"searchTrialJobSpec":{"models":["models","models"],"workerPoolSpecs":[{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}},{"containerSpec":{"args":["args","args"],"imageUri":"imageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"command":["command","command"]},"nfsMounts":[{"path":"path","server":"server","mountPoint":"mountPoint"},{"path":"path","server":"server","mountPoint":"mountPoint"}],"pythonPackageSpec":{"args":["args","args"],"packageUris":["packageUris","packageUris"],"executorImageUri":"executorImageUri","env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"pythonModule":"pythonModule"},"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}}],"protectedArtifactLocationId":"protectedArtifactLocationId","serviceAccount":"serviceAccount","network":"network","tensorboard":"tensorboard","enableWebAccess":True,"experiment":"experiment","persistentResourceId":"persistentResourceId","experimentRun":"experimentRun","enableDashboardAccess":True,"scheduling":{"restartJobOnWorkerRestart":True,"disableRetries":True,"timeout":"timeout"},"reservedIpRanges":["reservedIpRanges","reservedIpRanges"],"baseOutputDirectory":{"outputUriPrefix":"outputUriPrefix"}},"maxParallelTrialCount":6,"maxFailedTrialCount":0,"maxTrialCount":1}}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/nasJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_nas_jobs_list(client):
    """Test case for aiplatform_projects_locations_nas_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/nasJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_nas_jobs_nas_trial_details_list(client):
    """Test case for aiplatform_projects_locations_nas_jobs_nas_trial_details_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/nasTrialDetails'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtime_templates_create(client):
    """Test case for aiplatform_projects_locations_notebook_runtime_templates_create

    
    """
    body = {"shieldedVmConfig":{"enableSecureBoot":True},"dataPersistentDiskSpec":{"diskType":"diskType","diskSizeGb":"diskSizeGb"},"eucConfig":{"eucDisabled":True,"bypassActasCheck":True},"displayName":"displayName","reservationAffinity":{"consumeReservationType":"RESERVATION_AFFINITY_TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"description":"description","notebookRuntimeType":"NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED","serviceAccount":"serviceAccount","updateTime":"updateTime","labels":{"key":"labels"},"isDefault":True,"networkTags":["networkTags","networkTags"],"createTime":"createTime","idleShutdownConfig":{"idleShutdownDisabled":True,"idleTimeout":"idleTimeout"},"name":"name","etag":"etag","networkSpec":{"enableInternetAccess":True,"subnetwork":"subnetwork","network":"network"},"machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('notebookRuntimeTemplateId', 'notebook_runtime_template_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/notebookRuntimeTemplates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtime_templates_list(client):
    """Test case for aiplatform_projects_locations_notebook_runtime_templates_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/notebookRuntimeTemplates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtime_templates_set_iam_policy(client):
    """Test case for aiplatform_projects_locations_notebook_runtime_templates_set_iam_policy

    
    """
    body = {"policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtime_templates_test_iam_permissions(client):
    """Test case for aiplatform_projects_locations_notebook_runtime_templates_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('permissions', ['permissions_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtimes_assign(client):
    """Test case for aiplatform_projects_locations_notebook_runtimes_assign

    
    """
    body = {"notebookRuntimeTemplate":"notebookRuntimeTemplate","notebookRuntimeId":"notebookRuntimeId","notebookRuntime":{"displayName":"displayName","reservationAffinity":{"consumeReservationType":"RESERVATION_AFFINITY_TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"description":"description","notebookRuntimeType":"NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED","serviceAccount":"serviceAccount","updateTime":"updateTime","isUpgradable":True,"version":"version","notebookRuntimeTemplateRef":{"notebookRuntimeTemplate":"notebookRuntimeTemplate"},"labels":{"key":"labels"},"runtimeState":"RUNTIME_STATE_UNSPECIFIED","networkTags":["networkTags","networkTags"],"healthState":"HEALTH_STATE_UNSPECIFIED","createTime":"createTime","expirationTime":"expirationTime","name":"name","proxyUri":"proxyUri","runtimeUser":"runtimeUser"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/notebookRuntimes:assign'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtimes_generate_access_token(client):
    """Test case for aiplatform_projects_locations_notebook_runtimes_generate_access_token

    
    """
    body = {"vmToken":"vmToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namegenerate_access_toke}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtimes_list(client):
    """Test case for aiplatform_projects_locations_notebook_runtimes_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/notebookRuntimes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtimes_report_event(client):
    """Test case for aiplatform_projects_locations_notebook_runtimes_report_event

    
    """
    body = {"vmToken":"vmToken","eventDetails":{"key":"eventDetails"},"eventType":"EVENT_TYPE_UNSPECIFIED","internalOsServiceStateInstances":[{"serviceState":"UNKNOWN","serviceName":"INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED"},{"serviceState":"UNKNOWN","serviceName":"INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED"}],"internalOsServiceStateInstance":[{"serviceState":"UNKNOWN","serviceName":"INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED"},{"serviceState":"UNKNOWN","serviceName":"INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namereport_even}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtimes_start(client):
    """Test case for aiplatform_projects_locations_notebook_runtimes_start

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namestar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_notebook_runtimes_upgrade(client):
    """Test case for aiplatform_projects_locations_notebook_runtimes_upgrade

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameupgrad}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_persistent_resources_create(client):
    """Test case for aiplatform_projects_locations_persistent_resources_create

    
    """
    body = {"resourceRuntime":{"notebookRuntimeTemplate":"notebookRuntimeTemplate","accessUris":{"key":"accessUris"}},"displayName":"displayName","resourcePools":[{"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"id":"id","machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"},"usedReplicaCount":"usedReplicaCount","autoscalingSpec":{"minReplicaCount":"minReplicaCount","maxReplicaCount":"maxReplicaCount"}},{"replicaCount":"replicaCount","diskSpec":{"bootDiskType":"bootDiskType","bootDiskSizeGb":0},"id":"id","machineSpec":{"acceleratorType":"ACCELERATOR_TYPE_UNSPECIFIED","tpuTopology":"tpuTopology","acceleratorCount":5,"machineType":"machineType"},"usedReplicaCount":"usedReplicaCount","autoscalingSpec":{"minReplicaCount":"minReplicaCount","maxReplicaCount":"maxReplicaCount"}}],"resourceRuntimeSpec":{"raySpec":{"imageUri":"imageUri","rayMetricSpec":{"disabled":True},"resourcePoolImages":{"key":"resourcePoolImages"},"headNodeResourcePoolId":"headNodeResourcePoolId"},"serviceAccountSpec":{"enableCustomServiceAccount":True,"serviceAccount":"serviceAccount"}},"updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"network":"network","createTime":"createTime","name":"name","startTime":"startTime","state":"STATE_UNSPECIFIED","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('persistentResourceId', 'persistent_resource_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/persistentResources'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_persistent_resources_list(client):
    """Test case for aiplatform_projects_locations_persistent_resources_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/persistentResources'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_pipeline_jobs_batch_cancel(client):
    """Test case for aiplatform_projects_locations_pipeline_jobs_batch_cancel

    
    """
    body = {"names":["names","names"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/pipelineJobs:batchCancel'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_pipeline_jobs_batch_delete(client):
    """Test case for aiplatform_projects_locations_pipeline_jobs_batch_delete

    
    """
    body = {"names":["names","names"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/pipelineJobs:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_pipeline_jobs_create(client):
    """Test case for aiplatform_projects_locations_pipeline_jobs_create

    
    """
    body = {"scheduleName":"scheduleName","pipelineSpec":{"key":""},"jobDetail":{"pipelineContext":{"parentContexts":["parentContexts","parentContexts"],"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}},"pipelineRunContext":{"parentContexts":["parentContexts","parentContexts"],"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}},"taskDetails":[{"outputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"execution":{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}},"pipelineTaskStatus":[{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}],"inputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"parentTaskId":"parentTaskId","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"createTime":"createTime","executorDetail":{"customJobDetail":{"failedJobs":["failedJobs","failedJobs"],"job":"job"},"containerDetail":{"failedPreCachingCheckJobs":["failedPreCachingCheckJobs","failedPreCachingCheckJobs"],"failedMainJobs":["failedMainJobs","failedMainJobs"],"preCachingCheckJob":"preCachingCheckJob","mainJob":"mainJob"}},"startTime":"startTime","taskName":"taskName","endTime":"endTime","state":"STATE_UNSPECIFIED","taskId":"taskId"},{"outputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"execution":{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}},"pipelineTaskStatus":[{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}],"inputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"parentTaskId":"parentTaskId","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"createTime":"createTime","executorDetail":{"customJobDetail":{"failedJobs":["failedJobs","failedJobs"],"job":"job"},"containerDetail":{"failedPreCachingCheckJobs":["failedPreCachingCheckJobs","failedPreCachingCheckJobs"],"failedMainJobs":["failedMainJobs","failedMainJobs"],"preCachingCheckJob":"preCachingCheckJob","mainJob":"mainJob"}},"startTime":"startTime","taskName":"taskName","endTime":"endTime","state":"STATE_UNSPECIFIED","taskId":"taskId"}]},"displayName":"displayName","templateUri":"templateUri","serviceAccount":"serviceAccount","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"network":"network","preflightValidations":True,"createTime":"createTime","name":"name","runtimeConfig":{"gcsOutputDirectory":"gcsOutputDirectory","failurePolicy":"PIPELINE_FAILURE_POLICY_UNSPECIFIED","inputArtifacts":{"key":{"artifactId":"artifactId"}},"parameters":{"key":{"stringValue":"stringValue","intValue":"intValue","doubleValue":0.8008281904610115}},"parameterValues":{"key":""}},"startTime":"startTime","templateMetadata":{"version":"version"},"endTime":"endTime","state":"PIPELINE_STATE_UNSPECIFIED","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pipelineJobId', 'pipeline_job_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/pipelineJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_pipeline_jobs_list(client):
    """Test case for aiplatform_projects_locations_pipeline_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/pipelineJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_compute_tokens(client):
    """Test case for aiplatform_projects_locations_publishers_models_compute_tokens

    
    """
    body = {"instances":["",""]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointcompute_token}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_count_tokens(client):
    """Test case for aiplatform_projects_locations_publishers_models_count_tokens

    
    """
    body = {"contents":[{"role":"role","parts":[{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}},{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}}]},{"role":"role","parts":[{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}},{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}}]}],"instances":["",""],"model":"model"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointcount_token}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_generate_content(client):
    """Test case for aiplatform_projects_locations_publishers_models_generate_content

    
    """
    body = {"safetySettings":[{"threshold":"HARM_BLOCK_THRESHOLD_UNSPECIFIED","category":"HARM_CATEGORY_UNSPECIFIED"},{"threshold":"HARM_BLOCK_THRESHOLD_UNSPECIFIED","category":"HARM_CATEGORY_UNSPECIFIED"}],"contents":[{"role":"role","parts":[{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}},{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}}]},{"role":"role","parts":[{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}},{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}}]}],"generationConfig":{"topK":5.962134,"stopSequences":["stopSequences","stopSequences"],"temperature":1.4658129,"maxOutputTokens":6,"topP":5.637377,"candidateCount":0},"tools":[{"googleSearchRetrieval":{"disableAttribution":True},"retrieval":{"disableAttribution":True,"vertexAiSearch":{"datastore":"datastore"}},"functionDeclarations":[{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}},{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}}]},{"googleSearchRetrieval":{"disableAttribution":True},"retrieval":{"disableAttribution":True,"vertexAiSearch":{"datastore":"datastore"}},"functionDeclarations":[{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}},{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}}]}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{modelgenerate_conten}'.format(model='model_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_get_iam_policy(client):
    """Test case for aiplatform_projects_locations_publishers_models_get_iam_policy

    
    """
    body = {"options":{"requestedPolicyVersion":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_predict(client):
    """Test case for aiplatform_projects_locations_publishers_models_predict

    
    """
    body = {"instances":["",""],"parameters":""}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointpredic}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_raw_predict(client):
    """Test case for aiplatform_projects_locations_publishers_models_raw_predict

    
    """
    body = {"httpBody":{"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointraw_predic}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_server_streaming_predict(client):
    """Test case for aiplatform_projects_locations_publishers_models_server_streaming_predict

    
    """
    body = {"inputs":[{"doubleVal":[0.8008281904610115,0.8008281904610115],"intVal":[1,1],"shape":["shape","shape"],"stringVal":["stringVal","stringVal"],"dtype":"DATA_TYPE_UNSPECIFIED","bytesVal":["bytesVal","bytesVal"],"floatVal":[6.0274563,6.0274563],"boolVal":[True,True],"uintVal":[5,5],"structVal":{},"int64Val":["int64Val","int64Val"],"uint64Val":["uint64Val","uint64Val"],"listVal":[null,null],"tensorVal":"tensorVal"},{"doubleVal":[0.8008281904610115,0.8008281904610115],"intVal":[1,1],"shape":["shape","shape"],"stringVal":["stringVal","stringVal"],"dtype":"DATA_TYPE_UNSPECIFIED","bytesVal":["bytesVal","bytesVal"],"floatVal":[6.0274563,6.0274563],"boolVal":[True,True],"uintVal":[5,5],"structVal":{},"int64Val":["int64Val","int64Val"],"uint64Val":["uint64Val","uint64Val"],"listVal":[null,null],"tensorVal":"tensorVal"}],"parameters":{"doubleVal":[0.8008281904610115,0.8008281904610115],"intVal":[1,1],"shape":["shape","shape"],"stringVal":["stringVal","stringVal"],"dtype":"DATA_TYPE_UNSPECIFIED","bytesVal":["bytesVal","bytesVal"],"floatVal":[6.0274563,6.0274563],"boolVal":[True,True],"uintVal":[5,5],"structVal":{},"int64Val":["int64Val","int64Val"],"uint64Val":["uint64Val","uint64Val"],"listVal":[null,null],"tensorVal":"tensorVal"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{endpointserver_streaming_predic}'.format(endpoint='endpoint_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_publishers_models_stream_generate_content(client):
    """Test case for aiplatform_projects_locations_publishers_models_stream_generate_content

    
    """
    body = {"safetySettings":[{"threshold":"HARM_BLOCK_THRESHOLD_UNSPECIFIED","category":"HARM_CATEGORY_UNSPECIFIED"},{"threshold":"HARM_BLOCK_THRESHOLD_UNSPECIFIED","category":"HARM_CATEGORY_UNSPECIFIED"}],"contents":[{"role":"role","parts":[{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}},{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}}]},{"role":"role","parts":[{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}},{"functionResponse":{"response":{"key":""},"name":"name"},"fileData":{"fileUri":"fileUri","mimeType":"mimeType"},"functionCall":{"args":{"key":""},"name":"name"},"inlineData":{"data":"data","mimeType":"mimeType"},"text":"text","videoMetadata":{"endOffset":"endOffset","startOffset":"startOffset"}}]}],"generationConfig":{"topK":5.962134,"stopSequences":["stopSequences","stopSequences"],"temperature":1.4658129,"maxOutputTokens":6,"topP":5.637377,"candidateCount":0},"tools":[{"googleSearchRetrieval":{"disableAttribution":True},"retrieval":{"disableAttribution":True,"vertexAiSearch":{"datastore":"datastore"}},"functionDeclarations":[{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}},{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}}]},{"googleSearchRetrieval":{"disableAttribution":True},"retrieval":{"disableAttribution":True,"vertexAiSearch":{"datastore":"datastore"}},"functionDeclarations":[{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}},{"name":"name","description":"description","parameters":{"nullable":True,"format":"format","description":"description","type":"TYPE_UNSPECIFIED","enum":["enum","enum"],"properties":{},"required":["required","required"],"example":""}}]}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{modelstream_generate_conten}'.format(model='model_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_schedules_create(client):
    """Test case for aiplatform_projects_locations_schedules_create

    
    """
    body = {"cron":"cron","maxConcurrentRunCount":"maxConcurrentRunCount","displayName":"displayName","createPipelineJobRequest":{"parent":"parent","pipelineJob":{"scheduleName":"scheduleName","pipelineSpec":{"key":""},"jobDetail":{"pipelineContext":{"parentContexts":["parentContexts","parentContexts"],"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}},"pipelineRunContext":{"parentContexts":["parentContexts","parentContexts"],"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}},"taskDetails":[{"outputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"execution":{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}},"pipelineTaskStatus":[{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}],"inputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"parentTaskId":"parentTaskId","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"createTime":"createTime","executorDetail":{"customJobDetail":{"failedJobs":["failedJobs","failedJobs"],"job":"job"},"containerDetail":{"failedPreCachingCheckJobs":["failedPreCachingCheckJobs","failedPreCachingCheckJobs"],"failedMainJobs":["failedMainJobs","failedMainJobs"],"preCachingCheckJob":"preCachingCheckJob","mainJob":"mainJob"}},"startTime":"startTime","taskName":"taskName","endTime":"endTime","state":"STATE_UNSPECIFIED","taskId":"taskId"},{"outputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"execution":{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","labels":{"key":"labels"}},"pipelineTaskStatus":[{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}],"inputs":{"key":{"artifacts":[{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}},{"metadata":{"key":""},"schemaTitle":"schemaTitle","schemaVersion":"schemaVersion","createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"}}]}},"parentTaskId":"parentTaskId","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"createTime":"createTime","executorDetail":{"customJobDetail":{"failedJobs":["failedJobs","failedJobs"],"job":"job"},"containerDetail":{"failedPreCachingCheckJobs":["failedPreCachingCheckJobs","failedPreCachingCheckJobs"],"failedMainJobs":["failedMainJobs","failedMainJobs"],"preCachingCheckJob":"preCachingCheckJob","mainJob":"mainJob"}},"startTime":"startTime","taskName":"taskName","endTime":"endTime","state":"STATE_UNSPECIFIED","taskId":"taskId"}]},"displayName":"displayName","templateUri":"templateUri","serviceAccount":"serviceAccount","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"network":"network","preflightValidations":True,"createTime":"createTime","name":"name","runtimeConfig":{"gcsOutputDirectory":"gcsOutputDirectory","failurePolicy":"PIPELINE_FAILURE_POLICY_UNSPECIFIED","inputArtifacts":{"key":{"artifactId":"artifactId"}},"parameters":{"key":{"stringValue":"stringValue","intValue":"intValue","doubleValue":0.8008281904610115}},"parameterValues":{"key":""}},"startTime":"startTime","templateMetadata":{"version":"version"},"endTime":"endTime","state":"PIPELINE_STATE_UNSPECIFIED","reservedIpRanges":["reservedIpRanges","reservedIpRanges"]},"pipelineJobId":"pipelineJobId"},"updateTime":"updateTime","lastPauseTime":"lastPauseTime","lastResumeTime":"lastResumeTime","maxRunCount":"maxRunCount","nextRunTime":"nextRunTime","createTime":"createTime","allowQueueing":True,"catchUp":True,"name":"name","startTime":"startTime","endTime":"endTime","lastScheduledRunResponse":{"scheduledRunTime":"scheduledRunTime","runResponse":"runResponse"},"state":"STATE_UNSPECIFIED","startedRunCount":"startedRunCount"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/schedules'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_schedules_list(client):
    """Test case for aiplatform_projects_locations_schedules_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/schedules'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_schedules_pause(client):
    """Test case for aiplatform_projects_locations_schedules_pause

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namepaus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_schedules_resume(client):
    """Test case for aiplatform_projects_locations_schedules_resume

    
    """
    body = {"catchUp":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameresum}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_specialist_pools_create(client):
    """Test case for aiplatform_projects_locations_specialist_pools_create

    
    """
    body = {"specialistWorkerEmails":["specialistWorkerEmails","specialistWorkerEmails"],"specialistManagerEmails":["specialistManagerEmails","specialistManagerEmails"],"displayName":"displayName","name":"name","pendingDataLabelingJobs":["pendingDataLabelingJobs","pendingDataLabelingJobs"],"specialistManagersCount":0}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/specialistPools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_specialist_pools_list(client):
    """Test case for aiplatform_projects_locations_specialist_pools_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/specialistPools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_create(client):
    """Test case for aiplatform_projects_locations_studies_create

    
    """
    body = {"studySpec":{"convexStopConfig":{"maxNumSteps":"maxNumSteps","useSeconds":True,"learningRateParameterName":"learningRateParameterName","minNumSteps":"minNumSteps","autoregressiveOrder":"autoregressiveOrder"},"medianAutomatedStoppingSpec":{"useElapsedDuration":True},"studyStoppingConfig":{"minimumRuntimeConstraint":{"endTime":"endTime","maxDuration":"maxDuration"},"maximumRuntimeConstraint":{"endTime":"endTime","maxDuration":"maxDuration"},"shouldStopAsap":True,"maxDurationNoProgress":"maxDurationNoProgress","maxNumTrialsNoProgress":1,"minNumTrials":1,"maxNumTrials":7},"transferLearningConfig":{"disableTransferLearning":True,"priorStudyNames":["priorStudyNames","priorStudyNames"]},"measurementSelectionType":"MEASUREMENT_SELECTION_TYPE_UNSPECIFIED","convexAutomatedStoppingSpec":{"minMeasurementCount":"minMeasurementCount","minStepCount":"minStepCount","useElapsedDuration":True,"learningRateParameterName":"learningRateParameterName","maxStepCount":"maxStepCount","updateAllStoppedTrials":True},"decayCurveStoppingSpec":{"useElapsedDuration":True},"metrics":[{"safetyConfig":{"safetyThreshold":5.637376656633329,"desiredMinSafeTrialsFraction":5.962133916683182},"goal":"GOAL_TYPE_UNSPECIFIED","metricId":"metricId"},{"safetyConfig":{"safetyThreshold":5.637376656633329,"desiredMinSafeTrialsFraction":5.962133916683182},"goal":"GOAL_TYPE_UNSPECIFIED","metricId":"metricId"}],"parameters":[{"categoricalValueSpec":{"defaultValue":"defaultValue","values":["values","values"]},"parameterId":"parameterId","scaleType":"SCALE_TYPE_UNSPECIFIED","conditionalParameterSpecs":[{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}},{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}}],"doubleValueSpec":{"minValue":4.145608029883936,"defaultValue":3.616076749251911,"maxValue":2.027123023002322},"integerValueSpec":{"minValue":"minValue","defaultValue":"defaultValue","maxValue":"maxValue"},"discreteValueSpec":{"defaultValue":7.061401241503109,"values":[9.301444243932576,9.301444243932576]}},{"categoricalValueSpec":{"defaultValue":"defaultValue","values":["values","values"]},"parameterId":"parameterId","scaleType":"SCALE_TYPE_UNSPECIFIED","conditionalParameterSpecs":[{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}},{"parentIntValues":{"values":["values","values"]},"parentDiscreteValues":{"values":[2.3021358869347655,2.3021358869347655]},"parentCategoricalValues":{"values":["values","values"]}}],"doubleValueSpec":{"minValue":4.145608029883936,"defaultValue":3.616076749251911,"maxValue":2.027123023002322},"integerValueSpec":{"minValue":"minValue","defaultValue":"defaultValue","maxValue":"maxValue"},"discreteValueSpec":{"defaultValue":7.061401241503109,"values":[9.301444243932576,9.301444243932576]}}],"observationNoise":"OBSERVATION_NOISE_UNSPECIFIED","algorithm":"ALGORITHM_UNSPECIFIED"},"createTime":"createTime","displayName":"displayName","inactiveReason":"inactiveReason","name":"name","state":"STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/studies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_list(client):
    """Test case for aiplatform_projects_locations_studies_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/studies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_lookup(client):
    """Test case for aiplatform_projects_locations_studies_lookup

    
    """
    body = {"displayName":"displayName"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/studies:lookup'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_add_trial_measurement(client):
    """Test case for aiplatform_projects_locations_studies_trials_add_trial_measurement

    
    """
    body = {"measurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{trial_nameadd_trial_measuremen}'.format(trial_name='trial_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_check_trial_early_stopping_state(client):
    """Test case for aiplatform_projects_locations_studies_trials_check_trial_early_stopping_state

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{trial_namecheck_trial_early_stopping_stat}'.format(trial_name='trial_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_complete(client):
    """Test case for aiplatform_projects_locations_studies_trials_complete

    
    """
    body = {"infeasibleReason":"infeasibleReason","trialInfeasible":True,"finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namecomplet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_create(client):
    """Test case for aiplatform_projects_locations_studies_trials_create

    
    """
    body = {"customJob":"customJob","clientId":"clientId","infeasibleReason":"infeasibleReason","webAccessUris":{"key":"webAccessUris"},"name":"name","startTime":"startTime","endTime":"endTime","finalMeasurement":{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},"id":"id","state":"STATE_UNSPECIFIED","parameters":[{"parameterId":"parameterId","value":""},{"parameterId":"parameterId","value":""}],"measurements":[{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"},{"metrics":[{"metricId":"metricId","value":0.8008281904610115},{"metricId":"metricId","value":0.8008281904610115}],"stepCount":"stepCount","elapsedDuration":"elapsedDuration"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/trials'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_list(client):
    """Test case for aiplatform_projects_locations_studies_trials_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/trials'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_list_optimal_trials(client):
    """Test case for aiplatform_projects_locations_studies_trials_list_optimal_trials

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/trials:listOptimalTrials'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_stop(client):
    """Test case for aiplatform_projects_locations_studies_trials_stop

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namesto}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_studies_trials_suggest(client):
    """Test case for aiplatform_projects_locations_studies_trials_suggest

    
    """
    body = {"clientId":"clientId","suggestionCount":0,"contexts":[{"description":"description","parameters":[{"parameterId":"parameterId","value":""},{"parameterId":"parameterId","value":""}]},{"description":"description","parameters":[{"parameterId":"parameterId","value":""},{"parameterId":"parameterId","value":""}]}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/trials:suggest'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_batch_read(client):
    """Test case for aiplatform_projects_locations_tensorboards_batch_read

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('timeSeries', ['time_series_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{tensorboardbatch_rea}'.format(tensorboard='tensorboard_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_create(client):
    """Test case for aiplatform_projects_locations_tensorboards_create

    
    """
    body = {"blobStoragePathPrefix":"blobStoragePathPrefix","isDefault":True,"createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"runCount":0,"labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/tensorboards'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_batch_create(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_batch_create

    
    """
    body = {"requests":[{"parent":"parent","tensorboardTimeSeriesId":"tensorboardTimeSeriesId","tensorboardTimeSeries":{"metadata":{"maxBlobSequenceLength":"maxBlobSequenceLength","maxWallTime":"maxWallTime","maxStep":"maxStep"},"createTime":"createTime","pluginName":"pluginName","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","etag":"etag","pluginData":"pluginData","updateTime":"updateTime"}},{"parent":"parent","tensorboardTimeSeriesId":"tensorboardTimeSeriesId","tensorboardTimeSeries":{"metadata":{"maxBlobSequenceLength":"maxBlobSequenceLength","maxWallTime":"maxWallTime","maxStep":"maxStep"},"createTime":"createTime","pluginName":"pluginName","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","etag":"etag","pluginData":"pluginData","updateTime":"updateTime"}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parentbatch_creat}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_create(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","source":"source","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('tensorboardExperimentId', 'tensorboard_experiment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/experiments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_list(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/experiments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_batch_create(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_batch_create

    
    """
    body = {"requests":[{"parent":"parent","tensorboardRunId":"tensorboardRunId","tensorboardRun":{"createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}},{"parent":"parent","tensorboardRunId":"tensorboardRunId","tensorboardRun":{"createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/runs:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_create(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('tensorboardRunId', 'tensorboard_run_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/runs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_list(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/runs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_time_series_create(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_time_series_create

    
    """
    body = {"metadata":{"maxBlobSequenceLength":"maxBlobSequenceLength","maxWallTime":"maxWallTime","maxStep":"maxStep"},"createTime":"createTime","pluginName":"pluginName","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","etag":"etag","pluginData":"pluginData","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('tensorboardTimeSeriesId', 'tensorboard_time_series_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/timeSeries'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_time_series_export_tensorboard_time_series(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_time_series_export_tensorboard_time_series

    
    """
    body = {"filter":"filter","orderBy":"orderBy","pageSize":0,"pageToken":"pageToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{tensorboard_time_seriesexport_tensorboard_time_serie}'.format(tensorboard_time_series='tensorboard_time_series_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_time_series_list(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_time_series_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/timeSeries'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_time_series_patch(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_time_series_patch

    
    """
    body = {"metadata":{"maxBlobSequenceLength":"maxBlobSequenceLength","maxWallTime":"maxWallTime","maxStep":"maxStep"},"createTime":"createTime","pluginName":"pluginName","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","etag":"etag","pluginData":"pluginData","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('maxDataPoints', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{tensorboard_time_seriesrea}'.format(tensorboard_time_series='tensorboard_time_series_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read_blob_data(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_time_series_read_blob_data

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('blobIds', ['blob_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{time_seriesread_blob_dat}'.format(time_series='time_series_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_runs_write(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_runs_write

    
    """
    body = {"timeSeriesData":[{"tensorboardTimeSeriesId":"tensorboardTimeSeriesId","valueType":"VALUE_TYPE_UNSPECIFIED","values":[{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}},{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}}]},{"tensorboardTimeSeriesId":"tensorboardTimeSeriesId","valueType":"VALUE_TYPE_UNSPECIFIED","values":[{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}},{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}}]}],"tensorboardRun":"tensorboardRun"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{tensorboard_runwrit}'.format(tensorboard_run='tensorboard_run_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_experiments_write(client):
    """Test case for aiplatform_projects_locations_tensorboards_experiments_write

    
    """
    body = {"writeRunDataRequests":[{"timeSeriesData":[{"tensorboardTimeSeriesId":"tensorboardTimeSeriesId","valueType":"VALUE_TYPE_UNSPECIFIED","values":[{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}},{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}}]},{"tensorboardTimeSeriesId":"tensorboardTimeSeriesId","valueType":"VALUE_TYPE_UNSPECIFIED","values":[{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}},{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}}]}],"tensorboardRun":"tensorboardRun"},{"timeSeriesData":[{"tensorboardTimeSeriesId":"tensorboardTimeSeriesId","valueType":"VALUE_TYPE_UNSPECIFIED","values":[{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}},{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}}]},{"tensorboardTimeSeriesId":"tensorboardTimeSeriesId","valueType":"VALUE_TYPE_UNSPECIFIED","values":[{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}},{"blobs":{"values":[{"data":"data","id":"id"},{"data":"data","id":"id"}]},"scalar":{"value":0.8008281904610115},"step":"step","wallTime":"wallTime","tensor":{"value":"value","versionNumber":6}}]}],"tensorboardRun":"tensorboardRun"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{tensorboard_experimentwrit}'.format(tensorboard_experiment='tensorboard_experiment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_list(client):
    """Test case for aiplatform_projects_locations_tensorboards_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/tensorboards'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_read_size(client):
    """Test case for aiplatform_projects_locations_tensorboards_read_size

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{tensorboardread_siz}'.format(tensorboard='tensorboard_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_tensorboards_read_usage(client):
    """Test case for aiplatform_projects_locations_tensorboards_read_usage

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{tensorboardread_usag}'.format(tensorboard='tensorboard_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_training_pipelines_create(client):
    """Test case for aiplatform_projects_locations_training_pipelines_create

    
    """
    body = {"modelId":"modelId","displayName":"displayName","trainingTaskMetadata":"","updateTime":"updateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"trainingTaskInputs":"","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"createTime":"createTime","trainingTaskDefinition":"trainingTaskDefinition","name":"name","startTime":"startTime","endTime":"endTime","modelToUpload":{"versionDescription":"versionDescription","versionAliases":["versionAliases","versionAliases"],"metadata":"","originalModelInfo":{"model":"model"},"displayName":"displayName","versionCreateTime":"versionCreateTime","metadataSchemaUri":"metadataSchemaUri","description":"description","supportedOutputStorageFormats":["supportedOutputStorageFormats","supportedOutputStorageFormats"],"versionUpdateTime":"versionUpdateTime","encryptionSpec":{"kmsKeyName":"kmsKeyName"},"metadataArtifact":"metadataArtifact","supportedInputStorageFormats":["supportedInputStorageFormats","supportedInputStorageFormats"],"predictSchemata":{"instanceSchemaUri":"instanceSchemaUri","parametersSchemaUri":"parametersSchemaUri","predictionSchemaUri":"predictionSchemaUri"},"modelSourceInfo":{"sourceType":"MODEL_SOURCE_TYPE_UNSPECIFIED","copy":True},"baseModelSource":{"genieSource":{"baseModelUri":"baseModelUri"},"modelGardenSource":{"publicModelName":"publicModelName"}},"supportedDeploymentResourcesTypes":["DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED","DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED"],"artifactUri":"artifactUri","containerSpec":{"args":["args","args"],"healthProbe":{"periodSeconds":6,"timeoutSeconds":1,"exec":{"command":["command","command"]}},"imageUri":"imageUri","deploymentTimeout":"deploymentTimeout","predictRoute":"predictRoute","sharedMemorySizeMb":"sharedMemorySizeMb","grpcPorts":[{"containerPort":0},{"containerPort":0}],"startupProbe":{"periodSeconds":6,"timeoutSeconds":1,"exec":{"command":["command","command"]}},"env":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"healthRoute":"healthRoute","ports":[{"containerPort":0},{"containerPort":0}],"command":["command","command"]},"supportedExportFormats":[{"id":"id","exportableContents":["EXPORTABLE_CONTENT_UNSPECIFIED","EXPORTABLE_CONTENT_UNSPECIFIED"]},{"id":"id","exportableContents":["EXPORTABLE_CONTENT_UNSPECIFIED","EXPORTABLE_CONTENT_UNSPECIFIED"]}],"trainingPipeline":"trainingPipeline","updateTime":"updateTime","labels":{"key":"labels"},"explanationSpec":{"metadata":{"outputs":{"key":{"outputTensorName":"outputTensorName","indexDisplayNameMapping":"","displayNameMappingKey":"displayNameMappingKey"}},"inputs":{"key":{"groupName":"groupName","visualization":{"clipPercentLowerbound":4.145608,"clipPercentUpperbound":7.386282,"overlayType":"OVERLAY_TYPE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","colorMap":"COLOR_MAP_UNSPECIFIED","polarity":"POLARITY_UNSPECIFIED"},"modality":"modality","indexFeatureMapping":["indexFeatureMapping","indexFeatureMapping"],"inputTensorName":"inputTensorName","encodedBaselines":["",""],"denseShapeTensorName":"denseShapeTensorName","indicesTensorName":"indicesTensorName","encoding":"ENCODING_UNSPECIFIED","inputBaselines":["",""],"encodedTensorName":"encodedTensorName","featureValueDomain":{"originalStddev":2.027123,"minValue":9.301444,"maxValue":7.0614014,"originalMean":3.6160767}}},"featureAttributionsSchemaUri":"featureAttributionsSchemaUri","latentSpaceSource":"latentSpaceSource"},"parameters":{"topK":5,"examples":{"neighborCount":1,"presets":{"modality":"MODALITY_UNSPECIFIED","query":"PRECISE"},"nearestNeighborSearchConfig":"","gcsSource":{"uris":["uris","uris"]},"exampleGcsSource":{"dataFormat":"DATA_FORMAT_UNSPECIFIED","gcsSource":{"uris":["uris","uris"]}}},"outputIndices":["",""],"sampledShapleyAttribution":{"pathCount":4},"xraiAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":9},"integratedGradientsAttribution":{"blurBaselineConfig":{"maxBlurSigma":1.0246457},"smoothGradConfig":{"noiseSigma":6.846853,"featureNoiseSigma":{"noiseSigma":[{"sigma":1.4894159,"name":"name"},{"sigma":1.4894159,"name":"name"}]},"noisySampleCount":7},"stepCount":1}}},"versionId":"versionId","createTime":"createTime","name":"name","etag":"etag","deployedModels":[{"endpoint":"endpoint","deployedModelId":"deployedModelId"},{"endpoint":"endpoint","deployedModelId":"deployedModelId"}]},"state":"PIPELINE_STATE_UNSPECIFIED","parentModel":"parentModel","inputDataConfig":{"fractionSplit":{"validationFraction":1.4658129805029452,"testFraction":0.8008281904610115,"trainingFraction":6.027456183070403},"gcsDestination":{"outputUriPrefix":"outputUriPrefix"},"bigqueryDestination":{"outputUri":"outputUri"},"savedQueryId":"savedQueryId","persistMlUseAssignment":True,"datasetId":"datasetId","annotationSchemaUri":"annotationSchemaUri","filterSplit":{"validationFilter":"validationFilter","testFilter":"testFilter","trainingFilter":"trainingFilter"},"stratifiedSplit":{"validationFraction":2.3021358869347655,"testFraction":5.962133916683182,"trainingFraction":5.637376656633329,"key":"key"},"predefinedSplit":{"key":"key"},"timestampSplit":{"validationFraction":3.616076749251911,"testFraction":7.061401241503109,"trainingFraction":9.301444243932576,"key":"key"},"annotationsFilter":"annotationsFilter"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/trainingPipelines'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_training_pipelines_list(client):
    """Test case for aiplatform_projects_locations_training_pipelines_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/trainingPipelines'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_training_pipelines_operations_cancel(client):
    """Test case for aiplatform_projects_locations_training_pipelines_operations_cancel

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_training_pipelines_operations_delete(client):
    """Test case for aiplatform_projects_locations_training_pipelines_operations_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('force', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_training_pipelines_operations_list(client):
    """Test case for aiplatform_projects_locations_training_pipelines_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aiplatform_projects_locations_training_pipelines_operations_wait(client):
    """Test case for aiplatform_projects_locations_training_pipelines_operations_wait

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('timeout', 'timeout_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namewai}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

