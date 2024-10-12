# AwsMarketplaceCatalogService.ListEntitiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **String** | The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;  | 
**entityType** | **String** | The type of entities to retrieve. | 
**filterList** | [**[Filter]**](Filter.md) | An array of filter objects. Each filter object contains two attributes, &lt;code&gt;filterName&lt;/code&gt; and &lt;code&gt;filterValues&lt;/code&gt;. | [optional] 
**sort** | [**ListChangeSetsRequestSort**](ListChangeSetsRequestSort.md) |  | [optional] 
**nextToken** | **String** | The value of the next token, if it exists. Null if there are no more results. | [optional] 
**maxResults** | **Number** | Specifies the upper limit of the elements on a single page. If a value isn&#39;t provided, the default value is 20. | [optional] 
**ownershipType** | **String** |  | [optional] 



## Enum: OwnershipTypeEnum


* `SELF` (value: `"SELF"`)

* `SHARED` (value: `"SHARED"`)




