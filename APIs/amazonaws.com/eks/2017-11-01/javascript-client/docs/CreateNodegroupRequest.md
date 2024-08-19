# AmazonElasticKubernetesService.CreateNodegroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodegroupName** | **String** | The unique name to give your node group. | 
**scalingConfig** | [**CreateNodegroupRequestScalingConfig**](CreateNodegroupRequestScalingConfig.md) |  | [optional] 
**diskSize** | **Number** | The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB for Linux and Bottlerocket. The default disk size is 50 GiB for Windows. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, then don&#39;t specify &lt;code&gt;diskSize&lt;/code&gt;, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | [optional] 
**subnets** | **[String]** | The subnets to use for the Auto Scaling group that is created for your node group. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, then don&#39;t specify &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html\&quot;&gt; &lt;code&gt;SubnetId&lt;/code&gt; &lt;/a&gt; in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | 
**instanceTypes** | **[String]** | Specify the instance types for a node group. If you specify a GPU instance type, make sure to also specify an applicable GPU AMI type with the &lt;code&gt;amiType&lt;/code&gt; parameter. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, then you can specify zero or one instance type in your launch template &lt;i&gt;or&lt;/i&gt; you can specify 0-20 instance types for &lt;code&gt;instanceTypes&lt;/code&gt;. If however, you specify an instance type in your launch template &lt;i&gt;and&lt;/i&gt; specify any &lt;code&gt;instanceTypes&lt;/code&gt;, the node group deployment will fail. If you don&#39;t specify an instance type in a launch template or for &lt;code&gt;instanceTypes&lt;/code&gt;, then &lt;code&gt;t3.medium&lt;/code&gt; is used, by default. If you specify &lt;code&gt;Spot&lt;/code&gt; for &lt;code&gt;capacityType&lt;/code&gt;, then we recommend specifying multiple values for &lt;code&gt;instanceTypes&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html#managed-node-group-capacity-types\&quot;&gt;Managed node group capacity types&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | [optional] 
**amiType** | **String** | The AMI type for your node group. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, and your launch template uses a custom AMI, then don&#39;t specify &lt;code&gt;amiType&lt;/code&gt;, or the node group deployment will fail. If your launch template uses a Windows custom AMI, then add &lt;code&gt;eks:kube-proxy-windows&lt;/code&gt; to your Windows nodes &lt;code&gt;rolearn&lt;/code&gt; in the &lt;code&gt;aws-auth&lt;/code&gt; &lt;code&gt;ConfigMap&lt;/code&gt;. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | [optional] 
**remoteAccess** | [**CreateNodegroupRequestRemoteAccess**](CreateNodegroupRequestRemoteAccess.md) |  | [optional] 
**nodeRole** | **String** | The Amazon Resource Name (ARN) of the IAM role to associate with your node group. The Amazon EKS worker node &lt;code&gt;kubelet&lt;/code&gt; daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch nodes and register them into a cluster, you must create an IAM role for those nodes to use when they are launched. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html\&quot;&gt;Amazon EKS node IAM role&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon EKS User Guide&lt;/i&gt; &lt;/i&gt;. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, then don&#39;t specify &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html\&quot;&gt; &lt;code&gt;IamInstanceProfile&lt;/code&gt; &lt;/a&gt; in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | 
**labels** | **{String: String}** | The Kubernetes labels to be applied to the nodes in the node group when they are created. | [optional] 
**taints** | [**[Taint]**](Taint.md) | The Kubernetes taints to be applied to the nodes in the node group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html\&quot;&gt;Node taints on managed node groups&lt;/a&gt;. | [optional] 
**tags** | **{String: String}** | The metadata to apply to the node group to assist with categorization and organization. Each tag consists of a key and an optional value. You define both. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets. | [optional] 
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**launchTemplate** | [**CreateNodegroupRequestLaunchTemplate**](CreateNodegroupRequestLaunchTemplate.md) |  | [optional] 
**updateConfig** | [**CreateNodegroupRequestUpdateConfig**](CreateNodegroupRequestUpdateConfig.md) |  | [optional] 
**capacityType** | **String** | The capacity type for your node group. | [optional] 
**version** | **String** | The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the cluster is used, and this is the only accepted specified value. If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, and your launch template uses a custom AMI, then don&#39;t specify &lt;code&gt;version&lt;/code&gt;, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | [optional] 
**releaseVersion** | **String** | &lt;p&gt;The AMI version of the Amazon EKS optimized AMI to use with your node group. By default, the latest available AMI version for the node group&#39;s current Kubernetes version is used. For information about Linux versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html\&quot;&gt;Amazon EKS optimized Amazon Linux AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html\&quot;&gt;Amazon EKS optimized Windows AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;launchTemplate&lt;/code&gt;, and your launch template uses a custom AMI, then don&#39;t specify &lt;code&gt;releaseVersion&lt;/code&gt;, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] 



## Enum: AmiTypeEnum


* `AL2_x86_64` (value: `"AL2_x86_64"`)

* `AL2_x86_64_GPU` (value: `"AL2_x86_64_GPU"`)

* `AL2_ARM_64` (value: `"AL2_ARM_64"`)

* `CUSTOM` (value: `"CUSTOM"`)

* `BOTTLEROCKET_ARM_64` (value: `"BOTTLEROCKET_ARM_64"`)

* `BOTTLEROCKET_x86_64` (value: `"BOTTLEROCKET_x86_64"`)

* `BOTTLEROCKET_ARM_64_NVIDIA` (value: `"BOTTLEROCKET_ARM_64_NVIDIA"`)

* `BOTTLEROCKET_x86_64_NVIDIA` (value: `"BOTTLEROCKET_x86_64_NVIDIA"`)

* `WINDOWS_CORE_2019_x86_64` (value: `"WINDOWS_CORE_2019_x86_64"`)

* `WINDOWS_FULL_2019_x86_64` (value: `"WINDOWS_FULL_2019_x86_64"`)

* `WINDOWS_CORE_2022_x86_64` (value: `"WINDOWS_CORE_2022_x86_64"`)

* `WINDOWS_FULL_2022_x86_64` (value: `"WINDOWS_FULL_2022_x86_64"`)





## Enum: CapacityTypeEnum


* `ON_DEMAND` (value: `"ON_DEMAND"`)

* `SPOT` (value: `"SPOT"`)




