# OntologyApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOntDagsUsingGET**](OntologyApi.md#getOntDagsUsingGET) | **GET** /ontology/ont/{accId} | Returns child and parent terms for Accession ID |
| [**getTermUsingGET**](OntologyApi.md#getTermUsingGET) | **GET** /ontology/term/{accId} | Returns term for Accession ID |
| [**isDescendantOfUsingGET**](OntologyApi.md#isDescendantOfUsingGET) | **GET** /ontology/term/{accId1}/{accId2} | Returns true or false for terms |


<a id="getOntDagsUsingGET"></a>
# **getOntDagsUsingGET**
> Map&lt;String, List&lt;String&gt;&gt; getOntDagsUsingGET(accId)

Returns child and parent terms for Accession ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String accId = "accId_example"; // String | Accession ID
    try {
      Map<String, List<String>> result = apiInstance.getOntDagsUsingGET(accId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntDagsUsingGET");
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
| **accId** | **String**| Accession ID | |

### Return type

[**Map&lt;String, List&lt;String&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getTermUsingGET"></a>
# **getTermUsingGET**
> Term getTermUsingGET(accId)

Returns term for Accession ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String accId = "accId_example"; // String | Term Accession ID
    try {
      Term result = apiInstance.getTermUsingGET(accId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getTermUsingGET");
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
| **accId** | **String**| Term Accession ID | |

### Return type

[**Term**](Term.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="isDescendantOfUsingGET"></a>
# **isDescendantOfUsingGET**
> Boolean isDescendantOfUsingGET(accId1, accId2)

Returns true or false for terms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String accId1 = "accId1_example"; // String | Child Term Accession ID
    String accId2 = "accId2_example"; // String | Parent Term Accession ID
    try {
      Boolean result = apiInstance.isDescendantOfUsingGET(accId1, accId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#isDescendantOfUsingGET");
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
| **accId1** | **String**| Child Term Accession ID | |
| **accId2** | **String**| Parent Term Accession ID | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

