

# GoogleCloudChannelV1alpha1ChannelPartnerEvent

Represents Pub/Sub messages about updates to a Channel Partner. You can retrieve updated values through the ChannelPartnerLinks API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelPartner** | **String** | Resource name for the Channel Partner Link. Channel_partner uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id} |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Type of event performed on the Channel Partner. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| LINK_STATE_CHANGED | &quot;LINK_STATE_CHANGED&quot; |
| PARTNER_ADVANTAGE_INFO_CHANGED | &quot;PARTNER_ADVANTAGE_INFO_CHANGED&quot; |



