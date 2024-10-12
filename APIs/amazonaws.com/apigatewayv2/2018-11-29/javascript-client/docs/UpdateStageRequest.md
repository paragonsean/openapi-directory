# AmazonApiGatewayV2.UpdateStageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessLogSettings** | [**CreateStageRequestAccessLogSettings**](CreateStageRequestAccessLogSettings.md) |  | [optional] 
**autoDeploy** | **Boolean** | Specifies whether updates to an API automatically trigger a new deployment. The default value is false. | [optional] 
**clientCertificateId** | **String** | The identifier. | [optional] 
**defaultRouteSettings** | [**CreateStageRequestDefaultRouteSettings**](CreateStageRequestDefaultRouteSettings.md) |  | [optional] 
**deploymentId** | **String** | The identifier. | [optional] 
**description** | **String** | A string with a length between [0-1024]. | [optional] 
**routeSettings** | [**{String: RouteSettings}**](RouteSettings.md) | The route settings map. | [optional] 
**stageVariables** | **{String: String}** | The stage variable map. | [optional] 


