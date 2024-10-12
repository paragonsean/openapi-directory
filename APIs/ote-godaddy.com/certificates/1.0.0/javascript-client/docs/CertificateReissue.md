# OpenapiJsClient.CertificateReissue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | Required if client would like to receive stateful action via callback during certificate lifecyle | [optional] 
**commonName** | **String** | The common name of certificate to be secured | [optional] [default to &#39;Existing common name&#39;]
**csr** | **String** | Certificate Signing Request. | [optional] [default to &#39;Existing CSR&#39;]
**delayExistingRevoke** | **Number** | In hours, time to delay revoking existing certificate after issuance of new certificate. If revokeExistingCertOnIssuance is enabled, this value will be ignored | [optional] [default to 72]
**forceDomainRevetting** | **[String]** | Optional field. Domain verification will be required for each domain listed here. Specify a value of * to indicate that all domains associated with the request should have their domain information reverified. | [optional] 
**rootType** | **String** | Root Type. Depending on certificate expiration date, SHA_1 not be allowed. Will default to SHA_2 if expiration date exceeds sha1 allowed date | [optional] [default to &#39;GODADDY_SHA_1&#39;]
**subjectAlternativeNames** | **[String]** | Only used for UCC products. An array of subject alternative names to include in certificate. | [optional] 



## Enum: RootTypeEnum


* `GODADDY_SHA_1` (value: `"GODADDY_SHA_1"`)

* `GODADDY_SHA_2` (value: `"GODADDY_SHA_2"`)

* `STARFIELD_SHA_1` (value: `"STARFIELD_SHA_1"`)

* `STARFIELD_SHA_2` (value: `"STARFIELD_SHA_2"`)




