# CadenceImportsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CadenceImportsJsonPost**](CadenceImportsApi.md#v2CadenceImportsJsonPost) | **POST** /v2/cadence_imports.json | Import cadences from JSON |


<a id="v2CadenceImportsJsonPost"></a>
# **v2CadenceImportsJsonPost**
> CadenceImport v2CadenceImportsJsonPost(cadenceContent, settings, sharingSettings)

Import cadences from JSON

New cadences can be created or steps can be imported onto existing cadences which do not have steps. &lt;a href&#x3D;\&quot;/cadence-imports.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;Visit here for more details&lt;/a&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadenceImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadenceImportsApi apiInstance = new CadenceImportsApi(defaultClient);
    Object cadenceContent = null; // Object | Import data for cadence
    Object settings = null; // Object | Settings for a cadence
    Object sharingSettings = null; // Object | The shared settings for a cadence
    try {
      CadenceImport result = apiInstance.v2CadenceImportsJsonPost(cadenceContent, settings, sharingSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadenceImportsApi#v2CadenceImportsJsonPost");
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
| **cadenceContent** | [**Object**](Object.md)| Import data for cadence | [optional] |
| **settings** | [**Object**](Object.md)| Settings for a cadence | [optional] |
| **sharingSettings** | [**Object**](Object.md)| The shared settings for a cadence | [optional] |

### Return type

[**CadenceImport**](CadenceImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

