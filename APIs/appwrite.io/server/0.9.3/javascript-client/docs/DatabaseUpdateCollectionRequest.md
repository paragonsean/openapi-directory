# Appwrite.DatabaseUpdateCollectionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Collection name. Max length: 128 chars. | 
**read** | **[String]** | An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | [optional] 
**rules** | **[String]** | Array of [rule objects](/docs/rules). Each rule define a collection field name, data type and validation. | [optional] 
**write** | **[String]** | An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | [optional] 


