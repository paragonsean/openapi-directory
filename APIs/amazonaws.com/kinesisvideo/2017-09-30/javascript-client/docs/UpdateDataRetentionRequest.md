# AmazonKinesisVideoStreams.UpdateDataRetentionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streamName** | **String** | The name of the stream whose retention period you want to change. | [optional] 
**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream whose retention period you want to change. | [optional] 
**currentVersion** | **String** | The version of the stream whose retention period you want to change. To get the version, call either the &lt;code&gt;DescribeStream&lt;/code&gt; or the &lt;code&gt;ListStreams&lt;/code&gt; API. | 
**operation** | **String** | Indicates whether you want to increase or decrease the retention period. | 
**dataRetentionChangeInHours** | **Number** | The retention period, in hours. The value you specify replaces the current value. The maximum value for this parameter is 87600 (ten years). | 



## Enum: OperationEnum


* `INCREASE_DATA_RETENTION` (value: `"INCREASE_DATA_RETENTION"`)

* `DECREASE_DATA_RETENTION` (value: `"DECREASE_DATA_RETENTION"`)




