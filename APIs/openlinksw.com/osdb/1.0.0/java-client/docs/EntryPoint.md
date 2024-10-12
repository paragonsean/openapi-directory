

# EntryPoint


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentTypes** | **List&lt;String&gt;** | The supported MIME type(s) for an EntryPoint response. |  |
|**description** | **String** | A short description of the action. Optional - may be null. |  |
|**encodingTypes** | **List&lt;String&gt;** | The supported MIME type(s) for an EntryPoint request. Null if not applicable. |  |
|**httpMethod** | [**HttpMethodEnum**](#HttpMethodEnum) | The HTTP method used by the EntryPoint. |  |
|**name** | **String** | A word or short phrase to be used as the action&#39;s display name. Optional - may be null. |  |
|**parameters** | [**List&lt;EntryPointParameter&gt;**](EntryPointParameter.md) | Descriptions of the EntryPoint parameters. Null if not applicable. |  |
|**url** | **URI** | The EntryPoint URL. It will be non-null if url_template is null. |  |
|**urlTemplate** | **String** | The EntryPoint&#39;s URL template. Only required if the entry point URL is parameterized. Property &#39;url&#39; will be null if url_template is non-null. |  |



## Enum: HttpMethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| PUT | &quot;PUT&quot; |
| POST | &quot;POST&quot; |
| DELETE | &quot;DELETE&quot; |



