# OsConfigApi.AptSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludes** | **[String]** | List of packages to exclude from update. These packages will be excluded | [optional] 
**exclusivePackages** | **[String]** | An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field cannot be specified with any other patch configuration fields. | [optional] 
**type** | **String** | By changing the type to DIST, the patching is performed using &#x60;apt-get dist-upgrade&#x60; instead. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `DIST` (value: `"DIST"`)

* `UPGRADE` (value: `"UPGRADE"`)




