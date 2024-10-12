# ManifestsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createManifest**](ManifestsApi.md#createManifest) | **POST** /v1/manifests | Create Manifest |
| [**getManifestById**](ManifestsApi.md#getManifestById) | **GET** /v1/manifests/{manifest_id} | Get Manifest By Id |
| [**getManifestRequestById**](ManifestsApi.md#getManifestRequestById) | **GET** /v1/manifests/requests/{manifest_request_id} | Get Manifest Request By Id |
| [**listManifests**](ManifestsApi.md#listManifests) | **GET** /v1/manifests | List Manifests |


<a id="createManifest"></a>
# **createManifest**
> CreateManifestResponseBody createManifest(createManifestRequestBody)

Create Manifest

Each ShipEngine manifest is created for a specific warehouse, so you&#39;ll need to provide the warehouse_id rather than the ship_from address. You can create a warehouse for each location that you want to create manifests for. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManifestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ManifestsApi apiInstance = new ManifestsApi(defaultClient);
    CreateManifestRequestBody createManifestRequestBody = new CreateManifestRequestBody(); // CreateManifestRequestBody | 
    try {
      CreateManifestResponseBody result = apiInstance.createManifest(createManifestRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManifestsApi#createManifest");
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
| **createManifestRequestBody** | [**CreateManifestRequestBody**](CreateManifestRequestBody.md)|  | |

### Return type

[**CreateManifestResponseBody**](CreateManifestResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getManifestById"></a>
# **getManifestById**
> GetManifestByIdResponseBody getManifestById(manifestId)

Get Manifest By Id

Get Manifest By Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManifestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ManifestsApi apiInstance = new ManifestsApi(defaultClient);
    String manifestId = "manifestId_example"; // String | The Manifest Id
    try {
      GetManifestByIdResponseBody result = apiInstance.getManifestById(manifestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManifestsApi#getManifestById");
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
| **manifestId** | **String**| The Manifest Id | |

### Return type

[**GetManifestByIdResponseBody**](GetManifestByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getManifestRequestById"></a>
# **getManifestRequestById**
> CreateManifestResponseBody getManifestRequestById(manifestRequestId)

Get Manifest Request By Id

Get Manifest Request By Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManifestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ManifestsApi apiInstance = new ManifestsApi(defaultClient);
    String manifestRequestId = "manifestRequestId_example"; // String | The Manifest Request Id
    try {
      CreateManifestResponseBody result = apiInstance.getManifestRequestById(manifestRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManifestsApi#getManifestRequestById");
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
| **manifestRequestId** | **String**| The Manifest Request Id | |

### Return type

[**CreateManifestResponseBody**](CreateManifestResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listManifests"></a>
# **listManifests**
> ListManifestsResponseBody listManifests(warehouseId, shipDateStart, shipDateEnd, createdAtStart, createdAtEnd, carrierId, page, pageSize, labelIds)

List Manifests

Similar to querying shipments, we allow you to query manifests since there will likely be a large number over a long period of time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManifestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ManifestsApi apiInstance = new ManifestsApi(defaultClient);
    String warehouseId = "warehouseId_example"; // String | Warehouse ID
    OffsetDateTime shipDateStart = OffsetDateTime.parse("2018-09-23T15:00:00.000Z"); // OffsetDateTime | ship date start range
    OffsetDateTime shipDateEnd = OffsetDateTime.parse("2018-09-23T15:00:00.000Z"); // OffsetDateTime | ship date end range
    OffsetDateTime createdAtStart = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
    OffsetDateTime createdAtEnd = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)
    String carrierId = "carrierId_example"; // String | Carrier ID
    Integer page = 1; // Integer | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
    Integer pageSize = 25; // Integer | The number of results to return per response.
    List<String> labelIds = Arrays.asList(); // List<String> | 
    try {
      ListManifestsResponseBody result = apiInstance.listManifests(warehouseId, shipDateStart, shipDateEnd, createdAtStart, createdAtEnd, carrierId, page, pageSize, labelIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManifestsApi#listManifests");
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
| **warehouseId** | **String**| Warehouse ID | [optional] |
| **shipDateStart** | **OffsetDateTime**| ship date start range | [optional] |
| **shipDateEnd** | **OffsetDateTime**| ship date end range | [optional] |
| **createdAtStart** | **OffsetDateTime**| Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time) | [optional] |
| **createdAtEnd** | **OffsetDateTime**| Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time) | [optional] |
| **carrierId** | **String**| Carrier ID | [optional] |
| **page** | **Integer**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per response. | [optional] [default to 25] |
| **labelIds** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**ListManifestsResponseBody**](ListManifestsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

