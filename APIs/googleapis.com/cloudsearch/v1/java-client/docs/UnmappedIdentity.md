

# UnmappedIdentity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalIdentity** | [**Principal**](Principal.md) |  |  [optional] |
|**resolutionStatusCode** | [**ResolutionStatusCodeEnum**](#ResolutionStatusCodeEnum) | The resolution status for the external identity. |  [optional] |



## Enum: ResolutionStatusCodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| IDENTITY_SOURCE_NOT_FOUND | &quot;IDENTITY_SOURCE_NOT_FOUND&quot; |
| IDENTITY_SOURCE_MISCONFIGURED | &quot;IDENTITY_SOURCE_MISCONFIGURED&quot; |
| TOO_MANY_MAPPINGS_FOUND | &quot;TOO_MANY_MAPPINGS_FOUND&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |



