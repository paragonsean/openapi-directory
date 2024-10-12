# CategoriesApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCategory**](CategoriesApi.md#getCategory) | **GET** /providernetworks/{providernetworkUID}/categories/{categoryUID} | Get a Category by UID |
| [**listCategories**](CategoriesApi.md#listCategories) | **GET** /providernetworks/{providernetworkUID}/categories | Lists all categories |


<a id="getCategory"></a>
# **getCategory**
> CategoryJO getCategory(providernetworkUID, categoryUID, expand)

Get a Category by UID

Search for categorie.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String providernetworkUID = "providernetworkUID_example"; // String | Provider Network UID
    String categoryUID = "categoryUID_example"; // String | 
    String expand = "expand_example"; // String | 
    try {
      CategoryJO result = apiInstance.getCategory(providernetworkUID, categoryUID, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getCategory");
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
| **providernetworkUID** | **String**| Provider Network UID | |
| **categoryUID** | **String**|  | |
| **expand** | **String**|  | [optional] |

### Return type

[**CategoryJO**](CategoryJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request One or more parameters have invalid values. |  -  |
| **403** | Forbidden Provider is not allowed to use this interface. |  -  |

<a id="listCategories"></a>
# **listCategories**
> CategoryJO listCategories(providernetworkUID, expand)

Lists all categories

Search for categorie.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String providernetworkUID = "providernetworkUID_example"; // String | 
    String expand = "expand_example"; // String | 
    try {
      CategoryJO result = apiInstance.listCategories(providernetworkUID, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#listCategories");
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
| **providernetworkUID** | **String**|  | |
| **expand** | **String**|  | [optional] |

### Return type

[**CategoryJO**](CategoryJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request One or more parameters have invalid values. |  -  |
| **403** | Forbidden Provider is not allowed to use this interface. |  -  |

