

# BatchCreateChannelMembershipRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are always returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt;. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. Otherwise hidden members are not returned. This is only supported by moderators. |  [optional] |
|**memberArns** | **List&lt;String&gt;** | The ARNs of the members you want to add to the channel. Only &lt;code&gt;AppInstanceUsers&lt;/code&gt; and &lt;code&gt;AppInstanceBots&lt;/code&gt; can be added as a channel member. |  |
|**subChannelId** | **String** | &lt;p&gt;The ID of the SubChannel in the request. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when creating membership in a SubChannel for a moderator in an elastic channel.&lt;/p&gt; &lt;/note&gt; |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| HIDDEN | &quot;HIDDEN&quot; |



