# LiabilitiesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liabilitiesDeleteById**](LiabilitiesApi.md#liabilitiesDeleteById) | **DELETE** /api/Liabilities/{id} |  |
| [**liabilitiesGetById**](LiabilitiesApi.md#liabilitiesGetById) | **GET** /api/Liabilities/{id} |  |
| [**liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid**](LiabilitiesApi.md#liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid) | **GET** /api/Liabilities |  |
| [**liabilitiesPostByModel**](LiabilitiesApi.md#liabilitiesPostByModel) | **POST** /api/Liabilities |  |
| [**liabilitiesPutByIdModel**](LiabilitiesApi.md#liabilitiesPutByIdModel) | **PUT** /api/Liabilities/{id} |  |


<a id="liabilitiesDeleteById"></a>
# **liabilitiesDeleteById**
> liabilitiesDeleteById(id)



Description: The operation removes a Liability tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Liability from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    Integer id = 56; // Integer | The Liability ID used to identify which Liability to remove
    try {
      apiInstance.liabilitiesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesDeleteById");
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
| **id** | **Integer**| The Liability ID used to identify which Liability to remove | |

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
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Liability data access. |  -  |
| **403** | Request is restricted for access to Liability. |  -  |
| **404** | Liability not found. |  -  |

<a id="liabilitiesGetById"></a>
# **liabilitiesGetById**
> LiabilityWithIdModel liabilitiesGetById(id)



Description: This operation retrieves a single Liability for the specified Liability ID.&lt;br /&gt;                Purpose: Provides access to the Liability including owner and type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Liability used to retreive the Liability
    try {
      LiabilityWithIdModel result = apiInstance.liabilitiesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesGetById");
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
| **id** | **Integer**| The ID of the Liability used to retreive the Liability | |

### Return type

[**LiabilityWithIdModel**](LiabilityWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Liability data access. |  -  |
| **403** | Request is restricted for access to Liability. |  -  |
| **404** | Liability not found. |  -  |

<a id="liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid"></a>
# **liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid**
> LiabilitiesModel liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid(factFinderId, externalSourceId)



Description: This operation retrieves all Liabilities for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Liabilities including owner and type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Liabilities
    String externalSourceId = "externalSourceId_example"; // String | The external source ID used to filter Liabilities
    try {
      LiabilitiesModel result = apiInstance.liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid(factFinderId, externalSourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Liabilities | |
| **externalSourceId** | **String**| The external source ID used to filter Liabilities | [optional] |

### Return type

[**LiabilitiesModel**](LiabilitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Liability data access. |  -  |
| **403** | Request is restricted for access to Liability. |  -  |
| **404** | Liability not found. |  -  |

<a id="liabilitiesPostByModel"></a>
# **liabilitiesPostByModel**
> LiabilityWithIdModel liabilitiesPostByModel(model)



Description: The operation creates a Liability.&lt;br /&gt;                Purpose: Allows for creation of Liabilities on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    LiabilityModel model = new LiabilityModel(); // LiabilityModel | The Liability to be added to the Fact Finder
    try {
      LiabilityWithIdModel result = apiInstance.liabilitiesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesPostByModel");
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
| **model** | [**LiabilityModel**](LiabilityModel.md)| The Liability to be added to the Fact Finder | |

### Return type

[**LiabilityWithIdModel**](LiabilityWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Liability data access. |  -  |
| **403** | Request is restricted for access to Liability. |  -  |
| **404** | Liability not found. |  -  |

<a id="liabilitiesPutByIdModel"></a>
# **liabilitiesPutByIdModel**
> LiabilityWithIdModel liabilitiesPutByIdModel(id, model)



Description: The operation updates a Liability.&lt;br /&gt;                Purpose: Allows for complete replacement of a Liability on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    Integer id = 56; // Integer | The existing Liability ID used to identify which Liability to update
    LiabilityModel model = new LiabilityModel(); // LiabilityModel | The Liability to be updated on a Fact Finder
    try {
      LiabilityWithIdModel result = apiInstance.liabilitiesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesPutByIdModel");
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
| **id** | **Integer**| The existing Liability ID used to identify which Liability to update | |
| **model** | [**LiabilityModel**](LiabilityModel.md)| The Liability to be updated on a Fact Finder | |

### Return type

[**LiabilityWithIdModel**](LiabilityWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Liability data access. |  -  |
| **403** | Request is restricted for access to Liability. |  -  |
| **404** | Liability not found. |  -  |

