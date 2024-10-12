

# BuyOnGoogleProgramStatus

Response message for the GetProgramStatus method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessModel** | [**List&lt;BusinessModelEnum&gt;**](#List&lt;BusinessModelEnum&gt;) | The business models in which merchant participates. |  [optional] |
|**customerServicePendingEmail** | **String** | The customer service pending email. After verification this field becomes empty. |  [optional] |
|**customerServicePendingPhoneNumber** | **String** | The pending phone number specified for BuyOnGoogle program. It might be different than account level phone number. In order to update this field the customer_service_pending_phone_region_code must also be set. After verification this field becomes empty. |  [optional] |
|**customerServicePendingPhoneRegionCode** | **String** | Two letter country code for the pending phone number, for example &#x60;CA&#x60; for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. In order to update this field the customer_service_pending_phone_number must also be set. After verification this field becomes empty. |  [optional] |
|**customerServiceVerifiedEmail** | **String** | Output only. The customer service verified email. |  [optional] [readonly] |
|**customerServiceVerifiedPhoneNumber** | **String** | Output only. The verified phone number specified for BuyOnGoogle program. It might be different than account level phone number. |  [optional] [readonly] |
|**customerServiceVerifiedPhoneRegionCode** | **String** | Output only. Two letter country code for the verified phone number, for example &#x60;CA&#x60; for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. |  [optional] [readonly] |
|**onlineSalesChannel** | [**OnlineSalesChannelEnum**](#OnlineSalesChannelEnum) | The channels through which the merchant is selling. |  [optional] |
|**participationStage** | [**ParticipationStageEnum**](#ParticipationStageEnum) | Output only. The current participation stage for the program. |  [optional] [readonly] |



## Enum: List&lt;BusinessModelEnum&gt;

| Name | Value |
|---- | -----|
| BUSINESS_MODEL_UNSPECIFIED | &quot;BUSINESS_MODEL_UNSPECIFIED&quot; |
| MANUFACTURER | &quot;MANUFACTURER&quot; |
| IMPORTER | &quot;IMPORTER&quot; |
| RESELLER | &quot;RESELLER&quot; |
| OTHER | &quot;OTHER&quot; |



## Enum: OnlineSalesChannelEnum

| Name | Value |
|---- | -----|
| ONLINE_SALES_CHANNEL_UNSPECIFIED | &quot;ONLINE_SALES_CHANNEL_UNSPECIFIED&quot; |
| GOOGLE_EXCLUSIVE | &quot;GOOGLE_EXCLUSIVE&quot; |
| GOOGLE_AND_OTHER_WEBSITES | &quot;GOOGLE_AND_OTHER_WEBSITES&quot; |



## Enum: ParticipationStageEnum

| Name | Value |
|---- | -----|
| PROGRAM_PARTICIPATION_STAGE_UNSPECIFIED | &quot;PROGRAM_PARTICIPATION_STAGE_UNSPECIFIED&quot; |
| NOT_ELIGIBLE | &quot;NOT_ELIGIBLE&quot; |
| ELIGIBLE | &quot;ELIGIBLE&quot; |
| ONBOARDING | &quot;ONBOARDING&quot; |
| ELIGIBLE_FOR_REVIEW | &quot;ELIGIBLE_FOR_REVIEW&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| REVIEW_DISAPPROVED | &quot;REVIEW_DISAPPROVED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



