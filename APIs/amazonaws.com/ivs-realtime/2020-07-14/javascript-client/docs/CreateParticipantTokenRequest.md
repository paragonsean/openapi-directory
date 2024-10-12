# AmazonInteractiveVideoServiceRealTime.CreateParticipantTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. &lt;i&gt;This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.&lt;/i&gt;  | [optional] 
**capabilities** | [**[ParticipantTokenCapability]**](ParticipantTokenCapability.md) | Set of capabilities that the user is allowed to perform in the stage. Default: &lt;code&gt;PUBLISH, SUBSCRIBE&lt;/code&gt;. | [optional] 
**duration** | **Number** | Duration (in minutes), after which the token expires. Default: 720 (12 hours). | [optional] 
**stageArn** | **String** | ARN of the stage to which this token is scoped. | 
**userId** | **String** | Name that can be specified to help identify the token. This can be any UTF-8 encoded text. &lt;i&gt;This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.&lt;/i&gt;  | [optional] 


