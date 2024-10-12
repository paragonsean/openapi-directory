

# GoogleDatastoreAdminV1MigrationStateEvent

An event signifying a change in state of a [migration from Cloud Datastore to Cloud Firestore in Datastore mode](https://cloud.google.com/datastore/docs/upgrade-to-firestore).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | The new state of the migration. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| MIGRATION_STATE_UNSPECIFIED | &quot;MIGRATION_STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| PAUSED | &quot;PAUSED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



