

# NiResponseJsonAdvancedAsync

Advanced Response (Async)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callerIdentity** | [**NiCallerIdentity**](NiCallerIdentity.md) |  |  [optional] |
|**countryCode** | **String** | Two character country code for &#x60;number&#x60;. This is in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |  |
|**countryCodeIso3** | **String** | Three character country code for &#x60;number&#x60;. This is in [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format. |  |
|**countryName** | **String** | The full name of the country that &#x60;number&#x60; is registered in. |  |
|**countryPrefix** | **String** | The numeric prefix for the country that &#x60;number&#x60; is registered in. |  |
|**currentCarrier** | [**NiCurrentCarrierProperties**](NiCurrentCarrierProperties.md) |  |  [optional] |
|**internationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in international format. |  |
|**lookupOutcome** | [**LookupOutcomeEnum**](#LookupOutcomeEnum) | Shows if all information about a phone number has been returned. Possible values:  Code | Text --- | --- 0 | Success 1 | Partial success - some fields populated 2 | Failed  |  [optional] |
|**lookupOutcomeMessage** | **String** | Shows if all information about a phone number has been returned. |  [optional] |
|**nationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in the format used by the country the number belongs to. |  |
|**originalCarrier** | [**NiInitialCarrierProperties**](NiInitialCarrierProperties.md) |  |  [optional] |
|**ported** | [**PortedEnum**](#PortedEnum) | If the user has changed carrier for &#x60;number&#x60;. The assumed status means that the information supplier has replied to the request but has not said explicitly that the number is ported. |  [optional] |
|**reachable** | [**ReachableEnum**](#ReachableEnum) | Can you call &#x60;number&#x60; now. This is applicable to mobile numbers only. |  [optional] |
|**refundPrice** | **String** | If there is an internal lookup error, the &#x60;refund_price&#x60; will reflect the lookup price. If &#x60;cnam&#x60; is requested for a non-US number the &#x60;refund_price&#x60; will reflect the &#x60;cnam&#x60; price. If both of these conditions occur, &#x60;refund_price&#x60; is the sum of the lookup price and &#x60;cnam&#x60; price. |  [optional] |
|**remainingBalance** | **String** | Your account balance in EUR after this request. |  [optional] |
|**requestId** | **String** | The unique identifier for your request. This is a alphanumeric string up to 40 characters. |  |
|**requestPrice** | **String** | The amount in EUR charged to your account. |  [optional] |
|**roaming** | [**NiRoaming**](NiRoaming.md) |  |  [optional] |
|**status** | **NiStandardAdvancedStatus** |  |  |
|**statusMessage** | **String** | The status description of your request. |  |
|**validNumber** | [**ValidNumberEnum**](#ValidNumberEnum) | Does &#x60;number&#x60; exist. &#x60;unknown&#x60; means the number could not be validated. &#x60;valid&#x60; means the number is valid. &#x60;not_valid&#x60; means the number is not valid. &#x60;inferred_not_valid&#x60; means that the number could not be determined as valid or invalid via an external system and the best guess is that the number is invalid. This is applicable to mobile numbers only. |  [optional] |



## Enum: LookupOutcomeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: PortedEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| PORTED | &quot;ported&quot; |
| NOT_PORTED | &quot;not_ported&quot; |
| ASSUMED_NOT_PORTED | &quot;assumed_not_ported&quot; |
| ASSUMED_PORTED | &quot;assumed_ported&quot; |
| NULL | &quot;null&quot; |



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
| INFERRED | &quot;inferred&quot; |
| INFERRED_NOT_VALID | &quot;inferred_not_valid&quot; |



