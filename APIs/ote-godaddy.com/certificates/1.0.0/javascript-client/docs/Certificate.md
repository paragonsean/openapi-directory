# OpenapiJsClient.Certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateId** | **String** | The unique identifier of the certificate request. Only present if no errors returned | 
**commonName** | **String** | Common name of certificate | [optional] 
**contact** | [**CertificateContact**](CertificateContact.md) |  | 
**createdAt** | **String** | The date the certificate was ordered. | 
**deniedReason** | **String** | Only present if certificate order has been denied | [optional] 
**organization** | [**CertificateOrganization**](CertificateOrganization.md) |  | [optional] 
**period** | **Number** | Validity period of order. Specified in years | 
**productType** | **String** | Certificate product type | 
**progress** | **Number** | Percentage of completion for certificate vetting | [optional] 
**revokedAt** | **String** | The revocation date of certificate (if revoked). | [optional] 
**rootType** | **String** | Root Type | [optional] 
**serialNumber** | **String** | Serial number of certificate (if issued or revoked) | [optional] 
**serialNumberHex** | **String** | Hexadecmial format for Serial number of certificate(if issued or revoked) | [optional] 
**slotSize** | **String** | Number of subject alternative names(SAN) to be included in certificate  | [optional] 
**status** | **String** | Status of certificate | 
**subjectAlternativeNames** | [**[SubjectAlternativeNameDetails]**](SubjectAlternativeNameDetails.md) | Contains subject alternative names set | [optional] 
**validEnd** | **String** | The end date of the certificate&#39;s validity (if issued or revoked). | [optional] 
**validStart** | **String** | The start date of the certificate&#39;s validity (if issued or revoked). | [optional] 



## Enum: ProductTypeEnum


* `DV_SSL` (value: `"DV_SSL"`)

* `DV_WILDCARD_SSL` (value: `"DV_WILDCARD_SSL"`)

* `EV_SSL` (value: `"EV_SSL"`)

* `OV_CS` (value: `"OV_CS"`)

* `OV_DS` (value: `"OV_DS"`)

* `OV_SSL` (value: `"OV_SSL"`)

* `OV_WILDCARD_SSL` (value: `"OV_WILDCARD_SSL"`)

* `UCC_DV_SSL` (value: `"UCC_DV_SSL"`)

* `UCC_EV_SSL` (value: `"UCC_EV_SSL"`)

* `UCC_OV_SSL` (value: `"UCC_OV_SSL"`)





## Enum: RootTypeEnum


* `GODADDY_SHA_1` (value: `"GODADDY_SHA_1"`)

* `GODADDY_SHA_2` (value: `"GODADDY_SHA_2"`)

* `STARFIELD_SHA_1` (value: `"STARFIELD_SHA_1"`)

* `STARFIELD_SHA_2` (value: `"STARFIELD_SHA_2"`)





## Enum: SlotSizeEnum


* `FIVE` (value: `"FIVE"`)

* `TEN` (value: `"TEN"`)

* `FIFTEEN` (value: `"FIFTEEN"`)

* `TWENTY` (value: `"TWENTY"`)

* `THIRTY` (value: `"THIRTY"`)

* `FOURTY` (value: `"FOURTY"`)

* `FIFTY` (value: `"FIFTY"`)

* `ONE_HUNDRED` (value: `"ONE_HUNDRED"`)





## Enum: StatusEnum


* `PENDING_ISSUANCE` (value: `"PENDING_ISSUANCE"`)

* `ISSUED` (value: `"ISSUED"`)

* `REVOKED` (value: `"REVOKED"`)

* `CANCELED` (value: `"CANCELED"`)

* `DENIED` (value: `"DENIED"`)

* `PENDING_REVOCATION` (value: `"PENDING_REVOCATION"`)

* `PENDING_REKEY` (value: `"PENDING_REKEY"`)

* `UNUSED` (value: `"UNUSED"`)

* `EXPIRED` (value: `"EXPIRED"`)




