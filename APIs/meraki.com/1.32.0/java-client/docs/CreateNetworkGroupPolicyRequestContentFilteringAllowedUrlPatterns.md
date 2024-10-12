

# CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns

Settings for allowed URL patterns

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**patterns** | **List&lt;String&gt;** | A list of URL patterns that are allowed |  [optional] |
|**settings** | [**SettingsEnum**](#SettingsEnum) | How URL patterns are applied. Can be &#39;network default&#39;, &#39;append&#39; or &#39;override&#39;. |  [optional] |



## Enum: SettingsEnum

| Name | Value |
|---- | -----|
| APPEND | &quot;append&quot; |
| NETWORK_DEFAULT | &quot;network default&quot; |
| OVERRIDE | &quot;override&quot; |



