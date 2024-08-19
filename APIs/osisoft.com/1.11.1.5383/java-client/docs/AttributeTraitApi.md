# AttributeTraitApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attributeTraitGet**](AttributeTraitApi.md#attributeTraitGet) | **GET** /attributetraits/{name} | Retrieve an attribute trait. |
| [**attributeTraitGetByCategory**](AttributeTraitApi.md#attributeTraitGetByCategory) | **GET** /attributetraits | Retrieve all attribute traits of the specified category/categories. |


<a id="attributeTraitGet"></a>
# **attributeTraitGet**
> AttributeTrait attributeTraitGet(name, selectedFields)

Retrieve an attribute trait.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTraitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTraitApi apiInstance = new AttributeTraitApi(defaultClient);
    String name = "name_example"; // String | The name or abbreviation of the attribute trait.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    try {
      AttributeTrait result = apiInstance.attributeTraitGet(name, selectedFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTraitApi#attributeTraitGet");
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
| **name** | **String**| The name or abbreviation of the attribute trait. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |

### Return type

[**AttributeTrait**](AttributeTrait.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested attribute trait. |  -  |

<a id="attributeTraitGetByCategory"></a>
# **attributeTraitGetByCategory**
> ItemsAttributeTrait attributeTraitGetByCategory(category, selectedFields)

Retrieve all attribute traits of the specified category/categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTraitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTraitApi apiInstance = new AttributeTraitApi(defaultClient);
    List<String> category = Arrays.asList(); // List<String> | The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \"all\", then all attribute traits of all categories will be returned.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    try {
      ItemsAttributeTrait result = apiInstance.attributeTraitGetByCategory(category, selectedFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTraitApi#attributeTraitGetByCategory");
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
| **category** | [**List&lt;String&gt;**](String.md)| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |

### Return type

[**ItemsAttributeTrait**](ItemsAttributeTrait.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of attribute traits. |  -  |

