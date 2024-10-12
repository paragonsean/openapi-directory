# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1ImportEntriesMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Status]**](Status.md) | Partial errors that are encountered during the ImportEntries operation. There is no guarantee that all the encountered errors are reported. However, if no errors are reported, it means that no errors were encountered. | [optional] 
**state** | **String** | State of the import operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"IMPORT_STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"IMPORT_QUEUED"`)

* `IN_PROGRESS` (value: `"IMPORT_IN_PROGRESS"`)

* `DONE` (value: `"IMPORT_DONE"`)

* `OBSOLETE` (value: `"IMPORT_OBSOLETE"`)




