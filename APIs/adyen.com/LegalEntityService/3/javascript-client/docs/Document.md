# LegalEntityManagementApi.Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | [**Attachment**](Attachment.md) | Object that contains the document. | [optional] 
**attachments** | [**[Attachment]**](Attachment.md) | Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document. | [optional] 
**creationDate** | **Date** | The creation date of the document. | [optional] [readonly] 
**description** | **String** | Your description for the document. | 
**expiryDate** | **String** | The expiry date of the document, in YYYY-MM-DD format. | [optional] 
**fileName** | **String** | The filename of the document. | [optional] 
**id** | **String** | The unique identifier of the document. | [optional] [readonly] 
**issuerCountry** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. | [optional] 
**issuerState** | **String** | The state or province where the document was issued (AU only). | [optional] 
**modificationDate** | **Date** | The modification date of the document. | [optional] [readonly] 
**number** | **String** | The number in the document. | [optional] 
**owner** | [**OwnerEntity**](OwnerEntity.md) | Contains information about the resource that owns the document. | [optional] 
**type** | **String** | Type of document, used when providing an ID number or uploading a document. The possible values depend on the legal entity type.  * For **organization**, the &#x60;type&#x60; values can be **proofOfAddress**, **registrationDocument**, **vatDocument**, **proofOfOrganizationTaxInfo**, **proofOfOwnership**, **proofOfIndustry**, **proofOfSignatory**, or **proofOfFundingOrWealthSource**.  * For **individual**, the &#x60;type&#x60; values can be **identityCard**, **driversLicense**, **passport**, **liveSelfie**, **proofOfNationalIdNumber**, **proofOfResidency**, **proofOfIndustry**, **proofOfIndividualTaxId**, or **proofOfFundingOrWealthSource**.  * For **soleProprietorship**, the &#x60;type&#x60; values can be **constitutionalDocument**, **proofOfAddress**, or **proofOfIndustry**.  * Use **bankStatement** to upload documents for a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id). | 



## Enum: TypeEnum


* `bankStatement` (value: `"bankStatement"`)

* `driversLicense` (value: `"driversLicense"`)

* `identityCard` (value: `"identityCard"`)

* `nationalIdNumber` (value: `"nationalIdNumber"`)

* `passport` (value: `"passport"`)

* `proofOfAddress` (value: `"proofOfAddress"`)

* `proofOfNationalIdNumber` (value: `"proofOfNationalIdNumber"`)

* `proofOfResidency` (value: `"proofOfResidency"`)

* `registrationDocument` (value: `"registrationDocument"`)

* `vatDocument` (value: `"vatDocument"`)

* `proofOfOrganizationTaxInfo` (value: `"proofOfOrganizationTaxInfo"`)

* `proofOfIndividualTaxId` (value: `"proofOfIndividualTaxId"`)

* `proofOfOwnership` (value: `"proofOfOwnership"`)

* `proofOfSignatory` (value: `"proofOfSignatory"`)

* `liveSelfie` (value: `"liveSelfie"`)

* `proofOfIndustry` (value: `"proofOfIndustry"`)

* `constitutionalDocument` (value: `"constitutionalDocument"`)

* `proofOfFundingOrWealthSource` (value: `"proofOfFundingOrWealthSource"`)




