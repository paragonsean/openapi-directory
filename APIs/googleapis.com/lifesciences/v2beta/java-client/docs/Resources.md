

# Resources

The system resources for the pipeline run. At least one zone or region must be specified or the pipeline run will fail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**regions** | **List&lt;String&gt;** | The list of regions allowed for VM allocation. If set, the &#x60;zones&#x60; field must not be set. |  [optional] |
|**virtualMachine** | [**VirtualMachine**](VirtualMachine.md) |  |  [optional] |
|**zones** | **List&lt;String&gt;** | The list of zones allowed for VM allocation. If set, the &#x60;regions&#x60; field must not be set. |  [optional] |



