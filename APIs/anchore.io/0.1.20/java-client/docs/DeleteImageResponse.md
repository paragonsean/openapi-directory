

# DeleteImageResponse

Image deletion response containing status and details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** |  |  [optional] |
|**digest** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the image deletion |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_FOUND | &quot;not_found&quot; |
| DELETING | &quot;deleting&quot; |
| DELETE_FAILED | &quot;delete_failed&quot; |



