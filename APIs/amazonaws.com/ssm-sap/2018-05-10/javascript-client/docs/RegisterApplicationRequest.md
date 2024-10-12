# AwsSystemsManagerForSap.RegisterApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationId** | **String** | The ID of the application. | 
**applicationType** | **String** | The type of the application. | 
**instances** | **[String]** | The Amazon EC2 instances on which your SAP application is running. | 
**sapInstanceNumber** | **String** | The SAP instance number of the application. | [optional] 
**sid** | **String** | The System ID of the application. | [optional] 
**tags** | **{String: String}** | The tags to be attached to the SAP application. | [optional] 
**credentials** | [**[ApplicationCredential]**](ApplicationCredential.md) | The credentials of the SAP application. | 



## Enum: ApplicationTypeEnum


* `HANA` (value: `"HANA"`)




