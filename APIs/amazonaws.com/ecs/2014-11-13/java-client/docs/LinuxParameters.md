

# LinuxParameters

The Linux-specific options that are applied to the container, such as Linux <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html\">KernelCapabilities</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**LinuxParametersCapabilities**](LinuxParametersCapabilities.md) |  |  [optional] |
|**devices** | [**List**](List.md) |  |  [optional] |
|**initProcessEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**sharedMemorySize** | [**Integer**](Integer.md) |  |  [optional] |
|**tmpfs** | [**List**](List.md) |  |  [optional] |
|**maxSwap** | [**Integer**](Integer.md) |  |  [optional] |
|**swappiness** | [**Integer**](Integer.md) |  |  [optional] |



