# CertificateAuthorityApi.KeyUsageOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certSign** | **Boolean** | The key may be used to sign certificates. | [optional] 
**contentCommitment** | **Boolean** | The key may be used for cryptographic commitments. Note that this may also be referred to as \&quot;non-repudiation\&quot;. | [optional] 
**crlSign** | **Boolean** | The key may be used sign certificate revocation lists. | [optional] 
**dataEncipherment** | **Boolean** | The key may be used to encipher data. | [optional] 
**decipherOnly** | **Boolean** | The key may be used to decipher only. | [optional] 
**digitalSignature** | **Boolean** | The key may be used for digital signatures. | [optional] 
**encipherOnly** | **Boolean** | The key may be used to encipher only. | [optional] 
**keyAgreement** | **Boolean** | The key may be used in a key agreement protocol. | [optional] 
**keyEncipherment** | **Boolean** | The key may be used to encipher other keys. | [optional] 


