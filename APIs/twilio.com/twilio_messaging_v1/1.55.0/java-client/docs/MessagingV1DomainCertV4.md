

# MessagingV1DomainCertV4


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certInValidation** | **Object** | Optional JSON field describing the status and upload date of a new certificate in the process of validation |  [optional] |
|**certificateSid** | **String** | The unique string that we created to identify this Certificate resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | Date that this Domain was registered to the Twilio platform to create a new Domain object. |  [optional] |
|**dateExpires** | **OffsetDateTime** | Date that the private certificate associated with this domain expires. You will need to update the certificate before that date to ensure your shortened links will continue to work. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | Date that this Domain was last updated. |  [optional] |
|**domainName** | **URI** | Full url path for this domain. |  [optional] |
|**domainSid** | **String** | The unique string that we created to identify the Domain resource. |  [optional] |
|**url** | **URI** |  |  [optional] |



