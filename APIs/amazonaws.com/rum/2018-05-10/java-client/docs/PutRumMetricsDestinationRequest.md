

# PutRumMetricsDestinationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**DestinationEnum**](#DestinationEnum) | Defines the destination to send the metrics to. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;. If you specify &lt;code&gt;Evidently&lt;/code&gt;, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment. |  |
|**destinationArn** | **String** | Use this parameter only if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics. |  [optional] |
|**iamRoleArn** | **String** | &lt;p&gt;This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter.&lt;/p&gt; &lt;p&gt;This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.&lt;/p&gt; |  [optional] |



## Enum: DestinationEnum

| Name | Value |
|---- | -----|
| CLOUD_WATCH | &quot;CloudWatch&quot; |
| EVIDENTLY | &quot;Evidently&quot; |



