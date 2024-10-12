# LinodeApi.DatabaseBackupSnapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **String** | The label for the Database snapshot backup.  * Must include only ASCII letters or numbers. * Must be unique among other backup labels for this Database.  | 
**target** | **String** | The Database cluster target. If the Database is a high availability cluster, choosing &#x60;secondary&#x60; creates a snapshot backup of a replica node.  | [optional] [default to &#39;primary&#39;]



## Enum: TargetEnum


* `primary` (value: `"primary"`)

* `secondary` (value: `"secondary"`)




