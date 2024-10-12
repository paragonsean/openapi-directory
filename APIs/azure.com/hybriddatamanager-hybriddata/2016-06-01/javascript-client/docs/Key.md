# HybridDataManagementClient.Key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionChunkSizeInBytes** | **Number** | The maximum byte size that can be encrypted by the key. For a key size larger than the size, break into chunks and encrypt each chunk, append each encrypted chunk with : to mark the end of the chunk. | 
**keyExponent** | **String** | Exponent of the encryption key. | 
**keyModulus** | **String** | Modulus of the encryption key. | 


