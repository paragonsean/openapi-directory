# DatabasesApi

All URIs are relative to *https://api.notion.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryADatabase**](DatabasesApi.md#queryADatabase) | **POST** /v1/databases/{id}/query | Query a database |
| [**retrieveADatabase**](DatabasesApi.md#retrieveADatabase) | **GET** /v1/databases/{id} | Retrieve a database |
| [**updateADatabase**](DatabasesApi.md#updateADatabase) | **PATCH** /v1/databases/{id} | Update a database |


<a id="queryADatabase"></a>
# **queryADatabase**
> QueryADatabase200Response queryADatabase(id, notionVersion, queryADatabaseRequest)

Query a database

Query a database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String id = "{{DATABASE_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    QueryADatabaseRequest queryADatabaseRequest = new QueryADatabaseRequest(); // QueryADatabaseRequest | 
    try {
      QueryADatabase200Response result = apiInstance.queryADatabase(id, notionVersion, queryADatabaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#queryADatabase");
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
| **id** | **String**|  | |
| **notionVersion** | **String**|  | [optional] |
| **queryADatabaseRequest** | [**QueryADatabaseRequest**](QueryADatabaseRequest.md)|  | [optional] |

### Return type

[**QueryADatabase200Response**](QueryADatabase200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Query a Database (Single Filter) |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

<a id="retrieveADatabase"></a>
# **retrieveADatabase**
> RetrieveADatabase200Response retrieveADatabase(id, notionVersion)

Retrieve a database

Retrieves a database object using the ID specified in the request path. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String id = "id_example"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    try {
      RetrieveADatabase200Response result = apiInstance.retrieveADatabase(id, notionVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#retrieveADatabase");
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
| **id** | **String**|  | |
| **notionVersion** | **String**|  | [optional] |

### Return type

[**RetrieveADatabase200Response**](RetrieveADatabase200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve a Database |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

<a id="updateADatabase"></a>
# **updateADatabase**
> UpdateADatabase200Response updateADatabase(id, notionVersion, updateADatabaseRequest)

Update a database

Update a database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String id = "id_example"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    UpdateADatabaseRequest updateADatabaseRequest = new UpdateADatabaseRequest(); // UpdateADatabaseRequest | 
    try {
      UpdateADatabase200Response result = apiInstance.updateADatabase(id, notionVersion, updateADatabaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#updateADatabase");
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
| **id** | **String**|  | |
| **notionVersion** | **String**|  | [optional] |
| **updateADatabaseRequest** | [**UpdateADatabaseRequest**](UpdateADatabaseRequest.md)|  | [optional] |

### Return type

[**UpdateADatabase200Response**](UpdateADatabase200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Update a Database |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

