# CertificateApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificateCancelDeletion**](CertificateApi.md#certificateCancelDeletion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}/cancelDelete | Cancels a failed deletion of a certificate from the specified account. |
| [**certificateCreate**](CertificateApi.md#certificateCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} |  |
| [**certificateDelete**](CertificateApi.md#certificateDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} |  |
| [**certificateGet**](CertificateApi.md#certificateGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} |  |
| [**certificateListByBatchAccount**](CertificateApi.md#certificateListByBatchAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates |  |
| [**certificateUpdate**](CertificateApi.md#certificateUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} |  |


<a id="certificateCancelDeletion"></a>
# **certificateCancelDeletion**
> Certificate certificateCancelDeletion(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId)

Cancels a failed deletion of a certificate from the specified account.

If you try to delete a certificate that is being used by a pool or compute node, the status of the certificate changes to deleteFailed. If you decide that you want to continue using the certificate, you can use this operation to set the status of the certificate back to active. If you intend to delete the certificate, you do not need to run this operation after the deletion failed. You must make sure that the certificate is not being used by any resources, and then you can try again to delete the certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      Certificate result = apiInstance.certificateCancelDeletion(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#certificateCancelDeletion");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the certificate entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="certificateCreate"></a>
# **certificateCreate**
> Certificate certificateCreate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates a new certificate inside the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    CertificateCreateOrUpdateParameters parameters = new CertificateCreateOrUpdateParameters(); // CertificateCreateOrUpdateParameters | Additional parameters for certificate creation.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the certificate to update. A value of \"*\" can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored.
    try {
      Certificate result = apiInstance.certificateCreate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#certificateCreate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**CertificateCreateOrUpdateParameters**](CertificateCreateOrUpdateParameters.md)| Additional parameters for certificate creation. | |
| **ifMatch** | **String**| The entity state (ETag) version of the certificate to update. A value of \&quot;*\&quot; can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied. | [optional] |
| **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored. | [optional] |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the certificate entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="certificateDelete"></a>
# **certificateDelete**
> certificateDelete(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId)



Deletes the specified certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      apiInstance.certificateDelete(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#certificateDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. |  -  |
| **202** | The operation will be completed asynchronously. |  * Retry-After - Suggested delay to check the status of the asynchronous operation. The value is an integer that represents the seconds. <br>  * Location - The URL of the resource used to check the status of the asynchronous operation. <br>  |
| **204** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="certificateGet"></a>
# **certificateGet**
> Certificate certificateGet(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId)



Gets information about the specified certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      Certificate result = apiInstance.certificateGet(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#certificateGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the certificate entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="certificateListByBatchAccount"></a>
# **certificateListByBatchAccount**
> ListCertificatesResult certificateListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, maxresults, $select, $filter)



Lists all of the certificates in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    String $select = "$select_example"; // String | Comma separated list of properties that should be returned. e.g. \"properties/provisioningState\". Only top level properties under properties/ are valid for selection.
    String $filter = "$filter_example"; // String | OData filter expression. Valid properties for filtering are \"properties/provisioningState\", \"properties/provisioningStateTransitionTime\", \"name\".
    try {
      ListCertificatesResult result = apiInstance.certificateListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, maxresults, $select, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#certificateListByBatchAccount");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **$select** | **String**| Comma separated list of properties that should be returned. e.g. \&quot;properties/provisioningState\&quot;. Only top level properties under properties/ are valid for selection. | [optional] |
| **$filter** | **String**| OData filter expression. Valid properties for filtering are \&quot;properties/provisioningState\&quot;, \&quot;properties/provisioningStateTransitionTime\&quot;, \&quot;name\&quot;. | [optional] |

### Return type

[**ListCertificatesResult**](ListCertificatesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains a list of certificates associated with the account. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="certificateUpdate"></a>
# **certificateUpdate**
> Certificate certificateUpdate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, ifMatch)



Updates the properties of an existing certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    CertificateCreateOrUpdateParameters parameters = new CertificateCreateOrUpdateParameters(); // CertificateCreateOrUpdateParameters | Certificate entity to update.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the certificate to update. This value can be omitted or set to \"*\" to apply the operation unconditionally.
    try {
      Certificate result = apiInstance.certificateUpdate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#certificateUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**CertificateCreateOrUpdateParameters**](CertificateCreateOrUpdateParameters.md)| Certificate entity to update. | |
| **ifMatch** | **String**| The entity state (ETag) version of the certificate to update. This value can be omitted or set to \&quot;*\&quot; to apply the operation unconditionally. | [optional] |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the certificate entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

