

# DeletedSasDefinitionItem

The deleted SAS definition item containing metadata about the deleted SAS definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedDate** | **Integer** | The time when the SAS definition was deleted, in UTC |  [optional] [readonly] |
|**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted SAS definition. |  [optional] |
|**scheduledPurgeDate** | **Integer** | The time when the SAS definition is scheduled to be purged, in UTC |  [optional] [readonly] |
|**attributes** | [**SasDefinitionAttributes**](SasDefinitionAttributes.md) |  |  [optional] |
|**id** | **String** | The storage SAS identifier. |  [optional] [readonly] |
|**sid** | **String** | The storage account SAS definition secret id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] [readonly] |



