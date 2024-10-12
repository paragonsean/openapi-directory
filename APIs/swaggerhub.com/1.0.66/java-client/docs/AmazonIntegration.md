

# AmazonIntegration

Common configuration details for Amazon integrations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**accessKey** | **String** | AWS access key. Write-only property. Required to create and update the integration. |  [optional] |
|**apiId** | **String** | AWS ID of the API to update. Empty value will create a new API in AWS. |  [optional] |
|**basePathMode** | [**BasePathModeEnum**](#BasePathModeEnum) | How to handle the API&#39;s &#x60;basePath&#x60; value. Refer to [AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html) for details. |  [optional] |
|**deploymentMode** | [**DeploymentModeEnum**](#DeploymentModeEnum) | Should be \&quot;on save\&quot;. The value \&quot;never\&quot; means the integration is disabled. |  [optional] |
|**publishMode** | [**PublishModeEnum**](#PublishModeEnum) | How to update an existing API in AWS |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | AWS region where the API will be published |  |
|**secretKey** | **String** | AWS secret key. Write-only property. Required to create and update the integration. |  [optional] |
|**updateDefinition** | **Boolean** | Whether to update the API definition with Amazon-specific extensions and compatibility modifications |  [optional] |



## Enum: BasePathModeEnum

| Name | Value |
|---- | -----|
| IGNORE | &quot;ignore&quot; |
| PREPEND | &quot;prepend&quot; |
| SPLIT | &quot;split&quot; |



## Enum: DeploymentModeEnum

| Name | Value |
|---- | -----|
| ON_SAVE | &quot;on save&quot; |
| NEVER | &quot;never&quot; |



## Enum: PublishModeEnum

| Name | Value |
|---- | -----|
| MERGE | &quot;merge&quot; |
| OVERWRITE | &quot;overwrite&quot; |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| US_EAST_1 | &quot;us-east-1&quot; |
| US_EAST_2 | &quot;us-east-2&quot; |
| US_WEST_1 | &quot;us-west-1&quot; |
| US_WEST_2 | &quot;us-west-2&quot; |
| EU_WEST_1 | &quot;eu-west-1&quot; |
| EU_WEST_2 | &quot;eu-west-2&quot; |
| EU_WEST_3 | &quot;eu-west-3&quot; |
| EU_CENTRAL_1 | &quot;eu-central-1&quot; |
| EU_NORTH_1 | &quot;eu-north-1&quot; |
| EU_SOUTH_1 | &quot;eu-south-1&quot; |
| AP_EAST_1 | &quot;ap-east-1&quot; |
| AP_SOUTH_1 | &quot;ap-south-1&quot; |
| AP_SOUTHEAST_1 | &quot;ap-southeast-1&quot; |
| AP_SOUTHEAST_2 | &quot;ap-southeast-2&quot; |
| AP_NORTHEAST_1 | &quot;ap-northeast-1&quot; |
| AP_NORTHEAST_2 | &quot;ap-northeast-2&quot; |
| SA_EAST_1 | &quot;sa-east-1&quot; |
| CN_NORTH_1 | &quot;cn-north-1&quot; |
| CN_NORTHWEST_1 | &quot;cn-northwest-1&quot; |
| CA_CENTRAL_1 | &quot;ca-central-1&quot; |
| ME_SOUTH_1 | &quot;me-south-1&quot; |
| AF_SOUTH_1 | &quot;af-south-1&quot; |



