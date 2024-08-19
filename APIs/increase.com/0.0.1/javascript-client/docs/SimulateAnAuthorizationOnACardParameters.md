# IncreaseApi.SimulateAnAuthorizationOnACardParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The authorization amount in cents. | 
**cardId** | **String** | The identifier of the Card to be authorized. | [optional] 
**digitalWalletTokenId** | **String** | The identifier of the Digital Wallet Token to be authorized. | [optional] 
**eventSubscriptionId** | **String** | The identifier of the Event Subscription to use. If provided, will override the default real time event subscription. Because you can only create one real time decision event subscription, you can use this field to route events to any specified event subscription for testing purposes. | [optional] 


