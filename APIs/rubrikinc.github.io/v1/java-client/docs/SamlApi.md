# SamlApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configRubrikSamlMetadata**](SamlApi.md#configRubrikSamlMetadata) | **POST** /saml/rubrik_metadata | Configure and generate Rubrik SAML metadata |
| [**getSamlSsoStatus**](SamlApi.md#getSamlSsoStatus) | **GET** /saml/sso_status | Check SAML SSO Status |
| [**makeSamlAuthnRequest**](SamlApi.md#makeSamlAuthnRequest) | **POST** /saml/authn_request/{idp_name} | Make SAML authentication request |


<a id="configRubrikSamlMetadata"></a>
# **configRubrikSamlMetadata**
> RubrikSamlMetadataSummary configRubrikSamlMetadata(rubrikSamlMetadataInfo)

Configure and generate Rubrik SAML metadata

Configure and generate the SAML metadata for this Rubrik cluster. The call returns the download URL for the metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    RubrikSamlMetadataInfo rubrikSamlMetadataInfo = new RubrikSamlMetadataInfo(); // RubrikSamlMetadataInfo | Information for generating Rubrik SAML metadata file.
    try {
      RubrikSamlMetadataSummary result = apiInstance.configRubrikSamlMetadata(rubrikSamlMetadataInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#configRubrikSamlMetadata");
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
| **rubrikSamlMetadataInfo** | [**RubrikSamlMetadataInfo**](RubrikSamlMetadataInfo.md)| Information for generating Rubrik SAML metadata file. | |

### Return type

[**RubrikSamlMetadataSummary**](RubrikSamlMetadataSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the URL for downloading the Rubrik SAML metadata. |  -  |

<a id="getSamlSsoStatus"></a>
# **getSamlSsoStatus**
> SamlSsoStatus getSamlSsoStatus()

Check SAML SSO Status

An object that contains two values. A Boolean value that determines whether or not SSO is enabled and an optional String value that indicates the name of the default IdP authentication domain for SSO login. When the boolean value is &#39;true,&#39; SAML SSO is enabled. When the Boolean value is &#39;false,&#39; SAML SSO is disabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    try {
      SamlSsoStatus result = apiInstance.getSamlSsoStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#getSamlSsoStatus");
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

[**SamlSsoStatus**](SamlSsoStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return an object containing SAML SSO status. |  -  |

<a id="makeSamlAuthnRequest"></a>
# **makeSamlAuthnRequest**
> SamlSsoAuthnRequestDetail makeSamlAuthnRequest(idpName, samlSsoAuthnRequestInfo)

Make SAML authentication request

Make a SAML authentication request for a specified IdP Authentication Domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String idpName = "idpName_example"; // String | Name of the IdP Authentication Domain to authenticate with.
    SamlSsoAuthnRequestInfo samlSsoAuthnRequestInfo = new SamlSsoAuthnRequestInfo(); // SamlSsoAuthnRequestInfo | Additional information associated with a single sign-on (SSO) authentication request.
    try {
      SamlSsoAuthnRequestDetail result = apiInstance.makeSamlAuthnRequest(idpName, samlSsoAuthnRequestInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#makeSamlAuthnRequest");
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
| **idpName** | **String**| Name of the IdP Authentication Domain to authenticate with. | |
| **samlSsoAuthnRequestInfo** | [**SamlSsoAuthnRequestInfo**](SamlSsoAuthnRequestInfo.md)| Additional information associated with a single sign-on (SSO) authentication request. | [optional] |

### Return type

[**SamlSsoAuthnRequestDetail**](SamlSsoAuthnRequestDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the necessary data for constructing SAML authentication request. |  -  |

