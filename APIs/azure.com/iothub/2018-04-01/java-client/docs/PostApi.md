# PostApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotHubResourceCheckNameAvailability**](PostApi.md#iotHubResourceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/checkNameAvailability | Check if an IoT hub name is available |
| [**iotHubResourceExportDevices**](PostApi.md#iotHubResourceExportDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/exportDevices | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities |
| [**iotHubResourceGetKeysForKeyName**](PostApi.md#iotHubResourceGetKeysForKeyName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/IotHubKeys/{keyName}/listkeys | Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security |
| [**iotHubResourceImportDevices**](PostApi.md#iotHubResourceImportDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/importDevices | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities |
| [**iotHubResourceListKeys**](PostApi.md#iotHubResourceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/listkeys | Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security |
| [**iotHubResourceTestAllRoutes**](PostApi.md#iotHubResourceTestAllRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{iotHubName}/routing/routes/$testall | Test all routes |
| [**iotHubResourceTestRoute**](PostApi.md#iotHubResourceTestRoute) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{iotHubName}/routing/routes/$testnew | Test the new route |


<a id="iotHubResourceCheckNameAvailability"></a>
# **iotHubResourceCheckNameAvailability**
> IotHubNameAvailabilityInfo iotHubResourceCheckNameAvailability(apiVersion, subscriptionId, operationInputs)

Check if an IoT hub name is available

Check if an IoT hub name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    OperationInputs operationInputs = new OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the IoT hub to check.
    try {
      IotHubNameAvailabilityInfo result = apiInstance.iotHubResourceCheckNameAvailability(apiVersion, subscriptionId, operationInputs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceCheckNameAvailability");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **operationInputs** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the IoT hub to check. | |

### Return type

[**IotHubNameAvailabilityInfo**](IotHubNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoT hub name is available. If the name is not available, the body contains the reason. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceExportDevices"></a>
# **iotHubResourceExportDevices**
> JobResponse iotHubResourceExportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, exportDevicesParameters)

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    ExportDevicesRequest exportDevicesParameters = new ExportDevicesRequest(); // ExportDevicesRequest | The parameters that specify the export devices operation.
    try {
      JobResponse result = apiInstance.iotHubResourceExportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, exportDevicesParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceExportDevices");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **exportDevicesParameters** | [**ExportDevicesRequest**](ExportDevicesRequest.md)| The parameters that specify the export devices operation. | |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceGetKeysForKeyName"></a>
# **iotHubResourceGetKeysForKeyName**
> SharedAccessSignatureAuthorizationRule iotHubResourceGetKeysForKeyName(apiVersion, subscriptionId, resourceGroupName, resourceName, keyName)

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String keyName = "keyName_example"; // String | The name of the shared access policy.
    try {
      SharedAccessSignatureAuthorizationRule result = apiInstance.iotHubResourceGetKeysForKeyName(apiVersion, subscriptionId, resourceGroupName, resourceName, keyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceGetKeysForKeyName");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **keyName** | **String**| The name of the shared access policy. | |

### Return type

[**SharedAccessSignatureAuthorizationRule**](SharedAccessSignatureAuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized shared access policy, including keys, that you can use to access one or more IoT hub endpoints. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceImportDevices"></a>
# **iotHubResourceImportDevices**
> JobResponse iotHubResourceImportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, importDevicesParameters)

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    ImportDevicesRequest importDevicesParameters = new ImportDevicesRequest(); // ImportDevicesRequest | The parameters that specify the import devices operation.
    try {
      JobResponse result = apiInstance.iotHubResourceImportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, importDevicesParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceImportDevices");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **importDevicesParameters** | [**ImportDevicesRequest**](ImportDevicesRequest.md)| The parameters that specify the import devices operation. | |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceListKeys"></a>
# **iotHubResourceListKeys**
> SharedAccessSignatureAuthorizationRuleListResult iotHubResourceListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security

Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      SharedAccessSignatureAuthorizationRuleListResult result = apiInstance.iotHubResourceListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceListKeys");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |

### Return type

[**SharedAccessSignatureAuthorizationRuleListResult**](SharedAccessSignatureAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of shared access policies, including keys, that you can use to access the IoT hub endpoints. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceTestAllRoutes"></a>
# **iotHubResourceTestAllRoutes**
> TestAllRoutesResult iotHubResourceTestAllRoutes(iotHubName, subscriptionId, resourceGroupName, apiVersion, input)

Test all routes

Test all routes configured in this Iot Hub

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String iotHubName = "iotHubName_example"; // String | IotHub to be tested
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | resource group which Iot Hub belongs to
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    TestAllRoutesInput input = new TestAllRoutesInput(); // TestAllRoutesInput | Input for testing all routes
    try {
      TestAllRoutesResult result = apiInstance.iotHubResourceTestAllRoutes(iotHubName, subscriptionId, resourceGroupName, apiVersion, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceTestAllRoutes");
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
| **iotHubName** | **String**| IotHub to be tested | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| resource group which Iot Hub belongs to | |
| **apiVersion** | **String**| The version of the API. | |
| **input** | [**TestAllRoutesInput**](TestAllRoutesInput.md)| Input for testing all routes | |

### Return type

[**TestAllRoutesResult**](TestAllRoutesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceTestRoute"></a>
# **iotHubResourceTestRoute**
> TestRouteResult iotHubResourceTestRoute(iotHubName, subscriptionId, resourceGroupName, apiVersion, input)

Test the new route

Test the new route for this Iot Hub

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String iotHubName = "iotHubName_example"; // String | IotHub to be tested
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | resource group which Iot Hub belongs to
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    TestRouteInput input = new TestRouteInput(); // TestRouteInput | Route that needs to be tested
    try {
      TestRouteResult result = apiInstance.iotHubResourceTestRoute(iotHubName, subscriptionId, resourceGroupName, apiVersion, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotHubResourceTestRoute");
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
| **iotHubName** | **String**| IotHub to be tested | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| resource group which Iot Hub belongs to | |
| **apiVersion** | **String**| The version of the API. | |
| **input** | [**TestRouteInput**](TestRouteInput.md)| Route that needs to be tested | |

### Return type

[**TestRouteResult**](TestRouteResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | DefaultErrorResponse |  -  |

