# DefaultApi

All URIs are relative to *https://azure.local/api/preview*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTokensGet**](DefaultApi.md#apiTokensGet) | **GET** /apiTokens/{token_id} | Get an API token by ID. |
| [**apiTokensList**](DefaultApi.md#apiTokensList) | **GET** /apiTokens | Get the list of API tokens in an application. |
| [**apiTokensRemove**](DefaultApi.md#apiTokensRemove) | **DELETE** /apiTokens/{token_id} | Delete an API token. |
| [**apiTokensSet**](DefaultApi.md#apiTokensSet) | **PUT** /apiTokens/{token_id} | Create a new API token in the application. |
| [**continuousDataExportsGet**](DefaultApi.md#continuousDataExportsGet) | **GET** /continuousDataExports/{export_id} | Get a continuous data export by ID. |
| [**continuousDataExportsList**](DefaultApi.md#continuousDataExportsList) | **GET** /continuousDataExports | Get the list of continuous data exports in an application. |
| [**continuousDataExportsRemove**](DefaultApi.md#continuousDataExportsRemove) | **DELETE** /continuousDataExports/{export_id} | Delete a continuous data export. |
| [**continuousDataExportsSet**](DefaultApi.md#continuousDataExportsSet) | **PUT** /continuousDataExports/{export_id} | Create a new continuous data export or update an existing one by ID. |
| [**deviceTemplatesGet**](DefaultApi.md#deviceTemplatesGet) | **GET** /deviceTemplates/{device_template_id} | Get a device template by ID |
| [**deviceTemplatesGetMerged**](DefaultApi.md#deviceTemplatesGetMerged) | **GET** /deviceTemplates/{device_template_id}/merged | Get a merged device template by ID |
| [**deviceTemplatesList**](DefaultApi.md#deviceTemplatesList) | **GET** /deviceTemplates | Get the list of device templates in an application |
| [**deviceTemplatesListDevices**](DefaultApi.md#deviceTemplatesListDevices) | **GET** /deviceTemplates/{device_template_id}/devices | Get devices for a template |
| [**deviceTemplatesRemove**](DefaultApi.md#deviceTemplatesRemove) | **DELETE** /deviceTemplates/{device_template_id} | Delete a device template |
| [**deviceTemplatesSet**](DefaultApi.md#deviceTemplatesSet) | **PUT** /deviceTemplates/{device_template_id} | Create or update a device template by ID |
| [**devicesExecuteCommand**](DefaultApi.md#devicesExecuteCommand) | **POST** /devices/{device_id}/components/{component_name}/commands/{command_name} | Execute a device command |
| [**devicesGet**](DefaultApi.md#devicesGet) | **GET** /devices/{device_id} | Get a device by ID |
| [**devicesGetCloudProperties**](DefaultApi.md#devicesGetCloudProperties) | **GET** /devices/{device_id}/cloudProperties | Get device cloud properties |
| [**devicesGetCommandHistory**](DefaultApi.md#devicesGetCommandHistory) | **GET** /devices/{device_id}/components/{component_name}/commands/{command_name} | Get device command history |
| [**devicesGetComponentProperties**](DefaultApi.md#devicesGetComponentProperties) | **GET** /devices/{device_id}/components/{component_name}/properties | Get device properties for a specific component |
| [**devicesGetCredentials**](DefaultApi.md#devicesGetCredentials) | **GET** /devices/{device_id}/credentials | Get device credentials |
| [**devicesGetProperties**](DefaultApi.md#devicesGetProperties) | **GET** /devices/{device_id}/properties | Get device properties |
| [**devicesGetTelemetryValue**](DefaultApi.md#devicesGetTelemetryValue) | **GET** /devices/{device_id}/components/{component_name}/telemetry/{telemetry_name} | Get device telemetry value |
| [**devicesList**](DefaultApi.md#devicesList) | **GET** /devices | Get the list of devices in an application |
| [**devicesRemove**](DefaultApi.md#devicesRemove) | **DELETE** /devices/{device_id} | Delete a device |
| [**devicesSet**](DefaultApi.md#devicesSet) | **PUT** /devices/{device_id} | Create or update a device |
| [**devicesUpdateCloudProperties**](DefaultApi.md#devicesUpdateCloudProperties) | **PUT** /devices/{device_id}/cloudProperties | Update device cloud properties |
| [**devicesUpdateComponentProperties**](DefaultApi.md#devicesUpdateComponentProperties) | **PUT** /devices/{device_id}/components/{component_name}/properties | Update device properties for a specific component |
| [**devicesUpdateProperties**](DefaultApi.md#devicesUpdateProperties) | **PUT** /devices/{device_id}/properties | Update device properties |
| [**rolesGet**](DefaultApi.md#rolesGet) | **GET** /roles/{role_id} | Get a role by ID. |
| [**rolesList**](DefaultApi.md#rolesList) | **GET** /roles | Get the list of roles in an application. |


<a id="apiTokensGet"></a>
# **apiTokensGet**
> ApiToken apiTokensGet(tokenId)

Get an API token by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokenId = "tokenId_example"; // String | Unique ID for the API token.
    try {
      ApiToken result = apiInstance.apiTokensGet(tokenId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiTokensGet");
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
| **tokenId** | **String**| Unique ID for the API token. | |

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiTokensList"></a>
# **apiTokensList**
> ApiTokenCollection apiTokensList()

Get the list of API tokens in an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      ApiTokenCollection result = apiInstance.apiTokensList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiTokensList");
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

[**ApiTokenCollection**](ApiTokenCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiTokensRemove"></a>
# **apiTokensRemove**
> apiTokensRemove(tokenId)

Delete an API token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokenId = "tokenId_example"; // String | Unique ID for the API token.
    try {
      apiInstance.apiTokensRemove(tokenId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiTokensRemove");
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
| **tokenId** | **String**| Unique ID for the API token. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="apiTokensSet"></a>
# **apiTokensSet**
> ApiToken apiTokensSet(tokenId, body)

Create a new API token in the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokenId = "tokenId_example"; // String | Unique ID for the API token.
    ApiToken body = new ApiToken(); // ApiToken | API token body.
    try {
      ApiToken result = apiInstance.apiTokensSet(tokenId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiTokensSet");
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
| **tokenId** | **String**| Unique ID for the API token. | |
| **body** | [**ApiToken**](ApiToken.md)| API token body. | |

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="continuousDataExportsGet"></a>
# **continuousDataExportsGet**
> ContinuousDataExport continuousDataExportsGet(exportId)

Get a continuous data export by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "exportId_example"; // String | Unique ID for the continuous data export.
    try {
      ContinuousDataExport result = apiInstance.continuousDataExportsGet(exportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#continuousDataExportsGet");
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
| **exportId** | **String**| Unique ID for the continuous data export. | |

### Return type

[**ContinuousDataExport**](ContinuousDataExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="continuousDataExportsList"></a>
# **continuousDataExportsList**
> ContinuousDataExportCollection continuousDataExportsList()

Get the list of continuous data exports in an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      ContinuousDataExportCollection result = apiInstance.continuousDataExportsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#continuousDataExportsList");
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

[**ContinuousDataExportCollection**](ContinuousDataExportCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="continuousDataExportsRemove"></a>
# **continuousDataExportsRemove**
> continuousDataExportsRemove(exportId)

Delete a continuous data export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "exportId_example"; // String | Unique ID for the continuous data export.
    try {
      apiInstance.continuousDataExportsRemove(exportId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#continuousDataExportsRemove");
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
| **exportId** | **String**| Unique ID for the continuous data export. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="continuousDataExportsSet"></a>
# **continuousDataExportsSet**
> ContinuousDataExport continuousDataExportsSet(exportId, body)

Create a new continuous data export or update an existing one by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "exportId_example"; // String | Unique ID for the continuous data export.
    ContinuousDataExport body = new ContinuousDataExport(); // ContinuousDataExport | Data export body.
    try {
      ContinuousDataExport result = apiInstance.continuousDataExportsSet(exportId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#continuousDataExportsSet");
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
| **exportId** | **String**| Unique ID for the continuous data export. | |
| **body** | [**ContinuousDataExport**](ContinuousDataExport.md)| Data export body. | |

### Return type

[**ContinuousDataExport**](ContinuousDataExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deviceTemplatesGet"></a>
# **deviceTemplatesGet**
> DeviceTemplate deviceTemplatesGet(deviceTemplateId)

Get a device template by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
    try {
      DeviceTemplate result = apiInstance.deviceTemplatesGet(deviceTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deviceTemplatesGet");
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
| **deviceTemplateId** | **String**| Unique ID of the device template. | |

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deviceTemplatesGetMerged"></a>
# **deviceTemplatesGetMerged**
> DeviceTemplate deviceTemplatesGetMerged(deviceTemplateId)

Get a merged device template by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
    try {
      DeviceTemplate result = apiInstance.deviceTemplatesGetMerged(deviceTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deviceTemplatesGetMerged");
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
| **deviceTemplateId** | **String**| Unique ID of the device template. | |

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deviceTemplatesList"></a>
# **deviceTemplatesList**
> DeviceTemplateCollection deviceTemplatesList()

Get the list of device templates in an application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      DeviceTemplateCollection result = apiInstance.deviceTemplatesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deviceTemplatesList");
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

[**DeviceTemplateCollection**](DeviceTemplateCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deviceTemplatesListDevices"></a>
# **deviceTemplatesListDevices**
> DeviceCollection deviceTemplatesListDevices(deviceTemplateId)

Get devices for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
    try {
      DeviceCollection result = apiInstance.deviceTemplatesListDevices(deviceTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deviceTemplatesListDevices");
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
| **deviceTemplateId** | **String**| Unique ID of the device template. | |

### Return type

[**DeviceCollection**](DeviceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deviceTemplatesRemove"></a>
# **deviceTemplatesRemove**
> deviceTemplatesRemove(deviceTemplateId)

Delete a device template

Delete an existing device template by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
    try {
      apiInstance.deviceTemplatesRemove(deviceTemplateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deviceTemplatesRemove");
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
| **deviceTemplateId** | **String**| Unique ID of the device template. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="deviceTemplatesSet"></a>
# **deviceTemplatesSet**
> DeviceTemplate deviceTemplatesSet(deviceTemplateId, body)

Create or update a device template by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
    DeviceTemplate body = new DeviceTemplate(); // DeviceTemplate | Device template body.
    try {
      DeviceTemplate result = apiInstance.deviceTemplatesSet(deviceTemplateId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deviceTemplatesSet");
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
| **deviceTemplateId** | **String**| Unique ID of the device template. | |
| **body** | [**DeviceTemplate**](DeviceTemplate.md)| Device template body. | |

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesExecuteCommand"></a>
# **devicesExecuteCommand**
> DeviceCommand devicesExecuteCommand(deviceId, componentName, commandName, body)

Execute a device command

Execute a command on a device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    String componentName = "componentName_example"; // String | Name of the device component.
    String commandName = "commandName_example"; // String | Name of this device command.
    DeviceCommand body = new DeviceCommand(); // DeviceCommand | Device command body.
    try {
      DeviceCommand result = apiInstance.devicesExecuteCommand(deviceId, componentName, commandName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesExecuteCommand");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **componentName** | **String**| Name of the device component. | |
| **commandName** | **String**| Name of this device command. | |
| **body** | [**DeviceCommand**](DeviceCommand.md)| Device command body. | |

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

<a id="devicesGet"></a>
# **devicesGet**
> Device devicesGet(deviceId)

Get a device by ID

Get details about an existing device by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    try {
      Device result = apiInstance.devicesGet(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGet");
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
| **deviceId** | **String**| Unique ID of the device. | |

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesGetCloudProperties"></a>
# **devicesGetCloudProperties**
> Map&lt;String, Object&gt; devicesGetCloudProperties(deviceId)

Get device cloud properties

Get all cloud property values of a device by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    try {
      Map<String, Object> result = apiInstance.devicesGetCloudProperties(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGetCloudProperties");
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
| **deviceId** | **String**| Unique ID of the device. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesGetCommandHistory"></a>
# **devicesGetCommandHistory**
> DeviceCommandCollection devicesGetCommandHistory(deviceId, componentName, commandName)

Get device command history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    String componentName = "componentName_example"; // String | Name of the device component.
    String commandName = "commandName_example"; // String | Name of this device command.
    try {
      DeviceCommandCollection result = apiInstance.devicesGetCommandHistory(deviceId, componentName, commandName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGetCommandHistory");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **componentName** | **String**| Name of the device component. | |
| **commandName** | **String**| Name of this device command. | |

### Return type

[**DeviceCommandCollection**](DeviceCommandCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesGetComponentProperties"></a>
# **devicesGetComponentProperties**
> Map&lt;String, Object&gt; devicesGetComponentProperties(deviceId, componentName)

Get device properties for a specific component

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    String componentName = "componentName_example"; // String | Name of the device component.
    try {
      Map<String, Object> result = apiInstance.devicesGetComponentProperties(deviceId, componentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGetComponentProperties");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **componentName** | **String**| Name of the device component. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesGetCredentials"></a>
# **devicesGetCredentials**
> DeviceCredentials devicesGetCredentials(deviceId)

Get device credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    try {
      DeviceCredentials result = apiInstance.devicesGetCredentials(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGetCredentials");
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
| **deviceId** | **String**| Unique ID of the device. | |

### Return type

[**DeviceCredentials**](DeviceCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesGetProperties"></a>
# **devicesGetProperties**
> Map&lt;String, Object&gt; devicesGetProperties(deviceId)

Get device properties

Get all property values of a device by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    try {
      Map<String, Object> result = apiInstance.devicesGetProperties(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGetProperties");
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
| **deviceId** | **String**| Unique ID of the device. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesGetTelemetryValue"></a>
# **devicesGetTelemetryValue**
> Value devicesGetTelemetryValue(deviceId, componentName, telemetryName)

Get device telemetry value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    String componentName = "componentName_example"; // String | Name of the device component.
    String telemetryName = "telemetryName_example"; // String | Name of this device telemetry.
    try {
      Value result = apiInstance.devicesGetTelemetryValue(deviceId, componentName, telemetryName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesGetTelemetryValue");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **componentName** | **String**| Name of the device component. | |
| **telemetryName** | **String**| Name of this device telemetry. | |

### Return type

[**Value**](Value.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesList"></a>
# **devicesList**
> DeviceCollection devicesList()

Get the list of devices in an application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      DeviceCollection result = apiInstance.devicesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesList");
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

[**DeviceCollection**](DeviceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesRemove"></a>
# **devicesRemove**
> devicesRemove(deviceId)

Delete a device

Delete an existing device by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    try {
      apiInstance.devicesRemove(deviceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesRemove");
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
| **deviceId** | **String**| Unique ID of the device. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="devicesSet"></a>
# **devicesSet**
> Device devicesSet(deviceId, body)

Create or update a device

Create a new device or update an existing one by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    Device body = new Device(); // Device | Device body.
    try {
      Device result = apiInstance.devicesSet(deviceId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesSet");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **body** | [**Device**](Device.md)| Device body. | |

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesUpdateCloudProperties"></a>
# **devicesUpdateCloudProperties**
> Map&lt;String, Object&gt; devicesUpdateCloudProperties(deviceId, body)

Update device cloud properties

Update all cloud property values of a device by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    Map<String, Object> body = null; // Map<String, Object> | Device properties.
    try {
      Map<String, Object> result = apiInstance.devicesUpdateCloudProperties(deviceId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesUpdateCloudProperties");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **body** | [**Map&lt;String, Object&gt;**](Object.md)| Device properties. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="devicesUpdateComponentProperties"></a>
# **devicesUpdateComponentProperties**
> Map&lt;String, Object&gt; devicesUpdateComponentProperties(deviceId, componentName, body)

Update device properties for a specific component

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    String componentName = "componentName_example"; // String | Name of the device component.
    Map<String, Object> body = null; // Map<String, Object> | Device properties.
    try {
      Map<String, Object> result = apiInstance.devicesUpdateComponentProperties(deviceId, componentName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesUpdateComponentProperties");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **componentName** | **String**| Name of the device component. | |
| **body** | [**Map&lt;String, Object&gt;**](Object.md)| Device properties. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |

<a id="devicesUpdateProperties"></a>
# **devicesUpdateProperties**
> Map&lt;String, Object&gt; devicesUpdateProperties(deviceId, body)

Update device properties

Update all property values of a device by device ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique ID of the device.
    Map<String, Object> body = null; // Map<String, Object> | Device properties.
    try {
      Map<String, Object> result = apiInstance.devicesUpdateProperties(deviceId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#devicesUpdateProperties");
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
| **deviceId** | **String**| Unique ID of the device. | |
| **body** | [**Map&lt;String, Object&gt;**](Object.md)| Device properties. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |

<a id="rolesGet"></a>
# **rolesGet**
> Role rolesGet(roleId)

Get a role by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String roleId = "roleId_example"; // String | Unique ID for the role.
    try {
      Role result = apiInstance.rolesGet(roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rolesGet");
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
| **roleId** | **String**| Unique ID for the role. | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="rolesList"></a>
# **rolesList**
> RoleCollection rolesList()

Get the list of roles in an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/api/preview");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      RoleCollection result = apiInstance.rolesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rolesList");
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

[**RoleCollection**](RoleCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

