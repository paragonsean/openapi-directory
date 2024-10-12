# DataExporterConfigsApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBulkDataExporterConfigs**](DataExporterConfigsApi.md#createBulkDataExporterConfigs) | **POST** /api/data-exporter-configs/_bulk | Create a new data exporter configs |
| [**createDataExporterConfig**](DataExporterConfigsApi.md#createDataExporterConfig) | **POST** /api/data-exporter-configs | Create a new data exporter config |
| [**dataExporterTemplate**](DataExporterConfigsApi.md#dataExporterTemplate) | **GET** /api/data-exporter-configs/_template | Get all data exporter configs |
| [**deleteDataExporterConfig**](DataExporterConfigsApi.md#deleteDataExporterConfig) | **DELETE** /api/data-exporter-configs/{dataExporterConfigId} | Delete a data exporter config |
| [**deletebulkDataExporterConfig**](DataExporterConfigsApi.md#deletebulkDataExporterConfig) | **DELETE** /api/data-exporter-configs/_bulk | Delete a data exporter config |
| [**findAllDataExporters**](DataExporterConfigsApi.md#findAllDataExporters) | **GET** /api/data-exporter-configs | Get all data exporter configs |
| [**findDataExporterConfigById**](DataExporterConfigsApi.md#findDataExporterConfigById) | **GET** /api/data-exporter-configs/{dataExporterConfigId} | Get a data exporter config |
| [**patchBulkDataExporterConfig**](DataExporterConfigsApi.md#patchBulkDataExporterConfig) | **PATCH** /api/data-exporter-configs/_bulk | Update a data exporter configs with a diff |
| [**patchDataExporterConfig**](DataExporterConfigsApi.md#patchDataExporterConfig) | **PATCH** /api/data-exporter-configs/{dataExporterConfigId} | Update a data exporter config with a diff |
| [**updateBulkDataExporterConfig**](DataExporterConfigsApi.md#updateBulkDataExporterConfig) | **PUT** /api/data-exporter-configs/_bulk | Update a data exporter configs |
| [**updateDataExporterConfig**](DataExporterConfigsApi.md#updateDataExporterConfig) | **PUT** /api/data-exporter-configs/{dataExporterConfigId} | Update a data exporter config |


<a id="createBulkDataExporterConfigs"></a>
# **createBulkDataExporterConfigs**
> List&lt;CreateBulkDataExporterConfigs200ResponseInner&gt; createBulkDataExporterConfigs(dataExporterConfig)

Create a new data exporter configs

Create a new data exporter configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    DataExporterConfig dataExporterConfig = new DataExporterConfig(); // DataExporterConfig | 
    try {
      List<CreateBulkDataExporterConfigs200ResponseInner> result = apiInstance.createBulkDataExporterConfigs(dataExporterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#createBulkDataExporterConfigs");
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
| **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] |

### Return type

[**List&lt;CreateBulkDataExporterConfigs200ResponseInner&gt;**](CreateBulkDataExporterConfigs200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/ndjson
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="createDataExporterConfig"></a>
# **createDataExporterConfig**
> DataExporterConfig createDataExporterConfig(dataExporterConfig)

Create a new data exporter config

Create a new data exporter config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    DataExporterConfig dataExporterConfig = new DataExporterConfig(); // DataExporterConfig | 
    try {
      DataExporterConfig result = apiInstance.createDataExporterConfig(dataExporterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#createDataExporterConfig");
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
| **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] |

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="dataExporterTemplate"></a>
# **dataExporterTemplate**
> DataExporterConfig dataExporterTemplate(type)

Get all data exporter configs

Get all data exporter configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    String type = "type_example"; // String | The data exporter config type
    try {
      DataExporterConfig result = apiInstance.dataExporterTemplate(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#dataExporterTemplate");
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
| **type** | **String**| The data exporter config type | [optional] |

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="deleteDataExporterConfig"></a>
# **deleteDataExporterConfig**
> Deleted deleteDataExporterConfig(dataExporterConfigId)

Delete a data exporter config

Delete a data exporter config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    String dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
    try {
      Deleted result = apiInstance.deleteDataExporterConfig(dataExporterConfigId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#deleteDataExporterConfig");
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
| **dataExporterConfigId** | **String**| The data exporter config id | |

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="deletebulkDataExporterConfig"></a>
# **deletebulkDataExporterConfig**
> List&lt;DeletebulkDataExporterConfig200ResponseInner&gt; deletebulkDataExporterConfig(patchInner)

Delete a data exporter config

Delete a data exporter config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      List<DeletebulkDataExporterConfig200ResponseInner> result = apiInstance.deletebulkDataExporterConfig(patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#deletebulkDataExporterConfig");
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
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**List&lt;DeletebulkDataExporterConfig200ResponseInner&gt;**](DeletebulkDataExporterConfig200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/ndjson
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="findAllDataExporters"></a>
# **findAllDataExporters**
> List&lt;DataExporterConfig&gt; findAllDataExporters()

Get all data exporter configs

Get all data exporter configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    try {
      List<DataExporterConfig> result = apiInstance.findAllDataExporters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#findAllDataExporters");
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

[**List&lt;DataExporterConfig&gt;**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="findDataExporterConfigById"></a>
# **findDataExporterConfigById**
> DataExporterConfig findDataExporterConfigById(dataExporterConfigId)

Get a data exporter config

Get a data exporter config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    String dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
    try {
      DataExporterConfig result = apiInstance.findDataExporterConfigById(dataExporterConfigId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#findDataExporterConfigById");
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
| **dataExporterConfigId** | **String**| The data exporter config id | |

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="patchBulkDataExporterConfig"></a>
# **patchBulkDataExporterConfig**
> List&lt;UpdateBulkDataExporterConfig200ResponseInner&gt; patchBulkDataExporterConfig(patchInner)

Update a data exporter configs with a diff

Update a data exporter configs with a diff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      List<UpdateBulkDataExporterConfig200ResponseInner> result = apiInstance.patchBulkDataExporterConfig(patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#patchBulkDataExporterConfig");
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
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**List&lt;UpdateBulkDataExporterConfig200ResponseInner&gt;**](UpdateBulkDataExporterConfig200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/ndjson
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="patchDataExporterConfig"></a>
# **patchDataExporterConfig**
> DataExporterConfig patchDataExporterConfig(dataExporterConfigId, patchInner)

Update a data exporter config with a diff

Update a data exporter config with a diff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    String dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      DataExporterConfig result = apiInstance.patchDataExporterConfig(dataExporterConfigId, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#patchDataExporterConfig");
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
| **dataExporterConfigId** | **String**| The data exporter config id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="updateBulkDataExporterConfig"></a>
# **updateBulkDataExporterConfig**
> List&lt;UpdateBulkDataExporterConfig200ResponseInner&gt; updateBulkDataExporterConfig(dataExporterConfig)

Update a data exporter configs

Update a data exporter configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    DataExporterConfig dataExporterConfig = new DataExporterConfig(); // DataExporterConfig | 
    try {
      List<UpdateBulkDataExporterConfig200ResponseInner> result = apiInstance.updateBulkDataExporterConfig(dataExporterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#updateBulkDataExporterConfig");
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
| **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] |

### Return type

[**List&lt;UpdateBulkDataExporterConfig200ResponseInner&gt;**](UpdateBulkDataExporterConfig200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/ndjson
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="updateDataExporterConfig"></a>
# **updateDataExporterConfig**
> DataExporterConfig updateDataExporterConfig(dataExporterConfigId, dataExporterConfig)

Update a data exporter config

Update a data exporter config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExporterConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    DataExporterConfigsApi apiInstance = new DataExporterConfigsApi(defaultClient);
    String dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
    DataExporterConfig dataExporterConfig = new DataExporterConfig(); // DataExporterConfig | 
    try {
      DataExporterConfig result = apiInstance.updateDataExporterConfig(dataExporterConfigId, dataExporterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExporterConfigsApi#updateDataExporterConfig");
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
| **dataExporterConfigId** | **String**| The data exporter config id | |
| **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] |

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

