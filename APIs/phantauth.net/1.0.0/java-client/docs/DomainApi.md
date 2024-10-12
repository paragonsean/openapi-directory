# DomainApi

All URIs are relative to *https://phantauth.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainDomainnameGet**](DomainApi.md#domainDomainnameGet) | **GET** /domain/{domainname} | Get a Domain |


<a id="domainDomainnameGet"></a>
# **domainDomainnameGet**
> DomainDomainnameGet200Response domainDomainnameGet(domainname)

Get a Domain

This endpoint allows you to get the data of a given PhantAuth domain. To use the PhantAuth services, you don&#39;t need this endpoint. It is, therefore, mainly used for debug/diagnostic purposes in tenant customization.  Domainname is the fully qualified DNS name of the domain you get (e.g. *phantauth.net* or *phantauth.cf*).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    DomainApi apiInstance = new DomainApi(defaultClient);
    String domainname = "domainname_example"; // String | The domain ID integrated in the `sub` property.
    try {
      DomainDomainnameGet200Response result = apiInstance.domainDomainnameGet(domainname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainApi#domainDomainnameGet");
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
| **domainname** | **String**| The domain ID integrated in the &#x60;sub&#x60; property. | |

### Return type

[**DomainDomainnameGet200Response**](DomainDomainnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

