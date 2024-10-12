# KeyVaultClient.X509CertificateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ekus** | **[String]** | The enhanced key usage. | [optional] 
**keyUsage** | **[String]** | List of key usages. | [optional] 
**sans** | [**SubjectAlternativeNames**](SubjectAlternativeNames.md) |  | [optional] 
**subject** | **String** | The subject name. Should be a valid X509 distinguished Name. | [optional] 
**validityMonths** | **Number** | The duration that the certificate is valid in months. | [optional] 



## Enum: [KeyUsageEnum]


* `digitalSignature` (value: `"digitalSignature"`)

* `nonRepudiation` (value: `"nonRepudiation"`)

* `keyEncipherment` (value: `"keyEncipherment"`)

* `dataEncipherment` (value: `"dataEncipherment"`)

* `keyAgreement` (value: `"keyAgreement"`)

* `keyCertSign` (value: `"keyCertSign"`)

* `cRLSign` (value: `"cRLSign"`)

* `encipherOnly` (value: `"encipherOnly"`)

* `decipherOnly` (value: `"decipherOnly"`)




