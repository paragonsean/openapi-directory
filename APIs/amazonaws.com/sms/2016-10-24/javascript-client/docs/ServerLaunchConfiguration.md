# AwsServerMigrationService.ServerLaunchConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**ServerLaunchConfigurationServer**](ServerLaunchConfigurationServer.md) |  | [optional] 
**logicalId** | **String** |  | [optional] 
**vpc** | **String** |  | [optional] 
**subnet** | **String** |  | [optional] 
**securityGroup** | **String** |  | [optional] 
**ec2KeyName** | **String** |  | [optional] 
**userData** | [**ServerLaunchConfigurationUserData**](ServerLaunchConfigurationUserData.md) |  | [optional] 
**instanceType** | **String** |  | [optional] 
**associatePublicIpAddress** | **Boolean** |  | [optional] 
**iamInstanceProfileName** | **String** |  | [optional] 
**configureScript** | [**S3Location**](S3Location.md) |  | [optional] 
**configureScriptType** | [**ScriptType**](ScriptType.md) |  | [optional] 


