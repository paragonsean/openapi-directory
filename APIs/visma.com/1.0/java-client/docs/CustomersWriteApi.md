# CustomersWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addressesPatchAddress**](CustomersWriteApi.md#addressesPatchAddress) | **PATCH** /v1/addresses/{guid} | Update (Patch) an address or a part of it. |
| [**addressesPostCustomerAddress**](CustomersWriteApi.md#addressesPostCustomerAddress) | **POST** /v1/customers/{customerGuid}/addresses | Insert an address. |
| [**contactCommunicationsPatchContactCommunication**](CustomersWriteApi.md#contactCommunicationsPatchContactCommunication) | **PATCH** /v1/contactcommunications/{guid} | Update (Patch) a contact&#39;s communication or a part of it. |
| [**contactCommunicationsPostContactCommunication**](CustomersWriteApi.md#contactCommunicationsPostContactCommunication) | **POST** /v1/contactcommunications | Insert a communication for a contact. |
| [**contactsPatchContact**](CustomersWriteApi.md#contactsPatchContact) | **PATCH** /v1/contactpersons/{guid} | Update (Patch) an contact or a part of it. |
| [**contactsPostContact**](CustomersWriteApi.md#contactsPostContact) | **POST** /v1/contactpersons | Insert a contact. |
| [**customerCountrySettingsPatchCustomerCountrySettings**](CustomersWriteApi.md#customerCountrySettingsPatchCustomerCountrySettings) | **PATCH** /v1/customercountrysettings/{guid} | Update (Patch) a customer country setting. |
| [**customerCountrySettingsPostCustomerCountrySettings**](CustomersWriteApi.md#customerCountrySettingsPostCustomerCountrySettings) | **POST** /v1/customercountrysettings | Insert a customer country setting. |
| [**customerCustomValuesPatchCustomerCustomValue**](CustomersWriteApi.md#customerCustomValuesPatchCustomerCustomValue) | **PATCH** /v1/customers/customvalues/{guid} | Update (Patch) a customer custom value or a part of it. |
| [**customerCustomValuesPostCustomerCustomValue**](CustomersWriteApi.md#customerCustomValuesPostCustomerCustomValue) | **POST** /v1/customers/customvalues | Insert a customer custom value. |
| [**customerMarketSegmentsPostCustomerMarketSegment**](CustomersWriteApi.md#customerMarketSegmentsPostCustomerMarketSegment) | **POST** /v1/customermarketsegments | Add a market segment for customer. |
| [**customersPatchCustomer**](CustomersWriteApi.md#customersPatchCustomer) | **PATCH** /v1/customers/{guid} | Update (Patch) an customer or a part of it. |
| [**customersPostCustomer**](CustomersWriteApi.md#customersPostCustomer) | **POST** /v1/customers | Insert a customer. |
| [**keywordsLinkKeywordToContact**](CustomersWriteApi.md#keywordsLinkKeywordToContact) | **POST** /v1/contacts/{contactGuid}/keywords/{guid} | Link existing keyword to contact |
| [**salesNotesPatchCustomerSalesNote**](CustomersWriteApi.md#salesNotesPatchCustomerSalesNote) | **PATCH** /v1/customersalesnotes/{guid} | Update (Patch) a customer sales note or a part of it. |
| [**salesNotesPostCustomerSalesNotes**](CustomersWriteApi.md#salesNotesPostCustomerSalesNotes) | **POST** /v1/customersalesnotes | Insert a customer sales note. |


<a id="addressesPatchAddress"></a>
# **addressesPatchAddress**
> List&lt;AddressModel&gt; addressesPatchAddress(guid, patchOperation)

Update (Patch) an address or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the address.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of AddressModel.
    try {
      List<AddressModel> result = apiInstance.addressesPatchAddress(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#addressesPatchAddress");
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
| **guid** | **String**| ID of the address. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of AddressModel. | [optional] |

### Return type

[**List&lt;AddressModel&gt;**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated addresses. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="addressesPostCustomerAddress"></a>
# **addressesPostCustomerAddress**
> AddressModel addressesPostCustomerAddress(customerGuid, addressModel)

Insert an address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | ID of the customer to add the address for.
    AddressModel addressModel = new AddressModel(); // AddressModel | AddressModel.
    try {
      AddressModel result = apiInstance.addressesPostCustomerAddress(customerGuid, addressModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#addressesPostCustomerAddress");
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
| **customerGuid** | **String**| ID of the customer to add the address for. | |
| **addressModel** | [**AddressModel**](AddressModel.md)| AddressModel. | [optional] |

### Return type

[**AddressModel**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created address. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactCommunicationsPatchContactCommunication"></a>
# **contactCommunicationsPatchContactCommunication**
> ContactCommunicationModel contactCommunicationsPatchContactCommunication(guid, patchOperation)

Update (Patch) a contact&#39;s communication or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the contact's communication.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ContactCommunicationModel.
    try {
      ContactCommunicationModel result = apiInstance.contactCommunicationsPatchContactCommunication(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#contactCommunicationsPatchContactCommunication");
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
| **guid** | **String**| ID of the contact&#39;s communication. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ContactCommunicationModel. | [optional] |

### Return type

[**ContactCommunicationModel**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated contact communication model. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactCommunicationsPostContactCommunication"></a>
# **contactCommunicationsPostContactCommunication**
> ContactCommunicationModel contactCommunicationsPostContactCommunication(contactCommunicationModel)

Insert a communication for a contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    ContactCommunicationModel contactCommunicationModel = new ContactCommunicationModel(); // ContactCommunicationModel | ContactCommunicationModel.
    try {
      ContactCommunicationModel result = apiInstance.contactCommunicationsPostContactCommunication(contactCommunicationModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#contactCommunicationsPostContactCommunication");
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
| **contactCommunicationModel** | [**ContactCommunicationModel**](ContactCommunicationModel.md)| ContactCommunicationModel. | [optional] |

### Return type

[**ContactCommunicationModel**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted contact communication. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactsPatchContact"></a>
# **contactsPatchContact**
> List&lt;ContactModel&gt; contactsPatchContact(guid, patchOperation)

Update (Patch) an contact or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the contact.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ContactModel.
    try {
      List<ContactModel> result = apiInstance.contactsPatchContact(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#contactsPatchContact");
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
| **guid** | **String**| ID of the contact. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ContactModel. | [optional] |

### Return type

[**List&lt;ContactModel&gt;**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated contact persons. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactsPostContact"></a>
# **contactsPostContact**
> ContactModel contactsPostContact(contactModel)

Insert a contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    ContactModel contactModel = new ContactModel(); // ContactModel | ContactModel.
    try {
      ContactModel result = apiInstance.contactsPostContact(contactModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#contactsPostContact");
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
| **contactModel** | [**ContactModel**](ContactModel.md)| ContactModel. | [optional] |

### Return type

[**ContactModel**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted contact. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCountrySettingsPatchCustomerCountrySettings"></a>
# **customerCountrySettingsPatchCustomerCountrySettings**
> List&lt;CustomerCountrySettingsOutputModel&gt; customerCountrySettingsPatchCustomerCountrySettings(guid, patchOperation)

Update (Patch) a customer country setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the customer country setting.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of CustomerCountrySettingsModel.
    try {
      List<CustomerCountrySettingsOutputModel> result = apiInstance.customerCountrySettingsPatchCustomerCountrySettings(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customerCountrySettingsPatchCustomerCountrySettings");
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
| **guid** | **String**| ID of the customer country setting. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of CustomerCountrySettingsModel. | [optional] |

### Return type

[**List&lt;CustomerCountrySettingsOutputModel&gt;**](CustomerCountrySettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated customer country settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCountrySettingsPostCustomerCountrySettings"></a>
# **customerCountrySettingsPostCustomerCountrySettings**
> CustomerCountrySettingsOutputModel customerCountrySettingsPostCustomerCountrySettings(customerCountrySettingsInputModel)

Insert a customer country setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    CustomerCountrySettingsInputModel customerCountrySettingsInputModel = new CustomerCountrySettingsInputModel(); // CustomerCountrySettingsInputModel | CustomerCountrySettingsModel.
    try {
      CustomerCountrySettingsOutputModel result = apiInstance.customerCountrySettingsPostCustomerCountrySettings(customerCountrySettingsInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customerCountrySettingsPostCustomerCountrySettings");
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
| **customerCountrySettingsInputModel** | [**CustomerCountrySettingsInputModel**](CustomerCountrySettingsInputModel.md)| CustomerCountrySettingsModel. | [optional] |

### Return type

[**CustomerCountrySettingsOutputModel**](CustomerCountrySettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted customer country setting. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomValuesPatchCustomerCustomValue"></a>
# **customerCustomValuesPatchCustomerCustomValue**
> List&lt;CustomerCustomValueModel&gt; customerCustomValuesPatchCustomerCustomValue(guid, patchOperation)

Update (Patch) a customer custom value or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the customer custom value Can also be comma separate list of IDs to patch multiple customer custom values with one call. When multiple IDs are given, returns model which has list of succeeded customer custom values and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of CustomerCustomValueModel.
    try {
      List<CustomerCustomValueModel> result = apiInstance.customerCustomValuesPatchCustomerCustomValue(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customerCustomValuesPatchCustomerCustomValue");
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
| **guid** | **String**| ID of the customer custom value Can also be comma separate list of IDs to patch multiple customer custom values with one call. When multiple IDs are given, returns model which has list of succeeded customer custom values and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of CustomerCustomValueModel. | [optional] |

### Return type

[**List&lt;CustomerCustomValueModel&gt;**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated customer custom values. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomValuesPostCustomerCustomValue"></a>
# **customerCustomValuesPostCustomerCustomValue**
> List&lt;CustomerCustomValueModel&gt; customerCustomValuesPostCustomerCustomValue(customerCustomValueModel)

Insert a customer custom value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    CustomerCustomValueModel customerCustomValueModel = new CustomerCustomValueModel(); // CustomerCustomValueModel | CustomerCustomValueModel.
    try {
      List<CustomerCustomValueModel> result = apiInstance.customerCustomValuesPostCustomerCustomValue(customerCustomValueModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customerCustomValuesPostCustomerCustomValue");
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
| **customerCustomValueModel** | [**CustomerCustomValueModel**](CustomerCustomValueModel.md)| CustomerCustomValueModel. | [optional] |

### Return type

[**List&lt;CustomerCustomValueModel&gt;**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created customer custom value. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerMarketSegmentsPostCustomerMarketSegment"></a>
# **customerMarketSegmentsPostCustomerMarketSegment**
> CustomerMarketSegmentModel customerMarketSegmentsPostCustomerMarketSegment(customerMarketSegmentModel)

Add a market segment for customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    CustomerMarketSegmentModel customerMarketSegmentModel = new CustomerMarketSegmentModel(); // CustomerMarketSegmentModel | CustomerMarketSegmentModel.
    try {
      CustomerMarketSegmentModel result = apiInstance.customerMarketSegmentsPostCustomerMarketSegment(customerMarketSegmentModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customerMarketSegmentsPostCustomerMarketSegment");
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
| **customerMarketSegmentModel** | [**CustomerMarketSegmentModel**](CustomerMarketSegmentModel.md)| CustomerMarketSegmentModel. | [optional] |

### Return type

[**CustomerMarketSegmentModel**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created customer market segment. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customersPatchCustomer"></a>
# **customersPatchCustomer**
> List&lt;CustomerModel&gt; customersPatchCustomer(guid, patchOperation)

Update (Patch) an customer or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the customer.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of CustomerModel.
    try {
      List<CustomerModel> result = apiInstance.customersPatchCustomer(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customersPatchCustomer");
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
| **guid** | **String**| ID of the customer. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of CustomerModel. | [optional] |

### Return type

[**List&lt;CustomerModel&gt;**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated customers. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customersPostCustomer"></a>
# **customersPostCustomer**
> CustomerModel customersPostCustomer(customerModel)

Insert a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    CustomerModel customerModel = new CustomerModel(); // CustomerModel | CustomerModel.
    try {
      CustomerModel result = apiInstance.customersPostCustomer(customerModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#customersPostCustomer");
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
| **customerModel** | [**CustomerModel**](CustomerModel.md)| CustomerModel. | [optional] |

### Return type

[**CustomerModel**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted customer. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsLinkKeywordToContact"></a>
# **keywordsLinkKeywordToContact**
> ContactKeywordModel keywordsLinkKeywordToContact(contactGuid, guid)

Link existing keyword to contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String contactGuid = "contactGuid_example"; // String | 
    String guid = "guid_example"; // String | 
    try {
      ContactKeywordModel result = apiInstance.keywordsLinkKeywordToContact(contactGuid, guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#keywordsLinkKeywordToContact");
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

[**ContactKeywordModel**](ContactKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created contact keyword link. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesPatchCustomerSalesNote"></a>
# **salesNotesPatchCustomerSalesNote**
> List&lt;CustomerSalesNoteOutputModel&gt; salesNotesPatchCustomerSalesNote(guid, patchOperation)

Update (Patch) a customer sales note or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the customer sales note.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of customer sales note model.
    try {
      List<CustomerSalesNoteOutputModel> result = apiInstance.salesNotesPatchCustomerSalesNote(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#salesNotesPatchCustomerSalesNote");
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
| **guid** | **String**| ID of the customer sales note. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of customer sales note model. | [optional] |

### Return type

[**List&lt;CustomerSalesNoteOutputModel&gt;**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated sales notes. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesPostCustomerSalesNotes"></a>
# **salesNotesPostCustomerSalesNotes**
> CustomerSalesNoteOutputModel salesNotesPostCustomerSalesNotes(customerSalesNoteInputModel)

Insert a customer sales note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersWriteApi;

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

    CustomersWriteApi apiInstance = new CustomersWriteApi(defaultClient);
    CustomerSalesNoteInputModel customerSalesNoteInputModel = new CustomerSalesNoteInputModel(); // CustomerSalesNoteInputModel | SalesNoteOutputModel
    try {
      CustomerSalesNoteOutputModel result = apiInstance.salesNotesPostCustomerSalesNotes(customerSalesNoteInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersWriteApi#salesNotesPostCustomerSalesNotes");
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
| **customerSalesNoteInputModel** | [**CustomerSalesNoteInputModel**](CustomerSalesNoteInputModel.md)| SalesNoteOutputModel | [optional] |

### Return type

[**CustomerSalesNoteOutputModel**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created customer sales note. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

