

# CreateNetworkGroupPolicyRequestContentFilteringBlockedUrlCategories

Settings for blocked URL categories

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | **List&lt;String&gt;** | A list of URL categories to block |  [optional] |
|**settings** | [**SettingsEnum**](#SettingsEnum) | How URL categories are applied. Can be &#39;network default&#39;, &#39;append&#39; or &#39;override&#39;. |  [optional] |



## Enum: SettingsEnum

| Name | Value |
|---- | -----|
| APPEND | &quot;append&quot; |
| NETWORK_DEFAULT | &quot;network default&quot; |
| OVERRIDE | &quot;override&quot; |



