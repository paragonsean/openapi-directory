

# PartnerStoreCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aff** | **String** | Partner code. |  [optional] |
|**email** | **String** | New Store administrator email. |  [optional] |
|**locale** | **String** | ISO3166-2 code for the store langauge. |  [optional] |
|**password** | **String** | New Store administrator password. |  [optional] |
|**planName** | [**PlanNameEnum**](#PlanNameEnum) | New Store plan name. |  [optional] |
|**rejectDuplicates** | **Boolean** | Indicates whether the request should fail if the Store name provided is already in use. |  [optional] |
|**storeName** | **String** | New Store name. |  [optional] |



## Enum: PlanNameEnum

| Name | Value |
|---- | -----|
| PRO | &quot;pro&quot; |
| PLUS | &quot;plus&quot; |
| PREMIUM | &quot;premium&quot; |



