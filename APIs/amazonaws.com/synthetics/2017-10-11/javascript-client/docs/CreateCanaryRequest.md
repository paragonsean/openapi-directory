# Synthetics.CreateCanaryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | &lt;p&gt;The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.&lt;/p&gt; &lt;p&gt;Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\&quot;&gt;Security Considerations for Synthetics Canaries&lt;/a&gt;.&lt;/p&gt; | 
**code** | [**CreateCanaryRequestCode**](CreateCanaryRequestCode.md) |  | 
**artifactS3Location** | **String** | The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the S3 bucket can&#39;t include a period (.). | 
**executionRoleArn** | **String** | &lt;p&gt;The ARN of the IAM role to be used to run the canary. This role must already exist, and must include &lt;code&gt;lambda.amazonaws.com&lt;/code&gt; as a principal in the trust policy. The role must also have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:PutObject&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:GetBucketLocation&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;s3:ListAllMyBuckets&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudwatch:PutMetricData&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logs:CreateLogGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logs:CreateLogStream&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logs:PutLogEvents&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**schedule** | [**CreateCanaryRequestSchedule**](CreateCanaryRequestSchedule.md) |  | 
**runConfig** | [**CreateCanaryRequestRunConfig**](CreateCanaryRequestRunConfig.md) |  | [optional] 
**successRetentionPeriodInDays** | **Number** | The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days. | [optional] 
**failureRetentionPeriodInDays** | **Number** | The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days. | [optional] 
**runtimeVersion** | **String** | Specifies the runtime version to use for the canary. For a list of valid runtime versions and more information about runtime versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\&quot;&gt; Canary Runtime Versions&lt;/a&gt;. | 
**vpcConfig** | [**CreateCanaryRequestVpcConfig**](CreateCanaryRequestVpcConfig.md) |  | [optional] 
**tags** | **{String: String}** | &lt;p&gt;A list of key-value pairs to associate with the canary. You can associate as many as 50 tags with a canary.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.&lt;/p&gt; | [optional] 
**artifactConfig** | [**CreateCanaryRequestArtifactConfig**](CreateCanaryRequestArtifactConfig.md) |  | [optional] 


