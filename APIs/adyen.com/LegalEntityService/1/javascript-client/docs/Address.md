# LegalEntityManagementApi.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | The name of the city. Required if &#x60;stateOrProvince&#x60; is provided.  If you specify the city, you must also send &#x60;postalCode&#x60; and &#x60;street&#x60;. | [optional] 
**country** | **String** | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. | 
**postalCode** | **String** | Postal code. Required if &#x60;stateOrProvince&#x60; and/or &#x60;city&#x60; is provided. | [optional] 
**stateOrProvince** | **String** | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US.  If you specify the state or province, you must also send &#x60;city&#x60;, &#x60;postalCode&#x60;, and &#x60;street&#x60;. | [optional] 
**street** | **String** | The name of the street, and the house or building number. Required if &#x60;stateOrProvince&#x60; and/or &#x60;city&#x60; is provided. | [optional] 
**street2** | **String** | The apartment, unit, or suite number. | [optional] 


