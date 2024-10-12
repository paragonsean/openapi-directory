

# ListIncomingTypedLinksRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectReference** | [**AddFacetToObjectRequestObjectReference**](AddFacetToObjectRequestObjectReference.md) |  |  |
|**filterAttributeRanges** | [**List&lt;TypedLinkAttributeRange&gt;**](TypedLinkAttributeRange.md) | Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. |  [optional] |
|**filterTypedLink** | [**AttachTypedLinkRequestTypedLinkFacet**](AttachTypedLinkRequestTypedLinkFacet.md) |  |  [optional] |
|**nextToken** | **String** | The pagination token. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to retrieve. |  [optional] |
|**consistencyLevel** | [**ConsistencyLevelEnum**](#ConsistencyLevelEnum) | The consistency level to execute the request at. |  [optional] |



## Enum: ConsistencyLevelEnum

| Name | Value |
|---- | -----|
| SERIALIZABLE | &quot;SERIALIZABLE&quot; |
| EVENTUAL | &quot;EVENTUAL&quot; |



