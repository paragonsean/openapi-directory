# AmazonFsx.CreateFileCacheRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRequestToken** | **String** |  | [optional] 
**fileCacheType** | [**FileCacheType**](FileCacheType.md) |  | 
**fileCacheTypeVersion** | **String** |  | 
**storageCapacity** | **Number** |  | 
**subnetIds** | **[String]** | A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the &lt;code&gt;CreateFileCache&lt;/code&gt; operation. | 
**securityGroupIds** | **Array** |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. | [optional] 
**copyTagsToDataRepositoryAssociations** | **Boolean** |  | [optional] 
**kmsKeyId** | **String** |  | [optional] 
**lustreConfiguration** | [**CreateFileCacheRequestLustreConfiguration**](CreateFileCacheRequestLustreConfiguration.md) |  | [optional] 
**dataRepositoryAssociations** | **Array** |  | [optional] 


