# EavAttributeSetsAttributeSetIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eavAttributeSetRepositoryV1DeleteByIdDelete**](EavAttributeSetsAttributeSetIdApi.md#eavAttributeSetRepositoryV1DeleteByIdDelete) | **DELETE** /V1/eav/attribute-sets/{attributeSetId} | eav/attribute-sets/{attributeSetId} |
| [**eavAttributeSetRepositoryV1GetGet**](EavAttributeSetsAttributeSetIdApi.md#eavAttributeSetRepositoryV1GetGet) | **GET** /V1/eav/attribute-sets/{attributeSetId} | eav/attribute-sets/{attributeSetId} |
| [**eavAttributeSetRepositoryV1SavePut**](EavAttributeSetsAttributeSetIdApi.md#eavAttributeSetRepositoryV1SavePut) | **PUT** /V1/eav/attribute-sets/{attributeSetId} | eav/attribute-sets/{attributeSetId} |


<a id="eavAttributeSetRepositoryV1DeleteByIdDelete"></a>
# **eavAttributeSetRepositoryV1DeleteByIdDelete**
> Boolean eavAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId)

eav/attribute-sets/{attributeSetId}

Remove attribute set by given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EavAttributeSetsAttributeSetIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    EavAttributeSetsAttributeSetIdApi apiInstance = new EavAttributeSetsAttributeSetIdApi(defaultClient);
    Integer attributeSetId = 56; // Integer | 
    try {
      Boolean result = apiInstance.eavAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EavAttributeSetsAttributeSetIdApi#eavAttributeSetRepositoryV1DeleteByIdDelete");
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
| **attributeSetId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="eavAttributeSetRepositoryV1GetGet"></a>
# **eavAttributeSetRepositoryV1GetGet**
> EavDataAttributeSetInterface eavAttributeSetRepositoryV1GetGet(attributeSetId)

eav/attribute-sets/{attributeSetId}

Retrieve attribute set information based on given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EavAttributeSetsAttributeSetIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    EavAttributeSetsAttributeSetIdApi apiInstance = new EavAttributeSetsAttributeSetIdApi(defaultClient);
    Integer attributeSetId = 56; // Integer | 
    try {
      EavDataAttributeSetInterface result = apiInstance.eavAttributeSetRepositoryV1GetGet(attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EavAttributeSetsAttributeSetIdApi#eavAttributeSetRepositoryV1GetGet");
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
| **attributeSetId** | **Integer**|  | |

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="eavAttributeSetRepositoryV1SavePut"></a>
# **eavAttributeSetRepositoryV1SavePut**
> EavDataAttributeSetInterface eavAttributeSetRepositoryV1SavePut(attributeSetId, eavAttributeSetRepositoryV1SavePutRequest)

eav/attribute-sets/{attributeSetId}

Save attribute set data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EavAttributeSetsAttributeSetIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    EavAttributeSetsAttributeSetIdApi apiInstance = new EavAttributeSetsAttributeSetIdApi(defaultClient);
    String attributeSetId = "attributeSetId_example"; // String | 
    EavAttributeSetRepositoryV1SavePutRequest eavAttributeSetRepositoryV1SavePutRequest = new EavAttributeSetRepositoryV1SavePutRequest(); // EavAttributeSetRepositoryV1SavePutRequest | 
    try {
      EavDataAttributeSetInterface result = apiInstance.eavAttributeSetRepositoryV1SavePut(attributeSetId, eavAttributeSetRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EavAttributeSetsAttributeSetIdApi#eavAttributeSetRepositoryV1SavePut");
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
| **attributeSetId** | **String**|  | |
| **eavAttributeSetRepositoryV1SavePutRequest** | [**EavAttributeSetRepositoryV1SavePutRequest**](EavAttributeSetRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

