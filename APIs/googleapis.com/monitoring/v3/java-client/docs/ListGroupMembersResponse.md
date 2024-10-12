

# ListGroupMembersResponse

The ListGroupMembers response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**members** | [**List&lt;MonitoredResource&gt;**](MonitoredResource.md) | A set of monitored resources in the group. |  [optional] |
|**nextPageToken** | **String** | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |  [optional] |
|**totalSize** | **Integer** | The total number of elements matching this request. |  [optional] |



