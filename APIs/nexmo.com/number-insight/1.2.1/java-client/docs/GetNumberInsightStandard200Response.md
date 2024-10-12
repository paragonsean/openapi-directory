

# GetNumberInsightStandard200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryCode** | **String** | Two character country code for &#x60;number&#x60;. This is in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |  [optional] |
|**countryCodeIso3** | **String** | Three character country code for &#x60;number&#x60;. This is in [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format. |  [optional] |
|**countryName** | **String** | The full name of the country that &#x60;number&#x60; is registered in. |  [optional] |
|**countryPrefix** | **String** | The numeric prefix for the country that &#x60;number&#x60; is registered in. |  [optional] |
|**internationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in international format. |  [optional] |
|**nationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in the format used by the country the number belongs to. |  [optional] |
|**requestId** | **String** | The unique identifier for your request. This is a alphanumeric string up to 40 characters. |  [optional] |
|**status** | **NiBasicStatus** |  |  [optional] |
|**statusMessage** | **String** | The status description of your request. |  [optional] |
|**callerIdentity** | [**NiCallerIdentity**](NiCallerIdentity.md) |  |  [optional] |
|**callerName** | **String** | Full name of the person or business who owns the phone number. &#x60;unknown&#x60; if this information is not available. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**callerType** | [**CallerTypeEnum**](#CallerTypeEnum) | The value will be &#x60;business&#x60; if the owner of a phone number is a business. If the owner is an individual the value will be &#x60;consumer&#x60;. The value will be &#x60;unknown&#x60; if this information is not available. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**currentCarrier** | [**NiCurrentCarrierProperties**](NiCurrentCarrierProperties.md) |  |  [optional] |
|**firstName** | **String** | First name of the person who owns the phone number if the owner is an individual. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**lastName** | **String** | Last name of the person who owns the phone number if the owner is an individual. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**originalCarrier** | [**NiInitialCarrierProperties**](NiInitialCarrierProperties.md) |  |  [optional] |
|**ported** | [**PortedEnum**](#PortedEnum) | If the user has changed carrier for &#x60;number&#x60;. The assumed status means that the information supplier has replied to the request but has not said explicitly that the number is ported. |  [optional] |
|**refundPrice** | **String** | If there is an internal lookup error, the &#x60;refund_price&#x60; will reflect the lookup price. If &#x60;cnam&#x60; is requested for a non-US number the &#x60;refund_price&#x60; will reflect the &#x60;cnam&#x60; price. If both of these conditions occur, &#x60;refund_price&#x60; is the sum of the lookup price and &#x60;cnam&#x60; price. |  [optional] |
|**remainingBalance** | **String** | Your account balance in EUR after this request. |  [optional] |
|**requestPrice** | **String** | The amount in EUR charged to your account. |  [optional] |



## Enum: CallerTypeEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CONSUMER | &quot;consumer&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: PortedEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| PORTED | &quot;ported&quot; |
| NOT_PORTED | &quot;not_ported&quot; |
| ASSUMED_NOT_PORTED | &quot;assumed_not_ported&quot; |
| ASSUMED_PORTED | &quot;assumed_ported&quot; |
| NULL | &quot;null&quot; |



