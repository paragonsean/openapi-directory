

# ApiVersionSetUpdateRequestProperties

Properties used to create or update an API Version Set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Name of API Version Set |  [optional] |
|**versioningScheme** | [**VersioningSchemeEnum**](#VersioningSchemeEnum) | An value that determines where the API Version identifer will be located in a HTTP request. |  [optional] |



## Enum: VersioningSchemeEnum

| Name | Value |
|---- | -----|
| SEGMENT | &quot;Segment&quot; |
| QUERY | &quot;Query&quot; |
| HEADER | &quot;Header&quot; |



