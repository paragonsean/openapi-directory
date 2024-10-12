

# ListDnsAuthorizationsResponse

Response for the `ListDnsAuthorizations` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsAuthorizations** | [**List&lt;DnsAuthorization&gt;**](DnsAuthorization.md) | A list of dns authorizations for the parent resource. |  [optional] |
|**nextPageToken** | **String** | If there might be more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



