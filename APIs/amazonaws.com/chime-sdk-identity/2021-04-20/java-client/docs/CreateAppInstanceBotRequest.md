

# CreateAppInstanceBotRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appInstanceArn** | **String** | The ARN of the &lt;code&gt;AppInstance&lt;/code&gt; request. |  |
|**name** | **String** | The user&#39;s name. |  [optional] |
|**metadata** | **String** | The request metadata. Limited to a 1KB string in UTF-8. |  [optional] |
|**clientRequestToken** | **String** | The unique ID for the client making the request. Use different tokens for different &lt;code&gt;AppInstanceBots&lt;/code&gt;. |  |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tags assigned to the &lt;code&gt;AppInstanceBot&lt;/code&gt;. |  [optional] |
|**_configuration** | [**CreateAppInstanceBotRequestConfiguration**](CreateAppInstanceBotRequestConfiguration.md) |  |  |



