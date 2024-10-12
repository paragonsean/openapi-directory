# CadenceMembershipsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CadenceMembershipsIdJsonDelete**](CadenceMembershipsApi.md#v2CadenceMembershipsIdJsonDelete) | **DELETE** /v2/cadence_memberships/{id}.json | Delete a cadence membership |
| [**v2CadenceMembershipsIdJsonGet**](CadenceMembershipsApi.md#v2CadenceMembershipsIdJsonGet) | **GET** /v2/cadence_memberships/{id}.json | Fetch a cadence membership |
| [**v2CadenceMembershipsJsonGet**](CadenceMembershipsApi.md#v2CadenceMembershipsJsonGet) | **GET** /v2/cadence_memberships.json | List cadence memberships |
| [**v2CadenceMembershipsJsonPost**](CadenceMembershipsApi.md#v2CadenceMembershipsJsonPost) | **POST** /v2/cadence_memberships.json | Create a cadence membership |


<a id="v2CadenceMembershipsIdJsonDelete"></a>
# **v2CadenceMembershipsIdJsonDelete**
> v2CadenceMembershipsIdJsonDelete(id)

Delete a cadence membership

Cadence Membership 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadenceMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadenceMembershipsApi apiInstance = new CadenceMembershipsApi(defaultClient);
    String id = "id_example"; // String | CadenceMembership ID
    try {
      apiInstance.v2CadenceMembershipsIdJsonDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadenceMembershipsApi#v2CadenceMembershipsIdJsonDelete");
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
| **id** | **String**| CadenceMembership ID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The person has been removed from the cadence successfully |  -  |

<a id="v2CadenceMembershipsIdJsonGet"></a>
# **v2CadenceMembershipsIdJsonGet**
> CadenceMembership v2CadenceMembershipsIdJsonGet(id)

Fetch a cadence membership

Fetches a cadence membership, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadenceMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadenceMembershipsApi apiInstance = new CadenceMembershipsApi(defaultClient);
    String id = "id_example"; // String | CadenceMembership ID
    try {
      CadenceMembership result = apiInstance.v2CadenceMembershipsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadenceMembershipsApi#v2CadenceMembershipsIdJsonGet");
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
| **id** | **String**| CadenceMembership ID | |

### Return type

[**CadenceMembership**](CadenceMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CadenceMembershipsJsonGet"></a>
# **v2CadenceMembershipsJsonGet**
> List&lt;CadenceMembership&gt; v2CadenceMembershipsJsonGet(ids, personId, cadenceId, updatedAt, currentlyOnCadence, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List cadence memberships

Fetches multiple cadence membership records. The records can be filtered, paged, and sorted according to the respective parameters. A cadence membership is the association between a person and their current and historical time on a cadence. Cadence membership records are mutable and change over time. If a person is added to a cadence and re-added to the same cadence in the future, there is a single membership record. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadenceMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadenceMembershipsApi apiInstance = new CadenceMembershipsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of cadence memberships to fetch. If a record can't be found, that record won't be returned and your request will be successful
    Integer personId = 56; // Integer | ID of the person to find cadence memberships for
    Integer cadenceId = 56; // Integer | ID of the cadence to find cadence memberships for
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    Boolean currentlyOnCadence = true; // Boolean | If true, return only cadence memberships for people currently on cadences.  If false, return cadence memberships for people who have been removed from or have completed a cadence.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: added_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<CadenceMembership> result = apiInstance.v2CadenceMembershipsJsonGet(ids, personId, cadenceId, updatedAt, currentlyOnCadence, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadenceMembershipsApi#v2CadenceMembershipsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of cadence memberships to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **personId** | **Integer**| ID of the person to find cadence memberships for | [optional] |
| **cadenceId** | **Integer**| ID of the cadence to find cadence memberships for | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **currentlyOnCadence** | **Boolean**| If true, return only cadence memberships for people currently on cadences.  If false, return cadence memberships for people who have been removed from or have completed a cadence. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: added_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;CadenceMembership&gt;**](CadenceMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CadenceMembershipsJsonPost"></a>
# **v2CadenceMembershipsJsonPost**
> CadenceMembership v2CadenceMembershipsJsonPost(personId, cadenceId, userId, stepId)

Create a cadence membership

Adds a person to a cadence. person_id and cadence_id are required, and must be visible to the authenticated user. user_id will default to the authenticated user, but can be set to any visible user on the authenticated team.  A person cannot be added to a cadence on behalf of a teammate unless the cadence is a team cadence, the cadence is owned by the teammate, or the teammate has the Personal Cadence Admin permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadenceMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadenceMembershipsApi apiInstance = new CadenceMembershipsApi(defaultClient);
    Integer personId = 56; // Integer | ID of the person to create a cadence membership for
    Integer cadenceId = 56; // Integer | ID of the cadence to create a cadence membership for
    Integer userId = 56; // Integer | ID of the user to create a cadence membership for. The associated cadence must be owned by the user, or it must be a team cadence
    Integer stepId = 56; // Integer | ID of the step on which the person should start the cadence. Start on first step is the default behavior without this parameter.
    try {
      CadenceMembership result = apiInstance.v2CadenceMembershipsJsonPost(personId, cadenceId, userId, stepId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadenceMembershipsApi#v2CadenceMembershipsJsonPost");
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
| **personId** | **Integer**| ID of the person to create a cadence membership for | |
| **cadenceId** | **Integer**| ID of the cadence to create a cadence membership for | |
| **userId** | **Integer**| ID of the user to create a cadence membership for. The associated cadence must be owned by the user, or it must be a team cadence | [optional] |
| **stepId** | **Integer**| ID of the step on which the person should start the cadence. Start on first step is the default behavior without this parameter. | [optional] |

### Return type

[**CadenceMembership**](CadenceMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

