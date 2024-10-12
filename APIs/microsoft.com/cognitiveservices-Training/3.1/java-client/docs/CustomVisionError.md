

# CustomVisionError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The error code. |  |
|**message** | **String** | A message explaining the error reported by the service. |  |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NO_ERROR | &quot;NoError&quot; |
| BAD_REQUEST | &quot;BadRequest&quot; |
| BAD_REQUEST_EXCEEDED_BATCH_SIZE | &quot;BadRequestExceededBatchSize&quot; |
| BAD_REQUEST_NOT_SUPPORTED | &quot;BadRequestNotSupported&quot; |
| BAD_REQUEST_INVALID_IDS | &quot;BadRequestInvalidIds&quot; |
| BAD_REQUEST_PROJECT_NAME | &quot;BadRequestProjectName&quot; |
| BAD_REQUEST_PROJECT_NAME_NOT_UNIQUE | &quot;BadRequestProjectNameNotUnique&quot; |
| BAD_REQUEST_PROJECT_DESCRIPTION | &quot;BadRequestProjectDescription&quot; |
| BAD_REQUEST_PROJECT_UNKNOWN_DOMAIN | &quot;BadRequestProjectUnknownDomain&quot; |
| BAD_REQUEST_PROJECT_UNKNOWN_CLASSIFICATION | &quot;BadRequestProjectUnknownClassification&quot; |
| BAD_REQUEST_PROJECT_UNSUPPORTED_DOMAIN_TYPE_CHANGE | &quot;BadRequestProjectUnsupportedDomainTypeChange&quot; |
| BAD_REQUEST_PROJECT_UNSUPPORTED_EXPORT_PLATFORM | &quot;BadRequestProjectUnsupportedExportPlatform&quot; |
| BAD_REQUEST_PROJECT_IMAGE_PREPROCESSING_SETTINGS | &quot;BadRequestProjectImagePreprocessingSettings&quot; |
| BAD_REQUEST_ITERATION_NAME | &quot;BadRequestIterationName&quot; |
| BAD_REQUEST_ITERATION_NAME_NOT_UNIQUE | &quot;BadRequestIterationNameNotUnique&quot; |
| BAD_REQUEST_ITERATION_DESCRIPTION | &quot;BadRequestIterationDescription&quot; |
| BAD_REQUEST_ITERATION_IS_NOT_TRAINED | &quot;BadRequestIterationIsNotTrained&quot; |
| BAD_REQUEST_WORKSPACE_CANNOT_BE_MODIFIED | &quot;BadRequestWorkspaceCannotBeModified&quot; |
| BAD_REQUEST_WORKSPACE_NOT_DELETABLE | &quot;BadRequestWorkspaceNotDeletable&quot; |
| BAD_REQUEST_TAG_NAME | &quot;BadRequestTagName&quot; |
| BAD_REQUEST_TAG_NAME_NOT_UNIQUE | &quot;BadRequestTagNameNotUnique&quot; |
| BAD_REQUEST_TAG_DESCRIPTION | &quot;BadRequestTagDescription&quot; |
| BAD_REQUEST_TAG_TYPE | &quot;BadRequestTagType&quot; |
| BAD_REQUEST_MULTIPLE_NEGATIVE_TAG | &quot;BadRequestMultipleNegativeTag&quot; |
| BAD_REQUEST_IMAGE_TAGS | &quot;BadRequestImageTags&quot; |
| BAD_REQUEST_IMAGE_REGIONS | &quot;BadRequestImageRegions&quot; |
| BAD_REQUEST_NEGATIVE_AND_REGULAR_TAG_ON_SAME_IMAGE | &quot;BadRequestNegativeAndRegularTagOnSameImage&quot; |
| BAD_REQUEST_REQUIRED_PARAM_IS_NULL | &quot;BadRequestRequiredParamIsNull&quot; |
| BAD_REQUEST_ITERATION_IS_PUBLISHED | &quot;BadRequestIterationIsPublished&quot; |
| BAD_REQUEST_INVALID_PUBLISH_NAME | &quot;BadRequestInvalidPublishName&quot; |
| BAD_REQUEST_INVALID_PUBLISH_TARGET | &quot;BadRequestInvalidPublishTarget&quot; |
| BAD_REQUEST_UNPUBLISH_FAILED | &quot;BadRequestUnpublishFailed&quot; |
| BAD_REQUEST_ITERATION_NOT_PUBLISHED | &quot;BadRequestIterationNotPublished&quot; |
| BAD_REQUEST_SUBSCRIPTION_API | &quot;BadRequestSubscriptionApi&quot; |
| BAD_REQUEST_EXCEED_PROJECT_LIMIT | &quot;BadRequestExceedProjectLimit&quot; |
| BAD_REQUEST_EXCEED_ITERATION_PER_PROJECT_LIMIT | &quot;BadRequestExceedIterationPerProjectLimit&quot; |
| BAD_REQUEST_EXCEED_TAG_PER_PROJECT_LIMIT | &quot;BadRequestExceedTagPerProjectLimit&quot; |
| BAD_REQUEST_EXCEED_TAG_PER_IMAGE_LIMIT | &quot;BadRequestExceedTagPerImageLimit&quot; |
| BAD_REQUEST_EXCEEDED_QUOTA | &quot;BadRequestExceededQuota&quot; |
| BAD_REQUEST_CANNOT_MIGRATE_PROJECT_WITH_NAME | &quot;BadRequestCannotMigrateProjectWithName&quot; |
| BAD_REQUEST_NOT_LIMITED_TRIAL | &quot;BadRequestNotLimitedTrial&quot; |
| BAD_REQUEST_IMAGE_BATCH | &quot;BadRequestImageBatch&quot; |
| BAD_REQUEST_IMAGE_STREAM | &quot;BadRequestImageStream&quot; |
| BAD_REQUEST_IMAGE_URL | &quot;BadRequestImageUrl&quot; |
| BAD_REQUEST_IMAGE_FORMAT | &quot;BadRequestImageFormat&quot; |
| BAD_REQUEST_IMAGE_SIZE_BYTES | &quot;BadRequestImageSizeBytes&quot; |
| BAD_REQUEST_IMAGE_EXCEEDED_COUNT | &quot;BadRequestImageExceededCount&quot; |
| BAD_REQUEST_TRAINING_NOT_NEEDED | &quot;BadRequestTrainingNotNeeded&quot; |
| BAD_REQUEST_TRAINING_NOT_NEEDED_BUT_TRAINING_PIPELINE_UPDATED | &quot;BadRequestTrainingNotNeededButTrainingPipelineUpdated&quot; |
| BAD_REQUEST_TRAINING_VALIDATION_FAILED | &quot;BadRequestTrainingValidationFailed&quot; |
| BAD_REQUEST_CLASSIFICATION_TRAINING_VALIDATION_FAILED | &quot;BadRequestClassificationTrainingValidationFailed&quot; |
| BAD_REQUEST_MULTI_CLASS_CLASSIFICATION_TRAINING_VALIDATION_FAILED | &quot;BadRequestMultiClassClassificationTrainingValidationFailed&quot; |
| BAD_REQUEST_MULTI_LABEL_CLASSIFICATION_TRAINING_VALIDATION_FAILED | &quot;BadRequestMultiLabelClassificationTrainingValidationFailed&quot; |
| BAD_REQUEST_DETECTION_TRAINING_VALIDATION_FAILED | &quot;BadRequestDetectionTrainingValidationFailed&quot; |
| BAD_REQUEST_TRAINING_ALREADY_IN_PROGRESS | &quot;BadRequestTrainingAlreadyInProgress&quot; |
| BAD_REQUEST_DETECTION_TRAINING_NOT_ALLOW_NEGATIVE_TAG | &quot;BadRequestDetectionTrainingNotAllowNegativeTag&quot; |
| BAD_REQUEST_INVALID_EMAIL_ADDRESS | &quot;BadRequestInvalidEmailAddress&quot; |
| BAD_REQUEST_DOMAIN_NOT_SUPPORTED_FOR_ADVANCED_TRAINING | &quot;BadRequestDomainNotSupportedForAdvancedTraining&quot; |
| BAD_REQUEST_EXPORT_PLATFORM_NOT_SUPPORTED_FOR_ADVANCED_TRAINING | &quot;BadRequestExportPlatformNotSupportedForAdvancedTraining&quot; |
| BAD_REQUEST_RESERVED_BUDGET_IN_HOURS_NOT_ENOUGH_FOR_ADVANCED_TRAINING | &quot;BadRequestReservedBudgetInHoursNotEnoughForAdvancedTraining&quot; |
| BAD_REQUEST_EXPORT_VALIDATION_FAILED | &quot;BadRequestExportValidationFailed&quot; |
| BAD_REQUEST_EXPORT_ALREADY_IN_PROGRESS | &quot;BadRequestExportAlreadyInProgress&quot; |
| BAD_REQUEST_PREDICTION_IDS_MISSING | &quot;BadRequestPredictionIdsMissing&quot; |
| BAD_REQUEST_PREDICTION_IDS_EXCEEDED_COUNT | &quot;BadRequestPredictionIdsExceededCount&quot; |
| BAD_REQUEST_PREDICTION_TAGS_EXCEEDED_COUNT | &quot;BadRequestPredictionTagsExceededCount&quot; |
| BAD_REQUEST_PREDICTION_RESULTS_EXCEEDED_COUNT | &quot;BadRequestPredictionResultsExceededCount&quot; |
| BAD_REQUEST_PREDICTION_INVALID_APPLICATION_NAME | &quot;BadRequestPredictionInvalidApplicationName&quot; |
| BAD_REQUEST_PREDICTION_INVALID_QUERY_PARAMETERS | &quot;BadRequestPredictionInvalidQueryParameters&quot; |
| BAD_REQUEST_INVALID | &quot;BadRequestInvalid&quot; |
| UNSUPPORTED_MEDIA_TYPE | &quot;UnsupportedMediaType&quot; |
| FORBIDDEN | &quot;Forbidden&quot; |
| FORBIDDEN_USER | &quot;ForbiddenUser&quot; |
| FORBIDDEN_USER_RESOURCE | &quot;ForbiddenUserResource&quot; |
| FORBIDDEN_USER_SIGNUP_DISABLED | &quot;ForbiddenUserSignupDisabled&quot; |
| FORBIDDEN_USER_SIGNUP_ALLOWANCE_EXCEEDED | &quot;ForbiddenUserSignupAllowanceExceeded&quot; |
| FORBIDDEN_USER_DOES_NOT_EXIST | &quot;ForbiddenUserDoesNotExist&quot; |
| FORBIDDEN_USER_DISABLED | &quot;ForbiddenUserDisabled&quot; |
| FORBIDDEN_USER_INSUFFICIENT_CAPABILITY | &quot;ForbiddenUserInsufficientCapability&quot; |
| FORBIDDEN_DR_MODE_ENABLED | &quot;ForbiddenDRModeEnabled&quot; |
| FORBIDDEN_INVALID | &quot;ForbiddenInvalid&quot; |
| NOT_FOUND | &quot;NotFound&quot; |
| NOT_FOUND_PROJECT | &quot;NotFoundProject&quot; |
| NOT_FOUND_PROJECT_DEFAULT_ITERATION | &quot;NotFoundProjectDefaultIteration&quot; |
| NOT_FOUND_ITERATION | &quot;NotFoundIteration&quot; |
| NOT_FOUND_ITERATION_PERFORMANCE | &quot;NotFoundIterationPerformance&quot; |
| NOT_FOUND_TAG | &quot;NotFoundTag&quot; |
| NOT_FOUND_IMAGE | &quot;NotFoundImage&quot; |
| NOT_FOUND_DOMAIN | &quot;NotFoundDomain&quot; |
| NOT_FOUND_APIM_SUBSCRIPTION | &quot;NotFoundApimSubscription&quot; |
| NOT_FOUND_INVALID | &quot;NotFoundInvalid&quot; |
| CONFLICT | &quot;Conflict&quot; |
| CONFLICT_INVALID | &quot;ConflictInvalid&quot; |
| ERROR_UNKNOWN | &quot;ErrorUnknown&quot; |
| ERROR_PROJECT_INVALID_WORKSPACE | &quot;ErrorProjectInvalidWorkspace&quot; |
| ERROR_PROJECT_INVALID_PIPELINE_CONFIGURATION | &quot;ErrorProjectInvalidPipelineConfiguration&quot; |
| ERROR_PROJECT_INVALID_DOMAIN | &quot;ErrorProjectInvalidDomain&quot; |
| ERROR_PROJECT_TRAINING_REQUEST_FAILED | &quot;ErrorProjectTrainingRequestFailed&quot; |
| ERROR_PROJECT_EXPORT_REQUEST_FAILED | &quot;ErrorProjectExportRequestFailed&quot; |
| ERROR_FEATURIZATION_SERVICE_UNAVAILABLE | &quot;ErrorFeaturizationServiceUnavailable&quot; |
| ERROR_FEATURIZATION_QUEUE_TIMEOUT | &quot;ErrorFeaturizationQueueTimeout&quot; |
| ERROR_FEATURIZATION_INVALID_FEATURIZER | &quot;ErrorFeaturizationInvalidFeaturizer&quot; |
| ERROR_FEATURIZATION_AUGMENTATION_UNAVAILABLE | &quot;ErrorFeaturizationAugmentationUnavailable&quot; |
| ERROR_FEATURIZATION_UNRECOGNIZED_JOB | &quot;ErrorFeaturizationUnrecognizedJob&quot; |
| ERROR_FEATURIZATION_AUGMENTATION_ERROR | &quot;ErrorFeaturizationAugmentationError&quot; |
| ERROR_EXPORTER_INVALID_PLATFORM | &quot;ErrorExporterInvalidPlatform&quot; |
| ERROR_EXPORTER_INVALID_FEATURIZER | &quot;ErrorExporterInvalidFeaturizer&quot; |
| ERROR_EXPORTER_INVALID_CLASSIFIER | &quot;ErrorExporterInvalidClassifier&quot; |
| ERROR_PREDICTION_SERVICE_UNAVAILABLE | &quot;ErrorPredictionServiceUnavailable&quot; |
| ERROR_PREDICTION_MODEL_NOT_FOUND | &quot;ErrorPredictionModelNotFound&quot; |
| ERROR_PREDICTION_MODEL_NOT_CACHED | &quot;ErrorPredictionModelNotCached&quot; |
| ERROR_PREDICTION | &quot;ErrorPrediction&quot; |
| ERROR_PREDICTION_STORAGE | &quot;ErrorPredictionStorage&quot; |
| ERROR_REGION_PROPOSAL | &quot;ErrorRegionProposal&quot; |
| ERROR_INVALID | &quot;ErrorInvalid&quot; |



