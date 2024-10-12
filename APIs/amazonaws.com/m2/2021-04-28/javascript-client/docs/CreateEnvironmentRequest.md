# AwsMainframeModernization.CreateEnvironmentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.  | [optional] 
**description** | **String** | The description of the runtime environment. | [optional] 
**engineType** | **String** | The engine type for the runtime environment. | 
**engineVersion** | **String** | The version of the engine type for the runtime environment. | [optional] 
**highAvailabilityConfig** | [**CreateEnvironmentRequestHighAvailabilityConfig**](CreateEnvironmentRequestHighAvailabilityConfig.md) |  | [optional] 
**instanceType** | **String** | The type of instance for the runtime environment. | 
**kmsKeyId** | **String** | The identifier of a customer managed key. | [optional] 
**name** | **String** | The name of the runtime environment. Must be unique within the account. | 
**preferredMaintenanceWindow** | **String** | Configures the maintenance window you want for the runtime environment. If you do not provide a value, a random system-generated value will be assigned. | [optional] 
**publiclyAccessible** | **Boolean** | Specifies whether the runtime environment is publicly accessible. | [optional] 
**securityGroupIds** | **[String]** | The list of security groups for the VPC associated with this runtime environment. | [optional] 
**storageConfigurations** | [**[StorageConfiguration]**](StorageConfiguration.md) | Optional. The storage configurations for this runtime environment. | [optional] 
**subnetIds** | **[String]** | The list of subnets associated with the VPC for this runtime environment. | [optional] 
**tags** | **{String: String}** | The tags for the runtime environment. | [optional] 



## Enum: EngineTypeEnum


* `microfocus` (value: `"microfocus"`)

* `bluage` (value: `"bluage"`)




