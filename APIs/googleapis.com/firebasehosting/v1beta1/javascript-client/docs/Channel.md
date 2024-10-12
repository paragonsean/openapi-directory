# FirebaseHostingApi.Channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time at which the channel was created. | [optional] [readonly] 
**expireTime** | **String** | The time at which the channel will be automatically deleted. If null, the channel will not be automatically deleted. This field is present in the output whether it&#39;s set directly or via the &#x60;ttl&#x60; field. | [optional] 
**labels** | **{String: String}** | Text labels used for extra metadata and/or filtering. | [optional] 
**name** | **String** | The fully-qualified resource name for the channel, in the format: sites/ SITE_ID/channels/CHANNEL_ID | [optional] 
**release** | [**Release**](Release.md) |  | [optional] 
**retainedReleaseCount** | **Number** | The number of previous releases to retain on the channel for rollback or other purposes. Must be a number between 1-100. Defaults to 10 for new channels. | [optional] 
**ttl** | **String** | Input only. A time-to-live for this channel. Sets &#x60;expire_time&#x60; to the provided duration past the time of the request. | [optional] 
**updateTime** | **String** | Output only. The time at which the channel was last updated. | [optional] [readonly] 
**url** | **String** | Output only. The URL at which the content of this channel&#39;s current release can be viewed. This URL is a Firebase-provided subdomain of &#x60;web.app&#x60;. The content of this channel&#39;s current release can also be viewed at the Firebase-provided subdomain of &#x60;firebaseapp.com&#x60;. If this channel is the &#x60;live&#x60; channel for the Hosting site, then the content of this channel&#39;s current release can also be viewed at any connected custom domains. | [optional] [readonly] 


