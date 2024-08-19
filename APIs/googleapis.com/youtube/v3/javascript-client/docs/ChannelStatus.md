# YouTubeDataApiV3.ChannelStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isLinked** | **Boolean** | If true, then the user is linked to either a YouTube username or G+ account. Otherwise, the user doesn&#39;t have a public YouTube identity. | [optional] 
**longUploadsStatus** | **String** | The long uploads status of this channel. See https://support.google.com/youtube/answer/71673 for more information. | [optional] 
**madeForKids** | **Boolean** |  | [optional] 
**privacyStatus** | **String** | Privacy status of the channel. | [optional] 
**selfDeclaredMadeForKids** | **Boolean** |  | [optional] 



## Enum: LongUploadsStatusEnum


* `longUploadsUnspecified` (value: `"longUploadsUnspecified"`)

* `allowed` (value: `"allowed"`)

* `eligible` (value: `"eligible"`)

* `disallowed` (value: `"disallowed"`)





## Enum: PrivacyStatusEnum


* `public` (value: `"public"`)

* `unlisted` (value: `"unlisted"`)

* `private` (value: `"private"`)




