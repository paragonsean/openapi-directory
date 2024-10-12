# AddressesApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAddress**](AddressesApi.md#addAddress) | **POST** /addresses | Claim a new Mailscript address |
| [**deleteAddress**](AddressesApi.md#deleteAddress) | **DELETE** /addresses/{address} | Delete a mailscript address |
| [**getAllAddresses**](AddressesApi.md#getAllAddresses) | **GET** /addresses | Get all addresses you have access to |


<a id="addAddress"></a>
# **addAddress**
> addAddress(addAddressRequest)

Claim a new Mailscript address



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    AddAddressRequest addAddressRequest = new AddAddressRequest(); // AddAddressRequest | Address body
    try {
      apiInstance.addAddress(addAddressRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#addAddress");
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
| **addAddressRequest** | [**AddAddressRequest**](AddAddressRequest.md)| Address body | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Internal error |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="deleteAddress"></a>
# **deleteAddress**
> deleteAddress(address)

Delete a mailscript address



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String address = "address_example"; // String | ID of address
    try {
      apiInstance.deleteAddress(address);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#deleteAddress");
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
| **address** | **String**| ID of address | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful delete operation |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="getAllAddresses"></a>
# **getAllAddresses**
> GetAllAddressesResponse getAllAddresses()

Get all addresses you have access to



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    try {
      GetAllAddressesResponse result = apiInstance.getAllAddresses();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getAllAddresses");
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

[**GetAllAddressesResponse**](GetAllAddressesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

