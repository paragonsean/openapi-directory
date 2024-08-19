# StreamAnalyticsManagementClient.BlobDataSourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **String** | The name of a container within the associated Storage account. This container contains either the blob(s) to be read from or written to. Required on PUT (CreateOrReplace) requests. | [optional] 
**dateFormat** | **String** | The date format. Wherever {date} appears in pathPattern, the value of this property is used as the date format instead. | [optional] 
**pathPattern** | **String** | The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job. See https://docs.microsoft.com/en-us/rest/api/streamanalytics/stream-analytics-input or https://docs.microsoft.com/en-us/rest/api/streamanalytics/stream-analytics-output for a more detailed explanation and example. | [optional] 
**storageAccounts** | [**[StorageAccount]**](StorageAccount.md) | A list of one or more Azure Storage accounts. Required on PUT (CreateOrReplace) requests. | [optional] 
**timeFormat** | **String** | The time format. Wherever {time} appears in pathPattern, the value of this property is used as the time format instead. | [optional] 


