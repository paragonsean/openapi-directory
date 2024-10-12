

# Tag


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creator** | **Integer** | ID of the user that pushed the tag |  [optional] |
|**fullSize** | **Integer** | compressed size (sum of all layers) of the tagged image |  [optional] |
|**id** | **Integer** | tag ID |  [optional] |
|**images** | **Image** |  |  [optional] |
|**lastUpdated** | **String** | datetime of last update |  [optional] |
|**lastUpdater** | **Integer** | ID of the last user that updated the tag |  [optional] |
|**lastUpdaterUsername** | **String** | Hub username of the user that updated the tag |  [optional] |
|**name** | **String** | name of the tag |  [optional] |
|**repository** | **Integer** | repository ID |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | whether a tag has been pushed to or pulled in the past month |  [optional] |
|**tagLastPulled** | **String** | datetime of last pull |  [optional] |
|**tagLastPushed** | **String** | datetime of last push |  [optional] |
|**v2** | **String** | repository API version |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



