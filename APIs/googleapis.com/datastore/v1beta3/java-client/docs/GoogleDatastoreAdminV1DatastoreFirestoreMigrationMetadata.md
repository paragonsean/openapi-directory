

# GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadata

Metadata for Datastore to Firestore migration operations. The DatastoreFirestoreMigration operation is not started by the end-user via an explicit \"creation\" method. This is an intentional deviation from the LRO design pattern. This singleton resource can be accessed at: \"projects/{project_id}/operations/datastore-firestore-migration\"

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**migrationState** | [**MigrationStateEnum**](#MigrationStateEnum) | The current state of migration from Cloud Datastore to Cloud Firestore in Datastore mode. |  [optional] |
|**migrationStep** | [**MigrationStepEnum**](#MigrationStepEnum) | The current step of migration from Cloud Datastore to Cloud Firestore in Datastore mode. |  [optional] |



## Enum: MigrationStateEnum

| Name | Value |
|---- | -----|
| MIGRATION_STATE_UNSPECIFIED | &quot;MIGRATION_STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| PAUSED | &quot;PAUSED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



## Enum: MigrationStepEnum

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



