

# ListInsuranceNetworksResponse

Response message for InsuranceNetworkService.ListInsuranceNetworks

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**networks** | [**List&lt;InsuranceNetwork&gt;**](InsuranceNetwork.md) | A list of insurance networks that are supported by Google. |  [optional] |
|**nextPageToken** | **String** | If there are more insurance networks than the requested page size, then this field is populated with a token to fetch the next page of insurance networks on a subsequent call to ListInsuranceNetworks. |  [optional] |



