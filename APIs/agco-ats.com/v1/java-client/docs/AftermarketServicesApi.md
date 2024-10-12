# AftermarketServicesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aftermarketServicesGetCerts**](AftermarketServicesApi.md#aftermarketServicesGetCerts) | **GET** /api/v2/AftermarketServices/Certificates | No Documentation Found. |
| [**aftermarketServicesGetConnectionStatus**](AftermarketServicesApi.md#aftermarketServicesGetConnectionStatus) | **GET** /api/v2/AftermarketServices/Hello | Check whether there is connectivity to AGCO Power Web Services |
| [**aftermarketServicesGetEngineIQACodes**](AftermarketServicesApi.md#aftermarketServicesGetEngineIQACodes) | **GET** /api/v2/AftermarketServices/Engines/{serialNumber}/IQACodes | Get injector codes given engine. |
| [**aftermarketServicesGetProductionData**](AftermarketServicesApi.md#aftermarketServicesGetProductionData) | **GET** /api/v2/AftermarketServices/Engines/{serialNumber}/ProductionData | Get production calibration data for given engine. |
| [**aftermarketServicesGetUserStatus**](AftermarketServicesApi.md#aftermarketServicesGetUserStatus) | **GET** /api/v2/AftermarketServices/UserStatuses | Retrieve the status of an EDT Kit Registration with AGCO Power Web Services |
| [**aftermarketServicesPutECU**](AftermarketServicesApi.md#aftermarketServicesPutECU) | **PUT** /api/v2/AftermarketServices/ECUs/{serialNumber} | Activate or Deactivate an ECU, or Report an ECU as Damaged. |
| [**aftermarketServicesPutIQACodes**](AftermarketServicesApi.md#aftermarketServicesPutIQACodes) | **PUT** /api/v2/AftermarketServices/Engines/{serialNumber}/IQACodes | Report the IQA codes used by an engine |
| [**aftermarketServicesUpdateUserStatus**](AftermarketServicesApi.md#aftermarketServicesUpdateUserStatus) | **PUT** /api/v2/AftermarketServices/UserStatuses | Update the status of an EDT Kit Registration with AGCO Power Web Services |


<a id="aftermarketServicesGetCerts"></a>
# **aftermarketServicesGetCerts**
> Object aftermarketServicesGetCerts()

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    try {
      Object result = apiInstance.aftermarketServicesGetCerts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesGetCerts");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesGetConnectionStatus"></a>
# **aftermarketServicesGetConnectionStatus**
> Boolean aftermarketServicesGetConnectionStatus()

Check whether there is connectivity to AGCO Power Web Services

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    try {
      Boolean result = apiInstance.aftermarketServicesGetConnectionStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesGetConnectionStatus");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesGetEngineIQACodes"></a>
# **aftermarketServicesGetEngineIQACodes**
> List&lt;String&gt; aftermarketServicesGetEngineIQACodes(serialNumber, edTInstanceId)

Get injector codes given engine.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    String serialNumber = "serialNumber_example"; // String | The serial number of the engine.
    String edTInstanceId = "edTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
    try {
      List<String> result = apiInstance.aftermarketServicesGetEngineIQACodes(serialNumber, edTInstanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesGetEngineIQACodes");
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
| **serialNumber** | **String**| The serial number of the engine. | |
| **edTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesGetProductionData"></a>
# **aftermarketServicesGetProductionData**
> List&lt;AGCOPowerServicesModelsProductionData&gt; aftermarketServicesGetProductionData(serialNumber, edTInstanceId)

Get production calibration data for given engine.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    String serialNumber = "serialNumber_example"; // String | The serial number of the engine.
    String edTInstanceId = "edTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
    try {
      List<AGCOPowerServicesModelsProductionData> result = apiInstance.aftermarketServicesGetProductionData(serialNumber, edTInstanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesGetProductionData");
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
| **serialNumber** | **String**| The serial number of the engine. | |
| **edTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | |

### Return type

[**List&lt;AGCOPowerServicesModelsProductionData&gt;**](AGCOPowerServicesModelsProductionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesGetUserStatus"></a>
# **aftermarketServicesGetUserStatus**
> AGCOPowerServicesModelsUserStatus aftermarketServicesGetUserStatus(voucherCode, dealerCode)

Retrieve the status of an EDT Kit Registration with AGCO Power Web Services

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | 
    String dealerCode = "dealerCode_example"; // String | 
    try {
      AGCOPowerServicesModelsUserStatus result = apiInstance.aftermarketServicesGetUserStatus(voucherCode, dealerCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesGetUserStatus");
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
| **voucherCode** | **String**|  | |
| **dealerCode** | **String**|  | |

### Return type

[**AGCOPowerServicesModelsUserStatus**](AGCOPowerServicesModelsUserStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesPutECU"></a>
# **aftermarketServicesPutECU**
> AGCOPowerServicesModelsECU aftermarketServicesPutECU(serialNumber, edTInstanceId, agCOPowerServicesModelsECU)

Activate or Deactivate an ECU, or Report an ECU as Damaged.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    String serialNumber = "serialNumber_example"; // String | The serial number of the ECU.
    String edTInstanceId = "edTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
    AGCOPowerServicesModelsECU agCOPowerServicesModelsECU = new AGCOPowerServicesModelsECU(); // AGCOPowerServicesModelsECU | The ecu to modify.
    try {
      AGCOPowerServicesModelsECU result = apiInstance.aftermarketServicesPutECU(serialNumber, edTInstanceId, agCOPowerServicesModelsECU);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesPutECU");
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
| **serialNumber** | **String**| The serial number of the ECU. | |
| **edTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | |
| **agCOPowerServicesModelsECU** | [**AGCOPowerServicesModelsECU**](AGCOPowerServicesModelsECU.md)| The ecu to modify. | |

### Return type

[**AGCOPowerServicesModelsECU**](AGCOPowerServicesModelsECU.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesPutIQACodes"></a>
# **aftermarketServicesPutIQACodes**
> Boolean aftermarketServicesPutIQACodes(serialNumber, edTInstanceId, requestBody)

Report the IQA codes used by an engine

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    String serialNumber = "serialNumber_example"; // String | The serial number of the Engine
    String edTInstanceId = "edTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
    List<String> requestBody = Arrays.asList(); // List<String> | A string array of IQA codes in physical order
    try {
      Boolean result = apiInstance.aftermarketServicesPutIQACodes(serialNumber, edTInstanceId, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesPutIQACodes");
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
| **serialNumber** | **String**| The serial number of the Engine | |
| **edTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| A string array of IQA codes in physical order | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="aftermarketServicesUpdateUserStatus"></a>
# **aftermarketServicesUpdateUserStatus**
> Boolean aftermarketServicesUpdateUserStatus(agCOPowerServicesModelsUserStatus)

Update the status of an EDT Kit Registration with AGCO Power Web Services

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AftermarketServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AftermarketServicesApi apiInstance = new AftermarketServicesApi(defaultClient);
    AGCOPowerServicesModelsUserStatus agCOPowerServicesModelsUserStatus = new AGCOPowerServicesModelsUserStatus(); // AGCOPowerServicesModelsUserStatus | 
    try {
      Boolean result = apiInstance.aftermarketServicesUpdateUserStatus(agCOPowerServicesModelsUserStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AftermarketServicesApi#aftermarketServicesUpdateUserStatus");
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
| **agCOPowerServicesModelsUserStatus** | [**AGCOPowerServicesModelsUserStatus**](AGCOPowerServicesModelsUserStatus.md)|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

