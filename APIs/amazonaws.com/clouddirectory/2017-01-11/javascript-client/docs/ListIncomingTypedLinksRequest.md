# AmazonCloudDirectory.ListIncomingTypedLinksRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objectReference** | [**AddFacetToObjectRequestObjectReference**](AddFacetToObjectRequestObjectReference.md) |  | 
**filterAttributeRanges** | [**[TypedLinkAttributeRange]**](TypedLinkAttributeRange.md) | Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. | [optional] 
**filterTypedLink** | [**AttachTypedLinkRequestTypedLinkFacet**](AttachTypedLinkRequestTypedLinkFacet.md) |  | [optional] 
**nextToken** | **String** | The pagination token. | [optional] 
**maxResults** | **Number** | The maximum number of results to retrieve. | [optional] 
**consistencyLevel** | **String** | The consistency level to execute the request at. | [optional] 



## Enum: ConsistencyLevelEnum


* `SERIALIZABLE` (value: `"SERIALIZABLE"`)

* `EVENTUAL` (value: `"EVENTUAL"`)




