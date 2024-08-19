# AmazonConnectService.CreateInstanceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | The idempotency token. | [optional] 
**identityManagementType** | **String** | The type of identity management for your Amazon Connect users. | 
**instanceAlias** | **String** | The name for your instance. | [optional] 
**directoryId** | **String** | The identifier for the directory. | [optional] 
**inboundCallsEnabled** | **Boolean** | Your contact center handles incoming contacts. | 
**outboundCallsEnabled** | **Boolean** | Your contact center allows outbound calls. | 



## Enum: IdentityManagementTypeEnum


* `SAML` (value: `"SAML"`)

* `CONNECT_MANAGED` (value: `"CONNECT_MANAGED"`)

* `EXISTING_DIRECTORY` (value: `"EXISTING_DIRECTORY"`)




