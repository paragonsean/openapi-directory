

# ListEntitiesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalog** | **String** | The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;  |  |
|**entityType** | **String** | The type of entities to retrieve. |  |
|**filterList** | [**List&lt;Filter&gt;**](Filter.md) | An array of filter objects. Each filter object contains two attributes, &lt;code&gt;filterName&lt;/code&gt; and &lt;code&gt;filterValues&lt;/code&gt;. |  [optional] |
|**sort** | [**ListChangeSetsRequestSort**](ListChangeSetsRequestSort.md) |  |  [optional] |
|**nextToken** | **String** | The value of the next token, if it exists. Null if there are no more results. |  [optional] |
|**maxResults** | **Integer** | Specifies the upper limit of the elements on a single page. If a value isn&#39;t provided, the default value is 20. |  [optional] |
|**ownershipType** | [**OwnershipTypeEnum**](#OwnershipTypeEnum) |  |  [optional] |



## Enum: OwnershipTypeEnum

| Name | Value |
|---- | -----|
| SELF | &quot;SELF&quot; |
| SHARED | &quot;SHARED&quot; |



