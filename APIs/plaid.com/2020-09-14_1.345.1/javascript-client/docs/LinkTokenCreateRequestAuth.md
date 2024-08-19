# ThePlaidApi.LinkTokenCreateRequestAuth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authTypeSelectEnabled** | **Boolean** | Specifies whether Auth Type Select is enabled for the Link session, allowing the end user to choose between linking instantly or manually prior to selecting their financial institution. Note that this can only be true if &#x60;same_day_microdeposits_enabled&#x60; is set to true. | [optional] [default to false]
**automatedMicrodepositsEnabled** | **Boolean** | Specifies whether the Link session is enabled for the Automated Micro-deposits flow. | [optional] 
**flowType** | **String** | This field has been deprecated in favor of &#x60;auth_type_select_enabled&#x60;. | [optional] 
**instantMatchEnabled** | **Boolean** | Specifies whether the Link session is enabled for the Instant Match flow. As of November 2022, Instant Match will be enabled by default. Instant Match can be disabled by setting this field to &#x60;false&#x60;. | [optional] 
**sameDayMicrodepositsEnabled** | **Boolean** | Specifies whether the Link session is enabled for the Same Day Micro-deposits flow. | [optional] 



## Enum: FlowTypeEnum


* `FLEXIBLE_AUTH` (value: `"FLEXIBLE_AUTH"`)




