# CriticalIllnessInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**criticalIllnessInsurancePoliciesDeleteById**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesDeleteById) | **DELETE** /api/CriticalIllnessInsurancePolicies/{id} |  |
| [**criticalIllnessInsurancePoliciesGetById**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesGetById) | **GET** /api/CriticalIllnessInsurancePolicies/{id} |  |
| [**criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/CriticalIllnessInsurancePolicies |  |
| [**criticalIllnessInsurancePoliciesPostByModel**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesPostByModel) | **POST** /api/CriticalIllnessInsurancePolicies |  |
| [**criticalIllnessInsurancePoliciesPutByIdModel**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesPutByIdModel) | **PUT** /api/CriticalIllnessInsurancePolicies/{id} |  |


<a id="criticalIllnessInsurancePoliciesDeleteById"></a>
# **criticalIllnessInsurancePoliciesDeleteById**
> criticalIllnessInsurancePoliciesDeleteById(id)



Description: The operation removes a Critical Illness Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Critical Illness Insurance Policy from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePoliciesApi apiInstance = new CriticalIllnessInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to remove
    try {
      apiInstance.criticalIllnessInsurancePoliciesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePoliciesApi#criticalIllnessInsurancePoliciesDeleteById");
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
| **id** | **Integer**| The Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to remove | |

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
| **401** | Unauthorized for Critical Illness Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Critical Illness Insurance Policy. |  -  |
| **404** | Critical Illness Insurance Policy not found. |  -  |

<a id="criticalIllnessInsurancePoliciesGetById"></a>
# **criticalIllnessInsurancePoliciesGetById**
> CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePoliciesGetById(id)



Description: This operation retrieves a single Critical Illness Insurance Policy for the specified Critical Illness Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePoliciesApi apiInstance = new CriticalIllnessInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Critical Illness Insurance Policy used to retreive the Critical Illness Insurance Policy
    try {
      CriticalIllnessInsurancePolicyWithIdModel result = apiInstance.criticalIllnessInsurancePoliciesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePoliciesApi#criticalIllnessInsurancePoliciesGetById");
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
| **id** | **Integer**| The ID of the Critical Illness Insurance Policy used to retreive the Critical Illness Insurance Policy | |

### Return type

[**CriticalIllnessInsurancePolicyWithIdModel**](CriticalIllnessInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Critical Illness Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Critical Illness Insurance Policy. |  -  |
| **404** | Critical Illness Insurance Policy not found. |  -  |

<a id="criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid"></a>
# **criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid**
> CriticalIllnessInsurancePoliciesModel criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Critical Illness Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policies including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePoliciesApi apiInstance = new CriticalIllnessInsurancePoliciesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Critical Illness Insurance Policies
    try {
      CriticalIllnessInsurancePoliciesModel result = apiInstance.criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePoliciesApi#criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Critical Illness Insurance Policies | |

### Return type

[**CriticalIllnessInsurancePoliciesModel**](CriticalIllnessInsurancePoliciesModel.md)

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
| **401** | Unauthorized for Critical Illness Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Critical Illness Insurance Policy. |  -  |
| **404** | Critical Illness Insurance Policy not found. |  -  |

<a id="criticalIllnessInsurancePoliciesPostByModel"></a>
# **criticalIllnessInsurancePoliciesPostByModel**
> CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePoliciesPostByModel(model)



Description: The operation creates a Critical Illness Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Critical Illness Insurance Policies on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePoliciesApi apiInstance = new CriticalIllnessInsurancePoliciesApi(defaultClient);
    CriticalIllnessInsurancePolicyModel model = new CriticalIllnessInsurancePolicyModel(); // CriticalIllnessInsurancePolicyModel | The Critical Illness Insurance Policy to be added to the Fact Finder
    try {
      CriticalIllnessInsurancePolicyWithIdModel result = apiInstance.criticalIllnessInsurancePoliciesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePoliciesApi#criticalIllnessInsurancePoliciesPostByModel");
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
| **model** | [**CriticalIllnessInsurancePolicyModel**](CriticalIllnessInsurancePolicyModel.md)| The Critical Illness Insurance Policy to be added to the Fact Finder | |

### Return type

[**CriticalIllnessInsurancePolicyWithIdModel**](CriticalIllnessInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Critical Illness Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Critical Illness Insurance Policy. |  -  |
| **404** | Critical Illness Insurance Policy not found. |  -  |

<a id="criticalIllnessInsurancePoliciesPutByIdModel"></a>
# **criticalIllnessInsurancePoliciesPutByIdModel**
> CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Critical Illness Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Critical Illness Insurance Policy on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CriticalIllnessInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    CriticalIllnessInsurancePoliciesApi apiInstance = new CriticalIllnessInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The existing Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to update
    CriticalIllnessInsurancePolicyModel model = new CriticalIllnessInsurancePolicyModel(); // CriticalIllnessInsurancePolicyModel | The Critical Illness Insurance Policy to be updated on a Fact Finder
    try {
      CriticalIllnessInsurancePolicyWithIdModel result = apiInstance.criticalIllnessInsurancePoliciesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CriticalIllnessInsurancePoliciesApi#criticalIllnessInsurancePoliciesPutByIdModel");
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
| **id** | **Integer**| The existing Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to update | |
| **model** | [**CriticalIllnessInsurancePolicyModel**](CriticalIllnessInsurancePolicyModel.md)| The Critical Illness Insurance Policy to be updated on a Fact Finder | |

### Return type

[**CriticalIllnessInsurancePolicyWithIdModel**](CriticalIllnessInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Critical Illness Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Critical Illness Insurance Policy. |  -  |
| **404** | Critical Illness Insurance Policy not found. |  -  |

