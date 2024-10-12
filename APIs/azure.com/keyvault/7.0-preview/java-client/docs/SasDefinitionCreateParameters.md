

# SasDefinitionCreateParameters

The SAS definition create parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**SasDefinitionAttributes**](SasDefinitionAttributes.md) |  |  [optional] |
|**sasType** | [**SasTypeEnum**](#SasTypeEnum) | The type of SAS token the SAS definition will create. |  |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |
|**templateUri** | **String** | The SAS definition token template signed with an arbitrary key.  Tokens created according to the SAS definition will have the same properties as the template. |  |
|**validityPeriod** | **String** | The validity period of SAS tokens created according to the SAS definition. |  |



## Enum: SasTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |
| SERVICE | &quot;service&quot; |



