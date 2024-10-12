

# CreateBulkImportJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobName** | **String** | The unique name that helps identify the job request. |  |
|**jobRoleArn** | **String** | The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the IAM role that allows IoT SiteWise to read Amazon S3 data. |  |
|**files** | [**List&lt;ModelFile&gt;**](ModelFile.md) | The files in the specified Amazon S3 bucket that contain your data. |  |
|**errorReportLocation** | [**CreateBulkImportJobRequestErrorReportLocation**](CreateBulkImportJobRequestErrorReportLocation.md) |  |  |
|**jobConfiguration** | [**CreateBulkImportJobRequestJobConfiguration**](CreateBulkImportJobRequestJobConfiguration.md) |  |  |



