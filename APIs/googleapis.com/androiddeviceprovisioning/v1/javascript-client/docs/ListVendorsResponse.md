# AndroidDeviceProvisioningPartnerApi.ListVendorsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token to retrieve the next page of results. Omitted if no further results are available. | [optional] 
**totalSize** | **Number** | The total count of items in the list irrespective of pagination. | [optional] 
**vendors** | [**[Company]**](Company.md) | List of vendors of the reseller partner. Fields &#x60;name&#x60;, &#x60;companyId&#x60; and &#x60;companyName&#x60; are populated to the Company object. | [optional] 


