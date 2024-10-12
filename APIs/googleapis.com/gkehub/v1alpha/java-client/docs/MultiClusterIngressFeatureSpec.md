

# MultiClusterIngressFeatureSpec

**Multi-cluster Ingress**: The configuration for the MultiClusterIngress feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billing** | [**BillingEnum**](#BillingEnum) | Deprecated: This field will be ignored and should not be set. Customer&#39;s billing structure. |  [optional] |
|**configMembership** | **String** | Fully-qualified Membership name which hosts the MultiClusterIngress CRD. Example: &#x60;projects/foo-proj/locations/global/memberships/bar&#x60; |  [optional] |



## Enum: BillingEnum

| Name | Value |
|---- | -----|
| BILLING_UNSPECIFIED | &quot;BILLING_UNSPECIFIED&quot; |
| PAY_AS_YOU_GO | &quot;PAY_AS_YOU_GO&quot; |
| ANTHOS_LICENSE | &quot;ANTHOS_LICENSE&quot; |



