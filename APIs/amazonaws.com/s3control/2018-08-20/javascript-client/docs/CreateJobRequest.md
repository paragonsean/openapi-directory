# AwsS3Control.CreateJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmationRequired** | **Boolean** | Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console. | [optional] 
**operation** | [**CreateJobRequestOperation**](CreateJobRequestOperation.md) |  | 
**report** | [**CreateJobRequestReport**](CreateJobRequestReport.md) |  | 
**clientRequestToken** | **String** | An idempotency token to ensure that you don&#39;t accidentally submit the same request twice. You can use any string up to the maximum length. | 
**manifest** | [**CreateJobRequestManifest**](CreateJobRequestManifest.md) |  | [optional] 
**description** | **String** | A description for this job. You can use any string within the permitted length. Descriptions don&#39;t need to be unique and can be used for multiple jobs. | [optional] 
**priority** | **Number** | The numerical priority for this job. Higher numbers indicate higher priority. | 
**roleArn** | **String** | The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) role that Batch Operations will use to run this job&#39;s action on every object in the manifest. | 
**tags** | [**[S3Tag]**](S3Tag.md) | A set of tags to associate with the S3 Batch Operations job. This is an optional parameter.  | [optional] 
**manifestGenerator** | [**CreateJobRequestManifestGenerator**](CreateJobRequestManifestGenerator.md) |  | [optional] 


