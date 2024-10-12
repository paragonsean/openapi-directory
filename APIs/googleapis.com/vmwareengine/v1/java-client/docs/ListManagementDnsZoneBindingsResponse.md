

# ListManagementDnsZoneBindingsResponse

Response message for VmwareEngine.ListManagementDnsZoneBindings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managementDnsZoneBindings** | [**List&lt;ManagementDnsZoneBinding&gt;**](ManagementDnsZoneBinding.md) | A list of management DNS zone bindings. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached when making an aggregated query using wildcards. |  [optional] |



