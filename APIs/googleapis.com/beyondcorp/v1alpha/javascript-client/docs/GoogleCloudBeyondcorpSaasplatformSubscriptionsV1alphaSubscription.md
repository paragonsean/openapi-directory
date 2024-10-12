# BeyondCorpApi.GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoRenewEnabled** | **Boolean** | Output only. Represents that, if subscription will renew or end when the term ends. | [optional] [readonly] 
**createTime** | **String** | Output only. Create time of the subscription. | [optional] [readonly] 
**endTime** | **String** | Output only. End time of the subscription. | [optional] [readonly] 
**name** | **String** | Required. Unique resource name of the Subscription. The name is ignored when creating a subscription. | [optional] 
**seatCount** | **String** | Optional. Number of seats in the subscription. | [optional] 
**sku** | **String** | Required. SKU of subscription. | [optional] 
**startTime** | **String** | Output only. Start time of the subscription. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the subscription. | [optional] [readonly] 
**type** | **String** | Required. Type of subscription. | [optional] 



## Enum: SkuEnum


* `SKU_UNSPECIFIED` (value: `"SKU_UNSPECIFIED"`)

* `BCE_STANDARD_SKU` (value: `"BCE_STANDARD_SKU"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `COMPLETED` (value: `"COMPLETED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `TRIAL` (value: `"TRIAL"`)

* `PAID` (value: `"PAID"`)

* `ALLOWLIST` (value: `"ALLOWLIST"`)




