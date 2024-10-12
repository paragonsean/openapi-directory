# SwaggerHubRegistryApi.AmazonIntegration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether the integration is enabled or disabled | [optional] [default to true]
**id** | **String** | ID of the integration | [optional] [readonly] 
**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. | 
**accessKey** | **String** | AWS access key. Write-only property. Required to create and update the integration. | [optional] 
**apiId** | **String** | AWS ID of the API to update. Empty value will create a new API in AWS. | [optional] 
**basePathMode** | **String** | How to handle the API&#39;s &#x60;basePath&#x60; value. Refer to [AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html) for details. | [optional] [default to &#39;ignore&#39;]
**deploymentMode** | **String** | Should be \&quot;on save\&quot;. The value \&quot;never\&quot; means the integration is disabled. | [optional] [default to &#39;on save&#39;]
**publishMode** | **String** | How to update an existing API in AWS | [optional] [default to &#39;merge&#39;]
**region** | **String** | AWS region where the API will be published | 
**secretKey** | **String** | AWS secret key. Write-only property. Required to create and update the integration. | [optional] 
**updateDefinition** | **Boolean** | Whether to update the API definition with Amazon-specific extensions and compatibility modifications | [optional] [default to false]



## Enum: BasePathModeEnum


* `ignore` (value: `"ignore"`)

* `prepend` (value: `"prepend"`)

* `split` (value: `"split"`)





## Enum: DeploymentModeEnum


* `on save` (value: `"on save"`)

* `never` (value: `"never"`)





## Enum: PublishModeEnum


* `merge` (value: `"merge"`)

* `overwrite` (value: `"overwrite"`)





## Enum: RegionEnum


* `us-east-1` (value: `"us-east-1"`)

* `us-east-2` (value: `"us-east-2"`)

* `us-west-1` (value: `"us-west-1"`)

* `us-west-2` (value: `"us-west-2"`)

* `eu-west-1` (value: `"eu-west-1"`)

* `eu-west-2` (value: `"eu-west-2"`)

* `eu-west-3` (value: `"eu-west-3"`)

* `eu-central-1` (value: `"eu-central-1"`)

* `eu-north-1` (value: `"eu-north-1"`)

* `eu-south-1` (value: `"eu-south-1"`)

* `ap-east-1` (value: `"ap-east-1"`)

* `ap-south-1` (value: `"ap-south-1"`)

* `ap-southeast-1` (value: `"ap-southeast-1"`)

* `ap-southeast-2` (value: `"ap-southeast-2"`)

* `ap-northeast-1` (value: `"ap-northeast-1"`)

* `ap-northeast-2` (value: `"ap-northeast-2"`)

* `sa-east-1` (value: `"sa-east-1"`)

* `cn-north-1` (value: `"cn-north-1"`)

* `cn-northwest-1` (value: `"cn-northwest-1"`)

* `ca-central-1` (value: `"ca-central-1"`)

* `me-south-1` (value: `"me-south-1"`)

* `af-south-1` (value: `"af-south-1"`)




