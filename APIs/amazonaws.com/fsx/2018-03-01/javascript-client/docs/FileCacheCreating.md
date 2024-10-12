# AmazonFsx.FileCacheCreating

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ownerId** | **String** | An Amazon Web Services account ID. This ID is a 12-digit number that you use to construct Amazon Resource Names (ARNs) for resources. | [optional] 
**creationTime** | **Date** | The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time. | [optional] 
**fileCacheId** | **String** |  | [optional] 
**fileCacheType** | [**FileCacheType**](FileCacheType.md) |  | [optional] 
**fileCacheTypeVersion** | **String** |  | [optional] 
**lifecycle** | [**FileCacheLifecycle**](FileCacheLifecycle.md) |  | [optional] 
**failureDetails** | [**FileCacheCreatingFailureDetails**](FileCacheCreatingFailureDetails.md) |  | [optional] 
**storageCapacity** | **Number** |  | [optional] 
**vpcId** | **String** | The ID of your virtual private cloud (VPC). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html\&quot;&gt;VPC and subnets&lt;/a&gt; in the &lt;i&gt;Amazon VPC User Guide&lt;/i&gt;. | [optional] 
**subnetIds** | **[String]** | A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the &lt;code&gt;CreateFileCache&lt;/code&gt; operation. | [optional] 
**networkInterfaceIds** | **[String]** | A list of network interface IDs. | [optional] 
**dNSName** | **String** |  | [optional] 
**kmsKeyId** | **String** |  | [optional] 
**resourceARN** | **String** | The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. | [optional] 
**tags** | [**[Tag]**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. | [optional] 
**copyTagsToDataRepositoryAssociations** | **Boolean** |  | [optional] 
**lustreConfiguration** | [**FileCacheCreatingLustreConfiguration**](FileCacheCreatingLustreConfiguration.md) |  | [optional] 
**dataRepositoryAssociationIds** | **Array** |  | [optional] 


