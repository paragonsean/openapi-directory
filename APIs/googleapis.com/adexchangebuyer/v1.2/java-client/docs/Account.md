

# Account

Configuration data for an Ad Exchange buyer account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidderLocation** | [**List&lt;AccountBidderLocationInner&gt;**](AccountBidderLocationInner.md) | Your bidder locations that have distinct URLs. |  [optional] |
|**cookieMatchingNid** | **String** | The nid parameter value used in cookie match requests. Please contact your technical account manager if you need to change this. |  [optional] |
|**cookieMatchingUrl** | **String** | The base URL used in cookie match requests. |  [optional] |
|**id** | **Integer** | Account id. |  [optional] |
|**kind** | **String** | Resource type. |  [optional] |
|**maximumActiveCreatives** | **Integer** | The maximum number of active creatives that an account can have, where a creative is active if it was inserted or bid with in the last 30 days. Please contact your technical account manager if you need to change this. |  [optional] |
|**maximumTotalQps** | **Integer** | The sum of all bidderLocation.maximumQps values cannot exceed this. Please contact your technical account manager if you need to change this. |  [optional] |
|**numberActiveCreatives** | **Integer** | The number of creatives that this account inserted or bid with in the last 30 days. |  [optional] |



