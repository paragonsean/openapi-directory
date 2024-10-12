# AppPkgmApi

All URIs are relative to *http://etsi.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appDGET**](AppPkgmApi.md#appDGET) | **GET** /onboarded_app_packages/{appDId}/appd | Reads the content of the AppD of on-boarded individual application package resources. |
| [**appDIdGET**](AppPkgmApi.md#appDIdGET) | **GET** /onboarded_app_packages/{appDId}/package_content | Fetch the onboarded application package content identified by appPkgId or appDId. |
| [**appDIdPUT**](AppPkgmApi.md#appDIdPUT) | **PUT** /onboarded_app_packages/{appDId}/package_content | Uploads the content of application package. |
| [**appPackageDELETE**](AppPkgmApi.md#appPackageDELETE) | **DELETE** /app_packages/{appPkgId} | Deletes an individual application package resources |
| [**appPackageGET**](AppPkgmApi.md#appPackageGET) | **GET** /app_packages/{appPkgId} | Queries the information related to individual application package resources |
| [**appPackagePATCH**](AppPkgmApi.md#appPackagePATCH) | **PATCH** /app_packages/{appPkgId} | Updates the operational state of an individual application package resource |
| [**appPackagesGET**](AppPkgmApi.md#appPackagesGET) | **GET** /app_packages | Queries information relating to on-boarded application packages in the MEO |
| [**appPackagesPOST**](AppPkgmApi.md#appPackagesPOST) | **POST** /app_packages | Create a resource for on-boarding an application package to a MEO |
| [**appPkgGET**](AppPkgmApi.md#appPkgGET) | **GET** /app_packages/{appPkgId}/package_content | Fetch the onboarded application package content identified by appPkgId or appDId. |
| [**appPkgIdGET**](AppPkgmApi.md#appPkgIdGET) | **GET** /app_packages/{appPkgId}/appd | Reads the content of the AppD of on-boarded individual application package resources. |
| [**appPkgPUT**](AppPkgmApi.md#appPkgPUT) | **PUT** /app_packages/{appPkgId}/package_content | Uploads the content of application package. |
| [**individualSubscriptionDELETE**](AppPkgmApi.md#individualSubscriptionDELETE) | **DELETE** /subscriptions/{subscriptionId} | Deletes the individual subscription to notifications about application package changes in MEO. |
| [**individualSubscriptionGET**](AppPkgmApi.md#individualSubscriptionGET) | **GET** /subscriptions/{subscriptionId} | Used to represent an individual subscription to notifications about application package changes. |
| [**subscriptionsGET**](AppPkgmApi.md#subscriptionsGET) | **GET** /subscriptions | used to retrieve the information of subscriptions to individual application package resource in MEO |
| [**subscriptionsPOST**](AppPkgmApi.md#subscriptionsPOST) | **POST** /subscriptions | Subscribe to notifications about on-boarding an application package |


<a id="appDGET"></a>
# **appDGET**
> AppD appDGET(appDId, filter, allFields, fields, excludeFields, excludeDefault)

Reads the content of the AppD of on-boarded individual application package resources.

Reads the content of the AppD of on-boarded individual application package resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appDId = "appDId_example"; // String | Identifier of an application descriptor
    String filter = "filter_example"; // String | Attribute-based filtering parameters according to ETSI GS MEC 009
    String allFields = "allFields_example"; // String | Include all complex attributes in the response.
    String fields = "fields_example"; // String | Complex attributes of AppPkgInfo to be included into the response
    String excludeFields = "excludeFields_example"; // String | Complex attributes of AppPkgInfo to be excluded from the response.
    String excludeDefault = "excludeDefault_example"; // String | Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    try {
      AppD result = apiInstance.appDGET(appDId, filter, allFields, fields, excludeFields, excludeDefault);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appDGET");
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
| **appDId** | **String**| Identifier of an application descriptor | |
| **filter** | **String**| Attribute-based filtering parameters according to ETSI GS MEC 009 | [optional] |
| **allFields** | **String**| Include all complex attributes in the response. | [optional] |
| **fields** | **String**| Complex attributes of AppPkgInfo to be included into the response | [optional] |
| **excludeFields** | **String**| Complex attributes of AppPkgInfo to be excluded from the response. | [optional] |
| **excludeDefault** | **String**| Indicates to exclude the following complex attributes of AppPkgInfo from the response. | [optional] |

### Return type

[**AppD**](AppD.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of the AppD is returned. |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appDIdGET"></a>
# **appDIdGET**
> appDIdGET(appDId)

Fetch the onboarded application package content identified by appPkgId or appDId.

Fetch the onboarded application package content identified by appPkgId or appDId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appDId = "appDId_example"; // String | Identifier of an application descriptor
    try {
      apiInstance.appDIdGET(appDId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appDIdGET");
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
| **appDId** | **String**| Identifier of an application descriptor | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payload body shall contain a copy of the file representing the AppD or a ZIP file that contains the file or multiple files representing the AppD. |  -  |
| **206** | Partial content |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **416** | Range Not Satisfiable . |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appDIdPUT"></a>
# **appDIdPUT**
> appDIdPUT(appDId, body)

Uploads the content of application package.

Uploads the content of application package.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appDId = "appDId_example"; // String | Identifier of an application descriptor
    File body = new File("/path/to/file"); // File | 
    try {
      apiInstance.appDIdPUT(appDId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appDIdPUT");
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
| **appDId** | **String**| Identifier of an application descriptor | |
| **body** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/zip
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The application package has been accepted for uploading, but the processing has not been completed. |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **409** | Conflict : The operation cannot be executed currently, due to a conflict with the state of the resource |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPackageDELETE"></a>
# **appPackageDELETE**
> appPackageDELETE(appPkgId)

Deletes an individual application package resources

Deletes an individual application package resources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appPkgId = "appPkgId_example"; // String | Identifier of an individual application package resource
    try {
      apiInstance.appPackageDELETE(appPkgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPackageDELETE");
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
| **appPkgId** | **String**| Identifier of an individual application package resource | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPackageGET"></a>
# **appPackageGET**
> AppPkgInfo appPackageGET(appPkgId)

Queries the information related to individual application package resources

Queries the information related to individual application package resources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appPkgId = "appPkgId_example"; // String | Identifier of an individual application package resource
    try {
      AppPkgInfo result = apiInstance.appPackageGET(appPkgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPackageGET");
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
| **appPkgId** | **String**| Identifier of an individual application package resource | |

### Return type

[**AppPkgInfo**](AppPkgInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains a representation of the application package resource |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPackagePATCH"></a>
# **appPackagePATCH**
> AppPkgInfoModifications appPackagePATCH(appPkgId, appPkgInfoModifications)

Updates the operational state of an individual application package resource

Updates the operational state of an individual application package resources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appPkgId = "appPkgId_example"; // String | Identifier of an individual application package resource
    AppPkgInfoModifications appPkgInfoModifications = new AppPkgInfoModifications(); // AppPkgInfoModifications | Operational state to be set
    try {
      AppPkgInfoModifications result = apiInstance.appPackagePATCH(appPkgId, appPkgInfoModifications);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPackagePATCH");
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
| **appPkgId** | **String**| Identifier of an individual application package resource | |
| **appPkgInfoModifications** | [**AppPkgInfoModifications**](AppPkgInfoModifications.md)| Operational state to be set | |

### Return type

[**AppPkgInfoModifications**](AppPkgInfoModifications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shows that the operation has been completed successfully |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **409** | Conflict : The operation cannot be executed currently, due to a conflict with the state of the resource |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPackagesGET"></a>
# **appPackagesGET**
> List&lt;AppPkgInfo&gt; appPackagesGET(filter, allFields, fields, excludeFields, excludeDefault)

Queries information relating to on-boarded application packages in the MEO

queries information relating to on-boarded application packages in the MEO

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String filter = "filter_example"; // String | Attribute-based filtering parameters according to ETSI GS MEC 009
    String allFields = "allFields_example"; // String | Include all complex attributes in the response.
    String fields = "fields_example"; // String | Complex attributes of AppPkgInfo to be included into the response
    String excludeFields = "excludeFields_example"; // String | Complex attributes of AppPkgInfo to be excluded from the response.
    String excludeDefault = "excludeDefault_example"; // String | Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    try {
      List<AppPkgInfo> result = apiInstance.appPackagesGET(filter, allFields, fields, excludeFields, excludeDefault);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPackagesGET");
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
| **filter** | **String**| Attribute-based filtering parameters according to ETSI GS MEC 009 | [optional] |
| **allFields** | **String**| Include all complex attributes in the response. | [optional] |
| **fields** | **String**| Complex attributes of AppPkgInfo to be included into the response | [optional] |
| **excludeFields** | **String**| Complex attributes of AppPkgInfo to be excluded from the response. | [optional] |
| **excludeDefault** | **String**| Indicates to exclude the following complex attributes of AppPkgInfo from the response. | [optional] |

### Return type

[**List&lt;AppPkgInfo&gt;**](AppPkgInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains a representation of the application package resource |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPackagesPOST"></a>
# **appPackagesPOST**
> List&lt;AppPkgInfo&gt; appPackagesPOST(createAppPkg)

Create a resource for on-boarding an application package to a MEO

Create a resource for on-boarding an application package to a MEO

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    CreateAppPkg createAppPkg = new CreateAppPkg(); // CreateAppPkg | Resource to be created
    try {
      List<AppPkgInfo> result = apiInstance.appPackagesPOST(createAppPkg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPackagesPOST");
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
| **createAppPkg** | [**CreateAppPkg**](CreateAppPkg.md)| Resource to be created | |

### Return type

[**List&lt;AppPkgInfo&gt;**](AppPkgInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response for resource creation |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPkgGET"></a>
# **appPkgGET**
> appPkgGET(appPkgId)

Fetch the onboarded application package content identified by appPkgId or appDId.

Fetch the onboarded application package content identified by appPkgId or appDId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appPkgId = "appPkgId_example"; // String | Identifier of an on-boarded individual application package
    try {
      apiInstance.appPkgGET(appPkgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPkgGET");
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
| **appPkgId** | **String**| Identifier of an on-boarded individual application package | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payload body shall contain a copy of the file representing the AppD or a ZIP file that contains the file or multiple files representing the AppD. |  -  |
| **206** | Partial content |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **416** | Range Not Satisfiable . |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPkgIdGET"></a>
# **appPkgIdGET**
> AppD appPkgIdGET(appPkgId, filter, allFields, fields, excludeFields, excludeDefault)

Reads the content of the AppD of on-boarded individual application package resources.

Reads the content of the AppD of on-boarded individual application package resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appPkgId = "appPkgId_example"; // String | Identifier of an on-boarded individual application package
    String filter = "filter_example"; // String | Attribute-based filtering parameters according to ETSI GS MEC 009
    String allFields = "allFields_example"; // String | Include all complex attributes in the response.
    String fields = "fields_example"; // String | Complex attributes of AppPkgInfo to be included into the response
    String excludeFields = "excludeFields_example"; // String | Complex attributes of AppPkgInfo to be excluded from the response.
    String excludeDefault = "excludeDefault_example"; // String | Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    try {
      AppD result = apiInstance.appPkgIdGET(appPkgId, filter, allFields, fields, excludeFields, excludeDefault);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPkgIdGET");
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
| **appPkgId** | **String**| Identifier of an on-boarded individual application package | |
| **filter** | **String**| Attribute-based filtering parameters according to ETSI GS MEC 009 | [optional] |
| **allFields** | **String**| Include all complex attributes in the response. | [optional] |
| **fields** | **String**| Complex attributes of AppPkgInfo to be included into the response | [optional] |
| **excludeFields** | **String**| Complex attributes of AppPkgInfo to be excluded from the response. | [optional] |
| **excludeDefault** | **String**| Indicates to exclude the following complex attributes of AppPkgInfo from the response. | [optional] |

### Return type

[**AppD**](AppD.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of the AppD is returned. |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="appPkgPUT"></a>
# **appPkgPUT**
> appPkgPUT(appPkgId, body)

Uploads the content of application package.

Uploads the content of application package.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String appPkgId = "appPkgId_example"; // String | Identifier of an on-boarded individual application package
    File body = new File("/path/to/file"); // File | 
    try {
      apiInstance.appPkgPUT(appPkgId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#appPkgPUT");
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
| **appPkgId** | **String**| Identifier of an on-boarded individual application package | |
| **body** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/zip
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The application package has been accepted for uploading, but the processing has not been completed. |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **409** | Conflict : The operation cannot be executed currently, due to a conflict with the state of the resource |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="individualSubscriptionDELETE"></a>
# **individualSubscriptionDELETE**
> individualSubscriptionDELETE(subscriptionId)

Deletes the individual subscription to notifications about application package changes in MEO.

Deletes the individual subscription to notifications about application package changes in MEO.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of an individual subscription to notifications about application package changes
    try {
      apiInstance.individualSubscriptionDELETE(subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#individualSubscriptionDELETE");
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
| **subscriptionId** | **String**| Identifier of an individual subscription to notifications about application package changes | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="individualSubscriptionGET"></a>
# **individualSubscriptionGET**
> AppPkgSubscriptionInfo individualSubscriptionGET(subscriptionId)

Used to represent an individual subscription to notifications about application package changes.

Used to represent an individual subscription to notifications about application package changes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of an individual subscription to notifications about application package changes
    try {
      AppPkgSubscriptionInfo result = apiInstance.individualSubscriptionGET(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#individualSubscriptionGET");
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
| **subscriptionId** | **String**| Identifier of an individual subscription to notifications about application package changes | |

### Return type

[**AppPkgSubscriptionInfo**](AppPkgSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Representation of the resource. |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="subscriptionsGET"></a>
# **subscriptionsGET**
> AppPkgSubscriptionLinkList subscriptionsGET()

used to retrieve the information of subscriptions to individual application package resource in MEO

used to retrieve the information of subscriptions to individual application package resource in MEO package

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    try {
      AppPkgSubscriptionLinkList result = apiInstance.subscriptionsGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#subscriptionsGET");
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

[**AppPkgSubscriptionLinkList**](AppPkgSubscriptionLinkList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of zero or more subscriptions |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

<a id="subscriptionsPOST"></a>
# **subscriptionsPOST**
> AppPkgSubscriptionInfo subscriptionsPOST(appPkgSubscription)

Subscribe to notifications about on-boarding an application package

Subscribe to notifications about on-boarding an application package

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmApi apiInstance = new AppPkgmApi(defaultClient);
    AppPkgSubscription appPkgSubscription = new AppPkgSubscription(); // AppPkgSubscription | The input parameters of subscribe operation to notifications
    try {
      AppPkgSubscriptionInfo result = apiInstance.subscriptionsPOST(appPkgSubscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmApi#subscriptionsPOST");
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
| **appPkgSubscription** | [**AppPkgSubscription**](AppPkgSubscription.md)| The input parameters of subscribe operation to notifications | |

### Return type

[**AppPkgSubscriptionInfo**](AppPkgSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response for created subscription |  -  |
| **400** | Bad Request : used to indicate that incorrect parameters were passed to the request. |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **406** | Not Acceptable : used to indicate that the server cannot provide the any of the content formats supported by the client. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

