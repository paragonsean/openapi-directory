# AmazonNimbleStudio.CreateStudioRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminRoleArn** | **String** | The IAM role that studio admins will assume when logging in to the Nimble Studio portal. | 
**displayName** | **String** | A friendly name for the studio. | 
**studioEncryptionConfiguration** | [**CreateStudioRequestStudioEncryptionConfiguration**](CreateStudioRequestStudioEncryptionConfiguration.md) |  | [optional] 
**studioName** | **String** | The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users. | 
**tags** | **{String: String}** | A collection of labels, in the form of key-value pairs, that apply to this resource. | [optional] 
**userRoleArn** | **String** | The IAM role that studio users will assume when logging in to the Nimble Studio portal. | 


