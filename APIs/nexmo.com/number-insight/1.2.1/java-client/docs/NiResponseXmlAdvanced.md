

# NiResponseXmlAdvanced

Advanced

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callerIdentity** | [**NiResponseXmlAdvancedCallerIdentity**](NiResponseXmlAdvancedCallerIdentity.md) |  |  [optional] |
|**callerName** | **String** | Full name of the person or business who owns the phone number. &#x60;unknown&#x60; if this information is not available. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**callerType** | [**CallerTypeEnum**](#CallerTypeEnum) | The value will be &#x60;business&#x60; if the owner of a phone number is a business. If the owner is an individual the value will be &#x60;consumer&#x60;. The value will be &#x60;unknown&#x60; if this information is not available. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**currentCarrier** | [**NiCurrentCarrierProperties**](NiCurrentCarrierProperties.md) |  |  [optional] |
|**error** | [**NiResponseXmlAdvancedError**](NiResponseXmlAdvancedError.md) |  |  [optional] |
|**firsName** | **String** | First name of the person who owns the phone number if the owner is an individual. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**internationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in international format. |  [optional] |
|**ipWarnings** | **String** | This property is deprecated and can safely be ignored. |  [optional] |
|**lastName** | **String** | Last name of the person who owns the phone number if the owner is an individual. This parameter is only present if &#x60;cnam&#x60; had a value of &#x60;true&#x60; within the request. |  [optional] |
|**localNumber** | [**NiResponseXmlAdvancedLocalNumber**](NiResponseXmlAdvancedLocalNumber.md) |  |  [optional] |
|**lookupOutcome** | [**NiResponseXmlAdvancedLookupOutcome**](NiResponseXmlAdvancedLookupOutcome.md) |  |  [optional] |
|**originalCarrier** | [**NiInitialCarrierProperties**](NiInitialCarrierProperties.md) |  |  [optional] |
|**ported** | [**NiResponseXmlAdvancedPorted**](NiResponseXmlAdvancedPorted.md) |  |  [optional] |
|**reachable** | [**ReachableEnum**](#ReachableEnum) | Can you call &#x60;number&#x60; now. This is applicable to mobile numbers only. |  [optional] |
|**remainingBalance** | **String** | Your account balance in EUR after this request. |  [optional] |
|**requestId** | **String** | The unique identifier for your request. This is a alphanumeric string up to 40 characters. |  [optional] |
|**requestPrice** | **String** | If there is an internal lookup error, the &#x60;refund_price&#x60; will reflect the lookup price. If &#x60;cnam&#x60; is requested for a non-US number the &#x60;refund_price&#x60; will reflect the &#x60;cnam&#x60; price. If both of these conditions occur, &#x60;refund_price&#x60; is the sum of the lookup price and &#x60;cnam&#x60; price. |  [optional] |
|**roaming** | [**NiRoaming**](NiRoaming.md) |  |  [optional] |
|**validNumber** | [**ValidNumberEnum**](#ValidNumberEnum) | Does &#x60;number&#x60; exist. &#x60;unknown&#x60; means the number could not be validated. &#x60;valid&#x60; means the number is valid. &#x60;not_valid&#x60; means the number is not valid. &#x60;inferred_not_valid&#x60; means that the number could not be determined as valid or invalid via an external system and the best guess is that the number is invalid. This is applicable to mobile numbers only. |  [optional] |



## Enum: CallerTypeEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CONSUMER | &quot;consumer&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: ReachableEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| REACHABLE | &quot;reachable&quot; |
| UNDELIVERABLE | &quot;undeliverable&quot; |
| ABSENT | &quot;absent&quot; |
| BAD_NUMBER | &quot;bad_number&quot; |
| BLACKLISTED | &quot;blacklisted&quot; |
| NULL | &quot;null&quot; |



## Enum: ValidNumberEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| VALID | &quot;valid&quot; |
| NOT_VALID | &quot;not_valid&quot; |
| INFERRED_NOT_VALID | &quot;inferred_not_valid&quot; |



