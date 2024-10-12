# HdfsTemplateApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createHdfsTemplate**](HdfsTemplateApi.md#createHdfsTemplate) | **POST** /hdfs_template | Create a HDFS directory template |
| [**deleteHdfsTemplate**](HdfsTemplateApi.md#deleteHdfsTemplate) | **DELETE** /hdfs_template/{id} | Delete a HDFS directory template |
| [**getHdfsTemplate**](HdfsTemplateApi.md#getHdfsTemplate) | **GET** /hdfs_template/{id} | Get information for a HDFS directory template |
| [**queryHdfsTemplate**](HdfsTemplateApi.md#queryHdfsTemplate) | **GET** /hdfs_template | Get summary information for all HDFS directory templates |
| [**updateHdfsTemplate**](HdfsTemplateApi.md#updateHdfsTemplate) | **PATCH** /hdfs_template/{id} | Modify a HDFS directory template |


<a id="createHdfsTemplate"></a>
# **createHdfsTemplate**
> HdfsTemplateDetail createHdfsTemplate(hdfsTemplateCreate)

Create a HDFS directory template

Create a HDFS directory template. The template is applied to the host.  Each template is a set of paths on the host. A template uses full paths and wildcards to define the objects to include, exclude, and exempt from exclusion. The **_exceptions_** value specifies paths that should not be excluded from the HDFS directory by the **_exclude_** value. Specify an array of full path descriptions for each property **_include_**, **_exclude_**, and **_exceptions_**. Acceptable wildcard characters are. + **_\\*_** Single asterisk matches zero or more characters up to a path deliminator. + **_\\*\\*_** Double asterisk matches zero or more characters. The following rules apply to path descriptions. + Accepts UTF-8 characters. + Case sensitive. + Forward slash character **_/_** is the path deliminator. + Symbolic links must point to a subset of a non symbolic link path. + Paths that do not start with **_/_** are modified to start with **_\\*\\*_/_**. + Paths that do not end with **_\\*_** are modified to end with **_/\\*\\*_**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HdfsTemplateApi apiInstance = new HdfsTemplateApi(defaultClient);
    HdfsTemplateCreate hdfsTemplateCreate = new HdfsTemplateCreate(); // HdfsTemplateCreate | Provide an object with the HDFS directory template definition.
    try {
      HdfsTemplateDetail result = apiInstance.createHdfsTemplate(hdfsTemplateCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsTemplateApi#createHdfsTemplate");
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
| **hdfsTemplateCreate** | [**HdfsTemplateCreate**](HdfsTemplateCreate.md)| Provide an object with the HDFS directory template definition. | |

### Return type

[**HdfsTemplateDetail**](HdfsTemplateDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Summary information for the created HDFS directory template. |  -  |

<a id="deleteHdfsTemplate"></a>
# **deleteHdfsTemplate**
> deleteHdfsTemplate(id, preserveSnapshots)

Delete a HDFS directory template

Deletes the specfied HDFS directory template. All associated HDFS directories are deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HdfsTemplateApi apiInstance = new HdfsTemplateApi(defaultClient);
    String id = "id_example"; // String | ID of the HDFS directory template to remove.
    Boolean preserveSnapshots = true; // Boolean | A flag that indicates whether the snapshots of the HDFS directories of this template are converted to relics or deleted. By default, snapshots are converted. Set this flag to 'false' to delete the snapshots.
    try {
      apiInstance.deleteHdfsTemplate(id, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsTemplateApi#deleteHdfsTemplate");
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
| **id** | **String**| ID of the HDFS directory template to remove. | |
| **preserveSnapshots** | **Boolean**| A flag that indicates whether the snapshots of the HDFS directories of this template are converted to relics or deleted. By default, snapshots are converted. Set this flag to &#39;false&#39; to delete the snapshots. | [optional] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully removed the specified HDFS directory template. |  -  |

<a id="getHdfsTemplate"></a>
# **getHdfsTemplate**
> HdfsTemplateDetail getHdfsTemplate(id)

Get information for a HDFS directory template

Retrieve summary information for a specified HDFS directory template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HdfsTemplateApi apiInstance = new HdfsTemplateApi(defaultClient);
    String id = "id_example"; // String | The ID of the HDFS directory template.
    try {
      HdfsTemplateDetail result = apiInstance.getHdfsTemplate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsTemplateApi#getHdfsTemplate");
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
| **id** | **String**| The ID of the HDFS directory template. | |

### Return type

[**HdfsTemplateDetail**](HdfsTemplateDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for the specified HDFS directory template. |  -  |

<a id="queryHdfsTemplate"></a>
# **queryHdfsTemplate**
> HdfsTemplateDetailListResponse queryHdfsTemplate(primaryClusterId, name, sortBy, sortOrder)

Get summary information for all HDFS directory templates

Retrieve summary information for all HDFS directory templates, including: ID and name of the HDFS directory template, HDFS directory template creation timestamp, array of the included filepaths, array of the excluded filepaths.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HdfsTemplateApi apiInstance = new HdfsTemplateApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    String name = "name_example"; // String | Retrieve HDFS directory templates with a name matching the provided name. The search is performed as a case-insensitive infix search.
    String sortBy = "name"; // String | Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_includes_**, **_excludes_**, **_exceptions_**, **_hostCount_**. Default sort_order is ascending.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      HdfsTemplateDetailListResponse result = apiInstance.queryHdfsTemplate(primaryClusterId, name, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsTemplateApi#queryHdfsTemplate");
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
| **primaryClusterId** | **String**| Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session. | [optional] |
| **name** | **String**| Retrieve HDFS directory templates with a name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_includes_**, **_excludes_**, **_exceptions_**, **_hostCount_**. Default sort_order is ascending. | [optional] [default to name] [enum: name, hostCount, includes, excludes, exceptions] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**HdfsTemplateDetailListResponse**](HdfsTemplateDetailListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for all HDFS directory templates. |  -  |

<a id="updateHdfsTemplate"></a>
# **updateHdfsTemplate**
> HdfsTemplateDetail updateHdfsTemplate(id, hdfsTemplatePatch)

Modify a HDFS directory template

Modify the values of specified HDFS directory template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HdfsTemplateApi apiInstance = new HdfsTemplateApi(defaultClient);
    String id = "id_example"; // String | ID of the HDFS directory template to update.
    HdfsTemplatePatch hdfsTemplatePatch = new HdfsTemplatePatch(); // HdfsTemplatePatch | Provide an object with the HDFS directory template definition.
    try {
      HdfsTemplateDetail result = apiInstance.updateHdfsTemplate(id, hdfsTemplatePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsTemplateApi#updateHdfsTemplate");
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
| **id** | **String**| ID of the HDFS directory template to update. | |
| **hdfsTemplatePatch** | [**HdfsTemplatePatch**](HdfsTemplatePatch.md)| Provide an object with the HDFS directory template definition. | |

### Return type

[**HdfsTemplateDetail**](HdfsTemplateDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for modified HDFS directory template. |  -  |

