# CompanySetupConfigApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companySetupConfigGet**](CompanySetupConfigApi.md#companySetupConfigGet) | **GET** /v1/companySetupConfig | Returns the company configuration settings. |
| [**companySetupConfigGetCompanyOptions**](CompanySetupConfigApi.md#companySetupConfigGetCompanyOptions) | **GET** /v1/companySetupConfig/getCompanyOptions | Returns the company option setting. |
| [**companySetupConfigGetFinancialYear**](CompanySetupConfigApi.md#companySetupConfigGetFinancialYear) | **GET** /v1/companySetupConfig/getFinancialYear | Returns the financial year. |


<a id="companySetupConfigGet"></a>
# **companySetupConfigGet**
> CompanySetupConfigViewModel companySetupConfigGet()

Returns the company configuration settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanySetupConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CompanySetupConfigApi apiInstance = new CompanySetupConfigApi(defaultClient);
    try {
      CompanySetupConfigViewModel result = apiInstance.companySetupConfigGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanySetupConfigApi#companySetupConfigGet");
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

[**CompanySetupConfigViewModel**](CompanySetupConfigViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="companySetupConfigGetCompanyOptions"></a>
# **companySetupConfigGetCompanyOptions**
> CompanyOptionDto companySetupConfigGetCompanyOptions()

Returns the company option setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanySetupConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CompanySetupConfigApi apiInstance = new CompanySetupConfigApi(defaultClient);
    try {
      CompanyOptionDto result = apiInstance.companySetupConfigGetCompanyOptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanySetupConfigApi#companySetupConfigGetCompanyOptions");
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

[**CompanyOptionDto**](CompanyOptionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="companySetupConfigGetFinancialYear"></a>
# **companySetupConfigGetFinancialYear**
> FinancialYearDto companySetupConfigGetFinancialYear()

Returns the financial year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanySetupConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CompanySetupConfigApi apiInstance = new CompanySetupConfigApi(defaultClient);
    try {
      FinancialYearDto result = apiInstance.companySetupConfigGetFinancialYear();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanySetupConfigApi#companySetupConfigGetFinancialYear");
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

[**FinancialYearDto**](FinancialYearDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

