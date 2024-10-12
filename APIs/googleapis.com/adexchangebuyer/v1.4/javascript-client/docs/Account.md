# AdExchangeBuyerApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyPretargetingToNonGuaranteedDeals** | **Boolean** | When this is false, bid requests that include a deal ID for a private auction or preferred deal are always sent to your bidder. When true, all active pretargeting configs will be applied to private auctions and preferred deals. Programmatic Guaranteed deals (when enabled) are always sent to your bidder. | [optional] 
**bidderLocation** | [**[AccountBidderLocationInner]**](AccountBidderLocationInner.md) | Your bidder locations that have distinct URLs. | [optional] 
**cookieMatchingNid** | **String** | The nid parameter value used in cookie match requests. Please contact your technical account manager if you need to change this. | [optional] 
**cookieMatchingUrl** | **String** | The base URL used in cookie match requests. | [optional] 
**id** | **Number** | Account id. | [optional] 
**kind** | **String** | Resource type. | [optional] [default to &#39;adexchangebuyer#account&#39;]
**maximumActiveCreatives** | **Number** | The maximum number of active creatives that an account can have, where a creative is active if it was inserted or bid with in the last 30 days. Please contact your technical account manager if you need to change this. | [optional] 
**maximumTotalQps** | **Number** | The sum of all bidderLocation.maximumQps values cannot exceed this. Please contact your technical account manager if you need to change this. | [optional] 
**numberActiveCreatives** | **Number** | The number of creatives that this account inserted or bid with in the last 30 days. | [optional] 


