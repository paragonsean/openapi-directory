# CloudDatastoreApi.GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrationState** | **String** | The current state of migration from Cloud Datastore to Cloud Firestore in Datastore mode. | [optional] 
**migrationStep** | **String** | The current step of migration from Cloud Datastore to Cloud Firestore in Datastore mode. | [optional] 



## Enum: MigrationStateEnum


* `MIGRATION_STATE_UNSPECIFIED` (value: `"MIGRATION_STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `PAUSED` (value: `"PAUSED"`)

* `COMPLETE` (value: `"COMPLETE"`)





## Enum: MigrationStepEnum


* `MIGRATION_STEP_UNSPECIFIED` (value: `"MIGRATION_STEP_UNSPECIFIED"`)

* `PREPARE` (value: `"PREPARE"`)

* `START` (value: `"START"`)

* `APPLY_WRITES_SYNCHRONOUSLY` (value: `"APPLY_WRITES_SYNCHRONOUSLY"`)

* `COPY_AND_VERIFY` (value: `"COPY_AND_VERIFY"`)

* `REDIRECT_EVENTUALLY_CONSISTENT_READS` (value: `"REDIRECT_EVENTUALLY_CONSISTENT_READS"`)

* `REDIRECT_STRONGLY_CONSISTENT_READS` (value: `"REDIRECT_STRONGLY_CONSISTENT_READS"`)

* `REDIRECT_WRITES` (value: `"REDIRECT_WRITES"`)




