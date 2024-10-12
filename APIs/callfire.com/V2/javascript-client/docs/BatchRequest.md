# CallFireApiDocumentation.BatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactListId** | **Number** | An id of existing contact list | [optional] 
**name** | **String** | A name of batch | [optional] 
**recipients** | [**[Recipient]**](Recipient.md) | A list of Recipient objects. For each recipient you can set its phone number or existing contact id to use contact which already exists in account | [optional] 
**scrubDuplicates** | **Boolean** | Removes duplicate recipients from batch if true | [optional] 


