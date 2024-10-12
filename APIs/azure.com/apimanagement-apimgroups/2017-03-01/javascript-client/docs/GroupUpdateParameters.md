# ApiManagementClient.GroupUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Group description. | [optional] 
**externalId** | **String** | Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group object id&gt;; otherwise the value is null. | [optional] 
**name** | **String** | Group name. | [optional] 
**type** | **String** | Group type. | [optional] 



## Enum: TypeEnum


* `custom` (value: `"custom"`)

* `system` (value: `"system"`)

* `external` (value: `"external"`)




