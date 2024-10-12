# GlobalUsersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalUsersGetEnvironment**](GlobalUsersApi.md#globalUsersGetEnvironment) | **POST** /providers/Microsoft.LabServices/users/{userName}/getEnvironment |  |
| [**globalUsersGetOperationBatchStatus**](GlobalUsersApi.md#globalUsersGetOperationBatchStatus) | **POST** /providers/Microsoft.LabServices/users/{userName}/getOperationBatchStatus |  |
| [**globalUsersGetOperationStatus**](GlobalUsersApi.md#globalUsersGetOperationStatus) | **POST** /providers/Microsoft.LabServices/users/{userName}/getOperationStatus |  |
| [**globalUsersGetPersonalPreferences**](GlobalUsersApi.md#globalUsersGetPersonalPreferences) | **POST** /providers/Microsoft.LabServices/users/{userName}/getPersonalPreferences |  |
| [**globalUsersListEnvironments**](GlobalUsersApi.md#globalUsersListEnvironments) | **POST** /providers/Microsoft.LabServices/users/{userName}/listEnvironments |  |
| [**globalUsersListLabs**](GlobalUsersApi.md#globalUsersListLabs) | **POST** /providers/Microsoft.LabServices/users/{userName}/listLabs |  |
| [**globalUsersRegister**](GlobalUsersApi.md#globalUsersRegister) | **POST** /providers/Microsoft.LabServices/users/{userName}/register |  |
| [**globalUsersResetPassword**](GlobalUsersApi.md#globalUsersResetPassword) | **POST** /providers/Microsoft.LabServices/users/{userName}/resetPassword |  |
| [**globalUsersStartEnvironment**](GlobalUsersApi.md#globalUsersStartEnvironment) | **POST** /providers/Microsoft.LabServices/users/{userName}/startEnvironment |  |
| [**globalUsersStopEnvironment**](GlobalUsersApi.md#globalUsersStopEnvironment) | **POST** /providers/Microsoft.LabServices/users/{userName}/stopEnvironment |  |


<a id="globalUsersGetEnvironment"></a>
# **globalUsersGetEnvironment**
> GetEnvironmentResponse globalUsersGetEnvironment(userName, apiVersion, environmentOperationsPayload, $expand)



Gets the virtual machine details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    EnvironmentOperationsPayload environmentOperationsPayload = new EnvironmentOperationsPayload(); // EnvironmentOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=environment)'
    try {
      GetEnvironmentResponse result = apiInstance.globalUsersGetEnvironment(userName, apiVersion, environmentOperationsPayload, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersGetEnvironment");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environmentOperationsPayload** | [**EnvironmentOperationsPayload**](EnvironmentOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;environment)&#39; | [optional] |

### Return type

[**GetEnvironmentResponse**](GetEnvironmentResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersGetOperationBatchStatus"></a>
# **globalUsersGetOperationBatchStatus**
> OperationBatchStatusResponse globalUsersGetOperationBatchStatus(userName, apiVersion, operationBatchStatusPayload)



Get batch operation status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    OperationBatchStatusPayload operationBatchStatusPayload = new OperationBatchStatusPayload(); // OperationBatchStatusPayload | Payload to get the status of an operation
    try {
      OperationBatchStatusResponse result = apiInstance.globalUsersGetOperationBatchStatus(userName, apiVersion, operationBatchStatusPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersGetOperationBatchStatus");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **operationBatchStatusPayload** | [**OperationBatchStatusPayload**](OperationBatchStatusPayload.md)| Payload to get the status of an operation | |

### Return type

[**OperationBatchStatusResponse**](OperationBatchStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersGetOperationStatus"></a>
# **globalUsersGetOperationStatus**
> OperationStatusResponse globalUsersGetOperationStatus(userName, apiVersion, operationStatusPayload)



Gets the status of long running operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    OperationStatusPayload operationStatusPayload = new OperationStatusPayload(); // OperationStatusPayload | Payload to get the status of an operation
    try {
      OperationStatusResponse result = apiInstance.globalUsersGetOperationStatus(userName, apiVersion, operationStatusPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersGetOperationStatus");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **operationStatusPayload** | [**OperationStatusPayload**](OperationStatusPayload.md)| Payload to get the status of an operation | |

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersGetPersonalPreferences"></a>
# **globalUsersGetPersonalPreferences**
> GetPersonalPreferencesResponse globalUsersGetPersonalPreferences(userName, apiVersion, personalPreferencesOperationsPayload)



Get personal preferences for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    PersonalPreferencesOperationsPayload personalPreferencesOperationsPayload = new PersonalPreferencesOperationsPayload(); // PersonalPreferencesOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
    try {
      GetPersonalPreferencesResponse result = apiInstance.globalUsersGetPersonalPreferences(userName, apiVersion, personalPreferencesOperationsPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersGetPersonalPreferences");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **personalPreferencesOperationsPayload** | [**PersonalPreferencesOperationsPayload**](PersonalPreferencesOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | |

### Return type

[**GetPersonalPreferencesResponse**](GetPersonalPreferencesResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersListEnvironments"></a>
# **globalUsersListEnvironments**
> ListEnvironmentsResponse globalUsersListEnvironments(userName, apiVersion, listEnvironmentsPayload)



List Environments for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    ListEnvironmentsPayload listEnvironmentsPayload = new ListEnvironmentsPayload(); // ListEnvironmentsPayload | Represents the payload to list environments owned by a user
    try {
      ListEnvironmentsResponse result = apiInstance.globalUsersListEnvironments(userName, apiVersion, listEnvironmentsPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersListEnvironments");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **listEnvironmentsPayload** | [**ListEnvironmentsPayload**](ListEnvironmentsPayload.md)| Represents the payload to list environments owned by a user | |

### Return type

[**ListEnvironmentsResponse**](ListEnvironmentsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersListLabs"></a>
# **globalUsersListLabs**
> ListLabsResponse globalUsersListLabs(userName, apiVersion)



List labs for the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      ListLabsResponse result = apiInstance.globalUsersListLabs(userName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersListLabs");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

### Return type

[**ListLabsResponse**](ListLabsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersRegister"></a>
# **globalUsersRegister**
> globalUsersRegister(userName, apiVersion, registerPayload)



Register a user to a managed lab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    RegisterPayload registerPayload = new RegisterPayload(); // RegisterPayload | Represents payload for Register action.
    try {
      apiInstance.globalUsersRegister(userName, apiVersion, registerPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersRegister");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **registerPayload** | [**RegisterPayload**](RegisterPayload.md)| Represents payload for Register action. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersResetPassword"></a>
# **globalUsersResetPassword**
> globalUsersResetPassword(userName, apiVersion, resetPasswordPayload)



Resets the user password on an environment This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    ResetPasswordPayload resetPasswordPayload = new ResetPasswordPayload(); // ResetPasswordPayload | Represents the payload for resetting passwords.
    try {
      apiInstance.globalUsersResetPassword(userName, apiVersion, resetPasswordPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersResetPassword");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **resetPasswordPayload** | [**ResetPasswordPayload**](ResetPasswordPayload.md)| Represents the payload for resetting passwords. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersStartEnvironment"></a>
# **globalUsersStartEnvironment**
> globalUsersStartEnvironment(userName, apiVersion, environmentOperationsPayload)



Starts an environment by starting all resources inside the environment. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    EnvironmentOperationsPayload environmentOperationsPayload = new EnvironmentOperationsPayload(); // EnvironmentOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
    try {
      apiInstance.globalUsersStartEnvironment(userName, apiVersion, environmentOperationsPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersStartEnvironment");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environmentOperationsPayload** | [**EnvironmentOperationsPayload**](EnvironmentOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="globalUsersStopEnvironment"></a>
# **globalUsersStopEnvironment**
> globalUsersStopEnvironment(userName, apiVersion, environmentOperationsPayload)



Stops an environment by stopping all resources inside the environment This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalUsersApi apiInstance = new GlobalUsersApi(defaultClient);
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    EnvironmentOperationsPayload environmentOperationsPayload = new EnvironmentOperationsPayload(); // EnvironmentOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
    try {
      apiInstance.globalUsersStopEnvironment(userName, apiVersion, environmentOperationsPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalUsersApi#globalUsersStopEnvironment");
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
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environmentOperationsPayload** | [**EnvironmentOperationsPayload**](EnvironmentOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

