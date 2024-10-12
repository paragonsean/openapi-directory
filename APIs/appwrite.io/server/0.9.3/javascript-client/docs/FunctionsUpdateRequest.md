# Appwrite.FunctionsUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **[String]** | Events list. | [optional] 
**execute** | **[String]** | An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | 
**name** | **String** | Function name. Max length: 128 chars. | 
**schedule** | **String** | Schedule CRON syntax. | [optional] 
**timeout** | **Number** | Function maximum execution time in seconds. | [optional] 
**vars** | **Object** | Key-value JSON object. | [optional] 


