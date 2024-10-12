# CloudDatastoreApi.GoogleDatastoreAdminV1MigrationProgressEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prepareStepDetails** | [**GoogleDatastoreAdminV1PrepareStepDetails**](GoogleDatastoreAdminV1PrepareStepDetails.md) |  | [optional] 
**redirectWritesStepDetails** | [**GoogleDatastoreAdminV1RedirectWritesStepDetails**](GoogleDatastoreAdminV1RedirectWritesStepDetails.md) |  | [optional] 
**step** | **String** | The step that is starting. An event with step set to &#x60;START&#x60; indicates that the migration has been reverted back to the initial pre-migration state. | [optional] 



## Enum: StepEnum


* `MIGRATION_STEP_UNSPECIFIED` (value: `"MIGRATION_STEP_UNSPECIFIED"`)

* `PREPARE` (value: `"PREPARE"`)

* `START` (value: `"START"`)

* `APPLY_WRITES_SYNCHRONOUSLY` (value: `"APPLY_WRITES_SYNCHRONOUSLY"`)

* `COPY_AND_VERIFY` (value: `"COPY_AND_VERIFY"`)

* `REDIRECT_EVENTUALLY_CONSISTENT_READS` (value: `"REDIRECT_EVENTUALLY_CONSISTENT_READS"`)

* `REDIRECT_STRONGLY_CONSISTENT_READS` (value: `"REDIRECT_STRONGLY_CONSISTENT_READS"`)

* `REDIRECT_WRITES` (value: `"REDIRECT_WRITES"`)




