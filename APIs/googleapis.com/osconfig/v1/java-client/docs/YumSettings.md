

# YumSettings

Yum patching is performed by executing `yum update`. Additional options can be set to control how this is executed. Note that not all settings are supported on all platforms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludes** | **List&lt;String&gt;** | List of packages to exclude from update. These packages are excluded by using the yum &#x60;--exclude&#x60; flag. |  [optional] |
|**exclusivePackages** | **List&lt;String&gt;** | An exclusive list of packages to be updated. These are the only packages that will be updated. If these packages are not installed, they will be ignored. This field must not be specified with any other patch configuration fields. |  [optional] |
|**minimal** | **Boolean** | Will cause patch to run &#x60;yum update-minimal&#x60; instead. |  [optional] |
|**security** | **Boolean** | Adds the &#x60;--security&#x60; flag to &#x60;yum update&#x60;. Not supported on all platforms. |  [optional] |



