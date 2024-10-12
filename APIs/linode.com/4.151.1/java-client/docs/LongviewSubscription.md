

# LongviewSubscription

A Longview Subscription represents a tier of Longview service you can subscribe to. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientsIncluded** | **Integer** | The number of Longview Clients that may be created with this Subscription tier.  |  [optional] [readonly] |
|**id** | [**IdEnum**](#IdEnum) | The unique ID of this Subscription tier.  |  [optional] [readonly] |
|**label** | **String** | A display name for this Subscription tier.  |  [optional] [readonly] |
|**price** | [**LongviewSubscriptionPrice**](LongviewSubscriptionPrice.md) |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| _3 | &quot;longview-3&quot; |
| _10 | &quot;longview-10&quot; |
| _40 | &quot;longview-40&quot; |
| _100 | &quot;longview-100&quot; |



