

# PauseProposalDealsRequest

Request message to pause serving for finalized deals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalDealIds** | **List&lt;String&gt;** | The external_deal_id&#39;s of the deals to be paused. If empty, all the deals in the proposal will be paused. |  [optional] |
|**reason** | **String** | The reason why the deals are being paused. This human readable message will be displayed in the seller&#39;s UI. (Max length: 1000 unicode code units.) |  [optional] |



