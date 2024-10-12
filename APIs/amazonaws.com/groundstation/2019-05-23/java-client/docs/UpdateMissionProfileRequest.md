

# UpdateMissionProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactPostPassDurationSeconds** | **Integer** | Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating the pass has finished. |  [optional] |
|**contactPrePassDurationSeconds** | **Integer** | Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating the pass has finished. |  [optional] |
|**dataflowEdges** | **List&lt;List&lt;String&gt;&gt;** | A list of lists of ARNs. Each list of ARNs is an edge, with a &lt;i&gt;from&lt;/i&gt; &lt;code&gt;Config&lt;/code&gt; and a &lt;i&gt;to&lt;/i&gt; &lt;code&gt;Config&lt;/code&gt;. |  [optional] |
|**minimumViableContactDurationSeconds** | **Integer** | Smallest amount of time in seconds that you’d like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration. |  [optional] |
|**name** | **String** | Name of a mission profile. |  [optional] |
|**streamsKmsKey** | [**CreateMissionProfileRequestStreamsKmsKey**](CreateMissionProfileRequestStreamsKmsKey.md) |  |  [optional] |
|**streamsKmsRole** | **String** | Role to use for encrypting streams with KMS key. |  [optional] |
|**trackingConfigArn** | **String** | ARN of a tracking &lt;code&gt;Config&lt;/code&gt;. |  [optional] |



