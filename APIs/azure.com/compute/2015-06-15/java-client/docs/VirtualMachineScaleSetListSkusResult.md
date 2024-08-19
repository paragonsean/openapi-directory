

# VirtualMachineScaleSetListSkusResult

The Virtual Machine Scale Set List Skus operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | The URI to fetch the next page of skus available for the virtual machine scale set. Call ListNext() with this to fetch the next page of skus available for the virtual machine scale set. |  [optional] |
|**value** | [**List&lt;VirtualMachineScaleSetSku&gt;**](VirtualMachineScaleSetSku.md) | The list of skus available for the virtual machine scale set. |  [optional] [readonly] |



