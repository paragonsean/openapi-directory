

# ListExternalAccessRulesResponse

Response message for VmwareEngine.ListExternalAccessRules

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalAccessRules** | [**List&lt;ExternalAccessRule&gt;**](ExternalAccessRule.md) | A list of external access firewall rules. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached when making an aggregated query using wildcards. |  [optional] |



