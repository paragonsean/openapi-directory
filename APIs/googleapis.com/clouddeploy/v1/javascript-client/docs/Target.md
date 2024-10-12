# CloudDeployApi.Target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. | [optional] 
**anthosCluster** | [**AnthosCluster**](AnthosCluster.md) |  | [optional] 
**createTime** | **String** | Output only. Time at which the &#x60;Target&#x60; was created. | [optional] [readonly] 
**customTarget** | [**CustomTarget**](CustomTarget.md) |  | [optional] 
**deployParameters** | **{String: String}** | Optional. The deploy parameters to use for this target. | [optional] 
**description** | **String** | Optional. Description of the &#x60;Target&#x60;. Max length is 255 characters. | [optional] 
**etag** | **String** | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**executionConfigs** | [**[ExecutionConfig]**](ExecutionConfig.md) | Configurations for all execution that relates to this &#x60;Target&#x60;. Each &#x60;ExecutionEnvironmentUsage&#x60; value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the &#x60;RENDER&#x60; and &#x60;DEPLOY&#x60; &#x60;ExecutionEnvironmentUsage&#x60; values. When no configurations are specified, execution will use the default specified in &#x60;DefaultPool&#x60;. | [optional] 
**gke** | [**GkeCluster**](GkeCluster.md) |  | [optional] 
**labels** | **{String: String}** | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes. | [optional] 
**multiTarget** | [**MultiTarget**](MultiTarget.md) |  | [optional] 
**name** | **String** | Optional. Name of the &#x60;Target&#x60;. Format is &#x60;projects/{project}/locations/{location}/targets/a-z{0,62}&#x60;. | [optional] 
**requireApproval** | **Boolean** | Optional. Whether or not the &#x60;Target&#x60; requires approval. | [optional] 
**run** | [**CloudRunLocation**](CloudRunLocation.md) |  | [optional] 
**targetId** | **String** | Output only. Resource id of the &#x60;Target&#x60;. | [optional] [readonly] 
**uid** | **String** | Output only. Unique identifier of the &#x60;Target&#x60;. | [optional] [readonly] 
**updateTime** | **String** | Output only. Most recent time at which the &#x60;Target&#x60; was updated. | [optional] [readonly] 


