

# Endpoint

Bidder endpoint that receives bid requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidProtocol** | [**BidProtocolEnum**](#BidProtocolEnum) | The protocol that the bidder endpoint is using. |  [optional] |
|**maximumQps** | **String** | The maximum number of queries per second allowed to be sent to this server. |  [optional] |
|**name** | **String** | Output only. Name of the endpoint resource that must follow the pattern &#x60;bidders/{bidderAccountId}/endpoints/{endpointId}&#x60;, where {bidderAccountId} is the account ID of the bidder who operates this endpoint, and {endpointId} is a unique ID assigned by the server. |  [optional] [readonly] |
|**tradingLocation** | [**TradingLocationEnum**](#TradingLocationEnum) | The trading location that bid requests should be sent from. See https://developers.google.com/authorized-buyers/rtb/peer-guide#trading-locations for further information. |  [optional] |
|**url** | **String** | Output only. The URL that bid requests should be sent to. |  [optional] [readonly] |



## Enum: BidProtocolEnum

| Name | Value |
|---- | -----|
| BID_PROTOCOL_UNSPECIFIED | &quot;BID_PROTOCOL_UNSPECIFIED&quot; |
| GOOGLE_RTB | &quot;GOOGLE_RTB&quot; |
| OPENRTB_JSON | &quot;OPENRTB_JSON&quot; |
| OPENRTB_PROTOBUF | &quot;OPENRTB_PROTOBUF&quot; |



## Enum: TradingLocationEnum

| Name | Value |
|---- | -----|
| TRADING_LOCATION_UNSPECIFIED | &quot;TRADING_LOCATION_UNSPECIFIED&quot; |
| US_WEST | &quot;US_WEST&quot; |
| US_EAST | &quot;US_EAST&quot; |
| EUROPE | &quot;EUROPE&quot; |
| ASIA | &quot;ASIA&quot; |



