

# Version

Version contains structured information about the version of the package. For a discussion of this in Debian/Ubuntu: http://serverfault.com/questions/604541/debian-packages-version-convention For a discussion of this in Redhat/Fedora/Centos: http://blog.jasonantman.com/2014/07/how-yum-and-rpm-compare-versions/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**epoch** | **Integer** | Used to correct mistakes in the version numbering scheme. |  [optional] |
|**inclusive** | **Boolean** | Whether this version is vulnerable, when defining the version bounds. For example, if the minimum version is 2.0, inclusive&#x3D;true would say 2.0 is vulnerable, while inclusive&#x3D;false would say it&#39;s not |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Distinguish between sentinel MIN/MAX versions and normal versions. If kind is not NORMAL, then the other fields are ignored. |  [optional] |
|**name** | **String** | The main part of the version name. |  [optional] |
|**revision** | **String** | The iteration of the package build from the above version. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;NORMAL&quot; |
| MINIMUM | &quot;MINIMUM&quot; |
| MAXIMUM | &quot;MAXIMUM&quot; |



