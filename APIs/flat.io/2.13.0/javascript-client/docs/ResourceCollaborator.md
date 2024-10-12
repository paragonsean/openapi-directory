# FlatApi.ResourceCollaborator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aclAdmin** | **Boolean** | &#x60;True&#x60; if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] [default to false]
**aclRead** | **Boolean** | &#x60;True&#x60; if the current user can read the current document  | [optional] [default to false]
**aclWrite** | **Boolean** | &#x60;True&#x60; if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] [default to false]
**isCollaborator** | **Boolean** | &#x60;True&#x60; if the current user is a collaborator of the current document (direct or via group).  | [optional] [default to false]
**collection** | **String** | If this object is a permission of a collection, this property will contain the unique identifier of the collection | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**id** | **String** | The unique identifier of the permission | [optional] 
**invited** | **Boolean** | If this property is &#x60;true&#x60;, this is still a pending invitation  | [optional] 
**score** | **String** | If this object is a permission of a score, this property will contain the unique identifier of the score | [optional] 
**user** | [**UserPublic**](UserPublic.md) |  | [optional] 
**userEmail** | **String** | If the collaborator is not a user of Flat yet, this field will contain his email.  | [optional] 


