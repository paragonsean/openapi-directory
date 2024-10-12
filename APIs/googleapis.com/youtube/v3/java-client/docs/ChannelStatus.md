

# ChannelStatus

JSON template for the status part of a channel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isLinked** | **Boolean** | If true, then the user is linked to either a YouTube username or G+ account. Otherwise, the user doesn&#39;t have a public YouTube identity. |  [optional] |
|**longUploadsStatus** | [**LongUploadsStatusEnum**](#LongUploadsStatusEnum) | The long uploads status of this channel. See https://support.google.com/youtube/answer/71673 for more information. |  [optional] |
|**madeForKids** | **Boolean** |  |  [optional] |
|**privacyStatus** | [**PrivacyStatusEnum**](#PrivacyStatusEnum) | Privacy status of the channel. |  [optional] |
|**selfDeclaredMadeForKids** | **Boolean** |  |  [optional] |



## Enum: LongUploadsStatusEnum

| Name | Value |
|---- | -----|
| LONG_UPLOADS_UNSPECIFIED | &quot;longUploadsUnspecified&quot; |
| ALLOWED | &quot;allowed&quot; |
| ELIGIBLE | &quot;eligible&quot; |
| DISALLOWED | &quot;disallowed&quot; |



## Enum: PrivacyStatusEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| UNLISTED | &quot;unlisted&quot; |
| PRIVATE | &quot;private&quot; |



