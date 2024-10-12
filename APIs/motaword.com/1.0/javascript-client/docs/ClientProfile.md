# MotaWordApi.ClientProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCreationDate** | **Date** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z | [optional] 
**clientProjectCount** | **Number** | total project count that this client sent | [optional] 
**corporate** | **String** | corporate name | [optional] 
**corporateId** | **Number** | corporate id | [optional] 
**corporateUserCount** | **Number** | total user count in a corporation | [optional] 
**frequentFileExtension** | **String** | the file extension for the files that usually this client sent | [optional] 
**frequentLanguagePairs** | **[String]** | frequent language pairs | [optional] 
**fullName** | **String** | full name of the client | [optional] 
**growth** | **Boolean** | The answer for the question \&quot;Is there any growth for this corporate&#39;s spending\&quot;. The values can be true, false or null if the corporate is oour client for less than 6 months | [optional] 
**isComplex** | **Boolean** | the answer for the question \&quot;Is this client usually sent complex projects?\&quot; | [optional] 
**last12MonthsSpending** | **Number** | corporate&#39;s spending in twelve months | [optional] 
**lastProject** | **Number** | the quote number for the last project of this client | [optional] 
**lastProjectTime** | **Date** | the creation date of the last project that is sent by this client | [optional] 
**lastProofreaders** | [**[ProofreaderWithLanguage]**](ProofreaderWithLanguage.md) | list of prooofreaders for the target languages of last project | [optional] 
**notes** | **[String]** | notes that is submited for this client and/or with her projects | [optional] 
**nps** | [**ClientProfileNps**](ClientProfileNps.md) |  | [optional] 
**userRankInProjectCount** | **Number** | rank of the user in all corporate users for project count. If the user is the most active user foor sending projects her rank is 1 | [optional] 
**userRankInSpending** | **Number** | rank of the user in all corporate users for total spending. If the user is the most active user for spending her rank is 1 | [optional] 


