# RetargetingApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retargetingCount**](RetargetingApi.md#retargetingCount) | **GET** /retargeting/count | Retrieve count of retargeting scripts |
| [**retargetingDelete**](RetargetingApi.md#retargetingDelete) | **DELETE** /retargeting/{id} | Deletes a retargeting script (and remove associations) |
| [**retargetingGet**](RetargetingApi.md#retargetingGet) | **GET** /retargeting | List of all the retargeting scripts associated to the user |
| [**retargetingGetDatapoints**](RetargetingApi.md#retargetingGetDatapoints) | **GET** /retargeting/{id}/datapoints | List of all the datapoints associated to the retargeting script. |
| [**retargetingGetDatapointsCount**](RetargetingApi.md#retargetingGetDatapointsCount) | **GET** /retargeting/{id}/datapoints/count | Count the datapoints associated to the retargeting script. |
| [**retargetingIdGet**](RetargetingApi.md#retargetingIdGet) | **GET** /retargeting/{id} | Get a retargeting script object |
| [**retargetingPost**](RetargetingApi.md#retargetingPost) | **POST** /retargeting/{id} | Updates a retargeting script |
| [**retargetingPut**](RetargetingApi.md#retargetingPut) | **POST** /retargeting | Creates a retargeting script |


<a id="retargetingCount"></a>
# **retargetingCount**
> ApiCoreResponsesCountResponce retargetingCount()

Retrieve count of retargeting scripts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    try {
      ApiCoreResponsesCountResponce result = apiInstance.retargetingCount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingCount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingDelete"></a>
# **retargetingDelete**
> ApiCoreResponsesEntityUriSystemInt64 retargetingDelete(id)

Deletes a retargeting script (and remove associations)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    Long id = 56L; // Long | The id of the retargeting script
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.retargetingDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingDelete");
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
| **id** | **Long**| The id of the retargeting script | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingGet"></a>
# **retargetingGet**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 retargetingGet(offset, limit)

List of all the retargeting scripts associated to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.retargetingGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingGet");
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
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingGetDatapoints"></a>
# **retargetingGetDatapoints**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 retargetingGetDatapoints(id, offset, limit, status, tags, textSearch, onlyFavorites, sortBy, sortDirection, createdAfter, createdBefore)

List of all the datapoints associated to the retargeting script.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    Long id = 56L; // Long | Id of the retargeting script
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    String status = "deleted"; // String | Status of the datapoint
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    Boolean onlyFavorites = true; // Boolean | Filter fields by favourite status
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.retargetingGetDatapoints(id, offset, limit, status, tags, textSearch, onlyFavorites, sortBy, sortDirection, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingGetDatapoints");
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
| **id** | **Long**| Id of the retargeting script | |
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active, paused, spam] |
| **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingGetDatapointsCount"></a>
# **retargetingGetDatapointsCount**
> ApiCoreResponsesCountResponce retargetingGetDatapointsCount(id, status, tags, textSearch, onlyFavorites, createdAfter, createdBefore)

Count the datapoints associated to the retargeting script.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    String status = "deleted"; // String | Status of the datapoint
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    Boolean onlyFavorites = true; // Boolean | Filter fields by favourite status
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.retargetingGetDatapointsCount(id, status, tags, textSearch, onlyFavorites, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingGetDatapointsCount");
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
| **id** | **Long**| Id of the group | |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active, paused, spam] |
| **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] |
| **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingIdGet"></a>
# **retargetingIdGet**
> ApiCoreDtoRetargetingRetargetingScript retargetingIdGet(id)

Get a retargeting script object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    Long id = 56L; // Long | The id of the retargeting script
    try {
      ApiCoreDtoRetargetingRetargetingScript result = apiInstance.retargetingIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingIdGet");
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
| **id** | **Long**| The id of the retargeting script | |

### Return type

[**ApiCoreDtoRetargetingRetargetingScript**](ApiCoreDtoRetargetingRetargetingScript.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingPost"></a>
# **retargetingPost**
> ApiCoreResponsesEntityUriSystemInt64 retargetingPost(id, apiCoreDtoRetargetingRetargetingScript)

Updates a retargeting script

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    Long id = 56L; // Long | The id of the retargeting script
    ApiCoreDtoRetargetingRetargetingScript apiCoreDtoRetargetingRetargetingScript = new ApiCoreDtoRetargetingRetargetingScript(); // ApiCoreDtoRetargetingRetargetingScript | The body of the retargeting script
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.retargetingPost(id, apiCoreDtoRetargetingRetargetingScript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingPost");
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
| **id** | **Long**| The id of the retargeting script | |
| **apiCoreDtoRetargetingRetargetingScript** | [**ApiCoreDtoRetargetingRetargetingScript**](ApiCoreDtoRetargetingRetargetingScript.md)| The body of the retargeting script | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="retargetingPut"></a>
# **retargetingPut**
> ApiCoreResponsesEntityUriSystemInt64 retargetingPut(apiCoreDtoRetargetingRetargetingScript)

Creates a retargeting script

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetargetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RetargetingApi apiInstance = new RetargetingApi(defaultClient);
    ApiCoreDtoRetargetingRetargetingScript apiCoreDtoRetargetingRetargetingScript = new ApiCoreDtoRetargetingRetargetingScript(); // ApiCoreDtoRetargetingRetargetingScript | The body of the retargeting script
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.retargetingPut(apiCoreDtoRetargetingRetargetingScript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetargetingApi#retargetingPut");
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
| **apiCoreDtoRetargetingRetargetingScript** | [**ApiCoreDtoRetargetingRetargetingScript**](ApiCoreDtoRetargetingRetargetingScript.md)| The body of the retargeting script | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

