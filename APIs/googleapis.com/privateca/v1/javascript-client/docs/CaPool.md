# CertificateAuthorityApi.CaPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuancePolicy** | [**IssuancePolicy**](IssuancePolicy.md) |  | [optional] 
**labels** | **{String: String}** | Optional. Labels with user-defined metadata. | [optional] 
**name** | **String** | Output only. The resource name for this CaPool in the format &#x60;projects/_*_/locations/_*_/caPools/_*&#x60;. | [optional] [readonly] 
**publishingOptions** | [**PublishingOptions**](PublishingOptions.md) |  | [optional] 
**tier** | **String** | Required. Immutable. The Tier of this CaPool. | [optional] 



## Enum: TierEnum


* `TIER_UNSPECIFIED` (value: `"TIER_UNSPECIFIED"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `DEVOPS` (value: `"DEVOPS"`)




