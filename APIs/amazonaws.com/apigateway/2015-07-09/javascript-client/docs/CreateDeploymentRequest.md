# AmazonApiGateway.CreateDeploymentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stageName** | **String** | The name of the Stage resource for the Deployment resource to create. | [optional] 
**stageDescription** | **String** | The description of the Stage resource for the Deployment resource to create. | [optional] 
**description** | **String** | The description for the Deployment resource to create. | [optional] 
**cacheClusterEnabled** | **Boolean** | Enables a cache cluster for the Stage resource specified in the input. | [optional] 
**cacheClusterSize** | **String** | Returns the size of the CacheCluster. | [optional] 
**variables** | **{String: String}** | A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match &lt;code&gt;[A-Za-z0-9-._~:/?#&amp;amp;&#x3D;,]+&lt;/code&gt;. | [optional] 
**canarySettings** | [**CreateDeploymentRequestCanarySettings**](CreateDeploymentRequestCanarySettings.md) |  | [optional] 
**tracingEnabled** | **Boolean** | Specifies whether active tracing with X-ray is enabled for the Stage. | [optional] 



## Enum: CacheClusterSizeEnum


* `0.5` (value: `"0.5"`)

* `1.6` (value: `"1.6"`)

* `6.1` (value: `"6.1"`)

* `13.5` (value: `"13.5"`)

* `28.4` (value: `"28.4"`)

* `58.2` (value: `"58.2"`)

* `118` (value: `"118"`)

* `237` (value: `"237"`)




