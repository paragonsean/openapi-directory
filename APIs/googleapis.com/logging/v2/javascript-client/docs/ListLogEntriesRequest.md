# CloudLoggingApi.ListLogEntriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | Optional. A filter that chooses which log entries to return. For more information, see Logging query language (https://cloud.google.com/logging/docs/view/logging-query-language).Only log entries that match the filter are returned. An empty filter matches all log entries in the resources listed in resource_names. Referencing a parent resource that is not listed in resource_names will cause the filter to return no results. The maximum length of a filter is 20,000 characters. | [optional] 
**orderBy** | **String** | Optional. How the results should be sorted. Presently, the only permitted values are \&quot;timestamp asc\&quot; (default) and \&quot;timestamp desc\&quot;. The first option returns entries in order of increasing values of LogEntry.timestamp (oldest first), and the second option returns entries in order of decreasing timestamps (newest first). Entries with equal timestamps are returned in order of their insert_id values. | [optional] 
**pageSize** | **Number** | Optional. The maximum number of results to return from this request. Default is 50. If the value is negative, the request is rejected.The presence of next_page_token in the response indicates that more results might be available. | [optional] 
**pageToken** | **String** | Optional. If present, then retrieve the next batch of results from the preceding call to this method. page_token must be the value of next_page_token from the previous response. The values of other method parameters should be identical to those in the previous call. | [optional] 
**projectIds** | **[String]** | Optional. Deprecated. Use resource_names instead. One or more project identifiers or project numbers from which to retrieve log entries. Example: \&quot;my-project-1A\&quot;. | [optional] 
**resourceNames** | **[String]** | Required. Names of one or more parent resources from which to retrieve log entries: projects/[PROJECT_ID] organizations/[ORGANIZATION_ID] billingAccounts/[BILLING_ACCOUNT_ID] folders/[FOLDER_ID]May alternatively be one or more views: projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID] organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID] billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID] folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]Projects listed in the project_ids field are added to this list. A maximum of 100 resources may be specified in a single request. | [optional] 


