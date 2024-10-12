# RebillyRestApi.AML

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource, including links provided by the list. | [optional] [readonly] 
**address** | [**[AMLAddressInner]**](AMLAddressInner.md) | Addresses related to the identity. | [optional] [readonly] 
**aliases** | [**[AMLAliasesInner]**](AMLAliasesInner.md) | List of aliases, if any. | [optional] [readonly] 
**comments** | **String** | Extra information (the content varies per list). | [optional] [readonly] 
**confidence** | **String** | The source list&#39;s confidence in information. | [optional] [readonly] 
**dob** | **[Date]** | One or more possible dates of birth. | [optional] [readonly] 
**firstName** | **String** | First Name. | [optional] [readonly] 
**gender** | **String** | Gender of returned identity (if &#x60;type&#x60; is &#x60;individual&#x60;). | [optional] [readonly] 
**lastName** | **String** | Last Name. &#x60;null&#x60; if it is a single-name entity. | [optional] [readonly] 
**legalBasis** | **[String]** | List of references to legal documents if they exist. | [optional] [readonly] 
**nationality** | **String** | The nationality of the identity. | [optional] [readonly] 
**passport** | [**[AMLPassportInner]**](AMLPassportInner.md) | Passport information. | [optional] [readonly] 
**regime** | **String** | Regime. | [optional] [readonly] 
**source** | **String** | Which list this came from. | [optional] [readonly] 
**sourceType** | **String** | The list type. | [optional] [readonly] 
**title** | **[String]** | The title of their position. | [optional] [readonly] 
**type** | **String** | The record type. | [optional] [readonly] 



## Enum: ConfidenceEnum


* `weak` (value: `"weak"`)

* `medium` (value: `"medium"`)

* `strong` (value: `"strong"`)

* `very-strong` (value: `"very-strong"`)





## Enum: SourceTypeEnum


* `pep` (value: `"pep"`)

* `sanctions` (value: `"sanctions"`)

* `adverse-media` (value: `"adverse-media"`)





## Enum: TypeEnum


* `individual` (value: `"individual"`)

* `entity` (value: `"entity"`)




