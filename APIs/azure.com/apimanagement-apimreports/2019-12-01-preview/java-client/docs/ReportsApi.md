# ReportsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsListByApi**](ReportsApi.md#reportsListByApi) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byApi |  |
| [**reportsListByGeo**](ReportsApi.md#reportsListByGeo) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byGeo |  |
| [**reportsListByOperation**](ReportsApi.md#reportsListByOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byOperation |  |
| [**reportsListByProduct**](ReportsApi.md#reportsListByProduct) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byProduct |  |
| [**reportsListByRequest**](ReportsApi.md#reportsListByRequest) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byRequest |  |
| [**reportsListBySubscription**](ReportsApi.md#reportsListBySubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/bySubscription |  |
| [**reportsListByTime**](ReportsApi.md#reportsListByTime) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byTime |  |
| [**reportsListByUser**](ReportsApi.md#reportsListByUser) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/reports/byUser |  |


<a id="reportsListByApi"></a>
# **reportsListByApi**
> ReportsListByApi200Response reportsListByApi(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby)



Lists report records by API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    String $orderby = "$orderby_example"; // String | OData order by query option.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListByApi(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByApi");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| The filter to apply on the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **$orderby** | **String**| OData order by query option. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListByGeo"></a>
# **reportsListByGeo**
> ReportsListByApi200Response reportsListByGeo(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip)



Lists report records by geography.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter | ge, le |     | </br>| country | select |     |     | </br>| region | select |     |     | </br>| zip | select |     |     | </br>| apiRegion | filter | eq |     | </br>| userId | filter | eq |     | </br>| productId | filter | eq |     | </br>| subscriptionId | filter | eq |     | </br>| apiId | filter | eq |     | </br>| operationId | filter | eq |     | </br>| callCountSuccess | select |     |     | </br>| callCountBlocked | select |     |     | </br>| callCountFailed | select |     |     | </br>| callCountOther | select |     |     | </br>| bandwidth | select, orderBy |     |     | </br>| cacheHitsCount | select |     |     | </br>| cacheMissCount | select |     |     | </br>| apiTimeAvg | select |     |     | </br>| apiTimeMin | select |     |     | </br>| apiTimeMax | select |     |     | </br>| serviceTimeAvg | select |     |     | </br>| serviceTimeMin | select |     |     | </br>| serviceTimeMax | select |     |     | </br>
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListByGeo(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByGeo");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| country | select |     |     | &lt;/br&gt;| region | select |     |     | &lt;/br&gt;| zip | select |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select |     |     | &lt;/br&gt;| callCountBlocked | select |     |     | &lt;/br&gt;| callCountFailed | select |     |     | &lt;/br&gt;| callCountOther | select |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListByOperation"></a>
# **reportsListByOperation**
> ReportsListByApi200Response reportsListByOperation(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby)



Lists report records by API Operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter | ge, le |     | </br>| displayName | select, orderBy |     |     | </br>| apiRegion | filter | eq |     | </br>| userId | filter | eq |     | </br>| productId | filter | eq |     | </br>| subscriptionId | filter | eq |     | </br>| apiId | filter | eq |     | </br>| operationId | select, filter | eq |     | </br>| callCountSuccess | select, orderBy |     |     | </br>| callCountBlocked | select, orderBy |     |     | </br>| callCountFailed | select, orderBy |     |     | </br>| callCountOther | select, orderBy |     |     | </br>| callCountTotal | select, orderBy |     |     | </br>| bandwidth | select, orderBy |     |     | </br>| cacheHitsCount | select |     |     | </br>| cacheMissCount | select |     |     | </br>| apiTimeAvg | select, orderBy |     |     | </br>| apiTimeMin | select |     |     | </br>| apiTimeMax | select |     |     | </br>| serviceTimeAvg | select |     |     | </br>| serviceTimeMin | select |     |     | </br>| serviceTimeMax | select |     |     | </br>
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    String $orderby = "$orderby_example"; // String | OData order by query option.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListByOperation(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByOperation");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | select, filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **$orderby** | **String**| OData order by query option. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListByProduct"></a>
# **reportsListByProduct**
> ReportsListByApi200Response reportsListByProduct(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby)



Lists report records by Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter | ge, le |     | </br>| displayName | select, orderBy |     |     | </br>| apiRegion | filter | eq |     | </br>| userId | filter | eq |     | </br>| productId | select, filter | eq |     | </br>| subscriptionId | filter | eq |     | </br>| callCountSuccess | select, orderBy |     |     | </br>| callCountBlocked | select, orderBy |     |     | </br>| callCountFailed | select, orderBy |     |     | </br>| callCountOther | select, orderBy |     |     | </br>| callCountTotal | select, orderBy |     |     | </br>| bandwidth | select, orderBy |     |     | </br>| cacheHitsCount | select |     |     | </br>| cacheMissCount | select |     |     | </br>| apiTimeAvg | select, orderBy |     |     | </br>| apiTimeMin | select |     |     | </br>| apiTimeMax | select |     |     | </br>| serviceTimeAvg | select |     |     | </br>| serviceTimeMin | select |     |     | </br>| serviceTimeMax | select |     |     | </br>
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    String $orderby = "$orderby_example"; // String | OData order by query option.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListByProduct(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByProduct");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | select, filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **$orderby** | **String**| OData order by query option. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListByRequest"></a>
# **reportsListByRequest**
> ReportsListByRequest200Response reportsListByRequest(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip)



Lists report records by Request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter | ge, le |     | </br>| apiId | filter | eq |     | </br>| operationId | filter | eq |     | </br>| productId | filter | eq |     | </br>| userId | filter | eq |     | </br>| apiRegion | filter | eq |     | </br>| subscriptionId | filter | eq |     | </br>
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ReportsListByRequest200Response result = apiInstance.reportsListByRequest(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByRequest");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ReportsListByRequest200Response**](ReportsListByRequest200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListBySubscription"></a>
# **reportsListBySubscription**
> ReportsListByApi200Response reportsListBySubscription(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby)



Lists report records by subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter | ge, le |     | </br>| displayName | select, orderBy |     |     | </br>| apiRegion | filter | eq |     | </br>| userId | select, filter | eq |     | </br>| productId | select, filter | eq |     | </br>| subscriptionId | select, filter | eq |     | </br>| callCountSuccess | select, orderBy |     |     | </br>| callCountBlocked | select, orderBy |     |     | </br>| callCountFailed | select, orderBy |     |     | </br>| callCountOther | select, orderBy |     |     | </br>| callCountTotal | select, orderBy |     |     | </br>| bandwidth | select, orderBy |     |     | </br>| cacheHitsCount | select |     |     | </br>| cacheMissCount | select |     |     | </br>| apiTimeAvg | select, orderBy |     |     | </br>| apiTimeMin | select |     |     | </br>| apiTimeMax | select |     |     | </br>| serviceTimeAvg | select |     |     | </br>| serviceTimeMin | select |     |     | </br>| serviceTimeMax | select |     |     | </br>
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    String $orderby = "$orderby_example"; // String | OData order by query option.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListBySubscription(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListBySubscription");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | select, filter | eq |     | &lt;/br&gt;| productId | select, filter | eq |     | &lt;/br&gt;| subscriptionId | select, filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **$orderby** | **String**| OData order by query option. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListByTime"></a>
# **reportsListByTime**
> ReportsListByApi200Response reportsListByTime(resourceGroupName, serviceName, $filter, interval, apiVersion, subscriptionId, $top, $skip, $orderby)



Lists report records by Time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter, select | ge, le |     | </br>| interval | select |     |     | </br>| apiRegion | filter | eq |     | </br>| userId | filter | eq |     | </br>| productId | filter | eq |     | </br>| subscriptionId | filter | eq |     | </br>| apiId | filter | eq |     | </br>| operationId | filter | eq |     | </br>| callCountSuccess | select |     |     | </br>| callCountBlocked | select |     |     | </br>| callCountFailed | select |     |     | </br>| callCountOther | select |     |     | </br>| bandwidth | select, orderBy |     |     | </br>| cacheHitsCount | select |     |     | </br>| cacheMissCount | select |     |     | </br>| apiTimeAvg | select |     |     | </br>| apiTimeMin | select |     |     | </br>| apiTimeMax | select |     |     | </br>| serviceTimeAvg | select |     |     | </br>| serviceTimeMin | select |     |     | </br>| serviceTimeMax | select |     |     | </br>
    String interval = "interval_example"; // String | By time interval. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds)).
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    String $orderby = "$orderby_example"; // String | OData order by query option.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListByTime(resourceGroupName, serviceName, $filter, interval, apiVersion, subscriptionId, $top, $skip, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByTime");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter, select | ge, le |     | &lt;/br&gt;| interval | select |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select |     |     | &lt;/br&gt;| callCountBlocked | select |     |     | &lt;/br&gt;| callCountFailed | select |     |     | &lt;/br&gt;| callCountOther | select |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt; | |
| **interval** | **String**| By time interval. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds)). | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **$orderby** | **String**| OData order by query option. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

<a id="reportsListByUser"></a>
# **reportsListByUser**
> ReportsListByApi200Response reportsListByUser(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby)



Lists report records by User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| timestamp | filter | ge, le |     | </br>| displayName | select, orderBy |     |     | </br>| userId | select, filter | eq |     | </br>| apiRegion | filter | eq |     | </br>| productId | filter | eq |     | </br>| subscriptionId | filter | eq |     | </br>| apiId | filter | eq |     | </br>| operationId | filter | eq |     | </br>| callCountSuccess | select, orderBy |     |     | </br>| callCountBlocked | select, orderBy |     |     | </br>| callCountFailed | select, orderBy |     |     | </br>| callCountOther | select, orderBy |     |     | </br>| callCountTotal | select, orderBy |     |     | </br>| bandwidth | select, orderBy |     |     | </br>| cacheHitsCount | select |     |     | </br>| cacheMissCount | select |     |     | </br>| apiTimeAvg | select, orderBy |     |     | </br>| apiTimeMin | select |     |     | </br>| apiTimeMax | select |     |     | </br>| serviceTimeAvg | select |     |     | </br>| serviceTimeMin | select |     |     | </br>| serviceTimeMax | select |     |     | </br>
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    String $orderby = "$orderby_example"; // String | OData order by query option.
    try {
      ReportsListByApi200Response result = apiInstance.reportsListByUser(resourceGroupName, serviceName, $filter, apiVersion, subscriptionId, $top, $skip, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByUser");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| userId | select, filter | eq |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **$orderby** | **String**| OData order by query option. | [optional] |

### Return type

[**ReportsListByApi200Response**](ReportsListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of Report record. |  -  |

