# DefaultApi

All URIs are relative to *https://api.useapi.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountGet**](DefaultApi.md#accountGet) | **GET** /account |  |
| [**jobsBlendPost**](DefaultApi.md#jobsBlendPost) | **POST** /jobs/blend |  |
| [**jobsButtonPost**](DefaultApi.md#jobsButtonPost) | **POST** /jobs/button |  |
| [**jobsCancelGet**](DefaultApi.md#jobsCancelGet) | **GET** /jobs/cancel/ |  |
| [**jobsDescribePost**](DefaultApi.md#jobsDescribePost) | **POST** /jobs/describe |  |
| [**jobsGet**](DefaultApi.md#jobsGet) | **GET** /jobs |  |
| [**jobsGet_0**](DefaultApi.md#jobsGet_0) | **GET** /jobs/ |  |
| [**jobsImaginePost**](DefaultApi.md#jobsImaginePost) | **POST** /jobs/imagine |  |


<a id="accountGet"></a>
# **accountGet**
> AccountResponse accountGet()



Retrieve account information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      AccountResponse result = apiInstance.accountGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountGet");
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

[**AccountResponse**](AccountResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="jobsBlendPost"></a>
# **jobsBlendPost**
> BlendResponse jobsBlendPost(jobsBlendPostRequest)



Submit the Midjourney /blend command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    JobsBlendPostRequest jobsBlendPostRequest = new JobsBlendPostRequest(); // JobsBlendPostRequest | 
    try {
      BlendResponse result = apiInstance.jobsBlendPost(jobsBlendPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsBlendPost");
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
| **jobsBlendPostRequest** | [**JobsBlendPostRequest**](JobsBlendPostRequest.md)|  | |

### Return type

[**BlendResponse**](BlendResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **412** | blendUrls, discord, server or channel value is missing, one of blendUrls values not a valid URL or URL which can not be retrieved |  -  |
| **413** | replyRef or replyUrl is too long |  -  |
| **422** | Unable to find posted message, likely moderated or invalid url |  -  |
| **429** | API query is full and can not accept new jobs/blend requests |  -  |

<a id="jobsButtonPost"></a>
# **jobsButtonPost**
> ButtonResponse jobsButtonPost(jobsButtonPostRequest)



Submit the Midjourney /imagine command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    JobsButtonPostRequest jobsButtonPostRequest = new JobsButtonPostRequest(); // JobsButtonPostRequest | 
    try {
      ButtonResponse result = apiInstance.jobsButtonPost(jobsButtonPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsButtonPost");
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
| **jobsButtonPostRequest** | [**JobsButtonPostRequest**](JobsButtonPostRequest.md)|  | |

### Return type

[**ButtonResponse**](ButtonResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Button not supported or not found in jobid buttons array |  -  |
| **401** | Unauthorized |  -  |
| **404** | Unable to locate jobid |  -  |
| **409** | Upscale button already executed by jobid |  -  |
| **412** | jobid or button value is missing |  -  |
| **413** | replyRef or replyUrl is too long |  -  |
| **429** | API query is full and can not accept new jobs/button requests |  -  |

<a id="jobsCancelGet"></a>
# **jobsCancelGet**
> JobCancelResponse jobsCancelGet(jobid)



Cancel execution of job created by jobs/imagine, jobs/button, jobs/blend or jobs/describe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobid = "jobid_example"; // String | jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe
    try {
      JobCancelResponse result = apiInstance.jobsCancelGet(jobid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsCancelGet");
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
| **jobid** | **String**| jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe | |

### Return type

[**JobCancelResponse**](JobCancelResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Query param jobid not provided |  -  |
| **401** | Unauthorized |  -  |
| **404** | Unable to locate jobid |  -  |

<a id="jobsDescribePost"></a>
# **jobsDescribePost**
> DescribeResponse jobsDescribePost(jobsDescribePostRequest)



Submit the Midjourney /describe command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    JobsDescribePostRequest jobsDescribePostRequest = new JobsDescribePostRequest(); // JobsDescribePostRequest | 
    try {
      DescribeResponse result = apiInstance.jobsDescribePost(jobsDescribePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsDescribePost");
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
| **jobsDescribePostRequest** | [**JobsDescribePostRequest**](JobsDescribePostRequest.md)|  | |

### Return type

[**DescribeResponse**](DescribeResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **412** | describeUrl, discord, server or channel value is missing, describeUrl value not a valid URL or URL which can not be retrieved |  -  |
| **413** | replyRef or replyUrl is too long |  -  |
| **422** | Unable to find posted message, likely moderated or invalid url |  -  |
| **429** | API query is full and can not accept new jobs/blend requests |  -  |

<a id="jobsGet"></a>
# **jobsGet**
> List&lt;String&gt; jobsGet()



Get list of currently executing jobs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<String> result = apiInstance.jobsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsGet");
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

**List&lt;String&gt;**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="jobsGet_0"></a>
# **jobsGet_0**
> JobResponse jobsGet_0(jobid)



Retrieve status and results of jobs/imagine, jobs/button, jobs/blend or jobs/describe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobid = "jobid_example"; // String | jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe
    try {
      JobResponse result = apiInstance.jobsGet_0(jobid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsGet_0");
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
| **jobid** | **String**| jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe | |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Query param jobid not provided |  -  |
| **401** | Unauthorized |  -  |
| **404** | Unable to locate jobid |  -  |

<a id="jobsImaginePost"></a>
# **jobsImaginePost**
> ImagineResponse jobsImaginePost(jobsImaginePostRequest)



Submit the Midjourney /imagine command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.useapi.net/v1");
    
    // Configure HTTP bearer authorization: apiToken
    HttpBearerAuth apiToken = (HttpBearerAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    JobsImaginePostRequest jobsImaginePostRequest = new JobsImaginePostRequest(); // JobsImaginePostRequest | 
    try {
      ImagineResponse result = apiInstance.jobsImaginePost(jobsImaginePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsImaginePost");
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
| **jobsImaginePostRequest** | [**JobsImaginePostRequest**](JobsImaginePostRequest.md)|  | |

### Return type

[**ImagineResponse**](ImagineResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **412** | prompt, discord, server or channel value is missing |  -  |
| **413** | prompt, replyRef or replyUrl is too long |  -  |
| **422** | Unable to find posted message, likely moderated or invalid prompt |  -  |
| **429** | API query is full and can not accept new jobs/imagine requests |  -  |

