

# GetNamespaceRepositoryImagesResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **String** | The image&#39;s digest. |  [optional] |
|**lastPulled** | **String** | Time when this image was last pulled. Note this is updated at most once per hour. |  [optional] |
|**lastPushed** | **String** | Time when this image was last pushed. |  [optional] |
|**namespace** | **String** | The repository namespace. |  [optional] |
|**repository** | **String** | The repository name. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the image based on its last activity against the &#x60;active_from&#x60; time. |  [optional] |
|**tags** | [**List&lt;GetNamespaceRepositoryImagesResponseResultsInnerTagsInner&gt;**](GetNamespaceRepositoryImagesResponseResultsInnerTagsInner.md) | The current and historical tags for this image. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



