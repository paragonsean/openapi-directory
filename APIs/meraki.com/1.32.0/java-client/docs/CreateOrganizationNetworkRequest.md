

# CreateOrganizationNetworkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyFromNetworkId** | **String** | The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network&#39;s type exactly. |  [optional] |
|**name** | **String** | The name of the new network |  |
|**notes** | **String** | Add any notes or additional information about this network here. |  [optional] |
|**productTypes** | [**List&lt;ProductTypesEnum&gt;**](#List&lt;ProductTypesEnum&gt;) | The product type(s) of the new network. If more than one type is included, the network will be a combined network. |  |
|**tags** | **List&lt;String&gt;** | A list of tags to be applied to the network |  [optional] |
|**timeZone** | **String** | The timezone of the network. For a list of allowed timezones, please see the &#39;TZ&#39; column in the table in &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones&#39;&gt;this article.&lt;/a&gt; |  [optional] |



## Enum: List&lt;ProductTypesEnum&gt;

| Name | Value |
|---- | -----|
| APPLIANCE | &quot;appliance&quot; |
| CAMERA | &quot;camera&quot; |
| CELLULAR_GATEWAY | &quot;cellularGateway&quot; |
| SENSOR | &quot;sensor&quot; |
| SWITCH | &quot;switch&quot; |
| SYSTEMS_MANAGER | &quot;systemsManager&quot; |
| WIRELESS | &quot;wireless&quot; |



