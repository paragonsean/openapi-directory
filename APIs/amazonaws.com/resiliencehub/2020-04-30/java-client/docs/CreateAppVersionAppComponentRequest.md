

# CreateAppVersionAppComponentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfo** | **Map&lt;String, List&lt;String&gt;&gt;** | Currently, there is no supported additional information for Application Components. |  [optional] |
|**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  |
|**clientToken** | **String** | Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests. |  [optional] |
|**id** | **String** | Identifier of the Application Component. |  [optional] |
|**name** | **String** | Name of the Application Component. |  |
|**type** | **String** | Type of Application Component. For more information about the types of Application Component, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html\&quot;&gt;Grouping resources in an AppComponent&lt;/a&gt;. |  |



