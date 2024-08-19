# JumpsellerApi.PartnerStoreCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aff** | **String** | Partner code. | [optional] 
**email** | **String** | New Store administrator email. | [optional] 
**locale** | **String** | ISO3166-2 code for the store langauge. | [optional] [default to &#39;en&#39;]
**password** | **String** | New Store administrator password. | [optional] 
**planName** | **String** | New Store plan name. | [optional] [default to &#39;pro&#39;]
**rejectDuplicates** | **Boolean** | Indicates whether the request should fail if the Store name provided is already in use. | [optional] [default to false]
**storeName** | **String** | New Store name. | [optional] 



## Enum: PlanNameEnum


* `pro` (value: `"pro"`)

* `plus` (value: `"plus"`)

* `premium` (value: `"premium"`)




