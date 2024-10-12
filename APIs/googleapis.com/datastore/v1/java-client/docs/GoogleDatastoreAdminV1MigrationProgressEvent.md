

# GoogleDatastoreAdminV1MigrationProgressEvent

An event signifying the start of a new step in a [migration from Cloud Datastore to Cloud Firestore in Datastore mode](https://cloud.google.com/datastore/docs/upgrade-to-firestore).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**prepareStepDetails** | [**GoogleDatastoreAdminV1PrepareStepDetails**](GoogleDatastoreAdminV1PrepareStepDetails.md) |  |  [optional] |
|**redirectWritesStepDetails** | [**GoogleDatastoreAdminV1RedirectWritesStepDetails**](GoogleDatastoreAdminV1RedirectWritesStepDetails.md) |  |  [optional] |
|**step** | [**StepEnum**](#StepEnum) | The step that is starting. An event with step set to &#x60;START&#x60; indicates that the migration has been reverted back to the initial pre-migration state. |  [optional] |



## Enum: StepEnum

| Name | Value |
|---- | -----|
| MIGRATION_STEP_UNSPECIFIED | &quot;MIGRATION_STEP_UNSPECIFIED&quot; |
| PREPARE | &quot;PREPARE&quot; |
| START | &quot;START&quot; |
| APPLY_WRITES_SYNCHRONOUSLY | &quot;APPLY_WRITES_SYNCHRONOUSLY&quot; |
| COPY_AND_VERIFY | &quot;COPY_AND_VERIFY&quot; |
| REDIRECT_EVENTUALLY_CONSISTENT_READS | &quot;REDIRECT_EVENTUALLY_CONSISTENT_READS&quot; |
| REDIRECT_STRONGLY_CONSISTENT_READS | &quot;REDIRECT_STRONGLY_CONSISTENT_READS&quot; |
| REDIRECT_WRITES | &quot;REDIRECT_WRITES&quot; |



