

# FeatureSpec

**Workload Certificate**: The Hub-wide input for the WorkloadCertificate feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultConfig** | [**MembershipSpec**](MembershipSpec.md) |  |  [optional] |
|**provisionGoogleCa** | [**ProvisionGoogleCaEnum**](#ProvisionGoogleCaEnum) | Immutable. Specifies CA configuration. |  [optional] |



## Enum: ProvisionGoogleCaEnum

| Name | Value |
|---- | -----|
| GOOGLE_CA_PROVISIONING_UNSPECIFIED | &quot;GOOGLE_CA_PROVISIONING_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| ENABLED_WITH_MANAGED_CA | &quot;ENABLED_WITH_MANAGED_CA&quot; |
| ENABLED_WITH_DEFAULT_CA | &quot;ENABLED_WITH_DEFAULT_CA&quot; |



