# CustomersReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addressesGetAddress**](CustomersReadApi.md#addressesGetAddress) | **GET** /v1/addresses/{guid} | Get address by ID. |
| [**addressesGetAddresses**](CustomersReadApi.md#addressesGetAddresses) | **GET** /v1/addresses | Get the addresses. |
| [**addressesGetContactAddress**](CustomersReadApi.md#addressesGetContactAddress) | **GET** /v1/contactpersons/{contactGuid}/addresses | Get contact person&#39;s address |
| [**addressesGetCustomerAddresses**](CustomersReadApi.md#addressesGetCustomerAddresses) | **GET** /v1/customers/{customerGuid}/addresses | Get customer&#39;s addresses |
| [**contactCommunicationsGetCommunication**](CustomersReadApi.md#contactCommunicationsGetCommunication) | **GET** /v1/contactcommunications/{guid} | Get contact communication by ID. |
| [**contactCommunicationsGetCommunications**](CustomersReadApi.md#contactCommunicationsGetCommunications) | **GET** /v1/contactcommunications | Get all contact communications. |
| [**contactCommunicationsGetCommunications2**](CustomersReadApi.md#contactCommunicationsGetCommunications2) | **GET** /v1/contacts/{contactGuid}/contactcommunications | Get all communications for a contact. |
| [**contactsGetContact**](CustomersReadApi.md#contactsGetContact) | **GET** /v1/contactpersons/{guid} | Get contact by ID. |
| [**contactsGetContacts**](CustomersReadApi.md#contactsGetContacts) | **GET** /v1/contactpersons | Get all the contact persons. |
| [**contactsGetCustomerContacts**](CustomersReadApi.md#contactsGetCustomerContacts) | **GET** /v1/customers/{customerGuid}/contactpersons | Get the contact persons for a customer. |
| [**customerCountrySettingsGetCustomerCountrySettings**](CustomersReadApi.md#customerCountrySettingsGetCustomerCountrySettings) | **GET** /v1/customers/{customerGuid}/customercountrysettings | Get all the country settings for a customer. |
| [**customerCustomValuesGetCustomerCustomValue**](CustomersReadApi.md#customerCustomValuesGetCustomerCustomValue) | **GET** /v1/customers/customvalues/{guid} | Get customer custom value by ID. |
| [**customerCustomValuesGetCustomerCustomValues**](CustomersReadApi.md#customerCustomValuesGetCustomerCustomValues) | **GET** /v1/customers/{customerGuid}/customvalues | Get the customer custom values. |
| [**customerMarketSegmentsGetAllCustomerMarketSegments**](CustomersReadApi.md#customerMarketSegmentsGetAllCustomerMarketSegments) | **GET** /v1/customermarketsegments | Get all Customer Market Segments. |
| [**customerMarketSegmentsGetCustomerMarketSegment**](CustomersReadApi.md#customerMarketSegmentsGetCustomerMarketSegment) | **GET** /v1/customermarketsegments/{guid} | Get the customer market segment. |
| [**customerMarketSegmentsGetCustomerMarketSegments**](CustomersReadApi.md#customerMarketSegmentsGetCustomerMarketSegments) | **GET** /v1/customers/{customerGuid}/customermarketsegments | Get the Market Segments for a customer. |
| [**customersGetCustomer**](CustomersReadApi.md#customersGetCustomer) | **GET** /v1/customers/{guid} | Get customer by GUID. |
| [**customersGetCustomers**](CustomersReadApi.md#customersGetCustomers) | **GET** /v1/customers | Get all the customers |
| [**keywordsGetContactKeywords**](CustomersReadApi.md#keywordsGetContactKeywords) | **GET** /v1/contacts/{contactGuid}/keywords | Get all the keywords for contact. |
| [**salesNotesGetAllCustomerSalesNotes_0**](CustomersReadApi.md#salesNotesGetAllCustomerSalesNotes_0) | **GET** /v1/customers/{customerGuid}/salesnotes | Get the sales notes by customer guid. |
| [**salesNotesGetCustomerSalesNote**](CustomersReadApi.md#salesNotesGetCustomerSalesNote) | **GET** /v1/customersalesnotes/{guid} | Get customer sales note by ID. |
| [**salesNotesGetCustomerSalesNotes**](CustomersReadApi.md#salesNotesGetCustomerSalesNotes) | **GET** /v1/customers/{customerGuid}/customersalesnotes | Get the customer sales notes. |


<a id="addressesGetAddress"></a>
# **addressesGetAddress**
> AddressModel addressesGetAddress(guid)

Get address by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the address.
    try {
      AddressModel result = apiInstance.addressesGetAddress(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#addressesGetAddress");
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
| **guid** | **String**| GUID used to get the address. | |

### Return type

[**AddressModel**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="addressesGetAddresses"></a>
# **addressesGetAddresses**
> List&lt;AddressModel&gt; addressesGetAddresses(firstRow, rowCount, calculateRowCount, changedSince)

Get the addresses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get addresses that have been added or changed after this date time (greater or equal).
    try {
      List<AddressModel> result = apiInstance.addressesGetAddresses(firstRow, rowCount, calculateRowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#addressesGetAddresses");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **changedSince** | **OffsetDateTime**| Optional: Get addresses that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;AddressModel&gt;**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="addressesGetContactAddress"></a>
# **addressesGetContactAddress**
> List&lt;AddressModel&gt; addressesGetContactAddress(contactGuid)

Get contact person&#39;s address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String contactGuid = "contactGuid_example"; // String | ID for the contact person
    try {
      List<AddressModel> result = apiInstance.addressesGetContactAddress(contactGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#addressesGetContactAddress");
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
| **contactGuid** | **String**| ID for the contact person | |

### Return type

[**List&lt;AddressModel&gt;**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="addressesGetCustomerAddresses"></a>
# **addressesGetCustomerAddresses**
> List&lt;AddressModel&gt; addressesGetCustomerAddresses(customerGuid, firstRow, rowCount, calculateRowCount)

Get customer&#39;s addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | ID for the customer.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    try {
      List<AddressModel> result = apiInstance.addressesGetCustomerAddresses(customerGuid, firstRow, rowCount, calculateRowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#addressesGetCustomerAddresses");
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
| **customerGuid** | **String**| ID for the customer. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |

### Return type

[**List&lt;AddressModel&gt;**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Addresses for the customer |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactCommunicationsGetCommunication"></a>
# **contactCommunicationsGetCommunication**
> ContactCommunicationModel contactCommunicationsGetCommunication(guid)

Get contact communication by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the contact communication.
    try {
      ContactCommunicationModel result = apiInstance.contactCommunicationsGetCommunication(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#contactCommunicationsGetCommunication");
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
| **guid** | **String**| GUID used to get the contact communication. | |

### Return type

[**ContactCommunicationModel**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact communication. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactCommunicationsGetCommunications"></a>
# **contactCommunicationsGetCommunications**
> List&lt;ContactCommunicationModel&gt; contactCommunicationsGetCommunications(active, firstRow, rowCount, textToSearch, changedSince)

Get all contact communications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from contact communication value.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get contact communications that have been added or changed after this date time (greater or equal).
    try {
      List<ContactCommunicationModel> result = apiInstance.contactCommunicationsGetCommunications(active, firstRow, rowCount, textToSearch, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#contactCommunicationsGetCommunications");
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
| **active** | **Boolean**| If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from contact communication value. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get contact communications that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ContactCommunicationModel&gt;**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the contact communications. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactCommunicationsGetCommunications2"></a>
# **contactCommunicationsGetCommunications2**
> List&lt;ContactCommunicationModel&gt; contactCommunicationsGetCommunications2(contactGuid, active)

Get all communications for a contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String contactGuid = "contactGuid_example"; // String | Whose communications are requested.
    Boolean active = true; // Boolean | If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications.
    try {
      List<ContactCommunicationModel> result = apiInstance.contactCommunicationsGetCommunications2(contactGuid, active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#contactCommunicationsGetCommunications2");
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
| **contactGuid** | **String**| Whose communications are requested. | |
| **active** | **Boolean**| If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications. | [optional] |

### Return type

[**List&lt;ContactCommunicationModel&gt;**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the contact communications. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactsGetContact"></a>
# **contactsGetContact**
> ContactModel contactsGetContact(guid)

Get contact by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the contact.
    try {
      ContactModel result = apiInstance.contactsGetContact(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#contactsGetContact");
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
| **guid** | **String**| GUID used to get the contact. | |

### Return type

[**ContactModel**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactsGetContacts"></a>
# **contactsGetContacts**
> List&lt;ContactModel&gt; contactsGetContacts(active, firstRow, rowCount, textToSearch, searchCriterias, sortings, changedSince)

Get all the contact persons.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from contact person's name or communication method (i.e. phone number or email address).
    List<KeyValuePairOfStringAndObject> searchCriterias = Arrays.asList(); // List<KeyValuePairOfStringAndObject> | Optional: Search criterias.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=FirstName&sortings[0].value=Desc &sortings[1].key=LastName&sortings[1].value=Asc\".
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get contact persons that have been added or changed after this date time (greater or equal).
    try {
      List<ContactModel> result = apiInstance.contactsGetContacts(active, firstRow, rowCount, textToSearch, searchCriterias, sortings, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#contactsGetContacts");
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
| **active** | **Boolean**| If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from contact person&#39;s name or communication method (i.e. phone number or email address). | [optional] [default to ] |
| **searchCriterias** | [**List&lt;KeyValuePairOfStringAndObject&gt;**](KeyValuePairOfStringAndObject.md)| Optional: Search criterias. | [optional] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;FirstName&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;LastName&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get contact persons that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ContactModel&gt;**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of contacts for a customer. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactsGetCustomerContacts"></a>
# **contactsGetCustomerContacts**
> List&lt;ContactModel&gt; contactsGetCustomerContacts(customerGuid, active, firstRow, rowCount, textToSearch)

Get the contact persons for a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | Customer guid used to get the contact persons.
    Boolean active = true; // Boolean | If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from contact person's name or communication method (i.e. phone number or email address).
    try {
      List<ContactModel> result = apiInstance.contactsGetCustomerContacts(customerGuid, active, firstRow, rowCount, textToSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#contactsGetCustomerContacts");
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
| **customerGuid** | **String**| Customer guid used to get the contact persons. | |
| **active** | **Boolean**| If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from contact person&#39;s name or communication method (i.e. phone number or email address). | [optional] [default to ] |

### Return type

[**List&lt;ContactModel&gt;**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of contacts for a customer. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCountrySettingsGetCustomerCountrySettings"></a>
# **customerCountrySettingsGetCustomerCountrySettings**
> List&lt;CustomerCountrySettingsOutputModel&gt; customerCountrySettingsGetCustomerCountrySettings(customerGuid)

Get all the country settings for a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | GUID of the customer.
    try {
      List<CustomerCountrySettingsOutputModel> result = apiInstance.customerCountrySettingsGetCustomerCountrySettings(customerGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customerCountrySettingsGetCustomerCountrySettings");
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
| **customerGuid** | **String**| GUID of the customer. | |

### Return type

[**List&lt;CustomerCountrySettingsOutputModel&gt;**](CustomerCountrySettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Currencies. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomValuesGetCustomerCustomValue"></a>
# **customerCustomValuesGetCustomerCustomValue**
> CustomerCustomValueModel customerCustomValuesGetCustomerCustomValue(guid)

Get customer custom value by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the customer custom value.
    try {
      CustomerCustomValueModel result = apiInstance.customerCustomValuesGetCustomerCustomValue(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customerCustomValuesGetCustomerCustomValue");
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
| **guid** | **String**| Id used to get the customer custom value. | |

### Return type

[**CustomerCustomValueModel**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomValuesGetCustomerCustomValues"></a>
# **customerCustomValuesGetCustomerCustomValues**
> List&lt;CustomerCustomValueModel&gt; customerCustomValuesGetCustomerCustomValues(customerGuid, firstRow, rowCount, active, target, calculateRowCount, sortings)

Get the customer custom values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | ID of the customer.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean active = true; // Boolean | Optional: Get only values of active or inactive customer custom properties.
    List<String> target = Arrays.asList(); // List<String> | List of target for which to get the values.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<CustomerCustomValueModel> result = apiInstance.customerCustomValuesGetCustomerCustomValues(customerGuid, firstRow, rowCount, active, target, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customerCustomValuesGetCustomerCustomValues");
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
| **customerGuid** | **String**| ID of the customer. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **active** | **Boolean**| Optional: Get only values of active or inactive customer custom properties. | [optional] |
| **target** | [**List&lt;String&gt;**](String.md)| List of target for which to get the values. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;CustomerCustomValueModel&gt;**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerMarketSegmentsGetAllCustomerMarketSegments"></a>
# **customerMarketSegmentsGetAllCustomerMarketSegments**
> List&lt;CustomerMarketSegmentModel&gt; customerMarketSegmentsGetAllCustomerMarketSegments(firstRow, rowCount, textToSearch, parentMarketSegmentGuid, includeParentLevel)

Get all Customer Market Segments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from customer market segment name.
    String parentMarketSegmentGuid = "parentMarketSegmentGuid_example"; // String | Optional: Fetches all children of a parent based on parent market segment guid.
    Boolean includeParentLevel = true; // Boolean | Optional: Returns only child segments when false. Has no effect if parentMarketSegmentGuid parameter is defined. Default = true.
    try {
      List<CustomerMarketSegmentModel> result = apiInstance.customerMarketSegmentsGetAllCustomerMarketSegments(firstRow, rowCount, textToSearch, parentMarketSegmentGuid, includeParentLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customerMarketSegmentsGetAllCustomerMarketSegments");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from customer market segment name. | [optional] [default to ] |
| **parentMarketSegmentGuid** | **String**| Optional: Fetches all children of a parent based on parent market segment guid. | [optional] |
| **includeParentLevel** | **Boolean**| Optional: Returns only child segments when false. Has no effect if parentMarketSegmentGuid parameter is defined. Default &#x3D; true. | [optional] [default to true] |

### Return type

[**List&lt;CustomerMarketSegmentModel&gt;**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Customer Market Segments. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerMarketSegmentsGetCustomerMarketSegment"></a>
# **customerMarketSegmentsGetCustomerMarketSegment**
> CustomerMarketSegmentModel customerMarketSegmentsGetCustomerMarketSegment(guid)

Get the customer market segment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | Customer market segment guid.
    try {
      CustomerMarketSegmentModel result = apiInstance.customerMarketSegmentsGetCustomerMarketSegment(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customerMarketSegmentsGetCustomerMarketSegment");
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
| **guid** | **String**| Customer market segment guid. | |

### Return type

[**CustomerMarketSegmentModel**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Customer Market Segments. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerMarketSegmentsGetCustomerMarketSegments"></a>
# **customerMarketSegmentsGetCustomerMarketSegments**
> List&lt;CustomerMarketSegmentModel&gt; customerMarketSegmentsGetCustomerMarketSegments(customerGuid, firstRow, rowCount, includeMarketSegmentsFromRegistry)

Get the Market Segments for a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | ID of the customer.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean includeMarketSegmentsFromRegistry = false; // Boolean | Optional: Return also the markets segments that are not in use for the customer.
    try {
      List<CustomerMarketSegmentModel> result = apiInstance.customerMarketSegmentsGetCustomerMarketSegments(customerGuid, firstRow, rowCount, includeMarketSegmentsFromRegistry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customerMarketSegmentsGetCustomerMarketSegments");
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
| **customerGuid** | **String**| ID of the customer. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **includeMarketSegmentsFromRegistry** | **Boolean**| Optional: Return also the markets segments that are not in use for the customer. | [optional] [default to false] |

### Return type

[**List&lt;CustomerMarketSegmentModel&gt;**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Customer Market Segments. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customersGetCustomer"></a>
# **customersGetCustomer**
> CustomerModel customersGetCustomer(guid)

Get customer by GUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | ID used to get the customer.
    try {
      CustomerModel result = apiInstance.customersGetCustomer(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customersGetCustomer");
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
| **guid** | **String**| ID used to get the customer. | |

### Return type

[**CustomerModel**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customersGetCustomers"></a>
# **customersGetCustomers**
> List&lt;CustomerModel&gt; customersGetCustomers(pageToken, rowCount, isActive, customerOwnerGuids, isInternal, numbers, changedSince, emailAddresses, customerNames)

Get all the customers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | 
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    Boolean isActive = true; // Boolean | If not given, return all Customers, if given as true return only active Customers, if given as false returns only inactive Customers.
    List<String> customerOwnerGuids = Arrays.asList(); // List<String> | Optional: List of customer owner ids to search for. Default all.
    Boolean isInternal = true; // Boolean | Optional: When true returns only internal customer
    List<Long> numbers = Arrays.asList(); // List<Long> | Optional: List of customer numbers.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get customers that have been added or changed after this date time (greater or equal).
    List<String> emailAddresses = Arrays.asList(); // List<String> | Optional: Get customers where email address matches to any provided email address
    List<String> customerNames = Arrays.asList(); // List<String> | Optional: Get customers where customer name matches to any provided customer name
    try {
      List<CustomerModel> result = apiInstance.customersGetCustomers(pageToken, rowCount, isActive, customerOwnerGuids, isInternal, numbers, changedSince, emailAddresses, customerNames);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#customersGetCustomers");
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
| **pageToken** | **String**|  | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **isActive** | **Boolean**| If not given, return all Customers, if given as true return only active Customers, if given as false returns only inactive Customers. | [optional] |
| **customerOwnerGuids** | [**List&lt;String&gt;**](String.md)| Optional: List of customer owner ids to search for. Default all. | [optional] |
| **isInternal** | **Boolean**| Optional: When true returns only internal customer | [optional] |
| **numbers** | [**List&lt;Long&gt;**](Long.md)| Optional: List of customer numbers. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get customers that have been added or changed after this date time (greater or equal). | [optional] |
| **emailAddresses** | [**List&lt;String&gt;**](String.md)| Optional: Get customers where email address matches to any provided email address | [optional] |
| **customerNames** | [**List&lt;String&gt;**](String.md)| Optional: Get customers where customer name matches to any provided customer name | [optional] |

### Return type

[**List&lt;CustomerModel&gt;**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the customers |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsGetContactKeywords"></a>
# **keywordsGetContactKeywords**
> List&lt;KeywordModel&gt; keywordsGetContactKeywords(contactGuid, active, sortings)

Get all the keywords for contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String contactGuid = "contactGuid_example"; // String | ID of the user whose keywords are requested.
    Boolean active = true; // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
    try {
      List<KeywordModel> result = apiInstance.keywordsGetContactKeywords(contactGuid, active, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#keywordsGetContactKeywords");
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
| **contactGuid** | **String**| ID of the user whose keywords are requested. | |
| **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;KeywordModel&gt;**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keywords. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesGetAllCustomerSalesNotes_0"></a>
# **salesNotesGetAllCustomerSalesNotes_0**
> List&lt;SalesNoteOutputModel&gt; salesNotesGetAllCustomerSalesNotes_0(customerGuid, pageToken, rowCount, changedSince)

Get the sales notes by customer guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | Customer guid used to get the notes.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    try {
      List<SalesNoteOutputModel> result = apiInstance.salesNotesGetAllCustomerSalesNotes_0(customerGuid, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#salesNotesGetAllCustomerSalesNotes_0");
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
| **customerGuid** | **String**| Customer guid used to get the notes. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;SalesNoteOutputModel&gt;**](SalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of sales notes for a customer. |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesGetCustomerSalesNote"></a>
# **salesNotesGetCustomerSalesNote**
> CustomerSalesNoteOutputModel salesNotesGetCustomerSalesNote(guid)

Get customer sales note by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the customer sales note.
    try {
      CustomerSalesNoteOutputModel result = apiInstance.salesNotesGetCustomerSalesNote(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#salesNotesGetCustomerSalesNote");
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
| **guid** | **String**| GUID used to get the customer sales note. | |

### Return type

[**CustomerSalesNoteOutputModel**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectNote |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesGetCustomerSalesNotes"></a>
# **salesNotesGetCustomerSalesNotes**
> List&lt;CustomerSalesNoteOutputModel&gt; salesNotesGetCustomerSalesNotes(customerGuid, pageToken, rowCount, changedSince)

Get the customer sales notes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersReadApi;

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

    CustomersReadApi apiInstance = new CustomersReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | Customer guid used to get the notes.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    try {
      List<CustomerSalesNoteOutputModel> result = apiInstance.salesNotesGetCustomerSalesNotes(customerGuid, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersReadApi#salesNotesGetCustomerSalesNotes");
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
| **customerGuid** | **String**| Customer guid used to get the notes. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;CustomerSalesNoteOutputModel&gt;**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of sales notes for a customer. |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

