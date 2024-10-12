# NumberInsightApi.NiResponseJsonBasic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryCode** | **String** | Two character country code for &#x60;number&#x60;. This is in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. | [optional] 
**countryCodeIso3** | **String** | Three character country code for &#x60;number&#x60;. This is in [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format. | [optional] 
**countryName** | **String** | The full name of the country that &#x60;number&#x60; is registered in. | [optional] 
**countryPrefix** | **String** | The numeric prefix for the country that &#x60;number&#x60; is registered in. | [optional] 
**internationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in international format. | [optional] 
**nationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in the format used by the country the number belongs to. | [optional] 
**requestId** | **String** | The unique identifier for your request. This is a alphanumeric string up to 40 characters. | [optional] 
**status** | [**NiBasicStatus**](NiBasicStatus.md) |  | [optional] 
**statusMessage** | **String** | The status description of your request. | [optional] 


