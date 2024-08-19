

# ExternalSecuritySolution

Represents a security solution external to Azure Security Center which sends information to an OMS workspace and whose data is displayed by Azure Security Center.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of the external solution |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**type** | **String** | Resource type |  [optional] [readonly] |
|**location** | **String** | Location where the resource is stored |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| CEF | &quot;CEF&quot; |
| ATA | &quot;ATA&quot; |
| AAD | &quot;AAD&quot; |



