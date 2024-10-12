# OpenapiJsClient.CertificateCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | Required if client would like to receive stateful actions via callback during certificate lifecyle | [optional] 
**commonName** | **String** | Name to be secured in certificate. If provided, CN field in CSR will be ignored. | [optional] 
**contact** | [**CertificateContact**](CertificateContact.md) |  | 
**csr** | **String** | Certificate Signing Request | 
**intelVPro** | **Boolean** | Only used for OV | [optional] [default to false]
**organization** | [**CertificateOrganizationCreate**](CertificateOrganizationCreate.md) |  | [optional] 
**period** | **Number** | Number of years for certificate validity period | 
**productType** | **String** | Type of product requesting a certificate. Only required non-renewal | 
**rootType** | **String** | Root Type. Depending on certificate expiration date, SHA_1 not be allowed. Will default to SHA_2 if expiration date exceeds sha1 allowed date | [optional] [default to &#39;STARFIELD_SHA_2&#39;]
**slotSize** | **String** | Number of subject alternative names(SAN) to be included in certificate  | [optional] 
**subjectAlternativeNames** | **[String]** | Subject Alternative names. Collection of subjectAlternativeNames to be included in certificate. | [optional] 



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




