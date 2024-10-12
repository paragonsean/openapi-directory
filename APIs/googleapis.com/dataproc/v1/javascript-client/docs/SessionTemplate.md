# CloudDataprocApi.SessionTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the template was created. | [optional] [readonly] 
**creator** | **String** | Output only. The email address of the user who created the template. | [optional] [readonly] 
**description** | **String** | Optional. Brief description of the template. | [optional] 
**environmentConfig** | [**EnvironmentConfig**](EnvironmentConfig.md) |  | [optional] 
**jupyterSession** | [**JupyterConfig**](JupyterConfig.md) |  | [optional] 
**labels** | **{String: String}** | Optional. Labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. | [optional] 
**name** | **String** | Required. The resource name of the session template. | [optional] 
**runtimeConfig** | [**RuntimeConfig**](RuntimeConfig.md) |  | [optional] 
**updateTime** | **String** | Output only. The time the template was last updated. | [optional] [readonly] 
**uuid** | **String** | Output only. A session template UUID (Unique Universal Identifier). The service generates this value when it creates the session template. | [optional] [readonly] 


