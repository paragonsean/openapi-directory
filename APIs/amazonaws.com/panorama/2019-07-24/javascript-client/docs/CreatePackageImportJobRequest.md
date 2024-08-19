# AwsPanorama.CreatePackageImportJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A client token for the package import job. | 
**inputConfig** | [**CreatePackageImportJobRequestInputConfig**](CreatePackageImportJobRequestInputConfig.md) |  | 
**jobTags** | [**[JobResourceTags]**](JobResourceTags.md) | Tags for the package import job. | [optional] 
**jobType** | **String** | A job type for the package import job. | 
**outputConfig** | [**CreatePackageImportJobRequestOutputConfig**](CreatePackageImportJobRequestOutputConfig.md) |  | 



## Enum: JobTypeEnum


* `NODE_PACKAGE_VERSION` (value: `"NODE_PACKAGE_VERSION"`)

* `MARKETPLACE_NODE_PACKAGE_VERSION` (value: `"MARKETPLACE_NODE_PACKAGE_VERSION"`)




