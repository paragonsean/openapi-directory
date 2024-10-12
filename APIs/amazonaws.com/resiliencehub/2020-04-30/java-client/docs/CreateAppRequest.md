

# CreateAppRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assessmentSchedule** | [**AssessmentScheduleEnum**](#AssessmentScheduleEnum) |  Assessment execution schedule with &#39;Daily&#39; or &#39;Disabled&#39; values.  |  [optional] |
|**clientToken** | **String** | Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests. |  [optional] |
|**description** | **String** | The optional description for an app. |  [optional] |
|**eventSubscriptions** | [**List&lt;EventSubscription&gt;**](EventSubscription.md) | The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports only &lt;b&gt;Drift detected&lt;/b&gt; and &lt;b&gt;Scheduled assessment failure&lt;/b&gt; events notification. |  [optional] |
|**name** | **String** | Name of the application. |  |
|**permissionModel** | [**CreateAppRequestPermissionModel**](CreateAppRequestPermissionModel.md) |  |  [optional] |
|**policyArn** | **String** | Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:resiliency-policy/&lt;code&gt;policy-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair. |  [optional] |



## Enum: AssessmentScheduleEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| DAILY | &quot;Daily&quot; |



