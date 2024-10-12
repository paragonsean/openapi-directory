

# TensorflowResourceHandleProto

Protocol buffer representing a handle to a tensorflow resource. Handles are not valid across executions, but can be serialized back and forth from within a single run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | **String** | Container in which this resource is placed. |  [optional] |
|**device** | **String** | Unique name for the device containing the resource. |  [optional] |
|**hashCode** | **String** | Hash code for the type of the resource. Is only valid in the same device and in the same execution. |  [optional] |
|**maybeTypeName** | **String** | For debug-only, the name of the type pointed to by this handle, if available. |  [optional] |
|**name** | **String** | Unique name of this resource. |  [optional] |



