

# LinksResourceAttributes

Links endpoint resource object attributes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregate** | **Aggregate** | A string indicating whether a client that is following links to aggregate results from different OPTIMADE implementations should follow this link or not. This flag SHOULD NOT be indicated for links where &#x60;link_type&#x60; is not &#x60;child&#x60;.  If not specified, clients MAY assume that the value is &#x60;ok&#x60;. If specified, and the value is anything different than &#x60;ok&#x60;, the client MUST assume that the server is suggesting not to follow the link during aggregation by default (also if the value is not among the known ones, in case a future specification adds new accepted values).  Specific values indicate the reason why the server is providing the suggestion. A client MAY follow the link anyway if it has reason to do so (e.g., if the client is looking for all test databases, it MAY follow the links marked with &#x60;aggregate&#x60;&#x3D;&#x60;test&#x60;).  If specified, it MUST be one of the values listed in section Link Aggregate Options. |  [optional] |
|**baseUrl** | [**BaseUrl**](BaseUrl.md) |  |  |
|**description** | **String** | Human-readable description for the OPTIMADE API implementation, e.g., for use in clients to show a description to the end-user. |  |
|**homepage** | [**Homepage1**](Homepage1.md) |  |  |
|**linkType** | **LinkType** | The type of the linked relation. MUST be one of these values: &#39;child&#39;, &#39;root&#39;, &#39;external&#39;, &#39;providers&#39;. |  |
|**name** | **String** | Human-readable name for the OPTIMADE API implementation, e.g., for use in clients to show the name to the end-user. |  |
|**noAggregateReason** | **String** | An OPTIONAL human-readable string indicating the reason for suggesting not to aggregate results following the link. It SHOULD NOT be present if &#x60;aggregate&#x60;&#x3D;&#x60;ok&#x60;. |  [optional] |



