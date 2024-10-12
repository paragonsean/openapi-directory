

# PutSuppressedDestinationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | The email address that should be added to the suppression list for your account. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | &lt;p&gt;The reason that the address was added to the suppression list for your account. The value can be one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;COMPLAINT&lt;/code&gt; – Amazon SES added an email address to the suppression list for your account because a message sent to that address results in a complaint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BOUNCE&lt;/code&gt; – Amazon SES added an email address to the suppression list for your account because a message sent to that address results in a hard bounce.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| BOUNCE | &quot;BOUNCE&quot; |
| COMPLAINT | &quot;COMPLAINT&quot; |



