# openapi-java-client

CodeArtifact
- API version: 2018-09-22
  - Build date: 2024-10-12T12:07:53.978156-04:00[America/New_York]
  - Generator version: 7.9.0

<p> CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. </p> <p> <b>CodeArtifact Components</b> </p> <p>Use the information in this guide to help you work with the following CodeArtifact components:</p> <ul> <li> <p> <b>Repository</b>: A CodeArtifact repository contains a set of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\">package versions</a>, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <b> <code>npm</code> </b> CLI, the Maven CLI (<b> <code>mvn</code> </b>), Python CLIs (<b> <code>pip</code> </b> and <code>twine</code>), and NuGet CLIs (<code>nuget</code> and <code>dotnet</code>).</p> </li> <li> <p> <b>Domain</b>: Repositories are aggregated into a higher-level entity known as a <i>domain</i>. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it's present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in Key Management Service (KMS).</p> <p>Each repository is a member of a single domain and can't be moved to a different domain.</p> <p>The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.</p> <p>Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.</p> </li> <li> <p> <b>Package</b>: A <i>package</i> is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\">npm</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\">PyPI</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\">Maven</a>, and <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget\">NuGet</a> package formats.</p> <p>In CodeArtifact, a package consists of:</p> <ul> <li> <p>A <i>name</i> (for example, <code>webpack</code> is the name of a popular npm package)</p> </li> <li> <p>An optional namespace (for example, <code>@types</code> in <code>@types/node</code>)</p> </li> <li> <p>A set of versions (for example, <code>1.0.0</code>, <code>1.0.1</code>, <code>1.0.2</code>, etc.)</p> </li> <li> <p> Package-level metadata (for example, npm tags)</p> </li> </ul> </li> <li> <p> <b>Package version</b>: A version of a package, such as <code>@types/node 12.6.9</code>. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the <a href=\"https://semver.org/\">Semantic Versioning specification</a>. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.</p> </li> <li> <p> <b>Upstream repository</b>: One repository is <i>upstream</i> of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.</p> </li> <li> <p> <b>Asset</b>: An individual file stored in CodeArtifact associated with a package version, such as an npm <code>.tgz</code> file or Maven POM and JAR files.</p> </li> </ul> <p>CodeArtifact supports these operations:</p> <ul> <li> <p> <code>AssociateExternalConnection</code>: Adds an existing external connection to a repository. </p> </li> <li> <p> <code>CopyPackageVersions</code>: Copies package versions from one repository to another repository in the same domain.</p> </li> <li> <p> <code>CreateDomain</code>: Creates a domain</p> </li> <li> <p> <code>CreateRepository</code>: Creates a CodeArtifact repository in a domain. </p> </li> <li> <p> <code>DeleteDomain</code>: Deletes a domain. You cannot delete a domain that contains repositories. </p> </li> <li> <p> <code>DeleteDomainPermissionsPolicy</code>: Deletes the resource policy that is set on a domain.</p> </li> <li> <p> <code>DeletePackage</code>: Deletes a package and all associated package versions.</p> </li> <li> <p> <code>DeletePackageVersions</code>: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DeleteRepository</code>: Deletes a repository. </p> </li> <li> <p> <code>DeleteRepositoryPermissionsPolicy</code>: Deletes the resource policy that is set on a repository.</p> </li> <li> <p> <code>DescribeDomain</code>: Returns a <code>DomainDescription</code> object that contains information about the requested domain.</p> </li> <li> <p> <code>DescribePackage</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains details about a package. </p> </li> <li> <p> <code>DescribePackageVersion</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains details about a package version. </p> </li> <li> <p> <code>DescribeRepository</code>: Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p> </li> <li> <p> <code>DisposePackageVersions</code>: Disposes versions of a package. A package version with the status <code>Disposed</code> cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DisassociateExternalConnection</code>: Removes an existing external connection from a repository. </p> </li> <li> <p> <code>GetAuthorizationToken</code>: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.</p> </li> <li> <p> <code>GetDomainPermissionsPolicy</code>: Returns the policy of a resource that is attached to the specified domain. </p> </li> <li> <p> <code>GetPackageVersionAsset</code>: Returns the contents of an asset that is in a package version. </p> </li> <li> <p> <code>GetPackageVersionReadme</code>: Gets the readme file or descriptive text for a package version.</p> </li> <li> <p> <code>GetRepositoryEndpoint</code>: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> </ul> </li> <li> <p> <code>GetRepositoryPermissionsPolicy</code>: Returns the resource policy that is set on a repository. </p> </li> <li> <p> <code>ListDomains</code>: Returns a list of <code>DomainSummary</code> objects. Each returned <code>DomainSummary</code> object contains information about a domain.</p> </li> <li> <p> <code>ListPackages</code>: Lists the packages in a repository.</p> </li> <li> <p> <code>ListPackageVersionAssets</code>: Lists the assets for a given package version.</p> </li> <li> <p> <code>ListPackageVersionDependencies</code>: Returns a list of the direct dependencies for a package version. </p> </li> <li> <p> <code>ListPackageVersions</code>: Returns a list of package versions for a specified package in a repository.</p> </li> <li> <p> <code>ListRepositories</code>: Returns a list of repositories owned by the Amazon Web Services account that called this method.</p> </li> <li> <p> <code>ListRepositoriesInDomain</code>: Returns a list of the repositories in a domain.</p> </li> <li> <p> <code>PublishPackageVersion</code>: Creates a new package version containing one or more assets.</p> </li> <li> <p> <code>PutDomainPermissionsPolicy</code>: Attaches a resource policy to a domain.</p> </li> <li> <p> <code>PutPackageOriginConfiguration</code>: Sets the package origin configuration for a package, which determine how new versions of the package can be added to a specific repository.</p> </li> <li> <p> <code>PutRepositoryPermissionsPolicy</code>: Sets the resource policy on a repository that specifies permissions to access it. </p> </li> <li> <p> <code>UpdatePackageVersionsStatus</code>: Updates the status of one or more versions of a package.</p> </li> <li> <p> <code>UpdateRepository</code>: Updates the properties of a repository.</p> </li> </ul>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2018-09-22</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2018-09-22"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2018-09-22.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
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

## Documentation for API Endpoints

All URIs are relative to *http://codeartifact.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**associateExternalConnection**](docs/DefaultApi.md#associateExternalConnection) | **POST** /v1/repository/external-connection#domain&amp;repository&amp;external-connection | 
*DefaultApi* | [**copyPackageVersions**](docs/DefaultApi.md#copyPackageVersions) | **POST** /v1/package/versions/copy#domain&amp;source-repository&amp;destination-repository&amp;format&amp;package | 
*DefaultApi* | [**createDomain**](docs/DefaultApi.md#createDomain) | **POST** /v1/domain#domain | 
*DefaultApi* | [**createRepository**](docs/DefaultApi.md#createRepository) | **POST** /v1/repository#domain&amp;repository | 
*DefaultApi* | [**deleteDomain**](docs/DefaultApi.md#deleteDomain) | **DELETE** /v1/domain#domain | 
*DefaultApi* | [**deleteDomainPermissionsPolicy**](docs/DefaultApi.md#deleteDomainPermissionsPolicy) | **DELETE** /v1/domain/permissions/policy#domain | 
*DefaultApi* | [**deletePackage**](docs/DefaultApi.md#deletePackage) | **DELETE** /v1/package#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**deletePackageVersions**](docs/DefaultApi.md#deletePackageVersions) | **POST** /v1/package/versions/delete#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**deleteRepository**](docs/DefaultApi.md#deleteRepository) | **DELETE** /v1/repository#domain&amp;repository | 
*DefaultApi* | [**deleteRepositoryPermissionsPolicy**](docs/DefaultApi.md#deleteRepositoryPermissionsPolicy) | **DELETE** /v1/repository/permissions/policies#domain&amp;repository | 
*DefaultApi* | [**describeDomain**](docs/DefaultApi.md#describeDomain) | **GET** /v1/domain#domain | 
*DefaultApi* | [**describePackage**](docs/DefaultApi.md#describePackage) | **GET** /v1/package#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**describePackageVersion**](docs/DefaultApi.md#describePackageVersion) | **GET** /v1/package/version#domain&amp;repository&amp;format&amp;package&amp;version | 
*DefaultApi* | [**describeRepository**](docs/DefaultApi.md#describeRepository) | **GET** /v1/repository#domain&amp;repository | 
*DefaultApi* | [**disassociateExternalConnection**](docs/DefaultApi.md#disassociateExternalConnection) | **DELETE** /v1/repository/external-connection#domain&amp;repository&amp;external-connection | 
*DefaultApi* | [**disposePackageVersions**](docs/DefaultApi.md#disposePackageVersions) | **POST** /v1/package/versions/dispose#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**getAuthorizationToken**](docs/DefaultApi.md#getAuthorizationToken) | **POST** /v1/authorization-token#domain | 
*DefaultApi* | [**getDomainPermissionsPolicy**](docs/DefaultApi.md#getDomainPermissionsPolicy) | **GET** /v1/domain/permissions/policy#domain | 
*DefaultApi* | [**getPackageVersionAsset**](docs/DefaultApi.md#getPackageVersionAsset) | **GET** /v1/package/version/asset#domain&amp;repository&amp;format&amp;package&amp;version&amp;asset | 
*DefaultApi* | [**getPackageVersionReadme**](docs/DefaultApi.md#getPackageVersionReadme) | **GET** /v1/package/version/readme#domain&amp;repository&amp;format&amp;package&amp;version | 
*DefaultApi* | [**getRepositoryEndpoint**](docs/DefaultApi.md#getRepositoryEndpoint) | **GET** /v1/repository/endpoint#domain&amp;repository&amp;format | 
*DefaultApi* | [**getRepositoryPermissionsPolicy**](docs/DefaultApi.md#getRepositoryPermissionsPolicy) | **GET** /v1/repository/permissions/policy#domain&amp;repository | 
*DefaultApi* | [**listDomains**](docs/DefaultApi.md#listDomains) | **POST** /v1/domains | 
*DefaultApi* | [**listPackageVersionAssets**](docs/DefaultApi.md#listPackageVersionAssets) | **POST** /v1/package/version/assets#domain&amp;repository&amp;format&amp;package&amp;version | 
*DefaultApi* | [**listPackageVersionDependencies**](docs/DefaultApi.md#listPackageVersionDependencies) | **POST** /v1/package/version/dependencies#domain&amp;repository&amp;format&amp;package&amp;version | 
*DefaultApi* | [**listPackageVersions**](docs/DefaultApi.md#listPackageVersions) | **POST** /v1/package/versions#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**listPackages**](docs/DefaultApi.md#listPackages) | **POST** /v1/packages#domain&amp;repository | 
*DefaultApi* | [**listRepositories**](docs/DefaultApi.md#listRepositories) | **POST** /v1/repositories | 
*DefaultApi* | [**listRepositoriesInDomain**](docs/DefaultApi.md#listRepositoriesInDomain) | **POST** /v1/domain/repositories#domain | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /v1/tags#resourceArn | 
*DefaultApi* | [**publishPackageVersion**](docs/DefaultApi.md#publishPackageVersion) | **POST** /v1/package/version/publish#domain&amp;repository&amp;format&amp;package&amp;version&amp;asset&amp;x-amz-content-sha256 | 
*DefaultApi* | [**putDomainPermissionsPolicy**](docs/DefaultApi.md#putDomainPermissionsPolicy) | **PUT** /v1/domain/permissions/policy | 
*DefaultApi* | [**putPackageOriginConfiguration**](docs/DefaultApi.md#putPackageOriginConfiguration) | **POST** /v1/package#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**putRepositoryPermissionsPolicy**](docs/DefaultApi.md#putRepositoryPermissionsPolicy) | **PUT** /v1/repository/permissions/policy#domain&amp;repository | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /v1/tag#resourceArn | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /v1/untag#resourceArn | 
*DefaultApi* | [**updatePackageVersionsStatus**](docs/DefaultApi.md#updatePackageVersionsStatus) | **POST** /v1/package/versions/update_status#domain&amp;repository&amp;format&amp;package | 
*DefaultApi* | [**updateRepository**](docs/DefaultApi.md#updateRepository) | **PUT** /v1/repository#domain&amp;repository | 


## Documentation for Models

 - [AllowPublish](docs/AllowPublish.md)
 - [AllowUpstream](docs/AllowUpstream.md)
 - [AssetSummary](docs/AssetSummary.md)
 - [AssociateExternalConnectionResult](docs/AssociateExternalConnectionResult.md)
 - [AssociateExternalConnectionResultRepository](docs/AssociateExternalConnectionResultRepository.md)
 - [CopyPackageVersionsRequest](docs/CopyPackageVersionsRequest.md)
 - [CopyPackageVersionsResult](docs/CopyPackageVersionsResult.md)
 - [CreateDomainRequest](docs/CreateDomainRequest.md)
 - [CreateDomainResult](docs/CreateDomainResult.md)
 - [CreateDomainResultDomain](docs/CreateDomainResultDomain.md)
 - [CreateRepositoryRequest](docs/CreateRepositoryRequest.md)
 - [CreateRepositoryResult](docs/CreateRepositoryResult.md)
 - [CreateRepositoryResultRepository](docs/CreateRepositoryResultRepository.md)
 - [DeleteDomainPermissionsPolicyResult](docs/DeleteDomainPermissionsPolicyResult.md)
 - [DeleteDomainPermissionsPolicyResultPolicy](docs/DeleteDomainPermissionsPolicyResultPolicy.md)
 - [DeleteDomainResult](docs/DeleteDomainResult.md)
 - [DeleteDomainResultDomain](docs/DeleteDomainResultDomain.md)
 - [DeletePackageResult](docs/DeletePackageResult.md)
 - [DeletePackageVersionsRequest](docs/DeletePackageVersionsRequest.md)
 - [DeletePackageVersionsResult](docs/DeletePackageVersionsResult.md)
 - [DeleteRepositoryPermissionsPolicyResult](docs/DeleteRepositoryPermissionsPolicyResult.md)
 - [DeleteRepositoryPermissionsPolicyResultPolicy](docs/DeleteRepositoryPermissionsPolicyResultPolicy.md)
 - [DeleteRepositoryResult](docs/DeleteRepositoryResult.md)
 - [DeleteRepositoryResultRepository](docs/DeleteRepositoryResultRepository.md)
 - [DescribeDomainResult](docs/DescribeDomainResult.md)
 - [DescribePackageResult](docs/DescribePackageResult.md)
 - [DescribePackageResultPackage](docs/DescribePackageResultPackage.md)
 - [DescribePackageVersionResult](docs/DescribePackageVersionResult.md)
 - [DescribePackageVersionResultPackageVersion](docs/DescribePackageVersionResultPackageVersion.md)
 - [DescribeRepositoryResult](docs/DescribeRepositoryResult.md)
 - [DescribeRepositoryResultRepository](docs/DescribeRepositoryResultRepository.md)
 - [DisassociateExternalConnectionResult](docs/DisassociateExternalConnectionResult.md)
 - [DisassociateExternalConnectionResultRepository](docs/DisassociateExternalConnectionResultRepository.md)
 - [DisposePackageVersionsRequest](docs/DisposePackageVersionsRequest.md)
 - [DisposePackageVersionsResult](docs/DisposePackageVersionsResult.md)
 - [DomainDescription](docs/DomainDescription.md)
 - [DomainEntryPoint](docs/DomainEntryPoint.md)
 - [DomainStatus](docs/DomainStatus.md)
 - [DomainSummary](docs/DomainSummary.md)
 - [ExternalConnectionStatus](docs/ExternalConnectionStatus.md)
 - [GetAuthorizationTokenResult](docs/GetAuthorizationTokenResult.md)
 - [GetDomainPermissionsPolicyResult](docs/GetDomainPermissionsPolicyResult.md)
 - [GetDomainPermissionsPolicyResultPolicy](docs/GetDomainPermissionsPolicyResultPolicy.md)
 - [GetPackageVersionAssetResult](docs/GetPackageVersionAssetResult.md)
 - [GetPackageVersionReadmeResult](docs/GetPackageVersionReadmeResult.md)
 - [GetRepositoryEndpointResult](docs/GetRepositoryEndpointResult.md)
 - [GetRepositoryPermissionsPolicyResult](docs/GetRepositoryPermissionsPolicyResult.md)
 - [HashAlgorithm](docs/HashAlgorithm.md)
 - [LicenseInfo](docs/LicenseInfo.md)
 - [ListDomainsRequest](docs/ListDomainsRequest.md)
 - [ListDomainsResult](docs/ListDomainsResult.md)
 - [ListPackageVersionAssetsResult](docs/ListPackageVersionAssetsResult.md)
 - [ListPackageVersionDependenciesResult](docs/ListPackageVersionDependenciesResult.md)
 - [ListPackageVersionsResult](docs/ListPackageVersionsResult.md)
 - [ListPackagesResult](docs/ListPackagesResult.md)
 - [ListRepositoriesInDomainResult](docs/ListRepositoriesInDomainResult.md)
 - [ListRepositoriesResult](docs/ListRepositoriesResult.md)
 - [ListTagsForResourceResult](docs/ListTagsForResourceResult.md)
 - [PackageDependency](docs/PackageDependency.md)
 - [PackageDescription](docs/PackageDescription.md)
 - [PackageDescriptionOriginConfiguration](docs/PackageDescriptionOriginConfiguration.md)
 - [PackageFormat](docs/PackageFormat.md)
 - [PackageOriginConfiguration](docs/PackageOriginConfiguration.md)
 - [PackageOriginConfigurationRestrictions](docs/PackageOriginConfigurationRestrictions.md)
 - [PackageOriginRestrictions](docs/PackageOriginRestrictions.md)
 - [PackageSummary](docs/PackageSummary.md)
 - [PackageSummaryOriginConfiguration](docs/PackageSummaryOriginConfiguration.md)
 - [PackageVersionDescription](docs/PackageVersionDescription.md)
 - [PackageVersionDescriptionOrigin](docs/PackageVersionDescriptionOrigin.md)
 - [PackageVersionError](docs/PackageVersionError.md)
 - [PackageVersionErrorCode](docs/PackageVersionErrorCode.md)
 - [PackageVersionOrigin](docs/PackageVersionOrigin.md)
 - [PackageVersionOriginDomainEntryPoint](docs/PackageVersionOriginDomainEntryPoint.md)
 - [PackageVersionOriginType](docs/PackageVersionOriginType.md)
 - [PackageVersionSortType](docs/PackageVersionSortType.md)
 - [PackageVersionStatus](docs/PackageVersionStatus.md)
 - [PackageVersionSummary](docs/PackageVersionSummary.md)
 - [PublishPackageVersionRequest](docs/PublishPackageVersionRequest.md)
 - [PublishPackageVersionResult](docs/PublishPackageVersionResult.md)
 - [PublishPackageVersionResultAsset](docs/PublishPackageVersionResultAsset.md)
 - [PutDomainPermissionsPolicyRequest](docs/PutDomainPermissionsPolicyRequest.md)
 - [PutDomainPermissionsPolicyResult](docs/PutDomainPermissionsPolicyResult.md)
 - [PutDomainPermissionsPolicyResultPolicy](docs/PutDomainPermissionsPolicyResultPolicy.md)
 - [PutPackageOriginConfigurationRequest](docs/PutPackageOriginConfigurationRequest.md)
 - [PutPackageOriginConfigurationRequestRestrictions](docs/PutPackageOriginConfigurationRequestRestrictions.md)
 - [PutPackageOriginConfigurationResult](docs/PutPackageOriginConfigurationResult.md)
 - [PutPackageOriginConfigurationResultOriginConfiguration](docs/PutPackageOriginConfigurationResultOriginConfiguration.md)
 - [PutRepositoryPermissionsPolicyRequest](docs/PutRepositoryPermissionsPolicyRequest.md)
 - [PutRepositoryPermissionsPolicyResult](docs/PutRepositoryPermissionsPolicyResult.md)
 - [RepositoryDescription](docs/RepositoryDescription.md)
 - [RepositoryExternalConnectionInfo](docs/RepositoryExternalConnectionInfo.md)
 - [RepositorySummary](docs/RepositorySummary.md)
 - [ResourcePolicy](docs/ResourcePolicy.md)
 - [SuccessfulPackageVersionInfo](docs/SuccessfulPackageVersionInfo.md)
 - [Tag](docs/Tag.md)
 - [TagResourceRequest](docs/TagResourceRequest.md)
 - [UntagResourceRequest](docs/UntagResourceRequest.md)
 - [UpdatePackageVersionsStatusRequest](docs/UpdatePackageVersionsStatusRequest.md)
 - [UpdatePackageVersionsStatusResult](docs/UpdatePackageVersionsStatusResult.md)
 - [UpdateRepositoryRequest](docs/UpdateRepositoryRequest.md)
 - [UpdateRepositoryResult](docs/UpdateRepositoryResult.md)
 - [UpdateRepositoryResultRepository](docs/UpdateRepositoryResultRepository.md)
 - [UpstreamRepository](docs/UpstreamRepository.md)
 - [UpstreamRepositoryInfo](docs/UpstreamRepositoryInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="hmac"></a>
### hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

mike.ralphson@gmail.com

