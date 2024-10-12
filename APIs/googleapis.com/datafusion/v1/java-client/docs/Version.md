

# Version

The Data Fusion version. This proto message stores information about certain Data Fusion version, which is used for Data Fusion version upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableFeatures** | **List&lt;String&gt;** | Represents a list of available feature names for a given version. |  [optional] |
|**defaultVersion** | **Boolean** | Whether this is currently the default version for Cloud Data Fusion |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type represents the release availability of the version |  [optional] |
|**versionNumber** | **String** | The version number of the Data Fusion instance, such as &#39;6.0.1.0&#39;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PREVIEW | &quot;TYPE_PREVIEW&quot; |
| GENERAL_AVAILABILITY | &quot;TYPE_GENERAL_AVAILABILITY&quot; |



