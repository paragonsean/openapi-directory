

# LegalEntityInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**Map&lt;String, LegalEntityCapability&gt;**](LegalEntityCapability.md) | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |  [optional] [readonly] |
|**entityAssociations** | [**List&lt;LegalEntityAssociation&gt;**](LegalEntityAssociation.md) | List of legal entities associated with the current legal entity. For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. |  [optional] |
|**individual** | [**Individual**](Individual.md) | Information about the individual. Required if &#x60;type&#x60; is **individual**. |  [optional] |
|**organization** | [**Organization**](Organization.md) | Information about the organization. Required if &#x60;type&#x60; is **organization**. |  [optional] |
|**reference** | **String** | Your reference for the legal entity, maximum 150 characters. |  [optional] |
|**soleProprietorship** | [**SoleProprietorship**](SoleProprietorship.md) | Information about the sole proprietorship. Required if &#x60;type&#x60; is **soleProprietorship**. |  [optional] |
|**trust** | [**Trust**](Trust.md) | Information about the trust. Required if &#x60;type&#x60; is **trust**. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of legal entity.  Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**. |  [optional] |
|**unincorporatedPartnership** | [**UnincorporatedPartnership**](UnincorporatedPartnership.md) | Information about the unincorporated partnership. Required if &#x60;type&#x60; is **unincorporatedPartnership**. |  [optional] |
|**verificationPlan** | **String** | A key-value pair that specifies the [verification process](https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/) for a legal entity. Set to **upfront** for [upfront verification](https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details#upfront). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;individual&quot; |
| ORGANIZATION | &quot;organization&quot; |
| SOLE_PROPRIETORSHIP | &quot;soleProprietorship&quot; |
| TRUST | &quot;trust&quot; |
| UNINCORPORATED_PARTNERSHIP | &quot;unincorporatedPartnership&quot; |



