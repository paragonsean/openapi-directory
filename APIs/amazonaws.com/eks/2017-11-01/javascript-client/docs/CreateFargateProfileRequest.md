# AmazonElasticKubernetesService.CreateFargateProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fargateProfileName** | **String** | The name of the Fargate profile. | 
**podExecutionRoleArn** | **String** | The Amazon Resource Name (ARN) of the pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html\&quot;&gt;Pod Execution Role&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. | 
**subnets** | **[String]** | The IDs of subnets to launch your pods into. At this time, pods running on Fargate are not assigned public IP addresses, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter. | [optional] 
**selectors** | [**[FargateProfileSelector]**](FargateProfileSelector.md) | The selectors to match for pods to use this Fargate profile. Each selector must have an associated namespace. Optionally, you can also specify labels for a namespace. You may specify up to five selectors in a Fargate profile. | [optional] 
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**tags** | **{String: String}** | The metadata to apply to the Fargate profile to assist with categorization and organization. Each tag consists of a key and an optional value. You define both. Fargate profile tags do not propagate to any other resources associated with the Fargate profile, such as the pods that are scheduled with it. | [optional] 


