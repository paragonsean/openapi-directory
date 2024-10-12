

# CertificateReissue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUrl** | **String** | Required if client would like to receive stateful action via callback during certificate lifecyle |  [optional] |
|**commonName** | **String** | The common name of certificate to be secured |  [optional] |
|**csr** | **String** | Certificate Signing Request. |  [optional] |
|**delayExistingRevoke** | **Integer** | In hours, time to delay revoking existing certificate after issuance of new certificate. If revokeExistingCertOnIssuance is enabled, this value will be ignored |  [optional] |
|**forceDomainRevetting** | **Set&lt;String&gt;** | Optional field. Domain verification will be required for each domain listed here. Specify a value of * to indicate that all domains associated with the request should have their domain information reverified. |  [optional] |
|**rootType** | [**RootTypeEnum**](#RootTypeEnum) | Root Type. Depending on certificate expiration date, SHA_1 not be allowed. Will default to SHA_2 if expiration date exceeds sha1 allowed date |  [optional] |
|**subjectAlternativeNames** | **Set&lt;String&gt;** | Only used for UCC products. An array of subject alternative names to include in certificate. |  [optional] |



## Enum: RootTypeEnum

| Name | Value |
|---- | -----|
| GODADDY_SHA_1 | &quot;GODADDY_SHA_1&quot; |
| GODADDY_SHA_2 | &quot;GODADDY_SHA_2&quot; |
| STARFIELD_SHA_1 | &quot;STARFIELD_SHA_1&quot; |
| STARFIELD_SHA_2 | &quot;STARFIELD_SHA_2&quot; |



