

# RuntimeConfig

Runtime configuration for a workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerImage** | **String** | Optional. Optional custom container image for the job runtime environment. If not specified, a default container image will be used. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values, which are used to configure workload execution. |  [optional] |
|**repositoryConfig** | [**RepositoryConfig**](RepositoryConfig.md) |  |  [optional] |
|**version** | **String** | Optional. Version of the batch runtime. |  [optional] |



