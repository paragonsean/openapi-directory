

# PostTransitionsParametersAnyOf


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpu** | [**CpuEnum**](#CpuEnum) |  |  [optional] |
|**environment** | **Map&lt;String, String&gt;** |  |  [optional] |
|**environmentSecrets** | **List&lt;String&gt;** |  |  [optional] |
|**imageUrl** | **String** |  |  |
|**memory** | [**MemoryEnum**](#MemoryEnum) |  |  [optional] |
|**secretId** | **String** |  |  [optional] |



## Enum: CpuEnum

| Name | Value |
|---- | -----|
| NUMBER_256 | 256 |
| NUMBER_512 | 512 |
| NUMBER_1024 | 1024 |



## Enum: MemoryEnum

| Name | Value |
|---- | -----|
| NUMBER_512 | 512 |
| NUMBER_1024 | 1024 |
| NUMBER_2048 | 2048 |
| NUMBER_4096 | 4096 |
| NUMBER_8192 | 8192 |



