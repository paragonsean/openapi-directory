# AmazonApiGateway.CreateStageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stageName** | **String** | The name for the Stage resource. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters. | 
**deploymentId** | **String** | The identifier of the Deployment resource for the Stage resource. | 
**description** | **String** | The description of the Stage resource. | [optional] 
**cacheClusterEnabled** | **Boolean** | Whether cache clustering is enabled for the stage. | [optional] 
**cacheClusterSize** | **String** | Returns the size of the CacheCluster. | [optional] 
**variables** | **{String: String}** | A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match &lt;code&gt;[A-Za-z0-9-._~:/?#&amp;amp;&#x3D;,]+&lt;/code&gt;. | [optional] 
**documentationVersion** | **String** | The version of the associated API documentation. | [optional] 
**canarySettings** | [**CreateStageRequestCanarySettings**](CreateStageRequestCanarySettings.md) |  | [optional] 
**tracingEnabled** | **Boolean** | Specifies whether active tracing with X-ray is enabled for the Stage. | [optional] 
**tags** | **{String: String}** | The key-value map of strings. The valid character set is [a-zA-Z+-&#x3D;._:/]. The tag key can be up to 128 characters and must not start with &lt;code&gt;aws:&lt;/code&gt;. The tag value can be up to 256 characters. | [optional] 



## Enum: CacheClusterSizeEnum


* `0.5` (value: `"0.5"`)

* `1.6` (value: `"1.6"`)

* `6.1` (value: `"6.1"`)

* `13.5` (value: `"13.5"`)

* `28.4` (value: `"28.4"`)

* `58.2` (value: `"58.2"`)

* `118` (value: `"118"`)

* `237` (value: `"237"`)




