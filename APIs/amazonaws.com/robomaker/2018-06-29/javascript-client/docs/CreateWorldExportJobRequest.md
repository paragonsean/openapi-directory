# AwsRoboMaker.CreateWorldExportJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**worlds** | **[String]** | A list of Amazon Resource Names (arns) that correspond to worlds to export. | 
**outputLocation** | [**CreateSimulationJobRequestOutputLocation**](CreateSimulationJobRequestOutputLocation.md) |  | 
**iamRole** | **String** | The IAM role that the world export process uses to access the Amazon S3 bucket and put the export. | 
**tags** | **{String: String}** | A map that contains tag keys and tag values that are attached to the world export job. | [optional] 


