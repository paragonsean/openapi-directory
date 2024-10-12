# CacheRestApiApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cachekeyInvalidatePost**](CacheRestApiApi.md#cachekeyInvalidatePost) | **POST** /cachekey/invalidate |  |


<a id="cachekeyInvalidatePost"></a>
# **cachekeyInvalidatePost**
> cachekeyInvalidatePost(cacheInvalidationRequestSchema)



Takes a list of datasources, finds the associated cache records and invalidates them and removes the database records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CacheRestApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CacheRestApiApi apiInstance = new CacheRestApiApi(defaultClient);
    CacheInvalidationRequestSchema cacheInvalidationRequestSchema = new CacheInvalidationRequestSchema(); // CacheInvalidationRequestSchema | A list of datasources uuid or the tuples of database and datasource names
    try {
      apiInstance.cachekeyInvalidatePost(cacheInvalidationRequestSchema);
    } catch (ApiException e) {
      System.err.println("Exception when calling CacheRestApiApi#cachekeyInvalidatePost");
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
| **cacheInvalidationRequestSchema** | [**CacheInvalidationRequestSchema**](CacheInvalidationRequestSchema.md)| A list of datasources uuid or the tuples of database and datasource names | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | cache was successfully invalidated |  -  |
| **400** | Bad request |  -  |
| **500** | Fatal error |  -  |

