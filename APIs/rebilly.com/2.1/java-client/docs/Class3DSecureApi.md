# Class3DSecureApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**get3DSecure**](Class3DSecureApi.md#get3DSecure) | **GET** /3dsecure/{id} | Retrieve a ThreeDSecure entry |
| [**get3DSecureCollection**](Class3DSecureApi.md#get3DSecureCollection) | **GET** /3dsecure | Retrieve a list of ThreeDSecure entries |
| [**post3DSecure**](Class3DSecureApi.md#post3DSecure) | **POST** /3dsecure | Create a ThreeDSecure entry |


<a id="get3DSecure"></a>
# **get3DSecure**
> ThreeDSecure get3DSecure(id, organizationId)

Retrieve a ThreeDSecure entry

Retrieve a ThreeDSecure entry with specified identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3DSecureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    Class3DSecureApi apiInstance = new Class3DSecureApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      ThreeDSecure result = apiInstance.get3DSecure(id, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3DSecureApi#get3DSecure");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**ThreeDSecure**](ThreeDSecure.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ThreeDSecure entry was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="get3DSecureCollection"></a>
# **get3DSecureCollection**
> List&lt;ThreeDSecure&gt; get3DSecureCollection(organizationId, limit, offset)

Retrieve a list of ThreeDSecure entries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3DSecureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    Class3DSecureApi apiInstance = new Class3DSecureApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    try {
      List<ThreeDSecure> result = apiInstance.get3DSecureCollection(organizationId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3DSecureApi#get3DSecureCollection");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |

### Return type

[**List&lt;ThreeDSecure&gt;**](ThreeDSecure.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="post3DSecure"></a>
# **post3DSecure**
> ThreeDSecure post3DSecure(threeDSecure, organizationId)

Create a ThreeDSecure entry

Create a ThreeDSecure entry. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3DSecureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    Class3DSecureApi apiInstance = new Class3DSecureApi(defaultClient);
    ThreeDSecure threeDSecure = new ThreeDSecure(); // ThreeDSecure | ThreeDSecure resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      ThreeDSecure result = apiInstance.post3DSecure(threeDSecure, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3DSecureApi#post3DSecure");
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
| **threeDSecure** | [**ThreeDSecure**](ThreeDSecure.md)| ThreeDSecure resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**ThreeDSecure**](ThreeDSecure.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ThreeDSecure entry was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

