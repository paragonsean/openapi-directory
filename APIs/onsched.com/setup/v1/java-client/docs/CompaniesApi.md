# CompaniesApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1CompaniesDomainsGet**](CompaniesApi.md#setupV1CompaniesDomainsGet) | **GET** /setup/v1/companies/domains | List Company Domains |
| [**setupV1CompaniesDomainsIdDelete**](CompaniesApi.md#setupV1CompaniesDomainsIdDelete) | **DELETE** /setup/v1/companies/domains/{id} | Delete Company Domain |
| [**setupV1CompaniesDomainsIdGet**](CompaniesApi.md#setupV1CompaniesDomainsIdGet) | **GET** /setup/v1/companies/domains/{id} | Get Company Domain |
| [**setupV1CompaniesDomainsIdPut**](CompaniesApi.md#setupV1CompaniesDomainsIdPut) | **PUT** /setup/v1/companies/domains/{id} | Update Company Domain |
| [**setupV1CompaniesDomainsPost**](CompaniesApi.md#setupV1CompaniesDomainsPost) | **POST** /setup/v1/companies/domains | Create Company Domain |
| [**setupV1CompaniesEmailTemplatesGet**](CompaniesApi.md#setupV1CompaniesEmailTemplatesGet) | **GET** /setup/v1/companies/email/templates | List Email Templates |
| [**setupV1CompaniesEmailTemplatesMasterDelete**](CompaniesApi.md#setupV1CompaniesEmailTemplatesMasterDelete) | **DELETE** /setup/v1/companies/email/templates/master | Delete Master Template Settings |
| [**setupV1CompaniesEmailTemplatesMasterGet**](CompaniesApi.md#setupV1CompaniesEmailTemplatesMasterGet) | **GET** /setup/v1/companies/email/templates/master | Get Master Template Settings |
| [**setupV1CompaniesEmailTemplatesMasterPost**](CompaniesApi.md#setupV1CompaniesEmailTemplatesMasterPost) | **POST** /setup/v1/companies/email/templates/master | Create Master Template Settings |
| [**setupV1CompaniesEmailTemplatesTemplateNameGet**](CompaniesApi.md#setupV1CompaniesEmailTemplatesTemplateNameGet) | **GET** /setup/v1/companies/email/templates/{templateName} | Get Email Template |
| [**setupV1CompaniesGet**](CompaniesApi.md#setupV1CompaniesGet) | **GET** /setup/v1/companies | Get Company |
| [**setupV1CompaniesPost**](CompaniesApi.md#setupV1CompaniesPost) | **POST** /setup/v1/companies | Create Company |
| [**setupV1CompaniesPut**](CompaniesApi.md#setupV1CompaniesPut) | **PUT** /setup/v1/companies | Update Company |
| [**setupV1CompaniesRegionsGet**](CompaniesApi.md#setupV1CompaniesRegionsGet) | **GET** /setup/v1/companies/regions | List Regions |
| [**setupV1CompaniesRegionsIdDelete**](CompaniesApi.md#setupV1CompaniesRegionsIdDelete) | **DELETE** /setup/v1/companies/regions/{id} | Delete Region |
| [**setupV1CompaniesRegionsIdGet**](CompaniesApi.md#setupV1CompaniesRegionsIdGet) | **GET** /setup/v1/companies/regions/{id} | Get Region |
| [**setupV1CompaniesRegionsIdPut**](CompaniesApi.md#setupV1CompaniesRegionsIdPut) | **PUT** /setup/v1/companies/regions/{id} | Update Region |
| [**setupV1CompaniesRegionsPost**](CompaniesApi.md#setupV1CompaniesRegionsPost) | **POST** /setup/v1/companies/regions | Create Region |
| [**setupV1CompaniesTimezonesDateGet**](CompaniesApi.md#setupV1CompaniesTimezonesDateGet) | **GET** /setup/v1/companies/timezones/{date} | List Time Zones |


<a id="setupV1CompaniesDomainsGet"></a>
# **setupV1CompaniesDomainsGet**
> CompanyDomainListViewModel setupV1CompaniesDomainsGet()

List Company Domains

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Company Domains&lt;/b&gt; for the authorized company. To share the OnSchedJS booking widget on your website or in your application your domain must be listed.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      CompanyDomainListViewModel result = apiInstance.setupV1CompaniesDomainsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesDomainsGet");
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

[**CompanyDomainListViewModel**](CompanyDomainListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesDomainsIdDelete"></a>
# **setupV1CompaniesDomainsIdDelete**
> CompanyDomainViewModel setupV1CompaniesDomainsIdDelete(id)

Delete Company Domain

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; an OnSchedJs domain from your authorized company. A valid &lt;b&gt;companyDomain id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String id = "id_example"; // String | id of companyDomain object
    try {
      CompanyDomainViewModel result = apiInstance.setupV1CompaniesDomainsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesDomainsIdDelete");
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
| **id** | **String**| id of companyDomain object | |

### Return type

[**CompanyDomainViewModel**](CompanyDomainViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesDomainsIdGet"></a>
# **setupV1CompaniesDomainsIdGet**
> CompanyDomainViewModel setupV1CompaniesDomainsIdGet(id)

Get Company Domain

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Company Domain&lt;/b&gt; object. A valid &lt;b&gt;companyDomain id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String id = "id_example"; // String | id of companyDomain object
    try {
      CompanyDomainViewModel result = apiInstance.setupV1CompaniesDomainsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesDomainsIdGet");
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
| **id** | **String**| id of companyDomain object | |

### Return type

[**CompanyDomainViewModel**](CompanyDomainViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesDomainsIdPut"></a>
# **setupV1CompaniesDomainsIdPut**
> CompanyDomainViewModel setupV1CompaniesDomainsIdPut(id, companyDomainUpdateModel)

Update Company Domain

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; an OnSchedJs domain for your authorized company. A valid &lt;b&gt;companyDomain id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String id = "id_example"; // String | id of companyDomain object
    CompanyDomainUpdateModel companyDomainUpdateModel = new CompanyDomainUpdateModel(); // CompanyDomainUpdateModel | Company Domain Update Model
    try {
      CompanyDomainViewModel result = apiInstance.setupV1CompaniesDomainsIdPut(id, companyDomainUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesDomainsIdPut");
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
| **id** | **String**| id of companyDomain object | |
| **companyDomainUpdateModel** | [**CompanyDomainUpdateModel**](CompanyDomainUpdateModel.md)| Company Domain Update Model | [optional] |

### Return type

[**CompanyDomainViewModel**](CompanyDomainViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesDomainsPost"></a>
# **setupV1CompaniesDomainsPost**
> CompanyDomainViewModel setupV1CompaniesDomainsPost(companyDomainInputModel)

Create Company Domain

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; an OnSchedJs domain for your authorized company. To share the OnSchedJS booking widget on your website or in your application you must add the domain.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    CompanyDomainInputModel companyDomainInputModel = new CompanyDomainInputModel(); // CompanyDomainInputModel | Company Domain Input Model
    try {
      CompanyDomainViewModel result = apiInstance.setupV1CompaniesDomainsPost(companyDomainInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesDomainsPost");
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
| **companyDomainInputModel** | [**CompanyDomainInputModel**](CompanyDomainInputModel.md)| Company Domain Input Model | [optional] |

### Return type

[**CompanyDomainViewModel**](CompanyDomainViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesEmailTemplatesGet"></a>
# **setupV1CompaniesEmailTemplatesGet**
> EmailTemplateListViewModel setupV1CompaniesEmailTemplatesGet()

List Email Templates

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Email Templates&lt;/b&gt; that are provided and may be customized. If the template has been customized, the customized property is true. The scope parameter indicates if the email template has been customized at the Business Location level or Company level. This endpoint returns &lt;b&gt;only company level templates&lt;/b&gt;, so the scope is always company.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      EmailTemplateListViewModel result = apiInstance.setupV1CompaniesEmailTemplatesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesEmailTemplatesGet");
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

[**EmailTemplateListViewModel**](EmailTemplateListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesEmailTemplatesMasterDelete"></a>
# **setupV1CompaniesEmailTemplatesMasterDelete**
> MasterEmailTemplateSettingsViewModel setupV1CompaniesEmailTemplatesMasterDelete()

Delete Master Template Settings

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete Custom Master Email Template Settings&lt;/b&gt;. Deleting a custom master email template setting will reactivate the original default OnSched template settings.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      MasterEmailTemplateSettingsViewModel result = apiInstance.setupV1CompaniesEmailTemplatesMasterDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesEmailTemplatesMasterDelete");
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

[**MasterEmailTemplateSettingsViewModel**](MasterEmailTemplateSettingsViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesEmailTemplatesMasterGet"></a>
# **setupV1CompaniesEmailTemplatesMasterGet**
> MasterEmailTemplateSettingsViewModel setupV1CompaniesEmailTemplatesMasterGet()

Get Master Template Settings

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Master Email Template Settings&lt;/b&gt;. Settings exist for showing or hiding email panels and for changing color schemes. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      MasterEmailTemplateSettingsViewModel result = apiInstance.setupV1CompaniesEmailTemplatesMasterGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesEmailTemplatesMasterGet");
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

[**MasterEmailTemplateSettingsViewModel**](MasterEmailTemplateSettingsViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesEmailTemplatesMasterPost"></a>
# **setupV1CompaniesEmailTemplatesMasterPost**
> MasterEmailTemplateSettingsViewModel setupV1CompaniesEmailTemplatesMasterPost(masterTemplateSettingsInputModel)

Create Master Template Settings

&lt;p&gt;Use this endpoint to &lt;b&gt;Create Custom Master Email Template Settings&lt;/b&gt;. Settings exist for showing or hiding email panels and for changing color schemes. Use the &lt;i&gt;GET ​/setup​/v1​/companies​/email​/templates&lt;/i&gt; endpoint to display the settings offered. Changes to the Master Template Settings will be reflected in all business locations associated with this company. &lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. There are no endpoints to update the templates, we use the post endpoint to create a custom template instead. This endpoint creates a new custom Master Template Settings file that will be used instead. If you delete it you are deleting the custom template settings you created and the original default Master Template created by OnSched would be reactivated.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    MasterTemplateSettingsInputModel masterTemplateSettingsInputModel = new MasterTemplateSettingsInputModel(); // MasterTemplateSettingsInputModel | 
    try {
      MasterEmailTemplateSettingsViewModel result = apiInstance.setupV1CompaniesEmailTemplatesMasterPost(masterTemplateSettingsInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesEmailTemplatesMasterPost");
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
| **masterTemplateSettingsInputModel** | [**MasterTemplateSettingsInputModel**](MasterTemplateSettingsInputModel.md)|  | [optional] |

### Return type

[**MasterEmailTemplateSettingsViewModel**](MasterEmailTemplateSettingsViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesEmailTemplatesTemplateNameGet"></a>
# **setupV1CompaniesEmailTemplatesTemplateNameGet**
> ContentResult setupV1CompaniesEmailTemplatesTemplateNameGet(templateName)

Get Email Template

&lt;p&gt;Use this endpoint to return the requested &lt;b&gt;Email Template&lt;/b&gt;. If it wasn&#39;t customized the default template is returned. The response content is in html format. A valid emailTemplate &lt;b&gt;name&lt;/b&gt; is required. Find template names by using the: &lt;i&gt;GET ​/setup​/v1​/companies​/email​/templates&lt;/i&gt; endpoint. Note: The master template cannot be accessed here. &lt;/p&gt;  &lt;p&gt;To create custom company email templates, go to the &lt;i&gt;POST ​/setup​/v1​/locations​/{id}​/email​/templates&lt;/i&gt; endpoint and create a template using the Primary Business Location Id.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String templateName = "templateName_example"; // String | Email template name
    try {
      ContentResult result = apiInstance.setupV1CompaniesEmailTemplatesTemplateNameGet(templateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesEmailTemplatesTemplateNameGet");
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
| **templateName** | **String**| Email template name | |

### Return type

[**ContentResult**](ContentResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesGet"></a>
# **setupV1CompaniesGet**
> CompanyViewModel setupV1CompaniesGet()

Get Company

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Authorized Company&lt;/b&gt; information. The company is the main entity that oversees all business locations defined below it, hierarchically. &lt;/p&gt;  &lt;p&gt;Access to the company credentials gives you access to all business locations defined in the authorized company. Client credentials resolve to a single company and are purposely hidden from this endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      CompanyViewModel result = apiInstance.setupV1CompaniesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesGet");
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

[**CompanyViewModel**](CompanyViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesPost"></a>
# **setupV1CompaniesPost**
> CompanyViewModel setupV1CompaniesPost(companyInputModel)

Create Company

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new authorized company.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Note: Special API Partner credentials are required to access this endpoint.&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;name, registrationEmail, phone, country&lt;/b&gt; and &lt;b&gt;timezoneName&lt;/b&gt; are required fields. For &lt;b&gt;country&lt;/b&gt; use the standard ISO 3166 2-character country code.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;timezoneName&lt;/b&gt; must be expressed as an IANA Timezone e.g., &lt;i&gt;America/New_York&lt;/i&gt;.&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone IANA Wiki&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    CompanyInputModel companyInputModel = new CompanyInputModel(); // CompanyInputModel | Company Input Model
    try {
      CompanyViewModel result = apiInstance.setupV1CompaniesPost(companyInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesPost");
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
| **companyInputModel** | [**CompanyInputModel**](CompanyInputModel.md)| Company Input Model | [optional] |

### Return type

[**CompanyViewModel**](CompanyViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesPut"></a>
# **setupV1CompaniesPut**
> CompanyViewModel setupV1CompaniesPut(companyUpdateModel)

Update Company

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; the authorized company information. Your client credentials resolve to a single company. The timezoneName must be expressed as an IANA Timezone, e.g., &lt;i&gt;America/New_York&lt;/i&gt;. &lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone IANA Wiki&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    CompanyUpdateModel companyUpdateModel = new CompanyUpdateModel(); // CompanyUpdateModel | Company Update Model
    try {
      CompanyViewModel result = apiInstance.setupV1CompaniesPut(companyUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesPut");
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
| **companyUpdateModel** | [**CompanyUpdateModel**](CompanyUpdateModel.md)| Company Update Model | [optional] |

### Return type

[**CompanyViewModel**](CompanyViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesRegionsGet"></a>
# **setupV1CompaniesRegionsGet**
> RegionListViewModel setupV1CompaniesRegionsGet(offset, limit)

List Regions

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Regions&lt;/b&gt; in the authorized company. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      RegionListViewModel result = apiInstance.setupV1CompaniesRegionsGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesRegionsGet");
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
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**RegionListViewModel**](RegionListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | region object&#39;s |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error. |  -  |
| **404** | Resource was not found |  -  |

<a id="setupV1CompaniesRegionsIdDelete"></a>
# **setupV1CompaniesRegionsIdDelete**
> RegionViewModel setupV1CompaniesRegionsIdDelete(id)

Delete Region

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a region object. A valid &lt;b&gt;region id&lt;/b&gt; is required. If the region is related to any business locations it won&#39;t be deleted. You must first remove any references to region id from the business locations prior to deleting.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String id = "id_example"; // String | id of Region
    try {
      RegionViewModel result = apiInstance.setupV1CompaniesRegionsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesRegionsIdDelete");
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
| **id** | **String**| id of Region | |

### Return type

[**RegionViewModel**](RegionViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesRegionsIdGet"></a>
# **setupV1CompaniesRegionsIdGet**
> RegionViewModel setupV1CompaniesRegionsIdGet(id)

Get Region

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Region&lt;/b&gt; object. A valid &lt;b&gt;region id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String id = "id_example"; // String | id of a region object
    try {
      RegionViewModel result = apiInstance.setupV1CompaniesRegionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesRegionsIdGet");
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
| **id** | **String**| id of a region object | |

### Return type

[**RegionViewModel**](RegionViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesRegionsIdPut"></a>
# **setupV1CompaniesRegionsIdPut**
> RegionViewModel setupV1CompaniesRegionsIdPut(id, regionUpdateModel)

Update Region

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a region object. A valid &lt;b&gt;region id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String id = "id_example"; // String | id of Region
    RegionUpdateModel regionUpdateModel = new RegionUpdateModel(); // RegionUpdateModel | Region Update Model
    try {
      RegionViewModel result = apiInstance.setupV1CompaniesRegionsIdPut(id, regionUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesRegionsIdPut");
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
| **id** | **String**| id of Region | |
| **regionUpdateModel** | [**RegionUpdateModel**](RegionUpdateModel.md)| Region Update Model | [optional] |

### Return type

[**RegionViewModel**](RegionViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesRegionsPost"></a>
# **setupV1CompaniesRegionsPost**
> RegionViewModel setupV1CompaniesRegionsPost(regionInputModel)

Create Region

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a region object. Regions can be mapped to business locations. They can be used by the locations endpoints to filter locations by region id.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    RegionInputModel regionInputModel = new RegionInputModel(); // RegionInputModel | 
    try {
      RegionViewModel result = apiInstance.setupV1CompaniesRegionsPost(regionInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesRegionsPost");
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
| **regionInputModel** | [**RegionInputModel**](RegionInputModel.md)|  | [optional] |

### Return type

[**RegionViewModel**](RegionViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CompaniesTimezonesDateGet"></a>
# **setupV1CompaniesTimezonesDateGet**
> TimezoneViewModel setupV1CompaniesTimezonesDateGet(date)

List Time Zones

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of timezone names, timezoneIana and tzOffset values&lt;/b&gt; calculated for the date requested. Daylight Savings may or may not apply depending on the date specified.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | \"YYYY-MM-DD: Date for timezone info\"
    try {
      TimezoneViewModel result = apiInstance.setupV1CompaniesTimezonesDateGet(date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#setupV1CompaniesTimezonesDateGet");
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
| **date** | **OffsetDateTime**| \&quot;YYYY-MM-DD: Date for timezone info\&quot; | |

### Return type

[**TimezoneViewModel**](TimezoneViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

