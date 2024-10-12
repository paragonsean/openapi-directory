# CompanySettingsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companySettingsGet**](CompanySettingsApi.md#companySettingsGet) | **GET** /v1/companySettings | Returns a list of company settings. Supports OData querying protocol.  Filtering is forbidden. |


<a id="companySettingsGet"></a>
# **companySettingsGet**
> PageResultCompanySettingDto companySettingsGet()

Returns a list of company settings. Supports OData querying protocol.  Filtering is forbidden.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanySettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CompanySettingsApi apiInstance = new CompanySettingsApi(defaultClient);
    try {
      PageResultCompanySettingDto result = apiInstance.companySettingsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanySettingsApi#companySettingsGet");
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

[**PageResultCompanySettingDto**](PageResultCompanySettingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

