# MessagingApiV3X.UpdateNumberRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replyCallbackUrl** | **String** | Tell us the URL that replies to the Virtual Number should be sent to.  Note that if you don&#39;t include this field, any pre-existing replyCallbackUrl will be wiped.  Sample callback response:  &lt;pre&gt;&lt;code class&#x3D;\&quot;language-sh\&quot;&gt;{   \&quot;to\&quot;:\&quot;0476543210\&quot;,    \&quot;from\&quot;:\&quot;0401234567\&quot;,    \&quot;timestamp\&quot;:\&quot;2022-11-10T05:06:42.823Z\&quot;,   \&quot;messageId\&quot;:\&quot;75f263c0-60b5-11ed-8456-71ae4c63550d\&quot;,    \&quot;messageContent\&quot;:\&quot;Hi, example message\&quot;,    \&quot;multimedia\&quot;: {      \&quot;fileName:\&quot;image.jpeg\&quot;      \&quot;type:\&quot;image/jpeg\&quot;      \&quot;payload\&quot;:\&quot;base64 payload\&quot;    } }&lt;/code&gt;&lt;/pre&gt;  | [optional] 
**tags** | **[String]** | Create your own tags and use them to fetch, sort and report on your Virtual Numbers through our other endpoints. You can assign up to 10 tags per number.   Note that if you don&#39;t include this field, any pre-existing tags will be wiped.  | [optional] 


