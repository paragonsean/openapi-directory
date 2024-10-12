# LogicManagementClient.AS2ValidationSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkCertificateRevocationListOnReceive** | **Boolean** | The value indicating whether to check for certificate revocation list on receive. | [optional] 
**checkCertificateRevocationListOnSend** | **Boolean** | The value indicating whether to check for certificate revocation list on send. | [optional] 
**checkDuplicateMessage** | **Boolean** | The value indicating whether to check for duplicate message. | [optional] 
**compressMessage** | **Boolean** | The value indicating whether the message has to be compressed. | [optional] 
**encryptMessage** | **Boolean** | The value indicating whether the message has to be encrypted. | [optional] 
**encryptionAlgorithm** | [**EncryptionAlgorithm**](EncryptionAlgorithm.md) |  | [optional] 
**interchangeDuplicatesValidityDays** | **Number** | The number of days to look back for duplicate interchange. | [optional] 
**overrideMessageProperties** | **Boolean** | The value indicating whether to override incoming message properties with those in agreement. | [optional] 
**signMessage** | **Boolean** | The value indicating whether the message has to be signed. | [optional] 


