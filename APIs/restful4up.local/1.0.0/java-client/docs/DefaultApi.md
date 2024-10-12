# DefaultApi

All URIs are relative to *http://restful4up.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applyYaraRules**](DefaultApi.md#applyYaraRules) | **POST** /apply-yara-rules |  |
| [**clean**](DefaultApi.md#clean) | **HEAD** /clean |  |
| [**emulationOutput**](DefaultApi.md#emulationOutput) | **POST** /emulation-output |  |
| [**generatePartialYaraRule**](DefaultApi.md#generatePartialYaraRule) | **POST** /generate-partial-yara-rules |  |
| [**unpack**](DefaultApi.md#unpack) | **POST** /unpack |  |


<a id="applyYaraRules"></a>
# **applyYaraRules**
> ApplyYaraRules200Response applyYaraRules(_file, rules, isUnpackingRequired)



apply given YARA rules to the given executable. (upto 10 rules)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://restful4up.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | file
    List<String> rules = Arrays.asList(); // List<String> | 
    String isUnpackingRequired = "true"; // String | 
    try {
      ApplyYaraRules200Response result = apiInstance.applyYaraRules(_file, rules, isUnpackingRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applyYaraRules");
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
| **_file** | **File**| file | |
| **rules** | [**List&lt;String&gt;**](String.md)|  | |
| **isUnpackingRequired** | **String**|  | [optional] [enum: true, false] |

### Return type

[**ApplyYaraRules200Response**](ApplyYaraRules200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Yara rules |  -  |
| **400** | request error |  -  |
| **500** | server error |  -  |

<a id="clean"></a>
# **clean**
> clean()



clean up the uploaded files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://restful4up.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.clean();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clean");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Ok |  -  |
| **500** | server error |  -  |

<a id="emulationOutput"></a>
# **emulationOutput**
> EmulationOutput200Response emulationOutput(_file)



try to get the emulation output after unpacking the file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://restful4up.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | file
    try {
      EmulationOutput200Response result = apiInstance.emulationOutput(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#emulationOutput");
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
| **_file** | **File**| file | |

### Return type

[**EmulationOutput200Response**](EmulationOutput200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | emulation output after unpacking the file |  -  |
| **400** | request error |  -  |
| **500** | server error |  -  |

<a id="generatePartialYaraRule"></a>
# **generatePartialYaraRule**
> GeneratePartialYaraRule200Response generatePartialYaraRule(_file, isUnpackingRequired, minimumStringLength, stringsToIgnore)



generate partial YARA rules for give executable. (Rule without the condition section)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://restful4up.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | file
    String isUnpackingRequired = "true"; // String | 
    String minimumStringLength = "minimumStringLength_example"; // String | 
    List<String> stringsToIgnore = Arrays.asList(); // List<String> | 
    try {
      GeneratePartialYaraRule200Response result = apiInstance.generatePartialYaraRule(_file, isUnpackingRequired, minimumStringLength, stringsToIgnore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#generatePartialYaraRule");
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
| **_file** | **File**| file | |
| **isUnpackingRequired** | **String**|  | [optional] [enum: true, false] |
| **minimumStringLength** | **String**|  | [optional] |
| **stringsToIgnore** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**GeneratePartialYaraRule200Response**](GeneratePartialYaraRule200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Yara rules |  -  |
| **400** | request error |  -  |
| **500** | server error |  -  |

<a id="unpack"></a>
# **unpack**
> File unpack(_file)



try to unpack the given file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://restful4up.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | file
    try {
      File result = apiInstance.unpack(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#unpack");
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
| **_file** | **File**| file | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **400** | request error |  -  |
| **500** | server error |  -  |

