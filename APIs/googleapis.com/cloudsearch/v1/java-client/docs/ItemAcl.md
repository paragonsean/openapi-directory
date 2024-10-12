

# ItemAcl

Access control list information for the item. For more information see [Map ACLs](https://developers.google.com/cloud-search/docs/guides/acls).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aclInheritanceType** | [**AclInheritanceTypeEnum**](#AclInheritanceTypeEnum) | Sets the type of access rules to apply when an item inherits its ACL from a parent. This should always be set in tandem with the inheritAclFrom field. Also, when the inheritAclFrom field is set, this field should be set to a valid AclInheritanceType. |  [optional] |
|**deniedReaders** | [**List&lt;Principal&gt;**](Principal.md) | List of principals who are explicitly denied access to the item in search results. While principals are denied access by default, use denied readers to handle exceptions and override the list allowed readers. The maximum number of elements is 100. |  [optional] |
|**inheritAclFrom** | **String** | The name of the item to inherit the Access Permission List (ACL) from. Note: ACL inheritance *only* provides access permissions to child items and does not define structural relationships, nor does it provide convenient ways to delete large groups of items. Deleting an ACL parent from the index only alters the access permissions of child items that reference the parent in the inheritAclFrom field. The item is still in the index, but may not visible in search results. By contrast, deletion of a container item also deletes all items that reference the container via the containerName field. The maximum length for this field is 1536 characters. |  [optional] |
|**owners** | [**List&lt;Principal&gt;**](Principal.md) | Optional. List of owners for the item. This field has no bearing on document access permissions. It does, however, offer a slight ranking boosts items where the querying user is an owner. The maximum number of elements is 5. |  [optional] |
|**readers** | [**List&lt;Principal&gt;**](Principal.md) | List of principals who are allowed to see the item in search results. Optional if inheriting permissions from another item or if the item is not intended to be visible, such as virtual containers. The maximum number of elements is 1000. |  [optional] |



## Enum: AclInheritanceTypeEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;NOT_APPLICABLE&quot; |
| CHILD_OVERRIDE | &quot;CHILD_OVERRIDE&quot; |
| PARENT_OVERRIDE | &quot;PARENT_OVERRIDE&quot; |
| BOTH_PERMIT | &quot;BOTH_PERMIT&quot; |



