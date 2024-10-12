

# WindowsUpdateSettings

Windows patching is performed using the Windows Update Agent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classifications** | [**List&lt;ClassificationsEnum&gt;**](#List&lt;ClassificationsEnum&gt;) | Only apply updates of these windows update classifications. If empty, all updates are applied. |  [optional] |
|**excludes** | **List&lt;String&gt;** | List of KBs to exclude from update. |  [optional] |
|**exclusivePatches** | **List&lt;String&gt;** | An exclusive list of kbs to be updated. These are the only patches that will be updated. This field must not be used with other patch configurations. |  [optional] |



## Enum: List&lt;ClassificationsEnum&gt;

| Name | Value |
|---- | -----|
| CLASSIFICATION_UNSPECIFIED | &quot;CLASSIFICATION_UNSPECIFIED&quot; |
| CRITICAL | &quot;CRITICAL&quot; |
| SECURITY | &quot;SECURITY&quot; |
| DEFINITION | &quot;DEFINITION&quot; |
| DRIVER | &quot;DRIVER&quot; |
| FEATURE_PACK | &quot;FEATURE_PACK&quot; |
| SERVICE_PACK | &quot;SERVICE_PACK&quot; |
| TOOL | &quot;TOOL&quot; |
| UPDATE_ROLLUP | &quot;UPDATE_ROLLUP&quot; |
| UPDATE | &quot;UPDATE&quot; |



