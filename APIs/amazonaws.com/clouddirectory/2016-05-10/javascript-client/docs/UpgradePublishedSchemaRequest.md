# AmazonCloudDirectory.UpgradePublishedSchemaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developmentSchemaArn** | **String** | The ARN of the development schema with the changes used for the upgrade. | 
**publishedSchemaArn** | **String** | The ARN of the published schema to be upgraded. | 
**minorVersion** | **String** | Identifies the minor version of the published schema that will be created. This parameter is NOT optional. | 
**dryRun** | **Boolean** | Used for testing whether the Development schema provided is backwards compatible, or not, with the publish schema provided by the user to be upgraded. If schema compatibility fails, an exception would be thrown else the call would succeed. This parameter is optional and defaults to false. | [optional] 


