# RealTimeBiddingApi.Endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidProtocol** | **String** | The protocol that the bidder endpoint is using. | [optional] 
**maximumQps** | **String** | The maximum number of queries per second allowed to be sent to this server. | [optional] 
**name** | **String** | Output only. Name of the endpoint resource that must follow the pattern &#x60;bidders/{bidderAccountId}/endpoints/{endpointId}&#x60;, where {bidderAccountId} is the account ID of the bidder who operates this endpoint, and {endpointId} is a unique ID assigned by the server. | [optional] [readonly] 
**tradingLocation** | **String** | The trading location that bid requests should be sent from. See https://developers.google.com/authorized-buyers/rtb/peer-guide#trading-locations for further information. | [optional] 
**url** | **String** | Output only. The URL that bid requests should be sent to. | [optional] [readonly] 



## Enum: BidProtocolEnum


* `BID_PROTOCOL_UNSPECIFIED` (value: `"BID_PROTOCOL_UNSPECIFIED"`)

* `GOOGLE_RTB` (value: `"GOOGLE_RTB"`)

* `OPENRTB_JSON` (value: `"OPENRTB_JSON"`)

* `OPENRTB_PROTOBUF` (value: `"OPENRTB_PROTOBUF"`)





## Enum: TradingLocationEnum


* `TRADING_LOCATION_UNSPECIFIED` (value: `"TRADING_LOCATION_UNSPECIFIED"`)

* `US_WEST` (value: `"US_WEST"`)

* `US_EAST` (value: `"US_EAST"`)

* `EUROPE` (value: `"EUROPE"`)

* `ASIA` (value: `"ASIA"`)




