# AwsMigrationHubRefactorSpaces.CreateEnvironmentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**description** | **String** | The description of the environment. | [optional] 
**name** | **String** | The name of the environment. | 
**networkFabricType** | **String** | The network fabric type of the environment. | 
**tags** | **{String: String}** | A collection of up to 50 unique tags | [optional] 



## Enum: NetworkFabricTypeEnum


* `TRANSIT_GATEWAY` (value: `"TRANSIT_GATEWAY"`)

* `NONE` (value: `"NONE"`)




