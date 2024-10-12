# PasswordApi

All URIs are relative to *http://passwordutility.net:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**passwordGenerate**](PasswordApi.md#passwordGenerate) | **POST** /api/password/generate |  |
| [**passwordValidate**](PasswordApi.md#passwordValidate) | **POST** /api/password/validate |  |


<a id="passwordGenerate"></a>
# **passwordGenerate**
> Object passwordGenerate(length, upperCase, digits, specialCharacters)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://passwordutility.net:80");

    PasswordApi apiInstance = new PasswordApi(defaultClient);
    Integer length = 56; // Integer | 
    Boolean upperCase = true; // Boolean | 
    Boolean digits = true; // Boolean | 
    Boolean specialCharacters = true; // Boolean | 
    try {
      Object result = apiInstance.passwordGenerate(length, upperCase, digits, specialCharacters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordApi#passwordGenerate");
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
| **length** | **Integer**|  | |
| **upperCase** | **Boolean**|  | [optional] |
| **digits** | **Boolean**|  | [optional] |
| **specialCharacters** | **Boolean**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="passwordValidate"></a>
# **passwordValidate**
> Object passwordValidate(password)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://passwordutility.net:80");

    PasswordApi apiInstance = new PasswordApi(defaultClient);
    String password = "password_example"; // String | 
    try {
      Object result = apiInstance.passwordValidate(password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordApi#passwordValidate");
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
| **password** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

