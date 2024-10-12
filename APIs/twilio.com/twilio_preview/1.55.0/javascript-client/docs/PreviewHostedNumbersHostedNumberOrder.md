# TwilioPreview.PreviewHostedNumbersHostedNumberOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | A 34 character string that uniquely identifies the account. | [optional] 
**addressSid** | **String** | A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. | [optional] 
**callDelay** | **Number** | A value between 0-30 specifying the number of seconds to delay initiating the ownership verification call. | [optional] 
**capabilities** | [**PreviewHostedNumbersHostedNumberOrderCapabilities**](PreviewHostedNumbersHostedNumberOrderCapabilities.md) |  | [optional] 
**ccEmails** | **[String]** | A list of emails that LOA document for this HostedNumberOrder will be carbon copied to. | [optional] 
**dateCreated** | **Date** | The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**email** | **String** | Email of the owner of this phone number that is being hosted. | [optional] 
**extension** | **String** | A numerical extension to be used when making the ownership verification call. | [optional] 
**failureReason** | **String** | A message that explains why a hosted_number_order went to status \&quot;action-required\&quot; | [optional] 
**friendlyName** | **String** | A 64 character string that is a human-readable text that describes this resource. | [optional] 
**incomingPhoneNumberSid** | **String** | A 34 character string that uniquely identifies the [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the phone number being hosted. | [optional] 
**phoneNumber** | **String** | Phone number to be hosted. This must be in [E.164](https://en.wikipedia.org/wiki/E.164) format, e.g., +16175551212 | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this HostedNumberOrder. | [optional] 
**signingDocumentSid** | **String** | A 34 character string that uniquely identifies the [Authorization Document](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource) the user needs to sign. | [optional] 
**status** | [**HostedNumberOrderEnumStatus**](HostedNumberOrderEnumStatus.md) |  | [optional] 
**uniqueName** | **String** | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] 
**url** | **String** | The URL of this HostedNumberOrder. | [optional] 
**verificationAttempts** | **Number** | The number of attempts made to verify ownership of the phone number that is being hosted. | [optional] 
**verificationCallSids** | **[String]** | A list of 34 character strings that are unique identifiers for the calls placed as part of ownership verification. | [optional] 
**verificationCode** | **String** | A verification code provided in the response for a user to enter when they pick up the phone call. | [optional] 
**verificationDocumentSid** | **String** | A 34 character string that uniquely identifies the Identity Document resource that represents the document for verifying ownership of the number to be hosted. | [optional] 
**verificationType** | [**HostedNumberOrderEnumVerificationType**](HostedNumberOrderEnumVerificationType.md) |  | [optional] 


