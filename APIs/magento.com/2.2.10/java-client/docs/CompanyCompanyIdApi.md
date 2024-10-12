# CompanyCompanyIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCompanyRepositoryV1DeleteByIdDelete**](CompanyCompanyIdApi.md#companyCompanyRepositoryV1DeleteByIdDelete) | **DELETE** /V1/company/{companyId} | company/{companyId} |
| [**companyCompanyRepositoryV1GetGet**](CompanyCompanyIdApi.md#companyCompanyRepositoryV1GetGet) | **GET** /V1/company/{companyId} | company/{companyId} |
| [**companyCompanyRepositoryV1SavePut**](CompanyCompanyIdApi.md#companyCompanyRepositoryV1SavePut) | **PUT** /V1/company/{companyId} | company/{companyId} |


<a id="companyCompanyRepositoryV1DeleteByIdDelete"></a>
# **companyCompanyRepositoryV1DeleteByIdDelete**
> Boolean companyCompanyRepositoryV1DeleteByIdDelete(companyId)

company/{companyId}

Delete a company. Customers belonging to a company are not deleted with this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCompanyIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCompanyIdApi apiInstance = new CompanyCompanyIdApi(defaultClient);
    Integer companyId = 56; // Integer | 
    try {
      Boolean result = apiInstance.companyCompanyRepositoryV1DeleteByIdDelete(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCompanyIdApi#companyCompanyRepositoryV1DeleteByIdDelete");
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
| **companyId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="companyCompanyRepositoryV1GetGet"></a>
# **companyCompanyRepositoryV1GetGet**
> CompanyDataCompanyInterface companyCompanyRepositoryV1GetGet(companyId)

company/{companyId}

Returns company details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCompanyIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCompanyIdApi apiInstance = new CompanyCompanyIdApi(defaultClient);
    Integer companyId = 56; // Integer | 
    try {
      CompanyDataCompanyInterface result = apiInstance.companyCompanyRepositoryV1GetGet(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCompanyIdApi#companyCompanyRepositoryV1GetGet");
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
| **companyId** | **Integer**|  | |

### Return type

[**CompanyDataCompanyInterface**](CompanyDataCompanyInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="companyCompanyRepositoryV1SavePut"></a>
# **companyCompanyRepositoryV1SavePut**
> CompanyDataCompanyInterface companyCompanyRepositoryV1SavePut(companyId, companyCompanyRepositoryV1SavePostRequest)

company/{companyId}

Create or update a company account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCompanyIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCompanyIdApi apiInstance = new CompanyCompanyIdApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    CompanyCompanyRepositoryV1SavePostRequest companyCompanyRepositoryV1SavePostRequest = new CompanyCompanyRepositoryV1SavePostRequest(); // CompanyCompanyRepositoryV1SavePostRequest | 
    try {
      CompanyDataCompanyInterface result = apiInstance.companyCompanyRepositoryV1SavePut(companyId, companyCompanyRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCompanyIdApi#companyCompanyRepositoryV1SavePut");
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
| **companyId** | **String**|  | |
| **companyCompanyRepositoryV1SavePostRequest** | [**CompanyCompanyRepositoryV1SavePostRequest**](CompanyCompanyRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CompanyDataCompanyInterface**](CompanyDataCompanyInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

