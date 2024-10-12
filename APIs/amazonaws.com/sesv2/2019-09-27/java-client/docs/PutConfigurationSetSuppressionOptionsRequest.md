

# PutConfigurationSetSuppressionOptionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suppressedReasons** | **List&lt;SuppressionListReason&gt;** | &lt;p&gt;A list that contains the reasons that email addresses are automatically added to the suppression list for your account. This list can contain any or all of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;COMPLAINT&lt;/code&gt; – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BOUNCE&lt;/code&gt; – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



