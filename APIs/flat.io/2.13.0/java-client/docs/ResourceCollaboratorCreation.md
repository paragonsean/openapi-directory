

# ResourceCollaboratorCreation

Add a collaborator to a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aclAdmin** | **Boolean** | &#x60;True&#x60; if the related user can can manage the current document, i.e. changing the document permissions and deleting the document  |  [optional] |
|**aclRead** | **Boolean** | &#x60;True&#x60; if the related user can read the score. (probably true if the user has a permission on the document).  |  [optional] |
|**aclWrite** | **Boolean** | &#x60;True&#x60; if the related user can modify the score.  |  [optional] |
|**group** | **String** | The unique identifier of a Flat group |  [optional] |
|**user** | **String** | The unique identifier of a Flat user |  [optional] |
|**userEmail** | **String** | Fill this field to invite an individual user by email.  |  [optional] |
|**userToken** | **String** | Token received in an invitation to join the score.  |  [optional] |



