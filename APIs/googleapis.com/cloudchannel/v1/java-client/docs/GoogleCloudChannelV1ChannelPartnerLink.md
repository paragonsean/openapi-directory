

# GoogleCloudChannelV1ChannelPartnerLink

Entity representing a link between distributors and their indirect resellers in an n-tier resale channel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelPartnerCloudIdentityInfo** | [**GoogleCloudChannelV1CloudIdentityInfo**](GoogleCloudChannelV1CloudIdentityInfo.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp of when the channel partner link is created. |  [optional] [readonly] |
|**inviteLinkUri** | **String** | Output only. URI of the web page where partner accepts the link invitation. |  [optional] [readonly] |
|**linkState** | [**LinkStateEnum**](#LinkStateEnum) | Required. State of the channel partner link. |  [optional] |
|**name** | **String** | Output only. Resource name for the channel partner link, in the format accounts/{account_id}/channelPartnerLinks/{id}. |  [optional] [readonly] |
|**publicId** | **String** | Output only. Public identifier that a customer must use to generate a transfer token to move to this distributor-reseller combination. |  [optional] [readonly] |
|**resellerCloudIdentityId** | **String** | Required. Cloud Identity ID of the linked reseller. |  [optional] |
|**updateTime** | **String** | Output only. Timestamp of when the channel partner link is updated. |  [optional] [readonly] |



## Enum: LinkStateEnum

| Name | Value |
|---- | -----|
| CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED | &quot;CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED&quot; |
| INVITED | &quot;INVITED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| REVOKED | &quot;REVOKED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |



