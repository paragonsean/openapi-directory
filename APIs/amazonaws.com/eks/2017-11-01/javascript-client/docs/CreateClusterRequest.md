# AmazonElasticKubernetesService.CreateClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The unique name to give to your cluster. | 
**version** | **String** | &lt;p&gt;The desired Kubernetes version for your cluster. If you don&#39;t specify a value here, the default version available in Amazon EKS is used.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The default version might not be the latest version available.&lt;/p&gt; &lt;/note&gt; | [optional] 
**roleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to Amazon Web Services API operations on your behalf. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html\&quot;&gt;Amazon EKS Service IAM Role&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon EKS User Guide&lt;/i&gt; &lt;/i&gt;. | 
**resourcesVpcConfig** | [**CreateClusterRequestResourcesVpcConfig**](CreateClusterRequestResourcesVpcConfig.md) |  | 
**kubernetesNetworkConfig** | [**CreateClusterRequestKubernetesNetworkConfig**](CreateClusterRequestKubernetesNetworkConfig.md) |  | [optional] 
**logging** | [**CreateClusterRequestLogging**](CreateClusterRequestLogging.md) |  | [optional] 
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**tags** | **{String: String}** | The metadata to apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value. You define both. | [optional] 
**encryptionConfig** | [**[EncryptionConfig]**](EncryptionConfig.md) | The encryption configuration for the cluster. | [optional] 
**outpostConfig** | [**CreateClusterRequestOutpostConfig**](CreateClusterRequestOutpostConfig.md) |  | [optional] 


