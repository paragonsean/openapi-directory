# DefaultApi

All URIs are relative to *http://portal.sso.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRoleCredentials**](DefaultApi.md#getRoleCredentials) | **GET** /federation/credentials#role_name&amp;account_id&amp;x-amz-sso_bearer_token |  |
| [**listAccountRoles**](DefaultApi.md#listAccountRoles) | **GET** /assignment/roles#x-amz-sso_bearer_token&amp;account_id |  |
| [**listAccounts**](DefaultApi.md#listAccounts) | **GET** /assignment/accounts#x-amz-sso_bearer_token |  |
| [**logout**](DefaultApi.md#logout) | **POST** /logout#x-amz-sso_bearer_token |  |


<a id="getRoleCredentials"></a>
# **getRoleCredentials**
> GetRoleCredentialsResponse getRoleCredentials(roleName, accountId, xAmzSsoBearerToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns the STS short-term credentials for a given role name that is assigned to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://portal.sso.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String roleName = "roleName_example"; // String | The friendly name of the role that is assigned to the user.
    String accountId = "accountId_example"; // String | The identifier for the AWS account that is assigned to the user.
    String xAmzSsoBearerToken = "xAmzSsoBearerToken_example"; // String | The token issued by the <code>CreateToken</code> API call. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetRoleCredentialsResponse result = apiInstance.getRoleCredentials(roleName, accountId, xAmzSsoBearerToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRoleCredentials");
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
| **roleName** | **String**| The friendly name of the role that is assigned to the user. | |
| **accountId** | **String**| The identifier for the AWS account that is assigned to the user. | |
| **xAmzSsoBearerToken** | **String**| The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetRoleCredentialsResponse**](GetRoleCredentialsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | UnauthorizedException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="listAccountRoles"></a>
# **listAccountRoles**
> ListAccountRolesResponse listAccountRoles(xAmzSsoBearerToken, accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResult, maxResults, nextToken2)



Lists all roles that are assigned to the user for a given AWS account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://portal.sso.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzSsoBearerToken = "xAmzSsoBearerToken_example"; // String | The token issued by the <code>CreateToken</code> API call. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.
    String accountId = "accountId_example"; // String | The identifier for the AWS account that is assigned to the user.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The page token from the previous response output when you request subsequent pages.
    Integer maxResult = 56; // Integer | The number of items that clients can request per page.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAccountRolesResponse result = apiInstance.listAccountRoles(xAmzSsoBearerToken, accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResult, maxResults, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccountRoles");
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
| **xAmzSsoBearerToken** | **String**| The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;. | |
| **accountId** | **String**| The identifier for the AWS account that is assigned to the user. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The page token from the previous response output when you request subsequent pages. | [optional] |
| **maxResult** | **Integer**| The number of items that clients can request per page. | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAccountRolesResponse**](ListAccountRolesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | UnauthorizedException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="listAccounts"></a>
# **listAccounts**
> ListAccountsResponse listAccounts(xAmzSsoBearerToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResult, maxResults, nextToken2)



Lists all AWS accounts assigned to the user. These AWS accounts are assigned by the administrator of the account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html#assignusers\&quot;&gt;Assign User Access&lt;/a&gt; in the &lt;i&gt;IAM Identity Center User Guide&lt;/i&gt;. This operation returns a paginated response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://portal.sso.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzSsoBearerToken = "xAmzSsoBearerToken_example"; // String | The token issued by the <code>CreateToken</code> API call. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | (Optional) When requesting subsequent pages, this is the page token from the previous response output.
    Integer maxResult = 56; // Integer | This is the number of items clients can request per page.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAccountsResponse result = apiInstance.listAccounts(xAmzSsoBearerToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResult, maxResults, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccounts");
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
| **xAmzSsoBearerToken** | **String**| The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| (Optional) When requesting subsequent pages, this is the page token from the previous response output. | [optional] |
| **maxResult** | **Integer**| This is the number of items clients can request per page. | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | UnauthorizedException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="logout"></a>
# **logout**
> logout(xAmzSsoBearerToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes the locally stored SSO tokens from the client-side cache and sends an API call to the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center sign in session.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a user uses IAM Identity Center to access the AWS CLI, the user’s IAM Identity Center sign in session is used to obtain an IAM session, as specified in the corresponding IAM Identity Center permission set. More specifically, IAM Identity Center assumes an IAM role in the target account on behalf of the user, and the corresponding temporary AWS credentials are returned to the client.&lt;/p&gt; &lt;p&gt;After user logout, any existing IAM role sessions that were created by using IAM Identity Center permission sets continue based on the duration configured in the permission set. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html\&quot;&gt;User authentications&lt;/a&gt; in the &lt;i&gt;IAM Identity Center User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://portal.sso.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzSsoBearerToken = "xAmzSsoBearerToken_example"; // String | The token issued by the <code>CreateToken</code> API call. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.logout(xAmzSsoBearerToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#logout");
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
| **xAmzSsoBearerToken** | **String**| The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | UnauthorizedException |  -  |
| **482** | TooManyRequestsException |  -  |

