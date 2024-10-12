# RebillyRestApi.LeadSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[BankAccountAllOfLinks]**](BankAccountAllOfLinks.md) | The links related to resource. | [optional] [readonly] 
**affiliate** | **String** | Lead source affiliate (eg 123, Bob Smith). | [optional] 
**campaign** | **String** | Lead source campaign (eg go-big-123). | [optional] 
**clickId** | **String** | Lead source click id (may come from an ad server). | [optional] 
**content** | **String** | Lead source content (eg smiley faces). | [optional] 
**createdTime** | **Date** | Lead source created time. | [optional] [readonly] 
**medium** | **String** | Lead source medium (eg search, display). | [optional] 
**path** | **String** | Lead source path url (eg www.example.com/some/landing/path). | [optional] 
**referrer** | **String** | Lead source [&#x60;referer&#x60; url](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) as determined (eg www.example.com/some/landing/path). | [optional] 
**salesAgent** | **String** | Lead source sales agent (eg James Bond). | [optional] 
**source** | **String** | Lead source origin (eg google, yahoo). | [optional] 
**subAffiliate** | **String** | Lead source sub-affiliate also called a sub-id or click id in some circles (eg 123456). | [optional] 
**term** | **String** | Lead source term (eg salt shakers). | [optional] 
**original** | [**LeadSourceData**](LeadSourceData.md) |  | [optional] [readonly] 


