# IntegrationsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNewIntegration**](IntegrationsApi.md#addNewIntegration) | **POST** /org/{orgId}/integrations | Add new integration |
| [**callList**](IntegrationsApi.md#callList) | **GET** /org/{orgId}/integrations | List |
| [**cloneAnIntegrationWithSettingsAndCredentials**](IntegrationsApi.md#cloneAnIntegrationWithSettingsAndCredentials) | **POST** /org/{orgId}/integrations/{integrationId}/clone | Clone an integration (with settings and credentials) |
| [**deleteCredentials**](IntegrationsApi.md#deleteCredentials) | **DELETE** /org/{orgId}/integrations/{integrationId}/authentication | Delete credentials |
| [**getExistingIntegrationByType**](IntegrationsApi.md#getExistingIntegrationByType) | **GET** /org/{orgId}/integrations/{type} | Get existing integration by type |
| [**provisionNewBrokerToken**](IntegrationsApi.md#provisionNewBrokerToken) | **POST** /org/{orgId}/integrations/{integrationId}/authentication/provision-token | Provision new broker token |
| [**retrieve**](IntegrationsApi.md#retrieve) | **GET** /org/{orgId}/integrations/{integrationId}/settings | Retrieve |
| [**switchBetweenBrokerTokens**](IntegrationsApi.md#switchBetweenBrokerTokens) | **POST** /org/{orgId}/integrations/{integrationId}/authentication/switch-token | Switch between broker tokens |
| [**update**](IntegrationsApi.md#update) | **PUT** /org/{orgId}/integrations/{integrationId}/settings | Update |
| [**updateExistingIntegration**](IntegrationsApi.md#updateExistingIntegration) | **PUT** /org/{orgId}/integrations/{integrationId} | Update existing integration |


<a id="addNewIntegration"></a>
# **addNewIntegration**
> addNewIntegration(orgId, addNewIntegrationRequest)

Add new integration

Add new integration for given organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    AddNewIntegrationRequest addNewIntegrationRequest = new AddNewIntegrationRequest(); // AddNewIntegrationRequest | 
    try {
      apiInstance.addNewIntegration(orgId, addNewIntegrationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#addNewIntegration");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **addNewIntegrationRequest** | [**AddNewIntegrationRequest**](AddNewIntegrationRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="callList"></a>
# **callList**
> Object callList(orgId)

List



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization public ID. The `API_KEY` must have admin access to this organization.
    try {
      Object result = apiInstance.callList(orgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#callList");
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
| **orgId** | **String**| The organization public ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="cloneAnIntegrationWithSettingsAndCredentials"></a>
# **cloneAnIntegrationWithSettingsAndCredentials**
> cloneAnIntegrationWithSettingsAndCredentials(orgId, integrationId, cloneAnIntegrationWithSettingsAndCredentialsRequest)

Clone an integration (with settings and credentials)

Clone an integration, including all of its settings and credentials from one organization to another organization in the same group. This API supports both brokered and non-brokered integrations.  Use this API for when you want to share a Broker token between several Snyk organizations (integrations).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | Source organization public ID to clone integration settings from. The `API_KEY` must have access to this organization.
    String integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | Source integration public ID to clone.
    CloneAnIntegrationWithSettingsAndCredentialsRequest cloneAnIntegrationWithSettingsAndCredentialsRequest = new CloneAnIntegrationWithSettingsAndCredentialsRequest(); // CloneAnIntegrationWithSettingsAndCredentialsRequest | 
    try {
      apiInstance.cloneAnIntegrationWithSettingsAndCredentials(orgId, integrationId, cloneAnIntegrationWithSettingsAndCredentialsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#cloneAnIntegrationWithSettingsAndCredentials");
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
| **orgId** | **String**| Source organization public ID to clone integration settings from. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **integrationId** | **String**| Source integration public ID to clone. | |
| **cloneAnIntegrationWithSettingsAndCredentialsRequest** | [**CloneAnIntegrationWithSettingsAndCredentialsRequest**](CloneAnIntegrationWithSettingsAndCredentialsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteCredentials"></a>
# **deleteCredentials**
> deleteCredentials(orgId, integrationId)

Delete credentials

Removes any credentials set for this integration. If this is a brokered connection the operation will have no effect.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The integration ID.
    try {
      apiInstance.deleteCredentials(orgId, integrationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#deleteCredentials");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **integrationId** | **String**| The integration ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getExistingIntegrationByType"></a>
# **getExistingIntegrationByType**
> GetExistingIntegrationByType200Response getExistingIntegrationByType(orgId, type)

Get existing integration by type



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The `API_KEY` must have admin access to this organization.
    String type = "github"; // String | Integration type.
    try {
      GetExistingIntegrationByType200Response result = apiInstance.getExistingIntegrationByType(orgId, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#getExistingIntegrationByType");
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
| **orgId** | **String**| The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **type** | **String**| Integration type. | |

### Return type

[**GetExistingIntegrationByType200Response**](GetExistingIntegrationByType200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="provisionNewBrokerToken"></a>
# **provisionNewBrokerToken**
> provisionNewBrokerToken(orgId, integrationId)

Provision new broker token

Issue a new and unique provisional broker token for the brokered integration.  Used for zero down-time token rotation with the Snyk Broker. Once provisioned, the token can be used to initialize a new broker client before using the switch API to update the token in use by the integration.  The new provisional token will fail to be created if the integration, or any other integration in the same group, already has one provisioned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The `API_KEY` must have access to this organization.
    String integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | 
    try {
      apiInstance.provisionNewBrokerToken(orgId, integrationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#provisionNewBrokerToken");
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
| **orgId** | **String**| The &#x60;API_KEY&#x60; must have access to this organization. | |
| **integrationId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieve"></a>
# **retrieve**
> Retrieve200Response retrieve(orgId, integrationId)

Retrieve



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    try {
      Retrieve200Response result = apiInstance.retrieve(orgId, integrationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#retrieve");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | |

### Return type

[**Retrieve200Response**](Retrieve200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="switchBetweenBrokerTokens"></a>
# **switchBetweenBrokerTokens**
> switchBetweenBrokerTokens(orgId, integrationId)

Switch between broker tokens

Switch the existing broker token with the provisioned token for this integration and any other in the same group. Only perform this action when you have a Broker client running with the provisioned token. This action will fail if there is no token provisioned for this integration or any integration in the same group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The `API_KEY` must have access to this organization.
    String integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | 
    try {
      apiInstance.switchBetweenBrokerTokens(orgId, integrationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#switchBetweenBrokerTokens");
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
| **orgId** | **String**| The &#x60;API_KEY&#x60; must have access to this organization. | |
| **integrationId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="update"></a>
# **update**
> Retrieve200Response update(orgId, integrationId, updateRequest)

Update



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    UpdateRequest updateRequest = new UpdateRequest(); // UpdateRequest | 
    try {
      Retrieve200Response result = apiInstance.update(orgId, integrationId, updateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#update");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | |
| **updateRequest** | [**UpdateRequest**](UpdateRequest.md)|  | [optional] |

### Return type

[**Retrieve200Response**](Retrieve200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateExistingIntegration"></a>
# **updateExistingIntegration**
> updateExistingIntegration(orgId, integrationId, updateExistingIntegrationRequest)

Update existing integration

+ Update integration&#39;s credentials for given organization. Integration must be **not brokered**  + Enable or disable brokered integration for given organization. *Credentials required for disabling brokered integration*  Examples in right section:  1. Set up a broker for an existing integration  2. Update credentials for an existing non-brokered integration  3. Disable broker for an existing integration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    UpdateExistingIntegrationRequest updateExistingIntegrationRequest = new UpdateExistingIntegrationRequest(); // UpdateExistingIntegrationRequest | 
    try {
      apiInstance.updateExistingIntegration(orgId, integrationId, updateExistingIntegrationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#updateExistingIntegration");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | |
| **updateExistingIntegrationRequest** | [**UpdateExistingIntegrationRequest**](UpdateExistingIntegrationRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

