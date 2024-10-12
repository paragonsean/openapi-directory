# AmazonChimeSdkMessaging.CreateChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appInstanceArn** | **String** | The ARN of the channel request. | 
**name** | **String** | The name of the channel. | 
**mode** | **String** | The channel mode: &lt;code&gt;UNRESTRICTED&lt;/code&gt; or &lt;code&gt;RESTRICTED&lt;/code&gt;. Administrators, moderators, and channel members can add themselves and other members to unrestricted channels. Only administrators and moderators can add members to restricted channels. | [optional] 
**privacy** | **String** | The channel&#39;s privacy level: &lt;code&gt;PUBLIC&lt;/code&gt; or &lt;code&gt;PRIVATE&lt;/code&gt;. Private channels aren&#39;t discoverable by users outside the channel. Public channels are discoverable by anyone in the &lt;code&gt;AppInstance&lt;/code&gt;. | [optional] 
**metadata** | **String** | The metadata of the creation request. Limited to 1KB and UTF-8. | [optional] 
**clientRequestToken** | **String** | The client token for the request. An &lt;code&gt;Idempotency&lt;/code&gt; token. | 
**tags** | [**[Tag]**](Tag.md) | The tags for the creation request. | [optional] 
**channelId** | **String** | The ID of the channel in the request. | [optional] 
**memberArns** | **[String]** | The ARNs of the channel members in the request. | [optional] 
**moderatorArns** | **[String]** | The ARNs of the channel moderators in the request. | [optional] 
**elasticChannelConfiguration** | [**CreateChannelRequestElasticChannelConfiguration**](CreateChannelRequestElasticChannelConfiguration.md) |  | [optional] 
**expirationSettings** | [**CreateChannelRequestExpirationSettings**](CreateChannelRequestExpirationSettings.md) |  | [optional] 



## Enum: ModeEnum


* `UNRESTRICTED` (value: `"UNRESTRICTED"`)

* `RESTRICTED` (value: `"RESTRICTED"`)





## Enum: PrivacyEnum


* `PUBLIC` (value: `"PUBLIC"`)

* `PRIVATE` (value: `"PRIVATE"`)




