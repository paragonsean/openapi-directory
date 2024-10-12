

# CustomMachineType

Specification of a custom machine type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**machineSeries** | **String** | Required. The machine series. Only certain [machine series](https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) support custom configurations. For example: \&quot;n1\&quot;. |  [optional] |
|**memorySizeGb** | **Double** | Required. Memory size of the VM in GB (2^30 bytes). Must be an increment of 0.25 (256 MB). Each [machine series](https://cloud.google.com/compute/docs/machine-types#machine_type_comparison) has limitations on allowed values for the ratio of memory-to-vCPU count. |  [optional] |
|**virtualCpuCount** | **String** | Required. The number of vCPUs. The allowed values depend on the [machine series](https://cloud.google.com/compute/docs/machine-types#machine_type_comparison). |  [optional] |



