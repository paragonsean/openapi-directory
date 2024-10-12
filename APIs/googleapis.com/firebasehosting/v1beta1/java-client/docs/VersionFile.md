

# VersionFile

A static content file that is part of a version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hash** | **String** | The SHA256 content hash of the file. |  [optional] |
|**path** | **String** | The URI at which the file&#39;s content should display. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The current status of a particular file in the specified version. The value will be either &#x60;pending upload&#x60; or &#x60;uploaded&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| EXPECTED | &quot;EXPECTED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



