# ServiceConsumerManagementApi.UsageRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowUnregisteredCalls** | **Boolean** | If true, the selected method allows unregistered calls, e.g. calls that don&#39;t identify any user or application. | [optional] 
**selector** | **String** | Selects the methods to which this rule applies. Use &#39;*&#39; to indicate all methods in all APIs. Refer to selector for syntax details. | [optional] 
**skipServiceControl** | **Boolean** | If true, the selected method should skip service control and the control plane features, such as quota and billing, will not be available. This flag is used by Google Cloud Endpoints to bypass checks for internal methods, such as service health check methods. | [optional] 


