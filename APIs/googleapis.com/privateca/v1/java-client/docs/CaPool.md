

# CaPool

A CaPool represents a group of CertificateAuthorities that form a trust anchor. A CaPool can be used to manage issuance policies for one or more CertificateAuthority resources and to rotate CA certificates in and out of the trust anchor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issuancePolicy** | [**IssuancePolicy**](IssuancePolicy.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels with user-defined metadata. |  [optional] |
|**name** | **String** | Output only. The resource name for this CaPool in the format &#x60;projects/_*_/locations/_*_/caPools/_*&#x60;. |  [optional] [readonly] |
|**publishingOptions** | [**PublishingOptions**](PublishingOptions.md) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Required. Immutable. The Tier of this CaPool. |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| TIER_UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |
| DEVOPS | &quot;DEVOPS&quot; |



