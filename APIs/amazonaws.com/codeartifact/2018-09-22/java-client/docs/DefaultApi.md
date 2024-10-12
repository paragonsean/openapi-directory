# DefaultApi

All URIs are relative to *http://codeartifact.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateExternalConnection**](DefaultApi.md#associateExternalConnection) | **POST** /v1/repository/external-connection#domain&amp;repository&amp;external-connection |  |
| [**copyPackageVersions**](DefaultApi.md#copyPackageVersions) | **POST** /v1/package/versions/copy#domain&amp;source-repository&amp;destination-repository&amp;format&amp;package |  |
| [**createDomain**](DefaultApi.md#createDomain) | **POST** /v1/domain#domain |  |
| [**createRepository**](DefaultApi.md#createRepository) | **POST** /v1/repository#domain&amp;repository |  |
| [**deleteDomain**](DefaultApi.md#deleteDomain) | **DELETE** /v1/domain#domain |  |
| [**deleteDomainPermissionsPolicy**](DefaultApi.md#deleteDomainPermissionsPolicy) | **DELETE** /v1/domain/permissions/policy#domain |  |
| [**deletePackage**](DefaultApi.md#deletePackage) | **DELETE** /v1/package#domain&amp;repository&amp;format&amp;package |  |
| [**deletePackageVersions**](DefaultApi.md#deletePackageVersions) | **POST** /v1/package/versions/delete#domain&amp;repository&amp;format&amp;package |  |
| [**deleteRepository**](DefaultApi.md#deleteRepository) | **DELETE** /v1/repository#domain&amp;repository |  |
| [**deleteRepositoryPermissionsPolicy**](DefaultApi.md#deleteRepositoryPermissionsPolicy) | **DELETE** /v1/repository/permissions/policies#domain&amp;repository |  |
| [**describeDomain**](DefaultApi.md#describeDomain) | **GET** /v1/domain#domain |  |
| [**describePackage**](DefaultApi.md#describePackage) | **GET** /v1/package#domain&amp;repository&amp;format&amp;package |  |
| [**describePackageVersion**](DefaultApi.md#describePackageVersion) | **GET** /v1/package/version#domain&amp;repository&amp;format&amp;package&amp;version |  |
| [**describeRepository**](DefaultApi.md#describeRepository) | **GET** /v1/repository#domain&amp;repository |  |
| [**disassociateExternalConnection**](DefaultApi.md#disassociateExternalConnection) | **DELETE** /v1/repository/external-connection#domain&amp;repository&amp;external-connection |  |
| [**disposePackageVersions**](DefaultApi.md#disposePackageVersions) | **POST** /v1/package/versions/dispose#domain&amp;repository&amp;format&amp;package |  |
| [**getAuthorizationToken**](DefaultApi.md#getAuthorizationToken) | **POST** /v1/authorization-token#domain |  |
| [**getDomainPermissionsPolicy**](DefaultApi.md#getDomainPermissionsPolicy) | **GET** /v1/domain/permissions/policy#domain |  |
| [**getPackageVersionAsset**](DefaultApi.md#getPackageVersionAsset) | **GET** /v1/package/version/asset#domain&amp;repository&amp;format&amp;package&amp;version&amp;asset |  |
| [**getPackageVersionReadme**](DefaultApi.md#getPackageVersionReadme) | **GET** /v1/package/version/readme#domain&amp;repository&amp;format&amp;package&amp;version |  |
| [**getRepositoryEndpoint**](DefaultApi.md#getRepositoryEndpoint) | **GET** /v1/repository/endpoint#domain&amp;repository&amp;format |  |
| [**getRepositoryPermissionsPolicy**](DefaultApi.md#getRepositoryPermissionsPolicy) | **GET** /v1/repository/permissions/policy#domain&amp;repository |  |
| [**listDomains**](DefaultApi.md#listDomains) | **POST** /v1/domains |  |
| [**listPackageVersionAssets**](DefaultApi.md#listPackageVersionAssets) | **POST** /v1/package/version/assets#domain&amp;repository&amp;format&amp;package&amp;version |  |
| [**listPackageVersionDependencies**](DefaultApi.md#listPackageVersionDependencies) | **POST** /v1/package/version/dependencies#domain&amp;repository&amp;format&amp;package&amp;version |  |
| [**listPackageVersions**](DefaultApi.md#listPackageVersions) | **POST** /v1/package/versions#domain&amp;repository&amp;format&amp;package |  |
| [**listPackages**](DefaultApi.md#listPackages) | **POST** /v1/packages#domain&amp;repository |  |
| [**listRepositories**](DefaultApi.md#listRepositories) | **POST** /v1/repositories |  |
| [**listRepositoriesInDomain**](DefaultApi.md#listRepositoriesInDomain) | **POST** /v1/domain/repositories#domain |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /v1/tags#resourceArn |  |
| [**publishPackageVersion**](DefaultApi.md#publishPackageVersion) | **POST** /v1/package/version/publish#domain&amp;repository&amp;format&amp;package&amp;version&amp;asset&amp;x-amz-content-sha256 |  |
| [**putDomainPermissionsPolicy**](DefaultApi.md#putDomainPermissionsPolicy) | **PUT** /v1/domain/permissions/policy |  |
| [**putPackageOriginConfiguration**](DefaultApi.md#putPackageOriginConfiguration) | **POST** /v1/package#domain&amp;repository&amp;format&amp;package |  |
| [**putRepositoryPermissionsPolicy**](DefaultApi.md#putRepositoryPermissionsPolicy) | **PUT** /v1/repository/permissions/policy#domain&amp;repository |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /v1/tag#resourceArn |  |
| [**untagResource**](DefaultApi.md#untagResource) | **POST** /v1/untag#resourceArn |  |
| [**updatePackageVersionsStatus**](DefaultApi.md#updatePackageVersionsStatus) | **POST** /v1/package/versions/update_status#domain&amp;repository&amp;format&amp;package |  |
| [**updateRepository**](DefaultApi.md#updateRepository) | **PUT** /v1/repository#domain&amp;repository |  |


<a id="associateExternalConnection"></a>
# **associateExternalConnection**
> AssociateExternalConnectionResult associateExternalConnection(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



&lt;p&gt;Adds an existing external connection to a repository. One external connection is allowed per repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository can have one or more upstream repositories, or an external connection.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | The name of the domain that contains the repository.
    String repository = "repository_example"; // String |  The name of the repository to which the external connection is added. 
    String externalConnection = "externalConnection_example"; // String | <p> The name of the external connection to add to the repository. The following values are supported: </p> <ul> <li> <p> <code>public:npmjs</code> - for the npm public repository. </p> </li> <li> <p> <code>public:nuget-org</code> - for the NuGet Gallery. </p> </li> <li> <p> <code>public:pypi</code> - for the Python Package Index. </p> </li> <li> <p> <code>public:maven-central</code> - for Maven Central. </p> </li> <li> <p> <code>public:maven-googleandroid</code> - for the Google Android repository. </p> </li> <li> <p> <code>public:maven-gradleplugins</code> - for the Gradle plugins repository. </p> </li> <li> <p> <code>public:maven-commonsware</code> - for the CommonsWare Android repository. </p> </li> <li> <p> <code>public:maven-clojars</code> - for the Clojars repository. </p> </li> </ul>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      AssociateExternalConnectionResult result = apiInstance.associateExternalConnection(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateExternalConnection");
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
| **domain** | **String**| The name of the domain that contains the repository. | |
| **repository** | **String**|  The name of the repository to which the external connection is added.  | |
| **externalConnection** | **String**| &lt;p&gt; The name of the external connection to add to the repository. The following values are supported: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:npmjs&lt;/code&gt; - for the npm public repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:nuget-org&lt;/code&gt; - for the NuGet Gallery. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:pypi&lt;/code&gt; - for the Python Package Index. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-central&lt;/code&gt; - for Maven Central. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-googleandroid&lt;/code&gt; - for the Google Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-gradleplugins&lt;/code&gt; - for the Gradle plugins repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-commonsware&lt;/code&gt; - for the CommonsWare Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-clojars&lt;/code&gt; - for the Clojars repository. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**AssociateExternalConnectionResult**](AssociateExternalConnectionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="copyPackageVersions"></a>
# **copyPackageVersions**
> CopyPackageVersionsResult copyPackageVersions(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



&lt;p&gt; Copies package versions from one repository to another repository in the same domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the source and destination repositories. 
    String sourceRepository = "sourceRepository_example"; // String |  The name of the repository that contains the package versions to be copied. 
    String destinationRepository = "destinationRepository_example"; // String |  The name of the repository into which package versions are copied. 
    String format = "npm"; // String |  The format of the package versions to be copied. 
    String _package = "_package_example"; // String |  The name of the package that contains the versions to be copied. 
    CopyPackageVersionsRequest copyPackageVersionsRequest = new CopyPackageVersionsRequest(); // CopyPackageVersionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. The namespace is required when copying Maven package versions. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      CopyPackageVersionsResult result = apiInstance.copyPackageVersions(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyPackageVersions");
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
| **domain** | **String**|  The name of the domain that contains the source and destination repositories.  | |
| **sourceRepository** | **String**|  The name of the repository that contains the package versions to be copied.  | |
| **destinationRepository** | **String**|  The name of the repository into which package versions are copied.  | |
| **format** | **String**|  The format of the package versions to be copied.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package that contains the versions to be copied.  | |
| **copyPackageVersionsRequest** | [**CopyPackageVersionsRequest**](CopyPackageVersionsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when copying Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**CopyPackageVersionsResult**](CopyPackageVersionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="createDomain"></a>
# **createDomain**
> CreateDomainResult createDomain(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Creates a domain. CodeArtifact &lt;i&gt;domains&lt;/i&gt; make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it&#39;s in multiple repositories. &lt;/p&gt; &lt;p&gt;Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. &lt;/p&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable. 
    CreateDomainRequest createDomainRequest = new CreateDomainRequest(); // CreateDomainRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDomainResult result = apiInstance.createDomain(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDomain");
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
| **domain** | **String**|  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable.  | |
| **createDomainRequest** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDomainResult**](CreateDomainResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="createRepository"></a>
# **createRepository**
> CreateRepositoryResult createRepository(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Creates a repository. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the created repository. 
    String repository = "repository_example"; // String |  The name of the repository to create. 
    CreateRepositoryRequest createRepositoryRequest = new CreateRepositoryRequest(); // CreateRepositoryRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      CreateRepositoryResult result = apiInstance.createRepository(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRepository");
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
| **domain** | **String**|  The name of the domain that contains the created repository.  | |
| **repository** | **String**|  The name of the repository to create.  | |
| **createRepositoryRequest** | [**CreateRepositoryRequest**](CreateRepositoryRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**CreateRepositoryResult**](CreateRepositoryResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="deleteDomain"></a>
# **deleteDomain**
> DeleteDomainResult deleteDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain to delete. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      DeleteDomainResult result = apiInstance.deleteDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDomain");
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
| **domain** | **String**|  The name of the domain to delete.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**DeleteDomainResult**](DeleteDomainResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="deleteDomainPermissionsPolicy"></a>
# **deleteDomainPermissionsPolicy**
> DeleteDomainPermissionsPolicyResult deleteDomainPermissionsPolicy(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision)



 Deletes the resource policy set on a domain. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain associated with the resource policy to be deleted. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String policyRevision = "policyRevision_example"; // String |  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. 
    try {
      DeleteDomainPermissionsPolicyResult result = apiInstance.deleteDomainPermissionsPolicy(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDomainPermissionsPolicy");
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
| **domain** | **String**|  The name of the domain associated with the resource policy to be deleted.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **policyRevision** | **String**|  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy.  | [optional] |

### Return type

[**DeleteDomainPermissionsPolicyResult**](DeleteDomainPermissionsPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="deletePackage"></a>
# **deletePackage**
> DeletePackageResult deletePackage(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\&quot;&gt;DeletePackageVersions&lt;/a&gt; API.

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | The name of the domain that contains the package to delete.
    String repository = "repository_example"; // String | The name of the repository that contains the package to delete.
    String format = "npm"; // String | The format of the requested package to delete.
    String _package = "_package_example"; // String | The name of the package to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. The namespace is required when deleting Maven package versions. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>.</p> </li> <li> <p> Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      DeletePackageResult result = apiInstance.deletePackage(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePackage");
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
| **domain** | **String**| The name of the domain that contains the package to delete. | |
| **repository** | **String**| The name of the repository that contains the package to delete. | |
| **format** | **String**| The format of the requested package to delete. | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**| The name of the package to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**DeletePackageResult**](DeletePackageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="deletePackageVersions"></a>
# **deletePackageVersions**
> DeletePackageVersionsResult deletePackageVersions(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



 Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to &lt;code&gt;Archived&lt;/code&gt;. Archived packages cannot be downloaded from a repository and don&#39;t show up with list package APIs (for example, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt;), but you can restore them using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionsStatus&lt;/a&gt;. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the package to delete. 
    String repository = "repository_example"; // String |  The name of the repository that contains the package versions to delete. 
    String format = "npm"; // String |  The format of the package versions to delete. 
    String _package = "_package_example"; // String |  The name of the package with the versions to delete. 
    DeletePackageVersionsRequest deletePackageVersionsRequest = new DeletePackageVersionsRequest(); // DeletePackageVersionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. The namespace is required when deleting Maven package versions. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      DeletePackageVersionsResult result = apiInstance.deletePackageVersions(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePackageVersions");
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
| **domain** | **String**|  The name of the domain that contains the package to delete.  | |
| **repository** | **String**|  The name of the repository that contains the package versions to delete.  | |
| **format** | **String**|  The format of the package versions to delete.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package with the versions to delete.  | |
| **deletePackageVersionsRequest** | [**DeletePackageVersionsRequest**](DeletePackageVersionsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**DeletePackageVersionsResult**](DeletePackageVersionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="deleteRepository"></a>
# **deleteRepository**
> DeleteRepositoryResult deleteRepository(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Deletes a repository. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository to delete. 
    String repository = "repository_example"; // String |  The name of the repository to delete. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      DeleteRepositoryResult result = apiInstance.deleteRepository(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRepository");
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
| **domain** | **String**|  The name of the domain that contains the repository to delete.  | |
| **repository** | **String**|  The name of the repository to delete.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**DeleteRepositoryResult**](DeleteRepositoryResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="deleteRepositoryPermissionsPolicy"></a>
# **deleteRepositoryPermissionsPolicy**
> DeleteRepositoryPermissionsPolicyResult deleteRepositoryPermissionsPolicy(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision)



&lt;p&gt; Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. &lt;/p&gt; &lt;important&gt; &lt;p&gt; Use &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt; with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. &lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository associated with the resource policy to be deleted. 
    String repository = "repository_example"; // String |  The name of the repository that is associated with the resource policy to be deleted 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String policyRevision = "policyRevision_example"; // String |  The revision of the repository's resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository's resource policy. 
    try {
      DeleteRepositoryPermissionsPolicyResult result = apiInstance.deleteRepositoryPermissionsPolicy(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRepositoryPermissionsPolicy");
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
| **domain** | **String**|  The name of the domain that contains the repository associated with the resource policy to be deleted.  | |
| **repository** | **String**|  The name of the repository that is associated with the resource policy to be deleted  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **policyRevision** | **String**|  The revision of the repository&#39;s resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository&#39;s resource policy.  | [optional] |

### Return type

[**DeleteRepositoryPermissionsPolicyResult**](DeleteRepositoryPermissionsPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="describeDomain"></a>
# **describeDomain**
> DescribeDomainResult describeDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\&quot;&gt;DomainDescription&lt;/a&gt; object that contains information about the requested domain. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  A string that specifies the name of the requested domain. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      DescribeDomainResult result = apiInstance.describeDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeDomain");
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
| **domain** | **String**|  A string that specifies the name of the requested domain.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**DescribeDomainResult**](DescribeDomainResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="describePackage"></a>
# **describePackage**
> DescribePackageResult describePackage(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



 Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains information about the requested package.

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | The name of the domain that contains the repository that contains the package.
    String repository = "repository_example"; // String | The name of the repository that contains the requested package. 
    String format = "npm"; // String | A format that specifies the type of the requested package.
    String _package = "_package_example"; // String | The name of the requested package.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. The namespace is required when requesting Maven packages. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      DescribePackageResult result = apiInstance.describePackage(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describePackage");
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
| **domain** | **String**| The name of the domain that contains the repository that contains the package. | |
| **repository** | **String**| The name of the repository that contains the requested package.  | |
| **format** | **String**| A format that specifies the type of the requested package. | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**| The name of the requested package. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when requesting Maven packages. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**DescribePackageResult**](DescribePackageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="describePackageVersion"></a>
# **describePackageVersion**
> DescribePackageVersionResult describePackageVersion(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



 Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains information about the requested package version. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the package version. 
    String repository = "repository_example"; // String |  The name of the repository that contains the package version. 
    String format = "npm"; // String |  A format that specifies the type of the requested package version. 
    String _package = "_package_example"; // String |  The name of the requested package version. 
    String version = "version_example"; // String |  A string that contains the package version (for example, <code>3.5.2</code>). 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      DescribePackageVersionResult result = apiInstance.describePackageVersion(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describePackageVersion");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the package version.  | |
| **repository** | **String**|  The name of the repository that contains the package version.  | |
| **format** | **String**|  A format that specifies the type of the requested package version.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the requested package version.  | |
| **version** | **String**|  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**DescribePackageVersionResult**](DescribePackageVersionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="describeRepository"></a>
# **describeRepository**
> DescribeRepositoryResult describeRepository(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository to describe. 
    String repository = "repository_example"; // String |  A string that specifies the name of the requested repository. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      DescribeRepositoryResult result = apiInstance.describeRepository(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeRepository");
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
| **domain** | **String**|  The name of the domain that contains the repository to describe.  | |
| **repository** | **String**|  A string that specifies the name of the requested repository.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**DescribeRepositoryResult**](DescribeRepositoryResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="disassociateExternalConnection"></a>
# **disassociateExternalConnection**
> DisassociateExternalConnectionResult disassociateExternalConnection(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Removes an existing external connection from a repository. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | The name of the domain that contains the repository from which to remove the external repository. 
    String repository = "repository_example"; // String | The name of the repository from which the external connection will be removed. 
    String externalConnection = "externalConnection_example"; // String | The name of the external connection to be removed from the repository. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      DisassociateExternalConnectionResult result = apiInstance.disassociateExternalConnection(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateExternalConnection");
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
| **domain** | **String**| The name of the domain that contains the repository from which to remove the external repository.  | |
| **repository** | **String**| The name of the repository from which the external connection will be removed.  | |
| **externalConnection** | **String**| The name of the external connection to be removed from the repository.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**DisassociateExternalConnectionResult**](DisassociateExternalConnectionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="disposePackageVersions"></a>
# **disposePackageVersions**
> DisposePackageVersionsResult disposePackageVersions(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



&lt;p&gt; Deletes the assets in package versions and sets the package versions&#39; status to &lt;code&gt;Disposed&lt;/code&gt;. A disposed package version cannot be restored in your repository because its assets are deleted. &lt;/p&gt; &lt;p&gt; To view all disposed package versions in a repository, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt; and set the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\&quot;&gt;status&lt;/a&gt; parameter to &lt;code&gt;Disposed&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; To view information about a disposed package version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\&quot;&gt;DescribePackageVersion&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository you want to dispose. 
    String repository = "repository_example"; // String |  The name of the repository that contains the package versions you want to dispose. 
    String format = "npm"; // String |  A format that specifies the type of package versions you want to dispose. 
    String _package = "_package_example"; // String |  The name of the package with the versions you want to dispose. 
    DisposePackageVersionsRequest disposePackageVersionsRequest = new DisposePackageVersionsRequest(); // DisposePackageVersionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      DisposePackageVersionsResult result = apiInstance.disposePackageVersions(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disposePackageVersions");
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
| **domain** | **String**|  The name of the domain that contains the repository you want to dispose.  | |
| **repository** | **String**|  The name of the repository that contains the package versions you want to dispose.  | |
| **format** | **String**|  A format that specifies the type of package versions you want to dispose.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package with the versions you want to dispose.  | |
| **disposePackageVersionsRequest** | [**DisposePackageVersionsRequest**](DisposePackageVersionsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**DisposePackageVersionsResult**](DisposePackageVersionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="getAuthorizationToken"></a>
# **getAuthorizationToken**
> GetAuthorizationTokenResult getAuthorizationToken(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration)



&lt;p&gt; Generates a temporary authorization token for accessing repositories in the domain. This API requires the &lt;code&gt;codeartifact:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions. For more information about authorization tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\&quot;&gt;CodeArtifact authentication and tokens&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CodeArtifact authorization tokens are valid for a period of 12 hours when created with the &lt;code&gt;login&lt;/code&gt; command. You can call &lt;code&gt;login&lt;/code&gt; periodically to refresh the token. When you create an authorization token with the &lt;code&gt;GetAuthorizationToken&lt;/code&gt; API, you can set a custom authorization period, up to a maximum of 12 hours, with the &lt;code&gt;durationSeconds&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The authorization period begins after &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called. If &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call &lt;code&gt;sts assume-role&lt;/code&gt; and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.&lt;/p&gt; &lt;p&gt;See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\&quot;&gt;Using IAM Roles&lt;/a&gt; for more information on controlling session duration. &lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that is in scope for the generated authorization token. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    Integer duration = 56; // Integer | The time, in seconds, that the generated authorization token is valid. Valid values are <code>0</code> and any number between <code>900</code> (15 minutes) and <code>43200</code> (12 hours). A value of <code>0</code> will set the expiration of the authorization token to the same expiration of the user's role's temporary credentials.
    try {
      GetAuthorizationTokenResult result = apiInstance.getAuthorizationToken(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAuthorizationToken");
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
| **domain** | **String**|  The name of the domain that is in scope for the generated authorization token.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **duration** | **Integer**| The time, in seconds, that the generated authorization token is valid. Valid values are &lt;code&gt;0&lt;/code&gt; and any number between &lt;code&gt;900&lt;/code&gt; (15 minutes) and &lt;code&gt;43200&lt;/code&gt; (12 hours). A value of &lt;code&gt;0&lt;/code&gt; will set the expiration of the authorization token to the same expiration of the user&#39;s role&#39;s temporary credentials. | [optional] |

### Return type

[**GetAuthorizationTokenResult**](GetAuthorizationTokenResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="getDomainPermissionsPolicy"></a>
# **getDomainPermissionsPolicy**
> GetDomainPermissionsPolicyResult getDomainPermissionsPolicy(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



&lt;p&gt; Returns the resource policy attached to the specified domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; The policy is a resource-based policy, not an identity-based policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\&quot;&gt;Identity-based policies and resource-based policies &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain to which the resource policy is attached. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      GetDomainPermissionsPolicyResult result = apiInstance.getDomainPermissionsPolicy(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDomainPermissionsPolicy");
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
| **domain** | **String**|  The name of the domain to which the resource policy is attached.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**GetDomainPermissionsPolicyResult**](GetDomainPermissionsPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="getPackageVersionAsset"></a>
# **getPackageVersionAsset**
> GetPackageVersionAssetResult getPackageVersionAsset(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision)



 Returns an asset (or file) that is in a package. For example, for a Maven package version, use &lt;code&gt;GetPackageVersionAsset&lt;/code&gt; to download a &lt;code&gt;JAR&lt;/code&gt; file, a &lt;code&gt;POM&lt;/code&gt; file, or any other assets in the package version. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the package version with the requested asset. 
    String repository = "repository_example"; // String |  The repository that contains the package version with the requested asset. 
    String format = "npm"; // String |  A format that specifies the type of the package version with the requested asset file. 
    String _package = "_package_example"; // String |  The name of the package that contains the requested asset. 
    String version = "version_example"; // String |  A string that contains the package version (for example, <code>3.5.2</code>). 
    String asset = "asset_example"; // String |  The name of the requested asset. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    String revision = "revision_example"; // String |  The name of the package version revision that contains the requested asset. 
    try {
      GetPackageVersionAssetResult result = apiInstance.getPackageVersionAsset(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPackageVersionAsset");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the package version with the requested asset.  | |
| **repository** | **String**|  The repository that contains the package version with the requested asset.  | |
| **format** | **String**|  A format that specifies the type of the package version with the requested asset file.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package that contains the requested asset.  | |
| **version** | **String**|  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  | |
| **asset** | **String**|  The name of the requested asset.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **revision** | **String**|  The name of the package version revision that contains the requested asset.  | [optional] |

### Return type

[**GetPackageVersionAssetResult**](GetPackageVersionAssetResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |
| **485** | ConflictException |  -  |

<a id="getPackageVersionReadme"></a>
# **getPackageVersionReadme**
> GetPackageVersionReadmeResult getPackageVersionReadme(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



&lt;p&gt; Gets the readme file or descriptive text for a package version. &lt;/p&gt; &lt;p&gt; The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. &lt;/p&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the package version with the requested readme file. 
    String repository = "repository_example"; // String |  The repository that contains the package with the requested readme file. 
    String format = "npm"; // String |  A format that specifies the type of the package version with the requested readme file. 
    String _package = "_package_example"; // String |  The name of the package version that contains the requested readme file. 
    String version = "version_example"; // String |  A string that contains the package version (for example, <code>3.5.2</code>). 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
    try {
      GetPackageVersionReadmeResult result = apiInstance.getPackageVersionReadme(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPackageVersionReadme");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the package version with the requested readme file.  | |
| **repository** | **String**|  The repository that contains the package with the requested readme file.  | |
| **format** | **String**|  A format that specifies the type of the package version with the requested readme file.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package version that contains the requested readme file.  | |
| **version** | **String**|  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**GetPackageVersionReadmeResult**](GetPackageVersionReadmeResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="getRepositoryEndpoint"></a>
# **getRepositoryEndpoint**
> GetRepositoryEndpointResult getRepositoryEndpoint(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



&lt;p&gt; Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository. 
    String repository = "repository_example"; // String |  The name of the repository. 
    String format = "npm"; // String |  Returns which endpoint of a repository to return. A repository has one endpoint for each package format. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces. 
    try {
      GetRepositoryEndpointResult result = apiInstance.getRepositoryEndpoint(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRepositoryEndpoint");
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
| **domain** | **String**|  The name of the domain that contains the repository.  | |
| **repository** | **String**|  The name of the repository.  | |
| **format** | **String**|  Returns which endpoint of a repository to return. A repository has one endpoint for each package format.  | [enum: npm, pypi, maven, nuget, generic] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.  | [optional] |

### Return type

[**GetRepositoryEndpointResult**](GetRepositoryEndpointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="getRepositoryPermissionsPolicy"></a>
# **getRepositoryPermissionsPolicy**
> GetRepositoryPermissionsPolicyResult getRepositoryPermissionsPolicy(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Returns the resource policy that is set on a repository. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain containing the repository whose associated resource policy is to be retrieved. 
    String repository = "repository_example"; // String |  The name of the repository whose associated resource policy is to be retrieved. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      GetRepositoryPermissionsPolicyResult result = apiInstance.getRepositoryPermissionsPolicy(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRepositoryPermissionsPolicy");
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
| **domain** | **String**|  The name of the domain containing the repository whose associated resource policy is to be retrieved.  | |
| **repository** | **String**|  The name of the repository whose associated resource policy is to be retrieved.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**GetRepositoryPermissionsPolicyResult**](GetRepositoryPermissionsPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="listDomains"></a>
# **listDomains**
> ListDomainsResult listDomains(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;DomainSummary&lt;/a&gt; objects for all domains owned by the Amazon Web Services account that makes this call. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListDomainsRequest listDomainsRequest = new ListDomainsRequest(); // ListDomainsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListDomainsResult result = apiInstance.listDomains(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDomains");
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
| **listDomainsRequest** | [**ListDomainsRequest**](ListDomainsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListDomainsResult**](ListDomainsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="listPackageVersionAssets"></a>
# **listPackageVersionAssets**
> ListPackageVersionAssetsResult listPackageVersionAssets(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\&quot;&gt;AssetSummary&lt;/a&gt; objects for assets in a package version. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository associated with the package version assets. 
    String repository = "repository_example"; // String |  The name of the repository that contains the package that contains the requested package version assets. 
    String format = "npm"; // String |  The format of the package that contains the requested package version assets. 
    String _package = "_package_example"; // String |  The name of the package that contains the requested package version assets. 
    String version = "version_example"; // String |  A string that contains the package version (for example, <code>3.5.2</code>). 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    Integer maxResults = 56; // Integer |  The maximum number of results to return per page. 
    String nextToken = "nextToken_example"; // String |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListPackageVersionAssetsResult result = apiInstance.listPackageVersionAssets(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPackageVersionAssets");
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
| **domain** | **String**|  The name of the domain that contains the repository associated with the package version assets.  | |
| **repository** | **String**|  The name of the repository that contains the package that contains the requested package version assets.  | |
| **format** | **String**|  The format of the package that contains the requested package version assets.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package that contains the requested package version assets.  | |
| **version** | **String**|  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **maxResults** | **Integer**|  The maximum number of results to return per page.  | [optional] |
| **nextToken** | **String**|  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListPackageVersionAssetsResult**](ListPackageVersionAssetsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="listPackageVersionDependencies"></a>
# **listPackageVersionDependencies**
> ListPackageVersionDependenciesResult listPackageVersionDependencies(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken)



 Returns the direct dependencies for a package version. The dependencies are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\&quot;&gt;PackageDependency&lt;/a&gt; objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the &lt;code&gt;package.json&lt;/code&gt; file for npm packages and the &lt;code&gt;pom.xml&lt;/code&gt; file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the requested package version dependencies. 
    String repository = "repository_example"; // String |  The name of the repository that contains the requested package version. 
    String format = "npm"; // String |  The format of the package with the requested dependencies. 
    String _package = "_package_example"; // String |  The name of the package versions' package. 
    String version = "version_example"; // String |  A string that contains the package version (for example, <code>3.5.2</code>). 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    String nextToken = "nextToken_example"; // String |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    try {
      ListPackageVersionDependenciesResult result = apiInstance.listPackageVersionDependencies(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPackageVersionDependencies");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the requested package version dependencies.  | |
| **repository** | **String**|  The name of the repository that contains the requested package version.  | |
| **format** | **String**|  The format of the package with the requested dependencies.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package versions&#39; package.  | |
| **version** | **String**|  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **nextToken** | **String**|  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  | [optional] |

### Return type

[**ListPackageVersionDependenciesResult**](ListPackageVersionDependenciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="listPackageVersions"></a>
# **listPackageVersions**
> ListPackageVersionsResult listPackageVersions(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\&quot;&gt;PackageVersionSummary&lt;/a&gt; objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling &lt;code&gt;list-package-versions&lt;/code&gt; with no &lt;code&gt;--status&lt;/code&gt; parameter. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the requested package versions. 
    String repository = "repository_example"; // String |  The name of the repository that contains the requested package versions. 
    String format = "npm"; // String |  The format of the package versions you want to list. 
    String _package = "_package_example"; // String |  The name of the package for which you want to request package versions. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    String status = "Published"; // String |  A string that filters the requested package versions by status. 
    String sortBy = "PUBLISHED_TIME"; // String |  How to sort the requested list of package versions. 
    Integer maxResults = 56; // Integer |  The maximum number of results to return per page. 
    String nextToken = "nextToken_example"; // String |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    String originType = "INTERNAL"; // String | The <code>originType</code> used to filter package versions. Only package versions with the provided <code>originType</code> will be returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListPackageVersionsResult result = apiInstance.listPackageVersions(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPackageVersions");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the requested package versions.  | |
| **repository** | **String**|  The name of the repository that contains the requested package versions.  | |
| **format** | **String**|  The format of the package versions you want to list.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package for which you want to request package versions.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **status** | **String**|  A string that filters the requested package versions by status.  | [optional] [enum: Published, Unfinished, Unlisted, Archived, Disposed, Deleted] |
| **sortBy** | **String**|  How to sort the requested list of package versions.  | [optional] [enum: PUBLISHED_TIME] |
| **maxResults** | **Integer**|  The maximum number of results to return per page.  | [optional] |
| **nextToken** | **String**|  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  | [optional] |
| **originType** | **String**| The &lt;code&gt;originType&lt;/code&gt; used to filter package versions. Only package versions with the provided &lt;code&gt;originType&lt;/code&gt; will be returned. | [optional] [enum: INTERNAL, EXTERNAL, UNKNOWN] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListPackageVersionsResult**](ListPackageVersionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="listPackages"></a>
# **listPackages**
> ListPackagesResult listPackages(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\&quot;&gt;PackageSummary&lt;/a&gt; objects for packages in a repository that match the request parameters. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the requested packages. 
    String repository = "repository_example"; // String |  The name of the repository that contains the requested packages. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String format = "npm"; // String | The format used to filter requested packages. Only packages from the provided format will be returned.
    String namespace = "namespace_example"; // String | <p>The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called <code>--namespace</code> and not <code>--namespace-prefix</code>, it has prefix-matching behavior.</p> <p>Each package format uses namespace as follows:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    String packagePrefix = "packagePrefix_example"; // String |  A prefix used to filter requested packages. Only packages with names that start with <code>packagePrefix</code> are returned. 
    Integer maxResults = 56; // Integer |  The maximum number of results to return per page. 
    String nextToken = "nextToken_example"; // String |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    String publish = "ALLOW"; // String | The value of the <code>Publish</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a>.
    String upstream = "ALLOW"; // String | The value of the <code>Upstream</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a>.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListPackagesResult result = apiInstance.listPackages(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPackages");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the requested packages.  | |
| **repository** | **String**|  The name of the repository that contains the requested packages.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **format** | **String**| The format used to filter requested packages. Only packages from the provided format will be returned. | [optional] [enum: npm, pypi, maven, nuget, generic] |
| **namespace** | **String**| &lt;p&gt;The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called &lt;code&gt;--namespace&lt;/code&gt; and not &lt;code&gt;--namespace-prefix&lt;/code&gt;, it has prefix-matching behavior.&lt;/p&gt; &lt;p&gt;Each package format uses namespace as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **packagePrefix** | **String**|  A prefix used to filter requested packages. Only packages with names that start with &lt;code&gt;packagePrefix&lt;/code&gt; are returned.  | [optional] |
| **maxResults** | **Integer**|  The maximum number of results to return per page.  | [optional] |
| **nextToken** | **String**|  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  | [optional] |
| **publish** | **String**| The value of the &lt;code&gt;Publish&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. | [optional] [enum: ALLOW, BLOCK] |
| **upstream** | **String**| The value of the &lt;code&gt;Upstream&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. | [optional] [enum: ALLOW, BLOCK] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListPackagesResult**](ListPackagesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="listRepositories"></a>
# **listRepositories**
> ListRepositoriesResult listRepositories(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String repositoryPrefix = "repositoryPrefix_example"; // String |  A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned.
    Integer maxResults = 56; // Integer |  The maximum number of results to return per page. 
    String nextToken = "nextToken_example"; // String |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListRepositoriesResult result = apiInstance.listRepositories(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRepositories");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **repositoryPrefix** | **String**|  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned. | [optional] |
| **maxResults** | **Integer**|  The maximum number of results to return per page.  | [optional] |
| **nextToken** | **String**|  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListRepositoriesResult**](ListRepositoriesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="listRepositoriesInDomain"></a>
# **listRepositoriesInDomain**
> ListRepositoriesInDomainResult listRepositoriesInDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified domain and that matches the input parameters. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the returned list of repositories. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String administratorAccount = "administratorAccount_example"; // String |  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID. 
    String repositoryPrefix = "repositoryPrefix_example"; // String |  A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned. 
    Integer maxResults = 56; // Integer |  The maximum number of results to return per page. 
    String nextToken = "nextToken_example"; // String |  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListRepositoriesInDomainResult result = apiInstance.listRepositoriesInDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRepositoriesInDomain");
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
| **domain** | **String**|  The name of the domain that contains the returned list of repositories.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **administratorAccount** | **String**|  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID.  | [optional] |
| **repositoryPrefix** | **String**|  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned.  | [optional] |
| **maxResults** | **Integer**|  The maximum number of results to return per page.  | [optional] |
| **nextToken** | **String**|  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListRepositoriesInDomainResult**](ListRepositoriesInDomainResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResult listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to get tags for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResult result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to get tags for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResult**](ListTagsForResourceResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="publishPackageVersion"></a>
# **publishPackageVersion**
> PublishPackageVersionResult publishPackageVersion(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished)



&lt;p&gt;Creates a new package version containing one or more assets (or files).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;unfinished&lt;/code&gt; flag can be used to keep the package version in the &lt;code&gt;Unfinished&lt;/code&gt; state until all of its assets have been uploaded (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact user guide&lt;/i&gt;). To set the package version’s status to &lt;code&gt;Published&lt;/code&gt;, omit the &lt;code&gt;unfinished&lt;/code&gt; flag when uploading the final asset, or set the status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionStatus&lt;/a&gt;. Once a package version’s status is set to &lt;code&gt;Published&lt;/code&gt;, it cannot change back to &lt;code&gt;Unfinished&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only generic packages can be published using this API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\&quot;&gt;Using generic packages&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | The name of the domain that contains the repository that contains the package version to publish.
    String repository = "repository_example"; // String | The name of the repository that the package version will be published to.
    String format = "npm"; // String | <p>A format that specifies the type of the package version with the requested asset file.</p> <p>The only supported value is <code>generic</code>.</p>
    String _package = "_package_example"; // String | The name of the package version to publish.
    String version = "version_example"; // String | The package version to publish (for example, <code>3.5.2</code>).
    String asset = "asset_example"; // String | The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: <code>~ ! @ ^ &amp; ( ) - ` _ + [ ] { } ; , . `</code> 
    String xAmzContentSha257 = "xAmzContentSha256_example"; // String | <p>The SHA256 hash of the <code>assetContent</code> to publish. This value must be calculated by the caller and provided with the request (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\">Publishing a generic package</a> in the <i>CodeArtifact User Guide</i>).</p> <p>This value is used as an integrity check to verify that the <code>assetContent</code> has not changed after it was originally sent.</p>
    PublishPackageVersionRequest publishPackageVersionRequest = new PublishPackageVersionRequest(); // PublishPackageVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String | The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
    String namespace = "namespace_example"; // String | The namespace of the package version to publish.
    Boolean unfinished = true; // Boolean | <p>Specifies whether the package version should remain in the <code>unfinished</code> state. If omitted, the package version status will be set to <code>Published</code> (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\">Package version status</a> in the <i>CodeArtifact User Guide</i>).</p> <p>Valid values: <code>unfinished</code> </p>
    try {
      PublishPackageVersionResult result = apiInstance.publishPackageVersion(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishPackageVersion");
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
| **domain** | **String**| The name of the domain that contains the repository that contains the package version to publish. | |
| **repository** | **String**| The name of the repository that the package version will be published to. | |
| **format** | **String**| &lt;p&gt;A format that specifies the type of the package version with the requested asset file.&lt;/p&gt; &lt;p&gt;The only supported value is &lt;code&gt;generic&lt;/code&gt;.&lt;/p&gt; | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**| The name of the package version to publish. | |
| **version** | **String**| The package version to publish (for example, &lt;code&gt;3.5.2&lt;/code&gt;). | |
| **asset** | **String**| The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: &lt;code&gt;~ ! @ ^ &amp;amp; ( ) - &#x60; _ + [ ] { } ; , . &#x60;&lt;/code&gt;  | |
| **xAmzContentSha257** | **String**| &lt;p&gt;The SHA256 hash of the &lt;code&gt;assetContent&lt;/code&gt; to publish. This value must be calculated by the caller and provided with the request (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\&quot;&gt;Publishing a generic package&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;This value is used as an integrity check to verify that the &lt;code&gt;assetContent&lt;/code&gt; has not changed after it was originally sent.&lt;/p&gt; | |
| **publishPackageVersionRequest** | [**PublishPackageVersionRequest**](PublishPackageVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**| The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces. | [optional] |
| **namespace** | **String**| The namespace of the package version to publish. | [optional] |
| **unfinished** | **Boolean**| &lt;p&gt;Specifies whether the package version should remain in the &lt;code&gt;unfinished&lt;/code&gt; state. If omitted, the package version status will be set to &lt;code&gt;Published&lt;/code&gt; (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;unfinished&lt;/code&gt; &lt;/p&gt; | [optional] |

### Return type

[**PublishPackageVersionResult**](PublishPackageVersionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="putDomainPermissionsPolicy"></a>
# **putDomainPermissionsPolicy**
> PutDomainPermissionsPolicyResult putDomainPermissionsPolicy(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Sets a resource policy on a domain that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. &lt;/p&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest = new PutDomainPermissionsPolicyRequest(); // PutDomainPermissionsPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutDomainPermissionsPolicyResult result = apiInstance.putDomainPermissionsPolicy(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putDomainPermissionsPolicy");
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
| **putDomainPermissionsPolicyRequest** | [**PutDomainPermissionsPolicyRequest**](PutDomainPermissionsPolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutDomainPermissionsPolicyResult**](PutDomainPermissionsPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="putPackageOriginConfiguration"></a>
# **putPackageOriginConfiguration**
> PutPackageOriginConfigurationResult putPackageOriginConfiguration(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



&lt;p&gt;Sets the package origin configuration for a package.&lt;/p&gt; &lt;p&gt;The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\&quot;&gt;Editing package origin controls&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt; can be called on a package that doesn&#39;t yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.&lt;/p&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | The name of the domain that contains the repository that contains the package.
    String repository = "repository_example"; // String | The name of the repository that contains the package.
    String format = "npm"; // String | A format that specifies the type of the package to be updated.
    String _package = "_package_example"; // String | The name of the package to be updated.
    PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest = new PutPackageOriginConfigurationRequest(); // PutPackageOriginConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      PutPackageOriginConfigurationResult result = apiInstance.putPackageOriginConfiguration(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putPackageOriginConfiguration");
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
| **domain** | **String**| The name of the domain that contains the repository that contains the package. | |
| **repository** | **String**| The name of the repository that contains the package. | |
| **format** | **String**| A format that specifies the type of the package to be updated. | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**| The name of the package to be updated. | |
| **putPackageOriginConfigurationRequest** | [**PutPackageOriginConfigurationRequest**](PutPackageOriginConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**PutPackageOriginConfigurationResult**](PutPackageOriginConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="putRepositoryPermissionsPolicy"></a>
# **putRepositoryPermissionsPolicy**
> PutRepositoryPermissionsPolicyResult putRepositoryPermissionsPolicy(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



&lt;p&gt; Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. &lt;/p&gt;

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain containing the repository to set the resource policy on. 
    String repository = "repository_example"; // String |  The name of the repository to set the resource policy on. 
    PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest = new PutRepositoryPermissionsPolicyRequest(); // PutRepositoryPermissionsPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      PutRepositoryPermissionsPolicyResult result = apiInstance.putRepositoryPermissionsPolicy(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putRepositoryPermissionsPolicy");
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
| **domain** | **String**|  The name of the domain containing the repository to set the resource policy on.  | |
| **repository** | **String**|  The name of the repository to set the resource policy on.  | |
| **putRepositoryPermissionsPolicyRequest** | [**PutRepositoryPermissionsPolicyRequest**](PutRepositoryPermissionsPolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**PutRepositoryPermissionsPolicyResult**](PutRepositoryPermissionsPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds or updates tags for a resource in CodeArtifact.

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource that you want to add or update tags for. | |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ServiceQuotaExceededException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ValidationException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes tags from a resource in CodeArtifact.

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to remove tags from.
    UntagResourceRequest untagResourceRequest = new UntagResourceRequest(); // UntagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource that you want to remove tags from. | |
| **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="updatePackageVersionsStatus"></a>
# **updatePackageVersionsStatus**
> UpdatePackageVersionsStatusResult updatePackageVersionsStatus(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace)



 Updates the status of one or more versions of a package. Using &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;, you can update the status of package versions to &lt;code&gt;Archived&lt;/code&gt;, &lt;code&gt;Published&lt;/code&gt;, or &lt;code&gt;Unlisted&lt;/code&gt;. To set the status of a package version to &lt;code&gt;Disposed&lt;/code&gt;, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\&quot;&gt;DisposePackageVersions&lt;/a&gt;. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain that contains the repository that contains the package versions with a status to be updated. 
    String repository = "repository_example"; // String |  The repository that contains the package versions with the status you want to update. 
    String format = "npm"; // String |  A format that specifies the type of the package with the statuses to update. 
    String _package = "_package_example"; // String |  The name of the package with the version statuses to update. 
    UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest = new UpdatePackageVersionsStatusRequest(); // UpdatePackageVersionsStatusRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    String namespace = "namespace_example"; // String | <p>The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
    try {
      UpdatePackageVersionsStatusResult result = apiInstance.updatePackageVersionsStatus(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePackageVersionsStatus");
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
| **domain** | **String**|  The name of the domain that contains the repository that contains the package versions with a status to be updated.  | |
| **repository** | **String**|  The repository that contains the package versions with the status you want to update.  | |
| **format** | **String**|  A format that specifies the type of the package with the statuses to update.  | [enum: npm, pypi, maven, nuget, generic] |
| **_package** | **String**|  The name of the package with the version statuses to update.  | |
| **updatePackageVersionsStatusRequest** | [**UpdatePackageVersionsStatusRequest**](UpdatePackageVersionsStatusRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |
| **namespace** | **String**| &lt;p&gt;The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**UpdatePackageVersionsStatusResult**](UpdatePackageVersionsStatusResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ValidationException |  -  |

<a id="updateRepository"></a>
# **updateRepository**
> UpdateRepositoryResult updateRepository(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner)



 Update the properties of a repository. 

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
    defaultClient.setBasePath("http://codeartifact.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String |  The name of the domain associated with the repository to update. 
    String repository = "repository_example"; // String |  The name of the repository to update. 
    UpdateRepositoryRequest updateRepositoryRequest = new UpdateRepositoryRequest(); // UpdateRepositoryRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String domainOwner = "domainOwner_example"; // String |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    try {
      UpdateRepositoryResult result = apiInstance.updateRepository(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRepository");
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
| **domain** | **String**|  The name of the domain associated with the repository to update.  | |
| **repository** | **String**|  The name of the repository to update.  | |
| **updateRepositoryRequest** | [**UpdateRepositoryRequest**](UpdateRepositoryRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **domainOwner** | **String**|  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  | [optional] |

### Return type

[**UpdateRepositoryResult**](UpdateRepositoryResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | ConflictException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ValidationException |  -  |

