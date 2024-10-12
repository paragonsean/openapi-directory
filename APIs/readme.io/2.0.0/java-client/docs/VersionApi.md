# VersionApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVersion**](VersionApi.md#createVersion) | **POST** /version | Create version |
| [**deleteVersion**](VersionApi.md#deleteVersion) | **DELETE** /version/{versionId} | Delete version |
| [**getVersion**](VersionApi.md#getVersion) | **GET** /version/{versionId} | Get version |
| [**getVersions**](VersionApi.md#getVersions) | **GET** /version | Get versions |
| [**updateVersion**](VersionApi.md#updateVersion) | **PUT** /version/{versionId} | Update version |


<a id="createVersion"></a>
# **createVersion**
> createVersion(version)

Create version

Create a new version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    VersionApi apiInstance = new VersionApi(defaultClient);
    Version version = new Version(); // Version | Version object
    try {
      apiInstance.createVersion(version);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionApi#createVersion");
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
| **version** | [**Version**](Version.md)| Version object | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The model was successfully created and associated with the target project |  -  |
| **400** | That version already exists in the project, or there are validation errors with the request |  -  |
| **404** | Could not find target fork in database |  -  |

<a id="deleteVersion"></a>
# **deleteVersion**
> deleteVersion(versionId)

Delete version

Delete a version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    VersionApi apiInstance = new VersionApi(defaultClient);
    String versionId = "versionId_example"; // String | Semver version indentifier
    try {
      apiInstance.deleteVersion(versionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionApi#deleteVersion");
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
| **versionId** | **String**| Semver version indentifier | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The target version was successfully deleted |  -  |
| **400** | Cannot delete the main version for a project |  -  |
| **404** | Could not find target version in database |  -  |

<a id="getVersion"></a>
# **getVersion**
> getVersion(versionId)

Get version

Returns the version with this version ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    VersionApi apiInstance = new VersionApi(defaultClient);
    String versionId = "versionId_example"; // String | Semver version indentifier
    try {
      apiInstance.getVersion(versionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionApi#getVersion");
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
| **versionId** | **String**| Semver version indentifier | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON version model |  -  |
| **404** | Could not find target version in database |  -  |

<a id="getVersions"></a>
# **getVersions**
> getVersions()

Get versions

Retrieve a list of versions associated with a project API key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    VersionApi apiInstance = new VersionApi(defaultClient);
    try {
      apiInstance.getVersions();
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionApi#getVersions");
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON list of versions |  -  |

<a id="updateVersion"></a>
# **updateVersion**
> updateVersion(versionId, version)

Update version

Update an existing version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    VersionApi apiInstance = new VersionApi(defaultClient);
    String versionId = "versionId_example"; // String | Semver version indentifier
    Version version = new Version(); // Version | Version object
    try {
      apiInstance.updateVersion(versionId, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionApi#updateVersion");
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
| **versionId** | **String**| Semver version indentifier | |
| **version** | [**Version**](Version.md)| Version object | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The target version was successfully updated |  -  |
| **400** | Cannot demote a version through update |  -  |
| **404** | Could not find target version in database |  -  |

