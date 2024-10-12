# GoogleWorkspaceResellerApi.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressLine1** | **String** | A customer&#39;s physical address. An address can be composed of one to three lines. The &#x60;addressline2&#x60; and &#x60;addressLine3&#x60; are optional. | [optional] 
**addressLine2** | **String** | Line 2 of the address. | [optional] 
**addressLine3** | **String** | Line 3 of the address. | [optional] 
**contactName** | **String** | The customer contact&#39;s name. This is required. | [optional] 
**countryCode** | **String** | For &#x60;countryCode&#x60; information, see the ISO 3166 country code elements. Verify that country is approved for resale of Google products. This property is required when creating a new customer. | [optional] 
**kind** | **String** | Identifies the resource as a customer address. Value: &#x60;customers#address&#x60; | [optional] [default to &#39;customers#address&#39;]
**locality** | **String** | An example of a &#x60;locality&#x60; value is the city of &#x60;San Francisco&#x60;. | [optional] 
**organizationName** | **String** | The company or company division name. This is required. | [optional] 
**postalCode** | **String** | A &#x60;postalCode&#x60; example is a postal zip code such as &#x60;94043&#x60;. This property is required when creating a new customer. | [optional] 
**region** | **String** | An example of a &#x60;region&#x60; value is &#x60;CA&#x60; for the state of California. | [optional] 


