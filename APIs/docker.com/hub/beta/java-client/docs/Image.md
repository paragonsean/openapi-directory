

# Image


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | **String** | CPU architecture |  [optional] |
|**digest** | **String** | image digest |  [optional] |
|**features** | **String** | CPU features |  [optional] |
|**lastPulled** | **String** | datetime of last pull |  [optional] |
|**lastPushed** | **String** | datetime of last push |  [optional] |
|**layers** | [**List&lt;Layer&gt;**](Layer.md) |  |  [optional] |
|**os** | **String** | operating system |  [optional] |
|**osFeatures** | **String** | OS features |  [optional] |
|**osVersion** | **String** | OS version |  [optional] |
|**size** | **Integer** | size of the image |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the image |  [optional] |
|**variant** | **String** | CPU variant |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



