# GooglePlayAndroidDeveloperApi.SubscriptionPriceChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newPrice** | [**Price**](Price.md) |  | [optional] 
**state** | **Number** | The current state of the price change. Possible values are: 0. Outstanding: State for a pending price change waiting for the user to agree. In this state, you can optionally seek confirmation from the user using the In-App API. 1. Accepted: State for an accepted price change that the subscription will renew with unless it&#39;s canceled. The price change takes effect on a future date when the subscription renews. Note that the change might not occur when the subscription is renewed next. | [optional] 


