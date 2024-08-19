# ThePlaidApi.LinkTokenCreateRequestUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**UserAddress**](UserAddress.md) |  | [optional] 
**clientUserId** | **String** | A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the &#x60;client_user_id&#x60;. It is currently used as a means of searching logs for the given user in the Plaid Dashboard. | 
**dateOfBirth** | **Date** | To be provided in the format \&quot;yyyy-mm-dd\&quot;. Not currently used. | [optional] 
**emailAddress** | **String** | The user&#39;s email address. This field is optional, but required to enable the [pre-authenticated returning user flow](https://plaid.com/docs/link/returning-user/#pre-authenticated-rux). | [optional] 
**emailAddressVerifiedTime** | **Date** | The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDThh:mm:ssZ&#x60;). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: &#x60;2020-01-01T00:00:00Z&#x60; | [optional] 
**idNumber** | [**UserIDNumber**](UserIDNumber.md) |  | [optional] 
**legalName** | **String** | The user&#39;s full legal name, used for [micro-deposit based verification flows](https://plaid.com/docs/auth/coverage/). For a small number of customers on legacy flows, providing this field is required to enable micro-deposit-based flows. For all other customers, this field is optional, but providing the user&#39;s name in this field when using micro-deposit-based verification will enable certain risk checks and can reduce micro-deposit fraud. | [optional] 
**name** | [**LinkTokenCreateRequestUserName**](LinkTokenCreateRequestUserName.md) |  | [optional] 
**phoneNumber** | **String** | The user&#39;s phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](https://plaid.com/docs/link/returning-user). | [optional] 
**phoneNumberVerifiedTime** | **Date** | The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDThh:mm:ssZ&#x60;). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: &#x60;2020-01-01T00:00:00Z&#x60;  | [optional] 
**ssn** | **String** | To be provided in the format \&quot;ddd-dd-dddd\&quot;. Not currently used. | [optional] 


