

# Certificate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateId** | **String** | The unique identifier of the certificate request. Only present if no errors returned |  |
|**commonName** | **String** | Common name of certificate |  [optional] |
|**contact** | [**CertificateContact**](CertificateContact.md) |  |  |
|**createdAt** | **String** | The date the certificate was ordered. |  |
|**deniedReason** | **String** | Only present if certificate order has been denied |  [optional] |
|**organization** | [**CertificateOrganization**](CertificateOrganization.md) |  |  [optional] |
|**period** | **Integer** | Validity period of order. Specified in years |  |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) | Certificate product type |  |
|**progress** | **Integer** | Percentage of completion for certificate vetting |  [optional] |
|**revokedAt** | **String** | The revocation date of certificate (if revoked). |  [optional] |
|**rootType** | [**RootTypeEnum**](#RootTypeEnum) | Root Type |  [optional] |
|**serialNumber** | **String** | Serial number of certificate (if issued or revoked) |  [optional] |
|**serialNumberHex** | **String** | Hexadecmial format for Serial number of certificate(if issued or revoked) |  [optional] |
|**slotSize** | [**SlotSizeEnum**](#SlotSizeEnum) | Number of subject alternative names(SAN) to be included in certificate  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of certificate |  |
|**subjectAlternativeNames** | [**List&lt;SubjectAlternativeNameDetails&gt;**](SubjectAlternativeNameDetails.md) | Contains subject alternative names set |  [optional] |
|**validEnd** | **String** | The end date of the certificate&#39;s validity (if issued or revoked). |  [optional] |
|**validStart** | **String** | The start date of the certificate&#39;s validity (if issued or revoked). |  [optional] |



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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_ISSUANCE | &quot;PENDING_ISSUANCE&quot; |
| ISSUED | &quot;ISSUED&quot; |
| REVOKED | &quot;REVOKED&quot; |
| CANCELED | &quot;CANCELED&quot; |
| DENIED | &quot;DENIED&quot; |
| PENDING_REVOCATION | &quot;PENDING_REVOCATION&quot; |
| PENDING_REKEY | &quot;PENDING_REKEY&quot; |
| UNUSED | &quot;UNUSED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |



