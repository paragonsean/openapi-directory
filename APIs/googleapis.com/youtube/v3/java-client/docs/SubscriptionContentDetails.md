

# SubscriptionContentDetails

Details about the content to witch a subscription refers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityType** | [**ActivityTypeEnum**](#ActivityTypeEnum) | The type of activity this subscription is for (only uploads, everything). |  [optional] |
|**newItemCount** | **Integer** | The number of new items in the subscription since its content was last read. |  [optional] |
|**totalItemCount** | **Integer** | The approximate number of items that the subscription points to. |  [optional] |



## Enum: ActivityTypeEnum

| Name | Value |
|---- | -----|
| SUBSCRIPTION_ACTIVITY_TYPE_UNSPECIFIED | &quot;subscriptionActivityTypeUnspecified&quot; |
| ALL | &quot;all&quot; |
| UPLOADS | &quot;uploads&quot; |



