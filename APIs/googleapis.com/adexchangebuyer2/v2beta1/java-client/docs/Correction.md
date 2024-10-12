

# Correction

Output only. Shows any corrections that were applied to this creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contexts** | [**List&lt;ServingContext&gt;**](ServingContext.md) | The contexts for the correction. |  [optional] |
|**details** | **List&lt;String&gt;** | Additional details about what was corrected. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of correction that was applied to the creative. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CORRECTION_TYPE_UNSPECIFIED | &quot;CORRECTION_TYPE_UNSPECIFIED&quot; |
| VENDOR_IDS_ADDED | &quot;VENDOR_IDS_ADDED&quot; |
| SSL_ATTRIBUTE_REMOVED | &quot;SSL_ATTRIBUTE_REMOVED&quot; |
| FLASH_FREE_ATTRIBUTE_REMOVED | &quot;FLASH_FREE_ATTRIBUTE_REMOVED&quot; |
| FLASH_FREE_ATTRIBUTE_ADDED | &quot;FLASH_FREE_ATTRIBUTE_ADDED&quot; |
| REQUIRED_ATTRIBUTE_ADDED | &quot;REQUIRED_ATTRIBUTE_ADDED&quot; |
| REQUIRED_VENDOR_ADDED | &quot;REQUIRED_VENDOR_ADDED&quot; |
| SSL_ATTRIBUTE_ADDED | &quot;SSL_ATTRIBUTE_ADDED&quot; |
| IN_BANNER_VIDEO_ATTRIBUTE_ADDED | &quot;IN_BANNER_VIDEO_ATTRIBUTE_ADDED&quot; |
| MRAID_ATTRIBUTE_ADDED | &quot;MRAID_ATTRIBUTE_ADDED&quot; |
| FLASH_ATTRIBUTE_REMOVED | &quot;FLASH_ATTRIBUTE_REMOVED&quot; |
| VIDEO_IN_SNIPPET_ATTRIBUTE_ADDED | &quot;VIDEO_IN_SNIPPET_ATTRIBUTE_ADDED&quot; |



