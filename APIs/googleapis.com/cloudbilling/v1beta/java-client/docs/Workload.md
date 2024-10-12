

# Workload

Specifies usage on a single Google Cloud product over a time frame. Each Google Cloud product has its own message, containing specific product configuration parameters of the product usage amounts along each dimension in which the product is billed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudCdnEgressWorkload** | [**CloudCdnEgressWorkload**](CloudCdnEgressWorkload.md) |  |  [optional] |
|**cloudCdnWorkload** | [**CloudCdnWorkload**](CloudCdnWorkload.md) |  |  [optional] |
|**cloudInterconnectEgressWorkload** | [**CloudInterconnectEgressWorkload**](CloudInterconnectEgressWorkload.md) |  |  [optional] |
|**cloudInterconnectWorkload** | [**CloudInterconnectWorkload**](CloudInterconnectWorkload.md) |  |  [optional] |
|**cloudStorageEgressWorkload** | [**CloudStorageEgressWorkload**](CloudStorageEgressWorkload.md) |  |  [optional] |
|**cloudStorageWorkload** | [**CloudStorageWorkload**](CloudStorageWorkload.md) |  |  [optional] |
|**computeVmWorkload** | [**ComputeVmWorkload**](ComputeVmWorkload.md) |  |  [optional] |
|**name** | **String** | Required. A name for this workload. All workloads in a &#x60;CostScenario&#x60; must have a unique &#x60;name&#x60;. Each &#x60;name&#x60; may be at most 128 characters long. |  [optional] |
|**premiumTierEgressWorkload** | [**PremiumTierEgressWorkload**](PremiumTierEgressWorkload.md) |  |  [optional] |
|**standardTierEgressWorkload** | [**StandardTierEgressWorkload**](StandardTierEgressWorkload.md) |  |  [optional] |
|**vmToVmEgressWorkload** | [**VmToVmEgressWorkload**](VmToVmEgressWorkload.md) |  |  [optional] |



