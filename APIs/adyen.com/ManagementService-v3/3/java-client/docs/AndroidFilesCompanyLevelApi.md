# AndroidFilesCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompaniesCompanyIdAndroidApps**](AndroidFilesCompanyLevelApi.md#getCompaniesCompanyIdAndroidApps) | **GET** /companies/{companyId}/androidApps | Get a list of Android apps |
| [**getCompaniesCompanyIdAndroidAppsId**](AndroidFilesCompanyLevelApi.md#getCompaniesCompanyIdAndroidAppsId) | **GET** /companies/{companyId}/androidApps/{id} | Get Android app |
| [**getCompaniesCompanyIdAndroidCertificates**](AndroidFilesCompanyLevelApi.md#getCompaniesCompanyIdAndroidCertificates) | **GET** /companies/{companyId}/androidCertificates | Get a list of Android certificates |
| [**postCompaniesCompanyIdAndroidApps**](AndroidFilesCompanyLevelApi.md#postCompaniesCompanyIdAndroidApps) | **POST** /companies/{companyId}/androidApps | Upload Android App |


<a id="getCompaniesCompanyIdAndroidApps"></a>
# **getCompaniesCompanyIdAndroidApps**
> AndroidAppsResponse getCompaniesCompanyIdAndroidApps(companyId, pageNumber, pageSize, packageName, versionCode)

Get a list of Android apps

Returns a list of the Android apps that are available for the company identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write * Management API—Terminal actions read * Management API—Terminal actions read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AndroidFilesCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AndroidFilesCompanyLevelApi apiInstance = new AndroidFilesCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    Integer pageNumber = 56; // Integer | The number of the page to fetch.
    Integer pageSize = 56; // Integer | The number of items to have on a page, maximum 100. The default is 20 items on a page.
    String packageName = "packageName_example"; // String | The package name that uniquely identifies the Android app.
    Integer versionCode = 56; // Integer | The version number of the app.
    try {
      AndroidAppsResponse result = apiInstance.getCompaniesCompanyIdAndroidApps(companyId, pageNumber, pageSize, packageName, versionCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AndroidFilesCompanyLevelApi#getCompaniesCompanyIdAndroidApps");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **pageNumber** | **Integer**| The number of the page to fetch. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] |
| **packageName** | **String**| The package name that uniquely identifies the Android app. | [optional] |
| **versionCode** | **Integer**| The version number of the app. | [optional] |

### Return type

[**AndroidAppsResponse**](AndroidAppsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdAndroidAppsId"></a>
# **getCompaniesCompanyIdAndroidAppsId**
> AndroidApp getCompaniesCompanyIdAndroidAppsId(companyId, id)

Get Android app

Returns the details of the Android app identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AndroidFilesCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AndroidFilesCompanyLevelApi apiInstance = new AndroidFilesCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String id = "id_example"; // String | The unique identifier of the app.
    try {
      AndroidApp result = apiInstance.getCompaniesCompanyIdAndroidAppsId(companyId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AndroidFilesCompanyLevelApi#getCompaniesCompanyIdAndroidAppsId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **id** | **String**| The unique identifier of the app. | |

### Return type

[**AndroidApp**](AndroidApp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdAndroidCertificates"></a>
# **getCompaniesCompanyIdAndroidCertificates**
> AndroidCertificatesResponse getCompaniesCompanyIdAndroidCertificates(companyId, pageNumber, pageSize, certificateName)

Get a list of Android certificates

Returns a list of the Android certificates that are available for the company identified in the path. Typically, these certificates enable running apps on Android payment terminals. The certifcates in the list have been uploaded to Adyen and can be installed or uninstalled on Android terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write * Management API—Terminal actions read * Management API—Terminal actions read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AndroidFilesCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AndroidFilesCompanyLevelApi apiInstance = new AndroidFilesCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    Integer pageNumber = 56; // Integer | The number of the page to fetch.
    Integer pageSize = 56; // Integer | The number of items to have on a page, maximum 100. The default is 20 items on a page.
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    try {
      AndroidCertificatesResponse result = apiInstance.getCompaniesCompanyIdAndroidCertificates(companyId, pageNumber, pageSize, certificateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AndroidFilesCompanyLevelApi#getCompaniesCompanyIdAndroidCertificates");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **pageNumber** | **Integer**| The number of the page to fetch. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] |
| **certificateName** | **String**| The name of the certificate. | [optional] |

### Return type

[**AndroidCertificatesResponse**](AndroidCertificatesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdAndroidApps"></a>
# **postCompaniesCompanyIdAndroidApps**
> UploadAndroidAppResponse postCompaniesCompanyIdAndroidApps(companyId)

Upload Android App

Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read and write  &gt;By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept full responsibility and liability for any consequences of uploading, installing, or running any such applications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AndroidFilesCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AndroidFilesCompanyLevelApi apiInstance = new AndroidFilesCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    try {
      UploadAndroidAppResponse result = apiInstance.postCompaniesCompanyIdAndroidApps(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AndroidFilesCompanyLevelApi#postCompaniesCompanyIdAndroidApps");
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
| **companyId** | **String**| The unique identifier of the company account. | |

### Return type

[**UploadAndroidAppResponse**](UploadAndroidAppResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

