

# RegisterAppInstanceUserEndpointRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &lt;p&gt;The type of the &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;. Supported types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;APNS&lt;/code&gt;: The mobile notification service for an Apple device.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;APNS_SANDBOX&lt;/code&gt;: The sandbox environment of the mobile notification service for an Apple device.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GCM&lt;/code&gt;: The mobile notification service for an Android device.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Populate the &lt;code&gt;ResourceArn&lt;/code&gt; value of each type as &lt;code&gt;PinpointAppArn&lt;/code&gt;.&lt;/p&gt; |  |
|**resourceArn** | **String** | The ARN of the resource to which the endpoint belongs. |  |
|**endpointAttributes** | [**RegisterAppInstanceUserEndpointRequestEndpointAttributes**](RegisterAppInstanceUserEndpointRequestEndpointAttributes.md) |  |  |
|**clientRequestToken** | **String** | The unique ID assigned to the request. Use different tokens to register other endpoints. |  |
|**allowMessages** | [**AllowMessagesEnum**](#AllowMessagesEnum) | Boolean that controls whether the AppInstanceUserEndpoint is opted in to receive messages. &lt;code&gt;ALL&lt;/code&gt; indicates the endpoint receives all messages. &lt;code&gt;NONE&lt;/code&gt; indicates the endpoint receives no messages. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APNS | &quot;APNS&quot; |
| APNS_SANDBOX | &quot;APNS_SANDBOX&quot; |
| GCM | &quot;GCM&quot; |



## Enum: AllowMessagesEnum

| Name | Value |
|---- | -----|
| ALL | &quot;ALL&quot; |
| NONE | &quot;NONE&quot; |



