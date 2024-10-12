# RubrikRestApi.ParentAppInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | ID assigned to the vApp object that manages a specified virtual machine. | [optional] 
**isProtectedThruHierarchy** | **Boolean** | Boolean value that indicates whether a virtual machine is protected through the SLA Domain assigned to the parent vApp. Set to &#39;true&#39; when the virtual machine is protected through the parent vApp, otherwise set to &#39;false&#39;. Direct assignment of a virtual machine to an SLA Domain is not possible when this value is &#39;true&#39;. Also, setting this value to true is not possible when the virtual machine has an existing direct assignment to an SLA Domain. | 


