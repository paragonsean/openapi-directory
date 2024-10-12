# AccountApi.ViasAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | The name of the city. Required if the &#x60;houseNumberOrName&#x60;, &#x60;street&#x60;, &#x60;postalCode&#x60;, or &#x60;stateOrProvince&#x60; are provided. | [optional] 
**country** | **String** | The two-character country code of the address in ISO-3166-1 alpha-2 format. For example, **NL**. | 
**houseNumberOrName** | **String** | The number or name of the house. | [optional] 
**postalCode** | **String** | The postal code. Required if the &#x60;houseNumberOrName&#x60;, &#x60;street&#x60;, &#x60;city&#x60;, or &#x60;stateOrProvince&#x60; are provided.  Maximum length:  * 5 digits for addresses in the US.  * 10 characters for all other countries. | [optional] 
**stateOrProvince** | **String** | The abbreviation of the state or province. Required if the &#x60;houseNumberOrName&#x60;, &#x60;street&#x60;, &#x60;city&#x60;, or &#x60;postalCode&#x60; are provided.   Maximum length:  * 2 characters for addresses in the US or Canada.  * 3 characters for all other countries.  | [optional] 
**street** | **String** | The name of the street. Required if the &#x60;houseNumberOrName&#x60;, &#x60;city&#x60;, &#x60;postalCode&#x60;, or &#x60;stateOrProvince&#x60; are provided. | [optional] 


