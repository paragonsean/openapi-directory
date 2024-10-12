# BeezUpMerchantApi.SubscriptionPushReporting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **String** | The duration of the push operation | 
**errorMessage** | [**ErrorResponseMessage**](ErrorResponseMessage.md) |  | [optional] 
**eventId** | **String** | The message identifier. It&#39;s a guid. | 
**httpStatus** | **Number** | The HTTP status received from the consumer | [optional] 
**lastOrderModificationUtcDate** | **Date** | This modification date correspond to the last order pushed by your subscription consumer | 
**maxRetryCount** | **Number** | The maximum BeezUP will retry to push orders. When we the retry count will reach maximum retry count, the subscription will be deactivated. | [optional] 
**nextScheduledRetryUtcDate** | **Date** | The next scheduled  date we retry to send orders | [optional] 
**orderCount** | **Number** | The order count sent | 
**requestUri** | **String** | The URL &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/URL\&quot;&gt;https://en.wikipedia.org/wiki/URL&lt;/a&gt; | [optional] 
**responseUri** | **String** | The URL &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/URL\&quot;&gt;https://en.wikipedia.org/wiki/URL&lt;/a&gt; | [optional] 
**retryCount** | **Number** | The retry count. When we the retry count will reach maximum retry count, the subscription will be deactivated. | [optional] 
**subscriptionId** | **String** | The identifier of the subscription to the orders for a merchant | 
**succeed** | **Boolean** | Indicates if the push operation has succeed | 


