# ScaleUnitsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scaleUnitsCreateFromJson**](ScaleUnitsApi.md#scaleUnitsCreateFromJson) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/createFromJson |  |
| [**scaleUnitsGet**](ScaleUnitsApi.md#scaleUnitsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit} |  |
| [**scaleUnitsList**](ScaleUnitsApi.md#scaleUnitsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits |  |
| [**scaleUnitsScaleOut**](ScaleUnitsApi.md#scaleUnitsScaleOut) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/scaleOut |  |


<a id="scaleUnitsCreateFromJson"></a>
# **scaleUnitsCreateFromJson**
> scaleUnitsCreateFromJson(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, creationData)



Add a new scale unit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScaleUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScaleUnitsApi apiInstance = new ScaleUnitsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    CreateFromJsonScaleUnitParametersList creationData = new CreateFromJsonScaleUnitParametersList(); // CreateFromJsonScaleUnitParametersList | A list of input data that allows for creating the new scale unit.
    try {
      apiInstance.scaleUnitsCreateFromJson(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, creationData);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScaleUnitsApi#scaleUnitsCreateFromJson");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **scaleUnit** | **String**| Name of the scale units. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **creationData** | [**CreateFromJsonScaleUnitParametersList**](CreateFromJsonScaleUnitParametersList.md)| A list of input data that allows for creating the new scale unit. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | ACCEPTED |  -  |

<a id="scaleUnitsGet"></a>
# **scaleUnitsGet**
> ScaleUnit scaleUnitsGet(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion)



Returns the requested scale unit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScaleUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScaleUnitsApi apiInstance = new ScaleUnitsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      ScaleUnit result = apiInstance.scaleUnitsGet(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScaleUnitsApi#scaleUnitsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **scaleUnit** | **String**| Name of the scale units. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**ScaleUnit**](ScaleUnit.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="scaleUnitsList"></a>
# **scaleUnitsList**
> ScaleUnitList scaleUnitsList(subscriptionId, resourceGroupName, location, apiVersion, $filter)



Returns a list of all scale units at a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScaleUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScaleUnitsApi apiInstance = new ScaleUnitsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    String $filter = "$filter_example"; // String | OData filter parameter.
    try {
      ScaleUnitList result = apiInstance.scaleUnitsList(subscriptionId, resourceGroupName, location, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScaleUnitsApi#scaleUnitsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **$filter** | **String**| OData filter parameter. | [optional] |

### Return type

[**ScaleUnitList**](ScaleUnitList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="scaleUnitsScaleOut"></a>
# **scaleUnitsScaleOut**
> scaleUnitsScaleOut(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, scaleUnitNodeParameters)



Scales out a scale unit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScaleUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScaleUnitsApi apiInstance = new ScaleUnitsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    ScaleOutScaleUnitParametersList scaleUnitNodeParameters = new ScaleOutScaleUnitParametersList(); // ScaleOutScaleUnitParametersList | A list of input data that allows for adding a set of scale unit nodes.
    try {
      apiInstance.scaleUnitsScaleOut(subscriptionId, resourceGroupName, location, scaleUnit, apiVersion, scaleUnitNodeParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScaleUnitsApi#scaleUnitsScaleOut");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **scaleUnit** | **String**| Name of the scale units. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **scaleUnitNodeParameters** | [**ScaleOutScaleUnitParametersList**](ScaleOutScaleUnitParametersList.md)| A list of input data that allows for adding a set of scale unit nodes. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | ACCEPTED |  -  |

