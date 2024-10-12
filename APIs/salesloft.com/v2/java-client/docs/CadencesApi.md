# CadencesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CadencesIdJsonGet**](CadencesApi.md#v2CadencesIdJsonGet) | **GET** /v2/cadences/{id}.json | Fetch a cadence |
| [**v2CadencesJsonGet**](CadencesApi.md#v2CadencesJsonGet) | **GET** /v2/cadences.json | List cadences |


<a id="v2CadencesIdJsonGet"></a>
# **v2CadencesIdJsonGet**
> Cadence v2CadencesIdJsonGet(id)

Fetch a cadence

Fetches a cadence, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadencesApi apiInstance = new CadencesApi(defaultClient);
    String id = "id_example"; // String | Cadence ID
    try {
      Cadence result = apiInstance.v2CadencesIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadencesApi#v2CadencesIdJsonGet");
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
| **id** | **String**| Cadence ID | |

### Return type

[**Cadence**](Cadence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CadencesJsonGet"></a>
# **v2CadencesJsonGet**
> List&lt;Cadence&gt; v2CadencesJsonGet(ids, updatedAt, teamCadence, shared, ownedByGuid, peopleAddable, name, groupIds, archived, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List cadences

Fetches multiple cadence records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadencesApi apiInstance = new CadencesApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of cadences to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    Boolean teamCadence = true; // Boolean | Filters cadences by whether they are a team cadence or not
    Boolean shared = true; // Boolean | Filters cadences by whether they are shared
    List<String> ownedByGuid = Arrays.asList(); // List<String> | Filters cadences by the owner's guid. Multiple owner guids can be applied
    Boolean peopleAddable = true; // Boolean | Filters cadences by whether they are able to have people added to them
    List<String> name = Arrays.asList(); // List<String> | Filters cadences by name
    String groupIds = "groupIds_example"; // String | Filters by group ids. Also supports group ids passed in as a JSON array string
    Boolean archived = true; // Boolean | Filters by whether the Cadences have been archived. Excluding this field will result in both archived and unarchived Cadences to return.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Cadence> result = apiInstance.v2CadencesJsonGet(ids, updatedAt, teamCadence, shared, ownedByGuid, peopleAddable, name, groupIds, archived, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadencesApi#v2CadencesJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of cadences to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **teamCadence** | **Boolean**| Filters cadences by whether they are a team cadence or not | [optional] |
| **shared** | **Boolean**| Filters cadences by whether they are shared | [optional] |
| **ownedByGuid** | [**List&lt;String&gt;**](String.md)| Filters cadences by the owner&#39;s guid. Multiple owner guids can be applied | [optional] |
| **peopleAddable** | **Boolean**| Filters cadences by whether they are able to have people added to them | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| Filters cadences by name | [optional] |
| **groupIds** | **String**| Filters by group ids. Also supports group ids passed in as a JSON array string | [optional] |
| **archived** | **Boolean**| Filters by whether the Cadences have been archived. Excluding this field will result in both archived and unarchived Cadences to return. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Cadence&gt;**](Cadence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

