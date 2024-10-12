

# Domain

A registered domain resource in the Postmaster API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Timestamp when the user registered this domain. Assigned by the server. |  [optional] |
|**name** | **String** | The resource name of the Domain. Domain names have the form &#x60;domains/{domain_name}&#x60;, where domain_name is the fully qualified domain name (i.e., mymail.mydomain.com). |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | User’s permission for this domain. Assigned by the server. |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| PERMISSION_UNSPECIFIED | &quot;PERMISSION_UNSPECIFIED&quot; |
| OWNER | &quot;OWNER&quot; |
| READER | &quot;READER&quot; |
| NONE | &quot;NONE&quot; |



