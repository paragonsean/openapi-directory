

# UpdateInstanceConfigRequest

The request for UpdateInstanceConfigRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceConfig** | [**InstanceConfig**](InstanceConfig.md) |  |  [optional] |
|**updateMask** | **String** | Required. A mask specifying which fields in InstanceConfig should be updated. The field mask must always be specified; this prevents any future fields in InstanceConfig from being erased accidentally by clients that do not know about them. Only display_name and labels can be updated. |  [optional] |
|**validateOnly** | **Boolean** | An option to validate, but not actually execute, a request, and provide the same response. |  [optional] |



