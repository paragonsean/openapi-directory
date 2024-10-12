# SpecificationGroupApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSpecificationgroupGroupIdPut**](SpecificationGroupApi.md#apiCatalogPvtSpecificationgroupGroupIdPut) | **PUT** /api/catalog/pvt/specificationgroup/{groupId} | Update Specification Group |
| [**specificationGroupInsert2**](SpecificationGroupApi.md#specificationGroupInsert2) | **POST** /api/catalog/pvt/specificationgroup | Create Specification Group |
| [**specificationsGroupGet**](SpecificationGroupApi.md#specificationsGroupGet) | **GET** /api/catalog_system/pub/specification/groupGet/{groupId} | Get Specification Group |
| [**specificationsGroupListbyCategory**](SpecificationGroupApi.md#specificationsGroupListbyCategory) | **GET** /api/catalog_system/pvt/specification/groupbycategory/{categoryId} | List Specification Group by Category |


<a id="apiCatalogPvtSpecificationgroupGroupIdPut"></a>
# **apiCatalogPvtSpecificationgroupGroupIdPut**
> ApiCatalogPvtSpecificationgroupGroupIdPut200Response apiCatalogPvtSpecificationgroupGroupIdPut(contentType, accept, groupId, requestBody8)

Update Specification Group

Update a specification group.   &gt;⚠️ It is also possible to update a Specification Group by using an alternative legacy route: &#x60;/api/catalog_system/pvt/specification/group&#x60;.    ## Request and response body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1,      \&quot;Id\&quot;: 17,      \&quot;Name\&quot;: \&quot;NewGroupName\&quot;,      \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SpecificationGroupApi apiInstance = new SpecificationGroupApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer groupId = 1; // Integer | Group’s unique numerical identifier.
    RequestBody8 requestBody8 = new RequestBody8(); // RequestBody8 | 
    try {
      ApiCatalogPvtSpecificationgroupGroupIdPut200Response result = apiInstance.apiCatalogPvtSpecificationgroupGroupIdPut(contentType, accept, groupId, requestBody8);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationGroupApi#apiCatalogPvtSpecificationgroupGroupIdPut");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **groupId** | **Integer**| Group’s unique numerical identifier. | |
| **requestBody8** | [**RequestBody8**](RequestBody8.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSpecificationgroupGroupIdPut200Response**](ApiCatalogPvtSpecificationgroupGroupIdPut200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="specificationGroupInsert2"></a>
# **specificationGroupInsert2**
> SpecificationGroupInsert2200Response specificationGroupInsert2(contentType, accept, specificationGroupInsertRequest)

Create Specification Group

Create a specification group.   &gt;⚠️ It is also possible to create a Specification Group by using an alternative legacy route: &#x60;/api/catalog_system/pvt/specification/group&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1,      \&quot;Name\&quot;: \&quot;Sizes\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 6,    \&quot;CategoryId\&quot;: 1,    \&quot;Name\&quot;: \&quot;Sizes\&quot;,    \&quot;Position\&quot;: 3  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SpecificationGroupApi apiInstance = new SpecificationGroupApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SpecificationGroupInsertRequest specificationGroupInsertRequest = new SpecificationGroupInsertRequest(); // SpecificationGroupInsertRequest | 
    try {
      SpecificationGroupInsert2200Response result = apiInstance.specificationGroupInsert2(contentType, accept, specificationGroupInsertRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationGroupApi#specificationGroupInsert2");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **specificationGroupInsertRequest** | [**SpecificationGroupInsertRequest**](SpecificationGroupInsertRequest.md)|  | |

### Return type

[**SpecificationGroupInsert2200Response**](SpecificationGroupInsert2200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="specificationsGroupGet"></a>
# **specificationsGroupGet**
> SpecificationsGroup specificationsGroupGet(contentType, accept, groupId)

Get Specification Group

Retrieves details from a specification group by the ID of the group.   ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;CategoryId\&quot;: 1,    \&quot;Id\&quot;: 6,    \&quot;Name\&quot;: \&quot;Sizes\&quot;,    \&quot;Position\&quot;: 3  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SpecificationGroupApi apiInstance = new SpecificationGroupApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String groupId = "6"; // String | Specification Group ID.
    try {
      SpecificationsGroup result = apiInstance.specificationsGroupGet(contentType, accept, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationGroupApi#specificationsGroupGet");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **groupId** | **String**| Specification Group ID. | |

### Return type

[**SpecificationsGroup**](SpecificationsGroup.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="specificationsGroupListbyCategory"></a>
# **specificationsGroupListbyCategory**
> List&lt;SpecificationsGroup&gt; specificationsGroupListbyCategory(contentType, accept, categoryId)

List Specification Group by Category

Retrieves a list of specification groups by the category ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {        \&quot;CategoryId\&quot;: 1,        \&quot;Id\&quot;: 5,        \&quot;Name\&quot;: \&quot;Materials\&quot;,        \&quot;Position\&quot;: 2      },      {        \&quot;CategoryId\&quot;: 1,        \&quot;Id\&quot;: 6,        \&quot;Name\&quot;: \&quot;Sizes\&quot;,        \&quot;Position\&quot;: 3      }    ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SpecificationGroupApi apiInstance = new SpecificationGroupApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String categoryId = "1"; // String | 
    try {
      List<SpecificationsGroup> result = apiInstance.specificationsGroupListbyCategory(contentType, accept, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationGroupApi#specificationsGroupListbyCategory");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **categoryId** | **String**|  | |

### Return type

[**List&lt;SpecificationsGroup&gt;**](SpecificationsGroup.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

