

# NumbersV2AuthorizationDocumentDependentHostedNumberOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**addressSid** | **String** | A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. |  [optional] |
|**bulkHostingRequestSid** | **String** | A 34 character string that uniquely identifies the bulk hosting request associated with this HostedNumberOrder. |  [optional] |
|**capabilities** | [**NumbersV2AuthorizationDocumentDependentHostedNumberOrderCapabilities**](NumbersV2AuthorizationDocumentDependentHostedNumberOrderCapabilities.md) |  |  [optional] |
|**ccEmails** | **List&lt;String&gt;** | Email recipients who will be informed when an Authorization Document has been sent and signed |  [optional] |
|**contactPhoneNumber** | **String** | The contact phone number of the person authorized to sign the Authorization Document. |  [optional] |
|**contactTitle** | **String** | The title of the person authorized to sign the Authorization Document for this phone number. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**email** | **String** | Email of the owner of this phone number that is being hosted. |  [optional] |
|**failureReason** | **String** | A message that explains why a hosted_number_order went to status \&quot;action-required\&quot; |  [optional] |
|**friendlyName** | **String** | A human readable description of this resource, up to 128 characters. |  [optional] |
|**incomingPhoneNumberSid** | **String** | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. |  [optional] |
|**nextStep** | **String** | The next step you need to take to complete the hosted number order and request it successfully. |  [optional] |
|**phoneNumber** | **String** | An E164 formatted phone number hosted by this HostedNumberOrder. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this Authorization Document |  [optional] |
|**signingDocumentSid** | **String** | A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder. |  [optional] |
|**status** | **DependentHostedNumberOrderEnumStatus** |  |  [optional] |



