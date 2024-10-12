# DbrpsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDBRPID**](DbrpsApi.md#deleteDBRPID) | **DELETE** /dbrps/{dbrpID} | Delete a database retention policy |
| [**getDBRPs**](DbrpsApi.md#getDBRPs) | **GET** /dbrps | List all database retention policy mappings |
| [**getDBRPsID**](DbrpsApi.md#getDBRPsID) | **GET** /dbrps/{dbrpID} | Retrieve a database retention policy mapping |
| [**patchDBRPID**](DbrpsApi.md#patchDBRPID) | **PATCH** /dbrps/{dbrpID} | Update a database retention policy mapping |
| [**postDBRP**](DbrpsApi.md#postDBRP) | **POST** /dbrps | Add a database retention policy mapping |


<a id="deleteDBRPID"></a>
# **deleteDBRPID**
> deleteDBRPID(orgID, dbrpID, zapTraceSpan)

Delete a database retention policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbrpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DbrpsApi apiInstance = new DbrpsApi(defaultClient);
    String orgID = "orgID_example"; // String | Specifies the organization ID of the mapping
    String dbrpID = "dbrpID_example"; // String | The database retention policy mapping
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDBRPID(orgID, dbrpID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbrpsApi#deleteDBRPID");
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
| **orgID** | **String**| Specifies the organization ID of the mapping | |
| **dbrpID** | **String**| The database retention policy mapping | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **400** | if any of the IDs passed is invalid |  -  |
| **0** | Unexpected error |  -  |

<a id="getDBRPs"></a>
# **getDBRPs**
> DBRPs getDBRPs(orgID, zapTraceSpan, id, bucketID, _default, db, rp)

List all database retention policy mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbrpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DbrpsApi apiInstance = new DbrpsApi(defaultClient);
    String orgID = "orgID_example"; // String | Specifies the organization ID to filter on
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String id = "id_example"; // String | Specifies the mapping ID to filter on
    String bucketID = "bucketID_example"; // String | Specifies the bucket ID to filter on
    Boolean _default = true; // Boolean | Specifies filtering on default
    String db = "db_example"; // String | Specifies the database to filter on
    String rp = "rp_example"; // String | Specifies the retention policy to filter on
    try {
      DBRPs result = apiInstance.getDBRPs(orgID, zapTraceSpan, id, bucketID, _default, db, rp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbrpsApi#getDBRPs");
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
| **orgID** | **String**| Specifies the organization ID to filter on | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **id** | **String**| Specifies the mapping ID to filter on | [optional] |
| **bucketID** | **String**| Specifies the bucket ID to filter on | [optional] |
| **_default** | **Boolean**| Specifies filtering on default | [optional] |
| **db** | **String**| Specifies the database to filter on | [optional] |
| **rp** | **String**| Specifies the retention policy to filter on | [optional] |

### Return type

[**DBRPs**](DBRPs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all database retention policy mappings |  -  |
| **400** | if any of the parameter passed is invalid |  -  |
| **0** | Unexpected error |  -  |

<a id="getDBRPsID"></a>
# **getDBRPsID**
> DBRP getDBRPsID(orgID, dbrpID, zapTraceSpan)

Retrieve a database retention policy mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbrpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DbrpsApi apiInstance = new DbrpsApi(defaultClient);
    String orgID = "orgID_example"; // String | Specifies the organization ID of the mapping
    String dbrpID = "dbrpID_example"; // String | The database retention policy mapping ID
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      DBRP result = apiInstance.getDBRPsID(orgID, dbrpID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbrpsApi#getDBRPsID");
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
| **orgID** | **String**| Specifies the organization ID of the mapping | |
| **dbrpID** | **String**| The database retention policy mapping ID | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**DBRP**](DBRP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The database retention policy requested |  -  |
| **400** | if any of the IDs passed is invalid |  -  |
| **0** | Unexpected error |  -  |

<a id="patchDBRPID"></a>
# **patchDBRPID**
> DBRP patchDBRPID(orgID, dbrpID, dbRPUpdate, zapTraceSpan)

Update a database retention policy mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbrpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DbrpsApi apiInstance = new DbrpsApi(defaultClient);
    String orgID = "orgID_example"; // String | Specifies the organization ID of the mapping
    String dbrpID = "dbrpID_example"; // String | The database retention policy mapping.
    DBRPUpdate dbRPUpdate = new DBRPUpdate(); // DBRPUpdate | Database retention policy update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      DBRP result = apiInstance.patchDBRPID(orgID, dbrpID, dbRPUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbrpsApi#patchDBRPID");
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
| **orgID** | **String**| Specifies the organization ID of the mapping | |
| **dbrpID** | **String**| The database retention policy mapping. | |
| **dbRPUpdate** | [**DBRPUpdate**](DBRPUpdate.md)| Database retention policy update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**DBRP**](DBRP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated mapping |  -  |
| **400** | if any of the IDs passed is invalid |  -  |
| **404** | The mapping was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="postDBRP"></a>
# **postDBRP**
> DBRP postDBRP(DBRP, zapTraceSpan)

Add a database retention policy mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbrpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DbrpsApi apiInstance = new DbrpsApi(defaultClient);
    DBRP DBRP = new DBRP(); // DBRP | The database retention policy mapping to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      DBRP result = apiInstance.postDBRP(DBRP, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbrpsApi#postDBRP");
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
| **DBRP** | [**DBRP**](DBRP.md)| The database retention policy mapping to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**DBRP**](DBRP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Database retention policy mapping created |  -  |
| **400** | if any of the IDs in the mapping is invalid |  -  |
| **0** | Unexpected error |  -  |

