

# CreateChannelMembershipRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**memberArn** | **String** | The ARN of the member you want to add to the channel. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are always returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt;. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. Otherwise hidden members are not returned. This is only supported by moderators. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| HIDDEN | &quot;HIDDEN&quot; |



