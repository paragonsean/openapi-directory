

# AtaExternalSecuritySolution

Represents an ATA security solution which sends logs to an OMS workspace

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**AtaSolutionProperties**](AtaSolutionProperties.md) |  |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**type** | **String** | Resource type |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | The kind of the external solution |  [optional] |
|**location** | **String** | Location where the resource is stored |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| CEF | &quot;CEF&quot; |
| ATA | &quot;ATA&quot; |
| AAD | &quot;AAD&quot; |



