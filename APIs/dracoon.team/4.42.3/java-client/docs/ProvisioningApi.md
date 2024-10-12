# ProvisioningApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomer**](ProvisioningApi.md#createCustomer) | **POST** /v4/provisioning/customers | Create customer |
| [**createTenantWebhook**](ProvisioningApi.md#createTenantWebhook) | **POST** /v4/provisioning/webhooks | Create tenant webhook |
| [**removeCustomer**](ProvisioningApi.md#removeCustomer) | **DELETE** /v4/provisioning/customers/{customer_id} | Remove customer |
| [**removeCustomerAttribute**](ProvisioningApi.md#removeCustomerAttribute) | **DELETE** /v4/provisioning/customers/{customer_id}/customerAttributes/{key} | Remove customer attribute |
| [**removeTenantWebhook**](ProvisioningApi.md#removeTenantWebhook) | **DELETE** /v4/provisioning/webhooks/{webhook_id} | Remove tenant webhook |
| [**requestCustomer**](ProvisioningApi.md#requestCustomer) | **GET** /v4/provisioning/customers/{customer_id} | Get customer |
| [**requestCustomerAttributes**](ProvisioningApi.md#requestCustomerAttributes) | **GET** /v4/provisioning/customers/{customer_id}/customerAttributes | Request customer attributes |
| [**requestCustomerUsers**](ProvisioningApi.md#requestCustomerUsers) | **GET** /v4/provisioning/customers/{customer_id}/users | Request list of customer users |
| [**requestCustomers**](ProvisioningApi.md#requestCustomers) | **GET** /v4/provisioning/customers | Request list of customers |
| [**requestListOfEventTypesForTenant**](ProvisioningApi.md#requestListOfEventTypesForTenant) | **GET** /v4/provisioning/webhooks/event_types | Request list of event types |
| [**requestListOfTenantWebhooks**](ProvisioningApi.md#requestListOfTenantWebhooks) | **GET** /v4/provisioning/webhooks | Request list of tenant webhooks |
| [**requestTenantWebhook**](ProvisioningApi.md#requestTenantWebhook) | **GET** /v4/provisioning/webhooks/{webhook_id} | Request tenant webhook |
| [**resetTenantWebhookLifetime**](ProvisioningApi.md#resetTenantWebhookLifetime) | **POST** /v4/provisioning/webhooks/{webhook_id}/reset_lifetime | Reset tenant webhook lifetime |
| [**setCustomerAttributes**](ProvisioningApi.md#setCustomerAttributes) | **POST** /v4/provisioning/customers/{customer_id}/customerAttributes | Set customer attributes |
| [**updateCustomer**](ProvisioningApi.md#updateCustomer) | **PUT** /v4/provisioning/customers/{customer_id} | Update customer |
| [**updateCustomerAttributes**](ProvisioningApi.md#updateCustomerAttributes) | **PUT** /v4/provisioning/customers/{customer_id}/customerAttributes | Add or edit customer attributes |
| [**updateTenantWebhook**](ProvisioningApi.md#updateTenantWebhook) | **PUT** /v4/provisioning/webhooks/{webhook_id} | Update tenant webhook |


<a id="createCustomer"></a>
# **createCustomer**
> NewCustomerResponse createCustomer(newCustomerRequest, xSdsDateFormat, xSdsServiceToken)

Create customer

### Description: Create a new customer.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.    ### Postcondition: A new customer is created.  ### Further Information: If no company name is set, first letter of the first name separated by dot followed by last name of the first administrator is used (e.g. &#x60;J.Doe&#x60;).   Max quota has to be at least &#x60;1 MB&#x60; (&#x3D; &#x60;1.048.576 B&#x60;).  If &#x60;basic&#x60; authentication is enabled, the first administrator will get &#x60;basic&#x60; authentication by default.   To create a first administrator without &#x60;basic&#x60; authentication it **MUST** be disabled explicitly.    Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  ### Authentication Method Options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Option Key | Option Value | | :--- | :--- | :--- | | &#x60;basic&#x60; / &#x60;sql&#x60; | &#x60;username&#x60; | Unique user identifier | | &#x60;active_directory&#x60; | &#x60;ad_config_id&#x60; (optional) | Active Directory configuration ID | |  | &#x60;username&#x60; | Active Directory username according to authentication setting &#x60;userFilter&#x60; | | &#x60;radius&#x60; | &#x60;username&#x60; | RADIUS username | | &#x60;openid&#x60; | &#x60;openid_config_id&#x60; (optional) | OpenID Connect configuration ID | |  | &#x60;username&#x60; | OpenID Connect username according to authentication setting &#x60;mappingClaim&#x60; |  &lt;/details&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    NewCustomerRequest newCustomerRequest = new NewCustomerRequest(); // NewCustomerRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      NewCustomerResponse result = apiInstance.createCustomer(newCustomerRequest, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#createCustomer");
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
| **newCustomerRequest** | [**NewCustomerRequest**](NewCustomerRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**NewCustomerResponse**](NewCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |

<a id="createTenantWebhook"></a>
# **createTenantWebhook**
> Webhook createTenantWebhook(createWebhookRequest, xSdsDateFormat, xSdsServiceToken)

Create tenant webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Create a new webhook for the tenant scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: Webhook is created for given event types.  ### Further Information: URL must begin with the &#x60;HTTPS&#x60; scheme. Webhook names are limited to 150 characters.  ### Available event types: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;customer.created&#x60;** | Triggered when a new customer is created | Tenant Webhook | | **&#x60;customer.deleted&#x60;** | Triggered when a user is deleted | Tenant Webhook | | **&#x60;webhook.expiring&#x60;** | Triggered 30/20/10/1 days before a webhook expires |  Tenant Webhook |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    CreateWebhookRequest createWebhookRequest = new CreateWebhookRequest(); // CreateWebhookRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Webhook result = apiInstance.createTenantWebhook(createWebhookRequest, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#createTenantWebhook");
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
| **createWebhookRequest** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="removeCustomer"></a>
# **removeCustomer**
> removeCustomer(customerId, xSdsServiceToken)

Remove customer

### Description: Delete a customer.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.  ### Postcondition: Customer is deleted.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      apiInstance.removeCustomer(customerId, xSdsServiceToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#removeCustomer");
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
| **customerId** | **Long**| Customer ID | |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="removeCustomerAttribute"></a>
# **removeCustomerAttribute**
> removeCustomerAttribute(customerId, key, xSdsServiceToken)

Remove customer attribute

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.4.0&lt;/h3&gt;  ### Description: Delete a custom customer attribute.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; required.  ### Postcondition: Custom customer attribute gets deleted.  ### Further Information: * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    String key = "key_example"; // String | Key
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      apiInstance.removeCustomerAttribute(customerId, key, xSdsServiceToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#removeCustomerAttribute");
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
| **customerId** | **Long**| Customer ID | |
| **key** | **String**| Key | |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="removeTenantWebhook"></a>
# **removeTenantWebhook**
> removeTenantWebhook(webhookId, xSdsServiceToken)

Remove tenant webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Delete a webhook for the tenant scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: Webhook is deleted.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long webhookId = 56L; // Long | Webhook ID
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      apiInstance.removeTenantWebhook(webhookId, xSdsServiceToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#removeTenantWebhook");
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
| **webhookId** | **Long**| Webhook ID | |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestCustomer"></a>
# **requestCustomer**
> Customer requestCustomer(customerId, xSdsDateFormat, includeAttributes, xSdsServiceToken)

Get customer

### Description:   Receive details of a selected customer.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.  ### Postcondition: Customer details are returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    Boolean includeAttributes = true; // Boolean | Include custom customer attributes.
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Customer result = apiInstance.requestCustomer(customerId, xSdsDateFormat, includeAttributes, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestCustomer");
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
| **customerId** | **Long**| Customer ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **includeAttributes** | **Boolean**| Include custom customer attributes. | [optional] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestCustomerAttributes"></a>
# **requestCustomerAttributes**
> AttributesResponse requestCustomerAttributes(customerId, offset, limit, filter, sort, xSdsServiceToken)

Request customer attributes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.4.0&lt;/h3&gt;  ### Description:   Retrieve a list of customer attributes.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.   Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read all customers&lt;/span&gt; required.  ### Postcondition: List of attributes is returned.  ### Further Information:  ### Filtering: Filters are case insensitive.   All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:cn:searchString_1|value:cn:searchString_2&#x60;   Filter by attribute key contains &#x60;searchString_1&#x60; **AND** attribute value contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;key&#x60; | Customer attribute key filter | &#x60;cn, eq, sw&#x60; | Attribute key contains / equals / starts with value. | &#x60;search String&#x60; | | &#x60;value&#x60; | Customer attribute value filter | &#x60;cn, eq, sw&#x60; | Attribute value contains / equals / starts with value. | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:asc|value:desc&#x60;   Sort by &#x60;key&#x60; ascending **AND** by &#x60;value&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;key&#x60; | Customer attribute key | | &#x60;value&#x60; | Customer attribute value |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      AttributesResponse result = apiInstance.requestCustomerAttributes(customerId, offset, limit, filter, sort, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestCustomerAttributes");
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
| **customerId** | **Long**| Customer ID | |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**AttributesResponse**](AttributesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestCustomerUsers"></a>
# **requestCustomerUsers**
> UserList requestCustomerUsers(customerId, xSdsDateFormat, offset, limit, filter, sort, includeAttributes, includeRoles, includeManageableRooms, xSdsServiceToken)

Request list of customer users

### Description:   Receive a list of users associated with a certain customer.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.  ### Postcondition: List of customer users is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Except for &#x60;login&#x60;, &#x60;firstName&#x60; and  &#x60;lastName&#x60; - these are connected via logical disjunction (**OR**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;login:cn:searchString_1|firstName:cn:searchString_2|lockStatus:eq:2&#x60;   Filter users by login contains &#x60;searchString_1&#x60; **OR** firstName contains &#x60;searchString_2&#x60; **AND** those who are **NOT** locked.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;email&#x60; | Email filter | &#x60;eq&#x60;, &#x60;cn&#x60; | Email contains value. | &#x60;search String&#x60; | | &#x60;userName&#x60; | User name filter | &#x60;eq&#x60;, &#x60;cn&#x60; | UserName contains value. | &#x60;search String&#x60; | | &#x60;firstName&#x60; | User first name filter | &#x60;cn&#x60; | User first name contains value. | &#x60;search String&#x60; | | &#x60;lastName&#x60; | User last name filter | &#x60;cn&#x60; | User last name contains value. | &#x60;search String&#x60; | | &#x60;isLocked&#x60; | User lock status filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;effectiveRoles&#x60; | Filter users with DIRECT or DIRECT **AND** EFFECTIVE roles&lt;ul&gt;&lt;li&gt;&#x60;false&#x60;: DIRECT roles&lt;/li&gt;&lt;li&gt;&#x60;true&#x60;: DIRECT **AND** EFFECTIVE roles&lt;/li&gt;&lt;/ul&gt;DIRECT means: e.g. user gets role **directly** granted from someone with _grant permission_ right.&lt;br&gt;EFFECTIVE means: e.g. user gets role through **group membership**. | &#x60;eq&#x60; |  | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60; | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;phone&#x60; | Phone filter | &#x60;eq&#x60; | Phone equals value. | &#x60;search String&#x60; | | &#x60;isEncryptionEnabled&#x60; | Encryption status filter&lt;ul&gt;&lt;li&gt;client-side encryption&lt;/li&gt;&lt;li&gt;private key possession&lt;/li&gt;&lt;/ul&gt; | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;hasRole&#x60; | (**&#x60;NEW&#x60;**) User role filter&lt;br&gt;Depends on **effectiveRoles**.&lt;br&gt;For more information about roles check **&#x60;GET /roles&#x60;** API | &#x60;eq&#x60;, &#x60;neq&#x60; | User role equals value. | &lt;ul&gt;&lt;li&gt;&#x60;CONFIG_MANAGER&#x60; - Manages global configuration&lt;/li&gt;&lt;li&gt;&#x60;USER_MANAGER&#x60; - Manages users&lt;/li&gt;&lt;li&gt;&#x60;GROUP_MANAGER&#x60; - Manages user groups&lt;/li&gt;&lt;li&gt;&#x60;ROOM_MANAGER&#x60; - Manages top level rooms&lt;/li&gt;&lt;li&gt;&#x60;LOG_AUDITOR&#x60; - Reads audit logs&lt;/li&gt;&lt;li&gt;&#x60;NONMEMBER_VIEWER&#x60; - Views users and groups when having room _\&quot;manage\&quot;_ permission&lt;/li&gt;&lt;li&gt;&#x60;USER&#x60; - Regular User role&lt;/li&gt;&lt;li&gt;&#x60;GUEST_USER&#x60; - Guest User role&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;lockStatus&#x60;&lt;/del&gt; | User lock status filter | &#x60;eq&#x60; | User lock status equals value. | &lt;ul&gt;&lt;li&gt;&#x60;0&#x60; - Locked&lt;/li&gt;&lt;li&gt;&#x60;1&#x60; - Web access allowed&lt;/li&gt;&lt;li&gt;&#x60;2&#x60; - Web and mobile access allowed&lt;/li&gt;&lt;/ul&gt; | | &lt;del&gt;&#x60;login&#x60;&lt;/del&gt; |  User login filter | &#x60;cn&#x60; | User login contains value. | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;firstName:asc|lastLoginSuccessAt:desc&#x60;   Sort by &#x60;firstName&#x60; ascending **AND** by &#x60;lastLoginSuccessAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;userName&#x60; | User name | | &#x60;email&#x60; | User email | | &#x60;firstName&#x60; | User first name | | &#x60;lastName&#x60; | User last name | | &#x60;isLocked&#x60; | User lock status | | &#x60;lastLoginSuccessAt&#x60; | Last successful login date | | &#x60;expireAt&#x60; | Expiration date | | &#x60;createdAt&#x60; | Creation date |  &lt;/details&gt;  ### Deprecated sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &lt;del&gt;&#x60;gender&#x60;&lt;/del&gt; | Gender | | &lt;del&gt;&#x60;lockStatus&#x60;&lt;/del&gt; | User lock status | | &lt;del&gt;&#x60;login&#x60;&lt;/del&gt; | User login |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    Boolean includeAttributes = true; // Boolean | Include custom user attributes.
    Boolean includeRoles = true; // Boolean | Include roles
    Boolean includeManageableRooms = true; // Boolean | Include hasManageableRooms (deprecated)
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      UserList result = apiInstance.requestCustomerUsers(customerId, xSdsDateFormat, offset, limit, filter, sort, includeAttributes, includeRoles, includeManageableRooms, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestCustomerUsers");
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
| **customerId** | **Long**| Customer ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **includeAttributes** | **Boolean**| Include custom user attributes. | [optional] |
| **includeRoles** | **Boolean**| Include roles | [optional] |
| **includeManageableRooms** | **Boolean**| Include hasManageableRooms (deprecated) | [optional] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**UserList**](UserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestCustomers"></a>
# **requestCustomers**
> CustomerList requestCustomers(xSdsDateFormat, offset, limit, filter, sort, includeAttributes, xSdsServiceToken)

Request list of customers

### Description:   Receive a list of customers.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.  ### Postcondition: List of customers is returned.  ### Further Information: This list returns a maximum of **1000** entries.    ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;trialDaysLeft:le:10|userMax:le:100&#x60;   Get all customers with &#x60;10&#x60; trial days left **AND** user maximum **&lt;&#x3D;** &#x60;100&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;id&#x60; | Customer ID filter | &#x60;eq&#x60; | Customer ID equals value. | &#x60;positive Integer&#x60; | | &#x60;companyName&#x60; | Company name filter | &#x60;cn&#x60; | Company name contains value. | &#x60;search String&#x60; | | &#x60;customerContractType&#x60; | Customer contract type filter | &#x60;eq&#x60; | Customer contract type equals value. | &lt;ul&gt;&lt;li&gt;&#x60;demo&#x60;&lt;/li&gt;&lt;li&gt;&#x60;free&#x60;&lt;/li&gt;&lt;li&gt;&#x60;pay&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;trialDaysLeft&#x60; | Left trial days filter | &#x60;ge, le&#x60; | Left trial days are greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;trialDaysLeft:ge:5&#x60;&amp;#124;&#x60;trialDaysLeft:le:10&#x60; | | &#x60;providerCustomerId&#x60; | Provider Customer ID filter | &#x60;cn, eq&#x60; | Provider Customer ID contains / equals value. | &#x60;search String&#x60; | | &#x60;quotaMax&#x60; | Maximum quota filter | &#x60;ge, le&#x60; | Maximum quota is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;quotaMax:ge:1024&#x60;&amp;#124;&#x60;quotaMax:le:1073741824&#x60; | &#x60;positive Integer&#x60; | | &#x60;quotaUsed&#x60; | Used quota filter | &#x60;ge, le&#x60; | Used quota is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;quotaUsed:ge:1024&#x60;&amp;#124;&#x60;quotaUsed:le:1073741824&#x60; | &#x60;positive Integer&#x60; | | &#x60;userMax&#x60; | User maximum filter | &#x60;ge, le&#x60; | User maxiumum is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;userMax:ge:10&#x60;&amp;#124;&#x60;userMax:le:100&#x60; | &#x60;positive Integer&#x60; | | &#x60;userUsed&#x60; | Number of registered users filter | &#x60;ge, le&#x60; | Number of registered users is is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;userUsed:ge:10&#x60;&amp;#124;&#x60;userUsed:le:100&#x60; | &#x60;positive Integer&#x60; | | &#x60;isLocked&#x60; | Lock status filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;updatedAt&#x60; | Last modification date filter | &#x60;ge, le&#x60; | Last modification date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;updatedAt:ge:2016-12-31&#x60;&amp;#124;&#x60;updatedAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;lastLoginAt&#x60; | Last login date filter | &#x60;ge, le&#x60; | Last login date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;lastLoginAt:ge:2016-12-31&#x60;&amp;#124;&#x60;lastLoginAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;userLogin&#x60; | User login filter | &#x60;eq&#x60; | User login name equals value.&lt;br&gt;Search user all logins e.g. &#x60;basic&#x60;, &#x60;active_directory&#x60;, &#x60;radius&#x60;. | &#x60;search String&#x60; | | &#x60;attributeKey&#x60; | Customer attribute key filter | &#x60;eq&#x60;, &#x60;nex&#x60; | Customer attribute key equals value / Customer attribute does **NOT** exist at customer | &#x60;search String&#x60; | | &#x60;attributeValue&#x60; | Customer attribute value filter | &#x60;eq&#x60; | Customer attribute value equals value. | &#x60;search String&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;activationCode&#x60;&lt;/del&gt; | Activation code filter | &#x60;cn, eq&#x60; | Activation code contains / equals value. | &#x60;search String&#x60; | | &lt;del&gt;&#x60;lockStatus&#x60;&lt;/del&gt; | Lock status filter | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;0&#x60; - unlocked&lt;/li&gt;&lt;li&gt;&#x60;1&#x60; - locked&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;companyName:desc|userUsed:asc&#x60;   Sort by &#x60;companyName&#x60; descending **AND** &#x60;userUsed&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;companyName&#x60; | Company name | | &#x60;customerContractType&#x60; | Customer contract type | | &#x60;trialDaysLeft&#x60; | Number of remaining trial days (demo customers) | | &#x60;providerCustomerId&#x60; | Provider Customer ID | | &#x60;quotaMax&#x60; | Maximum quota | | &#x60;quotaUsed&#x60; | Currently used quota | | &#x60;userMax&#x60; | Maximum user number | | &#x60;userUsed&#x60; | Number of registered users | | &#x60;isLocked&#x60; | Lock status of customer | | &#x60;createdAt&#x60; | Creation date | | &#x60;updatedAt&#x60; | Last modification date | | &#x60;lastLoginAt&#x60; | Last login date of any user of this customer |  &lt;/details&gt;  ### Deprecated sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &lt;del&gt;&#x60;lockStatus&#x60;&lt;/del&gt; | Lock status of customer |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    Boolean includeAttributes = true; // Boolean | Include custom customer attributes.
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      CustomerList result = apiInstance.requestCustomers(xSdsDateFormat, offset, limit, filter, sort, includeAttributes, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestCustomers");
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
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **includeAttributes** | **Boolean**| Include custom customer attributes. | [optional] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**CustomerList**](CustomerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestListOfEventTypesForTenant"></a>
# **requestListOfEventTypesForTenant**
> EventTypeList requestListOfEventTypesForTenant(xSdsServiceToken)

Request list of event types

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of available event types.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: List of available event types is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      EventTypeList result = apiInstance.requestListOfEventTypesForTenant(xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestListOfEventTypesForTenant");
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
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**EventTypeList**](EventTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestListOfTenantWebhooks"></a>
# **requestListOfTenantWebhooks**
> WebhookList requestListOfTenantWebhooks(xSdsDateFormat, offset, limit, filter, sort, xSdsServiceToken)

Request list of tenant webhooks

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of webhooks for the tenant scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: List of webhooks is returned.  ### Further Information:   Output is limited to **500** entries.   For more results please use filter criteria and paging (&#x60;offset&#x60; + &#x60;limit&#x60;).   &#x60;EncryptionInfo&#x60; is **NOT** provided.   Wildcard character is the asterisk character: **&#x60;*&#x60;**  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:goo|createdAt:ge:2015-01-01&#x60;   Get webhooks where name contains &#x60;goo&#x60; **AND** webhook creation date is **&gt;&#x3D;** &#x60;2015-01-01&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;id&#x60;** | Webhook id filter | &#x60;eq&#x60; | Webhook id equals value.&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**). |&#x60;positive number&#x60;| | **&#x60;name&#x60;** | Webhook type name| &#x60;cn, eq&#x60; | Webhook name contains / equals value. | &#x60;search String&#x60; | | **&#x60;isEnabled&#x60;** | Webhook isEnabled filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | **&#x60;createdAt&#x60;** | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;updatedAt&#x60;** | Last modification date filter | &#x60;ge, le&#x60; | Last modification date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;updatedAt:ge:2016-12-31&#x60;&amp;#124;&#x60;updatedAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;expiration&#x60;** | Expiration date filter | &#x60;ge, le, eq&#x60; | Expiration date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;expiration:ge:2016-12-31&#x60;&amp;#124;&#x60;expiration:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;lastFailStatus&#x60;** | Failure status filter | &#x60;eq&#x60; | Last HTTP status code. Set when a webhook is auto-disabled due to repeated delivery failures |&#x60;positive number&#x60;|  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc|isEnabled:asc&#x60;   Sort by &#x60;name&#x60; descending and &#x60;isEnabled&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;id&#x60;** | Webhook id | | **&#x60;name&#x60;** | Webhook name | | **&#x60;isEnabled&#x60;** | Webhook isEnabled | | **&#x60;createdAt&#x60;** | Creation date | | **&#x60;updatedAt&#x60;** | Last modification date | | **&#x60;expiration&#x60;** | Expiration date |  &lt;/details&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      WebhookList result = apiInstance.requestListOfTenantWebhooks(xSdsDateFormat, offset, limit, filter, sort, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestListOfTenantWebhooks");
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
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestTenantWebhook"></a>
# **requestTenantWebhook**
> Webhook requestTenantWebhook(webhookId, xSdsDateFormat, xSdsServiceToken)

Request tenant webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a specific webhook for the tenant scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: Webhook is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long webhookId = 56L; // Long | Webhook ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Webhook result = apiInstance.requestTenantWebhook(webhookId, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#requestTenantWebhook");
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
| **webhookId** | **Long**| Webhook ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="resetTenantWebhookLifetime"></a>
# **resetTenantWebhookLifetime**
> Webhook resetTenantWebhookLifetime(webhookId, xSdsDateFormat, xSdsServiceToken)

Reset tenant webhook lifetime

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Reset the lifetime of a webhook for the tenant scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: Lifetime of the webhook is reset.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long webhookId = 56L; // Long | Webhook ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Webhook result = apiInstance.resetTenantWebhookLifetime(webhookId, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#resetTenantWebhookLifetime");
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
| **webhookId** | **Long**| Webhook ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="setCustomerAttributes"></a>
# **setCustomerAttributes**
> Customer setCustomerAttributes(customerId, customerAttributes, xSdsDateFormat, xSdsServiceToken)

Set customer attributes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.28.0&lt;/h3&gt;  ### Description:   Set custom customer attributes.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; required.  ### Postcondition: Custom customer attributes gets set.  ### Further Information: Batch function.   All existing customer attributes will be deleted.    * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    CustomerAttributes customerAttributes = new CustomerAttributes(); // CustomerAttributes | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Customer result = apiInstance.setCustomerAttributes(customerId, customerAttributes, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#setCustomerAttributes");
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
| **customerId** | **Long**| Customer ID | |
| **customerAttributes** | [**CustomerAttributes**](CustomerAttributes.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="updateCustomer"></a>
# **updateCustomer**
> UpdateCustomerResponse updateCustomer(customerId, updateCustomerRequest, xSdsDateFormat, xSdsServiceToken)

Update customer

### Description:   Change selected attributes of a customer.  ### Precondition: Authentication with &#x60;X-Sds-Service-Token&#x60; required.  ### Postcondition: Selected attributes of customer are updated.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    UpdateCustomerRequest updateCustomerRequest = new UpdateCustomerRequest(); // UpdateCustomerRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      UpdateCustomerResponse result = apiInstance.updateCustomer(customerId, updateCustomerRequest, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#updateCustomer");
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
| **customerId** | **Long**| Customer ID | |
| **updateCustomerRequest** | [**UpdateCustomerRequest**](UpdateCustomerRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**UpdateCustomerResponse**](UpdateCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="updateCustomerAttributes"></a>
# **updateCustomerAttributes**
> Customer updateCustomerAttributes(customerId, customerAttributes, xSdsDateFormat, xSdsServiceToken)

Add or edit customer attributes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.4.0&lt;/h3&gt;  ### Description:   Add or edit custom customer attributes. &lt;br/&gt;&lt;br/&gt;&lt;span style&#x3D;\&quot;font-weight: bold; color: red;\&quot;&gt; &amp;#128679; **Warning: Please note that the response with HTTP status code 200 (OK) is deprecated and will be replaced with HTTP status code 204 (No content)!**&lt;/span&gt;&lt;br/&gt;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; required.  ### Postcondition: Custom customer attributes get added or edited.  ### Further Information: Batch function.   If an entry exists before, it will be overwritten.    * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long customerId = 56L; // Long | Customer ID
    CustomerAttributes customerAttributes = new CustomerAttributes(); // CustomerAttributes | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Customer result = apiInstance.updateCustomerAttributes(customerId, customerAttributes, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#updateCustomerAttributes");
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
| **customerId** | **Long**| Customer ID | |
| **customerAttributes** | [**CustomerAttributes**](CustomerAttributes.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK **(DEPRECATED: WILL BE REPLACED BY 204: \&quot;No content\&quot;)** |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="updateTenantWebhook"></a>
# **updateTenantWebhook**
> Webhook updateTenantWebhook(webhookId, updateWebhookRequest, xSdsDateFormat, xSdsServiceToken)

Update tenant webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Update an existing webhook for the tenant scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage webhook&lt;/span&gt; required.  ### Postcondition: Webhook is updated.  ### Further Information: URL must begin with the &#x60;HTTPS&#x60; scheme. Webhook names are limited to 150 characters.  ### Available event types:  &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;customer.created&#x60;** | Triggered when a new customer is created | Tenant Webhook | | **&#x60;customer.deleted&#x60;** | Triggered when a user is deleted | Tenant Webhook | | **&#x60;webhook.expiring&#x60;** | Triggered 30/20/10/1 days before a webhook expires |  Tenant Webhook |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    Long webhookId = 56L; // Long | Webhook ID
    UpdateWebhookRequest updateWebhookRequest = new UpdateWebhookRequest(); // UpdateWebhookRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsServiceToken = "xSdsServiceToken_example"; // String | Service Authentication token
    try {
      Webhook result = apiInstance.updateTenantWebhook(webhookId, updateWebhookRequest, xSdsDateFormat, xSdsServiceToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#updateTenantWebhook");
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
| **webhookId** | **Long**| Webhook ID | |
| **updateWebhookRequest** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsServiceToken** | **String**| Service Authentication token | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

