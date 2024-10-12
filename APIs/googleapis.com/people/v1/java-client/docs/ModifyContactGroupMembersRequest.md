

# ModifyContactGroupMembersRequest

A request to modify an existing contact group's members. Contacts can be removed from any group but they can only be added to a user group or \"myContacts\" or \"starred\" system groups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceNamesToAdd** | **List&lt;String&gt;** | Optional. The resource names of the contact people to add in the form of &#x60;people/{person_id}&#x60;. The total number of resource names in &#x60;resource_names_to_add&#x60; and &#x60;resource_names_to_remove&#x60; must be less than or equal to 1000. |  [optional] |
|**resourceNamesToRemove** | **List&lt;String&gt;** | Optional. The resource names of the contact people to remove in the form of &#x60;people/{person_id}&#x60;. The total number of resource names in &#x60;resource_names_to_add&#x60; and &#x60;resource_names_to_remove&#x60; must be less than or equal to 1000. |  [optional] |



