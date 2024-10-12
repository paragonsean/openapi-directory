# AmazonChimeSdkIdentity.CreateAppInstanceUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appInstanceArn** | **String** | The ARN of the &lt;code&gt;AppInstance&lt;/code&gt; request. | 
**appInstanceUserId** | **String** | The user ID of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
**name** | **String** | The user&#39;s name. | 
**metadata** | **String** | The request&#39;s metadata. Limited to a 1KB string in UTF-8. | [optional] 
**clientRequestToken** | **String** | The unique ID of the request. Use different tokens to request additional &lt;code&gt;AppInstances&lt;/code&gt;. | 
**tags** | [**[Tag]**](Tag.md) | Tags assigned to the &lt;code&gt;AppInstanceUser&lt;/code&gt;. | [optional] 
**expirationSettings** | [**CreateAppInstanceUserRequestExpirationSettings**](CreateAppInstanceUserRequestExpirationSettings.md) |  | [optional] 


