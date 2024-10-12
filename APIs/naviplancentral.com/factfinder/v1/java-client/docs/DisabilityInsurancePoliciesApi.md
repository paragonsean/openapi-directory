# DisabilityInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disabilityInsurancePoliciesDeleteById**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesDeleteById) | **DELETE** /api/DisabilityInsurancePolicies/{id} |  |
| [**disabilityInsurancePoliciesGetById**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesGetById) | **GET** /api/DisabilityInsurancePolicies/{id} |  |
| [**disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/DisabilityInsurancePolicies |  |
| [**disabilityInsurancePoliciesPostByModel**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesPostByModel) | **POST** /api/DisabilityInsurancePolicies |  |
| [**disabilityInsurancePoliciesPutByIdModel**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesPutByIdModel) | **PUT** /api/DisabilityInsurancePolicies/{id} |  |


<a id="disabilityInsurancePoliciesDeleteById"></a>
# **disabilityInsurancePoliciesDeleteById**
> disabilityInsurancePoliciesDeleteById(id)



Description: The operation removes a Disability Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Disability Insurance Policy from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePoliciesApi apiInstance = new DisabilityInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The Disability Insurance Policy ID used to identify which Disability Insurance Policy to remove
    try {
      apiInstance.disabilityInsurancePoliciesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePoliciesApi#disabilityInsurancePoliciesDeleteById");
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
| **id** | **Integer**| The Disability Insurance Policy ID used to identify which Disability Insurance Policy to remove | |

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
| **401** | Unauthorized for Disability Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Disability Insurance Policy. |  -  |
| **404** | Disability Insurance Policy not found. |  -  |

<a id="disabilityInsurancePoliciesGetById"></a>
# **disabilityInsurancePoliciesGetById**
> DisabilityInsurancePolicyWithIdModel disabilityInsurancePoliciesGetById(id)



Description: This operation retrieves a single Disability Insurance Policy for the specified Disability Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePoliciesApi apiInstance = new DisabilityInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Disability Insurance Policy used to retreive the Disability Insurance Policy
    try {
      DisabilityInsurancePolicyWithIdModel result = apiInstance.disabilityInsurancePoliciesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePoliciesApi#disabilityInsurancePoliciesGetById");
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
| **id** | **Integer**| The ID of the Disability Insurance Policy used to retreive the Disability Insurance Policy | |

### Return type

[**DisabilityInsurancePolicyWithIdModel**](DisabilityInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Disability Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Disability Insurance Policy. |  -  |
| **404** | Disability Insurance Policy not found. |  -  |

<a id="disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid"></a>
# **disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid**
> DisabilityInsurancePoliciesModel disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Disability Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policies including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePoliciesApi apiInstance = new DisabilityInsurancePoliciesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Disability Insurance Policies
    try {
      DisabilityInsurancePoliciesModel result = apiInstance.disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePoliciesApi#disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Disability Insurance Policies | |

### Return type

[**DisabilityInsurancePoliciesModel**](DisabilityInsurancePoliciesModel.md)

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
| **401** | Unauthorized for Disability Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Disability Insurance Policy. |  -  |
| **404** | Disability Insurance Policy not found. |  -  |

<a id="disabilityInsurancePoliciesPostByModel"></a>
# **disabilityInsurancePoliciesPostByModel**
> DisabilityInsurancePolicyWithIdModel disabilityInsurancePoliciesPostByModel(model)



Description: The operation creates a Disability Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Disability Insurance Policies on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePoliciesApi apiInstance = new DisabilityInsurancePoliciesApi(defaultClient);
    DisabilityInsurancePolicyModel model = new DisabilityInsurancePolicyModel(); // DisabilityInsurancePolicyModel | The Disability Insurance Policy to be added to the Fact Finder
    try {
      DisabilityInsurancePolicyWithIdModel result = apiInstance.disabilityInsurancePoliciesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePoliciesApi#disabilityInsurancePoliciesPostByModel");
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
| **model** | [**DisabilityInsurancePolicyModel**](DisabilityInsurancePolicyModel.md)| The Disability Insurance Policy to be added to the Fact Finder | |

### Return type

[**DisabilityInsurancePolicyWithIdModel**](DisabilityInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Disability Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Disability Insurance Policy. |  -  |
| **404** | Disability Insurance Policy not found. |  -  |

<a id="disabilityInsurancePoliciesPutByIdModel"></a>
# **disabilityInsurancePoliciesPutByIdModel**
> DisabilityInsurancePolicyWithIdModel disabilityInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Disability Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Disability Insurance Policy on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisabilityInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DisabilityInsurancePoliciesApi apiInstance = new DisabilityInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The existing Disability Insurance Policy ID used to identify which Disability Insurance Policy to update
    DisabilityInsurancePolicyModel model = new DisabilityInsurancePolicyModel(); // DisabilityInsurancePolicyModel | The Disability Insurance Policy to be updated on a Fact Finder
    try {
      DisabilityInsurancePolicyWithIdModel result = apiInstance.disabilityInsurancePoliciesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisabilityInsurancePoliciesApi#disabilityInsurancePoliciesPutByIdModel");
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
| **id** | **Integer**| The existing Disability Insurance Policy ID used to identify which Disability Insurance Policy to update | |
| **model** | [**DisabilityInsurancePolicyModel**](DisabilityInsurancePolicyModel.md)| The Disability Insurance Policy to be updated on a Fact Finder | |

### Return type

[**DisabilityInsurancePolicyWithIdModel**](DisabilityInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Disability Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Disability Insurance Policy. |  -  |
| **404** | Disability Insurance Policy not found. |  -  |

