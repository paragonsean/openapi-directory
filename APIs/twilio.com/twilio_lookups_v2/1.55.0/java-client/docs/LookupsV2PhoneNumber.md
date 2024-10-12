

# LookupsV2PhoneNumber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callForwarding** | **Object** | An object that contains information on the unconditional call forwarding status of mobile phone number. |  [optional] |
|**callerName** | **Object** | An object that contains caller name information based on [CNAM](https://support.twilio.com/hc/en-us/articles/360051670533-Getting-Started-with-CNAM-Caller-ID). |  [optional] |
|**callingCountryCode** | **String** | International dialing prefix of the phone number defined in the E.164 standard. |  [optional] |
|**countryCode** | **String** | The phone number&#39;s [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |  [optional] |
|**identityMatch** | **Object** | An object that contains identity match information. The result of comparing user-provided information including name, address, date of birth, national ID, against authoritative phone-based data sources |  [optional] |
|**lineStatus** | **Object** | An object that contains line status information for a mobile phone number. |  [optional] |
|**lineTypeIntelligence** | **Object** | An object that contains line type information including the carrier name, mobile country code, and mobile network code. |  [optional] |
|**nationalFormat** | **String** | The phone number in [national format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers). |  [optional] |
|**phoneNumber** | **String** | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. |  [optional] |
|**phoneNumberQualityScore** | **Object** | An object that contains information of a mobile phone number quality score. Quality score will return a risk score about the phone number. |  [optional] |
|**reassignedNumber** | **Object** | An object that contains reassigned number information. Reassigned Numbers will return a phone number&#39;s reassignment status given a phone number and date |  [optional] |
|**simSwap** | **Object** | An object that contains information on the last date the subscriber identity module (SIM) was changed for a mobile phone number. |  [optional] |
|**smsPumpingRisk** | **Object** | An object that contains information on if a phone number has been currently or previously blocked by Verify Fraud Guard for receiving malicious SMS pumping traffic as well as other signals associated with risky carriers and low conversion rates. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**valid** | **Boolean** | Boolean which indicates if the phone number is in a valid range that can be freely assigned by a carrier to a user. |  [optional] |
|**validationErrors** | **List&lt;PhoneNumberEnumValidationError&gt;** | Contains reasons why a phone number is invalid. Possible values: TOO_SHORT, TOO_LONG, INVALID_BUT_POSSIBLE, INVALID_COUNTRY_CODE, INVALID_LENGTH, NOT_A_NUMBER. |  [optional] |



