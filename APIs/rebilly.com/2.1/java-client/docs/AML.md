

# AML


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource, including links provided by the list. |  [optional] [readonly] |
|**address** | [**List&lt;AMLAddressInner&gt;**](AMLAddressInner.md) | Addresses related to the identity. |  [optional] [readonly] |
|**aliases** | [**List&lt;AMLAliasesInner&gt;**](AMLAliasesInner.md) | List of aliases, if any. |  [optional] [readonly] |
|**comments** | **String** | Extra information (the content varies per list). |  [optional] [readonly] |
|**confidence** | [**ConfidenceEnum**](#ConfidenceEnum) | The source list&#39;s confidence in information. |  [optional] [readonly] |
|**dob** | **List&lt;LocalDate&gt;** | One or more possible dates of birth. |  [optional] [readonly] |
|**firstName** | **String** | First Name. |  [optional] [readonly] |
|**gender** | **String** | Gender of returned identity (if &#x60;type&#x60; is &#x60;individual&#x60;). |  [optional] [readonly] |
|**lastName** | **String** | Last Name. &#x60;null&#x60; if it is a single-name entity. |  [optional] [readonly] |
|**legalBasis** | **List&lt;String&gt;** | List of references to legal documents if they exist. |  [optional] [readonly] |
|**nationality** | **String** | The nationality of the identity. |  [optional] [readonly] |
|**passport** | [**List&lt;AMLPassportInner&gt;**](AMLPassportInner.md) | Passport information. |  [optional] [readonly] |
|**regime** | **String** | Regime. |  [optional] [readonly] |
|**source** | **String** | Which list this came from. |  [optional] [readonly] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The list type. |  [optional] [readonly] |
|**title** | **List&lt;String&gt;** | The title of their position. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The record type. |  [optional] [readonly] |



## Enum: ConfidenceEnum

| Name | Value |
|---- | -----|
| WEAK | &quot;weak&quot; |
| MEDIUM | &quot;medium&quot; |
| STRONG | &quot;strong&quot; |
| VERY_STRONG | &quot;very-strong&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| PEP | &quot;pep&quot; |
| SANCTIONS | &quot;sanctions&quot; |
| ADVERSE_MEDIA | &quot;adverse-media&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;individual&quot; |
| ENTITY | &quot;entity&quot; |



