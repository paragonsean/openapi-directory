

# AptSettings

Apt patching is completed by executing `apt-get update && apt-get upgrade`. Additional options can be set to control how this is executed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludes** | **List&lt;String&gt;** | List of packages to exclude from update. These packages will be excluded |  [optional] |
|**exclusivePackages** | **List&lt;String&gt;** | An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | By changing the type to DIST, the patching is performed using &#x60;apt-get dist-upgrade&#x60; instead. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| DIST | &quot;DIST&quot; |
| UPGRADE | &quot;UPGRADE&quot; |



