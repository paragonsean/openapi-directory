# CustomVisionTrainingClient.CustomVisionError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The error code. | 
**message** | **String** | A message explaining the error reported by the service. | 



## Enum: CodeEnum


* `NoError` (value: `"NoError"`)

* `BadRequest` (value: `"BadRequest"`)

* `BadRequestExceededBatchSize` (value: `"BadRequestExceededBatchSize"`)

* `BadRequestNotSupported` (value: `"BadRequestNotSupported"`)

* `BadRequestInvalidIds` (value: `"BadRequestInvalidIds"`)

* `BadRequestProjectName` (value: `"BadRequestProjectName"`)

* `BadRequestProjectNameNotUnique` (value: `"BadRequestProjectNameNotUnique"`)

* `BadRequestProjectDescription` (value: `"BadRequestProjectDescription"`)

* `BadRequestProjectUnknownDomain` (value: `"BadRequestProjectUnknownDomain"`)

* `BadRequestProjectUnknownClassification` (value: `"BadRequestProjectUnknownClassification"`)

* `BadRequestProjectUnsupportedDomainTypeChange` (value: `"BadRequestProjectUnsupportedDomainTypeChange"`)

* `BadRequestProjectUnsupportedExportPlatform` (value: `"BadRequestProjectUnsupportedExportPlatform"`)

* `BadRequestProjectImagePreprocessingSettings` (value: `"BadRequestProjectImagePreprocessingSettings"`)

* `BadRequestProjectDuplicated` (value: `"BadRequestProjectDuplicated"`)

* `BadRequestIterationName` (value: `"BadRequestIterationName"`)

* `BadRequestIterationNameNotUnique` (value: `"BadRequestIterationNameNotUnique"`)

* `BadRequestIterationDescription` (value: `"BadRequestIterationDescription"`)

* `BadRequestIterationIsNotTrained` (value: `"BadRequestIterationIsNotTrained"`)

* `BadRequestIterationValidationFailed` (value: `"BadRequestIterationValidationFailed"`)

* `BadRequestWorkspaceCannotBeModified` (value: `"BadRequestWorkspaceCannotBeModified"`)

* `BadRequestWorkspaceNotDeletable` (value: `"BadRequestWorkspaceNotDeletable"`)

* `BadRequestTagName` (value: `"BadRequestTagName"`)

* `BadRequestTagNameNotUnique` (value: `"BadRequestTagNameNotUnique"`)

* `BadRequestTagDescription` (value: `"BadRequestTagDescription"`)

* `BadRequestTagType` (value: `"BadRequestTagType"`)

* `BadRequestMultipleNegativeTag` (value: `"BadRequestMultipleNegativeTag"`)

* `BadRequestImageTags` (value: `"BadRequestImageTags"`)

* `BadRequestImageRegions` (value: `"BadRequestImageRegions"`)

* `BadRequestNegativeAndRegularTagOnSameImage` (value: `"BadRequestNegativeAndRegularTagOnSameImage"`)

* `BadRequestRequiredParamIsNull` (value: `"BadRequestRequiredParamIsNull"`)

* `BadRequestIterationIsPublished` (value: `"BadRequestIterationIsPublished"`)

* `BadRequestInvalidPublishName` (value: `"BadRequestInvalidPublishName"`)

* `BadRequestInvalidPublishTarget` (value: `"BadRequestInvalidPublishTarget"`)

* `BadRequestUnpublishFailed` (value: `"BadRequestUnpublishFailed"`)

* `BadRequestIterationNotPublished` (value: `"BadRequestIterationNotPublished"`)

* `BadRequestSubscriptionApi` (value: `"BadRequestSubscriptionApi"`)

* `BadRequestExceedProjectLimit` (value: `"BadRequestExceedProjectLimit"`)

* `BadRequestExceedIterationPerProjectLimit` (value: `"BadRequestExceedIterationPerProjectLimit"`)

* `BadRequestExceedTagPerProjectLimit` (value: `"BadRequestExceedTagPerProjectLimit"`)

* `BadRequestExceedTagPerImageLimit` (value: `"BadRequestExceedTagPerImageLimit"`)

* `BadRequestExceededQuota` (value: `"BadRequestExceededQuota"`)

* `BadRequestCannotMigrateProjectWithName` (value: `"BadRequestCannotMigrateProjectWithName"`)

* `BadRequestNotLimitedTrial` (value: `"BadRequestNotLimitedTrial"`)

* `BadRequestImageBatch` (value: `"BadRequestImageBatch"`)

* `BadRequestImageStream` (value: `"BadRequestImageStream"`)

* `BadRequestImageUrl` (value: `"BadRequestImageUrl"`)

* `BadRequestImageFormat` (value: `"BadRequestImageFormat"`)

* `BadRequestImageSizeBytes` (value: `"BadRequestImageSizeBytes"`)

* `BadRequestImageExceededCount` (value: `"BadRequestImageExceededCount"`)

* `BadRequestTrainingNotNeeded` (value: `"BadRequestTrainingNotNeeded"`)

* `BadRequestTrainingNotNeededButTrainingPipelineUpdated` (value: `"BadRequestTrainingNotNeededButTrainingPipelineUpdated"`)

* `BadRequestTrainingValidationFailed` (value: `"BadRequestTrainingValidationFailed"`)

* `BadRequestClassificationTrainingValidationFailed` (value: `"BadRequestClassificationTrainingValidationFailed"`)

* `BadRequestMultiClassClassificationTrainingValidationFailed` (value: `"BadRequestMultiClassClassificationTrainingValidationFailed"`)

* `BadRequestMultiLabelClassificationTrainingValidationFailed` (value: `"BadRequestMultiLabelClassificationTrainingValidationFailed"`)

* `BadRequestDetectionTrainingValidationFailed` (value: `"BadRequestDetectionTrainingValidationFailed"`)

* `BadRequestTrainingAlreadyInProgress` (value: `"BadRequestTrainingAlreadyInProgress"`)

* `BadRequestDetectionTrainingNotAllowNegativeTag` (value: `"BadRequestDetectionTrainingNotAllowNegativeTag"`)

* `BadRequestInvalidEmailAddress` (value: `"BadRequestInvalidEmailAddress"`)

* `BadRequestDomainNotSupportedForAdvancedTraining` (value: `"BadRequestDomainNotSupportedForAdvancedTraining"`)

* `BadRequestExportPlatformNotSupportedForAdvancedTraining` (value: `"BadRequestExportPlatformNotSupportedForAdvancedTraining"`)

* `BadRequestReservedBudgetInHoursNotEnoughForAdvancedTraining` (value: `"BadRequestReservedBudgetInHoursNotEnoughForAdvancedTraining"`)

* `BadRequestExportValidationFailed` (value: `"BadRequestExportValidationFailed"`)

* `BadRequestExportAlreadyInProgress` (value: `"BadRequestExportAlreadyInProgress"`)

* `BadRequestPredictionIdsMissing` (value: `"BadRequestPredictionIdsMissing"`)

* `BadRequestPredictionIdsExceededCount` (value: `"BadRequestPredictionIdsExceededCount"`)

* `BadRequestPredictionTagsExceededCount` (value: `"BadRequestPredictionTagsExceededCount"`)

* `BadRequestPredictionResultsExceededCount` (value: `"BadRequestPredictionResultsExceededCount"`)

* `BadRequestPredictionInvalidApplicationName` (value: `"BadRequestPredictionInvalidApplicationName"`)

* `BadRequestPredictionInvalidQueryParameters` (value: `"BadRequestPredictionInvalidQueryParameters"`)

* `BadRequestInvalidImportToken` (value: `"BadRequestInvalidImportToken"`)

* `BadRequestExportWhileTraining` (value: `"BadRequestExportWhileTraining"`)

* `BadRequestInvalid` (value: `"BadRequestInvalid"`)

* `UnsupportedMediaType` (value: `"UnsupportedMediaType"`)

* `Forbidden` (value: `"Forbidden"`)

* `ForbiddenUser` (value: `"ForbiddenUser"`)

* `ForbiddenUserResource` (value: `"ForbiddenUserResource"`)

* `ForbiddenUserSignupDisabled` (value: `"ForbiddenUserSignupDisabled"`)

* `ForbiddenUserSignupAllowanceExceeded` (value: `"ForbiddenUserSignupAllowanceExceeded"`)

* `ForbiddenUserDoesNotExist` (value: `"ForbiddenUserDoesNotExist"`)

* `ForbiddenUserDisabled` (value: `"ForbiddenUserDisabled"`)

* `ForbiddenUserInsufficientCapability` (value: `"ForbiddenUserInsufficientCapability"`)

* `ForbiddenDRModeEnabled` (value: `"ForbiddenDRModeEnabled"`)

* `ForbiddenInvalid` (value: `"ForbiddenInvalid"`)

* `NotFound` (value: `"NotFound"`)

* `NotFoundProject` (value: `"NotFoundProject"`)

* `NotFoundProjectDefaultIteration` (value: `"NotFoundProjectDefaultIteration"`)

* `NotFoundIteration` (value: `"NotFoundIteration"`)

* `NotFoundIterationPerformance` (value: `"NotFoundIterationPerformance"`)

* `NotFoundTag` (value: `"NotFoundTag"`)

* `NotFoundImage` (value: `"NotFoundImage"`)

* `NotFoundDomain` (value: `"NotFoundDomain"`)

* `NotFoundApimSubscription` (value: `"NotFoundApimSubscription"`)

* `NotFoundInvalid` (value: `"NotFoundInvalid"`)

* `Conflict` (value: `"Conflict"`)

* `ConflictInvalid` (value: `"ConflictInvalid"`)

* `ErrorUnknown` (value: `"ErrorUnknown"`)

* `ErrorIterationCopyFailed` (value: `"ErrorIterationCopyFailed"`)

* `ErrorPreparePerformanceMigrationFailed` (value: `"ErrorPreparePerformanceMigrationFailed"`)

* `ErrorProjectInvalidWorkspace` (value: `"ErrorProjectInvalidWorkspace"`)

* `ErrorProjectInvalidPipelineConfiguration` (value: `"ErrorProjectInvalidPipelineConfiguration"`)

* `ErrorProjectInvalidDomain` (value: `"ErrorProjectInvalidDomain"`)

* `ErrorProjectTrainingRequestFailed` (value: `"ErrorProjectTrainingRequestFailed"`)

* `ErrorProjectImportRequestFailed` (value: `"ErrorProjectImportRequestFailed"`)

* `ErrorProjectExportRequestFailed` (value: `"ErrorProjectExportRequestFailed"`)

* `ErrorFeaturizationServiceUnavailable` (value: `"ErrorFeaturizationServiceUnavailable"`)

* `ErrorFeaturizationQueueTimeout` (value: `"ErrorFeaturizationQueueTimeout"`)

* `ErrorFeaturizationInvalidFeaturizer` (value: `"ErrorFeaturizationInvalidFeaturizer"`)

* `ErrorFeaturizationAugmentationUnavailable` (value: `"ErrorFeaturizationAugmentationUnavailable"`)

* `ErrorFeaturizationUnrecognizedJob` (value: `"ErrorFeaturizationUnrecognizedJob"`)

* `ErrorFeaturizationAugmentationError` (value: `"ErrorFeaturizationAugmentationError"`)

* `ErrorExporterInvalidPlatform` (value: `"ErrorExporterInvalidPlatform"`)

* `ErrorExporterInvalidFeaturizer` (value: `"ErrorExporterInvalidFeaturizer"`)

* `ErrorExporterInvalidClassifier` (value: `"ErrorExporterInvalidClassifier"`)

* `ErrorPredictionServiceUnavailable` (value: `"ErrorPredictionServiceUnavailable"`)

* `ErrorPredictionModelNotFound` (value: `"ErrorPredictionModelNotFound"`)

* `ErrorPredictionModelNotCached` (value: `"ErrorPredictionModelNotCached"`)

* `ErrorPrediction` (value: `"ErrorPrediction"`)

* `ErrorPredictionStorage` (value: `"ErrorPredictionStorage"`)

* `ErrorRegionProposal` (value: `"ErrorRegionProposal"`)

* `ErrorInvalid` (value: `"ErrorInvalid"`)




