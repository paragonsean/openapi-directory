# AmazonChimeSdkMessaging.CreateChannelMembershipRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memberArn** | **String** | The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member you want to add to the channel. | 
**type** | **String** | The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are always returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt;. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. Otherwise hidden members are not returned. This is only supported by moderators. | 
**subChannelId** | **String** | &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when creating membership in a SubChannel for a moderator in an elastic channel.&lt;/p&gt; &lt;/note&gt; | [optional] 



## Enum: TypeEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `HIDDEN` (value: `"HIDDEN"`)




