

# UpdateCanaryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CreateCanaryRequestCode**](CreateCanaryRequestCode.md) |  |  [optional] |
|**executionRoleArn** | **String** | &lt;p&gt;The ARN of the IAM role to be used to run the canary. This role must already exist, and must include &lt;code&gt;lambda.amazonaws.com&lt;/code&gt; as a principal in the trust policy. The role must also have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:PutObject&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:GetBucketLocation&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:ListAllMyBuckets&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudwatch:PutMetricData&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logs:CreateLogGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logs:CreateLogStream&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logs:CreateLogStream&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**runtimeVersion** | **String** | Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\&quot;&gt; Canary Runtime Versions&lt;/a&gt;. |  [optional] |
|**schedule** | [**CreateCanaryRequestSchedule**](CreateCanaryRequestSchedule.md) |  |  [optional] |
|**runConfig** | [**CreateCanaryRequestRunConfig**](CreateCanaryRequestRunConfig.md) |  |  [optional] |
|**successRetentionPeriodInDays** | **Integer** | The number of days to retain data about successful runs of this canary. |  [optional] |
|**failureRetentionPeriodInDays** | **Integer** | The number of days to retain data about failed runs of this canary. |  [optional] |
|**vpcConfig** | [**CreateCanaryRequestVpcConfig**](CreateCanaryRequestVpcConfig.md) |  |  [optional] |
|**visualReference** | [**UpdateCanaryRequestVisualReference**](UpdateCanaryRequestVisualReference.md) |  |  [optional] |
|**artifactS3Location** | **String** | The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the S3 bucket can&#39;t include a period (.). |  [optional] |
|**artifactConfig** | [**CreateCanaryRequestArtifactConfig**](CreateCanaryRequestArtifactConfig.md) |  |  [optional] |



