# Taxamo.GetEuViesReportIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyCode** | **String** | ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code. | [optional] 
**endMonth** | **String** | Period end month in yyyy-MM format. | 
**euCountryCode** | **String** | ISO 2-letter country code which will be used for determining which country is domestic. | 
**format** | **String** | Output format. &#39;xml&#39;, &#39;csv&#39; and &#39;lff&#39; (only for Ireland) values are accepted as well | [optional] 
**fxDateType** | **String** | Which date should be used for FX. | [optional] 
**lffSequenceNumber** | **String** | Sequence number used to generate report in Large Filer Format. If not specified then &#39;0000000001&#39; will be used. | [optional] 
**periodLength** | **String** | Length of report period. &#39;month&#39;, &#39;quarter&#39; and &#39;year&#39; values are accepted. Required only if Large Filer Format is requested. | [optional] 
**startMonth** | **String** | Period start month in yyyy-MM format. | 
**taxId** | **String** | MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. | [optional] 
**transformation** | **String** | Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats. | [optional] 


