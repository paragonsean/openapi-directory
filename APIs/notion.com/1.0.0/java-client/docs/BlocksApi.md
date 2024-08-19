# BlocksApi

All URIs are relative to *https://api.notion.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appendBlockChildren**](BlocksApi.md#appendBlockChildren) | **PATCH** /v1/blocks/{id}/children | Append block children |
| [**deleteABlock**](BlocksApi.md#deleteABlock) | **DELETE** /v1/blocks/{id} | Delete a block |
| [**retrieveABlock**](BlocksApi.md#retrieveABlock) | **GET** /v1/blocks/{id} | Retrieve a block |
| [**retrieveBlockChildren**](BlocksApi.md#retrieveBlockChildren) | **GET** /v1/blocks/{id}/children | Retrieve block children |
| [**updateABlock**](BlocksApi.md#updateABlock) | **PATCH** /v1/blocks/{id} | Update a block |


<a id="appendBlockChildren"></a>
# **appendBlockChildren**
> AppendBlockChildren200Response appendBlockChildren(id, notionVersion, appendBlockChildrenRequest)

Append block children

Append block children

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String id = "{{PAGE_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    AppendBlockChildrenRequest appendBlockChildrenRequest = new AppendBlockChildrenRequest(); // AppendBlockChildrenRequest | 
    try {
      AppendBlockChildren200Response result = apiInstance.appendBlockChildren(id, notionVersion, appendBlockChildrenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#appendBlockChildren");
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
| **appendBlockChildrenRequest** | [**AppendBlockChildrenRequest**](AppendBlockChildrenRequest.md)|  | [optional] |

### Return type

[**AppendBlockChildren200Response**](AppendBlockChildren200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Append block children |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

<a id="deleteABlock"></a>
# **deleteABlock**
> DeleteABlock200Response deleteABlock(id, notionVersion)

Delete a block

Delete a block

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String id = "{{BLOCK_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    try {
      DeleteABlock200Response result = apiInstance.deleteABlock(id, notionVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#deleteABlock");
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

[**DeleteABlock200Response**](DeleteABlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Delete a block |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

<a id="retrieveABlock"></a>
# **retrieveABlock**
> RetrieveABlock200Response retrieveABlock(id, notionVersion)

Retrieve a block

Retrieve a block

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String id = "{{BLOCK_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    try {
      RetrieveABlock200Response result = apiInstance.retrieveABlock(id, notionVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#retrieveABlock");
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

[**RetrieveABlock200Response**](RetrieveABlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve a block |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

<a id="retrieveBlockChildren"></a>
# **retrieveBlockChildren**
> RetrieveBlockChildren200Response retrieveBlockChildren(id, pageSize, notionVersion)

Retrieve block children

Retrieve block children

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String id = "{{PAGE_ID}}"; // String | 
    String pageSize = "100"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    try {
      RetrieveBlockChildren200Response result = apiInstance.retrieveBlockChildren(id, pageSize, notionVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#retrieveBlockChildren");
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
| **pageSize** | **String**|  | [optional] |
| **notionVersion** | **String**|  | [optional] |

### Return type

[**RetrieveBlockChildren200Response**](RetrieveBlockChildren200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve block children |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

<a id="updateABlock"></a>
# **updateABlock**
> RetrieveABlock200Response updateABlock(id, notionVersion, updateABlockRequest)

Update a block

This endpoint allows you to update block content. [See Full Documentation](https://developers.notion.com/reference/update-a-block)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String id = "{{BLOCK_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    UpdateABlockRequest updateABlockRequest = new UpdateABlockRequest(); // UpdateABlockRequest | 
    try {
      RetrieveABlock200Response result = apiInstance.updateABlock(id, notionVersion, updateABlockRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#updateABlock");
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
| **updateABlockRequest** | [**UpdateABlockRequest**](UpdateABlockRequest.md)|  | [optional] |

### Return type

[**RetrieveABlock200Response**](RetrieveABlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Update a block |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

