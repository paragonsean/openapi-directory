

# FinalizedDeal

A finalized deal is a snapshot of the deal when both buyer and seller accept the deal. The buyer or seller can update the deal after it's been finalized and renegotiate on the deal targeting, terms and other fields, while at the same time the finalized snapshot of the deal can still be retrieved using this API. The finalized deal contains a copy of the deal as it existed when most recently finalized, as well as fields related to deal serving such as pause/resume status, RTB metrics, and more.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deal** | [**Deal**](Deal.md) |  |  [optional] |
|**dealPausingInfo** | [**DealPausingInfo**](DealPausingInfo.md) |  |  [optional] |
|**dealServingStatus** | [**DealServingStatusEnum**](#DealServingStatusEnum) | Serving status of the deal. |  [optional] |
|**name** | **String** | The resource name of the finalized deal. Format: &#x60;buyers/{accountId}/finalizedDeals/{finalizedDealId}&#x60; |  [optional] |
|**readyToServe** | **Boolean** | Whether the Programmatic Guaranteed deal is ready for serving. |  [optional] |
|**rtbMetrics** | [**RtbMetrics**](RtbMetrics.md) |  |  [optional] |



## Enum: DealServingStatusEnum

| Name | Value |
|---- | -----|
| DEAL_SERVING_STATUS_UNSPECIFIED | &quot;DEAL_SERVING_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ENDED | &quot;ENDED&quot; |
| PAUSED_BY_BUYER | &quot;PAUSED_BY_BUYER&quot; |
| PAUSED_BY_SELLER | &quot;PAUSED_BY_SELLER&quot; |



