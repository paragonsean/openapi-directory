

# Document


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachment** | [**Attachment**](Attachment.md) | Object that contains the document. |  [optional] |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document. |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of the document. |  [optional] [readonly] |
|**description** | **String** | Your description for the document. |  |
|**expiryDate** | **String** | The expiry date of the document, in YYYY-MM-DD format. |  [optional] |
|**fileName** | **String** | The filename of the document. |  [optional] |
|**id** | **String** | The unique identifier of the document. |  [optional] [readonly] |
|**issuerCountry** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |  [optional] |
|**issuerState** | **String** | The state or province where the document was issued (AU only). |  [optional] |
|**modificationDate** | **OffsetDateTime** | The modification date of the document. |  [optional] [readonly] |
|**number** | **String** | The number in the document. |  [optional] |
|**owner** | [**OwnerEntity**](OwnerEntity.md) | Contains information about the resource that owns the document. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of document, used when providing an ID number or uploading a document. The possible values depend on the legal entity type.  * For **organization**, the &#x60;type&#x60; values can be **proofOfAddress**, **registrationDocument**, **vatDocument**, **proofOfOrganizationTaxInfo**, **proofOfOwnership**, **proofOfIndustry**, **proofOfSignatory**, or **proofOfFundingOrWealthSource**.  * For **individual**, the &#x60;type&#x60; values can be **identityCard**, **driversLicense**, **passport**, **liveSelfie**, **proofOfResidency**, **proofOfIndustry**, **proofOfNationalIdNumber**, **proofOfIndividualTaxId**, or **proofOfFundingOrWealthSource**.  * For **soleProprietorship**, the &#x60;type&#x60; values can be **constitutionalDocument**, **proofOfAddress**, or **proofOfIndustry**.  * Use **bankStatement** to upload documents for a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id). |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_STATEMENT | &quot;bankStatement&quot; |
| DRIVERS_LICENSE | &quot;driversLicense&quot; |
| IDENTITY_CARD | &quot;identityCard&quot; |
| NATIONAL_ID_NUMBER | &quot;nationalIdNumber&quot; |
| PASSPORT | &quot;passport&quot; |
| PROOF_OF_ADDRESS | &quot;proofOfAddress&quot; |
| PROOF_OF_NATIONAL_ID_NUMBER | &quot;proofOfNationalIdNumber&quot; |
| PROOF_OF_RESIDENCY | &quot;proofOfResidency&quot; |
| REGISTRATION_DOCUMENT | &quot;registrationDocument&quot; |
| VAT_DOCUMENT | &quot;vatDocument&quot; |
| PROOF_OF_ORGANIZATION_TAX_INFO | &quot;proofOfOrganizationTaxInfo&quot; |
| PROOF_OF_INDIVIDUAL_TAX_ID | &quot;proofOfIndividualTaxId&quot; |
| PROOF_OF_OWNERSHIP | &quot;proofOfOwnership&quot; |
| PROOF_OF_SIGNATORY | &quot;proofOfSignatory&quot; |
| LIVE_SELFIE | &quot;liveSelfie&quot; |
| PROOF_OF_INDUSTRY | &quot;proofOfIndustry&quot; |
| CONSTITUTIONAL_DOCUMENT | &quot;constitutionalDocument&quot; |
| PROOF_OF_FUNDING_OR_WEALTH_SOURCE | &quot;proofOfFundingOrWealthSource&quot; |



