# SpotInsertionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2SpotinsertionsGet**](SpotInsertionsApi.md#apiV2SpotinsertionsGet) | **GET** /api/v2/spotinsertions | Returns the spot insertions matching the query parameters. |
| [**apiV2SpotinsertionsIdDelete**](SpotInsertionsApi.md#apiV2SpotinsertionsIdDelete) | **DELETE** /api/v2/spotinsertions/{id} | Deletes the spot insertion with the given ID. |
| [**apiV2SpotinsertionsIdGet**](SpotInsertionsApi.md#apiV2SpotinsertionsIdGet) | **GET** /api/v2/spotinsertions/{id} | Returns the spot insertion matching the given ID. |
| [**apiV2SpotinsertionsPost**](SpotInsertionsApi.md#apiV2SpotinsertionsPost) | **POST** /api/v2/spotinsertions | Creates a new spot insertion. |


<a id="apiV2SpotinsertionsGet"></a>
# **apiV2SpotinsertionsGet**
> List&lt;SpotInsertion&gt; apiV2SpotinsertionsGet(pageStart, pageSize, orderById)

Returns the spot insertions matching the query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotInsertionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotInsertionsApi apiInstance = new SpotInsertionsApi(defaultClient);
    Integer pageStart = 0; // Integer | The start page of the results to return. The first item is indexed at 0.
    Integer pageSize = 500; // Integer | The number of items to return. Must be between 0 and 500, inclusive.
    String orderById = "asc"; // String | The sort order of the list of spot insertions, based on ID. If unspecified, the spot insertions are returned in random order. If using paging to iterate through the results, sort order should be specified.
    try {
      List<SpotInsertion> result = apiInstance.apiV2SpotinsertionsGet(pageStart, pageSize, orderById);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotInsertionsApi#apiV2SpotinsertionsGet");
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
| **pageStart** | **Integer**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500] |
| **orderById** | **String**| The sort order of the list of spot insertions, based on ID. If unspecified, the spot insertions are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] [enum: asc, desc] |

### Return type

[**List&lt;SpotInsertion&gt;**](SpotInsertion.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spot insertions matching the query parameters |  -  |
| **403** | Authorization failed. |  -  |

<a id="apiV2SpotinsertionsIdDelete"></a>
# **apiV2SpotinsertionsIdDelete**
> apiV2SpotinsertionsIdDelete(id)

Deletes the spot insertion with the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotInsertionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotInsertionsApi apiInstance = new SpotInsertionsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.apiV2SpotinsertionsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotInsertionsApi#apiV2SpotinsertionsIdDelete");
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
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spot insertion was deleted. |  -  |
| **403** | Authorization failed, or the user is not permitted to delete the spot insertion. |  -  |
| **404** | The spot insertion cannot be found. |  -  |

<a id="apiV2SpotinsertionsIdGet"></a>
# **apiV2SpotinsertionsIdGet**
> SpotInsertion apiV2SpotinsertionsIdGet(id)

Returns the spot insertion matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotInsertionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotInsertionsApi apiInstance = new SpotInsertionsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      SpotInsertion result = apiInstance.apiV2SpotinsertionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotInsertionsApi#apiV2SpotinsertionsIdGet");
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
| **id** | **Long**|  | |

### Return type

[**SpotInsertion**](SpotInsertion.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spot insertion with the given ID. |  -  |
| **403** | Authorization failed, or the user is not permitted to view the spot insertion. |  -  |
| **404** | The spot insertion cannot be found. |  -  |

<a id="apiV2SpotinsertionsPost"></a>
# **apiV2SpotinsertionsPost**
> SpotInsertion apiV2SpotinsertionsPost(spotInsertion)

Creates a new spot insertion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotInsertionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotInsertionsApi apiInstance = new SpotInsertionsApi(defaultClient);
    SpotInsertion spotInsertion = new SpotInsertion(); // SpotInsertion | 
    try {
      SpotInsertion result = apiInstance.apiV2SpotinsertionsPost(spotInsertion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotInsertionsApi#apiV2SpotinsertionsPost");
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
| **spotInsertion** | [**SpotInsertion**](SpotInsertion.md)|  | [optional] |

### Return type

[**SpotInsertion**](SpotInsertion.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created spot insertion with fields populated. |  -  |
| **400** | The request is missing required data or invalid. |  -  |
| **403** | Authorization failed, or the user is not permitted to create the spot insertion. |  -  |
| **500** | Creating the spot insertion failed, even though the request was valid. |  -  |

