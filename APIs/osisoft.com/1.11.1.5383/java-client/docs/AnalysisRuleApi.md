# AnalysisRuleApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analysisRuleCreateAnalysisRule**](AnalysisRuleApi.md#analysisRuleCreateAnalysisRule) | **POST** /analysisrules/{webId}/analysisrules | Create a new Analysis Rule as a child of an existing Analysis Rule. |
| [**analysisRuleDelete**](AnalysisRuleApi.md#analysisRuleDelete) | **DELETE** /analysisrules/{webId} | Delete an Analysis Rule. |
| [**analysisRuleGet**](AnalysisRuleApi.md#analysisRuleGet) | **GET** /analysisrules/{webId} | Retrieve an Analysis Rule. |
| [**analysisRuleGetAnalysisRules**](AnalysisRuleApi.md#analysisRuleGetAnalysisRules) | **GET** /analysisrules/{webId}/analysisrules | Get the child Analysis Rules of the Analysis Rule. |
| [**analysisRuleGetByPath**](AnalysisRuleApi.md#analysisRuleGetByPath) | **GET** /analysisrules | Retrieve an Analysis Rule by path. |
| [**analysisRuleUpdate**](AnalysisRuleApi.md#analysisRuleUpdate) | **PATCH** /analysisrules/{webId} | Update an Analysis Rule by replacing items in its definition. |


<a id="analysisRuleCreateAnalysisRule"></a>
# **analysisRuleCreateAnalysisRule**
> analysisRuleCreateAnalysisRule(webId, analysisRule, webIdType)

Create a new Analysis Rule as a child of an existing Analysis Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRuleApi apiInstance = new AnalysisRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent Analysis Rule, on which to create the child Analysis Rule.
    AnalysisRule analysisRule = new AnalysisRule(); // AnalysisRule | The definition of the new Analysis Rule.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.analysisRuleCreateAnalysisRule(webId, analysisRule, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRuleApi#analysisRuleCreateAnalysisRule");
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
| **webId** | **String**| The ID of the parent Analysis Rule, on which to create the child Analysis Rule. | |
| **analysisRule** | [**AnalysisRule**](AnalysisRule.md)| The definition of the new Analysis Rule. | |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Analysis Rule was created. The response&#39;s Location header is a link to the created Analysis Rule. |  -  |

<a id="analysisRuleDelete"></a>
# **analysisRuleDelete**
> analysisRuleDelete(webId)

Delete an Analysis Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRuleApi apiInstance = new AnalysisRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Analysis Rule.
    try {
      apiInstance.analysisRuleDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRuleApi#analysisRuleDelete");
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
| **webId** | **String**| The ID of the Analysis Rule. | |

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
| **204** | The Analysis Rule was deleted. |  -  |

<a id="analysisRuleGet"></a>
# **analysisRuleGet**
> AnalysisRule analysisRuleGet(webId, selectedFields, webIdType)

Retrieve an Analysis Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRuleApi apiInstance = new AnalysisRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Analysis Rule.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AnalysisRule result = apiInstance.analysisRuleGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRuleApi#analysisRuleGet");
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
| **webId** | **String**| The ID of the Analysis Rule. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AnalysisRule**](AnalysisRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Analysis Rule. |  -  |

<a id="analysisRuleGetAnalysisRules"></a>
# **analysisRuleGetAnalysisRules**
> ItemsAnalysisRule analysisRuleGetAnalysisRules(webId, maxCount, nameFilter, searchFullHierarchy, selectedFields, sortField, sortOrder, startIndex, webIdType)

Get the child Analysis Rules of the Analysis Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRuleApi apiInstance = new AnalysisRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent Analysis Rule.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding Analysis Rules. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAnalysisRule result = apiInstance.analysisRuleGetAnalysisRules(webId, maxCount, nameFilter, searchFullHierarchy, selectedFields, sortField, sortOrder, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRuleApi#analysisRuleGetAnalysisRules");
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
| **webId** | **String**| The ID of the parent Analysis Rule. | |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding Analysis Rules. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAnalysisRule**](ItemsAnalysisRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of child Analysis Rules. |  -  |

<a id="analysisRuleGetByPath"></a>
# **analysisRuleGetByPath**
> AnalysisRule analysisRuleGetByPath(path, selectedFields, webIdType)

Retrieve an Analysis Rule by path.

This method returns an Analysis Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRuleApi apiInstance = new AnalysisRuleApi(defaultClient);
    String path = "path_example"; // String | The path to the Analysis Rule.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AnalysisRule result = apiInstance.analysisRuleGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRuleApi#analysisRuleGetByPath");
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
| **path** | **String**| The path to the Analysis Rule. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AnalysisRule**](AnalysisRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Analysis Rule. |  -  |

<a id="analysisRuleUpdate"></a>
# **analysisRuleUpdate**
> analysisRuleUpdate(webId, analysisRule)

Update an Analysis Rule by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRuleApi apiInstance = new AnalysisRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Analysis Rule.
    AnalysisRule analysisRule = new AnalysisRule(); // AnalysisRule | A partial Analysis Rule containing the desired changes.
    try {
      apiInstance.analysisRuleUpdate(webId, analysisRule);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRuleApi#analysisRuleUpdate");
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
| **webId** | **String**| The ID of the Analysis Rule. | |
| **analysisRule** | [**AnalysisRule**](AnalysisRule.md)| A partial Analysis Rule containing the desired changes. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Analysis Rule was updated. |  -  |

