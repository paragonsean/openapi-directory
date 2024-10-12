# ServiceFabricSchedulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceFabricSchedulesCreateOrUpdate**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} |  |
| [**serviceFabricSchedulesDelete**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} |  |
| [**serviceFabricSchedulesExecute**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesExecute) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}/execute |  |
| [**serviceFabricSchedulesGet**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} |  |
| [**serviceFabricSchedulesList**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules |  |
| [**serviceFabricSchedulesUpdate**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} |  |


<a id="serviceFabricSchedulesCreateOrUpdate"></a>
# **serviceFabricSchedulesCreateOrUpdate**
> Schedule serviceFabricSchedulesCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule)



Create or replace an existing schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceFabricSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceFabricSchedulesApi apiInstance = new ServiceFabricSchedulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
    String name = "name_example"; // String | The name of the schedule.
    String apiVersion = "2018-09-15"; // String | Client API version.
    Schedule schedule = new Schedule(); // Schedule | A schedule.
    try {
      Schedule result = apiInstance.serviceFabricSchedulesCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceFabricSchedulesApi#serviceFabricSchedulesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **serviceFabricName** | **String**| The name of the service fabric. | |
| **name** | **String**| The name of the schedule. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **schedule** | [**Schedule**](Schedule.md)| A schedule. | |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="serviceFabricSchedulesDelete"></a>
# **serviceFabricSchedulesDelete**
> serviceFabricSchedulesDelete(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion)



Delete schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceFabricSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceFabricSchedulesApi apiInstance = new ServiceFabricSchedulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
    String name = "name_example"; // String | The name of the schedule.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.serviceFabricSchedulesDelete(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceFabricSchedulesApi#serviceFabricSchedulesDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **serviceFabricName** | **String**| The name of the service fabric. | |
| **name** | **String**| The name of the schedule. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="serviceFabricSchedulesExecute"></a>
# **serviceFabricSchedulesExecute**
> serviceFabricSchedulesExecute(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion)



Execute a schedule. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceFabricSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceFabricSchedulesApi apiInstance = new ServiceFabricSchedulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
    String name = "name_example"; // String | The name of the schedule.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.serviceFabricSchedulesExecute(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceFabricSchedulesApi#serviceFabricSchedulesExecute");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **serviceFabricName** | **String**| The name of the service fabric. | |
| **name** | **String**| The name of the schedule. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="serviceFabricSchedulesGet"></a>
# **serviceFabricSchedulesGet**
> Schedule serviceFabricSchedulesGet(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, $expand)



Get schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceFabricSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceFabricSchedulesApi apiInstance = new ServiceFabricSchedulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
    String name = "name_example"; // String | The name of the schedule.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=status)'
    try {
      Schedule result = apiInstance.serviceFabricSchedulesGet(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceFabricSchedulesApi#serviceFabricSchedulesGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **serviceFabricName** | **String**| The name of the service fabric. | |
| **name** | **String**| The name of the schedule. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39; | [optional] |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="serviceFabricSchedulesList"></a>
# **serviceFabricSchedulesList**
> ScheduleList serviceFabricSchedulesList(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, apiVersion, $expand, $filter, $top, $orderby)



List schedules in a given service fabric.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceFabricSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceFabricSchedulesApi apiInstance = new ServiceFabricSchedulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=status)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation. Example: '$top=10'
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    try {
      ScheduleList result = apiInstance.serviceFabricSchedulesList(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceFabricSchedulesApi#serviceFabricSchedulesList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **serviceFabricName** | **String**| The name of the service fabric. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] |

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="serviceFabricSchedulesUpdate"></a>
# **serviceFabricSchedulesUpdate**
> Schedule serviceFabricSchedulesUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule)



Allows modifying tags of schedules. All other properties will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceFabricSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceFabricSchedulesApi apiInstance = new ServiceFabricSchedulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
    String name = "name_example"; // String | The name of the schedule.
    String apiVersion = "2018-09-15"; // String | Client API version.
    ScheduleFragment schedule = new ScheduleFragment(); // ScheduleFragment | A schedule.
    try {
      Schedule result = apiInstance.serviceFabricSchedulesUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceFabricSchedulesApi#serviceFabricSchedulesUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user profile. | |
| **serviceFabricName** | **String**| The name of the service fabric. | |
| **name** | **String**| The name of the schedule. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **schedule** | [**ScheduleFragment**](ScheduleFragment.md)| A schedule. | |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

