

# CreateFileCacheRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRequestToken** | [**String**](String.md) |  |  [optional] |
|**fileCacheType** | [**FileCacheType**](FileCacheType.md) |  |  |
|**fileCacheTypeVersion** | [**String**](String.md) |  |  |
|**storageCapacity** | [**Integer**](Integer.md) |  |  |
|**subnetIds** | **List&lt;String&gt;** | A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the &lt;code&gt;CreateFileCache&lt;/code&gt; operation. |  |
|**securityGroupIds** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. |  [optional] |
|**copyTagsToDataRepositoryAssociations** | [**Boolean**](Boolean.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**lustreConfiguration** | [**CreateFileCacheRequestLustreConfiguration**](CreateFileCacheRequestLustreConfiguration.md) |  |  [optional] |
|**dataRepositoryAssociations** | [**List**](List.md) |  |  [optional] |



