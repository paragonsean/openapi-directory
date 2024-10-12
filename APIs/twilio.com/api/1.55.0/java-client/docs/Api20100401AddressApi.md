# Api20100401AddressApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAddress**](Api20100401AddressApi.md#createAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/Addresses.json |  |
| [**deleteAddress**](Api20100401AddressApi.md#deleteAddress) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json |  |
| [**fetchAddress**](Api20100401AddressApi.md#fetchAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json |  |
| [**listAddress**](Api20100401AddressApi.md#listAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses.json |  |
| [**updateAddress**](Api20100401AddressApi.md#updateAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json |  |


<a id="createAddress"></a>
# **createAddress**
> ApiV2010AccountAddress createAddress(accountSid, city, customerName, isoCountry, postalCode, region, street, autoCorrectAddress, emergencyEnabled, friendlyName, streetSecondary)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AddressApi apiInstance = new Api20100401AddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource.
    String city = "city_example"; // String | The city of the new address.
    String customerName = "customerName_example"; // String | The name to associate with the new address.
    String isoCountry = "isoCountry_example"; // String | The ISO country code of the new address.
    String postalCode = "postalCode_example"; // String | The postal code of the new address.
    String region = "region_example"; // String | The state or region of the new address.
    String street = "street_example"; // String | The number and street address of the new address.
    Boolean autoCorrectAddress = true; // Boolean | Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
    Boolean emergencyEnabled = true; // Boolean | Whether to enable emergency calling on the new address. Can be: `true` or `false`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new address. It can be up to 64 characters long.
    String streetSecondary = "streetSecondary_example"; // String | The additional number and street address of the address.
    try {
      ApiV2010AccountAddress result = apiInstance.createAddress(accountSid, city, customerName, isoCountry, postalCode, region, street, autoCorrectAddress, emergencyEnabled, friendlyName, streetSecondary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AddressApi#createAddress");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource. | |
| **city** | **String**| The city of the new address. | |
| **customerName** | **String**| The name to associate with the new address. | |
| **isoCountry** | **String**| The ISO country code of the new address. | |
| **postalCode** | **String**| The postal code of the new address. | |
| **region** | **String**| The state or region of the new address. | |
| **street** | **String**| The number and street address of the new address. | |
| **autoCorrectAddress** | **Boolean**| Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide. | [optional] |
| **emergencyEnabled** | **Boolean**| Whether to enable emergency calling on the new address. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new address. It can be up to 64 characters long. | [optional] |
| **streetSecondary** | **String**| The additional number and street address of the address. | [optional] |

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteAddress"></a>
# **deleteAddress**
> deleteAddress(accountSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AddressApi apiInstance = new Api20100401AddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Address resource to delete.
    try {
      apiInstance.deleteAddress(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AddressApi#deleteAddress");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Address resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchAddress"></a>
# **fetchAddress**
> ApiV2010AccountAddress fetchAddress(accountSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AddressApi apiInstance = new Api20100401AddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Address resource to fetch.
    try {
      ApiV2010AccountAddress result = apiInstance.fetchAddress(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AddressApi#fetchAddress");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Address resource to fetch. | |

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAddress"></a>
# **listAddress**
> ListAddressResponse listAddress(accountSid, customerName, friendlyName, isoCountry, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AddressApi apiInstance = new Api20100401AddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read.
    String customerName = "customerName_example"; // String | The `customer_name` of the Address resources to read.
    String friendlyName = "friendlyName_example"; // String | The string that identifies the Address resources to read.
    String isoCountry = "isoCountry_example"; // String | The ISO country code of the Address resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAddressResponse result = apiInstance.listAddress(accountSid, customerName, friendlyName, isoCountry, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AddressApi#listAddress");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read. | |
| **customerName** | **String**| The &#x60;customer_name&#x60; of the Address resources to read. | [optional] |
| **friendlyName** | **String**| The string that identifies the Address resources to read. | [optional] |
| **isoCountry** | **String**| The ISO country code of the Address resources to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListAddressResponse**](ListAddressResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAddress"></a>
# **updateAddress**
> ApiV2010AccountAddress updateAddress(accountSid, sid, autoCorrectAddress, city, customerName, emergencyEnabled, friendlyName, postalCode, region, street, streetSecondary)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AddressApi apiInstance = new Api20100401AddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Address resource to update.
    Boolean autoCorrectAddress = true; // Boolean | Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
    String city = "city_example"; // String | The city of the address.
    String customerName = "customerName_example"; // String | The name to associate with the address.
    Boolean emergencyEnabled = true; // Boolean | Whether to enable emergency calling on the address. Can be: `true` or `false`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the address. It can be up to 64 characters long.
    String postalCode = "postalCode_example"; // String | The postal code of the address.
    String region = "region_example"; // String | The state or region of the address.
    String street = "street_example"; // String | The number and street address of the address.
    String streetSecondary = "streetSecondary_example"; // String | The additional number and street address of the address.
    try {
      ApiV2010AccountAddress result = apiInstance.updateAddress(accountSid, sid, autoCorrectAddress, city, customerName, emergencyEnabled, friendlyName, postalCode, region, street, streetSecondary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AddressApi#updateAddress");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Address resource to update. | |
| **autoCorrectAddress** | **Boolean**| Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide. | [optional] |
| **city** | **String**| The city of the address. | [optional] |
| **customerName** | **String**| The name to associate with the address. | [optional] |
| **emergencyEnabled** | **Boolean**| Whether to enable emergency calling on the address. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the address. It can be up to 64 characters long. | [optional] |
| **postalCode** | **String**| The postal code of the address. | [optional] |
| **region** | **String**| The state or region of the address. | [optional] |
| **street** | **String**| The number and street address of the address. | [optional] |
| **streetSecondary** | **String**| The additional number and street address of the address. | [optional] |

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

