# CustomersDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addressesDeleteAddress**](CustomersDeleteApi.md#addressesDeleteAddress) | **DELETE** /v1/addresses/{guid} | Delete an address. |
| [**contactCommunicationsDeleteContactCommunication**](CustomersDeleteApi.md#contactCommunicationsDeleteContactCommunication) | **DELETE** /v1/contactcommunications/{guid} | Deletes contact&#39;s communication. |
| [**contactsDeleteContact**](CustomersDeleteApi.md#contactsDeleteContact) | **DELETE** /v1/contactpersons/{guid} | Deletes a contact. |
| [**customerCountrySettingsDeleteCustomerCountrySetting**](CustomersDeleteApi.md#customerCountrySettingsDeleteCustomerCountrySetting) | **DELETE** /v1/customercountrysettings/{guid} | Deletes a customer country setting. |
| [**customerCustomValuesDeleteCustomerCustomValue**](CustomersDeleteApi.md#customerCustomValuesDeleteCustomerCustomValue) | **DELETE** /v1/customers/customvalues/{guid} | Deletes a customer custom value. |
| [**customerMarketSegmentsDeleteCustomerMarketSegment**](CustomersDeleteApi.md#customerMarketSegmentsDeleteCustomerMarketSegment) | **DELETE** /v1/customermarketsegments/{guid} | Deletes a customer market segment. |
| [**customersDeleteCustomer**](CustomersDeleteApi.md#customersDeleteCustomer) | **DELETE** /v1/customers/{guid} | Deletes a customer. |
| [**keywordsDeleteContactKeyword**](CustomersDeleteApi.md#keywordsDeleteContactKeyword) | **DELETE** /v1/contacts/{contactGuid}/keywords/{guid} | Delete a keyword from the contact |
| [**salesNotesDeleteCustomerSalesNote**](CustomersDeleteApi.md#salesNotesDeleteCustomerSalesNote) | **DELETE** /v1/customersalesnotes/{guid} | Deletes a customer sales note. |


<a id="addressesDeleteAddress"></a>
# **addressesDeleteAddress**
> addressesDeleteAddress(guid)

Delete an address.

Returns: No Content (204) if succeeded. Not found (404) if address can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the address to delete.
    try {
      apiInstance.addressesDeleteAddress(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#addressesDeleteAddress");
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
| **guid** | **String**| ID for the address to delete. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactCommunicationsDeleteContactCommunication"></a>
# **contactCommunicationsDeleteContactCommunication**
> contactCommunicationsDeleteContactCommunication(guid)

Deletes contact&#39;s communication.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the contact's communication.
    try {
      apiInstance.contactCommunicationsDeleteContactCommunication(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#contactCommunicationsDeleteContactCommunication");
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
| **guid** | **String**| GUID used to delete the contact&#39;s communication. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactsDeleteContact"></a>
# **contactsDeleteContact**
> contactsDeleteContact(guid)

Deletes a contact.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the contact.
    try {
      apiInstance.contactsDeleteContact(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#contactsDeleteContact");
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
| **guid** | **String**| GUID used to delete the contact. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCountrySettingsDeleteCustomerCountrySetting"></a>
# **customerCountrySettingsDeleteCustomerCountrySetting**
> customerCountrySettingsDeleteCustomerCountrySetting(guid)

Deletes a customer country setting.

Returns: No Content (204) if succeeded. Not found (404) if customer country setting can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the customer country setting.
    try {
      apiInstance.customerCountrySettingsDeleteCustomerCountrySetting(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#customerCountrySettingsDeleteCustomerCountrySetting");
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
| **guid** | **String**| GUID used to delete the customer country setting. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomValuesDeleteCustomerCustomValue"></a>
# **customerCustomValuesDeleteCustomerCustomValue**
> customerCustomValuesDeleteCustomerCustomValue(guid)

Deletes a customer custom value.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the customer custom value.
    try {
      apiInstance.customerCustomValuesDeleteCustomerCustomValue(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#customerCustomValuesDeleteCustomerCustomValue");
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
| **guid** | **String**| GUID used to delete the customer custom value. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerMarketSegmentsDeleteCustomerMarketSegment"></a>
# **customerMarketSegmentsDeleteCustomerMarketSegment**
> customerMarketSegmentsDeleteCustomerMarketSegment(guid)

Deletes a customer market segment.

Returns: No Content (204) if succeeded. Not found (404) if customer market segment can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the customer market segment to delete.
    try {
      apiInstance.customerMarketSegmentsDeleteCustomerMarketSegment(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#customerMarketSegmentsDeleteCustomerMarketSegment");
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
| **guid** | **String**| ID for the customer market segment to delete. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customersDeleteCustomer"></a>
# **customersDeleteCustomer**
> customersDeleteCustomer(guid)

Deletes a customer.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the customer.
    try {
      apiInstance.customersDeleteCustomer(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#customersDeleteCustomer");
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
| **guid** | **String**| GUID used to delete the customer. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsDeleteContactKeyword"></a>
# **keywordsDeleteContactKeyword**
> keywordsDeleteContactKeyword(contactGuid, guid)

Delete a keyword from the contact

Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String contactGuid = "contactGuid_example"; // String | 
    String guid = "guid_example"; // String | 
    try {
      apiInstance.keywordsDeleteContactKeyword(contactGuid, guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#keywordsDeleteContactKeyword");
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
| **contactGuid** | **String**|  | |
| **guid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesDeleteCustomerSalesNote"></a>
# **salesNotesDeleteCustomerSalesNote**
> salesNotesDeleteCustomerSalesNote(guid)

Deletes a customer sales note.

Returns: No Content (204) if succeeded. OK (200) if note has child notes and can&#39;t be deleted. It is marked as IsDeleted &#x3D; true. Not found (404) if note can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersDeleteApi apiInstance = new CustomersDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the customer sales note.
    try {
      apiInstance.salesNotesDeleteCustomerSalesNote(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersDeleteApi#salesNotesDeleteCustomerSalesNote");
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
| **guid** | **String**| GUID used to delete the customer sales note. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

