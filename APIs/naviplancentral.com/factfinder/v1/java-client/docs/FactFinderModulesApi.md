# FactFinderModulesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**factFinderModulesGetByFactfinderid**](FactFinderModulesApi.md#factFinderModulesGetByFactfinderid) | **GET** /api/FactFinders/{factFinderId}/Modules |  |
| [**factFinderModulesGetByFactfinderidId**](FactFinderModulesApi.md#factFinderModulesGetByFactfinderidId) | **GET** /api/FactFinders/{factFinderId}/Modules/{id} |  |
| [**factFinderModulesPutByModelFactfinderidId**](FactFinderModulesApi.md#factFinderModulesPutByModelFactfinderidId) | **PUT** /api/FactFinders/{factFinderId}/Modules/{id} |  |


<a id="factFinderModulesGetByFactfinderid"></a>
# **factFinderModulesGetByFactfinderid**
> FactFinderModulesModel factFinderModulesGetByFactfinderid(factFinderId)



Description: This operation retrieves all Fact Finder Modules for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder Modules including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFinderModulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFinderModulesApi apiInstance = new FactFinderModulesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Fact Finder Modules
    try {
      FactFinderModulesModel result = apiInstance.factFinderModulesGetByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFinderModulesApi#factFinderModulesGetByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Fact Finder Modules | |

### Return type

[**FactFinderModulesModel**](FactFinderModulesModel.md)

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
| **401** | Unauthorized for Fact Finder Module data access. |  -  |
| **404** | Fact Finder Module not found. |  -  |

<a id="factFinderModulesGetByFactfinderidId"></a>
# **factFinderModulesGetByFactfinderidId**
> FactFinderModuleWithIdModel factFinderModulesGetByFactfinderidId(factFinderId, id)



Description: This operation retrieves a single Fact Finder Module for the specified Fact Finder Module ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder Module including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFinderModulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFinderModulesApi apiInstance = new FactFinderModulesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Fact Finder Module
    Integer id = 56; // Integer | The ID of the Fact Finder Module used to retreive the Fact Finder Module
    try {
      FactFinderModuleWithIdModel result = apiInstance.factFinderModulesGetByFactfinderidId(factFinderId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFinderModulesApi#factFinderModulesGetByFactfinderidId");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Fact Finder Module | |
| **id** | **Integer**| The ID of the Fact Finder Module used to retreive the Fact Finder Module | |

### Return type

[**FactFinderModuleWithIdModel**](FactFinderModuleWithIdModel.md)

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
| **401** | Unauthorized for Fact Finder Module data access. |  -  |
| **404** | Fact Finder Module not found. |  -  |

<a id="factFinderModulesPutByModelFactfinderidId"></a>
# **factFinderModulesPutByModelFactfinderidId**
> FactFinderModuleWithIdModel factFinderModulesPutByModelFactfinderidId(factFinderId, id, model)



Description: The operation updates a Fact Finder Module.&lt;br /&gt;                Purpose: Allows for complete replacement of a Fact Finder Module on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFinderModulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFinderModulesApi apiInstance = new FactFinderModulesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to identify the Fact Finder Module to update
    Integer id = 56; // Integer | The existing Fact Finder Module ID used to identify which Fact Finder Module to update
    FactFinderModuleModel model = new FactFinderModuleModel(); // FactFinderModuleModel | The Fact Finder Module to be updated on a Fact Finder
    try {
      FactFinderModuleWithIdModel result = apiInstance.factFinderModulesPutByModelFactfinderidId(factFinderId, id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFinderModulesApi#factFinderModulesPutByModelFactfinderidId");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to identify the Fact Finder Module to update | |
| **id** | **Integer**| The existing Fact Finder Module ID used to identify which Fact Finder Module to update | |
| **model** | [**FactFinderModuleModel**](FactFinderModuleModel.md)| The Fact Finder Module to be updated on a Fact Finder | |

### Return type

[**FactFinderModuleWithIdModel**](FactFinderModuleWithIdModel.md)

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
| **401** | Unauthorized for Fact Finder Module data access. |  -  |
| **404** | Fact Finder Module not found. |  -  |

