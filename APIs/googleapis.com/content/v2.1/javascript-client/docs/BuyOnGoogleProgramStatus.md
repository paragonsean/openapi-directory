# ContentApiForShopping.BuyOnGoogleProgramStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businessModel** | **[String]** | The business models in which merchant participates. | [optional] 
**customerServicePendingEmail** | **String** | The customer service pending email. After verification this field becomes empty. | [optional] 
**customerServicePendingPhoneNumber** | **String** | The pending phone number specified for BuyOnGoogle program. It might be different than account level phone number. In order to update this field the customer_service_pending_phone_region_code must also be set. After verification this field becomes empty. | [optional] 
**customerServicePendingPhoneRegionCode** | **String** | Two letter country code for the pending phone number, for example &#x60;CA&#x60; for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. In order to update this field the customer_service_pending_phone_number must also be set. After verification this field becomes empty. | [optional] 
**customerServiceVerifiedEmail** | **String** | Output only. The customer service verified email. | [optional] [readonly] 
**customerServiceVerifiedPhoneNumber** | **String** | Output only. The verified phone number specified for BuyOnGoogle program. It might be different than account level phone number. | [optional] [readonly] 
**customerServiceVerifiedPhoneRegionCode** | **String** | Output only. Two letter country code for the verified phone number, for example &#x60;CA&#x60; for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. | [optional] [readonly] 
**onlineSalesChannel** | **String** | The channels through which the merchant is selling. | [optional] 
**participationStage** | **String** | Output only. The current participation stage for the program. | [optional] [readonly] 



## Enum: [BusinessModelEnum]


* `BUSINESS_MODEL_UNSPECIFIED` (value: `"BUSINESS_MODEL_UNSPECIFIED"`)

* `MANUFACTURER` (value: `"MANUFACTURER"`)

* `IMPORTER` (value: `"IMPORTER"`)

* `RESELLER` (value: `"RESELLER"`)

* `OTHER` (value: `"OTHER"`)





## Enum: OnlineSalesChannelEnum


* `ONLINE_SALES_CHANNEL_UNSPECIFIED` (value: `"ONLINE_SALES_CHANNEL_UNSPECIFIED"`)

* `GOOGLE_EXCLUSIVE` (value: `"GOOGLE_EXCLUSIVE"`)

* `GOOGLE_AND_OTHER_WEBSITES` (value: `"GOOGLE_AND_OTHER_WEBSITES"`)





## Enum: ParticipationStageEnum


* `PROGRAM_PARTICIPATION_STAGE_UNSPECIFIED` (value: `"PROGRAM_PARTICIPATION_STAGE_UNSPECIFIED"`)

* `NOT_ELIGIBLE` (value: `"NOT_ELIGIBLE"`)

* `ELIGIBLE` (value: `"ELIGIBLE"`)

* `ONBOARDING` (value: `"ONBOARDING"`)

* `ELIGIBLE_FOR_REVIEW` (value: `"ELIGIBLE_FOR_REVIEW"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `REVIEW_DISAPPROVED` (value: `"REVIEW_DISAPPROVED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `PAUSED` (value: `"PAUSED"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




