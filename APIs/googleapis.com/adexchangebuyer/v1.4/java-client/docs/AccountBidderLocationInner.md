

# AccountBidderLocationInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidProtocol** | **String** | The protocol that the bidder endpoint is using. OpenRTB protocols with prefix PROTOCOL_OPENRTB_PROTOBUF use proto buffer, otherwise use JSON.  Allowed values:   - PROTOCOL_ADX  - PROTOCOL_OPENRTB_2_2  - PROTOCOL_OPENRTB_2_3  - PROTOCOL_OPENRTB_2_4  - PROTOCOL_OPENRTB_2_5  - PROTOCOL_OPENRTB_PROTOBUF_2_3  - PROTOCOL_OPENRTB_PROTOBUF_2_4  - PROTOCOL_OPENRTB_PROTOBUF_2_5 |  [optional] |
|**maximumQps** | **Integer** | The maximum queries per second the Ad Exchange will send. |  [optional] |
|**region** | **String** | The geographical region the Ad Exchange should send requests from. Only used by some quota systems, but always setting the value is recommended. Allowed values:   - ASIA  - EUROPE  - US_EAST  - US_WEST |  [optional] |
|**url** | **String** | The URL to which the Ad Exchange will send bid requests. |  [optional] |



