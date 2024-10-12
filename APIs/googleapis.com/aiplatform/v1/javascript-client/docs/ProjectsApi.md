# VertexAiApi.ProjectsApi

All URIs are relative to *https://aiplatform.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aiplatformProjectsLocationsBatchPredictionJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsBatchPredictionJobsCreate) | **POST** /v1/{parent}/batchPredictionJobs | 
[**aiplatformProjectsLocationsBatchPredictionJobsList**](ProjectsApi.md#aiplatformProjectsLocationsBatchPredictionJobsList) | **GET** /v1/{parent}/batchPredictionJobs | 
[**aiplatformProjectsLocationsCustomJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsCustomJobsCreate) | **POST** /v1/{parent}/customJobs | 
[**aiplatformProjectsLocationsCustomJobsList**](ProjectsApi.md#aiplatformProjectsLocationsCustomJobsList) | **GET** /v1/{parent}/customJobs | 
[**aiplatformProjectsLocationsDataLabelingJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsDataLabelingJobsCreate) | **POST** /v1/{parent}/dataLabelingJobs | 
[**aiplatformProjectsLocationsDataLabelingJobsList**](ProjectsApi.md#aiplatformProjectsLocationsDataLabelingJobsList) | **GET** /v1/{parent}/dataLabelingJobs | 
[**aiplatformProjectsLocationsDatasetsCreate**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsCreate) | **POST** /v1/{parent}/datasets | 
[**aiplatformProjectsLocationsDatasetsDataItemsAnnotationsList**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsDataItemsAnnotationsList) | **GET** /v1/{parent}/annotations | 
[**aiplatformProjectsLocationsDatasetsDataItemsList**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsDataItemsList) | **GET** /v1/{parent}/dataItems | 
[**aiplatformProjectsLocationsDatasetsDatasetVersionsCreate**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsDatasetVersionsCreate) | **POST** /v1/{parent}/datasetVersions | 
[**aiplatformProjectsLocationsDatasetsDatasetVersionsList**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsDatasetVersionsList) | **GET** /v1/{parent}/datasetVersions | 
[**aiplatformProjectsLocationsDatasetsDatasetVersionsRestore**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsDatasetVersionsRestore) | **GET** /v1/{name}:restore | 
[**aiplatformProjectsLocationsDatasetsImport**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsImport) | **POST** /v1/{name}:import | 
[**aiplatformProjectsLocationsDatasetsList**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsList) | **GET** /v1/{parent}/datasets | 
[**aiplatformProjectsLocationsDatasetsSavedQueriesList**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsSavedQueriesList) | **GET** /v1/{parent}/savedQueries | 
[**aiplatformProjectsLocationsDatasetsSearchDataItems**](ProjectsApi.md#aiplatformProjectsLocationsDatasetsSearchDataItems) | **GET** /v1/{dataset}:searchDataItems | 
[**aiplatformProjectsLocationsDeploymentResourcePoolsCreate**](ProjectsApi.md#aiplatformProjectsLocationsDeploymentResourcePoolsCreate) | **POST** /v1/{parent}/deploymentResourcePools | 
[**aiplatformProjectsLocationsDeploymentResourcePoolsList**](ProjectsApi.md#aiplatformProjectsLocationsDeploymentResourcePoolsList) | **GET** /v1/{parent}/deploymentResourcePools | 
[**aiplatformProjectsLocationsDeploymentResourcePoolsQueryDeployedModels**](ProjectsApi.md#aiplatformProjectsLocationsDeploymentResourcePoolsQueryDeployedModels) | **GET** /v1/{deploymentResourcePool}:queryDeployedModels | 
[**aiplatformProjectsLocationsEndpointsCreate**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsCreate) | **POST** /v1/{parent}/endpoints | 
[**aiplatformProjectsLocationsEndpointsDeployModel**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsDeployModel) | **POST** /v1/{endpoint}:deployModel | 
[**aiplatformProjectsLocationsEndpointsDirectPredict**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsDirectPredict) | **POST** /v1/{endpoint}:directPredict | 
[**aiplatformProjectsLocationsEndpointsDirectRawPredict**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsDirectRawPredict) | **POST** /v1/{endpoint}:directRawPredict | 
[**aiplatformProjectsLocationsEndpointsExplain**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsExplain) | **POST** /v1/{endpoint}:explain | 
[**aiplatformProjectsLocationsEndpointsList**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsList) | **GET** /v1/{parent}/endpoints | 
[**aiplatformProjectsLocationsEndpointsMutateDeployedModel**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsMutateDeployedModel) | **POST** /v1/{endpoint}:mutateDeployedModel | 
[**aiplatformProjectsLocationsEndpointsUndeployModel**](ProjectsApi.md#aiplatformProjectsLocationsEndpointsUndeployModel) | **POST** /v1/{endpoint}:undeployModel | 
[**aiplatformProjectsLocationsFeatureGroupsCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeatureGroupsCreate) | **POST** /v1/{parent}/featureGroups | 
[**aiplatformProjectsLocationsFeatureGroupsList**](ProjectsApi.md#aiplatformProjectsLocationsFeatureGroupsList) | **GET** /v1/{parent}/featureGroups | 
[**aiplatformProjectsLocationsFeatureOnlineStoresCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresCreate) | **POST** /v1/{parent}/featureOnlineStores | 
[**aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsCreate) | **POST** /v1/{parent}/featureViews | 
[**aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFeatureViewSyncsList**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFeatureViewSyncsList) | **GET** /v1/{parent}/featureViewSyncs | 
[**aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFetchFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFetchFeatureValues) | **POST** /v1/{featureView}:fetchFeatureValues | 
[**aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsList**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsList) | **GET** /v1/{parent}/featureViews | 
[**aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSearchNearestEntities**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSearchNearestEntities) | **POST** /v1/{featureView}:searchNearestEntities | 
[**aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSync**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSync) | **POST** /v1/{featureView}:sync | 
[**aiplatformProjectsLocationsFeatureOnlineStoresList**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresList) | **GET** /v1/{parent}/featureOnlineStores | 
[**aiplatformProjectsLocationsFeatureOnlineStoresOperationsListWait**](ProjectsApi.md#aiplatformProjectsLocationsFeatureOnlineStoresOperationsListWait) | **GET** /v1/{name}:wait | 
[**aiplatformProjectsLocationsFeaturestoresBatchReadFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresBatchReadFeatureValues) | **POST** /v1/{featurestore}:batchReadFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresCreate) | **POST** /v1/{parent}/featurestores | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesCreate) | **POST** /v1/{parent}/entityTypes | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesDeleteFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesDeleteFeatureValues) | **POST** /v1/{entityType}:deleteFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesExportFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesExportFeatureValues) | **POST** /v1/{entityType}:exportFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesBatchCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesBatchCreate) | **POST** /v1/{parent}/features:batchCreate | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesCreate**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesCreate) | **POST** /v1/{parent}/features | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesList**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesList) | **GET** /v1/{parent}/features | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesImportFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesImportFeatureValues) | **POST** /v1/{entityType}:importFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesList**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesList) | **GET** /v1/{parent}/entityTypes | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesReadFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesReadFeatureValues) | **POST** /v1/{entityType}:readFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesStreamingReadFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesStreamingReadFeatureValues) | **POST** /v1/{entityType}:streamingReadFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresEntityTypesWriteFeatureValues**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresEntityTypesWriteFeatureValues) | **POST** /v1/{entityType}:writeFeatureValues | 
[**aiplatformProjectsLocationsFeaturestoresList**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresList) | **GET** /v1/{parent}/featurestores | 
[**aiplatformProjectsLocationsFeaturestoresSearchFeatures**](ProjectsApi.md#aiplatformProjectsLocationsFeaturestoresSearchFeatures) | **GET** /v1/{location}/featurestores:searchFeatures | 
[**aiplatformProjectsLocationsHyperparameterTuningJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsHyperparameterTuningJobsCreate) | **POST** /v1/{parent}/hyperparameterTuningJobs | 
[**aiplatformProjectsLocationsHyperparameterTuningJobsList**](ProjectsApi.md#aiplatformProjectsLocationsHyperparameterTuningJobsList) | **GET** /v1/{parent}/hyperparameterTuningJobs | 
[**aiplatformProjectsLocationsIndexEndpointsCreate**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsCreate) | **POST** /v1/{parent}/indexEndpoints | 
[**aiplatformProjectsLocationsIndexEndpointsDeployIndex**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsDeployIndex) | **POST** /v1/{indexEndpoint}:deployIndex | 
[**aiplatformProjectsLocationsIndexEndpointsFindNeighbors**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsFindNeighbors) | **POST** /v1/{indexEndpoint}:findNeighbors | 
[**aiplatformProjectsLocationsIndexEndpointsList**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsList) | **GET** /v1/{parent}/indexEndpoints | 
[**aiplatformProjectsLocationsIndexEndpointsMutateDeployedIndex**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsMutateDeployedIndex) | **POST** /v1/{indexEndpoint}:mutateDeployedIndex | 
[**aiplatformProjectsLocationsIndexEndpointsReadIndexDatapoints**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsReadIndexDatapoints) | **POST** /v1/{indexEndpoint}:readIndexDatapoints | 
[**aiplatformProjectsLocationsIndexEndpointsUndeployIndex**](ProjectsApi.md#aiplatformProjectsLocationsIndexEndpointsUndeployIndex) | **POST** /v1/{indexEndpoint}:undeployIndex | 
[**aiplatformProjectsLocationsIndexesCreate**](ProjectsApi.md#aiplatformProjectsLocationsIndexesCreate) | **POST** /v1/{parent}/indexes | 
[**aiplatformProjectsLocationsIndexesList**](ProjectsApi.md#aiplatformProjectsLocationsIndexesList) | **GET** /v1/{parent}/indexes | 
[**aiplatformProjectsLocationsIndexesRemoveDatapoints**](ProjectsApi.md#aiplatformProjectsLocationsIndexesRemoveDatapoints) | **POST** /v1/{index}:removeDatapoints | 
[**aiplatformProjectsLocationsIndexesUpsertDatapoints**](ProjectsApi.md#aiplatformProjectsLocationsIndexesUpsertDatapoints) | **POST** /v1/{index}:upsertDatapoints | 
[**aiplatformProjectsLocationsList**](ProjectsApi.md#aiplatformProjectsLocationsList) | **GET** /v1/{name}/locations | 
[**aiplatformProjectsLocationsMetadataStoresArtifactsCreate**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresArtifactsCreate) | **POST** /v1/{parent}/artifacts | 
[**aiplatformProjectsLocationsMetadataStoresArtifactsList**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresArtifactsList) | **GET** /v1/{parent}/artifacts | 
[**aiplatformProjectsLocationsMetadataStoresArtifactsPurge**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresArtifactsPurge) | **POST** /v1/{parent}/artifacts:purge | 
[**aiplatformProjectsLocationsMetadataStoresArtifactsQueryArtifactLineageSubgraph**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresArtifactsQueryArtifactLineageSubgraph) | **GET** /v1/{artifact}:queryArtifactLineageSubgraph | 
[**aiplatformProjectsLocationsMetadataStoresContextsAddContextArtifactsAndExecutions**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsAddContextArtifactsAndExecutions) | **POST** /v1/{context}:addContextArtifactsAndExecutions | 
[**aiplatformProjectsLocationsMetadataStoresContextsAddContextChildren**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsAddContextChildren) | **POST** /v1/{context}:addContextChildren | 
[**aiplatformProjectsLocationsMetadataStoresContextsCreate**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsCreate) | **POST** /v1/{parent}/contexts | 
[**aiplatformProjectsLocationsMetadataStoresContextsList**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsList) | **GET** /v1/{parent}/contexts | 
[**aiplatformProjectsLocationsMetadataStoresContextsPurge**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsPurge) | **POST** /v1/{parent}/contexts:purge | 
[**aiplatformProjectsLocationsMetadataStoresContextsQueryContextLineageSubgraph**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsQueryContextLineageSubgraph) | **GET** /v1/{context}:queryContextLineageSubgraph | 
[**aiplatformProjectsLocationsMetadataStoresContextsRemoveContextChildren**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresContextsRemoveContextChildren) | **POST** /v1/{context}:removeContextChildren | 
[**aiplatformProjectsLocationsMetadataStoresCreate**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresCreate) | **POST** /v1/{parent}/metadataStores | 
[**aiplatformProjectsLocationsMetadataStoresExecutionsAddExecutionEvents**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresExecutionsAddExecutionEvents) | **POST** /v1/{execution}:addExecutionEvents | 
[**aiplatformProjectsLocationsMetadataStoresExecutionsCreate**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresExecutionsCreate) | **POST** /v1/{parent}/executions | 
[**aiplatformProjectsLocationsMetadataStoresExecutionsList**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresExecutionsList) | **GET** /v1/{parent}/executions | 
[**aiplatformProjectsLocationsMetadataStoresExecutionsPurge**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresExecutionsPurge) | **POST** /v1/{parent}/executions:purge | 
[**aiplatformProjectsLocationsMetadataStoresExecutionsQueryExecutionInputsAndOutputs**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresExecutionsQueryExecutionInputsAndOutputs) | **GET** /v1/{execution}:queryExecutionInputsAndOutputs | 
[**aiplatformProjectsLocationsMetadataStoresList**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresList) | **GET** /v1/{parent}/metadataStores | 
[**aiplatformProjectsLocationsMetadataStoresMetadataSchemasCreate**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresMetadataSchemasCreate) | **POST** /v1/{parent}/metadataSchemas | 
[**aiplatformProjectsLocationsMetadataStoresMetadataSchemasList**](ProjectsApi.md#aiplatformProjectsLocationsMetadataStoresMetadataSchemasList) | **GET** /v1/{parent}/metadataSchemas | 
[**aiplatformProjectsLocationsMigratableResourcesBatchMigrate**](ProjectsApi.md#aiplatformProjectsLocationsMigratableResourcesBatchMigrate) | **POST** /v1/{parent}/migratableResources:batchMigrate | 
[**aiplatformProjectsLocationsMigratableResourcesSearch**](ProjectsApi.md#aiplatformProjectsLocationsMigratableResourcesSearch) | **POST** /v1/{parent}/migratableResources:search | 
[**aiplatformProjectsLocationsModelDeploymentMonitoringJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsModelDeploymentMonitoringJobsCreate) | **POST** /v1/{parent}/modelDeploymentMonitoringJobs | 
[**aiplatformProjectsLocationsModelDeploymentMonitoringJobsList**](ProjectsApi.md#aiplatformProjectsLocationsModelDeploymentMonitoringJobsList) | **GET** /v1/{parent}/modelDeploymentMonitoringJobs | 
[**aiplatformProjectsLocationsModelDeploymentMonitoringJobsSearchModelDeploymentMonitoringStatsAnomalies**](ProjectsApi.md#aiplatformProjectsLocationsModelDeploymentMonitoringJobsSearchModelDeploymentMonitoringStatsAnomalies) | **POST** /v1/{modelDeploymentMonitoringJob}:searchModelDeploymentMonitoringStatsAnomalies | 
[**aiplatformProjectsLocationsModelsCopy**](ProjectsApi.md#aiplatformProjectsLocationsModelsCopy) | **POST** /v1/{parent}/models:copy | 
[**aiplatformProjectsLocationsModelsDeleteVersion**](ProjectsApi.md#aiplatformProjectsLocationsModelsDeleteVersion) | **DELETE** /v1/{name}:deleteVersion | 
[**aiplatformProjectsLocationsModelsEvaluationsImport**](ProjectsApi.md#aiplatformProjectsLocationsModelsEvaluationsImport) | **POST** /v1/{parent}/evaluations:import | 
[**aiplatformProjectsLocationsModelsEvaluationsList**](ProjectsApi.md#aiplatformProjectsLocationsModelsEvaluationsList) | **GET** /v1/{parent}/evaluations | 
[**aiplatformProjectsLocationsModelsEvaluationsSlicesBatchImport**](ProjectsApi.md#aiplatformProjectsLocationsModelsEvaluationsSlicesBatchImport) | **POST** /v1/{parent}:batchImport | 
[**aiplatformProjectsLocationsModelsEvaluationsSlicesList**](ProjectsApi.md#aiplatformProjectsLocationsModelsEvaluationsSlicesList) | **GET** /v1/{parent}/slices | 
[**aiplatformProjectsLocationsModelsExport**](ProjectsApi.md#aiplatformProjectsLocationsModelsExport) | **POST** /v1/{name}:export | 
[**aiplatformProjectsLocationsModelsList**](ProjectsApi.md#aiplatformProjectsLocationsModelsList) | **GET** /v1/{parent}/models | 
[**aiplatformProjectsLocationsModelsListVersions**](ProjectsApi.md#aiplatformProjectsLocationsModelsListVersions) | **GET** /v1/{name}:listVersions | 
[**aiplatformProjectsLocationsModelsMergeVersionAliases**](ProjectsApi.md#aiplatformProjectsLocationsModelsMergeVersionAliases) | **POST** /v1/{name}:mergeVersionAliases | 
[**aiplatformProjectsLocationsModelsUpdateExplanationDataset**](ProjectsApi.md#aiplatformProjectsLocationsModelsUpdateExplanationDataset) | **POST** /v1/{model}:updateExplanationDataset | 
[**aiplatformProjectsLocationsModelsUpload**](ProjectsApi.md#aiplatformProjectsLocationsModelsUpload) | **POST** /v1/{parent}/models:upload | 
[**aiplatformProjectsLocationsNasJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsNasJobsCreate) | **POST** /v1/{parent}/nasJobs | 
[**aiplatformProjectsLocationsNasJobsList**](ProjectsApi.md#aiplatformProjectsLocationsNasJobsList) | **GET** /v1/{parent}/nasJobs | 
[**aiplatformProjectsLocationsNasJobsNasTrialDetailsList**](ProjectsApi.md#aiplatformProjectsLocationsNasJobsNasTrialDetailsList) | **GET** /v1/{parent}/nasTrialDetails | 
[**aiplatformProjectsLocationsNotebookRuntimeTemplatesCreate**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimeTemplatesCreate) | **POST** /v1/{parent}/notebookRuntimeTemplates | 
[**aiplatformProjectsLocationsNotebookRuntimeTemplatesGetIamPolicy**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimeTemplatesGetIamPolicy) | **POST** /v1/{resource}:getIamPolicy | 
[**aiplatformProjectsLocationsNotebookRuntimeTemplatesList**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimeTemplatesList) | **GET** /v1/{parent}/notebookRuntimeTemplates | 
[**aiplatformProjectsLocationsNotebookRuntimeTemplatesSetIamPolicy**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimeTemplatesSetIamPolicy) | **POST** /v1/{resource}:setIamPolicy | 
[**aiplatformProjectsLocationsNotebookRuntimeTemplatesTestIamPermissions**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimeTemplatesTestIamPermissions) | **POST** /v1/{resource}:testIamPermissions | 
[**aiplatformProjectsLocationsNotebookRuntimesAssign**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimesAssign) | **POST** /v1/{parent}/notebookRuntimes:assign | 
[**aiplatformProjectsLocationsNotebookRuntimesList**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimesList) | **GET** /v1/{parent}/notebookRuntimes | 
[**aiplatformProjectsLocationsNotebookRuntimesStart**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimesStart) | **POST** /v1/{name}:start | 
[**aiplatformProjectsLocationsNotebookRuntimesUpgrade**](ProjectsApi.md#aiplatformProjectsLocationsNotebookRuntimesUpgrade) | **POST** /v1/{name}:upgrade | 
[**aiplatformProjectsLocationsPipelineJobsCreate**](ProjectsApi.md#aiplatformProjectsLocationsPipelineJobsCreate) | **POST** /v1/{parent}/pipelineJobs | 
[**aiplatformProjectsLocationsPipelineJobsList**](ProjectsApi.md#aiplatformProjectsLocationsPipelineJobsList) | **GET** /v1/{parent}/pipelineJobs | 
[**aiplatformProjectsLocationsPublishersModelsComputeTokens**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsComputeTokens) | **POST** /v1/{endpoint}:computeTokens | 
[**aiplatformProjectsLocationsPublishersModelsCountTokens**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsCountTokens) | **POST** /v1/{endpoint}:countTokens | 
[**aiplatformProjectsLocationsPublishersModelsGenerateContent**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsGenerateContent) | **POST** /v1/{model}:generateContent | 
[**aiplatformProjectsLocationsPublishersModelsPredict**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsPredict) | **POST** /v1/{endpoint}:predict | 
[**aiplatformProjectsLocationsPublishersModelsRawPredict**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsRawPredict) | **POST** /v1/{endpoint}:rawPredict | 
[**aiplatformProjectsLocationsPublishersModelsServerStreamingPredict**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsServerStreamingPredict) | **POST** /v1/{endpoint}:serverStreamingPredict | 
[**aiplatformProjectsLocationsPublishersModelsStreamGenerateContent**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsStreamGenerateContent) | **POST** /v1/{model}:streamGenerateContent | 
[**aiplatformProjectsLocationsPublishersModelsStreamRawPredict**](ProjectsApi.md#aiplatformProjectsLocationsPublishersModelsStreamRawPredict) | **POST** /v1/{endpoint}:streamRawPredict | 
[**aiplatformProjectsLocationsSchedulesCreate**](ProjectsApi.md#aiplatformProjectsLocationsSchedulesCreate) | **POST** /v1/{parent}/schedules | 
[**aiplatformProjectsLocationsSchedulesList**](ProjectsApi.md#aiplatformProjectsLocationsSchedulesList) | **GET** /v1/{parent}/schedules | 
[**aiplatformProjectsLocationsSchedulesPause**](ProjectsApi.md#aiplatformProjectsLocationsSchedulesPause) | **POST** /v1/{name}:pause | 
[**aiplatformProjectsLocationsSchedulesResume**](ProjectsApi.md#aiplatformProjectsLocationsSchedulesResume) | **POST** /v1/{name}:resume | 
[**aiplatformProjectsLocationsSpecialistPoolsCreate**](ProjectsApi.md#aiplatformProjectsLocationsSpecialistPoolsCreate) | **POST** /v1/{parent}/specialistPools | 
[**aiplatformProjectsLocationsSpecialistPoolsList**](ProjectsApi.md#aiplatformProjectsLocationsSpecialistPoolsList) | **GET** /v1/{parent}/specialistPools | 
[**aiplatformProjectsLocationsStudiesCreate**](ProjectsApi.md#aiplatformProjectsLocationsStudiesCreate) | **POST** /v1/{parent}/studies | 
[**aiplatformProjectsLocationsStudiesList**](ProjectsApi.md#aiplatformProjectsLocationsStudiesList) | **GET** /v1/{parent}/studies | 
[**aiplatformProjectsLocationsStudiesLookup**](ProjectsApi.md#aiplatformProjectsLocationsStudiesLookup) | **POST** /v1/{parent}/studies:lookup | 
[**aiplatformProjectsLocationsStudiesTrialsAddTrialMeasurement**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsAddTrialMeasurement) | **POST** /v1/{trialName}:addTrialMeasurement | 
[**aiplatformProjectsLocationsStudiesTrialsCheckTrialEarlyStoppingState**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsCheckTrialEarlyStoppingState) | **POST** /v1/{trialName}:checkTrialEarlyStoppingState | 
[**aiplatformProjectsLocationsStudiesTrialsComplete**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsComplete) | **POST** /v1/{name}:complete | 
[**aiplatformProjectsLocationsStudiesTrialsCreate**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsCreate) | **POST** /v1/{parent}/trials | 
[**aiplatformProjectsLocationsStudiesTrialsList**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsList) | **GET** /v1/{parent}/trials | 
[**aiplatformProjectsLocationsStudiesTrialsListOptimalTrials**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsListOptimalTrials) | **POST** /v1/{parent}/trials:listOptimalTrials | 
[**aiplatformProjectsLocationsStudiesTrialsStop**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsStop) | **POST** /v1/{name}:stop | 
[**aiplatformProjectsLocationsStudiesTrialsSuggest**](ProjectsApi.md#aiplatformProjectsLocationsStudiesTrialsSuggest) | **POST** /v1/{parent}/trials:suggest | 
[**aiplatformProjectsLocationsTensorboardsBatchRead**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsBatchRead) | **GET** /v1/{tensorboard}:batchRead | 
[**aiplatformProjectsLocationsTensorboardsCreate**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsCreate) | **POST** /v1/{parent}/tensorboards | 
[**aiplatformProjectsLocationsTensorboardsExperimentsBatchCreate**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsBatchCreate) | **POST** /v1/{parent}:batchCreate | 
[**aiplatformProjectsLocationsTensorboardsExperimentsCreate**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsCreate) | **POST** /v1/{parent}/experiments | 
[**aiplatformProjectsLocationsTensorboardsExperimentsList**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsList) | **GET** /v1/{parent}/experiments | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsBatchCreate**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsBatchCreate) | **POST** /v1/{parent}/runs:batchCreate | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsCreate**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsCreate) | **POST** /v1/{parent}/runs | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsList**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsList) | **GET** /v1/{parent}/runs | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesCreate**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesCreate) | **POST** /v1/{parent}/timeSeries | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesExportTensorboardTimeSeries**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesExportTensorboardTimeSeries) | **POST** /v1/{tensorboardTimeSeries}:exportTensorboardTimeSeries | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesList**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesList) | **GET** /v1/{parent}/timeSeries | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesPatch**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesPatch) | **PATCH** /v1/{name} | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesRead**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesRead) | **GET** /v1/{tensorboardTimeSeries}:read | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesReadBlobData**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesReadBlobData) | **GET** /v1/{timeSeries}:readBlobData | 
[**aiplatformProjectsLocationsTensorboardsExperimentsRunsWrite**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsRunsWrite) | **POST** /v1/{tensorboardRun}:write | 
[**aiplatformProjectsLocationsTensorboardsExperimentsWrite**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsExperimentsWrite) | **POST** /v1/{tensorboardExperiment}:write | 
[**aiplatformProjectsLocationsTensorboardsList**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsList) | **GET** /v1/{parent}/tensorboards | 
[**aiplatformProjectsLocationsTensorboardsReadSize**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsReadSize) | **GET** /v1/{tensorboard}:readSize | 
[**aiplatformProjectsLocationsTensorboardsReadUsage**](ProjectsApi.md#aiplatformProjectsLocationsTensorboardsReadUsage) | **GET** /v1/{tensorboard}:readUsage | 
[**aiplatformProjectsLocationsTrainingPipelinesCreate**](ProjectsApi.md#aiplatformProjectsLocationsTrainingPipelinesCreate) | **POST** /v1/{parent}/trainingPipelines | 
[**aiplatformProjectsLocationsTrainingPipelinesList**](ProjectsApi.md#aiplatformProjectsLocationsTrainingPipelinesList) | **GET** /v1/{parent}/trainingPipelines | 
[**aiplatformProjectsLocationsTrainingPipelinesOperationsCancel**](ProjectsApi.md#aiplatformProjectsLocationsTrainingPipelinesOperationsCancel) | **POST** /v1/{name}:cancel | 
[**aiplatformProjectsLocationsTrainingPipelinesOperationsDelete**](ProjectsApi.md#aiplatformProjectsLocationsTrainingPipelinesOperationsDelete) | **DELETE** /v1/{name} | 
[**aiplatformProjectsLocationsTrainingPipelinesOperationsList**](ProjectsApi.md#aiplatformProjectsLocationsTrainingPipelinesOperationsList) | **GET** /v1/{name}/operations | 
[**aiplatformProjectsLocationsTrainingPipelinesOperationsWait**](ProjectsApi.md#aiplatformProjectsLocationsTrainingPipelinesOperationsWait) | **POST** /v1/{name}:wait | 



## aiplatformProjectsLocationsBatchPredictionJobsCreate

> GoogleCloudAiplatformV1BatchPredictionJob aiplatformProjectsLocationsBatchPredictionJobsCreate(parent, opts)



Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the BatchPredictionJob in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchPredictionJob': new VertexAiApi.GoogleCloudAiplatformV1BatchPredictionJob() // GoogleCloudAiplatformV1BatchPredictionJob | 
};
apiInstance.aiplatformProjectsLocationsBatchPredictionJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the BatchPredictionJob in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchPredictionJob** | [**GoogleCloudAiplatformV1BatchPredictionJob**](GoogleCloudAiplatformV1BatchPredictionJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1BatchPredictionJob**](GoogleCloudAiplatformV1BatchPredictionJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsBatchPredictionJobsList

> GoogleCloudAiplatformV1ListBatchPredictionJobsResponse aiplatformProjectsLocationsBatchPredictionJobsList(parent, opts)



Lists BatchPredictionJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the BatchPredictionJobs from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `model_display_name` supports `=`, `!=` comparisons. * `state` supports `=`, `!=` comparisons. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"JOB_STATE_SUCCEEDED\" AND display_name:\"my_job_*\"` * `state!=\"JOB_STATE_FAILED\" OR display_name=\"my_job\"` * `NOT display_name=\"my_job\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `labels.keyA=valueA` * `labels.keyB:*`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListBatchPredictionJobsResponse.next_page_token of the previous JobService.ListBatchPredictionJobs call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsBatchPredictionJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the BatchPredictionJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;model_display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListBatchPredictionJobsResponse.next_page_token of the previous JobService.ListBatchPredictionJobs call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListBatchPredictionJobsResponse**](GoogleCloudAiplatformV1ListBatchPredictionJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsCustomJobsCreate

> GoogleCloudAiplatformV1CustomJob aiplatformProjectsLocationsCustomJobsCreate(parent, opts)



Creates a CustomJob. A created CustomJob right away will be attempted to be run.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the CustomJob in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1CustomJob': new VertexAiApi.GoogleCloudAiplatformV1CustomJob() // GoogleCloudAiplatformV1CustomJob | 
};
apiInstance.aiplatformProjectsLocationsCustomJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the CustomJob in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1CustomJob** | [**GoogleCloudAiplatformV1CustomJob**](GoogleCloudAiplatformV1CustomJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1CustomJob**](GoogleCloudAiplatformV1CustomJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsCustomJobsList

> GoogleCloudAiplatformV1ListCustomJobsResponse aiplatformProjectsLocationsCustomJobsList(parent, opts)



Lists CustomJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the CustomJobs from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `state` supports `=`, `!=` comparisons. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"JOB_STATE_SUCCEEDED\" AND display_name:\"my_job_*\"` * `state!=\"JOB_STATE_FAILED\" OR display_name=\"my_job\"` * `NOT display_name=\"my_job\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `labels.keyA=valueA` * `labels.keyB:*`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListCustomJobsResponse.next_page_token of the previous JobService.ListCustomJobs call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsCustomJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the CustomJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListCustomJobsResponse.next_page_token of the previous JobService.ListCustomJobs call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListCustomJobsResponse**](GoogleCloudAiplatformV1ListCustomJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDataLabelingJobsCreate

> GoogleCloudAiplatformV1DataLabelingJob aiplatformProjectsLocationsDataLabelingJobsCreate(parent, opts)



Creates a DataLabelingJob.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent of the DataLabelingJob. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DataLabelingJob': new VertexAiApi.GoogleCloudAiplatformV1DataLabelingJob() // GoogleCloudAiplatformV1DataLabelingJob | 
};
apiInstance.aiplatformProjectsLocationsDataLabelingJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent of the DataLabelingJob. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DataLabelingJob** | [**GoogleCloudAiplatformV1DataLabelingJob**](GoogleCloudAiplatformV1DataLabelingJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1DataLabelingJob**](GoogleCloudAiplatformV1DataLabelingJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsDataLabelingJobsList

> GoogleCloudAiplatformV1ListDataLabelingJobsResponse aiplatformProjectsLocationsDataLabelingJobsList(parent, opts)



Lists DataLabelingJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent of the DataLabelingJob. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `state` supports `=`, `!=` comparisons. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"JOB_STATE_SUCCEEDED\" AND display_name:\"my_job_*\"` * `state!=\"JOB_STATE_FAILED\" OR display_name=\"my_job\"` * `NOT display_name=\"my_job\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `labels.keyA=valueA` * `labels.keyB:*`
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order by default. Use `desc` after a field name for descending.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read. FieldMask represents a set of symbolic field paths. For example, the mask can be `paths: \"name\"`. The \"name\" here is a field in DataLabelingJob. If this field is not set, all fields of the DataLabelingJob are returned.
};
apiInstance.aiplatformProjectsLocationsDataLabelingJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent of the DataLabelingJob. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60; | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order by default. Use &#x60;desc&#x60; after a field name for descending. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. FieldMask represents a set of symbolic field paths. For example, the mask can be &#x60;paths: \&quot;name\&quot;&#x60;. The \&quot;name\&quot; here is a field in DataLabelingJob. If this field is not set, all fields of the DataLabelingJob are returned. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListDataLabelingJobsResponse**](GoogleCloudAiplatformV1ListDataLabelingJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsDatasetsCreate(parent, opts)



Creates a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the Dataset in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1Dataset': new VertexAiApi.GoogleCloudAiplatformV1Dataset() // GoogleCloudAiplatformV1Dataset | 
};
apiInstance.aiplatformProjectsLocationsDatasetsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the Dataset in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1Dataset** | [**GoogleCloudAiplatformV1Dataset**](GoogleCloudAiplatformV1Dataset.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsDataItemsAnnotationsList

> GoogleCloudAiplatformV1ListAnnotationsResponse aiplatformProjectsLocationsDatasetsDataItemsAnnotationsList(parent, opts)



Lists Annotations belongs to a dataitem

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the DataItem to list Annotations from. Format: `projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsDatasetsDataItemsAnnotationsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the DataItem to list Annotations from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListAnnotationsResponse**](GoogleCloudAiplatformV1ListAnnotationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsDataItemsList

> GoogleCloudAiplatformV1ListDataItemsResponse aiplatformProjectsLocationsDatasetsDataItemsList(parent, opts)



Lists DataItems in a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Dataset to list DataItems from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsDatasetsDataItemsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Dataset to list DataItems from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListDataItemsResponse**](GoogleCloudAiplatformV1ListDataItemsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsDatasetVersionsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsDatasetsDatasetVersionsCreate(parent, opts)



Create a version from a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DatasetVersion': new VertexAiApi.GoogleCloudAiplatformV1DatasetVersion() // GoogleCloudAiplatformV1DatasetVersion | 
};
apiInstance.aiplatformProjectsLocationsDatasetsDatasetVersionsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the Dataset resource. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DatasetVersion** | [**GoogleCloudAiplatformV1DatasetVersion**](GoogleCloudAiplatformV1DatasetVersion.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsDatasetVersionsList

> GoogleCloudAiplatformV1ListDatasetVersionsResponse aiplatformProjectsLocationsDatasetsDatasetVersionsList(parent, opts)



Lists DatasetVersions in a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Dataset to list DatasetVersions from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. The standard list filter.
  'orderBy': "orderBy_example", // String | Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'pageSize': 56, // Number | Optional. The standard list page size.
  'pageToken': "pageToken_example", // String | Optional. The standard list page token.
  'readMask': "readMask_example" // String | Optional. Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsDatasetsDatasetVersionsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Dataset to list DatasetVersions from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. The standard list filter. | [optional] 
 **orderBy** | **String**| Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **pageSize** | **Number**| Optional. The standard list page size. | [optional] 
 **pageToken** | **String**| Optional. The standard list page token. | [optional] 
 **readMask** | **String**| Optional. Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListDatasetVersionsResponse**](GoogleCloudAiplatformV1ListDatasetVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsDatasetVersionsRestore

> GoogleLongrunningOperation aiplatformProjectsLocationsDatasetsDatasetVersionsRestore(name, opts)



Restores a dataset version.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the DatasetVersion resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.aiplatformProjectsLocationsDatasetsDatasetVersionsRestore(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the DatasetVersion resource. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsImport

> GoogleLongrunningOperation aiplatformProjectsLocationsDatasetsImport(name, opts)



Imports data into a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ImportDataRequest': new VertexAiApi.GoogleCloudAiplatformV1ImportDataRequest() // GoogleCloudAiplatformV1ImportDataRequest | 
};
apiInstance.aiplatformProjectsLocationsDatasetsImport(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the Dataset resource. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ImportDataRequest** | [**GoogleCloudAiplatformV1ImportDataRequest**](GoogleCloudAiplatformV1ImportDataRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsList

> GoogleCloudAiplatformV1ListDatasetsResponse aiplatformProjectsLocationsDatasetsList(parent, opts)



Lists Datasets in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the Dataset's parent resource. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `display_name`: supports = and != * `metadata_schema_uri`: supports = and != * `labels` supports general map functions that is: * `labels.key=value` - key:value equality * `labels.key:* or labels:key - key existence * A key including a space must be quoted. `labels.\"a key\"`. Some examples: * `displayName=\"myDisplayName\"` * `labels.myKey=\"myValue\"`
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `display_name` * `create_time` * `update_time`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsDatasetsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the Dataset&#39;s parent resource. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;display_name&#x60;: supports &#x3D; and !&#x3D; * &#x60;metadata_schema_uri&#x60;: supports &#x3D; and !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListDatasetsResponse**](GoogleCloudAiplatformV1ListDatasetsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsSavedQueriesList

> GoogleCloudAiplatformV1ListSavedQueriesResponse aiplatformProjectsLocationsDatasetsSavedQueriesList(parent, opts)



Lists SavedQueries in a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Dataset to list SavedQueries from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsDatasetsSavedQueriesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Dataset to list SavedQueries from. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListSavedQueriesResponse**](GoogleCloudAiplatformV1ListSavedQueriesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDatasetsSearchDataItems

> GoogleCloudAiplatformV1SearchDataItemsResponse aiplatformProjectsLocationsDatasetsSearchDataItems(dataset, opts)



Searches DataItems in a Dataset.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let dataset = "dataset_example"; // String | Required. The resource name of the Dataset from which to search DataItems. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'annotationFilters': ["null"], // [String] | An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned. * `annotation_spec_id` - for = or !=. Must specify `saved_query_id=` - saved query id that annotations should belong to.
  'annotationsFilter': "annotationsFilter_example", // String | An expression for filtering the Annotations that will be returned per DataItem. * `annotation_spec_id` - for = or !=.
  'annotationsLimit': 56, // Number | If set, only up to this many of Annotations will be returned per DataItemView. The maximum value is 1000. If not set, the maximum value will be used.
  'dataItemFilter': "dataItemFilter_example", // String | An expression for filtering the DataItem that will be returned. * `data_item_id` - for = or !=. * `labeled` - for = or !=. * `has_annotation(ANNOTATION_SPEC_ID)` - true only for DataItem that have at least one annotation with annotation_spec_id = `ANNOTATION_SPEC_ID` in the context of SavedQuery or DataLabelingJob. For example: * `data_item=1` * `has_annotation(5)`
  'dataLabelingJob': "dataLabelingJob_example", // String | The resource name of a DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}` If this field is set, all of the search will be done in the context of this DataLabelingJob.
  'fieldMask': "fieldMask_example", // String | Mask specifying which fields of DataItemView to read.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'orderByAnnotationOrderBy': "orderByAnnotationOrderBy_example", // String | A comma-separated list of annotation fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Must also specify saved_query.
  'orderByAnnotationSavedQuery': "orderByAnnotationSavedQuery_example", // String | Required. Saved query of the Annotation. Only Annotations belong to this saved query will be considered for ordering.
  'orderByDataItem': "orderByDataItem_example", // String | A comma-separated list of data item fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'pageSize': 56, // Number | Requested page size. Server may return fewer results than requested. Default and maximum page size is 100.
  'pageToken': "pageToken_example", // String | A token identifying a page of results for the server to return Typically obtained via SearchDataItemsResponse.next_page_token of the previous DatasetService.SearchDataItems call.
  'savedQuery': "savedQuery_example" // String | The resource name of a SavedQuery(annotation set in UI). Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}` All of the search will be done in the context of this SavedQuery.
};
apiInstance.aiplatformProjectsLocationsDatasetsSearchDataItems(dataset, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **String**| Required. The resource name of the Dataset from which to search DataItems. Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **annotationFilters** | [**[String]**](String.md)| An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned. * &#x60;annotation_spec_id&#x60; - for &#x3D; or !&#x3D;. Must specify &#x60;saved_query_id&#x3D;&#x60; - saved query id that annotations should belong to. | [optional] 
 **annotationsFilter** | **String**| An expression for filtering the Annotations that will be returned per DataItem. * &#x60;annotation_spec_id&#x60; - for &#x3D; or !&#x3D;. | [optional] 
 **annotationsLimit** | **Number**| If set, only up to this many of Annotations will be returned per DataItemView. The maximum value is 1000. If not set, the maximum value will be used. | [optional] 
 **dataItemFilter** | **String**| An expression for filtering the DataItem that will be returned. * &#x60;data_item_id&#x60; - for &#x3D; or !&#x3D;. * &#x60;labeled&#x60; - for &#x3D; or !&#x3D;. * &#x60;has_annotation(ANNOTATION_SPEC_ID)&#x60; - true only for DataItem that have at least one annotation with annotation_spec_id &#x3D; &#x60;ANNOTATION_SPEC_ID&#x60; in the context of SavedQuery or DataLabelingJob. For example: * &#x60;data_item&#x3D;1&#x60; * &#x60;has_annotation(5)&#x60; | [optional] 
 **dataLabelingJob** | **String**| The resource name of a DataLabelingJob. Format: &#x60;projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}&#x60; If this field is set, all of the search will be done in the context of this DataLabelingJob. | [optional] 
 **fieldMask** | **String**| Mask specifying which fields of DataItemView to read. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **orderByAnnotationOrderBy** | **String**| A comma-separated list of annotation fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Must also specify saved_query. | [optional] 
 **orderByAnnotationSavedQuery** | **String**| Required. Saved query of the Annotation. Only Annotations belong to this saved query will be considered for ordering. | [optional] 
 **orderByDataItem** | **String**| A comma-separated list of data item fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **pageSize** | **Number**| Requested page size. Server may return fewer results than requested. Default and maximum page size is 100. | [optional] 
 **pageToken** | **String**| A token identifying a page of results for the server to return Typically obtained via SearchDataItemsResponse.next_page_token of the previous DatasetService.SearchDataItems call. | [optional] 
 **savedQuery** | **String**| The resource name of a SavedQuery(annotation set in UI). Format: &#x60;projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}&#x60; All of the search will be done in the context of this SavedQuery. | [optional] 

### Return type

[**GoogleCloudAiplatformV1SearchDataItemsResponse**](GoogleCloudAiplatformV1SearchDataItemsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDeploymentResourcePoolsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsDeploymentResourcePoolsCreate(parent, opts)



Create a DeploymentResourcePool.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent location resource where this DeploymentResourcePool will be created. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1CreateDeploymentResourcePoolRequest': new VertexAiApi.GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest() // GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest | 
};
apiInstance.aiplatformProjectsLocationsDeploymentResourcePoolsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent location resource where this DeploymentResourcePool will be created. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1CreateDeploymentResourcePoolRequest** | [**GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest**](GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsDeploymentResourcePoolsList

> GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse aiplatformProjectsLocationsDeploymentResourcePoolsList(parent, opts)



List DeploymentResourcePools in a location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent Location which owns this collection of DeploymentResourcePools. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of DeploymentResourcePools to return. The service may return fewer than this value.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListDeploymentResourcePools` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDeploymentResourcePools` must match the call that provided the page token.
};
apiInstance.aiplatformProjectsLocationsDeploymentResourcePoolsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent Location which owns this collection of DeploymentResourcePools. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of DeploymentResourcePools to return. The service may return fewer than this value. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListDeploymentResourcePools&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListDeploymentResourcePools&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse**](GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsDeploymentResourcePoolsQueryDeployedModels

> GoogleCloudAiplatformV1QueryDeployedModelsResponse aiplatformProjectsLocationsDeploymentResourcePoolsQueryDeployedModels(deploymentResourcePool, opts)



List DeployedModels that have been deployed on this DeploymentResourcePool.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let deploymentResourcePool = "deploymentResourcePool_example"; // String | Required. The name of the target DeploymentResourcePool to query. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of DeployedModels to return. The service may return fewer than this value.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `QueryDeployedModels` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `QueryDeployedModels` must match the call that provided the page token.
};
apiInstance.aiplatformProjectsLocationsDeploymentResourcePoolsQueryDeployedModels(deploymentResourcePool, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploymentResourcePool** | **String**| Required. The name of the target DeploymentResourcePool to query. Format: &#x60;projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of DeployedModels to return. The service may return fewer than this value. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;QueryDeployedModels&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;QueryDeployedModels&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudAiplatformV1QueryDeployedModelsResponse**](GoogleCloudAiplatformV1QueryDeployedModelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsEndpointsCreate(parent, opts)



Creates an Endpoint.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the Endpoint in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'endpointId': "endpointId_example", // String | Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.
  'googleCloudAiplatformV1Endpoint': new VertexAiApi.GoogleCloudAiplatformV1Endpoint() // GoogleCloudAiplatformV1Endpoint | 
};
apiInstance.aiplatformProjectsLocationsEndpointsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the Endpoint in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **endpointId** | **String**| Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are &#x60;[a-z0-9-]&#x60;. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are &#x60;[0-9]&#x60; with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as &#x60;?endpoint_id&#x3D;12345&#x60;. This is the fallback for fields that are not included in either the URI or the body. | [optional] 
 **googleCloudAiplatformV1Endpoint** | [**GoogleCloudAiplatformV1Endpoint**](GoogleCloudAiplatformV1Endpoint.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsDeployModel

> GoogleLongrunningOperation aiplatformProjectsLocationsEndpointsDeployModel(endpoint, opts)



Deploys a Model into this Endpoint, creating a DeployedModel within it.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint resource into which to deploy a Model. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DeployModelRequest': new VertexAiApi.GoogleCloudAiplatformV1DeployModelRequest() // GoogleCloudAiplatformV1DeployModelRequest | 
};
apiInstance.aiplatformProjectsLocationsEndpointsDeployModel(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint resource into which to deploy a Model. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DeployModelRequest** | [**GoogleCloudAiplatformV1DeployModelRequest**](GoogleCloudAiplatformV1DeployModelRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsDirectPredict

> GoogleCloudAiplatformV1DirectPredictResponse aiplatformProjectsLocationsEndpointsDirectPredict(endpoint, opts)



Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DirectPredictRequest': new VertexAiApi.GoogleCloudAiplatformV1DirectPredictRequest() // GoogleCloudAiplatformV1DirectPredictRequest | 
};
apiInstance.aiplatformProjectsLocationsEndpointsDirectPredict(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DirectPredictRequest** | [**GoogleCloudAiplatformV1DirectPredictRequest**](GoogleCloudAiplatformV1DirectPredictRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1DirectPredictResponse**](GoogleCloudAiplatformV1DirectPredictResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsDirectRawPredict

> GoogleCloudAiplatformV1DirectRawPredictResponse aiplatformProjectsLocationsEndpointsDirectRawPredict(endpoint, opts)



Perform an unary online prediction request to a gRPC model server for custom containers.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DirectRawPredictRequest': new VertexAiApi.GoogleCloudAiplatformV1DirectRawPredictRequest() // GoogleCloudAiplatformV1DirectRawPredictRequest | 
};
apiInstance.aiplatformProjectsLocationsEndpointsDirectRawPredict(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DirectRawPredictRequest** | [**GoogleCloudAiplatformV1DirectRawPredictRequest**](GoogleCloudAiplatformV1DirectRawPredictRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1DirectRawPredictResponse**](GoogleCloudAiplatformV1DirectRawPredictResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsExplain

> GoogleCloudAiplatformV1ExplainResponse aiplatformProjectsLocationsEndpointsExplain(endpoint, opts)



Perform an online explanation. If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the explanation. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ExplainRequest': new VertexAiApi.GoogleCloudAiplatformV1ExplainRequest() // GoogleCloudAiplatformV1ExplainRequest | 
};
apiInstance.aiplatformProjectsLocationsEndpointsExplain(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the explanation. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ExplainRequest** | [**GoogleCloudAiplatformV1ExplainRequest**](GoogleCloudAiplatformV1ExplainRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ExplainResponse**](GoogleCloudAiplatformV1ExplainResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsList

> GoogleCloudAiplatformV1ListEndpointsResponse aiplatformProjectsLocationsEndpointsList(parent, opts)



Lists Endpoints in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location from which to list the Endpoints. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `endpoint` supports = and !=. `endpoint` represents the Endpoint ID, i.e. the last segment of the Endpoint's resource name. * `display_name` supports = and, != * `labels` supports general map functions that is: * `labels.key=value` - key:value equality * `labels.key:* or labels:key - key existence * A key including a space must be quoted. `labels.\"a key\"`. Some examples: * `endpoint=1` * `displayName=\"myDisplayName\"` * `labels.myKey=\"myValue\"`
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `display_name` * `create_time` * `update_time` Example: `display_name, create_time desc`.
  'pageSize': 56, // Number | Optional. The standard list page size.
  'pageToken': "pageToken_example", // String | Optional. The standard list page token. Typically obtained via ListEndpointsResponse.next_page_token of the previous EndpointService.ListEndpoints call.
  'readMask': "readMask_example" // String | Optional. Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsEndpointsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location from which to list the Endpoints. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;endpoint&#x60; supports &#x3D; and !&#x3D;. &#x60;endpoint&#x60; represents the Endpoint ID, i.e. the last segment of the Endpoint&#39;s resource name. * &#x60;display_name&#x60; supports &#x3D; and, !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;endpoint&#x3D;1&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;. | [optional] 
 **pageSize** | **Number**| Optional. The standard list page size. | [optional] 
 **pageToken** | **String**| Optional. The standard list page token. Typically obtained via ListEndpointsResponse.next_page_token of the previous EndpointService.ListEndpoints call. | [optional] 
 **readMask** | **String**| Optional. Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListEndpointsResponse**](GoogleCloudAiplatformV1ListEndpointsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsMutateDeployedModel

> GoogleLongrunningOperation aiplatformProjectsLocationsEndpointsMutateDeployedModel(endpoint, opts)



Updates an existing deployed model. Updatable fields include &#x60;min_replica_count&#x60;, &#x60;max_replica_count&#x60;, &#x60;autoscaling_metric_specs&#x60;, &#x60;disable_container_logging&#x60; (v1 only), and &#x60;enable_container_logging&#x60; (v1beta1 only).

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1MutateDeployedModelRequest': new VertexAiApi.GoogleCloudAiplatformV1MutateDeployedModelRequest() // GoogleCloudAiplatformV1MutateDeployedModelRequest | 
};
apiInstance.aiplatformProjectsLocationsEndpointsMutateDeployedModel(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1MutateDeployedModelRequest** | [**GoogleCloudAiplatformV1MutateDeployedModelRequest**](GoogleCloudAiplatformV1MutateDeployedModelRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsEndpointsUndeployModel

> GoogleLongrunningOperation aiplatformProjectsLocationsEndpointsUndeployModel(endpoint, opts)



Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it&#39;s using.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint resource from which to undeploy a Model. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1UndeployModelRequest': new VertexAiApi.GoogleCloudAiplatformV1UndeployModelRequest() // GoogleCloudAiplatformV1UndeployModelRequest | 
};
apiInstance.aiplatformProjectsLocationsEndpointsUndeployModel(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint resource from which to undeploy a Model. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1UndeployModelRequest** | [**GoogleCloudAiplatformV1UndeployModelRequest**](GoogleCloudAiplatformV1UndeployModelRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureGroupsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeatureGroupsCreate(parent, opts)



Creates a new FeatureGroup in a given project and location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}'`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'featureGroupId': "featureGroupId_example", // String | Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.
  'googleCloudAiplatformV1FeatureGroup': new VertexAiApi.GoogleCloudAiplatformV1FeatureGroup() // GoogleCloudAiplatformV1FeatureGroup | 
};
apiInstance.aiplatformProjectsLocationsFeatureGroupsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create FeatureGroups. Format: &#x60;projects/{project}/locations/{location}&#39;&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **featureGroupId** | **String**| Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within the project and location. | [optional] 
 **googleCloudAiplatformV1FeatureGroup** | [**GoogleCloudAiplatformV1FeatureGroup**](GoogleCloudAiplatformV1FeatureGroup.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureGroupsList

> GoogleCloudAiplatformV1ListFeatureGroupsResponse aiplatformProjectsLocationsFeatureGroupsList(parent, opts)



Lists FeatureGroups in a given project and location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the FeatureGroups that match the filter expression. The following fields are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality and key presence. Examples: * `create_time > \"2020-01-01\" OR update_time > \"2020-01-01\"` FeatureGroups created or updated after 2020-01-01. * `labels.env = \"prod\"` FeatureGroups with label \"env\" set to \"prod\".
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported Fields: * `create_time` * `update_time`
  'pageSize': 56, // Number | The maximum number of FeatureGroups to return. The service may return fewer than this value. If unspecified, at most 100 FeatureGroups will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous FeatureGroupAdminService.ListFeatureGroups call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureGroupAdminService.ListFeatureGroups must match the call that provided the page token.
};
apiInstance.aiplatformProjectsLocationsFeatureGroupsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list FeatureGroups. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the FeatureGroups that match the filter expression. The following fields are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality and key presence. Examples: * &#x60;create_time &gt; \&quot;2020-01-01\&quot; OR update_time &gt; \&quot;2020-01-01\&quot;&#x60; FeatureGroups created or updated after 2020-01-01. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; FeatureGroups with label \&quot;env\&quot; set to \&quot;prod\&quot;. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported Fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of FeatureGroups to return. The service may return fewer than this value. If unspecified, at most 100 FeatureGroups will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeatureGroupAdminService.ListFeatureGroups call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureGroupAdminService.ListFeatureGroups must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListFeatureGroupsResponse**](GoogleCloudAiplatformV1ListFeatureGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeatureOnlineStoresCreate(parent, opts)



Creates a new FeatureOnlineStore in a given project and location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'featureOnlineStoreId': "featureOnlineStoreId_example", // String | Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.
  'googleCloudAiplatformV1FeatureOnlineStore': new VertexAiApi.GoogleCloudAiplatformV1FeatureOnlineStore() // GoogleCloudAiplatformV1FeatureOnlineStore | 
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create FeatureOnlineStores. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **featureOnlineStoreId** | **String**| Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within the project and location. | [optional] 
 **googleCloudAiplatformV1FeatureOnlineStore** | [**GoogleCloudAiplatformV1FeatureOnlineStore**](GoogleCloudAiplatformV1FeatureOnlineStore.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsCreate(parent, opts)



Creates a new FeatureView in a given FeatureOnlineStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'featureViewId': "featureViewId_example", // String | Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.
  'runSyncImmediately': true, // Boolean | Immutable. If set to true, one on demand sync will be run immediately, regardless whether the FeatureView.sync_config is configured or not.
  'googleCloudAiplatformV1FeatureView': new VertexAiApi.GoogleCloudAiplatformV1FeatureView() // GoogleCloudAiplatformV1FeatureView | 
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **featureViewId** | **String**| Required. The ID to use for the FeatureView, which will become the final component of the FeatureView&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within a FeatureOnlineStore. | [optional] 
 **runSyncImmediately** | **Boolean**| Immutable. If set to true, one on demand sync will be run immediately, regardless whether the FeatureView.sync_config is configured or not. | [optional] 
 **googleCloudAiplatformV1FeatureView** | [**GoogleCloudAiplatformV1FeatureView**](GoogleCloudAiplatformV1FeatureView.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFeatureViewSyncsList

> GoogleCloudAiplatformV1ListFeatureViewSyncsResponse aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFeatureViewSyncsList(parent, opts)



Lists FeatureViewSyncs in a given FeatureView.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the FeatureViewSyncs that match the filter expression. The following filters are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. Examples: * `create_time > \\\"2020-01-31T15:30:00.000000Z\\\"` --> FeatureViewSyncs created after 2020-01-31T15:30:00.000000Z.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `create_time`
  'pageSize': 56, // Number | The maximum number of FeatureViewSyncs to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViewSyncs will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViewSyncs call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViewSyncs must match the call that provided the page token.
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFeatureViewSyncsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the FeatureViewSyncs that match the filter expression. The following filters are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. Examples: * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; FeatureViewSyncs created after 2020-01-31T15:30:00.000000Z. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;create_time&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of FeatureViewSyncs to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViewSyncs will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViewSyncs call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViewSyncs must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListFeatureViewSyncsResponse**](GoogleCloudAiplatformV1ListFeatureViewSyncsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFetchFeatureValues

> GoogleCloudAiplatformV1FetchFeatureValuesResponse aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFetchFeatureValues(featureView, opts)



Fetch feature values under a FeatureView.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let featureView = "featureView_example"; // String | Required. FeatureView resource format `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1FetchFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1FetchFeatureValuesRequest() // GoogleCloudAiplatformV1FetchFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsFetchFeatureValues(featureView, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featureView** | **String**| Required. FeatureView resource format &#x60;projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1FetchFeatureValuesRequest** | [**GoogleCloudAiplatformV1FetchFeatureValuesRequest**](GoogleCloudAiplatformV1FetchFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1FetchFeatureValuesResponse**](GoogleCloudAiplatformV1FetchFeatureValuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsList

> GoogleCloudAiplatformV1ListFeatureViewsResponse aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsList(parent, opts)



Lists FeatureViews in a given FeatureOnlineStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the FeatureViews that match the filter expression. The following filters are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality as well as key presence. Examples: * `create_time > \\\"2020-01-31T15:30:00.000000Z\\\" OR update_time > \\\"2020-01-31T15:30:00.000000Z\\\"` --> FeatureViews created or updated after 2020-01-31T15:30:00.000000Z. * `labels.active = yes AND labels.env = prod` --> FeatureViews having both (active: yes) and (env: prod) labels. * `labels.env: *` --> Any FeatureView which has a label with 'env' as the key.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `feature_view_id` * `create_time` * `update_time`
  'pageSize': 56, // Number | The maximum number of FeatureViews to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViews will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViews call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViews must match the call that provided the page token.
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the FeatureViews that match the filter expression. The following filters are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. Examples: * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot; OR update_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; FeatureViews created or updated after 2020-01-31T15:30:00.000000Z. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; FeatureViews having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any FeatureView which has a label with &#39;env&#39; as the key. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;feature_view_id&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of FeatureViews to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViews will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViews call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViews must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListFeatureViewsResponse**](GoogleCloudAiplatformV1ListFeatureViewsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSearchNearestEntities

> GoogleCloudAiplatformV1SearchNearestEntitiesResponse aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSearchNearestEntities(featureView, opts)



Search the nearest entities under a FeatureView. Search only works for indexable feature view; if a feature view isn&#39;t indexable, returns Invalid argument response.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let featureView = "featureView_example"; // String | Required. FeatureView resource format `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1SearchNearestEntitiesRequest': new VertexAiApi.GoogleCloudAiplatformV1SearchNearestEntitiesRequest() // GoogleCloudAiplatformV1SearchNearestEntitiesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSearchNearestEntities(featureView, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featureView** | **String**| Required. FeatureView resource format &#x60;projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1SearchNearestEntitiesRequest** | [**GoogleCloudAiplatformV1SearchNearestEntitiesRequest**](GoogleCloudAiplatformV1SearchNearestEntitiesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1SearchNearestEntitiesResponse**](GoogleCloudAiplatformV1SearchNearestEntitiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSync

> GoogleCloudAiplatformV1SyncFeatureViewResponse aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSync(featureView, opts)



Triggers on-demand sync for the FeatureView.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let featureView = "featureView_example"; // String | Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresFeatureViewsSync(featureView, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featureView** | **String**| Required. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1SyncFeatureViewResponse**](GoogleCloudAiplatformV1SyncFeatureViewResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresList

> GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse aiplatformProjectsLocationsFeatureOnlineStoresList(parent, opts)



Lists FeatureOnlineStores in a given project and location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the FeatureOnlineStores that match the filter expression. The following fields are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality and key presence. Examples: * `create_time > \"2020-01-01\" OR update_time > \"2020-01-01\"` FeatureOnlineStores created or updated after 2020-01-01. * `labels.env = \"prod\"` FeatureOnlineStores with label \"env\" set to \"prod\".
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported Fields: * `create_time` * `update_time`
  'pageSize': 56, // Number | The maximum number of FeatureOnlineStores to return. The service may return fewer than this value. If unspecified, at most 100 FeatureOnlineStores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureOnlineStores call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureOnlineStores must match the call that provided the page token.
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list FeatureOnlineStores. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the FeatureOnlineStores that match the filter expression. The following fields are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality and key presence. Examples: * &#x60;create_time &gt; \&quot;2020-01-01\&quot; OR update_time &gt; \&quot;2020-01-01\&quot;&#x60; FeatureOnlineStores created or updated after 2020-01-01. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; FeatureOnlineStores with label \&quot;env\&quot; set to \&quot;prod\&quot;. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported Fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of FeatureOnlineStores to return. The service may return fewer than this value. If unspecified, at most 100 FeatureOnlineStores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureOnlineStores call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureOnlineStores must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse**](GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeatureOnlineStoresOperationsListWait

> GoogleLongrunningListOperationsResponse aiplatformProjectsLocationsFeatureOnlineStoresOperationsListWait(name, opts)



Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation's parent resource.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example" // String | The standard list page token.
};
apiInstance.aiplatformProjectsLocationsFeatureOnlineStoresOperationsListWait(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of the operation&#39;s parent resource. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 

### Return type

[**GoogleLongrunningListOperationsResponse**](GoogleLongrunningListOperationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresBatchReadFeatureValues

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresBatchReadFeatureValues(featurestore, opts)



Batch reads Feature values from a Featurestore. This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance&#39;s read timestamp.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let featurestore = "featurestore_example"; // String | Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchReadFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1BatchReadFeatureValuesRequest() // GoogleCloudAiplatformV1BatchReadFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresBatchReadFeatureValues(featurestore, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore** | **String**| Required. The resource name of the Featurestore from which to query Feature values. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchReadFeatureValuesRequest** | [**GoogleCloudAiplatformV1BatchReadFeatureValuesRequest**](GoogleCloudAiplatformV1BatchReadFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresCreate(parent, opts)



Creates a new Featurestore in a given project and location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create Featurestores. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'featurestoreId': "featurestoreId_example", // String | Required. The ID to use for this Featurestore, which will become the final component of the Featurestore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.
  'googleCloudAiplatformV1Featurestore': new VertexAiApi.GoogleCloudAiplatformV1Featurestore() // GoogleCloudAiplatformV1Featurestore | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create Featurestores. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **featurestoreId** | **String**| Required. The ID to use for this Featurestore, which will become the final component of the Featurestore&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within the project and location. | [optional] 
 **googleCloudAiplatformV1Featurestore** | [**GoogleCloudAiplatformV1Featurestore**](GoogleCloudAiplatformV1Featurestore.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresEntityTypesCreate(parent, opts)



Creates a new EntityType in a given Featurestore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Featurestore to create EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'entityTypeId': "entityTypeId_example", // String | Required. The ID to use for the EntityType, which will become the final component of the EntityType's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a featurestore.
  'googleCloudAiplatformV1EntityType': new VertexAiApi.GoogleCloudAiplatformV1EntityType() // GoogleCloudAiplatformV1EntityType | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Featurestore to create EntityTypes. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **entityTypeId** | **String**| Required. The ID to use for the EntityType, which will become the final component of the EntityType&#39;s resource name. This value may be up to 60 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within a featurestore. | [optional] 
 **googleCloudAiplatformV1EntityType** | [**GoogleCloudAiplatformV1EntityType**](GoogleCloudAiplatformV1EntityType.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesDeleteFeatureValues

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresEntityTypesDeleteFeatureValues(entityType, opts)



Delete Feature values from Featurestore. The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done. If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let entityType = "entityType_example"; // String | Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DeleteFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1DeleteFeatureValuesRequest() // GoogleCloudAiplatformV1DeleteFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesDeleteFeatureValues(entityType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityType** | **String**| Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DeleteFeatureValuesRequest** | [**GoogleCloudAiplatformV1DeleteFeatureValuesRequest**](GoogleCloudAiplatformV1DeleteFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesExportFeatureValues

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresEntityTypesExportFeatureValues(entityType, opts)



Exports Feature values from all the entities of a target EntityType.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let entityType = "entityType_example"; // String | Required. The resource name of the EntityType from which to export Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ExportFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1ExportFeatureValuesRequest() // GoogleCloudAiplatformV1ExportFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesExportFeatureValues(entityType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityType** | **String**| Required. The resource name of the EntityType from which to export Feature values. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ExportFeatureValuesRequest** | [**GoogleCloudAiplatformV1ExportFeatureValuesRequest**](GoogleCloudAiplatformV1ExportFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesBatchCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesBatchCreate(parent, opts)



Creates a batch of Features in a given EntityType.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the EntityType to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchCreateFeaturesRequest': new VertexAiApi.GoogleCloudAiplatformV1BatchCreateFeaturesRequest() // GoogleCloudAiplatformV1BatchCreateFeaturesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesBatchCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the EntityType to create the batch of Features under. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchCreateFeaturesRequest** | [**GoogleCloudAiplatformV1BatchCreateFeaturesRequest**](GoogleCloudAiplatformV1BatchCreateFeaturesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesCreate(parent, opts)



Creates a new Feature in a given EntityType.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'featureId': "featureId_example", // String | Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.
  'googleCloudAiplatformV1Feature': new VertexAiApi.GoogleCloudAiplatformV1Feature() // GoogleCloudAiplatformV1Feature | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; Format for feature_group as parent: &#x60;projects/{project}/locations/{location}/featureGroups/{feature_group}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **featureId** | **String**| Required. The ID to use for the Feature, which will become the final component of the Feature&#39;s resource name. This value may be up to 128 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup. | [optional] 
 **googleCloudAiplatformV1Feature** | [**GoogleCloudAiplatformV1Feature**](GoogleCloudAiplatformV1Feature.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesList

> GoogleCloudAiplatformV1ListFeaturesResponse aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesList(parent, opts)



Lists Features in a given EntityType.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the Features that match the filter expression. The following filters are supported: * `value_type`: Supports = and != comparisons. * `create_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format. * `update_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality as well as key presence. Examples: * `value_type = DOUBLE` --> Features whose type is DOUBLE. * `create_time > \\\"2020-01-31T15:30:00.000000Z\\\" OR update_time > \\\"2020-01-31T15:30:00.000000Z\\\"` --> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. * `labels.active = yes AND labels.env = prod` --> Features having both (active: yes) and (env: prod) labels. * `labels.env: *` --> Any Feature which has a label with 'env' as the key.
  'latestStatsCount': 56, // Number | Only applicable for Vertex AI Feature Store (Legacy). If set, return the most recent ListFeaturesRequest.latest_stats_count of stats for each Feature in response. Valid value is [0, 10]. If number of stats exists < ListFeaturesRequest.latest_stats_count, return all existing stats.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `feature_id` * `value_type` (Not supported for FeatureRegistry Feature) * `create_time` * `update_time`
  'pageSize': 56, // Number | The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 1000 Features will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous FeaturestoreService.ListFeatures call or FeatureRegistryService.ListFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListFeatures or FeatureRegistryService.ListFeatures must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesFeaturesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list Features. Format for entity_type as parent: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; Format for feature_group as parent: &#x60;projects/{project}/locations/{location}/featureGroups/{feature_group}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the Features that match the filter expression. The following filters are supported: * &#x60;value_type&#x60;: Supports &#x3D; and !&#x3D; comparisons. * &#x60;create_time&#x60;: Supports &#x3D;, !&#x3D;, &lt;, &gt;, &gt;&#x3D;, and &lt;&#x3D; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x3D;, !&#x3D;, &lt;, &gt;, &gt;&#x3D;, and &lt;&#x3D; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. Examples: * &#x60;value_type &#x3D; DOUBLE&#x60; --&gt; Features whose type is DOUBLE. * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot; OR update_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; Features having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any Feature which has a label with &#39;env&#39; as the key. | [optional] 
 **latestStatsCount** | **Number**| Only applicable for Vertex AI Feature Store (Legacy). If set, return the most recent ListFeaturesRequest.latest_stats_count of stats for each Feature in response. Valid value is [0, 10]. If number of stats exists &lt; ListFeaturesRequest.latest_stats_count, return all existing stats. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;feature_id&#x60; * &#x60;value_type&#x60; (Not supported for FeatureRegistry Feature) * &#x60;create_time&#x60; * &#x60;update_time&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 1000 Features will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeaturestoreService.ListFeatures call or FeatureRegistryService.ListFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListFeatures or FeatureRegistryService.ListFeatures must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListFeaturesResponse**](GoogleCloudAiplatformV1ListFeaturesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesImportFeatureValues

> GoogleLongrunningOperation aiplatformProjectsLocationsFeaturestoresEntityTypesImportFeatureValues(entityType, opts)



Imports Feature values into the Featurestore from a source storage. The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done. If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done. There are also scenarios where the caller can cause inconsistency. - Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let entityType = "entityType_example"; // String | Required. The resource name of the EntityType grouping the Features for which values are being imported. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ImportFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1ImportFeatureValuesRequest() // GoogleCloudAiplatformV1ImportFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesImportFeatureValues(entityType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityType** | **String**| Required. The resource name of the EntityType grouping the Features for which values are being imported. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ImportFeatureValuesRequest** | [**GoogleCloudAiplatformV1ImportFeatureValuesRequest**](GoogleCloudAiplatformV1ImportFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesList

> GoogleCloudAiplatformV1ListEntityTypesResponse aiplatformProjectsLocationsFeaturestoresEntityTypesList(parent, opts)



Lists EntityTypes in a given Featurestore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the EntityTypes that match the filter expression. The following filters are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality as well as key presence. Examples: * `create_time > \\\"2020-01-31T15:30:00.000000Z\\\" OR update_time > \\\"2020-01-31T15:30:00.000000Z\\\"` --> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. * `labels.active = yes AND labels.env = prod` --> EntityTypes having both (active: yes) and (env: prod) labels. * `labels.env: *` --> Any EntityType which has a label with 'env' as the key.
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `entity_type_id` * `create_time` * `update_time`
  'pageSize': 56, // Number | The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous FeaturestoreService.ListEntityTypes call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListEntityTypes must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Featurestore to list EntityTypes. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the EntityTypes that match the filter expression. The following filters are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;&lt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. Examples: * &#x60;create_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot; OR update_time &gt; \\\&quot;2020-01-31T15:30:00.000000Z\\\&quot;&#x60; --&gt; EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; EntityTypes having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any EntityType which has a label with &#39;env&#39; as the key. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;entity_type_id&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeaturestoreService.ListEntityTypes call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListEntityTypes must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListEntityTypesResponse**](GoogleCloudAiplatformV1ListEntityTypesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesReadFeatureValues

> GoogleCloudAiplatformV1ReadFeatureValuesResponse aiplatformProjectsLocationsFeaturestoresEntityTypesReadFeatureValues(entityType, opts)



Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let entityType = "entityType_example"; // String | Required. The resource name of the EntityType for the entity being read. Value format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ReadFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1ReadFeatureValuesRequest() // GoogleCloudAiplatformV1ReadFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesReadFeatureValues(entityType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityType** | **String**| Required. The resource name of the EntityType for the entity being read. Value format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be &#x60;user&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ReadFeatureValuesRequest** | [**GoogleCloudAiplatformV1ReadFeatureValuesRequest**](GoogleCloudAiplatformV1ReadFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadFeatureValuesResponse**](GoogleCloudAiplatformV1ReadFeatureValuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesStreamingReadFeatureValues

> GoogleCloudAiplatformV1ReadFeatureValuesResponse aiplatformProjectsLocationsFeaturestoresEntityTypesStreamingReadFeatureValues(entityType, opts)



Reads Feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let entityType = "entityType_example"; // String | Required. The resource name of the entities' type. Value format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1StreamingReadFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest() // GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesStreamingReadFeatureValues(entityType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityType** | **String**| Required. The resource name of the entities&#39; type. Value format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be &#x60;user&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1StreamingReadFeatureValuesRequest** | [**GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest**](GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadFeatureValuesResponse**](GoogleCloudAiplatformV1ReadFeatureValuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresEntityTypesWriteFeatureValues

> Object aiplatformProjectsLocationsFeaturestoresEntityTypesWriteFeatureValues(entityType, opts)



Writes Feature values of one or more entities of an EntityType. The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let entityType = "entityType_example"; // String | Required. The resource name of the EntityType for the entities being written. Value format: `projects/{project}/locations/{location}/featurestores/ {featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1WriteFeatureValuesRequest': new VertexAiApi.GoogleCloudAiplatformV1WriteFeatureValuesRequest() // GoogleCloudAiplatformV1WriteFeatureValuesRequest | 
};
apiInstance.aiplatformProjectsLocationsFeaturestoresEntityTypesWriteFeatureValues(entityType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityType** | **String**| Required. The resource name of the EntityType for the entities being written. Value format: &#x60;projects/{project}/locations/{location}/featurestores/ {featurestore}/entityTypes/{entityType}&#x60;. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be &#x60;user&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1WriteFeatureValuesRequest** | [**GoogleCloudAiplatformV1WriteFeatureValuesRequest**](GoogleCloudAiplatformV1WriteFeatureValuesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresList

> GoogleCloudAiplatformV1ListFeaturestoresResponse aiplatformProjectsLocationsFeaturestoresList(parent, opts)



Lists Featurestores in a given project and location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list Featurestores. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the featurestores that match the filter expression. The following fields are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `online_serving_config.fixed_node_count`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. * `labels`: Supports key-value equality and key presence. Examples: * `create_time > \"2020-01-01\" OR update_time > \"2020-01-01\"` Featurestores created or updated after 2020-01-01. * `labels.env = \"prod\"` Featurestores with label \"env\" set to \"prod\".
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported Fields: * `create_time` * `update_time` * `online_serving_config.fixed_node_count`
  'pageSize': 56, // Number | The maximum number of Featurestores to return. The service may return fewer than this value. If unspecified, at most 100 Featurestores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
  'pageToken': "pageToken_example", // String | A page token, received from a previous FeaturestoreService.ListFeaturestores call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListFeaturestores must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsFeaturestoresList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list Featurestores. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the featurestores that match the filter expression. The following fields are supported: * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;online_serving_config.fixed_node_count&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. * &#x60;labels&#x60;: Supports key-value equality and key presence. Examples: * &#x60;create_time &gt; \&quot;2020-01-01\&quot; OR update_time &gt; \&quot;2020-01-01\&quot;&#x60; Featurestores created or updated after 2020-01-01. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; Featurestores with label \&quot;env\&quot; set to \&quot;prod\&quot;. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported Fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; * &#x60;online_serving_config.fixed_node_count&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of Featurestores to return. The service may return fewer than this value. If unspecified, at most 100 Featurestores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeaturestoreService.ListFeaturestores call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.ListFeaturestores must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListFeaturestoresResponse**](GoogleCloudAiplatformV1ListFeaturestoresResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsFeaturestoresSearchFeatures

> GoogleCloudAiplatformV1SearchFeaturesResponse aiplatformProjectsLocationsFeaturestoresSearchFeatures(location, opts)



Searches Features matching a query in a given project.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let location = "location_example"; // String | Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.
  'pageToken': "pageToken_example", // String | A page token, received from a previous FeaturestoreService.SearchFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.SearchFeatures, except `page_size`, must match the call that provided the page token.
  'query': "query_example" // String | Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `*` are treated as delimiters for tokens. `*` is treated as a wildcard that matches characters within a token. * Ignoring case. * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks (\"). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: * `feature_id` * `description` * `entity_type_id` Examples: * `feature_id: foo` --> Matches a Feature with ID containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`). * `feature_id: foo*feature` --> Matches a Feature with ID containing the substring `foo*feature` (eg. `foobarfeature`). * `feature_id: foo AND description: bar` --> Matches a Feature with ID containing the substring `foo` and description containing the substring `bar`. Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. * `feature_id`: Supports = comparisons. * `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes. * `entity_type_id`: Supports = comparisons. * `value_type`: Supports = and != comparisons. * `labels`: Supports key-value equality as well as key presence. * `featurestore_id`: Supports = comparisons. Examples: * `description = \"foo bar\"` --> Any Feature with description exactly equal to `foo bar` * `value_type = DOUBLE` --> Features whose type is DOUBLE. * `labels.active = yes AND labels.env = prod` --> Features having both (active: yes) and (env: prod) labels. * `labels.env: *` --> Any Feature which has a label with `env` as the key.
};
apiInstance.aiplatformProjectsLocationsFeaturestoresSearchFeatures(location, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **String**| Required. The resource name of the Location to search Features. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous FeaturestoreService.SearchFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.SearchFeatures, except &#x60;page_size&#x60;, must match the call that provided the page token. | [optional] 
 **query** | **String**| Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using &#x60;AND&#x60; to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature&#39;s FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric &#x60;[a-zA-Z0-9]&#x60;, underscore &#x60;_&#x60;, or asterisk &#x60;*&#x60; are treated as delimiters for tokens. &#x60;*&#x60; is treated as a wildcard that matches characters within a token. * Ignoring case. * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks (\&quot;). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: * &#x60;feature_id&#x60; * &#x60;description&#x60; * &#x60;entity_type_id&#x60; Examples: * &#x60;feature_id: foo&#x60; --&gt; Matches a Feature with ID containing the substring &#x60;foo&#x60; (eg. &#x60;foo&#x60;, &#x60;foofeature&#x60;, &#x60;barfoo&#x60;). * &#x60;feature_id: foo*feature&#x60; --&gt; Matches a Feature with ID containing the substring &#x60;foo*feature&#x60; (eg. &#x60;foobarfeature&#x60;). * &#x60;feature_id: foo AND description: bar&#x60; --&gt; Matches a Feature with ID containing the substring &#x60;foo&#x60; and description containing the substring &#x60;bar&#x60;. Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. * &#x60;feature_id&#x60;: Supports &#x3D; comparisons. * &#x60;description&#x60;: Supports &#x3D; comparisons. Multi-token filters should be enclosed in quotes. * &#x60;entity_type_id&#x60;: Supports &#x3D; comparisons. * &#x60;value_type&#x60;: Supports &#x3D; and !&#x3D; comparisons. * &#x60;labels&#x60;: Supports key-value equality as well as key presence. * &#x60;featurestore_id&#x60;: Supports &#x3D; comparisons. Examples: * &#x60;description &#x3D; \&quot;foo bar\&quot;&#x60; --&gt; Any Feature with description exactly equal to &#x60;foo bar&#x60; * &#x60;value_type &#x3D; DOUBLE&#x60; --&gt; Features whose type is DOUBLE. * &#x60;labels.active &#x3D; yes AND labels.env &#x3D; prod&#x60; --&gt; Features having both (active: yes) and (env: prod) labels. * &#x60;labels.env: *&#x60; --&gt; Any Feature which has a label with &#x60;env&#x60; as the key. | [optional] 

### Return type

[**GoogleCloudAiplatformV1SearchFeaturesResponse**](GoogleCloudAiplatformV1SearchFeaturesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsHyperparameterTuningJobsCreate

> GoogleCloudAiplatformV1HyperparameterTuningJob aiplatformProjectsLocationsHyperparameterTuningJobsCreate(parent, opts)



Creates a HyperparameterTuningJob

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the HyperparameterTuningJob in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1HyperparameterTuningJob': new VertexAiApi.GoogleCloudAiplatformV1HyperparameterTuningJob() // GoogleCloudAiplatformV1HyperparameterTuningJob | 
};
apiInstance.aiplatformProjectsLocationsHyperparameterTuningJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the HyperparameterTuningJob in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1HyperparameterTuningJob** | [**GoogleCloudAiplatformV1HyperparameterTuningJob**](GoogleCloudAiplatformV1HyperparameterTuningJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1HyperparameterTuningJob**](GoogleCloudAiplatformV1HyperparameterTuningJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsHyperparameterTuningJobsList

> GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse aiplatformProjectsLocationsHyperparameterTuningJobsList(parent, opts)



Lists HyperparameterTuningJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the HyperparameterTuningJobs from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `state` supports `=`, `!=` comparisons. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"JOB_STATE_SUCCEEDED\" AND display_name:\"my_job_*\"` * `state!=\"JOB_STATE_FAILED\" OR display_name=\"my_job\"` * `NOT display_name=\"my_job\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `labels.keyA=valueA` * `labels.keyB:*`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListHyperparameterTuningJobsResponse.next_page_token of the previous JobService.ListHyperparameterTuningJobs call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsHyperparameterTuningJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the HyperparameterTuningJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListHyperparameterTuningJobsResponse.next_page_token of the previous JobService.ListHyperparameterTuningJobs call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse**](GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsIndexEndpointsCreate(parent, opts)



Creates an IndexEndpoint.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the IndexEndpoint in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1IndexEndpoint': new VertexAiApi.GoogleCloudAiplatformV1IndexEndpoint() // GoogleCloudAiplatformV1IndexEndpoint | 
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the IndexEndpoint in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1IndexEndpoint** | [**GoogleCloudAiplatformV1IndexEndpoint**](GoogleCloudAiplatformV1IndexEndpoint.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsDeployIndex

> GoogleLongrunningOperation aiplatformProjectsLocationsIndexEndpointsDeployIndex(indexEndpoint, opts)



Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let indexEndpoint = "indexEndpoint_example"; // String | Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DeployIndexRequest': new VertexAiApi.GoogleCloudAiplatformV1DeployIndexRequest() // GoogleCloudAiplatformV1DeployIndexRequest | 
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsDeployIndex(indexEndpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexEndpoint** | **String**| Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DeployIndexRequest** | [**GoogleCloudAiplatformV1DeployIndexRequest**](GoogleCloudAiplatformV1DeployIndexRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsFindNeighbors

> GoogleCloudAiplatformV1FindNeighborsResponse aiplatformProjectsLocationsIndexEndpointsFindNeighbors(indexEndpoint, opts)



Finds the nearest neighbors of each vector within the request.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let indexEndpoint = "indexEndpoint_example"; // String | Required. The name of the index endpoint. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1FindNeighborsRequest': new VertexAiApi.GoogleCloudAiplatformV1FindNeighborsRequest() // GoogleCloudAiplatformV1FindNeighborsRequest | 
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsFindNeighbors(indexEndpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexEndpoint** | **String**| Required. The name of the index endpoint. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1FindNeighborsRequest** | [**GoogleCloudAiplatformV1FindNeighborsRequest**](GoogleCloudAiplatformV1FindNeighborsRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1FindNeighborsResponse**](GoogleCloudAiplatformV1FindNeighborsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsList

> GoogleCloudAiplatformV1ListIndexEndpointsResponse aiplatformProjectsLocationsIndexEndpointsList(parent, opts)



Lists IndexEndpoints in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location from which to list the IndexEndpoints. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `index_endpoint` supports = and !=. `index_endpoint` represents the IndexEndpoint ID, ie. the last segment of the IndexEndpoint's resourcename. * `display_name` supports =, != and regex() (uses [re2](https://github.com/google/re2/wiki/Syntax) syntax) * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* or labels:key - key existence A key including a space must be quoted. `labels.\"a key\"`. Some examples: * `index_endpoint=\"1\"` * `display_name=\"myDisplayName\"` * `regex(display_name, \"^A\") -> The display name starts with an A. * `labels.myKey=\"myValue\"`
  'pageSize': 56, // Number | Optional. The standard list page size.
  'pageToken': "pageToken_example", // String | Optional. The standard list page token. Typically obtained via ListIndexEndpointsResponse.next_page_token of the previous IndexEndpointService.ListIndexEndpoints call.
  'readMask': "readMask_example" // String | Optional. Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location from which to list the IndexEndpoints. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;index_endpoint&#x60; supports &#x3D; and !&#x3D;. &#x60;index_endpoint&#x60; represents the IndexEndpoint ID, ie. the last segment of the IndexEndpoint&#39;s resourcename. * &#x60;display_name&#x60; supports &#x3D;, !&#x3D; and regex() (uses [re2](https://github.com/google/re2/wiki/Syntax) syntax) * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* or labels:key - key existence A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;index_endpoint&#x3D;\&quot;1\&quot;&#x60; * &#x60;display_name&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;regex(display_name, \&quot;^A\&quot;) -&gt; The display name starts with an A. * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; | [optional] 
 **pageSize** | **Number**| Optional. The standard list page size. | [optional] 
 **pageToken** | **String**| Optional. The standard list page token. Typically obtained via ListIndexEndpointsResponse.next_page_token of the previous IndexEndpointService.ListIndexEndpoints call. | [optional] 
 **readMask** | **String**| Optional. Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListIndexEndpointsResponse**](GoogleCloudAiplatformV1ListIndexEndpointsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsMutateDeployedIndex

> GoogleLongrunningOperation aiplatformProjectsLocationsIndexEndpointsMutateDeployedIndex(indexEndpoint, opts)



Update an existing DeployedIndex under an IndexEndpoint.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let indexEndpoint = "indexEndpoint_example"; // String | Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1DeployedIndex': new VertexAiApi.GoogleCloudAiplatformV1DeployedIndex() // GoogleCloudAiplatformV1DeployedIndex | 
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsMutateDeployedIndex(indexEndpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexEndpoint** | **String**| Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1DeployedIndex** | [**GoogleCloudAiplatformV1DeployedIndex**](GoogleCloudAiplatformV1DeployedIndex.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsReadIndexDatapoints

> GoogleCloudAiplatformV1ReadIndexDatapointsResponse aiplatformProjectsLocationsIndexEndpointsReadIndexDatapoints(indexEndpoint, opts)



Reads the datapoints/vectors of the given IDs. A maximum of 1000 datapoints can be retrieved in a batch.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let indexEndpoint = "indexEndpoint_example"; // String | Required. The name of the index endpoint. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ReadIndexDatapointsRequest': new VertexAiApi.GoogleCloudAiplatformV1ReadIndexDatapointsRequest() // GoogleCloudAiplatformV1ReadIndexDatapointsRequest | 
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsReadIndexDatapoints(indexEndpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexEndpoint** | **String**| Required. The name of the index endpoint. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ReadIndexDatapointsRequest** | [**GoogleCloudAiplatformV1ReadIndexDatapointsRequest**](GoogleCloudAiplatformV1ReadIndexDatapointsRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadIndexDatapointsResponse**](GoogleCloudAiplatformV1ReadIndexDatapointsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexEndpointsUndeployIndex

> GoogleLongrunningOperation aiplatformProjectsLocationsIndexEndpointsUndeployIndex(indexEndpoint, opts)



Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it&#39;s using.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let indexEndpoint = "indexEndpoint_example"; // String | Required. The name of the IndexEndpoint resource from which to undeploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1UndeployIndexRequest': new VertexAiApi.GoogleCloudAiplatformV1UndeployIndexRequest() // GoogleCloudAiplatformV1UndeployIndexRequest | 
};
apiInstance.aiplatformProjectsLocationsIndexEndpointsUndeployIndex(indexEndpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexEndpoint** | **String**| Required. The name of the IndexEndpoint resource from which to undeploy an Index. Format: &#x60;projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1UndeployIndexRequest** | [**GoogleCloudAiplatformV1UndeployIndexRequest**](GoogleCloudAiplatformV1UndeployIndexRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexesCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsIndexesCreate(parent, opts)



Creates an Index.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the Index in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1Index': new VertexAiApi.GoogleCloudAiplatformV1Index() // GoogleCloudAiplatformV1Index | 
};
apiInstance.aiplatformProjectsLocationsIndexesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the Index in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1Index** | [**GoogleCloudAiplatformV1Index**](GoogleCloudAiplatformV1Index.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexesList

> GoogleCloudAiplatformV1ListIndexesResponse aiplatformProjectsLocationsIndexesList(parent, opts)



Lists Indexes in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location from which to list the Indexes. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListIndexesResponse.next_page_token of the previous IndexService.ListIndexes call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsIndexesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location from which to list the Indexes. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListIndexesResponse.next_page_token of the previous IndexService.ListIndexes call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListIndexesResponse**](GoogleCloudAiplatformV1ListIndexesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsIndexesRemoveDatapoints

> Object aiplatformProjectsLocationsIndexesRemoveDatapoints(index, opts)



Remove Datapoints from an Index.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let index = "index_example"; // String | Required. The name of the Index resource to be updated. Format: `projects/{project}/locations/{location}/indexes/{index}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1RemoveDatapointsRequest': new VertexAiApi.GoogleCloudAiplatformV1RemoveDatapointsRequest() // GoogleCloudAiplatformV1RemoveDatapointsRequest | 
};
apiInstance.aiplatformProjectsLocationsIndexesRemoveDatapoints(index, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **String**| Required. The name of the Index resource to be updated. Format: &#x60;projects/{project}/locations/{location}/indexes/{index}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1RemoveDatapointsRequest** | [**GoogleCloudAiplatformV1RemoveDatapointsRequest**](GoogleCloudAiplatformV1RemoveDatapointsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsIndexesUpsertDatapoints

> Object aiplatformProjectsLocationsIndexesUpsertDatapoints(index, opts)



Add/update Datapoints into an Index.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let index = "index_example"; // String | Required. The name of the Index resource to be updated. Format: `projects/{project}/locations/{location}/indexes/{index}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1UpsertDatapointsRequest': new VertexAiApi.GoogleCloudAiplatformV1UpsertDatapointsRequest() // GoogleCloudAiplatformV1UpsertDatapointsRequest | 
};
apiInstance.aiplatformProjectsLocationsIndexesUpsertDatapoints(index, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **String**| Required. The name of the Index resource to be updated. Format: &#x60;projects/{project}/locations/{location}/indexes/{index}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1UpsertDatapointsRequest** | [**GoogleCloudAiplatformV1UpsertDatapointsRequest**](GoogleCloudAiplatformV1UpsertDatapointsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsList

> GoogleCloudLocationListLocationsResponse aiplatformProjectsLocationsList(name, opts)



Lists information about the supported locations for this service.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | The resource that owns the locations collection, if applicable.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | A filter to narrow down results to a preferred subset. The filtering language accepts strings like `\"displayName=tokyo\"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
  'pageSize': 56, // Number | The maximum number of results to return. If not set, the service selects a default.
  'pageToken': "pageToken_example" // String | A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.
};
apiInstance.aiplatformProjectsLocationsList(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The resource that owns the locations collection, if applicable. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160). | [optional] 
 **pageSize** | **Number**| The maximum number of results to return. If not set, the service selects a default. | [optional] 
 **pageToken** | **String**| A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page. | [optional] 

### Return type

[**GoogleCloudLocationListLocationsResponse**](GoogleCloudLocationListLocationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresArtifactsCreate

> GoogleCloudAiplatformV1Artifact aiplatformProjectsLocationsMetadataStoresArtifactsCreate(parent, opts)



Creates an Artifact associated with a MetadataStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the MetadataStore where the Artifact should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'artifactId': "artifactId_example", // String | The {artifact} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` If not provided, the Artifact's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Artifacts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Artifact.)
  'googleCloudAiplatformV1Artifact': new VertexAiApi.GoogleCloudAiplatformV1Artifact() // GoogleCloudAiplatformV1Artifact | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresArtifactsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the MetadataStore where the Artifact should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **artifactId** | **String**| The {artifact} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}&#x60; If not provided, the Artifact&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all Artifacts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting Artifact.) | [optional] 
 **googleCloudAiplatformV1Artifact** | [**GoogleCloudAiplatformV1Artifact**](GoogleCloudAiplatformV1Artifact.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Artifact**](GoogleCloudAiplatformV1Artifact.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresArtifactsList

> GoogleCloudAiplatformV1ListArtifactsResponse aiplatformProjectsLocationsMetadataStoresArtifactsList(parent, opts)



Lists Artifacts in the MetadataStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The MetadataStore whose Artifacts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering**: For example: `display_name = \"test\"`. Supported fields include: `name`, `display_name`, `uri`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = \"2020-11-19T11:30:00-04:00\"` * **Metadata field**: To filter on metadata fields use traversal operation as follows: `metadata..`. For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata.\"field:1\".number_value = 10.0` * **Context based filtering**: To filter Artifacts based on the contexts to which they belong, use the function operator with the full resource name `in_context()`. For example: `in_context(\"projects//locations//metadataStores//contexts/\")` Each of the above supported filter types can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5. For example: `display_name = \"test\" AND metadata.field1.bool_value = true`.
  'orderBy': "orderBy_example", // String | How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \" desc\" suffix; for example: \"foo desc, bar\". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.
  'pageSize': 56, // Number | The maximum number of Artifacts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous MetadataService.ListArtifacts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
};
apiInstance.aiplatformProjectsLocationsMetadataStoresArtifactsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The MetadataStore whose Artifacts should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60;. Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;uri&#x60;, &#x60;state&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60; * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60;. For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60; In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; * **Context based filtering**: To filter Artifacts based on the contexts to which they belong, use the function operator with the full resource name &#x60;in_context()&#x60;. For example: &#x60;in_context(\&quot;projects//locations//metadataStores//contexts/\&quot;)&#x60; Each of the above supported filter types can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;. | [optional] 
 **orderBy** | **String**| How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \&quot; desc\&quot; suffix; for example: \&quot;foo desc, bar\&quot;. Subfields are specified with a &#x60;.&#x60; character, such as foo.bar. see https://google.aip.dev/132#ordering for more details. | [optional] 
 **pageSize** | **Number**| The maximum number of Artifacts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous MetadataService.ListArtifacts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListArtifactsResponse**](GoogleCloudAiplatformV1ListArtifactsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresArtifactsPurge

> GoogleLongrunningOperation aiplatformProjectsLocationsMetadataStoresArtifactsPurge(parent, opts)



Purges Artifacts.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The metadata store to purge Artifacts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1PurgeArtifactsRequest': new VertexAiApi.GoogleCloudAiplatformV1PurgeArtifactsRequest() // GoogleCloudAiplatformV1PurgeArtifactsRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresArtifactsPurge(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The metadata store to purge Artifacts from. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1PurgeArtifactsRequest** | [**GoogleCloudAiplatformV1PurgeArtifactsRequest**](GoogleCloudAiplatformV1PurgeArtifactsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresArtifactsQueryArtifactLineageSubgraph

> GoogleCloudAiplatformV1LineageSubgraph aiplatformProjectsLocationsMetadataStoresArtifactsQueryArtifactLineageSubgraph(artifact, opts)



Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let artifact = "artifact_example"; // String | Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the Lineage Subgraph. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering**: For example: `display_name = \"test\"` Supported fields include: `name`, `display_name`, `uri`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = \"2020-11-19T11:30:00-04:00\"` * **Metadata field**: To filter on metadata fields use traversal operation as follows: `metadata..`. For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata.\"field:1\".number_value = 10.0` Each of the above supported filter types can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5. For example: `display_name = \"test\" AND metadata.field1.bool_value = true`.
  'maxHops': 56 // Number | Specifies the size of the lineage graph in terms of number of hops from the specified artifact. Negative Value: INVALID_ARGUMENT error is returned 0: Only input artifact is returned. No value: Transitive closure is performed to return the complete graph.
};
apiInstance.aiplatformProjectsLocationsMetadataStoresArtifactsQueryArtifactLineageSubgraph(artifact, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact** | **String**| Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}&#x60; The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the Lineage Subgraph. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60; Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;uri&#x60;, &#x60;state&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60; * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60;. For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60; In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; Each of the above supported filter types can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;. | [optional] 
 **maxHops** | **Number**| Specifies the size of the lineage graph in terms of number of hops from the specified artifact. Negative Value: INVALID_ARGUMENT error is returned 0: Only input artifact is returned. No value: Transitive closure is performed to return the complete graph. | [optional] 

### Return type

[**GoogleCloudAiplatformV1LineageSubgraph**](GoogleCloudAiplatformV1LineageSubgraph.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsAddContextArtifactsAndExecutions

> Object aiplatformProjectsLocationsMetadataStoresContextsAddContextArtifactsAndExecutions(context, opts)



Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let context = "context_example"; // String | Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest': new VertexAiApi.GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest() // GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsAddContextArtifactsAndExecutions(context, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **String**| Required. The resource name of the Context that the Artifacts and Executions belong to. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest** | [**GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest**](GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsAddContextChildren

> Object aiplatformProjectsLocationsMetadataStoresContextsAddContextChildren(context, opts)



Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let context = "context_example"; // String | Required. The resource name of the parent Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1AddContextChildrenRequest': new VertexAiApi.GoogleCloudAiplatformV1AddContextChildrenRequest() // GoogleCloudAiplatformV1AddContextChildrenRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsAddContextChildren(context, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **String**| Required. The resource name of the parent Context. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1AddContextChildrenRequest** | [**GoogleCloudAiplatformV1AddContextChildrenRequest**](GoogleCloudAiplatformV1AddContextChildrenRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsCreate

> GoogleCloudAiplatformV1Context aiplatformProjectsLocationsMetadataStoresContextsCreate(parent, opts)



Creates a Context associated with a MetadataStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the MetadataStore where the Context should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'contextId': "contextId_example", // String | The {context} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`. If not provided, the Context's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Contexts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Context.)
  'googleCloudAiplatformV1Context': new VertexAiApi.GoogleCloudAiplatformV1Context() // GoogleCloudAiplatformV1Context | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the MetadataStore where the Context should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **contextId** | **String**| The {context} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60;. If not provided, the Context&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all Contexts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting Context.) | [optional] 
 **googleCloudAiplatformV1Context** | [**GoogleCloudAiplatformV1Context**](GoogleCloudAiplatformV1Context.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Context**](GoogleCloudAiplatformV1Context.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsList

> GoogleCloudAiplatformV1ListContextsResponse aiplatformProjectsLocationsMetadataStoresContextsList(parent, opts)



Lists Contexts on the MetadataStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The MetadataStore whose Contexts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Filter specifying the boolean condition for the Contexts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering**: For example: `display_name = \"test\"`. Supported fields include: `name`, `display_name`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = \"2020-11-19T11:30:00-04:00\"`. * **Metadata field**: To filter on metadata fields use traversal operation as follows: `metadata..`. For example: `metadata.field_1.number_value = 10.0`. In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata.\"field:1\".number_value = 10.0` * **Parent Child filtering**: To filter Contexts based on parent-child relationship use the HAS operator as follows: ``` parent_contexts: \"projects//locations//metadataStores//contexts/\" child_contexts: \"projects//locations//metadataStores//contexts/\" ``` Each of the above supported filters can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5. For example: `display_name = \"test\" AND metadata.field1.bool_value = true`.
  'orderBy': "orderBy_example", // String | How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \" desc\" suffix; for example: \"foo desc, bar\". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.
  'pageSize': 56, // Number | The maximum number of Contexts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous MetadataService.ListContexts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The MetadataStore whose Contexts should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Filter specifying the boolean condition for the Contexts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60;. Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60;. * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60;. For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60;. In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; * **Parent Child filtering**: To filter Contexts based on parent-child relationship use the HAS operator as follows: &#x60;&#x60;&#x60; parent_contexts: \&quot;projects//locations//metadataStores//contexts/\&quot; child_contexts: \&quot;projects//locations//metadataStores//contexts/\&quot; &#x60;&#x60;&#x60; Each of the above supported filters can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;. | [optional] 
 **orderBy** | **String**| How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \&quot; desc\&quot; suffix; for example: \&quot;foo desc, bar\&quot;. Subfields are specified with a &#x60;.&#x60; character, such as foo.bar. see https://google.aip.dev/132#ordering for more details. | [optional] 
 **pageSize** | **Number**| The maximum number of Contexts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous MetadataService.ListContexts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListContextsResponse**](GoogleCloudAiplatformV1ListContextsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsPurge

> GoogleLongrunningOperation aiplatformProjectsLocationsMetadataStoresContextsPurge(parent, opts)



Purges Contexts.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The metadata store to purge Contexts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1PurgeContextsRequest': new VertexAiApi.GoogleCloudAiplatformV1PurgeContextsRequest() // GoogleCloudAiplatformV1PurgeContextsRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsPurge(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The metadata store to purge Contexts from. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1PurgeContextsRequest** | [**GoogleCloudAiplatformV1PurgeContextsRequest**](GoogleCloudAiplatformV1PurgeContextsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsQueryContextLineageSubgraph

> GoogleCloudAiplatformV1LineageSubgraph aiplatformProjectsLocationsMetadataStoresContextsQueryContextLineageSubgraph(context, opts)



Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let context = "context_example"; // String | Required. The resource name of the Context whose Artifacts and Executions should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsQueryContextLineageSubgraph(context, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **String**| Required. The resource name of the Context whose Artifacts and Executions should be retrieved as a LineageSubgraph. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60; The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleCloudAiplatformV1LineageSubgraph**](GoogleCloudAiplatformV1LineageSubgraph.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresContextsRemoveContextChildren

> Object aiplatformProjectsLocationsMetadataStoresContextsRemoveContextChildren(context, opts)



Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let context = "context_example"; // String | Required. The resource name of the parent Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1RemoveContextChildrenRequest': new VertexAiApi.GoogleCloudAiplatformV1RemoveContextChildrenRequest() // GoogleCloudAiplatformV1RemoveContextChildrenRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresContextsRemoveContextChildren(context, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **String**| Required. The resource name of the parent Context. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1RemoveContextChildrenRequest** | [**GoogleCloudAiplatformV1RemoveContextChildrenRequest**](GoogleCloudAiplatformV1RemoveContextChildrenRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsMetadataStoresCreate(parent, opts)



Initializes a MetadataStore, including allocation of resources.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location where the MetadataStore should be created. Format: `projects/{project}/locations/{location}/`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'metadataStoreId': "metadataStoreId_example", // String | The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)
  'googleCloudAiplatformV1MetadataStore': new VertexAiApi.GoogleCloudAiplatformV1MetadataStore() // GoogleCloudAiplatformV1MetadataStore | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location where the MetadataStore should be created. Format: &#x60;projects/{project}/locations/{location}/&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **metadataStoreId** | **String**| The {metadatastore} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; If not provided, the MetadataStore&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting MetadataStore.) | [optional] 
 **googleCloudAiplatformV1MetadataStore** | [**GoogleCloudAiplatformV1MetadataStore**](GoogleCloudAiplatformV1MetadataStore.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresExecutionsAddExecutionEvents

> Object aiplatformProjectsLocationsMetadataStoresExecutionsAddExecutionEvents(execution, opts)



Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let execution = "execution_example"; // String | Required. The resource name of the Execution that the Events connect Artifacts with. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1AddExecutionEventsRequest': new VertexAiApi.GoogleCloudAiplatformV1AddExecutionEventsRequest() // GoogleCloudAiplatformV1AddExecutionEventsRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresExecutionsAddExecutionEvents(execution, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution** | **String**| Required. The resource name of the Execution that the Events connect Artifacts with. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1AddExecutionEventsRequest** | [**GoogleCloudAiplatformV1AddExecutionEventsRequest**](GoogleCloudAiplatformV1AddExecutionEventsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresExecutionsCreate

> GoogleCloudAiplatformV1Execution aiplatformProjectsLocationsMetadataStoresExecutionsCreate(parent, opts)



Creates an Execution associated with a MetadataStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the MetadataStore where the Execution should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'executionId': "executionId_example", // String | The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)
  'googleCloudAiplatformV1Execution': new VertexAiApi.GoogleCloudAiplatformV1Execution() // GoogleCloudAiplatformV1Execution | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresExecutionsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the MetadataStore where the Execution should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **executionId** | **String**| The {execution} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60; If not provided, the Execution&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting Execution.) | [optional] 
 **googleCloudAiplatformV1Execution** | [**GoogleCloudAiplatformV1Execution**](GoogleCloudAiplatformV1Execution.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Execution**](GoogleCloudAiplatformV1Execution.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresExecutionsList

> GoogleCloudAiplatformV1ListExecutionsResponse aiplatformProjectsLocationsMetadataStoresExecutionsList(parent, opts)



Lists Executions in the MetadataStore.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The MetadataStore whose Executions should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Filter specifying the boolean condition for the Executions to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering**: For example: `display_name = \"test\"`. Supported fields include: `name`, `display_name`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = \"2020-11-19T11:30:00-04:00\"`. * **Metadata field**: To filter on metadata fields use traversal operation as follows: `metadata..` For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata.\"field:1\".number_value = 10.0` * **Context based filtering**: To filter Executions based on the contexts to which they belong use the function operator with the full resource name: `in_context()`. For example: `in_context(\"projects//locations//metadataStores//contexts/\")` Each of the above supported filters can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5. For example: `display_name = \"test\" AND metadata.field1.bool_value = true`.
  'orderBy': "orderBy_example", // String | How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \" desc\" suffix; for example: \"foo desc, bar\". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.
  'pageSize': 56, // Number | The maximum number of Executions to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous MetadataService.ListExecutions call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with an INVALID_ARGUMENT error.)
};
apiInstance.aiplatformProjectsLocationsMetadataStoresExecutionsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The MetadataStore whose Executions should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Filter specifying the boolean condition for the Executions to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering**: For example: &#x60;display_name &#x3D; \&quot;test\&quot;&#x60;. Supported fields include: &#x60;name&#x60;, &#x60;display_name&#x60;, &#x60;state&#x60;, &#x60;schema_title&#x60;, &#x60;create_time&#x60;, and &#x60;update_time&#x60;. Time fields, such as &#x60;create_time&#x60; and &#x60;update_time&#x60;, require values specified in RFC-3339 format. For example: &#x60;create_time &#x3D; \&quot;2020-11-19T11:30:00-04:00\&quot;&#x60;. * **Metadata field**: To filter on metadata fields use traversal operation as follows: &#x60;metadata..&#x60; For example: &#x60;metadata.field_1.number_value &#x3D; 10.0&#x60; In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: &#x60;metadata.\&quot;field:1\&quot;.number_value &#x3D; 10.0&#x60; * **Context based filtering**: To filter Executions based on the contexts to which they belong use the function operator with the full resource name: &#x60;in_context()&#x60;. For example: &#x60;in_context(\&quot;projects//locations//metadataStores//contexts/\&quot;)&#x60; Each of the above supported filters can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). Maximum nested expression depth allowed is 5. For example: &#x60;display_name &#x3D; \&quot;test\&quot; AND metadata.field1.bool_value &#x3D; true&#x60;. | [optional] 
 **orderBy** | **String**| How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a \&quot; desc\&quot; suffix; for example: \&quot;foo desc, bar\&quot;. Subfields are specified with a &#x60;.&#x60; character, such as foo.bar. see https://google.aip.dev/132#ordering for more details. | [optional] 
 **pageSize** | **Number**| The maximum number of Executions to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous MetadataService.ListExecutions call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with an INVALID_ARGUMENT error.) | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListExecutionsResponse**](GoogleCloudAiplatformV1ListExecutionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresExecutionsPurge

> GoogleLongrunningOperation aiplatformProjectsLocationsMetadataStoresExecutionsPurge(parent, opts)



Purges Executions.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The metadata store to purge Executions from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1PurgeExecutionsRequest': new VertexAiApi.GoogleCloudAiplatformV1PurgeExecutionsRequest() // GoogleCloudAiplatformV1PurgeExecutionsRequest | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresExecutionsPurge(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The metadata store to purge Executions from. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1PurgeExecutionsRequest** | [**GoogleCloudAiplatformV1PurgeExecutionsRequest**](GoogleCloudAiplatformV1PurgeExecutionsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresExecutionsQueryExecutionInputsAndOutputs

> GoogleCloudAiplatformV1LineageSubgraph aiplatformProjectsLocationsMetadataStoresExecutionsQueryExecutionInputsAndOutputs(execution, opts)



Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let execution = "execution_example"; // String | Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.aiplatformProjectsLocationsMetadataStoresExecutionsQueryExecutionInputsAndOutputs(execution, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution** | **String**| Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleCloudAiplatformV1LineageSubgraph**](GoogleCloudAiplatformV1LineageSubgraph.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresList

> GoogleCloudAiplatformV1ListMetadataStoresResponse aiplatformProjectsLocationsMetadataStoresList(parent, opts)



Lists MetadataStores for a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Location whose MetadataStores should be listed. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of Metadata Stores to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous MetadataService.ListMetadataStores call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
};
apiInstance.aiplatformProjectsLocationsMetadataStoresList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The Location whose MetadataStores should be listed. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of Metadata Stores to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous MetadataService.ListMetadataStores call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListMetadataStoresResponse**](GoogleCloudAiplatformV1ListMetadataStoresResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresMetadataSchemasCreate

> GoogleCloudAiplatformV1MetadataSchema aiplatformProjectsLocationsMetadataStoresMetadataSchemasCreate(parent, opts)



Creates a MetadataSchema.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the MetadataStore where the MetadataSchema should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'metadataSchemaId': "metadataSchemaId_example", // String | The {metadata_schema} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataSchemas in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataSchema.)
  'googleCloudAiplatformV1MetadataSchema': new VertexAiApi.GoogleCloudAiplatformV1MetadataSchema() // GoogleCloudAiplatformV1MetadataSchema | 
};
apiInstance.aiplatformProjectsLocationsMetadataStoresMetadataSchemasCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the MetadataStore where the MetadataSchema should be created. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **metadataSchemaId** | **String**| The {metadata_schema} portion of the resource name with the format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}&#x60; If not provided, the MetadataStore&#39;s ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are &#x60;/a-z-/&#x60;. Must be unique across all MetadataSchemas in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can&#39;t view the preexisting MetadataSchema.) | [optional] 
 **googleCloudAiplatformV1MetadataSchema** | [**GoogleCloudAiplatformV1MetadataSchema**](GoogleCloudAiplatformV1MetadataSchema.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1MetadataSchema**](GoogleCloudAiplatformV1MetadataSchema.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMetadataStoresMetadataSchemasList

> GoogleCloudAiplatformV1ListMetadataSchemasResponse aiplatformProjectsLocationsMetadataStoresMetadataSchemasList(parent, opts)



Lists MetadataSchemas.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The MetadataStore whose MetadataSchemas should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | A query to filter available MetadataSchemas for matching results.
  'pageSize': 56, // Number | The maximum number of MetadataSchemas to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous MetadataService.ListMetadataSchemas call. Provide this to retrieve the next page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)
};
apiInstance.aiplatformProjectsLocationsMetadataStoresMetadataSchemasList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The MetadataStore whose MetadataSchemas should be listed. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| A query to filter available MetadataSchemas for matching results. | [optional] 
 **pageSize** | **Number**| The maximum number of MetadataSchemas to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous MetadataService.ListMetadataSchemas call. Provide this to retrieve the next page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListMetadataSchemasResponse**](GoogleCloudAiplatformV1ListMetadataSchemasResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsMigratableResourcesBatchMigrate

> GoogleLongrunningOperation aiplatformProjectsLocationsMigratableResourcesBatchMigrate(parent, opts)



Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchMigrateResourcesRequest': new VertexAiApi.GoogleCloudAiplatformV1BatchMigrateResourcesRequest() // GoogleCloudAiplatformV1BatchMigrateResourcesRequest | 
};
apiInstance.aiplatformProjectsLocationsMigratableResourcesBatchMigrate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The location of the migrated resource will live in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchMigrateResourcesRequest** | [**GoogleCloudAiplatformV1BatchMigrateResourcesRequest**](GoogleCloudAiplatformV1BatchMigrateResourcesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsMigratableResourcesSearch

> GoogleCloudAiplatformV1SearchMigratableResourcesResponse aiplatformProjectsLocationsMigratableResourcesSearch(parent, opts)



Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI&#39;s given location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The location that the migratable resources should be searched from. It's the Vertex AI location that the resources can be migrated to, not the resources' original location. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1SearchMigratableResourcesRequest': new VertexAiApi.GoogleCloudAiplatformV1SearchMigratableResourcesRequest() // GoogleCloudAiplatformV1SearchMigratableResourcesRequest | 
};
apiInstance.aiplatformProjectsLocationsMigratableResourcesSearch(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The location that the migratable resources should be searched from. It&#39;s the Vertex AI location that the resources can be migrated to, not the resources&#39; original location. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1SearchMigratableResourcesRequest** | [**GoogleCloudAiplatformV1SearchMigratableResourcesRequest**](GoogleCloudAiplatformV1SearchMigratableResourcesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1SearchMigratableResourcesResponse**](GoogleCloudAiplatformV1SearchMigratableResourcesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelDeploymentMonitoringJobsCreate

> GoogleCloudAiplatformV1ModelDeploymentMonitoringJob aiplatformProjectsLocationsModelDeploymentMonitoringJobsCreate(parent, opts)



Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ModelDeploymentMonitoringJob': new VertexAiApi.GoogleCloudAiplatformV1ModelDeploymentMonitoringJob() // GoogleCloudAiplatformV1ModelDeploymentMonitoringJob | 
};
apiInstance.aiplatformProjectsLocationsModelDeploymentMonitoringJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent of the ModelDeploymentMonitoringJob. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ModelDeploymentMonitoringJob** | [**GoogleCloudAiplatformV1ModelDeploymentMonitoringJob**](GoogleCloudAiplatformV1ModelDeploymentMonitoringJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ModelDeploymentMonitoringJob**](GoogleCloudAiplatformV1ModelDeploymentMonitoringJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelDeploymentMonitoringJobsList

> GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse aiplatformProjectsLocationsModelDeploymentMonitoringJobsList(parent, opts)



Lists ModelDeploymentMonitoringJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `state` supports `=`, `!=` comparisons. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"JOB_STATE_SUCCEEDED\" AND display_name:\"my_job_*\"` * `state!=\"JOB_STATE_FAILED\" OR display_name=\"my_job\"` * `NOT display_name=\"my_job\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `labels.keyA=valueA` * `labels.keyB:*`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read
};
apiInstance.aiplatformProjectsLocationsModelDeploymentMonitoringJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent of the ModelDeploymentMonitoringJob. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse**](GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsModelDeploymentMonitoringJobsSearchModelDeploymentMonitoringStatsAnomalies

> GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse aiplatformProjectsLocationsModelDeploymentMonitoringJobsSearchModelDeploymentMonitoringStatsAnomalies(modelDeploymentMonitoringJob, opts)



Searches Model Monitoring Statistics generated within a given time window.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let modelDeploymentMonitoringJob = "modelDeploymentMonitoringJob_example"; // String | Required. ModelDeploymentMonitoring Job resource name. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest': new VertexAiApi.GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest() // GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest | 
};
apiInstance.aiplatformProjectsLocationsModelDeploymentMonitoringJobsSearchModelDeploymentMonitoringStatsAnomalies(modelDeploymentMonitoringJob, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modelDeploymentMonitoringJob** | **String**| Required. ModelDeploymentMonitoring Job resource name. Format: &#x60;projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest** | [**GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest**](GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse**](GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsCopy

> GoogleLongrunningOperation aiplatformProjectsLocationsModelsCopy(parent, opts)



Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1CopyModelRequest': new VertexAiApi.GoogleCloudAiplatformV1CopyModelRequest() // GoogleCloudAiplatformV1CopyModelRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsCopy(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location into which to copy the Model. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1CopyModelRequest** | [**GoogleCloudAiplatformV1CopyModelRequest**](GoogleCloudAiplatformV1CopyModelRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsDeleteVersion

> GoogleLongrunningOperation aiplatformProjectsLocationsModelsDeleteVersion(name, opts)



Deletes a Model version. Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the model version to be deleted, with a version ID explicitly included. Example: `projects/{project}/locations/{location}/models/{model}@1234`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.aiplatformProjectsLocationsModelsDeleteVersion(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the model version to be deleted, with a version ID explicitly included. Example: &#x60;projects/{project}/locations/{location}/models/{model}@1234&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsModelsEvaluationsImport

> GoogleCloudAiplatformV1ModelEvaluation aiplatformProjectsLocationsModelsEvaluationsImport(parent, opts)



Imports an externally generated ModelEvaluation.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the parent model resource. Format: `projects/{project}/locations/{location}/models/{model}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ImportModelEvaluationRequest': new VertexAiApi.GoogleCloudAiplatformV1ImportModelEvaluationRequest() // GoogleCloudAiplatformV1ImportModelEvaluationRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsEvaluationsImport(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the parent model resource. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ImportModelEvaluationRequest** | [**GoogleCloudAiplatformV1ImportModelEvaluationRequest**](GoogleCloudAiplatformV1ImportModelEvaluationRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ModelEvaluation**](GoogleCloudAiplatformV1ModelEvaluation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsEvaluationsList

> GoogleCloudAiplatformV1ListModelEvaluationsResponse aiplatformProjectsLocationsModelsEvaluationsList(parent, opts)



Lists ModelEvaluations in a Model.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Model to list the ModelEvaluations from. Format: `projects/{project}/locations/{location}/models/{model}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListModelEvaluationsResponse.next_page_token of the previous ModelService.ListModelEvaluations call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsModelsEvaluationsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Model to list the ModelEvaluations from. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListModelEvaluationsResponse.next_page_token of the previous ModelService.ListModelEvaluations call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListModelEvaluationsResponse**](GoogleCloudAiplatformV1ListModelEvaluationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsModelsEvaluationsSlicesBatchImport

> GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse aiplatformProjectsLocationsModelsEvaluationsSlicesBatchImport(parent, opts)



Imports a list of externally generated EvaluatedAnnotations.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the parent ModelEvaluationSlice resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest': new VertexAiApi.GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest() // GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsEvaluationsSlicesBatchImport(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the parent ModelEvaluationSlice resource. Format: &#x60;projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest** | [**GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest**](GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse**](GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsEvaluationsSlicesList

> GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse aiplatformProjectsLocationsModelsEvaluationsSlicesList(parent, opts)



Lists ModelEvaluationSlices in a ModelEvaluation.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the ModelEvaluation to list the ModelEvaluationSlices from. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. * `slice.dimension` - for =.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListModelEvaluationSlicesResponse.next_page_token of the previous ModelService.ListModelEvaluationSlices call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsModelsEvaluationsSlicesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the ModelEvaluation to list the ModelEvaluationSlices from. Format: &#x60;projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. * &#x60;slice.dimension&#x60; - for &#x3D;. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListModelEvaluationSlicesResponse.next_page_token of the previous ModelService.ListModelEvaluationSlices call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse**](GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsModelsExport

> GoogleLongrunningOperation aiplatformProjectsLocationsModelsExport(name, opts)



Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The resource name of the Model to export. The resource name may contain version id or version alias to specify the version, if no version is specified, the default version will be exported.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ExportModelRequest': new VertexAiApi.GoogleCloudAiplatformV1ExportModelRequest() // GoogleCloudAiplatformV1ExportModelRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsExport(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The resource name of the Model to export. The resource name may contain version id or version alias to specify the version, if no version is specified, the default version will be exported. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ExportModelRequest** | [**GoogleCloudAiplatformV1ExportModelRequest**](GoogleCloudAiplatformV1ExportModelRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsList

> GoogleCloudAiplatformV1ListModelsResponse aiplatformProjectsLocationsModelsList(parent, opts)



Lists Models in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the Models from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `model` supports = and !=. `model` represents the Model ID, i.e. the last segment of the Model's resource name. * `display_name` supports = and != * `labels` supports general map functions that is: * `labels.key=value` - key:value equality * `labels.key:* or labels:key - key existence * A key including a space must be quoted. `labels.\"a key\"`. Some examples: * `model=1234` * `displayName=\"myDisplayName\"` * `labels.myKey=\"myValue\"`
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `display_name` * `create_time` * `update_time` Example: `display_name, create_time desc`.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListModelsResponse.next_page_token of the previous ModelService.ListModels call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsModelsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the Models from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;model&#x60; supports &#x3D; and !&#x3D;. &#x60;model&#x60; represents the Model ID, i.e. the last segment of the Model&#39;s resource name. * &#x60;display_name&#x60; supports &#x3D; and !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;model&#x3D;1234&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListModelsResponse.next_page_token of the previous ModelService.ListModels call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListModelsResponse**](GoogleCloudAiplatformV1ListModelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsModelsListVersions

> GoogleCloudAiplatformV1ListModelVersionsResponse aiplatformProjectsLocationsModelsListVersions(name, opts)



Lists versions of the specified model.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the model to list versions for.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `labels` supports general map functions that is: * `labels.key=value` - key:value equality * `labels.key:* or labels:key - key existence * A key including a space must be quoted. `labels.\"a key\"`. Some examples: * `labels.myKey=\"myValue\"`
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `create_time` * `update_time` Example: `update_time asc, create_time desc`.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via next_page_token of the previous ListModelVersions call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsModelsListVersions(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the model to list versions for. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. Some examples: * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;update_time asc, create_time desc&#x60;. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via next_page_token of the previous ListModelVersions call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListModelVersionsResponse**](GoogleCloudAiplatformV1ListModelVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsModelsMergeVersionAliases

> GoogleCloudAiplatformV1Model aiplatformProjectsLocationsModelsMergeVersionAliases(name, opts)



Merges a set of aliases for a Model version.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the model version to merge aliases, with a version ID explicitly included. Example: `projects/{project}/locations/{location}/models/{model}@1234`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1MergeVersionAliasesRequest': new VertexAiApi.GoogleCloudAiplatformV1MergeVersionAliasesRequest() // GoogleCloudAiplatformV1MergeVersionAliasesRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsMergeVersionAliases(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the model version to merge aliases, with a version ID explicitly included. Example: &#x60;projects/{project}/locations/{location}/models/{model}@1234&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1MergeVersionAliasesRequest** | [**GoogleCloudAiplatformV1MergeVersionAliasesRequest**](GoogleCloudAiplatformV1MergeVersionAliasesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Model**](GoogleCloudAiplatformV1Model.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsUpdateExplanationDataset

> GoogleLongrunningOperation aiplatformProjectsLocationsModelsUpdateExplanationDataset(model, opts)



Incrementally update the dataset used for an examples model.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let model = "model_example"; // String | Required. The resource name of the Model to update. Format: `projects/{project}/locations/{location}/models/{model}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1UpdateExplanationDatasetRequest': new VertexAiApi.GoogleCloudAiplatformV1UpdateExplanationDatasetRequest() // GoogleCloudAiplatformV1UpdateExplanationDatasetRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsUpdateExplanationDataset(model, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **String**| Required. The resource name of the Model to update. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1UpdateExplanationDatasetRequest** | [**GoogleCloudAiplatformV1UpdateExplanationDatasetRequest**](GoogleCloudAiplatformV1UpdateExplanationDatasetRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsModelsUpload

> GoogleLongrunningOperation aiplatformProjectsLocationsModelsUpload(parent, opts)



Uploads a Model artifact into Vertex AI.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location into which to upload the Model. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1UploadModelRequest': new VertexAiApi.GoogleCloudAiplatformV1UploadModelRequest() // GoogleCloudAiplatformV1UploadModelRequest | 
};
apiInstance.aiplatformProjectsLocationsModelsUpload(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location into which to upload the Model. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1UploadModelRequest** | [**GoogleCloudAiplatformV1UploadModelRequest**](GoogleCloudAiplatformV1UploadModelRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsNasJobsCreate

> GoogleCloudAiplatformV1NasJob aiplatformProjectsLocationsNasJobsCreate(parent, opts)



Creates a NasJob

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the NasJob in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1NasJob': new VertexAiApi.GoogleCloudAiplatformV1NasJob() // GoogleCloudAiplatformV1NasJob | 
};
apiInstance.aiplatformProjectsLocationsNasJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the NasJob in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1NasJob** | [**GoogleCloudAiplatformV1NasJob**](GoogleCloudAiplatformV1NasJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1NasJob**](GoogleCloudAiplatformV1NasJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsNasJobsList

> GoogleCloudAiplatformV1ListNasJobsResponse aiplatformProjectsLocationsNasJobsList(parent, opts)



Lists NasJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the NasJobs from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `state` supports `=`, `!=` comparisons. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"JOB_STATE_SUCCEEDED\" AND display_name:\"my_job_*\"` * `state!=\"JOB_STATE_FAILED\" OR display_name=\"my_job\"` * `NOT display_name=\"my_job\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `labels.keyA=valueA` * `labels.keyB:*`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListNasJobsResponse.next_page_token of the previous JobService.ListNasJobs call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsNasJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the NasJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;JOB_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_job_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;JOB_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_job\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;labels.keyA&#x3D;valueA&#x60; * &#x60;labels.keyB:*&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListNasJobsResponse.next_page_token of the previous JobService.ListNasJobs call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListNasJobsResponse**](GoogleCloudAiplatformV1ListNasJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsNasJobsNasTrialDetailsList

> GoogleCloudAiplatformV1ListNasTrialDetailsResponse aiplatformProjectsLocationsNasJobsNasTrialDetailsList(parent, opts)



List top NasTrialDetails of a NasJob.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the NasJob resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example" // String | The standard list page token. Typically obtained via ListNasTrialDetailsResponse.next_page_token of the previous JobService.ListNasTrialDetails call.
};
apiInstance.aiplatformProjectsLocationsNasJobsNasTrialDetailsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the NasJob resource. Format: &#x60;projects/{project}/locations/{location}/nasJobs/{nas_job}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListNasTrialDetailsResponse.next_page_token of the previous JobService.ListNasTrialDetails call. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListNasTrialDetailsResponse**](GoogleCloudAiplatformV1ListNasTrialDetailsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimeTemplatesCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsNotebookRuntimeTemplatesCreate(parent, opts)



Creates a NotebookRuntimeTemplate.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the NotebookRuntimeTemplate. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'notebookRuntimeTemplateId': "notebookRuntimeTemplateId_example", // String | Optional. User specified ID for the notebook runtime template.
  'googleCloudAiplatformV1NotebookRuntimeTemplate': new VertexAiApi.GoogleCloudAiplatformV1NotebookRuntimeTemplate() // GoogleCloudAiplatformV1NotebookRuntimeTemplate | 
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimeTemplatesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the NotebookRuntimeTemplate. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **notebookRuntimeTemplateId** | **String**| Optional. User specified ID for the notebook runtime template. | [optional] 
 **googleCloudAiplatformV1NotebookRuntimeTemplate** | [**GoogleCloudAiplatformV1NotebookRuntimeTemplate**](GoogleCloudAiplatformV1NotebookRuntimeTemplate.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimeTemplatesGetIamPolicy

> GoogleIamV1Policy aiplatformProjectsLocationsNotebookRuntimeTemplatesGetIamPolicy(resource, opts)



Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'optionsRequestedPolicyVersion': 56 // Number | Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimeTemplatesGetIamPolicy(resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **String**| REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **optionsRequestedPolicyVersion** | **Number**| Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). | [optional] 

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimeTemplatesList

> GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse aiplatformProjectsLocationsNotebookRuntimeTemplatesList(parent, opts)



Lists NotebookRuntimeTemplates in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location from which to list the NotebookRuntimeTemplates. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `notebookRuntimeTemplate` supports = and !=. `notebookRuntimeTemplate` represents the NotebookRuntimeTemplate ID, i.e. the last segment of the NotebookRuntimeTemplate's resource name. * `display_name` supports = and != * `labels` supports general map functions that is: * `labels.key=value` - key:value equality * `labels.key:* or labels:key - key existence * A key including a space must be quoted. `labels.\"a key\"`. * `notebookRuntimeType` supports = and !=. notebookRuntimeType enum: [USER_DEFINED, ONE_CLICK]. Some examples: * `notebookRuntimeTemplate=notebookRuntimeTemplate123` * `displayName=\"myDisplayName\"` * `labels.myKey=\"myValue\"` * `notebookRuntimeType=USER_DEFINED`
  'orderBy': "orderBy_example", // String | Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `display_name` * `create_time` * `update_time` Example: `display_name, create_time desc`.
  'pageSize': 56, // Number | Optional. The standard list page size.
  'pageToken': "pageToken_example", // String | Optional. The standard list page token. Typically obtained via ListNotebookRuntimeTemplatesResponse.next_page_token of the previous NotebookService.ListNotebookRuntimeTemplates call.
  'readMask': "readMask_example" // String | Optional. Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimeTemplatesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location from which to list the NotebookRuntimeTemplates. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;notebookRuntimeTemplate&#x60; supports &#x3D; and !&#x3D;. &#x60;notebookRuntimeTemplate&#x60; represents the NotebookRuntimeTemplate ID, i.e. the last segment of the NotebookRuntimeTemplate&#39;s resource name. * &#x60;display_name&#x60; supports &#x3D; and !&#x3D; * &#x60;labels&#x60; supports general map functions that is: * &#x60;labels.key&#x3D;value&#x60; - key:value equality * &#x60;labels.key:* or labels:key - key existence * A key including a space must be quoted. &#x60;labels.\&quot;a key\&quot;&#x60;. * &#x60;notebookRuntimeType&#x60; supports &#x3D; and !&#x3D;. notebookRuntimeType enum: [USER_DEFINED, ONE_CLICK]. Some examples: * &#x60;notebookRuntimeTemplate&#x3D;notebookRuntimeTemplate123&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; * &#x60;labels.myKey&#x3D;\&quot;myValue\&quot;&#x60; * &#x60;notebookRuntimeType&#x3D;USER_DEFINED&#x60; | [optional] 
 **orderBy** | **String**| Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;. | [optional] 
 **pageSize** | **Number**| Optional. The standard list page size. | [optional] 
 **pageToken** | **String**| Optional. The standard list page token. Typically obtained via ListNotebookRuntimeTemplatesResponse.next_page_token of the previous NotebookService.ListNotebookRuntimeTemplates call. | [optional] 
 **readMask** | **String**| Optional. Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse**](GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimeTemplatesSetIamPolicy

> GoogleIamV1Policy aiplatformProjectsLocationsNotebookRuntimeTemplatesSetIamPolicy(resource, opts)



Sets the access control policy on the specified resource. Replaces any existing policy. Can return &#x60;NOT_FOUND&#x60;, &#x60;INVALID_ARGUMENT&#x60;, and &#x60;PERMISSION_DENIED&#x60; errors.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleIamV1SetIamPolicyRequest': new VertexAiApi.GoogleIamV1SetIamPolicyRequest() // GoogleIamV1SetIamPolicyRequest | 
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimeTemplatesSetIamPolicy(resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **String**| REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleIamV1SetIamPolicyRequest** | [**GoogleIamV1SetIamPolicyRequest**](GoogleIamV1SetIamPolicyRequest.md)|  | [optional] 

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimeTemplatesTestIamPermissions

> GoogleIamV1TestIamPermissionsResponse aiplatformProjectsLocationsNotebookRuntimeTemplatesTestIamPermissions(resource, opts)



Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a &#x60;NOT_FOUND&#x60; error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'permissions': ["null"] // [String] | The set of permissions to check for the `resource`. Permissions with wildcards (such as `*` or `storage.*`) are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimeTemplatesTestIamPermissions(resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **String**| REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **permissions** | [**[String]**](String.md)| The set of permissions to check for the &#x60;resource&#x60;. Permissions with wildcards (such as &#x60;*&#x60; or &#x60;storage.*&#x60;) are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). | [optional] 

### Return type

[**GoogleIamV1TestIamPermissionsResponse**](GoogleIamV1TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimesAssign

> GoogleLongrunningOperation aiplatformProjectsLocationsNotebookRuntimesAssign(parent, opts)



Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to get the NotebookRuntime assignment. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1AssignNotebookRuntimeRequest': new VertexAiApi.GoogleCloudAiplatformV1AssignNotebookRuntimeRequest() // GoogleCloudAiplatformV1AssignNotebookRuntimeRequest | 
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimesAssign(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to get the NotebookRuntime assignment. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1AssignNotebookRuntimeRequest** | [**GoogleCloudAiplatformV1AssignNotebookRuntimeRequest**](GoogleCloudAiplatformV1AssignNotebookRuntimeRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimesList

> GoogleCloudAiplatformV1ListNotebookRuntimesResponse aiplatformProjectsLocationsNotebookRuntimesList(parent, opts)



Lists NotebookRuntimes in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location from which to list the NotebookRuntimes. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `notebookRuntime` supports = and !=. `notebookRuntime` represents the NotebookRuntime ID, i.e. the last segment of the NotebookRuntime's resource name. * `displayName` supports = and != and regex. * `notebookRuntimeTemplate` supports = and !=. `notebookRuntimeTemplate` represents the NotebookRuntimeTemplate ID, i.e. the last segment of the NotebookRuntimeTemplate's resource name. * `healthState` supports = and !=. healthState enum: [HEALTHY, UNHEALTHY, HEALTH_STATE_UNSPECIFIED]. * `runtimeState` supports = and !=. runtimeState enum: [RUNTIME_STATE_UNSPECIFIED, RUNNING, BEING_STARTED, BEING_STOPPED, STOPPED, BEING_UPGRADED]. * `runtimeUser` supports = and !=. * API version is UI only: `uiState` supports = and !=. uiState enum: [UI_RESOURCE_STATE_UNSPECIFIED, UI_RESOURCE_STATE_BEING_CREATED, UI_RESOURCE_STATE_ACTIVE, UI_RESOURCE_STATE_BEING_DELETED, UI_RESOURCE_STATE_CREATION_FAILED]. * `notebookRuntimeType` supports = and !=. notebookRuntimeType enum: [USER_DEFINED, ONE_CLICK]. Some examples: * `notebookRuntime=\"notebookRuntime123\"` * `displayName=\"myDisplayName\"` and `displayName=~\"myDisplayNameRegex\"` * `notebookRuntimeTemplate=\"notebookRuntimeTemplate321\"` * `healthState=HEALTHY` * `runtimeState=RUNNING` * `runtimeUser=\"test@google.com\"` * `uiState=UI_RESOURCE_STATE_BEING_DELETED` * `notebookRuntimeType=USER_DEFINED`
  'orderBy': "orderBy_example", // String | Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending. Supported fields: * `display_name` * `create_time` * `update_time` Example: `display_name, create_time desc`.
  'pageSize': 56, // Number | Optional. The standard list page size.
  'pageToken': "pageToken_example", // String | Optional. The standard list page token. Typically obtained via ListNotebookRuntimesResponse.next_page_token of the previous NotebookService.ListNotebookRuntimes call.
  'readMask': "readMask_example" // String | Optional. Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location from which to list the NotebookRuntimes. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * &#x60;notebookRuntime&#x60; supports &#x3D; and !&#x3D;. &#x60;notebookRuntime&#x60; represents the NotebookRuntime ID, i.e. the last segment of the NotebookRuntime&#39;s resource name. * &#x60;displayName&#x60; supports &#x3D; and !&#x3D; and regex. * &#x60;notebookRuntimeTemplate&#x60; supports &#x3D; and !&#x3D;. &#x60;notebookRuntimeTemplate&#x60; represents the NotebookRuntimeTemplate ID, i.e. the last segment of the NotebookRuntimeTemplate&#39;s resource name. * &#x60;healthState&#x60; supports &#x3D; and !&#x3D;. healthState enum: [HEALTHY, UNHEALTHY, HEALTH_STATE_UNSPECIFIED]. * &#x60;runtimeState&#x60; supports &#x3D; and !&#x3D;. runtimeState enum: [RUNTIME_STATE_UNSPECIFIED, RUNNING, BEING_STARTED, BEING_STOPPED, STOPPED, BEING_UPGRADED]. * &#x60;runtimeUser&#x60; supports &#x3D; and !&#x3D;. * API version is UI only: &#x60;uiState&#x60; supports &#x3D; and !&#x3D;. uiState enum: [UI_RESOURCE_STATE_UNSPECIFIED, UI_RESOURCE_STATE_BEING_CREATED, UI_RESOURCE_STATE_ACTIVE, UI_RESOURCE_STATE_BEING_DELETED, UI_RESOURCE_STATE_CREATION_FAILED]. * &#x60;notebookRuntimeType&#x60; supports &#x3D; and !&#x3D;. notebookRuntimeType enum: [USER_DEFINED, ONE_CLICK]. Some examples: * &#x60;notebookRuntime&#x3D;\&quot;notebookRuntime123\&quot;&#x60; * &#x60;displayName&#x3D;\&quot;myDisplayName\&quot;&#x60; and &#x60;displayName&#x3D;~\&quot;myDisplayNameRegex\&quot;&#x60; * &#x60;notebookRuntimeTemplate&#x3D;\&quot;notebookRuntimeTemplate321\&quot;&#x60; * &#x60;healthState&#x3D;HEALTHY&#x60; * &#x60;runtimeState&#x3D;RUNNING&#x60; * &#x60;runtimeUser&#x3D;\&quot;test@google.com\&quot;&#x60; * &#x60;uiState&#x3D;UI_RESOURCE_STATE_BEING_DELETED&#x60; * &#x60;notebookRuntimeType&#x3D;USER_DEFINED&#x60; | [optional] 
 **orderBy** | **String**| Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. Supported fields: * &#x60;display_name&#x60; * &#x60;create_time&#x60; * &#x60;update_time&#x60; Example: &#x60;display_name, create_time desc&#x60;. | [optional] 
 **pageSize** | **Number**| Optional. The standard list page size. | [optional] 
 **pageToken** | **String**| Optional. The standard list page token. Typically obtained via ListNotebookRuntimesResponse.next_page_token of the previous NotebookService.ListNotebookRuntimes call. | [optional] 
 **readMask** | **String**| Optional. Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListNotebookRuntimesResponse**](GoogleCloudAiplatformV1ListNotebookRuntimesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimesStart

> GoogleLongrunningOperation aiplatformProjectsLocationsNotebookRuntimesStart(name, opts)



Starts a NotebookRuntime.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the NotebookRuntime resource to be started. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimesStart(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the NotebookRuntime resource to be started. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsNotebookRuntimesUpgrade

> GoogleLongrunningOperation aiplatformProjectsLocationsNotebookRuntimesUpgrade(name, opts)



Upgrades a NotebookRuntime.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the NotebookRuntime resource to be upgrade. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsNotebookRuntimesUpgrade(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the NotebookRuntime resource to be upgrade. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPipelineJobsCreate

> GoogleCloudAiplatformV1PipelineJob aiplatformProjectsLocationsPipelineJobsCreate(parent, opts)



Creates a PipelineJob. A PipelineJob will run immediately when created.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the PipelineJob in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pipelineJobId': "pipelineJobId_example", // String | The ID to use for the PipelineJob, which will become the final component of the PipelineJob name. If not provided, an ID will be automatically generated. This value should be less than 128 characters, and valid characters are `/a-z-/`.
  'googleCloudAiplatformV1PipelineJob': new VertexAiApi.GoogleCloudAiplatformV1PipelineJob() // GoogleCloudAiplatformV1PipelineJob | 
};
apiInstance.aiplatformProjectsLocationsPipelineJobsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the PipelineJob in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pipelineJobId** | **String**| The ID to use for the PipelineJob, which will become the final component of the PipelineJob name. If not provided, an ID will be automatically generated. This value should be less than 128 characters, and valid characters are &#x60;/a-z-/&#x60;. | [optional] 
 **googleCloudAiplatformV1PipelineJob** | [**GoogleCloudAiplatformV1PipelineJob**](GoogleCloudAiplatformV1PipelineJob.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1PipelineJob**](GoogleCloudAiplatformV1PipelineJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPipelineJobsList

> GoogleCloudAiplatformV1ListPipelineJobsResponse aiplatformProjectsLocationsPipelineJobsList(parent, opts)



Lists PipelineJobs in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the PipelineJobs from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the PipelineJobs that match the filter expression. The following fields are supported: * `pipeline_name`: Supports `=` and `!=` comparisons. * `display_name`: Supports `=`, `!=` comparisons, and `:` wildcard. * `pipeline_job_user_id`: Supports `=`, `!=` comparisons, and `:` wildcard. for example, can check if pipeline's display_name contains *step* by doing display_name:\\\"*step*\\\" * `state`: Supports `=` and `!=` comparisons. * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `end_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality and key presence. * `template_uri`: Supports `=`, `!=` comparisons, and `:` wildcard. * `template_metadata.version`: Supports `=`, `!=` comparisons, and `:` wildcard. Filter expressions can be combined together using logical operators (`AND` & `OR`). For example: `pipeline_name=\"test\" AND create_time>\"2020-05-18T13:30:00Z\"`. The syntax to define filter expression is based on https://google.aip.dev/160. Examples: * `create_time>\"2021-05-18T00:00:00Z\" OR update_time>\"2020-05-18T00:00:00Z\"` PipelineJobs created or updated after 2020-05-18 00:00:00 UTC. * `labels.env = \"prod\"` PipelineJobs with label \"env\" set to \"prod\".
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by. The default sort order is in ascending order. Use \"desc\" after a field name for descending. You can have multiple order_by fields provided e.g. \"create_time desc, end_time\", \"end_time, start_time, update_time\" For example, using \"create_time desc, end_time\" will order results by create time in descending order, and if there are multiple jobs having the same create time, order them by the end time in ascending order. if order_by is not specified, it will order by default order is create time in descending order. Supported fields: * `create_time` * `update_time` * `end_time` * `start_time`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListPipelineJobsResponse.next_page_token of the previous PipelineService.ListPipelineJobs call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsPipelineJobsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the PipelineJobs from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the PipelineJobs that match the filter expression. The following fields are supported: * &#x60;pipeline_name&#x60;: Supports &#x60;&#x3D;&#x60; and &#x60;!&#x3D;&#x60; comparisons. * &#x60;display_name&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;pipeline_job_user_id&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. for example, can check if pipeline&#39;s display_name contains *step* by doing display_name:\\\&quot;*step*\\\&quot; * &#x60;state&#x60;: Supports &#x60;&#x3D;&#x60; and &#x60;!&#x3D;&#x60; comparisons. * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;update_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;end_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;labels&#x60;: Supports key-value equality and key presence. * &#x60;template_uri&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;template_metadata.version&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. Filter expressions can be combined together using logical operators (&#x60;AND&#x60; &amp; &#x60;OR&#x60;). For example: &#x60;pipeline_name&#x3D;\&quot;test\&quot; AND create_time&gt;\&quot;2020-05-18T13:30:00Z\&quot;&#x60;. The syntax to define filter expression is based on https://google.aip.dev/160. Examples: * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot; OR update_time&gt;\&quot;2020-05-18T00:00:00Z\&quot;&#x60; PipelineJobs created or updated after 2020-05-18 00:00:00 UTC. * &#x60;labels.env &#x3D; \&quot;prod\&quot;&#x60; PipelineJobs with label \&quot;env\&quot; set to \&quot;prod\&quot;. | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by. The default sort order is in ascending order. Use \&quot;desc\&quot; after a field name for descending. You can have multiple order_by fields provided e.g. \&quot;create_time desc, end_time\&quot;, \&quot;end_time, start_time, update_time\&quot; For example, using \&quot;create_time desc, end_time\&quot; will order results by create time in descending order, and if there are multiple jobs having the same create time, order them by the end time in ascending order. if order_by is not specified, it will order by default order is create time in descending order. Supported fields: * &#x60;create_time&#x60; * &#x60;update_time&#x60; * &#x60;end_time&#x60; * &#x60;start_time&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListPipelineJobsResponse.next_page_token of the previous PipelineService.ListPipelineJobs call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListPipelineJobsResponse**](GoogleCloudAiplatformV1ListPipelineJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsComputeTokens

> GoogleCloudAiplatformV1ComputeTokensResponse aiplatformProjectsLocationsPublishersModelsComputeTokens(endpoint, opts)



Return a list of tokens based on the input text.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to get lists of tokens and token ids.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ComputeTokensRequest': new VertexAiApi.GoogleCloudAiplatformV1ComputeTokensRequest() // GoogleCloudAiplatformV1ComputeTokensRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsComputeTokens(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to get lists of tokens and token ids. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ComputeTokensRequest** | [**GoogleCloudAiplatformV1ComputeTokensRequest**](GoogleCloudAiplatformV1ComputeTokensRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ComputeTokensResponse**](GoogleCloudAiplatformV1ComputeTokensResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsCountTokens

> GoogleCloudAiplatformV1CountTokensResponse aiplatformProjectsLocationsPublishersModelsCountTokens(endpoint, opts)



Perform a token counting.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to perform token counting. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1CountTokensRequest': new VertexAiApi.GoogleCloudAiplatformV1CountTokensRequest() // GoogleCloudAiplatformV1CountTokensRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsCountTokens(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to perform token counting. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1CountTokensRequest** | [**GoogleCloudAiplatformV1CountTokensRequest**](GoogleCloudAiplatformV1CountTokensRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1CountTokensResponse**](GoogleCloudAiplatformV1CountTokensResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsGenerateContent

> GoogleCloudAiplatformV1GenerateContentResponse aiplatformProjectsLocationsPublishersModelsGenerateContent(model, opts)



Generate content with multimodal inputs.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let model = "model_example"; // String | Required. The name of the publisher model requested to serve the prediction. Format: `projects/{project}/locations/{location}/publishers/_*_/models/_*`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1GenerateContentRequest': new VertexAiApi.GoogleCloudAiplatformV1GenerateContentRequest() // GoogleCloudAiplatformV1GenerateContentRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsGenerateContent(model, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **String**| Required. The name of the publisher model requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/publishers/_*_/models/_*&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1GenerateContentRequest** | [**GoogleCloudAiplatformV1GenerateContentRequest**](GoogleCloudAiplatformV1GenerateContentRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1GenerateContentResponse**](GoogleCloudAiplatformV1GenerateContentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsPredict

> GoogleCloudAiplatformV1PredictResponse aiplatformProjectsLocationsPublishersModelsPredict(endpoint, opts)



Perform an online prediction.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1PredictRequest': new VertexAiApi.GoogleCloudAiplatformV1PredictRequest() // GoogleCloudAiplatformV1PredictRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsPredict(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1PredictRequest** | [**GoogleCloudAiplatformV1PredictRequest**](GoogleCloudAiplatformV1PredictRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1PredictResponse**](GoogleCloudAiplatformV1PredictResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsRawPredict

> GoogleApiHttpBody aiplatformProjectsLocationsPublishersModelsRawPredict(endpoint, opts)



Perform an online prediction with an arbitrary HTTP payload. The response includes the following HTTP headers: * &#x60;X-Vertex-AI-Endpoint-Id&#x60;: ID of the Endpoint that served this prediction. * &#x60;X-Vertex-AI-Deployed-Model-Id&#x60;: ID of the Endpoint&#39;s DeployedModel that served this prediction.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1RawPredictRequest': new VertexAiApi.GoogleCloudAiplatformV1RawPredictRequest() // GoogleCloudAiplatformV1RawPredictRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsRawPredict(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1RawPredictRequest** | [**GoogleCloudAiplatformV1RawPredictRequest**](GoogleCloudAiplatformV1RawPredictRequest.md)|  | [optional] 

### Return type

[**GoogleApiHttpBody**](GoogleApiHttpBody.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsServerStreamingPredict

> GoogleCloudAiplatformV1StreamingPredictResponse aiplatformProjectsLocationsPublishersModelsServerStreamingPredict(endpoint, opts)



Perform a server-side streaming online prediction request for Vertex LLM streaming.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1StreamingPredictRequest': new VertexAiApi.GoogleCloudAiplatformV1StreamingPredictRequest() // GoogleCloudAiplatformV1StreamingPredictRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsServerStreamingPredict(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1StreamingPredictRequest** | [**GoogleCloudAiplatformV1StreamingPredictRequest**](GoogleCloudAiplatformV1StreamingPredictRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1StreamingPredictResponse**](GoogleCloudAiplatformV1StreamingPredictResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsStreamGenerateContent

> GoogleCloudAiplatformV1GenerateContentResponse aiplatformProjectsLocationsPublishersModelsStreamGenerateContent(model, opts)



Generate content with multimodal inputs with streaming support.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let model = "model_example"; // String | Required. The name of the publisher model requested to serve the prediction. Format: `projects/{project}/locations/{location}/publishers/_*_/models/_*`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1GenerateContentRequest': new VertexAiApi.GoogleCloudAiplatformV1GenerateContentRequest() // GoogleCloudAiplatformV1GenerateContentRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsStreamGenerateContent(model, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **String**| Required. The name of the publisher model requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/publishers/_*_/models/_*&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1GenerateContentRequest** | [**GoogleCloudAiplatformV1GenerateContentRequest**](GoogleCloudAiplatformV1GenerateContentRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1GenerateContentResponse**](GoogleCloudAiplatformV1GenerateContentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsPublishersModelsStreamRawPredict

> GoogleApiHttpBody aiplatformProjectsLocationsPublishersModelsStreamRawPredict(endpoint, opts)



Perform a streaming online prediction with an arbitrary HTTP payload.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let endpoint = "endpoint_example"; // String | Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1StreamRawPredictRequest': new VertexAiApi.GoogleCloudAiplatformV1StreamRawPredictRequest() // GoogleCloudAiplatformV1StreamRawPredictRequest | 
};
apiInstance.aiplatformProjectsLocationsPublishersModelsStreamRawPredict(endpoint, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **String**| Required. The name of the Endpoint requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1StreamRawPredictRequest** | [**GoogleCloudAiplatformV1StreamRawPredictRequest**](GoogleCloudAiplatformV1StreamRawPredictRequest.md)|  | [optional] 

### Return type

[**GoogleApiHttpBody**](GoogleApiHttpBody.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsSchedulesCreate

> GoogleCloudAiplatformV1Schedule aiplatformProjectsLocationsSchedulesCreate(parent, opts)



Creates a Schedule.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1Schedule': new VertexAiApi.GoogleCloudAiplatformV1Schedule() // GoogleCloudAiplatformV1Schedule | 
};
apiInstance.aiplatformProjectsLocationsSchedulesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the Schedule in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1Schedule** | [**GoogleCloudAiplatformV1Schedule**](GoogleCloudAiplatformV1Schedule.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Schedule**](GoogleCloudAiplatformV1Schedule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsSchedulesList

> GoogleCloudAiplatformV1ListSchedulesResponse aiplatformProjectsLocationsSchedulesList(parent, opts)



Lists Schedules in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the Schedules from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the Schedules that match the filter expression. The following fields are supported: * `display_name`: Supports `=`, `!=` comparisons, and `:` wildcard. * `state`: Supports `=` and `!=` comparisons. * `request`: Supports existence of the check. (e.g. `create_pipeline_job_request:*` --> Schedule has create_pipeline_job_request). * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `start_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. * `end_time`: Supports `=`, `!=`, `<`, `>`, `<=`, `>=` comparisons and `:*` existence check. Values must be in RFC 3339 format. * `next_run_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. Filter expressions can be combined together using logical operators (`NOT`, `AND` & `OR`). The syntax to define filter expression is based on https://google.aip.dev/160. Examples: * `state=\"ACTIVE\" AND display_name:\"my_schedule_*\"` * `NOT display_name=\"my_schedule\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `end_time>\"2021-05-18T00:00:00Z\" OR NOT end_time:*` * `create_pipeline_job_request:*`
  'orderBy': "orderBy_example", // String | A comma-separated list of fields to order by. The default sort order is in ascending order. Use \"desc\" after a field name for descending. You can have multiple order_by fields provided. For example, using \"create_time desc, end_time\" will order results by create time in descending order, and if there are multiple schedules having the same create time, order them by the end time in ascending order. If order_by is not specified, it will order by default with create_time in descending order. Supported fields: * `create_time` * `start_time` * `end_time` * `next_run_time`
  'pageSize': 56, // Number | The standard list page size. Default to 100 if not specified.
  'pageToken': "pageToken_example" // String | The standard list page token. Typically obtained via ListSchedulesResponse.next_page_token of the previous ScheduleService.ListSchedules call.
};
apiInstance.aiplatformProjectsLocationsSchedulesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the Schedules from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the Schedules that match the filter expression. The following fields are supported: * &#x60;display_name&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60;: Supports &#x60;&#x3D;&#x60; and &#x60;!&#x3D;&#x60; comparisons. * &#x60;request&#x60;: Supports existence of the check. (e.g. &#x60;create_pipeline_job_request:*&#x60; --&gt; Schedule has create_pipeline_job_request). * &#x60;create_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;start_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. * &#x60;end_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons and &#x60;:*&#x60; existence check. Values must be in RFC 3339 format. * &#x60;next_run_time&#x60;: Supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&gt;&#x3D;&#x60; comparisons. Values must be in RFC 3339 format. Filter expressions can be combined together using logical operators (&#x60;NOT&#x60;, &#x60;AND&#x60; &amp; &#x60;OR&#x60;). The syntax to define filter expression is based on https://google.aip.dev/160. Examples: * &#x60;state&#x3D;\&quot;ACTIVE\&quot; AND display_name:\&quot;my_schedule_*\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_schedule\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;end_time&gt;\&quot;2021-05-18T00:00:00Z\&quot; OR NOT end_time:*&#x60; * &#x60;create_pipeline_job_request:*&#x60; | [optional] 
 **orderBy** | **String**| A comma-separated list of fields to order by. The default sort order is in ascending order. Use \&quot;desc\&quot; after a field name for descending. You can have multiple order_by fields provided. For example, using \&quot;create_time desc, end_time\&quot; will order results by create time in descending order, and if there are multiple schedules having the same create time, order them by the end time in ascending order. If order_by is not specified, it will order by default with create_time in descending order. Supported fields: * &#x60;create_time&#x60; * &#x60;start_time&#x60; * &#x60;end_time&#x60; * &#x60;next_run_time&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. Default to 100 if not specified. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListSchedulesResponse.next_page_token of the previous ScheduleService.ListSchedules call. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListSchedulesResponse**](GoogleCloudAiplatformV1ListSchedulesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsSchedulesPause

> Object aiplatformProjectsLocationsSchedulesPause(name, opts)



Pauses a Schedule. Will mark Schedule.state to &#39;PAUSED&#39;. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsSchedulesPause(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the Schedule resource to be paused. Format: &#x60;projects/{project}/locations/{location}/schedules/{schedule}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsSchedulesResume

> Object aiplatformProjectsLocationsSchedulesResume(name, opts)



Resumes a paused Schedule to start scheduling new runs. Will mark Schedule.state to &#39;ACTIVE&#39;. Only paused Schedule can be resumed. When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If Schedule.catchUp is set up true, all missed runs will be scheduled for backfill first.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ResumeScheduleRequest': new VertexAiApi.GoogleCloudAiplatformV1ResumeScheduleRequest() // GoogleCloudAiplatformV1ResumeScheduleRequest | 
};
apiInstance.aiplatformProjectsLocationsSchedulesResume(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The name of the Schedule resource to be resumed. Format: &#x60;projects/{project}/locations/{location}/schedules/{schedule}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ResumeScheduleRequest** | [**GoogleCloudAiplatformV1ResumeScheduleRequest**](GoogleCloudAiplatformV1ResumeScheduleRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsSpecialistPoolsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsSpecialistPoolsCreate(parent, opts)



Creates a SpecialistPool.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1SpecialistPool': new VertexAiApi.GoogleCloudAiplatformV1SpecialistPool() // GoogleCloudAiplatformV1SpecialistPool | 
};
apiInstance.aiplatformProjectsLocationsSpecialistPoolsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The parent Project name for the new SpecialistPool. The form is &#x60;projects/{project}/locations/{location}&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1SpecialistPool** | [**GoogleCloudAiplatformV1SpecialistPool**](GoogleCloudAiplatformV1SpecialistPool.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsSpecialistPoolsList

> GoogleCloudAiplatformV1ListSpecialistPoolsResponse aiplatformProjectsLocationsSpecialistPoolsList(parent, opts)



Lists SpecialistPools in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained by ListSpecialistPoolsResponse.next_page_token of the previous SpecialistPoolService.ListSpecialistPools call. Return first page if empty.
  'readMask': "readMask_example" // String | Mask specifying which fields to read. FieldMask represents a set of
};
apiInstance.aiplatformProjectsLocationsSpecialistPoolsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the SpecialistPool&#39;s parent resource. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained by ListSpecialistPoolsResponse.next_page_token of the previous SpecialistPoolService.ListSpecialistPools call. Return first page if empty. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. FieldMask represents a set of | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListSpecialistPoolsResponse**](GoogleCloudAiplatformV1ListSpecialistPoolsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesCreate

> GoogleCloudAiplatformV1Study aiplatformProjectsLocationsStudiesCreate(parent, opts)



Creates a Study. A resource name will be generated after creation of the Study.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the CustomJob in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1Study': new VertexAiApi.GoogleCloudAiplatformV1Study() // GoogleCloudAiplatformV1Study | 
};
apiInstance.aiplatformProjectsLocationsStudiesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the CustomJob in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1Study** | [**GoogleCloudAiplatformV1Study**](GoogleCloudAiplatformV1Study.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Study**](GoogleCloudAiplatformV1Study.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesList

> GoogleCloudAiplatformV1ListStudiesResponse aiplatformProjectsLocationsStudiesList(parent, opts)



Lists all the studies in a region for an associated project.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the Study from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | Optional. The maximum number of studies to return per \"page\" of results. If unspecified, service will pick an appropriate default.
  'pageToken': "pageToken_example" // String | Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages.
};
apiInstance.aiplatformProjectsLocationsStudiesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the Study from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of studies to return per \&quot;page\&quot; of results. If unspecified, service will pick an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListStudiesResponse**](GoogleCloudAiplatformV1ListStudiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesLookup

> GoogleCloudAiplatformV1Study aiplatformProjectsLocationsStudiesLookup(parent, opts)



Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to get the Study from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1LookupStudyRequest': new VertexAiApi.GoogleCloudAiplatformV1LookupStudyRequest() // GoogleCloudAiplatformV1LookupStudyRequest | 
};
apiInstance.aiplatformProjectsLocationsStudiesLookup(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to get the Study from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1LookupStudyRequest** | [**GoogleCloudAiplatformV1LookupStudyRequest**](GoogleCloudAiplatformV1LookupStudyRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Study**](GoogleCloudAiplatformV1Study.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsAddTrialMeasurement

> GoogleCloudAiplatformV1Trial aiplatformProjectsLocationsStudiesTrialsAddTrialMeasurement(trialName, opts)



Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let trialName = "trialName_example"; // String | Required. The name of the trial to add measurement. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1AddTrialMeasurementRequest': new VertexAiApi.GoogleCloudAiplatformV1AddTrialMeasurementRequest() // GoogleCloudAiplatformV1AddTrialMeasurementRequest | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsAddTrialMeasurement(trialName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trialName** | **String**| Required. The name of the trial to add measurement. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1AddTrialMeasurementRequest** | [**GoogleCloudAiplatformV1AddTrialMeasurementRequest**](GoogleCloudAiplatformV1AddTrialMeasurementRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Trial**](GoogleCloudAiplatformV1Trial.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsCheckTrialEarlyStoppingState

> GoogleLongrunningOperation aiplatformProjectsLocationsStudiesTrialsCheckTrialEarlyStoppingState(trialName, opts)



Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let trialName = "trialName_example"; // String | Required. The Trial's name. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsCheckTrialEarlyStoppingState(trialName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trialName** | **String**| Required. The Trial&#39;s name. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsComplete

> GoogleCloudAiplatformV1Trial aiplatformProjectsLocationsStudiesTrialsComplete(name, opts)



Marks a Trial as complete.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The Trial's name. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1CompleteTrialRequest': new VertexAiApi.GoogleCloudAiplatformV1CompleteTrialRequest() // GoogleCloudAiplatformV1CompleteTrialRequest | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsComplete(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The Trial&#39;s name. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1CompleteTrialRequest** | [**GoogleCloudAiplatformV1CompleteTrialRequest**](GoogleCloudAiplatformV1CompleteTrialRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Trial**](GoogleCloudAiplatformV1Trial.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsCreate

> GoogleCloudAiplatformV1Trial aiplatformProjectsLocationsStudiesTrialsCreate(parent, opts)



Adds a user provided Trial to a Study.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Study to create the Trial in. Format: `projects/{project}/locations/{location}/studies/{study}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1Trial': new VertexAiApi.GoogleCloudAiplatformV1Trial() // GoogleCloudAiplatformV1Trial | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Study to create the Trial in. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1Trial** | [**GoogleCloudAiplatformV1Trial**](GoogleCloudAiplatformV1Trial.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Trial**](GoogleCloudAiplatformV1Trial.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsList

> GoogleCloudAiplatformV1ListTrialsResponse aiplatformProjectsLocationsStudiesTrialsList(parent, opts)



Lists the Trials associated with a Study.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Study to list the Trial from. Format: `projects/{project}/locations/{location}/studies/{study}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | Optional. The number of Trials to retrieve per \"page\" of results. If unspecified, the service will pick an appropriate default.
  'pageToken': "pageToken_example" // String | Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages.
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Study to list the Trial from. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| Optional. The number of Trials to retrieve per \&quot;page\&quot; of results. If unspecified, the service will pick an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListTrialsResponse**](GoogleCloudAiplatformV1ListTrialsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsListOptimalTrials

> GoogleCloudAiplatformV1ListOptimalTrialsResponse aiplatformProjectsLocationsStudiesTrialsListOptimalTrials(parent, opts)



Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the Study that the optimal Trial belongs to.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsListOptimalTrials(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The name of the Study that the optimal Trial belongs to. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListOptimalTrialsResponse**](GoogleCloudAiplatformV1ListOptimalTrialsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsStop

> GoogleCloudAiplatformV1Trial aiplatformProjectsLocationsStudiesTrialsStop(name, opts)



Stops a Trial.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Required. The Trial's name. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsStop(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The Trial&#39;s name. Format: &#x60;projects/{project}/locations/{location}/studies/{study}/trials/{trial}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1Trial**](GoogleCloudAiplatformV1Trial.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsStudiesTrialsSuggest

> GoogleLongrunningOperation aiplatformProjectsLocationsStudiesTrialsSuggest(parent, opts)



Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The project and location that the Study belongs to. Format: `projects/{project}/locations/{location}/studies/{study}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1SuggestTrialsRequest': new VertexAiApi.GoogleCloudAiplatformV1SuggestTrialsRequest() // GoogleCloudAiplatformV1SuggestTrialsRequest | 
};
apiInstance.aiplatformProjectsLocationsStudiesTrialsSuggest(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The project and location that the Study belongs to. Format: &#x60;projects/{project}/locations/{location}/studies/{study}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1SuggestTrialsRequest** | [**GoogleCloudAiplatformV1SuggestTrialsRequest**](GoogleCloudAiplatformV1SuggestTrialsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsBatchRead

> GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse aiplatformProjectsLocationsTensorboardsBatchRead(tensorboard, opts)



Reads multiple TensorboardTimeSeries&#39; data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboard = "tensorboard_example"; // String | Required. The resource name of the Tensorboard containing TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`. The TensorboardTimeSeries referenced by time_series must be sub resources of this Tensorboard.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'timeSeries': ["null"] // [String] | Required. The resource names of the TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
};
apiInstance.aiplatformProjectsLocationsTensorboardsBatchRead(tensorboard, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboard** | **String**| Required. The resource name of the Tensorboard containing TensorboardTimeSeries to read data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60;. The TensorboardTimeSeries referenced by time_series must be sub resources of this Tensorboard. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **timeSeries** | [**[String]**](String.md)| Required. The resource names of the TensorboardTimeSeries to read data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60; | [optional] 

### Return type

[**GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse**](GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsCreate

> GoogleLongrunningOperation aiplatformProjectsLocationsTensorboardsCreate(parent, opts)



Creates a Tensorboard.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the Tensorboard in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1Tensorboard': new VertexAiApi.GoogleCloudAiplatformV1Tensorboard() // GoogleCloudAiplatformV1Tensorboard | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the Tensorboard in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1Tensorboard** | [**GoogleCloudAiplatformV1Tensorboard**](GoogleCloudAiplatformV1Tensorboard.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsBatchCreate

> GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse aiplatformProjectsLocationsTensorboardsExperimentsBatchCreate(parent, opts)



Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the TensorboardExperiment to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The TensorboardRuns referenced by the parent fields in the CreateTensorboardTimeSeriesRequest messages must be sub resources of this TensorboardExperiment.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest': new VertexAiApi.GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest() // GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsBatchCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the TensorboardExperiment to create the TensorboardTimeSeries in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; The TensorboardRuns referenced by the parent fields in the CreateTensorboardTimeSeriesRequest messages must be sub resources of this TensorboardExperiment. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest** | [**GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest**](GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse**](GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsCreate

> GoogleCloudAiplatformV1TensorboardExperiment aiplatformProjectsLocationsTensorboardsExperimentsCreate(parent, opts)



Creates a TensorboardExperiment.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Tensorboard to create the TensorboardExperiment in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'tensorboardExperimentId': "tensorboardExperimentId_example", // String | Required. The ID to use for the Tensorboard experiment, which becomes the final component of the Tensorboard experiment's resource name. This value should be 1-128 characters, and valid characters are `/a-z-/`.
  'googleCloudAiplatformV1TensorboardExperiment': new VertexAiApi.GoogleCloudAiplatformV1TensorboardExperiment() // GoogleCloudAiplatformV1TensorboardExperiment | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Tensorboard to create the TensorboardExperiment in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **tensorboardExperimentId** | **String**| Required. The ID to use for the Tensorboard experiment, which becomes the final component of the Tensorboard experiment&#39;s resource name. This value should be 1-128 characters, and valid characters are &#x60;/a-z-/&#x60;. | [optional] 
 **googleCloudAiplatformV1TensorboardExperiment** | [**GoogleCloudAiplatformV1TensorboardExperiment**](GoogleCloudAiplatformV1TensorboardExperiment.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1TensorboardExperiment**](GoogleCloudAiplatformV1TensorboardExperiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsList

> GoogleCloudAiplatformV1ListTensorboardExperimentsResponse aiplatformProjectsLocationsTensorboardsExperimentsList(parent, opts)



Lists TensorboardExperiments in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Tensorboard to list TensorboardExperiments. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the TensorboardExperiments that match the filter expression.
  'orderBy': "orderBy_example", // String | Field to use to sort the list.
  'pageSize': 56, // Number | The maximum number of TensorboardExperiments to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardExperiments are returned. The maximum value is 1000; values above 1000 are coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous TensorboardService.ListTensorboardExperiments call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardExperiments must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Tensorboard to list TensorboardExperiments. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the TensorboardExperiments that match the filter expression. | [optional] 
 **orderBy** | **String**| Field to use to sort the list. | [optional] 
 **pageSize** | **Number**| The maximum number of TensorboardExperiments to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardExperiments are returned. The maximum value is 1000; values above 1000 are coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous TensorboardService.ListTensorboardExperiments call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardExperiments must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListTensorboardExperimentsResponse**](GoogleCloudAiplatformV1ListTensorboardExperimentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsBatchCreate

> GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse aiplatformProjectsLocationsTensorboardsExperimentsRunsBatchCreate(parent, opts)



Batch create TensorboardRuns.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the TensorboardExperiment to create the TensorboardRuns in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The parent field in the CreateTensorboardRunRequest messages must match this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1BatchCreateTensorboardRunsRequest': new VertexAiApi.GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest() // GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsBatchCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the TensorboardExperiment to create the TensorboardRuns in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; The parent field in the CreateTensorboardRunRequest messages must match this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1BatchCreateTensorboardRunsRequest** | [**GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest**](GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse**](GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsCreate

> GoogleCloudAiplatformV1TensorboardRun aiplatformProjectsLocationsTensorboardsExperimentsRunsCreate(parent, opts)



Creates a TensorboardRun.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'tensorboardRunId': "tensorboardRunId_example", // String | Required. The ID to use for the Tensorboard run, which becomes the final component of the Tensorboard run's resource name. This value should be 1-128 characters, and valid characters are `/a-z-/`.
  'googleCloudAiplatformV1TensorboardRun': new VertexAiApi.GoogleCloudAiplatformV1TensorboardRun() // GoogleCloudAiplatformV1TensorboardRun | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **tensorboardRunId** | **String**| Required. The ID to use for the Tensorboard run, which becomes the final component of the Tensorboard run&#39;s resource name. This value should be 1-128 characters, and valid characters are &#x60;/a-z-/&#x60;. | [optional] 
 **googleCloudAiplatformV1TensorboardRun** | [**GoogleCloudAiplatformV1TensorboardRun**](GoogleCloudAiplatformV1TensorboardRun.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1TensorboardRun**](GoogleCloudAiplatformV1TensorboardRun.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsList

> GoogleCloudAiplatformV1ListTensorboardRunsResponse aiplatformProjectsLocationsTensorboardsExperimentsRunsList(parent, opts)



Lists TensorboardRuns in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the TensorboardExperiment to list TensorboardRuns. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the TensorboardRuns that match the filter expression.
  'orderBy': "orderBy_example", // String | Field to use to sort the list.
  'pageSize': 56, // Number | The maximum number of TensorboardRuns to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardRuns are returned. The maximum value is 1000; values above 1000 are coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous TensorboardService.ListTensorboardRuns call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardRuns must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the TensorboardExperiment to list TensorboardRuns. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the TensorboardRuns that match the filter expression. | [optional] 
 **orderBy** | **String**| Field to use to sort the list. | [optional] 
 **pageSize** | **Number**| The maximum number of TensorboardRuns to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardRuns are returned. The maximum value is 1000; values above 1000 are coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous TensorboardService.ListTensorboardRuns call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardRuns must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListTensorboardRunsResponse**](GoogleCloudAiplatformV1ListTensorboardRunsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesCreate

> GoogleCloudAiplatformV1TensorboardTimeSeries aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesCreate(parent, opts)



Creates a TensorboardTimeSeries.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'tensorboardTimeSeriesId': "tensorboardTimeSeriesId_example", // String | Optional. The user specified unique ID to use for the TensorboardTimeSeries, which becomes the final component of the TensorboardTimeSeries's resource name. This value should match \"a-z0-9{0, 127}\"
  'googleCloudAiplatformV1TensorboardTimeSeries': new VertexAiApi.GoogleCloudAiplatformV1TensorboardTimeSeries() // GoogleCloudAiplatformV1TensorboardTimeSeries | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **tensorboardTimeSeriesId** | **String**| Optional. The user specified unique ID to use for the TensorboardTimeSeries, which becomes the final component of the TensorboardTimeSeries&#39;s resource name. This value should match \&quot;a-z0-9{0, 127}\&quot; | [optional] 
 **googleCloudAiplatformV1TensorboardTimeSeries** | [**GoogleCloudAiplatformV1TensorboardTimeSeries**](GoogleCloudAiplatformV1TensorboardTimeSeries.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1TensorboardTimeSeries**](GoogleCloudAiplatformV1TensorboardTimeSeries.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesExportTensorboardTimeSeries

> GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesExportTensorboardTimeSeries(tensorboardTimeSeries, opts)



Exports a TensorboardTimeSeries&#39; data. Data is returned in paginated responses.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboardTimeSeries = "tensorboardTimeSeries_example"; // String | Required. The resource name of the TensorboardTimeSeries to export data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest': new VertexAiApi.GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest() // GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesExportTensorboardTimeSeries(tensorboardTimeSeries, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboardTimeSeries** | **String**| Required. The resource name of the TensorboardTimeSeries to export data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest** | [**GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest**](GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse**](GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesList

> GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesList(parent, opts)



Lists TensorboardTimeSeries in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the TensorboardRun to list TensorboardTimeSeries. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the TensorboardTimeSeries that match the filter expression.
  'orderBy': "orderBy_example", // String | Field to use to sort the list.
  'pageSize': 56, // Number | The maximum number of TensorboardTimeSeries to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardTimeSeries are returned. The maximum value is 1000; values above 1000 are coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous TensorboardService.ListTensorboardTimeSeries call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardTimeSeries must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the TensorboardRun to list TensorboardTimeSeries. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the TensorboardTimeSeries that match the filter expression. | [optional] 
 **orderBy** | **String**| Field to use to sort the list. | [optional] 
 **pageSize** | **Number**| The maximum number of TensorboardTimeSeries to return. The service may return fewer than this value. If unspecified, at most 50 TensorboardTimeSeries are returned. The maximum value is 1000; values above 1000 are coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous TensorboardService.ListTensorboardTimeSeries call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboardTimeSeries must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse**](GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesPatch

> GoogleCloudAiplatformV1TensorboardTimeSeries aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesPatch(name, opts)



Updates a TensorboardTimeSeries.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | Output only. Name of the TensorboardTimeSeries.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | Required. Field mask is used to specify the fields to be overwritten in the TensorboardTimeSeries resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it's in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.
  'googleCloudAiplatformV1TensorboardTimeSeries': new VertexAiApi.GoogleCloudAiplatformV1TensorboardTimeSeries() // GoogleCloudAiplatformV1TensorboardTimeSeries | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesPatch(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Output only. Name of the TensorboardTimeSeries. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| Required. Field mask is used to specify the fields to be overwritten in the TensorboardTimeSeries resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it&#39;s in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified. | [optional] 
 **googleCloudAiplatformV1TensorboardTimeSeries** | [**GoogleCloudAiplatformV1TensorboardTimeSeries**](GoogleCloudAiplatformV1TensorboardTimeSeries.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1TensorboardTimeSeries**](GoogleCloudAiplatformV1TensorboardTimeSeries.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesRead

> GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesRead(tensorboardTimeSeries, opts)



Reads a TensorboardTimeSeries&#39; data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can&#39;t be greater than 10k.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboardTimeSeries = "tensorboardTimeSeries_example"; // String | Required. The resource name of the TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Reads the TensorboardTimeSeries' data that match the filter expression.
  'maxDataPoints': 56 // Number | The maximum number of TensorboardTimeSeries' data to return. This value should be a positive integer. This value can be set to -1 to return all data.
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesRead(tensorboardTimeSeries, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboardTimeSeries** | **String**| Required. The resource name of the TensorboardTimeSeries to read data from. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Reads the TensorboardTimeSeries&#39; data that match the filter expression. | [optional] 
 **maxDataPoints** | **Number**| The maximum number of TensorboardTimeSeries&#39; data to return. This value should be a positive integer. This value can be set to -1 to return all data. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse**](GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesReadBlobData

> GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesReadBlobData(timeSeries, opts)



Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project&#39;s Cloud Storage bucket without users having to obtain Cloud Storage access permission.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let timeSeries = "timeSeries_example"; // String | Required. The resource name of the TensorboardTimeSeries to list Blobs. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'blobIds': ["null"] // [String] | IDs of the blobs to read.
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsTimeSeriesReadBlobData(timeSeries, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeSeries** | **String**| Required. The resource name of the TensorboardTimeSeries to list Blobs. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **blobIds** | [**[String]**](String.md)| IDs of the blobs to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse**](GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsRunsWrite

> Object aiplatformProjectsLocationsTensorboardsExperimentsRunsWrite(tensorboardRun, opts)



Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboardRun = "tensorboardRun_example"; // String | Required. The resource name of the TensorboardRun to write data to. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1WriteTensorboardRunDataRequest': new VertexAiApi.GoogleCloudAiplatformV1WriteTensorboardRunDataRequest() // GoogleCloudAiplatformV1WriteTensorboardRunDataRequest | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsRunsWrite(tensorboardRun, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboardRun** | **String**| Required. The resource name of the TensorboardRun to write data to. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1WriteTensorboardRunDataRequest** | [**GoogleCloudAiplatformV1WriteTensorboardRunDataRequest**](GoogleCloudAiplatformV1WriteTensorboardRunDataRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsExperimentsWrite

> Object aiplatformProjectsLocationsTensorboardsExperimentsWrite(tensorboardExperiment, opts)



Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun&#39;s. If any data fail to be ingested, an error is returned.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboardExperiment = "tensorboardExperiment_example"; // String | Required. The resource name of the TensorboardExperiment to write data to. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1WriteTensorboardExperimentDataRequest': new VertexAiApi.GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest() // GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest | 
};
apiInstance.aiplatformProjectsLocationsTensorboardsExperimentsWrite(tensorboardExperiment, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboardExperiment** | **String**| Required. The resource name of the TensorboardExperiment to write data to. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1WriteTensorboardExperimentDataRequest** | [**GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest**](GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsList

> GoogleCloudAiplatformV1ListTensorboardsResponse aiplatformProjectsLocationsTensorboardsList(parent, opts)



Lists Tensorboards in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list Tensorboards. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Lists the Tensorboards that match the filter expression.
  'orderBy': "orderBy_example", // String | Field to use to sort the list.
  'pageSize': 56, // Number | The maximum number of Tensorboards to return. The service may return fewer than this value. If unspecified, at most 100 Tensorboards are returned. The maximum value is 100; values above 100 are coerced to 100.
  'pageToken': "pageToken_example", // String | A page token, received from a previous TensorboardService.ListTensorboards call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboards must match the call that provided the page token.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsTensorboardsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list Tensorboards. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Lists the Tensorboards that match the filter expression. | [optional] 
 **orderBy** | **String**| Field to use to sort the list. | [optional] 
 **pageSize** | **Number**| The maximum number of Tensorboards to return. The service may return fewer than this value. If unspecified, at most 100 Tensorboards are returned. The maximum value is 100; values above 100 are coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous TensorboardService.ListTensorboards call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to TensorboardService.ListTensorboards must match the call that provided the page token. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListTensorboardsResponse**](GoogleCloudAiplatformV1ListTensorboardsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsReadSize

> GoogleCloudAiplatformV1ReadTensorboardSizeResponse aiplatformProjectsLocationsTensorboardsReadSize(tensorboard, opts)



Returns the storage size for a given TensorBoard instance.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboard = "tensorboard_example"; // String | Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.aiplatformProjectsLocationsTensorboardsReadSize(tensorboard, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboard** | **String**| Required. The name of the Tensorboard resource. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadTensorboardSizeResponse**](GoogleCloudAiplatformV1ReadTensorboardSizeResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTensorboardsReadUsage

> GoogleCloudAiplatformV1ReadTensorboardUsageResponse aiplatformProjectsLocationsTensorboardsReadUsage(tensorboard, opts)



Returns a list of monthly active users for a given TensorBoard instance.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let tensorboard = "tensorboard_example"; // String | Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.aiplatformProjectsLocationsTensorboardsReadUsage(tensorboard, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tensorboard** | **String**| Required. The name of the Tensorboard resource. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleCloudAiplatformV1ReadTensorboardUsageResponse**](GoogleCloudAiplatformV1ReadTensorboardUsageResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTrainingPipelinesCreate

> GoogleCloudAiplatformV1TrainingPipeline aiplatformProjectsLocationsTrainingPipelinesCreate(parent, opts)



Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to create the TrainingPipeline in. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudAiplatformV1TrainingPipeline': new VertexAiApi.GoogleCloudAiplatformV1TrainingPipeline() // GoogleCloudAiplatformV1TrainingPipeline | 
};
apiInstance.aiplatformProjectsLocationsTrainingPipelinesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to create the TrainingPipeline in. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudAiplatformV1TrainingPipeline** | [**GoogleCloudAiplatformV1TrainingPipeline**](GoogleCloudAiplatformV1TrainingPipeline.md)|  | [optional] 

### Return type

[**GoogleCloudAiplatformV1TrainingPipeline**](GoogleCloudAiplatformV1TrainingPipeline.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTrainingPipelinesList

> GoogleCloudAiplatformV1ListTrainingPipelinesResponse aiplatformProjectsLocationsTrainingPipelinesList(parent, opts)



Lists TrainingPipelines in a Location.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the Location to list the TrainingPipelines from. Format: `projects/{project}/locations/{location}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter. Supported fields: * `display_name` supports `=`, `!=` comparisons, and `:` wildcard. * `state` supports `=`, `!=` comparisons. * `training_task_definition` `=`, `!=` comparisons, and `:` wildcard. * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format. * `labels` supports general map functions that is: `labels.key=value` - key:value equality `labels.key:* - key existence Some examples of using the filter are: * `state=\"PIPELINE_STATE_SUCCEEDED\" AND display_name:\"my_pipeline_*\"` * `state!=\"PIPELINE_STATE_FAILED\" OR display_name=\"my_pipeline\"` * `NOT display_name=\"my_pipeline\"` * `create_time>\"2021-05-18T00:00:00Z\"` * `training_task_definition:\"*automl_text_classification*\"`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token. Typically obtained via ListTrainingPipelinesResponse.next_page_token of the previous PipelineService.ListTrainingPipelines call.
  'readMask': "readMask_example" // String | Mask specifying which fields to read.
};
apiInstance.aiplatformProjectsLocationsTrainingPipelinesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The resource name of the Location to list the TrainingPipelines from. Format: &#x60;projects/{project}/locations/{location}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. Supported fields: * &#x60;display_name&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;state&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons. * &#x60;training_task_definition&#x60; &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; comparisons, and &#x60;:&#x60; wildcard. * &#x60;create_time&#x60; supports &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;,&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;,&#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60; comparisons. &#x60;create_time&#x60; must be in RFC 3339 format. * &#x60;labels&#x60; supports general map functions that is: &#x60;labels.key&#x3D;value&#x60; - key:value equality &#x60;labels.key:* - key existence Some examples of using the filter are: * &#x60;state&#x3D;\&quot;PIPELINE_STATE_SUCCEEDED\&quot; AND display_name:\&quot;my_pipeline_*\&quot;&#x60; * &#x60;state!&#x3D;\&quot;PIPELINE_STATE_FAILED\&quot; OR display_name&#x3D;\&quot;my_pipeline\&quot;&#x60; * &#x60;NOT display_name&#x3D;\&quot;my_pipeline\&quot;&#x60; * &#x60;create_time&gt;\&quot;2021-05-18T00:00:00Z\&quot;&#x60; * &#x60;training_task_definition:\&quot;*automl_text_classification*\&quot;&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. Typically obtained via ListTrainingPipelinesResponse.next_page_token of the previous PipelineService.ListTrainingPipelines call. | [optional] 
 **readMask** | **String**| Mask specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1ListTrainingPipelinesResponse**](GoogleCloudAiplatformV1ListTrainingPipelinesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTrainingPipelinesOperationsCancel

> Object aiplatformProjectsLocationsTrainingPipelinesOperationsCancel(name, opts)



Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation resource to be cancelled.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.aiplatformProjectsLocationsTrainingPipelinesOperationsCancel(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of the operation resource to be cancelled. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aiplatformProjectsLocationsTrainingPipelinesOperationsDelete

> Object aiplatformProjectsLocationsTrainingPipelinesOperationsDelete(name, opts)



Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation resource to be deleted.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'force': true // Boolean | If set to true, any specialist managers in this SpecialistPool will also be deleted. (Otherwise, the request will only work if the SpecialistPool has no specialist managers.)
};
apiInstance.aiplatformProjectsLocationsTrainingPipelinesOperationsDelete(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of the operation resource to be deleted. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **force** | **Boolean**| If set to true, any specialist managers in this SpecialistPool will also be deleted. (Otherwise, the request will only work if the SpecialistPool has no specialist managers.) | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTrainingPipelinesOperationsList

> GoogleLongrunningListOperationsResponse aiplatformProjectsLocationsTrainingPipelinesOperationsList(name, opts)



Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation's parent resource.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example" // String | The standard list page token.
};
apiInstance.aiplatformProjectsLocationsTrainingPipelinesOperationsList(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of the operation&#39;s parent resource. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 

### Return type

[**GoogleLongrunningListOperationsResponse**](GoogleLongrunningListOperationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformProjectsLocationsTrainingPipelinesOperationsWait

> GoogleLongrunningOperation aiplatformProjectsLocationsTrainingPipelinesOperationsWait(name, opts)



Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. If the operation is already done, the latest state is immediately returned. If the timeout specified is greater than the default HTTP/RPC timeout, the HTTP/RPC timeout is used. If the server does not support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Note that this method is on a best-effort basis. It may return the latest state before the specified timeout (including immediately), meaning even an immediate response is no guarantee that the operation is done.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation resource to wait on.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'timeout': "timeout_example" // String | The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used.
};
apiInstance.aiplatformProjectsLocationsTrainingPipelinesOperationsWait(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of the operation resource to wait on. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **timeout** | **String**| The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used. | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

