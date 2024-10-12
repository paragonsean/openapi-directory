

# ListLFTagsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  |  [optional] |
|**resourceShareType** | [**ResourceShareTypeEnum**](#ResourceShareTypeEnum) | If resource share type is &lt;code&gt;ALL&lt;/code&gt;, returns both in-account LF-tags and shared LF-tags that the requester has permission to view. If resource share type is &lt;code&gt;FOREIGN&lt;/code&gt;, returns all share LF-tags that the requester can view. If no resource share type is passed, lists LF-tags in the given catalog ID that the requester has permission to view. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return. |  [optional] |
|**nextToken** | **String** | A continuation token, if this is not the first call to retrieve this list. |  [optional] |



## Enum: ResourceShareTypeEnum

| Name | Value |
|---- | -----|
| FOREIGN | &quot;FOREIGN&quot; |
| ALL | &quot;ALL&quot; |



