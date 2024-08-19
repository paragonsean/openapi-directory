# CloudWatchRum.UpdateRumMetricDefinitionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **String** | The destination to send the metrics to. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;. If you specify &lt;code&gt;Evidently&lt;/code&gt;, you must also specify the ARN of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment. | 
**destinationArn** | **String** | &lt;p&gt;This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter.&lt;/p&gt; &lt;p&gt;This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html\&quot;&gt;PutRumMetricsDestination&lt;/a&gt;.&lt;/p&gt; | [optional] 
**metricDefinition** | [**UpdateRumMetricDefinitionRequestMetricDefinition**](UpdateRumMetricDefinitionRequestMetricDefinition.md) |  | 
**metricDefinitionId** | **String** | The ID of the metric definition to update. | 



## Enum: DestinationEnum


* `CloudWatch` (value: `"CloudWatch"`)

* `Evidently` (value: `"Evidently"`)




