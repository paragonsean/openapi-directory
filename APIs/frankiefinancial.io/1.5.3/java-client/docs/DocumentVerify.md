

# DocumentVerify

This is the document we wish to verify in some way, along with an entity object that contains some/all of the details we wish to verify.  For example, if we're attempting to verify a drivers licence, we generally need to pass in a name, address, DoB, etc as well. the entity gives the structure to be able to do this.   Note, only the document in the \"document\" parameter is to be processed. any additional documents found in the entity (there shouldn't be, but given the way this has been defined, there can be) will be ignored. Only the Name, Address, DoB and Gender fields will be potentially used during the verification process.  The EntityObject can take one of two forms.    - It can be a single entityId - in which case the details will be pulled from the database. If using an existing document, then the entity must also own the document or the request will fail.   - You can supply a \"single use\" entity with fields, etc. In this case the entity details will be used to verify the document, then will be discarded.    If you wish to save the entity, use the /entity comments instead to create the entity and attach the document there. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | [**IdentityDocumentObject**](IdentityDocumentObject.md) |  |  [optional] |
|**entityData** | [**EntityObject**](EntityObject.md) |  |  [optional] |



