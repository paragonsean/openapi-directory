

# ImageCreateResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**image** | [**Image**](Image.md) |  |  [optional] |
|**sourceUrl** | **String** | Source URL of the image. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the image creation. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| OK_DUPLICATE | &quot;OKDuplicate&quot; |
| ERROR_SOURCE | &quot;ErrorSource&quot; |
| ERROR_IMAGE_FORMAT | &quot;ErrorImageFormat&quot; |
| ERROR_IMAGE_SIZE | &quot;ErrorImageSize&quot; |
| ERROR_STORAGE | &quot;ErrorStorage&quot; |
| ERROR_LIMIT_EXCEED | &quot;ErrorLimitExceed&quot; |
| ERROR_TAG_LIMIT_EXCEED | &quot;ErrorTagLimitExceed&quot; |
| ERROR_REGION_LIMIT_EXCEED | &quot;ErrorRegionLimitExceed&quot; |
| ERROR_UNKNOWN | &quot;ErrorUnknown&quot; |
| ERROR_NEGATIVE_AND_REGULAR_TAG_ON_SAME_IMAGE | &quot;ErrorNegativeAndRegularTagOnSameImage&quot; |



