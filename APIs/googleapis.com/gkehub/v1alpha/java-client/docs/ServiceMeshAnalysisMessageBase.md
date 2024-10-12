

# ServiceMeshAnalysisMessageBase

AnalysisMessageBase describes some common information that is needed for all messages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentationUrl** | **String** | A url pointing to the Service Mesh or Istio documentation for this specific error type. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Represents how severe a message is. |  [optional] |
|**type** | [**ServiceMeshType**](ServiceMeshType.md) |  |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;LEVEL_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| WARNING | &quot;WARNING&quot; |
| INFO | &quot;INFO&quot; |



