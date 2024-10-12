# OrganizationApi

All URIs are relative to *https://api.flat.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countOrgaUsers**](OrganizationApi.md#countOrgaUsers) | **GET** /organizations/users/count | Count the organization users using the provided filters |
| [**createLtiCredentials**](OrganizationApi.md#createLtiCredentials) | **POST** /organizations/lti/credentials | Create a new couple of LTI 1.x credentials |
| [**createOrganizationInvitation**](OrganizationApi.md#createOrganizationInvitation) | **POST** /organizations/invitations | Create a new invitation to join the organization |
| [**createOrganizationUser**](OrganizationApi.md#createOrganizationUser) | **POST** /organizations/users | Create a new user account |
| [**listLtiCredentials**](OrganizationApi.md#listLtiCredentials) | **GET** /organizations/lti/credentials | List LTI 1.x credentials |
| [**listOrganizationInvitations**](OrganizationApi.md#listOrganizationInvitations) | **GET** /organizations/invitations | List the organization invitations |
| [**listOrganizationUsers**](OrganizationApi.md#listOrganizationUsers) | **GET** /organizations/users | List the organization users |
| [**removeOrganizationInvitation**](OrganizationApi.md#removeOrganizationInvitation) | **DELETE** /organizations/invitations/{invitation} | Remove an organization invitation |
| [**removeOrganizationUser**](OrganizationApi.md#removeOrganizationUser) | **DELETE** /organizations/users/{user} | Remove an account from Flat |
| [**revokeLtiCredentials**](OrganizationApi.md#revokeLtiCredentials) | **DELETE** /organizations/lti/credentials/{credentials} | Revoke LTI 1.x credentials |
| [**updateOrganizationUser**](OrganizationApi.md#updateOrganizationUser) | **PUT** /organizations/users/{user} | Update account information |


<a id="countOrgaUsers"></a>
# **countOrgaUsers**
> List&lt;UserDetailsAdmin&gt; countOrgaUsers(role, q, group, noActiveLicense)

Count the organization users using the provided filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    List<String> role = Arrays.asList(); // List<String> | Filter users by role
    String q = "q_example"; // String | The query to search
    List<String> group = Arrays.asList(); // List<String> | Filter users by group
    Boolean noActiveLicense = true; // Boolean | Filter users who don't have an active license
    try {
      List<UserDetailsAdmin> result = apiInstance.countOrgaUsers(role, q, group, noActiveLicense);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#countOrgaUsers");
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
| **role** | [**List&lt;String&gt;**](String.md)| Filter users by role | [optional] [enum: user, teacher, admin] |
| **q** | **String**| The query to search | [optional] |
| **group** | [**List&lt;String&gt;**](String.md)| Filter users by group | [optional] |
| **noActiveLicense** | **Boolean**| Filter users who don&#39;t have an active license | [optional] |

### Return type

[**List&lt;UserDetailsAdmin&gt;**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of users |  -  |
| **0** | Error |  -  |

<a id="createLtiCredentials"></a>
# **createLtiCredentials**
> LtiCredentials createLtiCredentials(body)

Create a new couple of LTI 1.x credentials

Flat for Education is a Certified LTI Provider. You can use these API methods to automate the creation of LTI credentials. You can read more about our LTI implementation, supported components and LTI Endpoints in our [Developer Documentation](https://flat.io/developers/docs/lti/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    LtiCredentialsCreation body = new LtiCredentialsCreation(); // LtiCredentialsCreation | 
    try {
      LtiCredentials result = apiInstance.createLtiCredentials(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#createLtiCredentials");
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
| **body** | [**LtiCredentialsCreation**](LtiCredentialsCreation.md)|  | |

### Return type

[**LtiCredentials**](LtiCredentials.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The LTI Credentials |  -  |
| **403** | Not admin of an organization |  -  |
| **0** | Error |  -  |

<a id="createOrganizationInvitation"></a>
# **createOrganizationInvitation**
> OrganizationInvitation createOrganizationInvitation(body)

Create a new invitation to join the organization

This method creates and sends invitation for teachers and admins.  Invitations can only be used by new Flat users or users who are not part of the organization yet.  If the email of the user is already associated to a user of your organization, the API will simply update the role of the existing user and won&#39;t send an invitation. In this case, the property &#x60;usedBy&#x60; will be directly filled with the uniquer identifier of the corresponding user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    OrganizationInvitationCreation body = new OrganizationInvitationCreation(); // OrganizationInvitationCreation | 
    try {
      OrganizationInvitation result = apiInstance.createOrganizationInvitation(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#createOrganizationInvitation");
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
| **body** | [**OrganizationInvitationCreation**](OrganizationInvitationCreation.md)|  | [optional] |

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New invitation created |  -  |
| **0** | Error |  -  |

<a id="createOrganizationUser"></a>
# **createOrganizationUser**
> UserDetailsAdmin createOrganizationUser(body)

Create a new user account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    UserCreation body = new UserCreation(); // UserCreation | 
    try {
      UserDetailsAdmin result = apiInstance.createOrganizationUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#createOrganizationUser");
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
| **body** | [**UserCreation**](UserCreation.md)|  | [optional] |

### Return type

[**UserDetailsAdmin**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New user created |  -  |
| **0** | Error |  -  |

<a id="listLtiCredentials"></a>
# **listLtiCredentials**
> List&lt;LtiCredentials&gt; listLtiCredentials()

List LTI 1.x credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    try {
      List<LtiCredentials> result = apiInstance.listLtiCredentials();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#listLtiCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;LtiCredentials&gt;**](LtiCredentials.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of LTI Credentials |  -  |
| **403** | Not admin of an organization |  -  |
| **0** | Error |  -  |

<a id="listOrganizationInvitations"></a>
# **listOrganizationInvitations**
> List&lt;OrganizationInvitation&gt; listOrganizationInvitations(role, limit, next, previous)

List the organization invitations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String role = "user"; // String | Filter users by role
    Integer limit = 50; // Integer | This is the maximum number of objects that may be returned
    String next = "next_example"; // String | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data. 
    String previous = "previous_example"; // String | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data. 
    try {
      List<OrganizationInvitation> result = apiInstance.listOrganizationInvitations(role, limit, next, previous);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#listOrganizationInvitations");
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
| **role** | **String**| Filter users by role | [optional] [enum: user, teacher, admin] |
| **limit** | **Integer**| This is the maximum number of objects that may be returned | [optional] [default to 50] |
| **next** | **String**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] |
| **previous** | **String**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] |

### Return type

[**List&lt;OrganizationInvitation&gt;**](OrganizationInvitation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of invitations |  -  |
| **0** | Error |  -  |

<a id="listOrganizationUsers"></a>
# **listOrganizationUsers**
> List&lt;UserDetailsAdmin&gt; listOrganizationUsers(sort, direction, next, previous, role, q, group, noActiveLicense, licenseExpirationDate, onlyIds, limit)

List the organization users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    List<String> sort = Arrays.asList(); // List<String> | The order to sort the user list
    String direction = "asc"; // String | Sort direction
    String next = "next_example"; // String | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data. 
    String previous = "previous_example"; // String | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data. 
    List<String> role = Arrays.asList(); // List<String> | Filter users by role
    String q = "q_example"; // String | The query to search
    List<String> group = Arrays.asList(); // List<String> | Filter users by group
    Boolean noActiveLicense = true; // Boolean | Filter users who don't have an active license
    List<String> licenseExpirationDate = Arrays.asList(); // List<String> | Filter users by license expiration date or `active` / `notActive`
    Boolean onlyIds = true; // Boolean | Return only user ids
    Integer limit = 25; // Integer | This is the maximum number of objects that may be returned
    try {
      List<UserDetailsAdmin> result = apiInstance.listOrganizationUsers(sort, direction, next, previous, role, q, group, noActiveLicense, licenseExpirationDate, onlyIds, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#listOrganizationUsers");
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
| **sort** | [**List&lt;String&gt;**](String.md)| The order to sort the user list | [optional] [enum: firstname, lastname, lastActivityDate, licenseExpirationDate] |
| **direction** | **String**| Sort direction | [optional] [enum: asc, desc] |
| **next** | **String**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] |
| **previous** | **String**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] |
| **role** | [**List&lt;String&gt;**](String.md)| Filter users by role | [optional] [enum: user, teacher, admin] |
| **q** | **String**| The query to search | [optional] |
| **group** | [**List&lt;String&gt;**](String.md)| Filter users by group | [optional] |
| **noActiveLicense** | **Boolean**| Filter users who don&#39;t have an active license | [optional] |
| **licenseExpirationDate** | [**List&lt;String&gt;**](String.md)| Filter users by license expiration date or &#x60;active&#x60; / &#x60;notActive&#x60; | [optional] |
| **onlyIds** | **Boolean**| Return only user ids | [optional] |
| **limit** | **Integer**| This is the maximum number of objects that may be returned | [optional] [default to 25] |

### Return type

[**List&lt;UserDetailsAdmin&gt;**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users |  -  |
| **0** | Error |  -  |

<a id="removeOrganizationInvitation"></a>
# **removeOrganizationInvitation**
> removeOrganizationInvitation(invitation)

Remove an organization invitation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String invitation = "invitation_example"; // String | Unique identifier of the invitation
    try {
      apiInstance.removeOrganizationInvitation(invitation);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#removeOrganizationInvitation");
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
| **invitation** | **String**| Unique identifier of the invitation | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The invitation has been removed |  -  |
| **0** | Error |  -  |

<a id="removeOrganizationUser"></a>
# **removeOrganizationUser**
> removeOrganizationUser(user, convertToIndividual)

Remove an account from Flat

This operation removes an account from Flat and its data, including: * The music scores created by this user (documents, history, comments, collaboration information) * Education related data (assignments and classroom information) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String user = "user_example"; // String | Unique identifier of the Flat account 
    Boolean convertToIndividual = true; // Boolean | If `true`, the account will be only removed from the organization and converted into an individual account on our public website, https://flat.io. This operation will remove the education-related data from the account. Before realizing this operation, you need to be sure that the user is at least 13 years old and that this one has read and agreed to the Individual Terms of Services of Flat available on https://flat.io/legal. 
    try {
      apiInstance.removeOrganizationUser(user, convertToIndividual);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#removeOrganizationUser");
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
| **user** | **String**| Unique identifier of the Flat account  | |
| **convertToIndividual** | **Boolean**| If &#x60;true&#x60;, the account will be only removed from the organization and converted into an individual account on our public website, https://flat.io. This operation will remove the education-related data from the account. Before realizing this operation, you need to be sure that the user is at least 13 years old and that this one has read and agreed to the Individual Terms of Services of Flat available on https://flat.io/legal.  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User deleted |  -  |
| **0** | Error |  -  |

<a id="revokeLtiCredentials"></a>
# **revokeLtiCredentials**
> revokeLtiCredentials(credentials)

Revoke LTI 1.x credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String credentials = "credentials_example"; // String | Credentials unique identifier 
    try {
      apiInstance.revokeLtiCredentials(credentials);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#revokeLtiCredentials");
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
| **credentials** | **String**| Credentials unique identifier  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Credentials revoked |  -  |
| **403** | Not admin of an organization |  -  |
| **404** | Credentials not found |  -  |
| **0** | Error |  -  |

<a id="updateOrganizationUser"></a>
# **updateOrganizationUser**
> UserDetailsAdmin updateOrganizationUser(user, body)

Update account information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String user = "user_example"; // String | Unique identifier of the Flat account 
    UserAdminUpdate body = new UserAdminUpdate(); // UserAdminUpdate | 
    try {
      UserDetailsAdmin result = apiInstance.updateOrganizationUser(user, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#updateOrganizationUser");
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
| **user** | **String**| Unique identifier of the Flat account  | |
| **body** | [**UserAdminUpdate**](UserAdminUpdate.md)|  | |

### Return type

[**UserDetailsAdmin**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User updated |  -  |
| **0** | Error |  -  |

