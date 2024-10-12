

# ZypperSettings

Zypper patching is performed by running `zypper patch`. See also https://en.opensuse.org/SDB:Zypper_manual.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | **List&lt;String&gt;** | Install only patches with these categories. Common categories include security, recommended, and feature. |  [optional] |
|**excludes** | **List&lt;String&gt;** | List of patches to exclude from update. |  [optional] |
|**exclusivePatches** | **List&lt;String&gt;** | An exclusive list of patches to be updated. These are the only patches that will be installed using &#39;zypper patch patch:&#39; command. This field must not be used with any other patch configuration fields. |  [optional] |
|**severities** | **List&lt;String&gt;** | Install only patches with these severities. Common severities include critical, important, moderate, and low. |  [optional] |
|**withOptional** | **Boolean** | Adds the &#x60;--with-optional&#x60; flag to &#x60;zypper patch&#x60;. |  [optional] |
|**withUpdate** | **Boolean** | Adds the &#x60;--with-update&#x60; flag, to &#x60;zypper patch&#x60;. |  [optional] |



