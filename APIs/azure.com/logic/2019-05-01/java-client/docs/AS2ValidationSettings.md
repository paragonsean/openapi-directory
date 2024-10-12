

# AS2ValidationSettings

The AS2 agreement validation settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkCertificateRevocationListOnReceive** | **Boolean** | The value indicating whether to check for certificate revocation list on receive. |  |
|**checkCertificateRevocationListOnSend** | **Boolean** | The value indicating whether to check for certificate revocation list on send. |  |
|**checkDuplicateMessage** | **Boolean** | The value indicating whether to check for duplicate message. |  |
|**compressMessage** | **Boolean** | The value indicating whether the message has to be compressed. |  |
|**encryptMessage** | **Boolean** | The value indicating whether the message has to be encrypted. |  |
|**encryptionAlgorithm** | **EncryptionAlgorithm** |  |  |
|**interchangeDuplicatesValidityDays** | **Integer** | The number of days to look back for duplicate interchange. |  |
|**overrideMessageProperties** | **Boolean** | The value indicating whether to override incoming message properties with those in agreement. |  |
|**signMessage** | **Boolean** | The value indicating whether the message has to be signed. |  |
|**signingAlgorithm** | **SigningAlgorithm** |  |  [optional] |



