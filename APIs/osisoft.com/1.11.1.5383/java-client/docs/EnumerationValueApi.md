# EnumerationValueApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enumerationValueDeleteEnumerationValue**](EnumerationValueApi.md#enumerationValueDeleteEnumerationValue) | **DELETE** /enumerationvalues/{webId} | Delete an enumeration value from an enumeration set. |
| [**enumerationValueGet**](EnumerationValueApi.md#enumerationValueGet) | **GET** /enumerationvalues/{webId} | Retrieve an enumeration value mapping |
| [**enumerationValueGetByPath**](EnumerationValueApi.md#enumerationValueGetByPath) | **GET** /enumerationvalues | Retrieve an enumeration value by path. |
| [**enumerationValueUpdateEnumerationValue**](EnumerationValueApi.md#enumerationValueUpdateEnumerationValue) | **PATCH** /enumerationvalues/{webId} | Update an enumeration value by replacing items in its definition. |


<a id="enumerationValueDeleteEnumerationValue"></a>
# **enumerationValueDeleteEnumerationValue**
> enumerationValueDeleteEnumerationValue(webId)

Delete an enumeration value from an enumeration set.

Deleting a value will remove it from the enumeration set along with any value references within the PI Web API system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumerationValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EnumerationValueApi apiInstance = new EnumerationValueApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the enumeration value.
    try {
      apiInstance.enumerationValueDeleteEnumerationValue(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumerationValueApi#enumerationValueDeleteEnumerationValue");
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
| **webId** | **String**| The ID of the enumeration value. | |

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
| **204** | The enumeration value was deleted. |  -  |

<a id="enumerationValueGet"></a>
# **enumerationValueGet**
> EnumerationValue enumerationValueGet(webId, selectedFields, webIdType)

Retrieve an enumeration value mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumerationValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EnumerationValueApi apiInstance = new EnumerationValueApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the enumeration value.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      EnumerationValue result = apiInstance.enumerationValueGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumerationValueApi#enumerationValueGet");
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
| **webId** | **String**| The ID of the enumeration value. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**EnumerationValue**](EnumerationValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified enumeration value mapping |  -  |

<a id="enumerationValueGetByPath"></a>
# **enumerationValueGetByPath**
> EnumerationValue enumerationValueGetByPath(path, selectedFields, webIdType)

Retrieve an enumeration value by path.

This method returns a enumeration value based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumerationValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EnumerationValueApi apiInstance = new EnumerationValueApi(defaultClient);
    String path = "path_example"; // String | The path to the target enumeration value.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      EnumerationValue result = apiInstance.enumerationValueGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumerationValueApi#enumerationValueGetByPath");
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
| **path** | **String**| The path to the target enumeration value. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**EnumerationValue**](EnumerationValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified enumeration set. |  -  |

<a id="enumerationValueUpdateEnumerationValue"></a>
# **enumerationValueUpdateEnumerationValue**
> enumerationValueUpdateEnumerationValue(webId, enumerationValue)

Update an enumeration value by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumerationValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EnumerationValueApi apiInstance = new EnumerationValueApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the enumeration value to update.
    EnumerationValue enumerationValue = new EnumerationValue(); // EnumerationValue | A partial enumeration value containing the desired changes.
    try {
      apiInstance.enumerationValueUpdateEnumerationValue(webId, enumerationValue);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumerationValueApi#enumerationValueUpdateEnumerationValue");
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
| **webId** | **String**| The ID of the enumeration value to update. | |
| **enumerationValue** | [**EnumerationValue**](EnumerationValue.md)| A partial enumeration value containing the desired changes. | |

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
| **204** | The enumeration set was updated. |  -  |

