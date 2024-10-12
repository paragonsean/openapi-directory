# TwilioNumbers.NumbersV1PortingBulkPortability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetimeCreated** | **Date** | The date that the Portability check was created, given in ISO 8601 format. | [optional] 
**phoneNumbers** | **[Object]** | Contains a list with all the information of the requested phone numbers. Each phone number contains the following properties: &#x60;phone_number&#x60;: The phone number which portability is to be checked. &#x60;portable&#x60;: Boolean flag specifying if phone number is portable or not. &#x60;not_portable_reason&#x60;: Reason why the phone number cannot be ported into Twilio, &#x60;null&#x60; otherwise. &#x60;not_portable_reason_code&#x60;: The Portability Reason Code for the phone number if it cannot be ported in Twilio, &#x60;null&#x60; otherwise. &#x60;pin_and_account_number_required&#x60;: Boolean flag specifying if PIN and account number is required for the phone number. &#x60;number_type&#x60;: The type of the requested phone number. &#x60;country&#x60; Country the phone number belongs to. &#x60;messaging_carrier&#x60; Current messaging carrier of the phone number. &#x60;voice_carrier&#x60; Current voice carrier of the phone number. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this Portability check. | [optional] 
**status** | [**PortingBulkPortabilityEnumStatus**](PortingBulkPortabilityEnumStatus.md) |  | [optional] 
**url** | **String** | This is the url of the request that you&#39;re trying to reach out to locate the resource. | [optional] 


