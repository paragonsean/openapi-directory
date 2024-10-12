

# ListDirectoriesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextToken** | **String** | The pagination token. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to retrieve. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the directories in the list. Can be either Enabled, Disabled, or Deleted. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| DELETED | &quot;DELETED&quot; |



