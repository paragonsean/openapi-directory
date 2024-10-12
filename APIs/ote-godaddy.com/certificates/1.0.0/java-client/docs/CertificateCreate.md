

# CertificateCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUrl** | **String** | Required if client would like to receive stateful actions via callback during certificate lifecyle |  [optional] |
|**commonName** | **String** | Name to be secured in certificate. If provided, CN field in CSR will be ignored. |  [optional] |
|**contact** | [**CertificateContact**](CertificateContact.md) |  |  |
|**csr** | **String** | Certificate Signing Request |  |
|**intelVPro** | **Boolean** | Only used for OV |  [optional] |
|**organization** | [**CertificateOrganizationCreate**](CertificateOrganizationCreate.md) |  |  [optional] |
|**period** | **Integer** | Number of years for certificate validity period |  |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) | Type of product requesting a certificate. Only required non-renewal |  |
|**rootType** | [**RootTypeEnum**](#RootTypeEnum) | Root Type. Depending on certificate expiration date, SHA_1 not be allowed. Will default to SHA_2 if expiration date exceeds sha1 allowed date |  [optional] |
|**slotSize** | [**SlotSizeEnum**](#SlotSizeEnum) | Number of subject alternative names(SAN) to be included in certificate  |  [optional] |
|**subjectAlternativeNames** | **Set&lt;String&gt;** | Subject Alternative names. Collection of subjectAlternativeNames to be included in certificate. |  [optional] |



## Enum: ProductTypeEnum

| Name | Value |
|---- | -----|
| DV_SSL | &quot;DV_SSL&quot; |
| DV_WILDCARD_SSL | &quot;DV_WILDCARD_SSL&quot; |
| EV_SSL | &quot;EV_SSL&quot; |
| OV_CS | &quot;OV_CS&quot; |
| OV_DS | &quot;OV_DS&quot; |
| OV_SSL | &quot;OV_SSL&quot; |
| OV_WILDCARD_SSL | &quot;OV_WILDCARD_SSL&quot; |
| UCC_DV_SSL | &quot;UCC_DV_SSL&quot; |
| UCC_EV_SSL | &quot;UCC_EV_SSL&quot; |
| UCC_OV_SSL | &quot;UCC_OV_SSL&quot; |



## Enum: RootTypeEnum

| Name | Value |
|---- | -----|
| GODADDY_SHA_1 | &quot;GODADDY_SHA_1&quot; |
| GODADDY_SHA_2 | &quot;GODADDY_SHA_2&quot; |
| STARFIELD_SHA_1 | &quot;STARFIELD_SHA_1&quot; |
| STARFIELD_SHA_2 | &quot;STARFIELD_SHA_2&quot; |



## Enum: SlotSizeEnum

| Name | Value |
|---- | -----|
| FIVE | &quot;FIVE&quot; |
| TEN | &quot;TEN&quot; |
| FIFTEEN | &quot;FIFTEEN&quot; |
| TWENTY | &quot;TWENTY&quot; |
| THIRTY | &quot;THIRTY&quot; |
| FOURTY | &quot;FOURTY&quot; |
| FIFTY | &quot;FIFTY&quot; |
| ONE_HUNDRED | &quot;ONE_HUNDRED&quot; |



