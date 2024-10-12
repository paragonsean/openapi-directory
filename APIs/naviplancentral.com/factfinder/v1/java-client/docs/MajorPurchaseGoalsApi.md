# MajorPurchaseGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**majorPurchaseGoalsDeleteById**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsDeleteById) | **DELETE** /api/MajorPurchaseGoals/{id} |  |
| [**majorPurchaseGoalsGetById**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsGetById) | **GET** /api/MajorPurchaseGoals/{id} |  |
| [**majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid) | **GET** /api/MajorPurchaseGoals |  |
| [**majorPurchaseGoalsPostByModel**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsPostByModel) | **POST** /api/MajorPurchaseGoals |  |
| [**majorPurchaseGoalsPutByIdModel**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsPutByIdModel) | **PUT** /api/MajorPurchaseGoals/{id} |  |


<a id="majorPurchaseGoalsDeleteById"></a>
# **majorPurchaseGoalsDeleteById**
> majorPurchaseGoalsDeleteById(id)



Description: The operation removes a Major Purchase tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Major Purchase from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalsApi apiInstance = new MajorPurchaseGoalsApi(defaultClient);
    Integer id = 56; // Integer | The Major Purchase ID used to identify which Major Purchase to remove
    try {
      apiInstance.majorPurchaseGoalsDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalsApi#majorPurchaseGoalsDeleteById");
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
| **id** | **Integer**| The Major Purchase ID used to identify which Major Purchase to remove | |

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
| **401** | Unauthorized for Major Purchase data access. |  -  |
| **403** | Request is restricted for access to Major Purchase. |  -  |
| **404** | Major Purchase not found. |  -  |

<a id="majorPurchaseGoalsGetById"></a>
# **majorPurchaseGoalsGetById**
> MajorPurchaseGoalWithIdModel majorPurchaseGoalsGetById(id)



Description: This operation retrieves a single Major Purchase for the specified Major Purchase ID.&lt;br /&gt;                Purpose: Provides access to the Major Purchase including description and amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalsApi apiInstance = new MajorPurchaseGoalsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Major Purchase used to retreive the Major Purchase
    try {
      MajorPurchaseGoalWithIdModel result = apiInstance.majorPurchaseGoalsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalsApi#majorPurchaseGoalsGetById");
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
| **id** | **Integer**| The ID of the Major Purchase used to retreive the Major Purchase | |

### Return type

[**MajorPurchaseGoalWithIdModel**](MajorPurchaseGoalWithIdModel.md)

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
| **401** | Unauthorized for Major Purchase data access. |  -  |
| **403** | Request is restricted for access to Major Purchase. |  -  |
| **404** | Major Purchase not found. |  -  |

<a id="majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid"></a>
# **majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid**
> MajorPurchaseGoalsModel majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Major Purchases for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Major Purchases including description and amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalsApi apiInstance = new MajorPurchaseGoalsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Major Purchases
    try {
      MajorPurchaseGoalsModel result = apiInstance.majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalsApi#majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Major Purchases | |

### Return type

[**MajorPurchaseGoalsModel**](MajorPurchaseGoalsModel.md)

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
| **401** | Unauthorized for Major Purchase data access. |  -  |
| **403** | Request is restricted for access to Major Purchase. |  -  |
| **404** | Major Purchase not found. |  -  |

<a id="majorPurchaseGoalsPostByModel"></a>
# **majorPurchaseGoalsPostByModel**
> MajorPurchaseGoalWithIdModel majorPurchaseGoalsPostByModel(model)



Description: The operation creates a Major Purchase.&lt;br /&gt;                Purpose: Allows for creation of Major Purchases on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalsApi apiInstance = new MajorPurchaseGoalsApi(defaultClient);
    MajorPurchaseGoalModel model = new MajorPurchaseGoalModel(); // MajorPurchaseGoalModel | The Major Purchase to be added to the Fact Finder
    try {
      MajorPurchaseGoalWithIdModel result = apiInstance.majorPurchaseGoalsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalsApi#majorPurchaseGoalsPostByModel");
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
| **model** | [**MajorPurchaseGoalModel**](MajorPurchaseGoalModel.md)| The Major Purchase to be added to the Fact Finder | |

### Return type

[**MajorPurchaseGoalWithIdModel**](MajorPurchaseGoalWithIdModel.md)

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
| **401** | Unauthorized for Major Purchase data access. |  -  |
| **403** | Request is restricted for access to Major Purchase. |  -  |
| **404** | Major Purchase not found. |  -  |

<a id="majorPurchaseGoalsPutByIdModel"></a>
# **majorPurchaseGoalsPutByIdModel**
> MajorPurchaseGoalWithIdModel majorPurchaseGoalsPutByIdModel(id, model)



Description: The operation updates a Major Purchase.&lt;br /&gt;                Purpose: Allows for complete replacement of a Major Purchase on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MajorPurchaseGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    MajorPurchaseGoalsApi apiInstance = new MajorPurchaseGoalsApi(defaultClient);
    Integer id = 56; // Integer | The existing Major Purchase ID used to identify which Major Purchase to update
    MajorPurchaseGoalModel model = new MajorPurchaseGoalModel(); // MajorPurchaseGoalModel | The Major Purchase to be updated on a Fact Finder
    try {
      MajorPurchaseGoalWithIdModel result = apiInstance.majorPurchaseGoalsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MajorPurchaseGoalsApi#majorPurchaseGoalsPutByIdModel");
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
| **id** | **Integer**| The existing Major Purchase ID used to identify which Major Purchase to update | |
| **model** | [**MajorPurchaseGoalModel**](MajorPurchaseGoalModel.md)| The Major Purchase to be updated on a Fact Finder | |

### Return type

[**MajorPurchaseGoalWithIdModel**](MajorPurchaseGoalWithIdModel.md)

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
| **401** | Unauthorized for Major Purchase data access. |  -  |
| **403** | Request is restricted for access to Major Purchase. |  -  |
| **404** | Major Purchase not found. |  -  |

