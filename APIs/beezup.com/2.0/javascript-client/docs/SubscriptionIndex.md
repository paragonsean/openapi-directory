# BeezUpMerchantApi.SubscriptionIndex

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerHealthStatus** | [**ConsumptionAvailabilityStatus**](ConsumptionAvailabilityStatus.md) |  | [optional] 
**consumerLastRequestSentUri** | **String** | The URL &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/URL\&quot;&gt;https://en.wikipedia.org/wiki/URL&lt;/a&gt; | [optional] 
**consumerUnvailableSinceUtcDate** | **Date** | This date indicates since when the subscription consumer is unavailable | [optional] 
**id** | **String** | The identifier of the subscription to the orders for a merchant | 
**lastErrorMessage** | [**ErrorResponseMessage**](ErrorResponseMessage.md) |  | [optional] 
**lastOrderPushedModificationUtcDate** | **Date** | This modification date correspond to the last order pushed by your subscription consumer | [optional] 
**lastRetryUtcDate** | **Date** | The last date we retry to send orders | [optional] 
**lastSuccessfulOrderPushedUtcDate** | **Date** | The date of the last pushed order successfully received by your subscription consumer | [optional] 
**maxRetryCount** | **Number** | The maximum BeezUP will retry to push orders. When we the retry count will reach maximum retry count, the subscription will be deactivated. | [optional] 
**merchantApplicationName** | **String** | The name of your application | 
**merchantApplicationVersion** | **String** | The version of your application | [default to &#39;1.0&#39;]
**merchantEmailAlert** | **String** | The email | [optional] 
**name** | **String** | The subscription name you want to use | 
**nextScheduledRetryUtcDate** | **Date** | The next scheduled  date we retry to send orders | [optional] 
**recoverBeginPeriodOrderLastModificationUtcDate** | **Date** | Recover existing orders using the begin period order last modification date. If not set then you will receive new/updated orders in real-time. | [optional] 
**recoverEndPeriodOrderLastModificationUtcDate** | **Date** | Recover existing orders using the begin and the end period order last modification date. Otherwise, you will receive new/updated orders in real-time.  | [optional] 
**retryCount** | **Number** | The retry count. When we the retry count will reach maximum retry count, the subscription will be deactivated. | [optional] 
**status** | [**SubscriptionStatus**](SubscriptionStatus.md) |  | 
**targetUrl** | **String** | The URL &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/URL\&quot;&gt;https://en.wikipedia.org/wiki/URL&lt;/a&gt; | 
**links** | [**SubscriptionLinks**](SubscriptionLinks.md) |  | [optional] 


