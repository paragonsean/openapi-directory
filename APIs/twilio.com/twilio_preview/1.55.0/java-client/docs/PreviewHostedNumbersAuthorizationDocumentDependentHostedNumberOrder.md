

# PreviewHostedNumbersAuthorizationDocumentDependentHostedNumberOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**addressSid** | **String** | A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. |  [optional] |
|**callDelay** | **Integer** | A value between 0-30 specifying the number of seconds to delay initiating the ownership verification call. |  [optional] |
|**capabilities** | [**PreviewHostedNumbersAuthorizationDocumentDependentHostedNumberOrderCapabilities**](PreviewHostedNumbersAuthorizationDocumentDependentHostedNumberOrderCapabilities.md) |  |  [optional] |
|**ccEmails** | **List&lt;String&gt;** | Email recipients who will be informed when an Authorization Document has been sent and signed |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**email** | **String** | Email of the owner of this phone number that is being hosted. |  [optional] |
|**extension** | **String** | A numerical extension to be used when making the ownership verification call. |  [optional] |
|**failureReason** | **String** | A message that explains why a hosted_number_order went to status \&quot;action-required\&quot; |  [optional] |
|**friendlyName** | **String** | A human readable description of this resource, up to 64 characters. |  [optional] |
|**incomingPhoneNumberSid** | **String** | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. |  [optional] |
|**phoneNumber** | **String** | An E164 formatted phone number hosted by this HostedNumberOrder. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this Authorization Document |  [optional] |
|**signingDocumentSid** | **String** | A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder. |  [optional] |
|**status** | **DependentHostedNumberOrderEnumStatus** |  |  [optional] |
|**uniqueName** | **String** | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. |  [optional] |
|**verificationAttempts** | **Integer** | The number of attempts made to verify ownership of the phone number that is being hosted. |  [optional] |
|**verificationCallSids** | **List&lt;String&gt;** | A list of 34 character strings that are unique identifiers for the calls placed as part of ownership verification. |  [optional] |
|**verificationCode** | **String** | The digits passed during the ownership verification call. |  [optional] |
|**verificationDocumentSid** | **String** | A 34 character string that uniquely identifies the Identity Document resource that represents the document for verifying ownership of the number to be hosted. |  [optional] |
|**verificationType** | **DependentHostedNumberOrderEnumVerificationType** |  |  [optional] |



