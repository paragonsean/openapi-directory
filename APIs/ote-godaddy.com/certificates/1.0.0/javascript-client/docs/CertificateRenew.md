# OpenapiJsClient.CertificateRenew

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | Required if client would like to receive stateful actions via callback during certificate lifecyle | [optional] 
**commonName** | **String** | The common name of certificate to be secured | [optional] [default to &#39;Existing common name&#39;]
**csr** | **String** | Certificate Signing Request. | [optional] [default to &#39;Existing CSR&#39;]
**period** | **Number** | Number of years for certificate validity period, if different from previous certificate | [optional] [default to 0]
**rootType** | **String** | Root Type. Depending on certificate expiration date, SHA_1 not be allowed. Will default to SHA_2 if expiration date exceeds sha1 allowed date | [optional] [default to &#39;GODADDY_SHA_1&#39;]
**subjectAlternativeNames** | **[String]** | Only used for UCC products. An array of subject alternative names to include in certificate. Not including a subject alternative name that was in the previous certificate will remove it from the renewed certificate. | [optional] 



## Enum: RootTypeEnum


* `GODADDY_SHA_1` (value: `"GODADDY_SHA_1"`)

* `GODADDY_SHA_2` (value: `"GODADDY_SHA_2"`)

* `STARFIELD_SHA_1` (value: `"STARFIELD_SHA_1"`)

* `STARFIELD_SHA_2` (value: `"STARFIELD_SHA_2"`)




