

# StartAppRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A &lt;code&gt;ClientToken&lt;/code&gt; is also known as an &lt;i&gt;idempotency token&lt;/i&gt;. A &lt;code&gt;ClientToken&lt;/code&gt; expires after 24 hours. |  [optional] |
|**description** | **String** | The description of the app. |  [optional] |
|**domain** | **String** | The name of the domain of the app. |  |
|**launchOverrides** | [**StartAppRequestLaunchOverrides**](StartAppRequestLaunchOverrides.md) |  |  [optional] |
|**name** | **String** | The name of the app. |  |
|**simulation** | **String** | The name of the simulation of the app. |  |



