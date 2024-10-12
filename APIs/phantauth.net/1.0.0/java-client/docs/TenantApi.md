# TenantApi

All URIs are relative to *https://phantauth.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantTenantnameGet**](TenantApi.md#tenantTenantnameGet) | **GET** /tenant/{tenantname} | Get a Tenant |


<a id="tenantTenantnameGet"></a>
# **tenantTenantnameGet**
> TenantTenantnameGet200Response tenantTenantnameGet(tenantname)

Get a Tenant

This endpoint allows you to get the data of a given PhantAuth tenant. To use the PhantAuth services, you don&#39;t need this endpoint. It is, therefore, mainly used for debug/diagnostic purposes in tenant customization.  Tenantname is the name of the full DNS domain of the tenant you get. In the case of an official and shared tenant (phantauth.net and phantauth.cf DNS domains), the DNS domain can be omitted (e.g. *default* or *faker*).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    TenantApi apiInstance = new TenantApi(defaultClient);
    String tenantname = "tenantname_example"; // String | The tenant ID integrated in the `sub` property.
    try {
      TenantTenantnameGet200Response result = apiInstance.tenantTenantnameGet(tenantname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantApi#tenantTenantnameGet");
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
| **tenantname** | **String**| The tenant ID integrated in the &#x60;sub&#x60; property. | |

### Return type

[**TenantTenantnameGet200Response**](TenantTenantnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

