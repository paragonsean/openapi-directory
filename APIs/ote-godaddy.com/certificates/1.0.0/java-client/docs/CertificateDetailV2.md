

# CertificateDetailV2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateId** | **String** | The unique identifier of the certificate request. Only present if no errors returned |  |
|**commonName** | **String** | Common name of certificate |  |
|**completedAt** | **String** | The date the certificate request completed processing. |  [optional] |
|**contact** | [**CertificateContact**](CertificateContact.md) |  |  |
|**createdAt** | **String** | The date the certificate was ordered. |  |
|**csr** | **String** | Certificate signing request (if present) in PEM format |  [optional] |
|**deniedReason** | **String** | Only present if certificate order has been denied |  [optional] |
|**organization** | [**CertificateOrganization**](CertificateOrganization.md) |  |  [optional] |
|**period** | **Integer** | Validity period of order. Specified in years |  |
|**progress** | **Integer** | Percentage of completion for certificate vetting |  [optional] |
|**renewalAvailable** | **Boolean** | Only returned when a renewal is available. |  [optional] |
|**revokedAt** | **String** | The revocation date of certificate (if revoked). |  [optional] |
|**rootType** | [**RootTypeEnum**](#RootTypeEnum) | Root type:    * &#x60;GODADDY_SHA_1&#x60; - GoDaddy (Secure Hash Algorithm 1) SHA-1 root type   * &#x60;GODADDY_SHA_2&#x60; - GoDaddy (Secure Hash Algorithm 2) SHA-2 root type   * &#x60;STARFIELD_SHA_1&#x60; - Starfield SHA-1 root type   * &#x60;STARFIELD_SHA_2&#x60; - Starfield SHA-2 root type  |  [optional] |
|**serialNumber** | **String** | Serial number of certificate (if issued or revoked) |  [optional] |
|**serialNumberHex** | **String** | Hexadecmial format for Serial number of certificate(if issued or revoked) |  [optional] |
|**slotSize** | [**SlotSizeEnum**](#SlotSizeEnum) | Number of subject alternative names (SAN) to be included in certificate (if UCC):    * &#x60;FIVE&#x60; - Five slot UCC request   * &#x60;TEN&#x60; - Ten slot UCC request   * &#x60;FIFTEEN&#x60; - Fifteen slot UCC request   * &#x60;TWENTY&#x60; - Twenty slot UCC request   * &#x60;THIRTY&#x60; - Thirty slot UCC request   * &#x60;FOURTY&#x60; - Fourty slot UCC request   * &#x60;FIFTY&#x60; - Fifty slot UCC request   * &#x60;ONE_HUNDRED&#x60; - One hundred slot UCC request  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Certificate status (if issued or revoked):    * &#x60;CANCELED&#x60; - Certificate request was canceled by customer   * &#x60;DENIED&#x60; - Certificate request was denied by customer\\n  * &#x60;EXPIRED&#x60; - Issued certificate has exceeded the valid end date   * &#x60;ISSUED&#x60; - Certificate has been issued and is within validity period   * &#x60;PENDING_ISSUANCE&#x60; - Certificate request has completed domain verification and is in the process of being issued   * &#x60;PENDING_REKEY&#x60; - Previously issued certificate was rekeyed by customer and is in the process of being reissued   * &#x60;PENDING_REVOCATION&#x60; - Previously issued certificate is in the process of being revoked   * &#x60;REVOKED&#x60; - Issued certificate has been revoked\\n  * &#x60;UNUSED&#x60; - Certificate in an error state  |  |
|**subjectAlternativeNames** | **Set&lt;String&gt;** | Subject Alternative names. Collection of subjectAlternativeNames to be included in certificate. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Certificate type:    * &#x60;DV_SSL&#x60; - (Domain Validated Secure Sockets Layer) SSL certificate validated using domain name only   * &#x60;DV_WILDCARD_SSL&#x60; - SSL certificate containing subdomains which is validated using domain name only   * &#x60;EV_SSL&#x60; - (Extended Validation) SSL certificate validated using organization information, domain name, business legal status, and other factors   * &#x60;OV_CODE_SIGNING&#x60; - Code signing SSL certificate used by software developers to digitally sign apps. Validated using organization information   * &#x60;OV_DRIVER_SIGNING&#x60; - Driver signing SSL certificate request used by software developers to digitally sign secure code for Windows hardware drivers. Validated using organization information   * &#x60;OV_SSL&#x60; - SSL certificate validated using organization information and domain name   * &#x60;OV_WILDCARD_SSL&#x60; - SSL certificate containing subdomains which is validated using organization information and domain name   * &#x60;UCC_DV_SSL&#x60; - (Unified Communication Certificate) Multi domain SSL certificate validated using domain name only   * &#x60;UCC_EV_SSL&#x60; - Multi domain SSL certificate validated using organization information, domain name, business legal status, and other factors   * &#x60;UCC_OV_SSL&#x60; - Multi domain SSL certificate validated using organization information and domain name  |  |
|**validEndAt** | **String** | The end date of the certificate&#39;s validity (if issued or revoked). |  [optional] |
|**validStartAt** | **String** | The start date of the certificate&#39;s validity (if issued or revoked). |  [optional] |



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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DV_SSL | &quot;DV_SSL&quot; |
| DV_WILDCARD_SSL | &quot;DV_WILDCARD_SSL&quot; |
| EV_SSL | &quot;EV_SSL&quot; |
| OV_CODE_SIGNING | &quot;OV_CODE_SIGNING&quot; |
| OV_DRIVER_SIGNING | &quot;OV_DRIVER_SIGNING&quot; |
| OV_SSL | &quot;OV_SSL&quot; |
| OV_WILDCARD_SSL | &quot;OV_WILDCARD_SSL&quot; |
| UCC_DV_SSL | &quot;UCC_DV_SSL&quot; |
| UCC_EV_SSL | &quot;UCC_EV_SSL&quot; |
| UCC_OV_SSL | &quot;UCC_OV_SSL&quot; |



