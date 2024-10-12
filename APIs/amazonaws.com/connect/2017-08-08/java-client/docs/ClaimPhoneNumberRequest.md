

# ClaimPhoneNumberRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetArn** | **String** | The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution groups that phone numbers are claimed to. |  |
|**phoneNumber** | **String** | The phone number you want to claim. Phone numbers are formatted &lt;code&gt;[+] [country code] [subscriber number including area code]&lt;/code&gt;. |  |
|**phoneNumberDescription** | **String** | The description of the phone number. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |
|**clientToken** | **String** | &lt;p&gt;A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Pattern: &lt;code&gt;^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$&lt;/code&gt; &lt;/p&gt; |  [optional] |



