

# BuildVersion

BuildVersion combines SemVer version of extension with free-form build information (i.e. 'alpha', 'private-build') as a set of strings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | **Map&lt;String, Object&gt;** | Free-form build information. Envoy defines several well known keys in the source/common/version/version.h file |  [optional] |
|**version** | [**SemanticVersion**](SemanticVersion.md) |  |  [optional] |



