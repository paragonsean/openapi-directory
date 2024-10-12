

# OrderSubscriptionMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clk** | **String** | Token value delta (received in MarketChangeMessage) that should be passed to resume a subscription |  [optional] |
|**conflateMs** | **Long** | Conflate Milliseconds - the conflation rate (looped back on initial image after validation: bounds are 0 to 120000) |  [optional] |
|**heartbeatMs** | **Long** | Heartbeat Milliseconds - the heartbeat rate (looped back on initial image after validation: bounds are 500 to 5000) |  [optional] |
|**initialClk** | **String** | Token value (received in initial MarketChangeMessage) that should be passed to resume a subscription |  [optional] |
|**orderFilter** | [**OrderFilter**](OrderFilter.md) |  |  [optional] |
|**segmentationEnabled** | **Boolean** | Segmentation Enabled - allow the server to send large sets of data in segments, instead of a single block |  [optional] |



