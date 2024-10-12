# GmailApi.SmimeInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptedKeyPassword** | **String** | Encrypted key password, when key is encrypted. | [optional] 
**expiration** | **String** | When the certificate expires (in milliseconds since epoch). | [optional] 
**id** | **String** | The immutable ID for the SmimeInfo. | [optional] 
**isDefault** | **Boolean** | Whether this SmimeInfo is the default one for this user&#39;s send-as address. | [optional] 
**issuerCn** | **String** | The S/MIME certificate issuer&#39;s common name. | [optional] 
**pem** | **String** | PEM formatted X509 concatenated certificate string (standard base64 encoding). Format used for returning key, which includes public key as well as certificate chain (not private key). | [optional] 
**pkcs12** | **Blob** | PKCS#12 format containing a single private/public key pair and certificate chain. This format is only accepted from client for creating a new SmimeInfo and is never returned, because the private key is not intended to be exported. PKCS#12 may be encrypted, in which case encryptedKeyPassword should be set appropriately. | [optional] 


