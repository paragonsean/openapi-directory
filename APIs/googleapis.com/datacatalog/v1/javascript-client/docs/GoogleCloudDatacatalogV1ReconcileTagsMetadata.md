# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1ReconcileTagsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**{String: Status}**](Status.md) | Maps the name of each tagged column (or empty string for a sole entry) to tagging operation status. | [optional] 
**state** | **String** | State of the reconciliation operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"RECONCILIATION_STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"RECONCILIATION_QUEUED"`)

* `IN_PROGRESS` (value: `"RECONCILIATION_IN_PROGRESS"`)

* `DONE` (value: `"RECONCILIATION_DONE"`)




