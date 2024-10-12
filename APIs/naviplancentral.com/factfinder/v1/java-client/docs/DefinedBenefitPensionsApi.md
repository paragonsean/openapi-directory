# DefinedBenefitPensionsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**definedBenefitPensionsDeleteDefinedBenefitPensionById**](DefinedBenefitPensionsApi.md#definedBenefitPensionsDeleteDefinedBenefitPensionById) | **DELETE** /api/DefinedBenefitPensions/{id} |  |
| [**definedBenefitPensionsGetById**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetById) | **GET** /api/DefinedBenefitPensions/{id} |  |
| [**definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid) | **GET** /api/DefinedBenefitPensions |  |
| [**definedBenefitPensionsPostByModel**](DefinedBenefitPensionsApi.md#definedBenefitPensionsPostByModel) | **POST** /api/DefinedBenefitPensions |  |
| [**definedBenefitPensionsPutDefinedBenefitPensionByIdModel**](DefinedBenefitPensionsApi.md#definedBenefitPensionsPutDefinedBenefitPensionByIdModel) | **PUT** /api/DefinedBenefitPensions/{id} |  |


<a id="definedBenefitPensionsDeleteDefinedBenefitPensionById"></a>
# **definedBenefitPensionsDeleteDefinedBenefitPensionById**
> Object definedBenefitPensionsDeleteDefinedBenefitPensionById(id)



Description: The operation removes a Defined Benefit Pension tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Defined Benefit Pension from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    Integer id = 56; // Integer | The Defined Benefit Pension ID used to identify which Defined Benefit Pension to remove
    try {
      Object result = apiInstance.definedBenefitPensionsDeleteDefinedBenefitPensionById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsDeleteDefinedBenefitPensionById");
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
| **id** | **Integer**| The Defined Benefit Pension ID used to identify which Defined Benefit Pension to remove | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Defined Benefit Pension data access. |  -  |
| **403** | Request is restricted for access to Defined Benefit Pension. |  -  |
| **404** | Defined Benefit Pension not found. |  -  |

<a id="definedBenefitPensionsGetById"></a>
# **definedBenefitPensionsGetById**
> DefinedBenefitPensionWithIdModel definedBenefitPensionsGetById(id)



Description: This operation retrieves a single Defined Benefit Pension for the specified Defined Benefit Pension ID.&lt;br /&gt;                Purpose: Provides access to the Defined Benefit Pension including description and start date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Defined Benefit Pension used to retreive the Defined Benefit Pension
    try {
      DefinedBenefitPensionWithIdModel result = apiInstance.definedBenefitPensionsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsGetById");
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
| **id** | **Integer**| The ID of the Defined Benefit Pension used to retreive the Defined Benefit Pension | |

### Return type

[**DefinedBenefitPensionWithIdModel**](DefinedBenefitPensionWithIdModel.md)

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
| **401** | Unauthorized for Defined Benefit Pension data access. |  -  |
| **403** | Request is restricted for access to Defined Benefit Pension. |  -  |
| **404** | Defined Benefit Pension not found. |  -  |

<a id="definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid"></a>
# **definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid**
> DefinedBenefitPensionsModel definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Defined Benefit Pensions for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Defined Benefit Pensions including description and start date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Defined Benefit Pensions
    try {
      DefinedBenefitPensionsModel result = apiInstance.definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Defined Benefit Pensions | |

### Return type

[**DefinedBenefitPensionsModel**](DefinedBenefitPensionsModel.md)

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
| **401** | Unauthorized for Defined Benefit Pension data access. |  -  |
| **403** | Request is restricted for access to Defined Benefit Pension. |  -  |
| **404** | Defined Benefit Pension not found. |  -  |

<a id="definedBenefitPensionsPostByModel"></a>
# **definedBenefitPensionsPostByModel**
> Object definedBenefitPensionsPostByModel(model)



Description: The operation creates a Defined Benefit Pension.&lt;br /&gt;                Purpose: Allows for creation of Defined Benefit Pensions on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    DefinedBenefitPensionModel model = new DefinedBenefitPensionModel(); // DefinedBenefitPensionModel | The Defined Benefit Pension to be added to the Fact Finder
    try {
      Object result = apiInstance.definedBenefitPensionsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsPostByModel");
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
| **model** | [**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)| The Defined Benefit Pension to be added to the Fact Finder | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Defined Benefit Pension data access. |  -  |
| **403** | Request is restricted for access to Defined Benefit Pension. |  -  |
| **404** | Defined Benefit Pension not found. |  -  |

<a id="definedBenefitPensionsPutDefinedBenefitPensionByIdModel"></a>
# **definedBenefitPensionsPutDefinedBenefitPensionByIdModel**
> DefinedBenefitPensionModel definedBenefitPensionsPutDefinedBenefitPensionByIdModel(id, model)



Description: The operation updates a Defined Benefit Pension.&lt;br /&gt;                Purpose: Allows for complete replacement of a Defined Benefit Pension on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    Integer id = 56; // Integer | The existing Defined Benefit Pension ID used to identify which Defined Benefit Pension to update
    DefinedBenefitPensionModel model = new DefinedBenefitPensionModel(); // DefinedBenefitPensionModel | The Defined Benefit Pension to be updated on a Fact Finder
    try {
      DefinedBenefitPensionModel result = apiInstance.definedBenefitPensionsPutDefinedBenefitPensionByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsPutDefinedBenefitPensionByIdModel");
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
| **id** | **Integer**| The existing Defined Benefit Pension ID used to identify which Defined Benefit Pension to update | |
| **model** | [**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)| The Defined Benefit Pension to be updated on a Fact Finder | |

### Return type

[**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)

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
| **401** | Unauthorized for Defined Benefit Pension data access. |  -  |
| **403** | Request is restricted for access to Defined Benefit Pension. |  -  |
| **404** | Defined Benefit Pension not found. |  -  |

