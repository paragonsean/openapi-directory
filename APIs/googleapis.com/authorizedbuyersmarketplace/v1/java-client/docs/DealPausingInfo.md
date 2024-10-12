

# DealPausingInfo

Information related to deal pausing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pauseReason** | **String** | The reason for the pausing of the deal; empty for active deals. |  [optional] |
|**pauseRole** | [**PauseRoleEnum**](#PauseRoleEnum) | The party that first paused the deal; unspecified for active deals. |  [optional] |
|**pausingConsented** | **Boolean** | Whether pausing is consented between buyer and seller for the deal. |  [optional] |



## Enum: PauseRoleEnum

| Name | Value |
|---- | -----|
| BUYER_SELLER_ROLE_UNSPECIFIED | &quot;BUYER_SELLER_ROLE_UNSPECIFIED&quot; |
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



