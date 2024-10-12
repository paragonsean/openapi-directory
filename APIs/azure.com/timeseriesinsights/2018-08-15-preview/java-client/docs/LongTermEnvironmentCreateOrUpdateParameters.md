

# LongTermEnvironmentCreateOrUpdateParameters

Parameters supplied to the Create or Update Environment operation for a long-term environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**LongTermEnvironmentCreationProperties**](LongTermEnvironmentCreationProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | The kind of the environment. |  |
|**sku** | [**Sku**](Sku.md) |  |  |
|**location** | **String** | The location of the resource. |  |
|**tags** | **Map&lt;String, String&gt;** | Key-value pairs of additional properties for the resource. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| LONG_TERM | &quot;LongTerm&quot; |



