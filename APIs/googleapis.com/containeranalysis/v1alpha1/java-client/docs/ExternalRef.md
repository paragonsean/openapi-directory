

# ExternalRef

An External Reference allows a Package to reference an external source of additional information, metadata, enumerations, asset identifiers, or downloadable content believed to be relevant to the Package

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | An External Reference allows a Package to reference an external source of additional information, metadata, enumerations, asset identifiers, or downloadable content believed to be relevant to the Package |  [optional] |
|**comment** | **String** | Human-readable information about the purpose and target of the reference |  [optional] |
|**locator** | **String** | The unique string with no spaces necessary to access the package-specific information, metadata, or content within the target location |  [optional] |
|**type** | **String** | Type of category (e.g. &#39;npm&#39; for the PACKAGE_MANAGER category) |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CATEGORY_UNSPECIFIED | &quot;CATEGORY_UNSPECIFIED&quot; |
| SECURITY | &quot;SECURITY&quot; |
| PACKAGE_MANAGER | &quot;PACKAGE_MANAGER&quot; |
| PERSISTENT_ID | &quot;PERSISTENT_ID&quot; |
| OTHER | &quot;OTHER&quot; |



