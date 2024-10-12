# ApplicantApi

All URIs are relative to *https://api.slideroom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicantDeleteAttributesV2**](ApplicantApi.md#applicantDeleteAttributesV2) | **DELETE** /api/v2/applicant/attributes | Deletes a custom attribute for an applicant. |
| [**applicantGetAttributeNamesV2**](ApplicantApi.md#applicantGetAttributeNamesV2) | **GET** /api/v2/applicant/attributes/names | Gets the custom applicant attributes used by the organization. |
| [**applicantGetAttributesV2**](ApplicantApi.md#applicantGetAttributesV2) | **GET** /api/v2/applicant/attributes | Gets the custom attributes for an applicant. |
| [**applicantPostAttributesV2**](ApplicantApi.md#applicantPostAttributesV2) | **POST** /api/v2/applicant/attributes | Updates the custom attributes for an applicant. |


<a id="applicantDeleteAttributesV2"></a>
# **applicantDeleteAttributesV2**
> String applicantDeleteAttributesV2(email, name, pool, commonAppYear)

Deletes a custom attribute for an applicant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicantApi apiInstance = new ApplicantApi(defaultClient);
    String email = "email_example"; // String | The email address of the applicant.
    String name = "name_example"; // String | The name of the attribute to be deleted.
    String pool = "Standard"; // String | 
    Integer commonAppYear = 56; // Integer | 
    try {
      String result = apiInstance.applicantDeleteAttributesV2(email, name, pool, commonAppYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicantApi#applicantDeleteAttributesV2");
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
| **email** | **String**| The email address of the applicant. | |
| **name** | **String**| The name of the attribute to be deleted. | |
| **pool** | **String**|  | [optional] [enum: Standard, CommonAppSDS] |
| **commonAppYear** | **Integer**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicantGetAttributeNamesV2"></a>
# **applicantGetAttributeNamesV2**
> List&lt;String&gt; applicantGetAttributeNamesV2()

Gets the custom applicant attributes used by the organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicantApi apiInstance = new ApplicantApi(defaultClient);
    try {
      List<String> result = apiInstance.applicantGetAttributeNamesV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicantApi#applicantGetAttributeNamesV2");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicantGetAttributesV2"></a>
# **applicantGetAttributesV2**
> Map&lt;String, String&gt; applicantGetAttributesV2(email, pool, commonAppYear)

Gets the custom attributes for an applicant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicantApi apiInstance = new ApplicantApi(defaultClient);
    String email = "email_example"; // String | The email address of the applicant.
    String pool = "Standard"; // String | 
    Integer commonAppYear = 56; // Integer | 
    try {
      Map<String, String> result = apiInstance.applicantGetAttributesV2(email, pool, commonAppYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicantApi#applicantGetAttributesV2");
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
| **email** | **String**| The email address of the applicant. | |
| **pool** | **String**|  | [optional] [enum: Standard, CommonAppSDS] |
| **commonAppYear** | **Integer**|  | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicantPostAttributesV2"></a>
# **applicantPostAttributesV2**
> String applicantPostAttributesV2(email, data, pool, commonAppYear)

Updates the custom attributes for an applicant.

This method only adds or updates attributes. Null values will be updated as nulls, but not deleted. API Import is available in the Advanced Plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicantApi apiInstance = new ApplicantApi(defaultClient);
    String email = "email_example"; // String | The email address of the applicant.
    Map<String, String> data = new HashMap(); // Map<String, String> | The name/value pairs of the attributes.
    String pool = "Standard"; // String | 
    Integer commonAppYear = 56; // Integer | 
    try {
      String result = apiInstance.applicantPostAttributesV2(email, data, pool, commonAppYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicantApi#applicantPostAttributesV2");
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
| **email** | **String**| The email address of the applicant. | |
| **data** | [**Map&lt;String, String&gt;**](String.md)| The name/value pairs of the attributes. | |
| **pool** | **String**|  | [optional] [enum: Standard, CommonAppSDS] |
| **commonAppYear** | **Integer**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

