# LongTermCareInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**longTermCareInsurancePoliciesDeleteById**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesDeleteById) | **DELETE** /api/LongTermCareInsurancePolicies/{id} |  |
| [**longTermCareInsurancePoliciesGetById**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesGetById) | **GET** /api/LongTermCareInsurancePolicies/{id} |  |
| [**longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/LongTermCareInsurancePolicies |  |
| [**longTermCareInsurancePoliciesPostByModel**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesPostByModel) | **POST** /api/LongTermCareInsurancePolicies |  |
| [**longTermCareInsurancePoliciesPutByIdModel**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesPutByIdModel) | **PUT** /api/LongTermCareInsurancePolicies/{id} |  |


<a id="longTermCareInsurancePoliciesDeleteById"></a>
# **longTermCareInsurancePoliciesDeleteById**
> longTermCareInsurancePoliciesDeleteById(id)



Description: The operation removes a Long Term Care Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Long Term Care Insurance Policy from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermCareInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LongTermCareInsurancePoliciesApi apiInstance = new LongTermCareInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to remove
    try {
      apiInstance.longTermCareInsurancePoliciesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermCareInsurancePoliciesApi#longTermCareInsurancePoliciesDeleteById");
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
| **id** | **Integer**| The Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to remove | |

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
| **401** | Unauthorized for Long Term Care Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Long Term Care Insurance Policy. |  -  |
| **404** | Long Term Care Insurance Policy not found. |  -  |

<a id="longTermCareInsurancePoliciesGetById"></a>
# **longTermCareInsurancePoliciesGetById**
> LongTermCareInsurancePolicyWithIdModel longTermCareInsurancePoliciesGetById(id)



Description: This operation retrieves a single Long Term Care Insurance Policy for the specified Long Term Care Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Long Term Care Insurance Policy including description and premium.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermCareInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LongTermCareInsurancePoliciesApi apiInstance = new LongTermCareInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Long Term Care Insurance Policy used to retreive the Long Term Care Insurance Policy
    try {
      LongTermCareInsurancePolicyWithIdModel result = apiInstance.longTermCareInsurancePoliciesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermCareInsurancePoliciesApi#longTermCareInsurancePoliciesGetById");
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
| **id** | **Integer**| The ID of the Long Term Care Insurance Policy used to retreive the Long Term Care Insurance Policy | |

### Return type

[**LongTermCareInsurancePolicyWithIdModel**](LongTermCareInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Long Term Care Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Long Term Care Insurance Policy. |  -  |
| **404** | Long Term Care Insurance Policy not found. |  -  |

<a id="longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid"></a>
# **longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid**
> LongTermCareInsurancePoliciesModel longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Long Term Care Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Long Term Care Insurance Policies including description and premium.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermCareInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LongTermCareInsurancePoliciesApi apiInstance = new LongTermCareInsurancePoliciesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Long Term Care Insurance Policies
    try {
      LongTermCareInsurancePoliciesModel result = apiInstance.longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermCareInsurancePoliciesApi#longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Long Term Care Insurance Policies | |

### Return type

[**LongTermCareInsurancePoliciesModel**](LongTermCareInsurancePoliciesModel.md)

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
| **401** | Unauthorized for Long Term Care Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Long Term Care Insurance Policy. |  -  |
| **404** | Long Term Care Insurance Policy not found. |  -  |

<a id="longTermCareInsurancePoliciesPostByModel"></a>
# **longTermCareInsurancePoliciesPostByModel**
> LongTermCareInsurancePolicyWithIdModel longTermCareInsurancePoliciesPostByModel(model)



Description: The operation creates a Long Term Care Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Long Term Care Insurance Policies on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermCareInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LongTermCareInsurancePoliciesApi apiInstance = new LongTermCareInsurancePoliciesApi(defaultClient);
    LongTermCareInsurancePolicyModel model = new LongTermCareInsurancePolicyModel(); // LongTermCareInsurancePolicyModel | The Long Term Care Insurance Policy to be added to the Fact Finder
    try {
      LongTermCareInsurancePolicyWithIdModel result = apiInstance.longTermCareInsurancePoliciesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermCareInsurancePoliciesApi#longTermCareInsurancePoliciesPostByModel");
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
| **model** | [**LongTermCareInsurancePolicyModel**](LongTermCareInsurancePolicyModel.md)| The Long Term Care Insurance Policy to be added to the Fact Finder | |

### Return type

[**LongTermCareInsurancePolicyWithIdModel**](LongTermCareInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Long Term Care Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Long Term Care Insurance Policy. |  -  |
| **404** | Long Term Care Insurance Policy not found. |  -  |

<a id="longTermCareInsurancePoliciesPutByIdModel"></a>
# **longTermCareInsurancePoliciesPutByIdModel**
> LongTermCareInsurancePolicyWithIdModel longTermCareInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Long Term Care Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Long Term Care Insurance Policy on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermCareInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LongTermCareInsurancePoliciesApi apiInstance = new LongTermCareInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The existing Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to update
    LongTermCareInsurancePolicyModel model = new LongTermCareInsurancePolicyModel(); // LongTermCareInsurancePolicyModel | The Long Term Care Insurance Policy to be updated on a Fact Finder
    try {
      LongTermCareInsurancePolicyWithIdModel result = apiInstance.longTermCareInsurancePoliciesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermCareInsurancePoliciesApi#longTermCareInsurancePoliciesPutByIdModel");
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
| **id** | **Integer**| The existing Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to update | |
| **model** | [**LongTermCareInsurancePolicyModel**](LongTermCareInsurancePolicyModel.md)| The Long Term Care Insurance Policy to be updated on a Fact Finder | |

### Return type

[**LongTermCareInsurancePolicyWithIdModel**](LongTermCareInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Long Term Care Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Long Term Care Insurance Policy. |  -  |
| **404** | Long Term Care Insurance Policy not found. |  -  |

