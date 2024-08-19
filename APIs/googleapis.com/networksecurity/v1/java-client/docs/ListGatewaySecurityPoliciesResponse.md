

# ListGatewaySecurityPoliciesResponse

Response returned by the ListGatewaySecurityPolicies method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewaySecurityPolicies** | [**List&lt;GatewaySecurityPolicy&gt;**](GatewaySecurityPolicy.md) | List of GatewaySecurityPolicies resources. |  [optional] |
|**nextPageToken** | **String** | If there might be more results than those appearing in this response, then &#39;next_page_token&#39; is included. To get the next set of results, call this method again using the value of &#39;next_page_token&#39; as &#39;page_token&#39;. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



