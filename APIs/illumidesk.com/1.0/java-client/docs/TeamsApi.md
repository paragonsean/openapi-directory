# TeamsApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamsBillingInvoiceItemsList**](TeamsApi.md#teamsBillingInvoiceItemsList) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/ | Get team invoice items for a given invoice. |
| [**teamsBillingInvoiceItemsRead**](TeamsApi.md#teamsBillingInvoiceItemsRead) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/{id} | Get a specific team InvoiceItem. |
| [**teamsBillingInvoicesList**](TeamsApi.md#teamsBillingInvoicesList) | **GET** /v1/teams/{team}/billing/invoices/ | Get team invoices |
| [**teamsBillingInvoicesRead**](TeamsApi.md#teamsBillingInvoicesRead) | **GET** /v1/teams/{team}/billing/invoices/{id}/ | Get an invoice |
| [**teamsBillingSubscriptionsCreate**](TeamsApi.md#teamsBillingSubscriptionsCreate) | **POST** /v1/teams/{team}/billing/subscriptions/ | Create a new team subscription |
| [**teamsBillingSubscriptionsDelete**](TeamsApi.md#teamsBillingSubscriptionsDelete) | **DELETE** /v1/teams/{team}/billing/subscriptions/{id}/ | Delete a subscription |
| [**teamsBillingSubscriptionsList**](TeamsApi.md#teamsBillingSubscriptionsList) | **GET** /v1/teams/{team}/billing/subscriptions/ | Get active team subscriptons |
| [**teamsBillingSubscriptionsRead**](TeamsApi.md#teamsBillingSubscriptionsRead) | **GET** /v1/teams/{team}/billing/subscriptions/{id}/ | Get team subscriptions |
| [**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /v1/teams/ | Create a new team |
| [**teamsDelete**](TeamsApi.md#teamsDelete) | **DELETE** /v1/teams/{team}/ | Delete a team |
| [**teamsGroupsAddToGroup**](TeamsApi.md#teamsGroupsAddToGroup) | **POST** /v1/teams/{team}/groups/{group}/add/ | Add user to group |
| [**teamsGroupsDelete**](TeamsApi.md#teamsGroupsDelete) | **DELETE** /v1/teams/{team}/groups/{group}/ | Delete team group |
| [**teamsGroupsList**](TeamsApi.md#teamsGroupsList) | **GET** /v1/teams/{team}/groups/ | Get team groups |
| [**teamsGroupsRead**](TeamsApi.md#teamsGroupsRead) | **GET** /v1/teams/{team}/groups/{group}/ | Get team group |
| [**teamsGroupsRemoveFromGroup**](TeamsApi.md#teamsGroupsRemoveFromGroup) | **POST** /v1/teams/{team}/groups/{group}/remove/ | User removed from group |
| [**teamsGroupsReplace**](TeamsApi.md#teamsGroupsReplace) | **PUT** /v1/teams/{team}/groups/{group}/ | Patch team group |
| [**teamsGroupsUpdate**](TeamsApi.md#teamsGroupsUpdate) | **PATCH** /v1/teams/{team}/groups/{group}/ | Patch team group |
| [**teamsList**](TeamsApi.md#teamsList) | **GET** /v1/teams/ | Get teams |
| [**teamsRead**](TeamsApi.md#teamsRead) | **GET** /v1/teams/{team}/ | Get a team |
| [**teamsReplace**](TeamsApi.md#teamsReplace) | **PUT** /v1/teams/{team}/ | Replace a team |
| [**teamsUpdate**](TeamsApi.md#teamsUpdate) | **PATCH** /v1/teams/{team}/ | Update a team |


<a id="teamsBillingInvoiceItemsList"></a>
# **teamsBillingInvoiceItemsList**
> List&lt;InvoiceItem&gt; teamsBillingInvoiceItemsList(team, invoiceId, limit, offset, ordering)

Get team invoice items for a given invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<InvoiceItem> result = apiInstance.teamsBillingInvoiceItemsList(team, invoiceId, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingInvoiceItemsList");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **invoiceId** | **String**| Invoice id, expressed as UUID. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;InvoiceItem&gt;**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team invoiceItem list. |  -  |

<a id="teamsBillingInvoiceItemsRead"></a>
# **teamsBillingInvoiceItemsRead**
> InvoiceItem teamsBillingInvoiceItemsRead(team, invoiceId, id)

Get a specific team InvoiceItem.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
    String id = "id_example"; // String | InvoiceItem id, expressed as UUID.
    try {
      InvoiceItem result = apiInstance.teamsBillingInvoiceItemsRead(team, invoiceId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingInvoiceItemsRead");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **invoiceId** | **String**| Invoice id, expressed as UUID. | |
| **id** | **String**| InvoiceItem id, expressed as UUID. | |

### Return type

[**InvoiceItem**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team invoiceItem retrieved. |  -  |
| **404** | InvoiceItem not found. |  -  |

<a id="teamsBillingInvoicesList"></a>
# **teamsBillingInvoicesList**
> List&lt;Invoice&gt; teamsBillingInvoicesList(team, limit, offset)

Get team invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    try {
      List<Invoice> result = apiInstance.teamsBillingInvoicesList(team, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingInvoicesList");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |

### Return type

[**List&lt;Invoice&gt;**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice list. |  -  |

<a id="teamsBillingInvoicesRead"></a>
# **teamsBillingInvoicesRead**
> Invoice teamsBillingInvoicesRead(team, id)

Get an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String id = "id_example"; // String | Invoice unique identifier expressed as UUID.
    try {
      Invoice result = apiInstance.teamsBillingInvoicesRead(team, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingInvoicesRead");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **id** | **String**| Invoice unique identifier expressed as UUID. | |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team invoice retrieved. |  -  |
| **404** | Team invoice not found. |  -  |

<a id="teamsBillingSubscriptionsCreate"></a>
# **teamsBillingSubscriptionsCreate**
> Subscription teamsBillingSubscriptionsCreate(team, subscriptionData)

Create a new team subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    SubscriptionData subscriptionData = new SubscriptionData(); // SubscriptionData | 
    try {
      Subscription result = apiInstance.teamsBillingSubscriptionsCreate(team, subscriptionData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingSubscriptionsCreate");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **subscriptionData** | [**SubscriptionData**](SubscriptionData.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Team subscription created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="teamsBillingSubscriptionsDelete"></a>
# **teamsBillingSubscriptionsDelete**
> teamsBillingSubscriptionsDelete(team, id)

Delete a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String id = "id_example"; // String | Subscription unique identifier expressed as UUID.
    try {
      apiInstance.teamsBillingSubscriptionsDelete(team, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingSubscriptionsDelete");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **id** | **String**| Subscription unique identifier expressed as UUID. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Subscription deleted. |  -  |
| **404** | Subscription not found. |  -  |

<a id="teamsBillingSubscriptionsList"></a>
# **teamsBillingSubscriptionsList**
> List&lt;Subscription&gt; teamsBillingSubscriptionsList(team, limit, offset, ordering)

Get active team subscriptons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<Subscription> result = apiInstance.teamsBillingSubscriptionsList(team, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingSubscriptionsList");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Teams subscription list. |  -  |

<a id="teamsBillingSubscriptionsRead"></a>
# **teamsBillingSubscriptionsRead**
> Subscription teamsBillingSubscriptionsRead(team, id)

Get team subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String id = "id_example"; // String | Unique identifier expressed as UUID.
    try {
      Subscription result = apiInstance.teamsBillingSubscriptionsRead(team, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsBillingSubscriptionsRead");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **id** | **String**| Unique identifier expressed as UUID. | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team subscription retrieved. |  -  |
| **404** | Subscription not found. |  -  |

<a id="teamsCreate"></a>
# **teamsCreate**
> Team teamsCreate(teamData)

Create a new team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamData teamData = new TeamData(); // TeamData | 
    try {
      Team result = apiInstance.teamsCreate(teamData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCreate");
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
| **teamData** | [**TeamData**](TeamData.md)|  | [optional] |

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Team created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="teamsDelete"></a>
# **teamsDelete**
> teamsDelete(team)

Delete a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    try {
      apiInstance.teamsDelete(team);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsDelete");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Team deleted. |  -  |
| **404** | Team not found. |  -  |

<a id="teamsGroupsAddToGroup"></a>
# **teamsGroupsAddToGroup**
> GroupUser teamsGroupsAddToGroup(team, group)

Add user to group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String group = "group_example"; // String | Group unique identifier expressed as UUID or name.
    try {
      GroupUser result = apiInstance.teamsGroupsAddToGroup(team, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsAddToGroup");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **group** | **String**| Group unique identifier expressed as UUID or name. | |

### Return type

[**GroupUser**](GroupUser.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User added to group. |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Group not found |  -  |

<a id="teamsGroupsDelete"></a>
# **teamsGroupsDelete**
> teamsGroupsDelete(team, group)

Delete team group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String group = "group_example"; // String | Group unique identifier expressed as UUID or name.
    try {
      apiInstance.teamsGroupsDelete(team, group);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsDelete");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **group** | **String**| Group unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Group deleted |  -  |
| **404** | Group not found. |  -  |

<a id="teamsGroupsList"></a>
# **teamsGroupsList**
> List&lt;Group&gt; teamsGroupsList(team, limit, offset)

Get team groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String limit = "limit_example"; // String | Limit when getting data.
    String offset = "offset_example"; // String | Offset when getting data.
    try {
      List<Group> result = apiInstance.teamsGroupsList(team, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsList");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **limit** | **String**| Limit when getting data. | [optional] |
| **offset** | **String**| Offset when getting data. | [optional] |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team groups list |  -  |

<a id="teamsGroupsRead"></a>
# **teamsGroupsRead**
> Group teamsGroupsRead(team, group)

Get team group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String group = "group_example"; // String | Group unique identifier expressed as UUID or name.
    try {
      Group result = apiInstance.teamsGroupsRead(team, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsRead");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **group** | **String**| Group unique identifier expressed as UUID or name. | |

### Return type

[**Group**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group retrieved. |  -  |

<a id="teamsGroupsRemoveFromGroup"></a>
# **teamsGroupsRemoveFromGroup**
> teamsGroupsRemoveFromGroup(team, group)

User removed from group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String group = "group_example"; // String | Group unique identifier expressed as UUID or name.
    try {
      apiInstance.teamsGroupsRemoveFromGroup(team, group);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsRemoveFromGroup");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **group** | **String**| Group unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User removed from group. |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Group not found |  -  |

<a id="teamsGroupsReplace"></a>
# **teamsGroupsReplace**
> Group teamsGroupsReplace(team, group, groupData)

Patch team group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String group = "group_example"; // String | Group unique identifier expressed as UUID or name.
    GroupData groupData = new GroupData(); // GroupData | 
    try {
      Group result = apiInstance.teamsGroupsReplace(team, group, groupData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsReplace");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **group** | **String**| Group unique identifier expressed as UUID or name. | |
| **groupData** | [**GroupData**](GroupData.md)|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group replaced |  -  |
| **400** | Invalid data supplied |  -  |

<a id="teamsGroupsUpdate"></a>
# **teamsGroupsUpdate**
> Group teamsGroupsUpdate(team, group, groupData)

Patch team group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String group = "group_example"; // String | Group unique identifier expressed as UUID or name.
    GroupData groupData = new GroupData(); // GroupData | 
    try {
      Group result = apiInstance.teamsGroupsUpdate(team, group, groupData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGroupsUpdate");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **group** | **String**| Group unique identifier expressed as UUID or name. | |
| **groupData** | [**GroupData**](GroupData.md)|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Group not found. |  -  |

<a id="teamsList"></a>
# **teamsList**
> List&lt;Team&gt; teamsList(limit, offset)

Get teams

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String limit = "limit_example"; // String | Limit when getting data.
    String offset = "offset_example"; // String | Offset when getting data.
    try {
      List<Team> result = apiInstance.teamsList(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsList");
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
| **limit** | **String**| Limit when getting data. | [optional] |
| **offset** | **String**| Offset when getting data. | [optional] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team list |  -  |

<a id="teamsRead"></a>
# **teamsRead**
> Team teamsRead(team)

Get a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    try {
      Team result = apiInstance.teamsRead(team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsRead");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team retrieved successfully. |  -  |
| **404** | Team not found. |  -  |

<a id="teamsReplace"></a>
# **teamsReplace**
> Team teamsReplace(team, teamData)

Replace a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    TeamData teamData = new TeamData(); // TeamData | 
    try {
      Team result = apiInstance.teamsReplace(team, teamData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsReplace");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **teamData** | [**TeamData**](TeamData.md)|  | [optional] |

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team updated |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="teamsUpdate"></a>
# **teamsUpdate**
> Team teamsUpdate(team, teamData)

Update a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    TeamData teamData = new TeamData(); // TeamData | 
    try {
      Team result = apiInstance.teamsUpdate(team, teamData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdate");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **teamData** | [**TeamData**](TeamData.md)|  | [optional] |

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Team not found |  -  |

