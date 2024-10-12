# AmazonCloudDirectory.ListObjectParentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objectReference** | [**AddFacetToObjectRequestObjectReference**](AddFacetToObjectRequestObjectReference.md) |  | 
**nextToken** | **String** | The pagination token. | [optional] 
**maxResults** | **Number** | The maximum number of items to be retrieved in a single call. This is an approximate number. | [optional] 
**includeAllLinksToEachParent** | **Boolean** | When set to True, returns all &lt;a&gt;ListObjectParentsResponse$ParentLinks&lt;/a&gt;. There could be multiple links between a parent-child pair. | [optional] 


