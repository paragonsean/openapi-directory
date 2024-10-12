

# CertificateRenew


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUrl** | **String** | Required if client would like to receive stateful actions via callback during certificate lifecyle |  [optional] |
|**commonName** | **String** | The common name of certificate to be secured |  [optional] |
|**csr** | **String** | Certificate Signing Request. |  [optional] |
|**period** | **Integer** | Number of years for certificate validity period, if different from previous certificate |  [optional] |
|**rootType** | [**RootTypeEnum**](#RootTypeEnum) | Root Type. Depending on certificate expiration date, SHA_1 not be allowed. Will default to SHA_2 if expiration date exceeds sha1 allowed date |  [optional] |
|**subjectAlternativeNames** | **Set&lt;String&gt;** | Only used for UCC products. An array of subject alternative names to include in certificate. Not including a subject alternative name that was in the previous certificate will remove it from the renewed certificate. |  [optional] |



## Enum: RootTypeEnum

| Name | Value |
|---- | -----|
| GODADDY_SHA_1 | &quot;GODADDY_SHA_1&quot; |
| GODADDY_SHA_2 | &quot;GODADDY_SHA_2&quot; |
| STARFIELD_SHA_1 | &quot;STARFIELD_SHA_1&quot; |
| STARFIELD_SHA_2 | &quot;STARFIELD_SHA_2&quot; |



