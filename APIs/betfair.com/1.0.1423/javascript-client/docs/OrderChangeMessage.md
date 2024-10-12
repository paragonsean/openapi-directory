# BetfairExchangeStreamingApi.OrderChangeMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clk** | **String** | Token value (non-null) should be stored and passed in a MarketSubscriptionMessage to resume subscription (in case of disconnect) | [optional] 
**conflateMs** | **Number** | Conflate Milliseconds - the conflation rate (may differ from that requested if subscription is delayed) | [optional] 
**ct** | **String** | Change Type - set to indicate the type of change - if null this is a delta) | [optional] 
**heartbeatMs** | **Number** | Heartbeat Milliseconds - the heartbeat rate (may differ from requested: bounds are 500 to 30000) | [optional] 
**initialClk** | **String** | Token value (non-null) should be stored and passed in a MarketSubscriptionMessage to resume subscription (in case of disconnect) | [optional] 
**oc** | [**[OrderMarketChange]**](OrderMarketChange.md) | OrderMarketChanges - the modifications to account&#39;s orders (will be null on a heartbeat | [optional] 
**pt** | **Number** | Publish Time (in millis since epoch) that the changes were generated | [optional] 
**segmentType** | **String** | Segment Type - if the change is split into multiple segments, this denotes the beginning and end of a change, and segments in between. Will be null if data is not segmented | [optional] 
**status** | **Number** | Stream status: set to null if the exchange stream data is up to date and 503 if the downstream services are experiencing latencies | [optional] 



## Enum: CtEnum


* `SUB_IMAGE` (value: `"SUB_IMAGE"`)

* `RESUB_DELTA` (value: `"RESUB_DELTA"`)

* `HEARTBEAT` (value: `"HEARTBEAT"`)





## Enum: SegmentTypeEnum


* `SEG_START` (value: `"SEG_START"`)

* `SEG` (value: `"SEG"`)

* `SEG_END` (value: `"SEG_END"`)




