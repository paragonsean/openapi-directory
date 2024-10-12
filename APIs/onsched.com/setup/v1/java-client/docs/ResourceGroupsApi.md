# ResourceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1ResourcegroupsGet**](ResourceGroupsApi.md#setupV1ResourcegroupsGet) | **GET** /setup/v1/resourcegroups | List Resource Groups |
| [**setupV1ResourcegroupsIdDelete**](ResourceGroupsApi.md#setupV1ResourcegroupsIdDelete) | **DELETE** /setup/v1/resourcegroups/{id} | Delete Resource Group |
| [**setupV1ResourcegroupsIdGet**](ResourceGroupsApi.md#setupV1ResourcegroupsIdGet) | **GET** /setup/v1/resourcegroups/{id} | Get Resource Group |
| [**setupV1ResourcegroupsIdPut**](ResourceGroupsApi.md#setupV1ResourcegroupsIdPut) | **PUT** /setup/v1/resourcegroups/{id} | Update Resource Group |
| [**setupV1ResourcegroupsIdRecoverPut**](ResourceGroupsApi.md#setupV1ResourcegroupsIdRecoverPut) | **PUT** /setup/v1/resourcegroups/{id}/recover | Recover Resource Group |
| [**setupV1ResourcegroupsPost**](ResourceGroupsApi.md#setupV1ResourcegroupsPost) | **POST** /setup/v1/resourcegroups | Create Resource Group |


<a id="setupV1ResourcegroupsGet"></a>
# **setupV1ResourcegroupsGet**
> ResourceGroupListViewModel setupV1ResourcegroupsGet(locationId, deleted, offset, limit)

List Resource Groups

&lt;p&gt;Use this endpoint to &lt;b&gt;List Resource Groups&lt;/b&gt; for the specified location. If not specified, the business location defaults to the primary business location. &lt;b&gt;Name&lt;/b&gt; is a required field.&lt;/p&gt;  &lt;p&gt;Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Boolean deleted = true; // Boolean | Filter results by deleted status
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceGroupListViewModel result = apiInstance.setupV1ResourcegroupsGet(locationId, deleted, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#setupV1ResourcegroupsGet");
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
| **locationId** | **String**| id of business location, defaults to primary business location | [optional] |
| **deleted** | **Boolean**| Filter results by deleted status | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ResourceGroupListViewModel**](ResourceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcegroupsIdDelete"></a>
# **setupV1ResourcegroupsIdDelete**
> ResourceGroupViewModel setupV1ResourcegroupsIdDelete(id)

Delete Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. The resource group is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/resourcegroups​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String id = "id_example"; // String | id of resourceGroup object
    try {
      ResourceGroupViewModel result = apiInstance.setupV1ResourcegroupsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#setupV1ResourcegroupsIdDelete");
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
| **id** | **String**| id of resourceGroup object | |

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcegroupsIdGet"></a>
# **setupV1ResourcegroupsIdGet**
> ResourceGroupViewModel setupV1ResourcegroupsIdGet(id)

Get Resource Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Group&lt;/b&gt; object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. Find resourceGroup id&#39;s by using the &lt;i&gt;GET setup/v1/resourceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String id = "id_example"; // String | id of resourceGroup object
    try {
      ResourceGroupViewModel result = apiInstance.setupV1ResourcegroupsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#setupV1ResourcegroupsIdGet");
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
| **id** | **String**| id of resourceGroup object | |

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcegroupsIdPut"></a>
# **setupV1ResourcegroupsIdPut**
> ResourceGroupViewModel setupV1ResourcegroupsIdPut(id, resourceGroupUpdateModel)

Update Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String id = "id_example"; // String | id of resourcGroup object
    ResourceGroupUpdateModel resourceGroupUpdateModel = new ResourceGroupUpdateModel(); // ResourceGroupUpdateModel | Resource Group Update Model
    try {
      ResourceGroupViewModel result = apiInstance.setupV1ResourcegroupsIdPut(id, resourceGroupUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#setupV1ResourcegroupsIdPut");
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
| **id** | **String**| id of resourcGroup object | |
| **resourceGroupUpdateModel** | [**ResourceGroupUpdateModel**](ResourceGroupUpdateModel.md)| Resource Group Update Model | [optional] |

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcegroupsIdRecoverPut"></a>
# **setupV1ResourcegroupsIdRecoverPut**
> ResourceViewModel setupV1ResourcegroupsIdRecoverPut(id)

Recover Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String id = "id_example"; // String | id of resourceGroup object
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcegroupsIdRecoverPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#setupV1ResourcegroupsIdRecoverPut");
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
| **id** | **String**| id of resourceGroup object | |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcegroupsPost"></a>
# **setupV1ResourcegroupsPost**
> ResourceGroupViewModel setupV1ResourcegroupsPost(resourceGroupInputModel)

Create Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a resourceGroup object. Resource groups are used to categorize your resources.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    ResourceGroupInputModel resourceGroupInputModel = new ResourceGroupInputModel(); // ResourceGroupInputModel | Resource input model
    try {
      ResourceGroupViewModel result = apiInstance.setupV1ResourcegroupsPost(resourceGroupInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#setupV1ResourcegroupsPost");
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
| **resourceGroupInputModel** | [**ResourceGroupInputModel**](ResourceGroupInputModel.md)| Resource input model | [optional] |

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

