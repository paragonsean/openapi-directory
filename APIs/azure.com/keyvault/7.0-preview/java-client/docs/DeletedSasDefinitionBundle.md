

# DeletedSasDefinitionBundle

A deleted SAS definition bundle consisting of its previous id, attributes and its tags, as well as information on when it will be purged.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedDate** | **Integer** | The time when the SAS definition was deleted, in UTC |  [optional] [readonly] |
|**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted SAS definition. |  [optional] |
|**scheduledPurgeDate** | **Integer** | The time when the SAS definition is scheduled to be purged, in UTC |  [optional] [readonly] |
|**attributes** | [**SasDefinitionAttributes**](SasDefinitionAttributes.md) |  |  [optional] |
|**id** | **String** | The SAS definition id. |  [optional] [readonly] |
|**sasType** | [**SasTypeEnum**](#SasTypeEnum) | The type of SAS token the SAS definition will create. |  [optional] [readonly] |
|**sid** | **String** | Storage account SAS definition secret id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs |  [optional] [readonly] |
|**templateUri** | **String** | The SAS definition token template signed with an arbitrary key.  Tokens created according to the SAS definition will have the same properties as the template. |  [optional] [readonly] |
|**validityPeriod** | **String** | The validity period of SAS tokens created according to the SAS definition. |  [optional] [readonly] |



## Enum: SasTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |
| SERVICE | &quot;service&quot; |



