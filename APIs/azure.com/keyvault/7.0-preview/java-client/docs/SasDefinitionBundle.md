

# SasDefinitionBundle

A SAS definition bundle consists of key vault SAS definition details plus its attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



