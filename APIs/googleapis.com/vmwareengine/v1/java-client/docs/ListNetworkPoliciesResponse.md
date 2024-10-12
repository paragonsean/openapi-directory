

# ListNetworkPoliciesResponse

Response message for VmwareEngine.ListNetworkPolicies

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**networkPolicies** | [**List&lt;NetworkPolicy&gt;**](NetworkPolicy.md) | A list of network policies. |  [optional] |
|**nextPageToken** | **String** | A token, which can be send as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached when making an aggregated query using wildcards. |  [optional] |



