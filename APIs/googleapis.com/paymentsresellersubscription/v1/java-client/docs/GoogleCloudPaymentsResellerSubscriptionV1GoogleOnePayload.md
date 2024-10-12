

# GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayload

Payload specific to Google One products.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaigns** | **List&lt;String&gt;** | Campaign attributed to sales of this subscription. |  [optional] |
|**offering** | [**OfferingEnum**](#OfferingEnum) | The type of offering the subscription was sold by the partner. e.g. VAS. |  [optional] |
|**salesChannel** | [**SalesChannelEnum**](#SalesChannelEnum) | The type of sales channel through which the subscription was sold. |  [optional] |
|**storeId** | **String** | The identifier for the partner store where the subscription was sold. |  [optional] |



## Enum: OfferingEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OFFERING_UNSPECIFIED&quot; |
| VAS_BUNDLE | &quot;OFFERING_VAS_BUNDLE&quot; |
| VAS_STANDALONE | &quot;OFFERING_VAS_STANDALONE&quot; |
| HARD_BUNDLE | &quot;OFFERING_HARD_BUNDLE&quot; |
| SOFT_BUNDLE | &quot;OFFERING_SOFT_BUNDLE&quot; |



## Enum: SalesChannelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CHANNEL_UNSPECIFIED&quot; |
| RETAIL | &quot;CHANNEL_RETAIL&quot; |
| ONLINE_WEB | &quot;CHANNEL_ONLINE_WEB&quot; |
| ONLINE_ANDROID_APP | &quot;CHANNEL_ONLINE_ANDROID_APP&quot; |
| ONLINE_IOS_APP | &quot;CHANNEL_ONLINE_IOS_APP&quot; |



