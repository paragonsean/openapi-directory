# PeopleApi.Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costCenter** | **String** | The person&#39;s cost center at the organization. | [optional] 
**current** | **Boolean** | True if the organization is the person&#39;s current organization; false if the organization is a past organization. | [optional] 
**department** | **String** | The person&#39;s department at the organization. | [optional] 
**domain** | **String** | The domain name associated with the organization; for example, &#x60;google.com&#x60;. | [optional] 
**endDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**formattedType** | **String** | Output only. The type of the organization translated and formatted in the viewer&#39;s account locale or the &#x60;Accept-Language&#x60; HTTP header locale. | [optional] [readonly] 
**fullTimeEquivalentMillipercent** | **Number** | The person&#39;s full-time equivalent millipercent within the organization (100000 &#x3D; 100%). | [optional] 
**jobDescription** | **String** | The person&#39;s job description at the organization. | [optional] 
**location** | **String** | The location of the organization office the person works at. | [optional] 
**metadata** | [**FieldMetadata**](FieldMetadata.md) |  | [optional] 
**name** | **String** | The name of the organization. | [optional] 
**phoneticName** | **String** | The phonetic name of the organization. | [optional] 
**startDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**symbol** | **String** | The symbol associated with the organization; for example, a stock ticker symbol, abbreviation, or acronym. | [optional] 
**title** | **String** | The person&#39;s job title at the organization. | [optional] 
**type** | **String** | The type of the organization. The type can be custom or one of these predefined values: * &#x60;work&#x60; * &#x60;school&#x60; | [optional] 


