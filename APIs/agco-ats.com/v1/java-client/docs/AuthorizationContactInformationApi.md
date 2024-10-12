# AuthorizationContactInformationApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorizationContactInformationGet**](AuthorizationContactInformationApi.md#authorizationContactInformationGet) | **GET** /api/v2/AuthorizationContactInformation | Get contact information for authorization codes. |
| [**authorizationContactInformationPost**](AuthorizationContactInformationApi.md#authorizationContactInformationPost) | **POST** /api/v2/AuthorizationContactInformation | Add contact information for authorization code. |


<a id="authorizationContactInformationGet"></a>
# **authorizationContactInformationGet**
> APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation authorizationContactInformationGet(limit, offset, authorizationCode, afterDate, beforeDate, dealerCode)

Get contact information for authorization codes.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationContactInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationContactInformationApi apiInstance = new AuthorizationContactInformationApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    String authorizationCode = "authorizationCode_example"; // String | Optional. Search by authorization code.
    OffsetDateTime afterDate = OffsetDateTime.now(); // OffsetDateTime | Optional. Include only data for authorization codes created after a provided date.
    OffsetDateTime beforeDate = OffsetDateTime.now(); // OffsetDateTime | Optional. Include only data for authorization codes created before a provided date.
    String dealerCode = "dealerCode_example"; // String | Optional. Search by dealer code.
    try {
      APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation result = apiInstance.authorizationContactInformationGet(limit, offset, authorizationCode, afterDate, beforeDate, dealerCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationContactInformationApi#authorizationContactInformationGet");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **authorizationCode** | **String**| Optional. Search by authorization code. | [optional] |
| **afterDate** | **OffsetDateTime**| Optional. Include only data for authorization codes created after a provided date. | [optional] |
| **beforeDate** | **OffsetDateTime**| Optional. Include only data for authorization codes created before a provided date. | [optional] |
| **dealerCode** | **String**| Optional. Search by dealer code. | [optional] |

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation**](APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationContactInformationPost"></a>
# **authorizationContactInformationPost**
> Integer authorizationContactInformationPost(authorizationCodesSharedModelsAuthorizationContactInformation)

Add contact information for authorization code.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationContactInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationContactInformationApi apiInstance = new AuthorizationContactInformationApi(defaultClient);
    AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesSharedModelsAuthorizationContactInformation = new AuthorizationCodesSharedModelsAuthorizationContactInformation(); // AuthorizationCodesSharedModelsAuthorizationContactInformation | A contact information.
    try {
      Integer result = apiInstance.authorizationContactInformationPost(authorizationCodesSharedModelsAuthorizationContactInformation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationContactInformationApi#authorizationContactInformationPost");
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
| **authorizationCodesSharedModelsAuthorizationContactInformation** | [**AuthorizationCodesSharedModelsAuthorizationContactInformation**](AuthorizationCodesSharedModelsAuthorizationContactInformation.md)| A contact information. | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

