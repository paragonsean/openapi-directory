# SalesLoftPlatform.EmailsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ActivitiesEmailsIdJsonGet**](EmailsApi.md#v2ActivitiesEmailsIdJsonGet) | **GET** /v2/activities/emails/{id}.json | Fetch an email
[**v2ActivitiesEmailsJsonGet**](EmailsApi.md#v2ActivitiesEmailsJsonGet) | **GET** /v2/activities/emails.json | List emails



## v2ActivitiesEmailsIdJsonGet

> Email v2ActivitiesEmailsIdJsonGet(id)

Fetch an email

Fetches an email, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.EmailsApi();
let id = "id_example"; // String | Email ID
apiInstance.v2ActivitiesEmailsIdJsonGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Email ID | 

### Return type

[**Email**](Email.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2ActivitiesEmailsJsonGet

> [Email] v2ActivitiesEmailsJsonGet(opts)

List emails

Fetches multiple email records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.EmailsApi();
let opts = {
  'ids': [null], // [Number] | IDs of emails to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'updatedAt': ["null"], // [String] | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'bounced': true, // Boolean | Filters emails by whether they have bounced or not
  'crmActivityId': [null], // [Number] | Filters emails by crm_activity_id. Multiple crm activty ids can be applied
  'actionId': [null], // [Number] | Filters emails by action_id. Multiple action ids can be applied
  'userId': [null], // [Number] | Filters emails by user_id. Multiple User ids can be applied
  'status': ["null"], // [String] | Filters emails by status. Multiple status can be applied, possible values are sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external
  'cadenceId': [null], // [Number] | Filters emails by cadence. Multiple cadence ids can be applied
  'stepId': [null], // [Number] | Filters emails by step. Multiple step ids can be applied
  'oneOff': true, // Boolean | Filters emails by one-off only
  'scopedFields': ["null"], // [String] | Specify explicit scoped fields desired on the Email Resource.
  'personId': [null], // [Number] | Filters emails by person_id. Multiple person ids can be applied
  'emailAddresses': ["null"], // [String] | Filters emails by recipient email address. Multiple emails can be applied.
  'personalization': ["null"], // [String] | Filters emails by personalization score
  'sentAt': ["null"], // [String] | Equality filters that are applied to the sent_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: updated_at, send_time. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2ActivitiesEmailsJsonGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[Number]**](Number.md)| IDs of emails to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **updatedAt** | [**[String]**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **bounced** | **Boolean**| Filters emails by whether they have bounced or not | [optional] 
 **crmActivityId** | [**[Number]**](Number.md)| Filters emails by crm_activity_id. Multiple crm activty ids can be applied | [optional] 
 **actionId** | [**[Number]**](Number.md)| Filters emails by action_id. Multiple action ids can be applied | [optional] 
 **userId** | [**[Number]**](Number.md)| Filters emails by user_id. Multiple User ids can be applied | [optional] 
 **status** | [**[String]**](String.md)| Filters emails by status. Multiple status can be applied, possible values are sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external | [optional] 
 **cadenceId** | [**[Number]**](Number.md)| Filters emails by cadence. Multiple cadence ids can be applied | [optional] 
 **stepId** | [**[Number]**](Number.md)| Filters emails by step. Multiple step ids can be applied | [optional] 
 **oneOff** | **Boolean**| Filters emails by one-off only | [optional] 
 **scopedFields** | [**[String]**](String.md)| Specify explicit scoped fields desired on the Email Resource. | [optional] 
 **personId** | [**[Number]**](Number.md)| Filters emails by person_id. Multiple person ids can be applied | [optional] 
 **emailAddresses** | [**[String]**](String.md)| Filters emails by recipient email address. Multiple emails can be applied. | [optional] 
 **personalization** | [**[String]**](String.md)| Filters emails by personalization score | [optional] 
 **sentAt** | [**[String]**](String.md)| Equality filters that are applied to the sent_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: updated_at, send_time. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Email]**](Email.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

