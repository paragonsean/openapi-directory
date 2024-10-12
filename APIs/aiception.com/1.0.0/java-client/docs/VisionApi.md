# VisionApi

All URIs are relative to *https://aiception.com/api/v2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adultContentPost**](VisionApi.md#adultContentPost) | **POST** /adult_content | Image contains nudity or sexually explicit content? [ image_url -&gt; id ] |
| [**adultContentTaskIdGet**](VisionApi.md#adultContentTaskIdGet) | **GET** /adult_content/{taskId} | Gets the adult_content task [ id -&gt; adult content task ] |
| [**detectObjectPost**](VisionApi.md#detectObjectPost) | **POST** /detect_object | What is that object? [ image_url -&gt; id ] |
| [**detectObjectTaskIdGet**](VisionApi.md#detectObjectTaskIdGet) | **GET** /detect_object/{taskId} | Gets the detect_object task [ id -&gt; detect object task] |
| [**faceAgePost**](VisionApi.md#faceAgePost) | **POST** /face_age | How old is the person in the image? [ image_url -&gt; id ] |
| [**faceAgeTaskIdGet**](VisionApi.md#faceAgeTaskIdGet) | **GET** /face_age/{taskId} | Gets the face_age task [ id -&gt; face age task ] |
| [**facePost**](VisionApi.md#facePost) | **POST** /face | Find all faces in the image [ image_url -&gt; id ] |
| [**faceTaskIdGet**](VisionApi.md#faceTaskIdGet) | **GET** /face/{taskId} | Gets the face task [ id -&gt; face task ] |


<a id="adultContentPost"></a>
# **adultContentPost**
> Task adultContentPost(body)

Image contains nudity or sexually explicit content? [ image_url -&gt; id ]

Creates a new adult_content task that tells the if the image has nudity or sexual content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    AdultContentPostRequest body = new AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
    try {
      Task result = apiInstance.adultContentPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#adultContentPost");
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
| **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Task succesfully created. |  -  |
| **400** | Task could not be created. |  -  |

<a id="adultContentTaskIdGet"></a>
# **adultContentTaskIdGet**
> Task adultContentTaskIdGet(taskId)

Gets the adult_content task [ id -&gt; adult content task ]

Gets the adult_content task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    String taskId = "taskId_example"; // String | An internal id for the task
    try {
      Task result = apiInstance.adultContentTaskIdGet(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#adultContentTaskIdGet");
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
| **taskId** | **String**| An internal id for the task | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contents of the adult_content task. |  -  |
| **404** | The Task does not exists. |  -  |

<a id="detectObjectPost"></a>
# **detectObjectPost**
> Task detectObjectPost(body)

What is that object? [ image_url -&gt; id ]

Creates a new detect object task that recognizes the object in the image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    AdultContentPostRequest body = new AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
    try {
      Task result = apiInstance.detectObjectPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#detectObjectPost");
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
| **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Task succesfully created. |  -  |
| **400** | Task could not be created. |  -  |

<a id="detectObjectTaskIdGet"></a>
# **detectObjectTaskIdGet**
> Task detectObjectTaskIdGet(taskId)

Gets the detect_object task [ id -&gt; detect object task]

Gets the detect_object task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    String taskId = "taskId_example"; // String | An internal id for the task
    try {
      Task result = apiInstance.detectObjectTaskIdGet(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#detectObjectTaskIdGet");
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
| **taskId** | **String**| An internal id for the task | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contents of the detect_object task. |  -  |
| **404** | The Task does not exists. |  -  |

<a id="faceAgePost"></a>
# **faceAgePost**
> Task faceAgePost(body)

How old is the person in the image? [ image_url -&gt; id ]

Creates a new face age task that approximates the age of the person in the image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    AdultContentPostRequest body = new AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
    try {
      Task result = apiInstance.faceAgePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#faceAgePost");
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
| **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Task succesfully created. |  -  |
| **400** | Task could not be created. |  -  |

<a id="faceAgeTaskIdGet"></a>
# **faceAgeTaskIdGet**
> Task faceAgeTaskIdGet(taskId)

Gets the face_age task [ id -&gt; face age task ]

Gets the face_age task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    String taskId = "taskId_example"; // String | An internal id for the task
    try {
      Task result = apiInstance.faceAgeTaskIdGet(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#faceAgeTaskIdGet");
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
| **taskId** | **String**| An internal id for the task | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contents of the face_age task. |  -  |
| **404** | The Task does not exists. |  -  |

<a id="facePost"></a>
# **facePost**
> Task facePost(body)

Find all faces in the image [ image_url -&gt; id ]

Get a list of all the locations of the faces in the image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    AdultContentPostRequest body = new AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
    try {
      Task result = apiInstance.facePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#facePost");
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
| **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Task succesfully created. |  -  |
| **400** | Task could not be created. |  -  |

<a id="faceTaskIdGet"></a>
# **faceTaskIdGet**
> Task faceTaskIdGet(taskId)

Gets the face task [ id -&gt; face task ]

Gets the face task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiception.com/api/v2.1");
    
    // Configure HTTP basic authorization: UserSecurity
    HttpBasicAuth UserSecurity = (HttpBasicAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setUsername("YOUR USERNAME");
    UserSecurity.setPassword("YOUR PASSWORD");

    VisionApi apiInstance = new VisionApi(defaultClient);
    String taskId = "taskId_example"; // String | An internal id for the task
    try {
      Task result = apiInstance.faceTaskIdGet(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionApi#faceTaskIdGet");
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
| **taskId** | **String**| An internal id for the task | |

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contents of the face task. |  -  |
| **404** | The Task does not exists. |  -  |

