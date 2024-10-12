# LegalEntityManagementApi.LegalEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**{String: LegalEntityCapability}**](LegalEntityCapability.md) | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. | [optional] [readonly] 
**documents** | [**[EntityReference]**](EntityReference.md) | List of documents uploaded for the legal entity. | [optional] 
**entityAssociations** | [**[LegalEntityAssociation]**](LegalEntityAssociation.md) | List of legal entities associated with the current legal entity. For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. | [optional] 
**id** | **String** | The unique identifier of the legal entity. | [readonly] 
**individual** | [**Individual**](Individual.md) | Information about the individual. Required if &#x60;type&#x60; is **individual**. | [optional] 
**organization** | [**Organization**](Organization.md) | Information about the organization. Required if &#x60;type&#x60; is **organization**. | [optional] 
**reference** | **String** | Your reference for the legal entity, maximum 150 characters. | [optional] 
**transferInstruments** | [**[TransferInstrumentReference]**](TransferInstrumentReference.md) | List of transfer instruments that the legal entity owns. | [optional] 
**trust** | [**Trust**](Trust.md) | Information about the trust. Required if &#x60;type&#x60; is **trust**. | [optional] 
**type** | **String** | The type of legal entity.   Possible values: **individual** or **organization** | [optional] 
**unincorporatedPartnership** | [**UnincorporatedPartnership**](UnincorporatedPartnership.md) | Information about the unincorporated partnership. Required if &#x60;type&#x60; is **unincorporatedPartnership**. | [optional] 
**verificationPlan** | **String** | A key-value pair that specifies the [verification process](https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/) for a legal entity. Set to **upfront** for [upfront verification](https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details#upfront). | [optional] 



## Enum: TypeEnum


* `individual` (value: `"individual"`)

* `organization` (value: `"organization"`)




