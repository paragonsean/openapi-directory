# AwsIoTGreengrassV2.CreateComponentVersionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inlineRecipe** | **String** | &lt;p&gt;The recipe to use to create the component. The recipe defines the component&#39;s metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility.&lt;/p&gt; &lt;p&gt;You must specify either &lt;code&gt;inlineRecipe&lt;/code&gt; or &lt;code&gt;lambdaFunction&lt;/code&gt;.&lt;/p&gt; | [optional] 
**lambdaFunction** | [**CreateComponentVersionRequestLambdaFunction**](CreateComponentVersionRequestLambdaFunction.md) |  | [optional] 
**tags** | **{String: String}** | A list of key-value pairs that contain metadata for the resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html\&quot;&gt;Tag your resources&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;. | [optional] 
**clientToken** | **String** | A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours. | [optional] 


