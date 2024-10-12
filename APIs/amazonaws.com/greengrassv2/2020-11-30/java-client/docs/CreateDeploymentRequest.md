

# CreateDeploymentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetArn** | **String** | The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the target IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group. |  |
|**deploymentName** | **String** | The name of the deployment. |  [optional] |
|**components** | [**Map&lt;String, ComponentDeploymentSpecification&gt;**](ComponentDeploymentSpecification.md) | The components to deploy. This is a dictionary, where each key is the name of a component, and each key&#39;s value is the version and configuration to deploy for that component. |  [optional] |
|**iotJobConfiguration** | [**CreateDeploymentRequestIotJobConfiguration**](CreateDeploymentRequestIotJobConfiguration.md) |  |  [optional] |
|**deploymentPolicies** | [**CreateDeploymentRequestDeploymentPolicies**](CreateDeploymentRequestDeploymentPolicies.md) |  |  [optional] |
|**parentTargetArn** | **String** | The parent deployment&#39;s target &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; within a subdeployment. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of key-value pairs that contain metadata for the resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html\&quot;&gt;Tag your resources&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;. |  [optional] |
|**clientToken** | **String** | A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours. |  [optional] |



