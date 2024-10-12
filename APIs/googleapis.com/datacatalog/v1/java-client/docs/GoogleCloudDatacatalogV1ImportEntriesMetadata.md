

# GoogleCloudDatacatalogV1ImportEntriesMetadata

Metadata message for long-running operation returned by the ImportEntries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Status&gt;**](Status.md) | Partial errors that are encountered during the ImportEntries operation. There is no guarantee that all the encountered errors are reported. However, if no errors are reported, it means that no errors were encountered. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the import operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;IMPORT_STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;IMPORT_QUEUED&quot; |
| IN_PROGRESS | &quot;IMPORT_IN_PROGRESS&quot; |
| DONE | &quot;IMPORT_DONE&quot; |
| OBSOLETE | &quot;IMPORT_OBSOLETE&quot; |



