

# GoogleCloudChannelV1alpha1CustomerEvent

Represents Pub/Sub message content describing customer update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | **String** | Resource name of the customer. Format: accounts/{account_id}/customers/{customer_id} |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Type of event which happened on the customer. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PRIMARY_DOMAIN_CHANGED | &quot;PRIMARY_DOMAIN_CHANGED&quot; |
| PRIMARY_DOMAIN_VERIFIED | &quot;PRIMARY_DOMAIN_VERIFIED&quot; |



