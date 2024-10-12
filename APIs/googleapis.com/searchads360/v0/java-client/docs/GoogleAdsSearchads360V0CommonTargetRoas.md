

# GoogleAdsSearchads360V0CommonTargetRoas

An automated bidding strategy that helps you maximize revenue while averaging a specific target return on ad spend (ROAS).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpcBidCeilingMicros** | **String** | Maximum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. This should only be set for portfolio bid strategies. |  [optional] |
|**cpcBidFloorMicros** | **String** | Minimum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. This should only be set for portfolio bid strategies. |  [optional] |
|**targetRoas** | **Double** | Required. The chosen revenue (based on conversion data) per unit of spend. Value must be between 0.01 and 1000.0, inclusive. |  [optional] |



