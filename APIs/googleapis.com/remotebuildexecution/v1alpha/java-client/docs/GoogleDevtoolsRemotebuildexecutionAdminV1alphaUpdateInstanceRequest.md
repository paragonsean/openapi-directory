

# GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateInstanceRequest

The request used for `UpdateInstance`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instance** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance.md) |  |  [optional] |
|**loggingEnabled** | **Boolean** | Deprecated, use instance.logging_enabled instead. Whether to enable Stackdriver logging for this instance. |  [optional] |
|**name** | **String** | Deprecated, use instance.Name instead. Name of the instance to update. Format: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;. |  [optional] |
|**updateMask** | **String** | The update mask applies to instance. For the &#x60;FieldMask&#x60; definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask If an empty update_mask is provided, only the non-default valued field in the worker pool field will be updated. Note that in order to update a field to the default value (zero, false, empty string) an explicit update_mask must be provided. |  [optional] |



