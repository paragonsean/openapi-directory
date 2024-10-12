

# ListPrivateCloudsResponse

Response message for VmwareEngine.ListPrivateClouds

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**privateClouds** | [**List&lt;PrivateCloud&gt;**](PrivateCloud.md) | A list of private clouds. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached when making an aggregated query using wildcards. |  [optional] |



