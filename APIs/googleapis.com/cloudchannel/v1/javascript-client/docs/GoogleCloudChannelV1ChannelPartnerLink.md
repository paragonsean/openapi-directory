# CloudChannelApi.GoogleCloudChannelV1ChannelPartnerLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelPartnerCloudIdentityInfo** | [**GoogleCloudChannelV1CloudIdentityInfo**](GoogleCloudChannelV1CloudIdentityInfo.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp of when the channel partner link is created. | [optional] [readonly] 
**inviteLinkUri** | **String** | Output only. URI of the web page where partner accepts the link invitation. | [optional] [readonly] 
**linkState** | **String** | Required. State of the channel partner link. | [optional] 
**name** | **String** | Output only. Resource name for the channel partner link, in the format accounts/{account_id}/channelPartnerLinks/{id}. | [optional] [readonly] 
**publicId** | **String** | Output only. Public identifier that a customer must use to generate a transfer token to move to this distributor-reseller combination. | [optional] [readonly] 
**resellerCloudIdentityId** | **String** | Required. Cloud Identity ID of the linked reseller. | [optional] 
**updateTime** | **String** | Output only. Timestamp of when the channel partner link is updated. | [optional] [readonly] 



## Enum: LinkStateEnum


* `CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED` (value: `"CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED"`)

* `INVITED` (value: `"INVITED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `REVOKED` (value: `"REVOKED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)




