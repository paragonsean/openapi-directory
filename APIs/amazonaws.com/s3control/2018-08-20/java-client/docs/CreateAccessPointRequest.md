

# CreateAccessPointRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | **String** | &lt;p&gt;The name of the bucket that you want to associate this access point with.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; |  |
|**vpcConfiguration** | [**CreateAccessPointRequestVpcConfiguration**](CreateAccessPointRequestVpcConfiguration.md) |  |  [optional] |
|**publicAccessBlockConfiguration** | [**CreateAccessPointRequestPublicAccessBlockConfiguration**](CreateAccessPointRequestPublicAccessBlockConfiguration.md) |  |  [optional] |
|**bucketAccountId** | **String** | The Amazon Web Services account ID associated with the S3 bucket associated with this access point. |  [optional] |



