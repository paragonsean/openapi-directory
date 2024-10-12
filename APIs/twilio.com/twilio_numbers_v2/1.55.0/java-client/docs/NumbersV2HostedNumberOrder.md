

# NumbersV2HostedNumberOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | A 34 character string that uniquely identifies the account. |  [optional] |
|**addressSid** | **String** | A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. |  [optional] |
|**bulkHostingRequestSid** | **String** | A 34 character string that uniquely identifies the bulk hosting request associated with this HostedNumberOrder. |  [optional] |
|**capabilities** | [**NumbersV2HostedNumberOrderCapabilities**](NumbersV2HostedNumberOrderCapabilities.md) |  |  [optional] |
|**ccEmails** | **List&lt;String&gt;** | A list of emails that LOA document for this HostedNumberOrder will be carbon copied to. |  [optional] |
|**contactPhoneNumber** | **String** | The contact phone number of the person authorized to sign the Authorization Document. |  [optional] |
|**contactTitle** | **String** | The title of the person authorized to sign the Authorization Document for this phone number. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**email** | **String** | Email of the owner of this phone number that is being hosted. |  [optional] |
|**failureReason** | **String** | A message that explains why a hosted_number_order went to status \&quot;action-required\&quot; |  [optional] |
|**friendlyName** | **String** | A 128 character string that is a human-readable text that describes this resource. |  [optional] |
|**incomingPhoneNumberSid** | **String** | A 34 character string that uniquely identifies the [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the phone number being hosted. |  [optional] |
|**nextStep** | **String** | The next step you need to take to complete the hosted number order and request it successfully. |  [optional] |
|**phoneNumber** | **String** | Phone number to be hosted. This must be in [E.164](https://en.wikipedia.org/wiki/E.164) format, e.g., +16175551212 |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this HostedNumberOrder. |  [optional] |
|**signingDocumentSid** | **String** | A 34 character string that uniquely identifies the [Authorization Document](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource) the user needs to sign. |  [optional] |
|**status** | **HostedNumberOrderEnumStatus** |  |  [optional] |
|**url** | **URI** | The URL of this HostedNumberOrder. |  [optional] |



