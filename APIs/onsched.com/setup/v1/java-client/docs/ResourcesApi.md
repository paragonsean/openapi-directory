# ResourcesApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1ResourcesAllocationsIdDelete**](ResourcesApi.md#setupV1ResourcesAllocationsIdDelete) | **DELETE** /setup/v1/resources/allocations/{id} | Delete Allocation |
| [**setupV1ResourcesAllocationsIdGet**](ResourcesApi.md#setupV1ResourcesAllocationsIdGet) | **GET** /setup/v1/resources/allocations/{id} | Get Allocation |
| [**setupV1ResourcesAllocationsIdPut**](ResourcesApi.md#setupV1ResourcesAllocationsIdPut) | **PUT** /setup/v1/resources/allocations/{id} | Update Allocation |
| [**setupV1ResourcesBlockIdDelete**](ResourcesApi.md#setupV1ResourcesBlockIdDelete) | **DELETE** /setup/v1/resources/block/{id} | Delete Block |
| [**setupV1ResourcesBlockIdPut**](ResourcesApi.md#setupV1ResourcesBlockIdPut) | **PUT** /setup/v1/resources/block/{id} | Update Block |
| [**setupV1ResourcesBlocksIdGet**](ResourcesApi.md#setupV1ResourcesBlocksIdGet) | **GET** /setup/v1/resources/blocks/{id} | Get Block |
| [**setupV1ResourcesBulkPost**](ResourcesApi.md#setupV1ResourcesBulkPost) | **POST** /setup/v1/resources/bulk | Create Resources Bulk |
| [**setupV1ResourcesBulkPut**](ResourcesApi.md#setupV1ResourcesBulkPut) | **PUT** /setup/v1/resources/bulk | Update Resources Bulk |
| [**setupV1ResourcesGet**](ResourcesApi.md#setupV1ResourcesGet) | **GET** /setup/v1/resources | List Resources |
| [**setupV1ResourcesIdAllocationsGet**](ResourcesApi.md#setupV1ResourcesIdAllocationsGet) | **GET** /setup/v1/resources/{id}/allocations | List Resource Allocations |
| [**setupV1ResourcesIdAllocationsPost**](ResourcesApi.md#setupV1ResourcesIdAllocationsPost) | **POST** /setup/v1/resources/{id}/allocations | Create Allocation |
| [**setupV1ResourcesIdAvailabilityGet**](ResourcesApi.md#setupV1ResourcesIdAvailabilityGet) | **GET** /setup/v1/resources/{id}/availability | List Weekly Availability |
| [**setupV1ResourcesIdAvailabilityPut**](ResourcesApi.md#setupV1ResourcesIdAvailabilityPut) | **PUT** /setup/v1/resources/{id}/availability | Update Weekly Availability |
| [**setupV1ResourcesIdBlockPost**](ResourcesApi.md#setupV1ResourcesIdBlockPost) | **POST** /setup/v1/resources/{id}/block | Create Block |
| [**setupV1ResourcesIdBlocksGet**](ResourcesApi.md#setupV1ResourcesIdBlocksGet) | **GET** /setup/v1/resources/{id}/blocks | List Resource Blocks |
| [**setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet**](ResourcesApi.md#setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet) | **GET** /setup/v1/resources/{id}/calendar/auth/google/{googleEmailAddress} | Get Resource Google URL |
| [**setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet**](ResourcesApi.md#setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet) | **GET** /setup/v1/resources/{id}/calendar/auth/outlook/{outlookEmailAddress} | Get Resource Outlook URL |
| [**setupV1ResourcesIdDelete**](ResourcesApi.md#setupV1ResourcesIdDelete) | **DELETE** /setup/v1/resources/{id} | Delete Resource |
| [**setupV1ResourcesIdDeleteimageDelete**](ResourcesApi.md#setupV1ResourcesIdDeleteimageDelete) | **DELETE** /setup/v1/resources/{id}/deleteimage | Delete Resource Image |
| [**setupV1ResourcesIdGet**](ResourcesApi.md#setupV1ResourcesIdGet) | **GET** /setup/v1/resources/{id} | Get Resource |
| [**setupV1ResourcesIdPut**](ResourcesApi.md#setupV1ResourcesIdPut) | **PUT** /setup/v1/resources/{id} | Update Resource |
| [**setupV1ResourcesIdReassignAppointmentsResourceIdPut**](ResourcesApi.md#setupV1ResourcesIdReassignAppointmentsResourceIdPut) | **PUT** /setup/v1/resources/{id}/reassign/appointments/{resourceId} | Reassign Resource |
| [**setupV1ResourcesIdRecoverPut**](ResourcesApi.md#setupV1ResourcesIdRecoverPut) | **PUT** /setup/v1/resources/{id}/recover | Recover Resource |
| [**setupV1ResourcesIdServicesDelete**](ResourcesApi.md#setupV1ResourcesIdServicesDelete) | **DELETE** /setup/v1/resources/{id}/services | Delete Linked Services |
| [**setupV1ResourcesIdServicesPost**](ResourcesApi.md#setupV1ResourcesIdServicesPost) | **POST** /setup/v1/resources/{id}/services | Create Linked Services |
| [**setupV1ResourcesIdServicesPut**](ResourcesApi.md#setupV1ResourcesIdServicesPut) | **PUT** /setup/v1/resources/{id}/services | Update Linked Services |
| [**setupV1ResourcesIdUploadimagePost**](ResourcesApi.md#setupV1ResourcesIdUploadimagePost) | **POST** /setup/v1/resources/{id}/uploadimage | Upload Resource Image |
| [**setupV1ResourcesPost**](ResourcesApi.md#setupV1ResourcesPost) | **POST** /setup/v1/resources | Create Resource |
| [**setupV1ResourcesTimezonesGet**](ResourcesApi.md#setupV1ResourcesTimezonesGet) | **GET** /setup/v1/resources/timezones | Get Time Zones |


<a id="setupV1ResourcesAllocationsIdDelete"></a>
# **setupV1ResourcesAllocationsIdDelete**
> ResourceBlockViewModel setupV1ResourcesAllocationsIdDelete(id)

Delete Allocation

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Resource Allocation. A valid &lt;b&gt;resourceAllocation id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resourceAllocation object
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesAllocationsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesAllocationsIdDelete");
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
| **id** | **String**| id of resourceAllocation object | |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesAllocationsIdGet"></a>
# **setupV1ResourcesAllocationsIdGet**
> ResourceAllocationViewModel setupV1ResourcesAllocationsIdGet(id)

Get Allocation

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Allocation&lt;/b&gt;. A valid &lt;b&gt;resourceAllocation id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resourceAllocation object
    try {
      ResourceAllocationViewModel result = apiInstance.setupV1ResourcesAllocationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesAllocationsIdGet");
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
| **id** | **String**| id of resourceAllocation object | |

### Return type

[**ResourceAllocationViewModel**](ResourceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesAllocationsIdPut"></a>
# **setupV1ResourcesAllocationsIdPut**
> ResourceBlockViewModel setupV1ResourcesAllocationsIdPut(id, resourceAllocationUpdateModel)

Update Allocation

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resource allocation. A valid &lt;b&gt;resourceAllocation id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST /setup/v1/resources/{id}/allocations&lt;/i&gt; endpoint for details.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resourceAllocation object
    ResourceAllocationUpdateModel resourceAllocationUpdateModel = new ResourceAllocationUpdateModel(); // ResourceAllocationUpdateModel | Resource allocation update model
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesAllocationsIdPut(id, resourceAllocationUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesAllocationsIdPut");
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
| **id** | **String**| id of resourceAllocation object | |
| **resourceAllocationUpdateModel** | [**ResourceAllocationUpdateModel**](ResourceAllocationUpdateModel.md)| Resource allocation update model | [optional] |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesBlockIdDelete"></a>
# **setupV1ResourcesBlockIdDelete**
> ResourceBlockViewModel setupV1ResourcesBlockIdDelete(id)

Delete Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resourceBlock id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resourceBlock object
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesBlockIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesBlockIdDelete");
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
| **id** | **String**| id of resourceBlock object | |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesBlockIdPut"></a>
# **setupV1ResourcesBlockIdPut**
> ResourceBlockViewModel setupV1ResourcesBlockIdPut(id, resourceBlockUpdateModel)

Update Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resourceBlock id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/block&lt;/i&gt; endpoint for fieldnames and details.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resourceBlock object
    ResourceBlockUpdateModel resourceBlockUpdateModel = new ResourceBlockUpdateModel(); // ResourceBlockUpdateModel | Resource Block update model
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesBlockIdPut(id, resourceBlockUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesBlockIdPut");
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
| **id** | **String**| id of resourceBlock object | |
| **resourceBlockUpdateModel** | [**ResourceBlockUpdateModel**](ResourceBlockUpdateModel.md)| Resource Block update model | [optional] |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesBlocksIdGet"></a>
# **setupV1ResourcesBlocksIdGet**
> ResourceBlockViewModel setupV1ResourcesBlocksIdGet(id)

Get Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Get&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resourceBlock id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resourceBlock object
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesBlocksIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesBlocksIdGet");
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
| **id** | **String**| id of resourceBlock object | |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesBulkPost"></a>
# **setupV1ResourcesBulkPost**
> List&lt;ResourceViewModel&gt; setupV1ResourcesBulkPost(googleAuthReturnUrl, outlookAuthReturnUrl, resourcesInputModel)

Create Resources Bulk

&lt;p&gt;Use this endpoint to &lt;b&gt;Bulk Create&lt;/b&gt; resources. Valid &lt;b&gt;resource ids&lt;/b&gt; are required. The posted list of resources cannot exceed 100 resource objects per transaction for performance purposes.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    ResourcesInputModel resourcesInputModel = new ResourcesInputModel(); // ResourcesInputModel | Resources input model
    try {
      List<ResourceViewModel> result = apiInstance.setupV1ResourcesBulkPost(googleAuthReturnUrl, outlookAuthReturnUrl, resourcesInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesBulkPost");
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
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |
| **resourcesInputModel** | [**ResourcesInputModel**](ResourcesInputModel.md)| Resources input model | [optional] |

### Return type

[**List&lt;ResourceViewModel&gt;**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesBulkPut"></a>
# **setupV1ResourcesBulkPut**
> List&lt;ResourceViewModel&gt; setupV1ResourcesBulkPut(googleAuthReturnUrl, outlookAuthReturnUrl, resourcesUpdateModel)

Update Resources Bulk

&lt;p&gt;Use this endpoint to &lt;b&gt;Bulk Update&lt;/b&gt; resources. Valid &lt;b&gt;resource id&#39;s&lt;/b&gt; are required. The list of resources cannot exceed 100 resource objects per transaction for performance purposes.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    ResourcesUpdateModel resourcesUpdateModel = new ResourcesUpdateModel(); // ResourcesUpdateModel | Resources update model
    try {
      List<ResourceViewModel> result = apiInstance.setupV1ResourcesBulkPut(googleAuthReturnUrl, outlookAuthReturnUrl, resourcesUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesBulkPut");
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
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |
| **resourcesUpdateModel** | [**ResourcesUpdateModel**](ResourcesUpdateModel.md)| Resources update model | [optional] |

### Return type

[**List&lt;ResourceViewModel&gt;**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesGet"></a>
# **setupV1ResourcesGet**
> ResourceListViewModel setupV1ResourcesGet(locationId, resourceGroupId, email, name, deleted, googleAuthReturnUrl, outlookAuthReturnUrl, offset, limit)

List Resources

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Resources&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    String resourceGroupId = "resourceGroupId_example"; // String | Filter by group Id
    String email = "email_example"; // String | Filter by email address
    String name = "name_example"; // String | Search by name
    Boolean deleted = true; // Boolean | Show by deleted status, default is false
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max is 100
    try {
      ResourceListViewModel result = apiInstance.setupV1ResourcesGet(locationId, resourceGroupId, email, name, deleted, googleAuthReturnUrl, outlookAuthReturnUrl, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesGet");
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
| **resourceGroupId** | **String**| Filter by group Id | [optional] |
| **email** | **String**| Filter by email address | [optional] |
| **name** | **String**| Search by name | [optional] |
| **deleted** | **Boolean**| Show by deleted status, default is false | [optional] |
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max is 100 | [optional] |

### Return type

[**ResourceListViewModel**](ResourceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resource object |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **404** | Resource was not found |  -  |

<a id="setupV1ResourcesIdAllocationsGet"></a>
# **setupV1ResourcesIdAllocationsGet**
> ResourceAllocationListViewModel setupV1ResourcesIdAllocationsGet(id, startDate, endDate, offset, limit)

List Resource Allocations

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Allocations&lt;/b&gt; for a specified resource. We recommend using allocations if a resource&#39;s schedule changes frequently from day to day or week to week. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource to list allocations for
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | yyyy-mm-dd, filter allocations on/after startDate
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | yyyy-mm-dd, filter on/before endDate
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceAllocationListViewModel result = apiInstance.setupV1ResourcesIdAllocationsGet(id, startDate, endDate, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdAllocationsGet");
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
| **id** | **String**| id of resource to list allocations for | |
| **startDate** | **OffsetDateTime**| yyyy-mm-dd, filter allocations on/after startDate | [optional] |
| **endDate** | **OffsetDateTime**| yyyy-mm-dd, filter on/before endDate | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ResourceAllocationListViewModel**](ResourceAllocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resource allocation objects |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error. |  -  |
| **404** | Resource was not found |  -  |

<a id="setupV1ResourcesIdAllocationsPost"></a>
# **setupV1ResourcesIdAllocationsPost**
> ResourceBlockViewModel setupV1ResourcesIdAllocationsPost(id, resourceAllocationInputModel)

Create Allocation

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a resource allocation for a resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;. Resource allocations can be set to specific time ranges or for the whole day by setting startTime&#x3D;0 and endTime&#x3D;2400. They can repeat for a specific date range instance or set to repeat at a specified frequency.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M &lt;/b&gt;for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the allocation repeats. For example, an interval of 2 for a weekly allocation means that the allocation will repeat every 2nd week beginning at the day specified. A daily allocation with an interval of 10 means the allocation will repeat every 10 days. The interval property applies to all repeat frequencies.  &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY ALLOCATIONS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY ALLOCATIONS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;. You must specify the &lt;b&gt;“weekdays”&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;.  For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the allocation date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY ALLOCATIONS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly. &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want allocated.  If monthDay&#x3D;’15’ this means to allocate the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on.  For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits:  day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    ResourceAllocationInputModel resourceAllocationInputModel = new ResourceAllocationInputModel(); // ResourceAllocationInputModel | 
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesIdAllocationsPost(id, resourceAllocationInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdAllocationsPost");
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
| **id** | **String**| id of resource object | |
| **resourceAllocationInputModel** | [**ResourceAllocationInputModel**](ResourceAllocationInputModel.md)|  | [optional] |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdAvailabilityGet"></a>
# **setupV1ResourcesIdAvailabilityGet**
> ResourceAvailabilityViewModel setupV1ResourcesIdAvailabilityGet(id)

List Weekly Availability

&lt;p&gt;Use this endpoint to view the &lt;b&gt;Weekly Availability&lt;/b&gt; for a resource. The displayed available times are represented in the resource&#39;s timezone. The resource timezone can be set to any world timezone. If not provided, by default it is set to the Business timezone.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    try {
      ResourceAvailabilityViewModel result = apiInstance.setupV1ResourcesIdAvailabilityGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdAvailabilityGet");
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
| **id** | **String**| id of resource object | |

### Return type

[**ResourceAvailabilityViewModel**](ResourceAvailabilityViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdAvailabilityPut"></a>
# **setupV1ResourcesIdAvailabilityPut**
> ResourceAvailabilityViewModel setupV1ResourcesIdAvailabilityPut(id, availabilityInputModel)

Update Weekly Availability

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; resource weekly availability. A valid &lt;b&gt;resource id&lt;/b&gt; is required. The availability day entries are created when a resource object is created.&lt;/p&gt;  &lt;p&gt;To update weekly availability hours, all days of the week must be provided. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri&lt;/b&gt; and &lt;b&gt;sat&lt;/b&gt;. The &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; fields are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. We support 24-hour availability, set startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0.&lt;/p&gt;  &lt;p&gt;If you require times in between specified hours to be unavailable, use the resource blocks endpoints. Times entered represent the timezone of the resource. Resources can be set to any world timezone. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    AvailabilityInputModel availabilityInputModel = new AvailabilityInputModel(); // AvailabilityInputModel | Resource Availability Input Model
    try {
      ResourceAvailabilityViewModel result = apiInstance.setupV1ResourcesIdAvailabilityPut(id, availabilityInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdAvailabilityPut");
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
| **id** | **String**| id of resource object | |
| **availabilityInputModel** | [**AvailabilityInputModel**](AvailabilityInputModel.md)| Resource Availability Input Model | [optional] |

### Return type

[**ResourceAvailabilityViewModel**](ResourceAvailabilityViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdBlockPost"></a>
# **setupV1ResourcesIdBlockPost**
> ResourceBlockViewModel setupV1ResourcesIdBlockPost(id, resourceBlockInputModel)

Create Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;Resource blocks can be set to specific time ranges or for the whole day. Use the &lt;b&gt;AllDay&lt;/b&gt; setting to create an all-day block. &lt;b&gt;AllDay&lt;/b&gt; will automatically set startTime to 0 and endTime to 2400.&lt;/p&gt;  &lt;p&gt;Resource blocks can be for a specific date range instance or set to repeat at a specified frequency. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the block repeats. For example, an interval of 2 for a weekly block means that the block will repeat every 2nd week beginning at the day specified. A daily block with an interval of 10 means the block will repeat every 10 days. The interval property applies to all repeat frequencies. &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY BLOCKS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY BLOCKS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;.  You must specify the &lt;b&gt;weekdays&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;. For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the block date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY BLOCKS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly, &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want blocked.  If monthDay&#x3D;’15’ this means to block the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on. For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits: day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    ResourceBlockInputModel resourceBlockInputModel = new ResourceBlockInputModel(); // ResourceBlockInputModel | 
    try {
      ResourceBlockViewModel result = apiInstance.setupV1ResourcesIdBlockPost(id, resourceBlockInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdBlockPost");
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
| **id** | **String**| id of resource object | |
| **resourceBlockInputModel** | [**ResourceBlockInputModel**](ResourceBlockInputModel.md)|  | [optional] |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdBlocksGet"></a>
# **setupV1ResourcesIdBlocksGet**
> ResourceBlockListViewModel setupV1ResourcesIdBlocksGet(id, startDate, endDate, offset, limit)

List Resource Blocks

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Blocks&lt;/b&gt;. A valid &lt;b&gt;resource id&lt;/b&gt; is required. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource to list blocks for
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | YYYY-MM-DD, filter blocks on/after startDate
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | YYYY-MM-DD, filter on/before endDate
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceBlockListViewModel result = apiInstance.setupV1ResourcesIdBlocksGet(id, startDate, endDate, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdBlocksGet");
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
| **id** | **String**| id of resource to list blocks for | |
| **startDate** | **OffsetDateTime**| YYYY-MM-DD, filter blocks on/after startDate | [optional] |
| **endDate** | **OffsetDateTime**| YYYY-MM-DD, filter on/before endDate | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ResourceBlockListViewModel**](ResourceBlockListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resource block object&#39;s |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error. |  -  |
| **404** | Resource was not found |  -  |

<a id="setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet"></a>
# **setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet**
> CalendarAuthViewModel setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet(id, googleEmailAddress, googleAuthReturnUrl)

Get Resource Google URL

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Resources Google Calendar Authorization URL&lt;/b&gt;. A valid &lt;b&gt;resource id&lt;/b&gt; and &lt;b&gt;Google Email Address&lt;/b&gt; are required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    String googleEmailAddress = "googleEmailAddress_example"; // String | Email address of Google Calendar
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    try {
      CalendarAuthViewModel result = apiInstance.setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet(id, googleEmailAddress, googleAuthReturnUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdCalendarAuthGoogleGoogleEmailAddressGet");
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
| **id** | **String**| id of resource object | |
| **googleEmailAddress** | **String**| Email address of Google Calendar | |
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |

### Return type

[**CalendarAuthViewModel**](CalendarAuthViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet"></a>
# **setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet**
> CalendarAuthViewModel setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet(id, outlookEmailAddress, outlookAuthReturnUrl)

Get Resource Outlook URL

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Resources Outlook Calendar Authorization URL&lt;/b&gt;. A valid &lt;b&gt;resource id&lt;/b&gt; and &lt;b&gt;Outlook Email Address&lt;/b&gt; are required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    String outlookEmailAddress = "outlookEmailAddress_example"; // String | Email address of Outlook Calendar
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    try {
      CalendarAuthViewModel result = apiInstance.setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet(id, outlookEmailAddress, outlookAuthReturnUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdCalendarAuthOutlookOutlookEmailAddressGet");
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
| **id** | **String**| id of resource object | |
| **outlookEmailAddress** | **String**| Email address of Outlook Calendar | |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |

### Return type

[**CalendarAuthViewModel**](CalendarAuthViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdDelete"></a>
# **setupV1ResourcesIdDelete**
> ResourceViewModel setupV1ResourcesIdDelete(id)

Delete Resource

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a resource. The resource is not permanently deleted and can be recovered. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdDelete");
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
| **id** | **String**| id of resource object | |

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

<a id="setupV1ResourcesIdDeleteimageDelete"></a>
# **setupV1ResourcesIdDeleteimageDelete**
> ResourceViewModel setupV1ResourcesIdDeleteimageDelete(id)

Delete Resource Image

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a previously uploaded resource image. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdDeleteimageDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdDeleteimageDelete");
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
| **id** | **String**| id of resource object | |

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

<a id="setupV1ResourcesIdGet"></a>
# **setupV1ResourcesIdGet**
> ResourceViewModel setupV1ResourcesIdGet(id, googleAuthReturnUrl, outlookAuthReturnUrl)

Get Resource

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource&lt;/b&gt; object. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Find resource id&#39;s by using the: &lt;i&gt;GET /setup/v1/resources&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdGet(id, googleAuthReturnUrl, outlookAuthReturnUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdGet");
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
| **id** | **String**| id of resource object | |
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |

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

<a id="setupV1ResourcesIdPut"></a>
# **setupV1ResourcesIdPut**
> ResourceViewModel setupV1ResourcesIdPut(id, googleAuthReturnUrl, outlookAuthReturnUrl, resourceUpdateModel)

Update Resource

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    ResourceUpdateModel resourceUpdateModel = new ResourceUpdateModel(); // ResourceUpdateModel | Resource Update Model
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdPut(id, googleAuthReturnUrl, outlookAuthReturnUrl, resourceUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdPut");
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
| **id** | **String**| id of resource object | |
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |
| **resourceUpdateModel** | [**ResourceUpdateModel**](ResourceUpdateModel.md)| Resource Update Model | [optional] |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdReassignAppointmentsResourceIdPut"></a>
# **setupV1ResourcesIdReassignAppointmentsResourceIdPut**
> List&lt;AppointmentViewModel&gt; setupV1ResourcesIdReassignAppointmentsResourceIdPut(id, resourceId, startDate, endDate, calendarId)

Reassign Resource

&lt;p&gt;Use this endpoint to &lt;b&gt;Reassign&lt;/b&gt; appointments from one resource to another. If the startDate is not supplied, the default is today&#39;s date + 1 day; If the endDate is not supplied, all future appointments from the start date will be reassigned. If the calendar id is not supplied the default is the primary calendar of the location.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of the original resource
    String resourceId = "resourceId_example"; // String | id of the target resource
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | YYYY-MM-DD, Appt range start date
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | YYYY-MM-DD, Appt range end date
    String calendarId = "calendarId_example"; // String | CalendarId of calendar containing appointments
    try {
      List<AppointmentViewModel> result = apiInstance.setupV1ResourcesIdReassignAppointmentsResourceIdPut(id, resourceId, startDate, endDate, calendarId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdReassignAppointmentsResourceIdPut");
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
| **id** | **String**| id of the original resource | |
| **resourceId** | **String**| id of the target resource | |
| **startDate** | **OffsetDateTime**| YYYY-MM-DD, Appt range start date | [optional] |
| **endDate** | **OffsetDateTime**| YYYY-MM-DD, Appt range end date | [optional] |
| **calendarId** | **String**| CalendarId of calendar containing appointments | [optional] |

### Return type

[**List&lt;AppointmentViewModel&gt;**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdRecoverPut"></a>
# **setupV1ResourcesIdRecoverPut**
> ResourceViewModel setupV1ResourcesIdRecoverPut(id, googleAuthReturnUrl, outlookAuthReturnUrl)

Recover Resource

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdRecoverPut(id, googleAuthReturnUrl, outlookAuthReturnUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdRecoverPut");
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
| **id** | **String**| id of resource object | |
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |

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

<a id="setupV1ResourcesIdServicesDelete"></a>
# **setupV1ResourcesIdServicesDelete**
> ResourceViewModel setupV1ResourcesIdServicesDelete(id)

Delete Linked Services

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; linked services from a Resource, i.e. unlink the services. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Once deleted, all services become available to the resource.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdServicesDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdServicesDelete");
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
| **id** | **String**| id of resource object | |

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

<a id="setupV1ResourcesIdServicesPost"></a>
# **setupV1ResourcesIdServicesPost**
> ResourceViewModel setupV1ResourcesIdServicesPost(id, requestBody)

Create Linked Services

&lt;p&gt;Use this endpoint to explicitly &lt;b&gt;Link Services&lt;/b&gt; to a Resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Note:&lt;/b&gt; By default, the services array is empty which signifies that all services are provided by the resource. Linking services here will add to the linked service(s) array available to this resource. This will limit the services available to the resource.&lt;/p&gt;  &lt;p&gt;You cannot post services that already exist in the array, you can only add new ones. Use the &lt;i&gt;PUT ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint to update the entire list.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    List<String> requestBody = Arrays.asList(); // List<String> | Array of valid service object id's
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdServicesPost(id, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdServicesPost");
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
| **id** | **String**| id of resource object | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| Array of valid service object id&#39;s | [optional] |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdServicesPut"></a>
# **setupV1ResourcesIdServicesPut**
> ResourceViewModel setupV1ResourcesIdServicesPut(id, requestBody)

Update Linked Services

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; the linked services of a Resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Updating services with this endpoint will update the linked services available to the resource. Only those services will be available to the resource.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Note:&lt;/b&gt; This is a destructive process, any existing linked services will be removed and replaced with the list of services supplied here. Provide the resources complete list of services when using this endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    List<String> requestBody = Arrays.asList(); // List<String> | Array of valid service object id's
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdServicesPut(id, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdServicesPut");
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
| **id** | **String**| id of resource object | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| Array of valid service object id&#39;s | [optional] |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesIdUploadimagePost"></a>
# **setupV1ResourcesIdUploadimagePost**
> ResourceViewModel setupV1ResourcesIdUploadimagePost(id, resourceImageInputModel)

Upload Resource Image

&lt;p&gt;Use this endpoint to &lt;b&gt;Upload&lt;/b&gt; a resource image to the resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required. You must convert the image to a &lt;b&gt;base64 encoded string&lt;/b&gt; and pass that string as input along with your &lt;b&gt;filename&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String id = "id_example"; // String | id of resource object
    ResourceImageInputModel resourceImageInputModel = new ResourceImageInputModel(); // ResourceImageInputModel | Input model for image upload
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesIdUploadimagePost(id, resourceImageInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesIdUploadimagePost");
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
| **id** | **String**| id of resource object | |
| **resourceImageInputModel** | [**ResourceImageInputModel**](ResourceImageInputModel.md)| Input model for image upload | [optional] |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesPost"></a>
# **setupV1ResourcesPost**
> ResourceViewModel setupV1ResourcesPost(googleAuthReturnUrl, outlookAuthReturnUrl, resourceInputModel)

Create Resource

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new resource.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String googleAuthReturnUrl = "googleAuthReturnUrl_example"; // String | Google calendar authorization return url
    String outlookAuthReturnUrl = "outlookAuthReturnUrl_example"; // String | Outlook calendar authorization return url
    ResourceInputModel resourceInputModel = new ResourceInputModel(); // ResourceInputModel | Resource input model
    try {
      ResourceViewModel result = apiInstance.setupV1ResourcesPost(googleAuthReturnUrl, outlookAuthReturnUrl, resourceInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesPost");
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
| **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] |
| **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] |
| **resourceInputModel** | [**ResourceInputModel**](ResourceInputModel.md)| Resource input model | [optional] |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ResourcesTimezonesGet"></a>
# **setupV1ResourcesTimezonesGet**
> SystemTimezoneViewModel setupV1ResourcesTimezonesGet()

Get Time Zones

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Time Zones&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    try {
      SystemTimezoneViewModel result = apiInstance.setupV1ResourcesTimezonesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#setupV1ResourcesTimezonesGet");
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

[**SystemTimezoneViewModel**](SystemTimezoneViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

