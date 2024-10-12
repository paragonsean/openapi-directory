

# ListVmwareEngineNetworksResponse

Response message for VmwareEngine.ListVmwareEngineNetworks

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Unreachable resources. |  [optional] |
|**vmwareEngineNetworks** | [**List&lt;VmwareEngineNetwork&gt;**](VmwareEngineNetwork.md) | A list of VMware Engine networks. |  [optional] |



