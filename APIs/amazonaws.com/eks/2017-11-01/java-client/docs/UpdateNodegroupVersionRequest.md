

# UpdateNodegroupVersionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**version** | **String** | The Kubernetes version to update to. If no version is specified, then the Kubernetes version of the node group does not change. You can specify the Kubernetes version of the cluster to update the node group to the latest AMI version of the cluster&#39;s Kubernetes version. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, and your launch template uses a custom AMI, then don&#39;t specify &lt;code&gt;version&lt;/code&gt;, or the node group update will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. |  [optional] |
|**releaseVersion** | **String** | &lt;p&gt;The AMI version of the Amazon EKS optimized AMI to use for the update. By default, the latest available AMI version for the node group&#39;s Kubernetes version is used. For information about Linux versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html\&quot;&gt;Amazon EKS optimized Amazon Linux AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html\&quot;&gt;Amazon EKS optimized Windows AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, and your launch template uses a custom AMI, then don&#39;t specify &lt;code&gt;releaseVersion&lt;/code&gt;, or the node group update will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; |  [optional] |
|**launchTemplate** | [**CreateNodegroupRequestLaunchTemplate**](CreateNodegroupRequestLaunchTemplate.md) |  |  [optional] |
|**force** | **Boolean** | Force the update if the existing node group&#39;s pods are unable to be drained due to a pod disruption budget issue. If an update fails because pods could not be drained, you can force the update after it fails to terminate the old node whether or not any pods are running on the node. |  [optional] |
|**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  [optional] |



