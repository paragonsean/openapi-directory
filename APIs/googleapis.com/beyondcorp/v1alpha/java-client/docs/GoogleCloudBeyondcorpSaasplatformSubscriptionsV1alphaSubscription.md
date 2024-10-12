

# GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription

A BeyondCorp Subscription resource represents BeyondCorp Enterprise Subscription. BeyondCorp Enterprise Subscription enables BeyondCorp Enterprise permium features for an organization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoRenewEnabled** | **Boolean** | Output only. Represents that, if subscription will renew or end when the term ends. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Create time of the subscription. |  [optional] [readonly] |
|**endTime** | **String** | Output only. End time of the subscription. |  [optional] [readonly] |
|**name** | **String** | Required. Unique resource name of the Subscription. The name is ignored when creating a subscription. |  [optional] |
|**seatCount** | **String** | Optional. Number of seats in the subscription. |  [optional] |
|**sku** | [**SkuEnum**](#SkuEnum) | Required. SKU of subscription. |  [optional] |
|**startTime** | **String** | Output only. Start time of the subscription. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the subscription. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Type of subscription. |  [optional] |



## Enum: SkuEnum

| Name | Value |
|---- | -----|
| SKU_UNSPECIFIED | &quot;SKU_UNSPECIFIED&quot; |
| BCE_STANDARD_SKU | &quot;BCE_STANDARD_SKU&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| TRIAL | &quot;TRIAL&quot; |
| PAID | &quot;PAID&quot; |
| ALLOWLIST | &quot;ALLOWLIST&quot; |



