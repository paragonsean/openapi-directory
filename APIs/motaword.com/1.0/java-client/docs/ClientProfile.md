

# ClientProfile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCreationDate** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**clientProjectCount** | **BigDecimal** | total project count that this client sent |  [optional] |
|**corporate** | **String** | corporate name |  [optional] |
|**corporateId** | **BigDecimal** | corporate id |  [optional] |
|**corporateUserCount** | **BigDecimal** | total user count in a corporation |  [optional] |
|**frequentFileExtension** | **String** | the file extension for the files that usually this client sent |  [optional] |
|**frequentLanguagePairs** | **List&lt;String&gt;** | frequent language pairs |  [optional] |
|**fullName** | **String** | full name of the client |  [optional] |
|**growth** | **Boolean** | The answer for the question \&quot;Is there any growth for this corporate&#39;s spending\&quot;. The values can be true, false or null if the corporate is oour client for less than 6 months |  [optional] |
|**isComplex** | **Boolean** | the answer for the question \&quot;Is this client usually sent complex projects?\&quot; |  [optional] |
|**last12MonthsSpending** | **Float** | corporate&#39;s spending in twelve months |  [optional] |
|**lastProject** | **BigDecimal** | the quote number for the last project of this client |  [optional] |
|**lastProjectTime** | **OffsetDateTime** | the creation date of the last project that is sent by this client |  [optional] |
|**lastProofreaders** | [**List&lt;ProofreaderWithLanguage&gt;**](ProofreaderWithLanguage.md) | list of prooofreaders for the target languages of last project |  [optional] |
|**notes** | **List&lt;String&gt;** | notes that is submited for this client and/or with her projects |  [optional] |
|**nps** | [**ClientProfileNps**](ClientProfileNps.md) |  |  [optional] |
|**userRankInProjectCount** | **BigDecimal** | rank of the user in all corporate users for project count. If the user is the most active user foor sending projects her rank is 1 |  [optional] |
|**userRankInSpending** | **BigDecimal** | rank of the user in all corporate users for total spending. If the user is the most active user for spending her rank is 1 |  [optional] |



