

# BatchRequest

Request object is used for adding new batch to an existing broadcast

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactListId** | **Long** | An id of existing contact list |  [optional] |
|**name** | **String** | A name of batch |  [optional] |
|**recipients** | [**List&lt;Recipient&gt;**](Recipient.md) | A list of Recipient objects. For each recipient you can set its phone number or existing contact id to use contact which already exists in account |  [optional] |
|**scrubDuplicates** | **Boolean** | Removes duplicate recipients from batch if true |  [optional] |



