# GmailApi.CseKeyPair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableTime** | **String** | Output only. If a key pair is set to &#x60;DISABLED&#x60;, the time that the key pair&#39;s state changed from &#x60;ENABLED&#x60; to &#x60;DISABLED&#x60;. This field is present only when the key pair is in state &#x60;DISABLED&#x60;. | [optional] [readonly] 
**enablementState** | **String** | Output only. The current state of the key pair. | [optional] [readonly] 
**keyPairId** | **String** | Output only. The immutable ID for the client-side encryption S/MIME key pair. | [optional] [readonly] 
**pem** | **String** | Output only. The public key and its certificate chain, in [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format. | [optional] [readonly] 
**pkcs7** | **String** | Input only. The public key and its certificate chain. The chain must be in [PKCS#7](https://en.wikipedia.org/wiki/PKCS_7) format and use PEM encoding and ASCII armor. | [optional] 
**privateKeyMetadata** | [**[CsePrivateKeyMetadata]**](CsePrivateKeyMetadata.md) | Metadata for instances of this key pair&#39;s private key. | [optional] 
**subjectEmailAddresses** | **[String]** | Output only. The email address identities that are specified on the leaf certificate. | [optional] [readonly] 



## Enum: EnablementStateEnum


* `stateUnspecified` (value: `"stateUnspecified"`)

* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




