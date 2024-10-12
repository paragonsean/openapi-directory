# CallDataRecordsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CallDataRecordsIdJsonGet**](CallDataRecordsApi.md#v2CallDataRecordsIdJsonGet) | **GET** /v2/call_data_records/{id}.json | Fetch a call data record |
| [**v2CallDataRecordsJsonGet**](CallDataRecordsApi.md#v2CallDataRecordsJsonGet) | **GET** /v2/call_data_records.json | List call data records |


<a id="v2CallDataRecordsIdJsonGet"></a>
# **v2CallDataRecordsIdJsonGet**
> CallDataRecord v2CallDataRecordsIdJsonGet(id)

Fetch a call data record

Fetches a call data record, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallDataRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallDataRecordsApi apiInstance = new CallDataRecordsApi(defaultClient);
    String id = "id_example"; // String | CallDataRecord ID
    try {
      CallDataRecord result = apiInstance.v2CallDataRecordsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallDataRecordsApi#v2CallDataRecordsIdJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| CallDataRecord ID | |

### Return type

[**CallDataRecord**](CallDataRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CallDataRecordsJsonGet"></a>
# **v2CallDataRecordsJsonGet**
> List&lt;CallDataRecord&gt; v2CallDataRecordsJsonGet(ids, hasCall, createdAt, updatedAt, userGuid, personId, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List call data records

Fetches multiple call data records. The records can be filtered, paged, and sorted according to the respective parameters.  Call data records are records of all inbound and outbound calls through Salesloft. A call data record may be associated with a call, but does not have to be. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallDataRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallDataRecordsApi apiInstance = new CallDataRecordsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of call data records to fetch. If a record can't be found, that record won't be returned and your request will be successful
    Boolean hasCall = true; // Boolean | Return only call data records which have or do not have a call logged for them
    List<String> createdAt = Arrays.asList(); // List<String> | Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> userGuid = Arrays.asList(); // List<String> | Filters list to only include guids
    List<Integer> personId = Arrays.asList(); // List<Integer> | Filters list by person_id. Multiple person ids can be applied
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<CallDataRecord> result = apiInstance.v2CallDataRecordsJsonGet(ids, hasCall, createdAt, updatedAt, userGuid, personId, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallDataRecordsApi#v2CallDataRecordsJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of call data records to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **hasCall** | **Boolean**| Return only call data records which have or do not have a call logged for them | [optional] |
| **createdAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **userGuid** | [**List&lt;String&gt;**](String.md)| Filters list to only include guids | [optional] |
| **personId** | [**List&lt;Integer&gt;**](Integer.md)| Filters list by person_id. Multiple person ids can be applied | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;CallDataRecord&gt;**](CallDataRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

