

# TestFunction20200531Request


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | [**StageEnum**](#StageEnum) | The stage of the function that you are testing, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. |  [optional] |
|**eventObject** | **String** | The event object to test the function with. For more information about the structure of the event object, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function\&quot;&gt;Testing functions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;. |  |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| DEVELOPMENT | &quot;DEVELOPMENT&quot; |
| LIVE | &quot;LIVE&quot; |



