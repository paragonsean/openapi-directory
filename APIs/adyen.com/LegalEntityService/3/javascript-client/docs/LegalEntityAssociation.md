# LegalEntityManagementApi.LegalEntityAssociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associatorId** | **String** | The unique identifier of another legal entity with which the &#x60;legalEntityId&#x60; is associated. When the &#x60;legalEntityId&#x60; is associated to legal entities other than the current one, the response returns all the associations. | [optional] [readonly] 
**entityType** | **String** | The legal entity type of associated legal entity.  For example, **organization**, **soleProprietorship** or **individual**. | [optional] [readonly] 
**jobTitle** | **String** | The individual&#39;s job title if the &#x60;type&#x60; is **uboThroughControl** or **signatory**. | [optional] 
**legalEntityId** | **String** | The unique identifier of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id). | 
**name** | **String** | The name of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id).  - For **individual**, &#x60;name.firstName&#x60; and &#x60;name.lastName&#x60;. - For **organization**, &#x60;legalName&#x60;. - For **soleProprietorship**, &#x60;name&#x60;. | [optional] [readonly] 
**settlorExemptionReason** | **[String]** | Defines the Kyc Exemption Reason for a Settlor associated with a trust.  For example, **professionalServiceProvider**, **deceased**, or **contributionBelowThreshold**. | [optional] 
**type** | **String** | Defines the relationship of the legal entity to the current legal entity.  Possible values for organizations: **uboThroughOwnership**, **uboThroughControl**, **director**, **signatory**, or **ultimateParentCompany**.  Possible values for sole proprietorships: **soleProprietorship**.  Possible value for trusts: **trust**  Possible values for trust members: **definedBeneficiary**, **protector**, **secondaryTrustee**, **settlor**, **uboThroughControl**, or **uboThroughOwnership**. | 



## Enum: TypeEnum


* `definedBeneficiary` (value: `"definedBeneficiary"`)

* `director` (value: `"director"`)

* `pciSignatory` (value: `"pciSignatory"`)

* `protector` (value: `"protector"`)

* `secondaryTrustee` (value: `"secondaryTrustee"`)

* `settlor` (value: `"settlor"`)

* `signatory` (value: `"signatory"`)

* `soleProprietorship` (value: `"soleProprietorship"`)

* `trust` (value: `"trust"`)

* `trustOwnership` (value: `"trustOwnership"`)

* `uboThroughControl` (value: `"uboThroughControl"`)

* `uboThroughOwnership` (value: `"uboThroughOwnership"`)

* `ultimateParentCompany` (value: `"ultimateParentCompany"`)

* `undefinedBeneficiary` (value: `"undefinedBeneficiary"`)




