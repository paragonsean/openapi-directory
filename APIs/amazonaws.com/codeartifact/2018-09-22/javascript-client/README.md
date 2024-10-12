# code_artifact

CodeArtifact - JavaScript client for code_artifact
<p> CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. </p> <p> <b>CodeArtifact Components</b> </p> <p>Use the information in this guide to help you work with the following CodeArtifact components:</p> <ul> <li> <p> <b>Repository</b>: A CodeArtifact repository contains a set of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\">package versions</a>, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <b> <code>npm</code> </b> CLI, the Maven CLI (<b> <code>mvn</code> </b>), Python CLIs (<b> <code>pip</code> </b> and <code>twine</code>), and NuGet CLIs (<code>nuget</code> and <code>dotnet</code>).</p> </li> <li> <p> <b>Domain</b>: Repositories are aggregated into a higher-level entity known as a <i>domain</i>. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it's present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in Key Management Service (KMS).</p> <p>Each repository is a member of a single domain and can't be moved to a different domain.</p> <p>The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.</p> <p>Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.</p> </li> <li> <p> <b>Package</b>: A <i>package</i> is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\">npm</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\">PyPI</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\">Maven</a>, and <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget\">NuGet</a> package formats.</p> <p>In CodeArtifact, a package consists of:</p> <ul> <li> <p>A <i>name</i> (for example, <code>webpack</code> is the name of a popular npm package)</p> </li> <li> <p>An optional namespace (for example, <code>@types</code> in <code>@types/node</code>)</p> </li> <li> <p>A set of versions (for example, <code>1.0.0</code>, <code>1.0.1</code>, <code>1.0.2</code>, etc.)</p> </li> <li> <p> Package-level metadata (for example, npm tags)</p> </li> </ul> </li> <li> <p> <b>Package version</b>: A version of a package, such as <code>@types/node 12.6.9</code>. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the <a href=\"https://semver.org/\">Semantic Versioning specification</a>. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.</p> </li> <li> <p> <b>Upstream repository</b>: One repository is <i>upstream</i> of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.</p> </li> <li> <p> <b>Asset</b>: An individual file stored in CodeArtifact associated with a package version, such as an npm <code>.tgz</code> file or Maven POM and JAR files.</p> </li> </ul> <p>CodeArtifact supports these operations:</p> <ul> <li> <p> <code>AssociateExternalConnection</code>: Adds an existing external connection to a repository. </p> </li> <li> <p> <code>CopyPackageVersions</code>: Copies package versions from one repository to another repository in the same domain.</p> </li> <li> <p> <code>CreateDomain</code>: Creates a domain</p> </li> <li> <p> <code>CreateRepository</code>: Creates a CodeArtifact repository in a domain. </p> </li> <li> <p> <code>DeleteDomain</code>: Deletes a domain. You cannot delete a domain that contains repositories. </p> </li> <li> <p> <code>DeleteDomainPermissionsPolicy</code>: Deletes the resource policy that is set on a domain.</p> </li> <li> <p> <code>DeletePackage</code>: Deletes a package and all associated package versions.</p> </li> <li> <p> <code>DeletePackageVersions</code>: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DeleteRepository</code>: Deletes a repository. </p> </li> <li> <p> <code>DeleteRepositoryPermissionsPolicy</code>: Deletes the resource policy that is set on a repository.</p> </li> <li> <p> <code>DescribeDomain</code>: Returns a <code>DomainDescription</code> object that contains information about the requested domain.</p> </li> <li> <p> <code>DescribePackage</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains details about a package. </p> </li> <li> <p> <code>DescribePackageVersion</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains details about a package version. </p> </li> <li> <p> <code>DescribeRepository</code>: Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p> </li> <li> <p> <code>DisposePackageVersions</code>: Disposes versions of a package. A package version with the status <code>Disposed</code> cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DisassociateExternalConnection</code>: Removes an existing external connection from a repository. </p> </li> <li> <p> <code>GetAuthorizationToken</code>: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.</p> </li> <li> <p> <code>GetDomainPermissionsPolicy</code>: Returns the policy of a resource that is attached to the specified domain. </p> </li> <li> <p> <code>GetPackageVersionAsset</code>: Returns the contents of an asset that is in a package version. </p> </li> <li> <p> <code>GetPackageVersionReadme</code>: Gets the readme file or descriptive text for a package version.</p> </li> <li> <p> <code>GetRepositoryEndpoint</code>: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> </ul> </li> <li> <p> <code>GetRepositoryPermissionsPolicy</code>: Returns the resource policy that is set on a repository. </p> </li> <li> <p> <code>ListDomains</code>: Returns a list of <code>DomainSummary</code> objects. Each returned <code>DomainSummary</code> object contains information about a domain.</p> </li> <li> <p> <code>ListPackages</code>: Lists the packages in a repository.</p> </li> <li> <p> <code>ListPackageVersionAssets</code>: Lists the assets for a given package version.</p> </li> <li> <p> <code>ListPackageVersionDependencies</code>: Returns a list of the direct dependencies for a package version. </p> </li> <li> <p> <code>ListPackageVersions</code>: Returns a list of package versions for a specified package in a repository.</p> </li> <li> <p> <code>ListRepositories</code>: Returns a list of repositories owned by the Amazon Web Services account that called this method.</p> </li> <li> <p> <code>ListRepositoriesInDomain</code>: Returns a list of the repositories in a domain.</p> </li> <li> <p> <code>PublishPackageVersion</code>: Creates a new package version containing one or more assets.</p> </li> <li> <p> <code>PutDomainPermissionsPolicy</code>: Attaches a resource policy to a domain.</p> </li> <li> <p> <code>PutPackageOriginConfiguration</code>: Sets the package origin configuration for a package, which determine how new versions of the package can be added to a specific repository.</p> </li> <li> <p> <code>PutRepositoryPermissionsPolicy</code>: Sets the resource policy on a repository that specifies permissions to access it. </p> </li> <li> <p> <code>UpdatePackageVersionsStatus</code>: Updates the status of one or more versions of a package.</p> </li> <li> <p> <code>UpdateRepository</code>: Updates the properties of a repository.</p> </li> </ul>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2018-09-22
- Package version: 2018-09-22
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install code_artifact --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your code_artifact from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CodeArtifact = require('code_artifact');

var defaultClient = CodeArtifact.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new CodeArtifact.DefaultApi()
var domain = "domain_example"; // {String} The name of the domain that contains the repository.
var repository = "repository_example"; // {String}  The name of the repository to which the external connection is added. 
var externalConnection = "externalConnection_example"; // {String} <p> The name of the external connection to add to the repository. The following values are supported: </p> <ul> <li> <p> <code>public:npmjs</code> - for the npm public repository. </p> </li> <li> <p> <code>public:nuget-org</code> - for the NuGet Gallery. </p> </li> <li> <p> <code>public:pypi</code> - for the Python Package Index. </p> </li> <li> <p> <code>public:maven-central</code> - for Maven Central. </p> </li> <li> <p> <code>public:maven-googleandroid</code> - for the Google Android repository. </p> </li> <li> <p> <code>public:maven-gradleplugins</code> - for the Gradle plugins repository. </p> </li> <li> <p> <code>public:maven-commonsware</code> - for the CommonsWare Android repository. </p> </li> <li> <p> <code>public:maven-clojars</code> - for the Clojars repository. </p> </li> </ul>
var opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // {String} 
  'xAmzDate': "xAmzDate_example", // {String} 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // {String} 
  'xAmzCredential': "xAmzCredential_example", // {String} 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // {String} 
  'xAmzSignature': "xAmzSignature_example", // {String} 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // {String} 
  'domainOwner': "domainOwner_example" // {String}  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.associateExternalConnection(domain, repository, externalConnection, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://codeartifact.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CodeArtifact.DefaultApi* | [**associateExternalConnection**](docs/DefaultApi.md#associateExternalConnection) | **POST** /v1/repository/external-connection#domain&amp;repository&amp;external-connection | 
*CodeArtifact.DefaultApi* | [**copyPackageVersions**](docs/DefaultApi.md#copyPackageVersions) | **POST** /v1/package/versions/copy#domain&amp;source-repository&amp;destination-repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**createDomain**](docs/DefaultApi.md#createDomain) | **POST** /v1/domain#domain | 
*CodeArtifact.DefaultApi* | [**createRepository**](docs/DefaultApi.md#createRepository) | **POST** /v1/repository#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**deleteDomain**](docs/DefaultApi.md#deleteDomain) | **DELETE** /v1/domain#domain | 
*CodeArtifact.DefaultApi* | [**deleteDomainPermissionsPolicy**](docs/DefaultApi.md#deleteDomainPermissionsPolicy) | **DELETE** /v1/domain/permissions/policy#domain | 
*CodeArtifact.DefaultApi* | [**deletePackage**](docs/DefaultApi.md#deletePackage) | **DELETE** /v1/package#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**deletePackageVersions**](docs/DefaultApi.md#deletePackageVersions) | **POST** /v1/package/versions/delete#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**deleteRepository**](docs/DefaultApi.md#deleteRepository) | **DELETE** /v1/repository#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**deleteRepositoryPermissionsPolicy**](docs/DefaultApi.md#deleteRepositoryPermissionsPolicy) | **DELETE** /v1/repository/permissions/policies#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**describeDomain**](docs/DefaultApi.md#describeDomain) | **GET** /v1/domain#domain | 
*CodeArtifact.DefaultApi* | [**describePackage**](docs/DefaultApi.md#describePackage) | **GET** /v1/package#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**describePackageVersion**](docs/DefaultApi.md#describePackageVersion) | **GET** /v1/package/version#domain&amp;repository&amp;format&amp;package&amp;version | 
*CodeArtifact.DefaultApi* | [**describeRepository**](docs/DefaultApi.md#describeRepository) | **GET** /v1/repository#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**disassociateExternalConnection**](docs/DefaultApi.md#disassociateExternalConnection) | **DELETE** /v1/repository/external-connection#domain&amp;repository&amp;external-connection | 
*CodeArtifact.DefaultApi* | [**disposePackageVersions**](docs/DefaultApi.md#disposePackageVersions) | **POST** /v1/package/versions/dispose#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**getAuthorizationToken**](docs/DefaultApi.md#getAuthorizationToken) | **POST** /v1/authorization-token#domain | 
*CodeArtifact.DefaultApi* | [**getDomainPermissionsPolicy**](docs/DefaultApi.md#getDomainPermissionsPolicy) | **GET** /v1/domain/permissions/policy#domain | 
*CodeArtifact.DefaultApi* | [**getPackageVersionAsset**](docs/DefaultApi.md#getPackageVersionAsset) | **GET** /v1/package/version/asset#domain&amp;repository&amp;format&amp;package&amp;version&amp;asset | 
*CodeArtifact.DefaultApi* | [**getPackageVersionReadme**](docs/DefaultApi.md#getPackageVersionReadme) | **GET** /v1/package/version/readme#domain&amp;repository&amp;format&amp;package&amp;version | 
*CodeArtifact.DefaultApi* | [**getRepositoryEndpoint**](docs/DefaultApi.md#getRepositoryEndpoint) | **GET** /v1/repository/endpoint#domain&amp;repository&amp;format | 
*CodeArtifact.DefaultApi* | [**getRepositoryPermissionsPolicy**](docs/DefaultApi.md#getRepositoryPermissionsPolicy) | **GET** /v1/repository/permissions/policy#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**listDomains**](docs/DefaultApi.md#listDomains) | **POST** /v1/domains | 
*CodeArtifact.DefaultApi* | [**listPackageVersionAssets**](docs/DefaultApi.md#listPackageVersionAssets) | **POST** /v1/package/version/assets#domain&amp;repository&amp;format&amp;package&amp;version | 
*CodeArtifact.DefaultApi* | [**listPackageVersionDependencies**](docs/DefaultApi.md#listPackageVersionDependencies) | **POST** /v1/package/version/dependencies#domain&amp;repository&amp;format&amp;package&amp;version | 
*CodeArtifact.DefaultApi* | [**listPackageVersions**](docs/DefaultApi.md#listPackageVersions) | **POST** /v1/package/versions#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**listPackages**](docs/DefaultApi.md#listPackages) | **POST** /v1/packages#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**listRepositories**](docs/DefaultApi.md#listRepositories) | **POST** /v1/repositories | 
*CodeArtifact.DefaultApi* | [**listRepositoriesInDomain**](docs/DefaultApi.md#listRepositoriesInDomain) | **POST** /v1/domain/repositories#domain | 
*CodeArtifact.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /v1/tags#resourceArn | 
*CodeArtifact.DefaultApi* | [**publishPackageVersion**](docs/DefaultApi.md#publishPackageVersion) | **POST** /v1/package/version/publish#domain&amp;repository&amp;format&amp;package&amp;version&amp;asset&amp;x-amz-content-sha256 | 
*CodeArtifact.DefaultApi* | [**putDomainPermissionsPolicy**](docs/DefaultApi.md#putDomainPermissionsPolicy) | **PUT** /v1/domain/permissions/policy | 
*CodeArtifact.DefaultApi* | [**putPackageOriginConfiguration**](docs/DefaultApi.md#putPackageOriginConfiguration) | **POST** /v1/package#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**putRepositoryPermissionsPolicy**](docs/DefaultApi.md#putRepositoryPermissionsPolicy) | **PUT** /v1/repository/permissions/policy#domain&amp;repository | 
*CodeArtifact.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /v1/tag#resourceArn | 
*CodeArtifact.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /v1/untag#resourceArn | 
*CodeArtifact.DefaultApi* | [**updatePackageVersionsStatus**](docs/DefaultApi.md#updatePackageVersionsStatus) | **POST** /v1/package/versions/update_status#domain&amp;repository&amp;format&amp;package | 
*CodeArtifact.DefaultApi* | [**updateRepository**](docs/DefaultApi.md#updateRepository) | **PUT** /v1/repository#domain&amp;repository | 


## Documentation for Models

 - [CodeArtifact.AllowPublish](docs/AllowPublish.md)
 - [CodeArtifact.AllowUpstream](docs/AllowUpstream.md)
 - [CodeArtifact.AssetSummary](docs/AssetSummary.md)
 - [CodeArtifact.AssociateExternalConnectionResult](docs/AssociateExternalConnectionResult.md)
 - [CodeArtifact.AssociateExternalConnectionResultRepository](docs/AssociateExternalConnectionResultRepository.md)
 - [CodeArtifact.CopyPackageVersionsRequest](docs/CopyPackageVersionsRequest.md)
 - [CodeArtifact.CopyPackageVersionsResult](docs/CopyPackageVersionsResult.md)
 - [CodeArtifact.CreateDomainRequest](docs/CreateDomainRequest.md)
 - [CodeArtifact.CreateDomainResult](docs/CreateDomainResult.md)
 - [CodeArtifact.CreateDomainResultDomain](docs/CreateDomainResultDomain.md)
 - [CodeArtifact.CreateRepositoryRequest](docs/CreateRepositoryRequest.md)
 - [CodeArtifact.CreateRepositoryResult](docs/CreateRepositoryResult.md)
 - [CodeArtifact.CreateRepositoryResultRepository](docs/CreateRepositoryResultRepository.md)
 - [CodeArtifact.DeleteDomainPermissionsPolicyResult](docs/DeleteDomainPermissionsPolicyResult.md)
 - [CodeArtifact.DeleteDomainPermissionsPolicyResultPolicy](docs/DeleteDomainPermissionsPolicyResultPolicy.md)
 - [CodeArtifact.DeleteDomainResult](docs/DeleteDomainResult.md)
 - [CodeArtifact.DeleteDomainResultDomain](docs/DeleteDomainResultDomain.md)
 - [CodeArtifact.DeletePackageResult](docs/DeletePackageResult.md)
 - [CodeArtifact.DeletePackageVersionsRequest](docs/DeletePackageVersionsRequest.md)
 - [CodeArtifact.DeletePackageVersionsResult](docs/DeletePackageVersionsResult.md)
 - [CodeArtifact.DeleteRepositoryPermissionsPolicyResult](docs/DeleteRepositoryPermissionsPolicyResult.md)
 - [CodeArtifact.DeleteRepositoryPermissionsPolicyResultPolicy](docs/DeleteRepositoryPermissionsPolicyResultPolicy.md)
 - [CodeArtifact.DeleteRepositoryResult](docs/DeleteRepositoryResult.md)
 - [CodeArtifact.DeleteRepositoryResultRepository](docs/DeleteRepositoryResultRepository.md)
 - [CodeArtifact.DescribeDomainResult](docs/DescribeDomainResult.md)
 - [CodeArtifact.DescribePackageResult](docs/DescribePackageResult.md)
 - [CodeArtifact.DescribePackageResultPackage](docs/DescribePackageResultPackage.md)
 - [CodeArtifact.DescribePackageVersionResult](docs/DescribePackageVersionResult.md)
 - [CodeArtifact.DescribePackageVersionResultPackageVersion](docs/DescribePackageVersionResultPackageVersion.md)
 - [CodeArtifact.DescribeRepositoryResult](docs/DescribeRepositoryResult.md)
 - [CodeArtifact.DescribeRepositoryResultRepository](docs/DescribeRepositoryResultRepository.md)
 - [CodeArtifact.DisassociateExternalConnectionResult](docs/DisassociateExternalConnectionResult.md)
 - [CodeArtifact.DisassociateExternalConnectionResultRepository](docs/DisassociateExternalConnectionResultRepository.md)
 - [CodeArtifact.DisposePackageVersionsRequest](docs/DisposePackageVersionsRequest.md)
 - [CodeArtifact.DisposePackageVersionsResult](docs/DisposePackageVersionsResult.md)
 - [CodeArtifact.DomainDescription](docs/DomainDescription.md)
 - [CodeArtifact.DomainEntryPoint](docs/DomainEntryPoint.md)
 - [CodeArtifact.DomainStatus](docs/DomainStatus.md)
 - [CodeArtifact.DomainSummary](docs/DomainSummary.md)
 - [CodeArtifact.ExternalConnectionStatus](docs/ExternalConnectionStatus.md)
 - [CodeArtifact.GetAuthorizationTokenResult](docs/GetAuthorizationTokenResult.md)
 - [CodeArtifact.GetDomainPermissionsPolicyResult](docs/GetDomainPermissionsPolicyResult.md)
 - [CodeArtifact.GetDomainPermissionsPolicyResultPolicy](docs/GetDomainPermissionsPolicyResultPolicy.md)
 - [CodeArtifact.GetPackageVersionAssetResult](docs/GetPackageVersionAssetResult.md)
 - [CodeArtifact.GetPackageVersionReadmeResult](docs/GetPackageVersionReadmeResult.md)
 - [CodeArtifact.GetRepositoryEndpointResult](docs/GetRepositoryEndpointResult.md)
 - [CodeArtifact.GetRepositoryPermissionsPolicyResult](docs/GetRepositoryPermissionsPolicyResult.md)
 - [CodeArtifact.HashAlgorithm](docs/HashAlgorithm.md)
 - [CodeArtifact.LicenseInfo](docs/LicenseInfo.md)
 - [CodeArtifact.ListDomainsRequest](docs/ListDomainsRequest.md)
 - [CodeArtifact.ListDomainsResult](docs/ListDomainsResult.md)
 - [CodeArtifact.ListPackageVersionAssetsResult](docs/ListPackageVersionAssetsResult.md)
 - [CodeArtifact.ListPackageVersionDependenciesResult](docs/ListPackageVersionDependenciesResult.md)
 - [CodeArtifact.ListPackageVersionsResult](docs/ListPackageVersionsResult.md)
 - [CodeArtifact.ListPackagesResult](docs/ListPackagesResult.md)
 - [CodeArtifact.ListRepositoriesInDomainResult](docs/ListRepositoriesInDomainResult.md)
 - [CodeArtifact.ListRepositoriesResult](docs/ListRepositoriesResult.md)
 - [CodeArtifact.ListTagsForResourceResult](docs/ListTagsForResourceResult.md)
 - [CodeArtifact.PackageDependency](docs/PackageDependency.md)
 - [CodeArtifact.PackageDescription](docs/PackageDescription.md)
 - [CodeArtifact.PackageDescriptionOriginConfiguration](docs/PackageDescriptionOriginConfiguration.md)
 - [CodeArtifact.PackageFormat](docs/PackageFormat.md)
 - [CodeArtifact.PackageOriginConfiguration](docs/PackageOriginConfiguration.md)
 - [CodeArtifact.PackageOriginConfigurationRestrictions](docs/PackageOriginConfigurationRestrictions.md)
 - [CodeArtifact.PackageOriginRestrictions](docs/PackageOriginRestrictions.md)
 - [CodeArtifact.PackageSummary](docs/PackageSummary.md)
 - [CodeArtifact.PackageSummaryOriginConfiguration](docs/PackageSummaryOriginConfiguration.md)
 - [CodeArtifact.PackageVersionDescription](docs/PackageVersionDescription.md)
 - [CodeArtifact.PackageVersionDescriptionOrigin](docs/PackageVersionDescriptionOrigin.md)
 - [CodeArtifact.PackageVersionError](docs/PackageVersionError.md)
 - [CodeArtifact.PackageVersionErrorCode](docs/PackageVersionErrorCode.md)
 - [CodeArtifact.PackageVersionOrigin](docs/PackageVersionOrigin.md)
 - [CodeArtifact.PackageVersionOriginDomainEntryPoint](docs/PackageVersionOriginDomainEntryPoint.md)
 - [CodeArtifact.PackageVersionOriginType](docs/PackageVersionOriginType.md)
 - [CodeArtifact.PackageVersionSortType](docs/PackageVersionSortType.md)
 - [CodeArtifact.PackageVersionStatus](docs/PackageVersionStatus.md)
 - [CodeArtifact.PackageVersionSummary](docs/PackageVersionSummary.md)
 - [CodeArtifact.PublishPackageVersionRequest](docs/PublishPackageVersionRequest.md)
 - [CodeArtifact.PublishPackageVersionResult](docs/PublishPackageVersionResult.md)
 - [CodeArtifact.PublishPackageVersionResultAsset](docs/PublishPackageVersionResultAsset.md)
 - [CodeArtifact.PutDomainPermissionsPolicyRequest](docs/PutDomainPermissionsPolicyRequest.md)
 - [CodeArtifact.PutDomainPermissionsPolicyResult](docs/PutDomainPermissionsPolicyResult.md)
 - [CodeArtifact.PutDomainPermissionsPolicyResultPolicy](docs/PutDomainPermissionsPolicyResultPolicy.md)
 - [CodeArtifact.PutPackageOriginConfigurationRequest](docs/PutPackageOriginConfigurationRequest.md)
 - [CodeArtifact.PutPackageOriginConfigurationRequestRestrictions](docs/PutPackageOriginConfigurationRequestRestrictions.md)
 - [CodeArtifact.PutPackageOriginConfigurationResult](docs/PutPackageOriginConfigurationResult.md)
 - [CodeArtifact.PutPackageOriginConfigurationResultOriginConfiguration](docs/PutPackageOriginConfigurationResultOriginConfiguration.md)
 - [CodeArtifact.PutRepositoryPermissionsPolicyRequest](docs/PutRepositoryPermissionsPolicyRequest.md)
 - [CodeArtifact.PutRepositoryPermissionsPolicyResult](docs/PutRepositoryPermissionsPolicyResult.md)
 - [CodeArtifact.RepositoryDescription](docs/RepositoryDescription.md)
 - [CodeArtifact.RepositoryExternalConnectionInfo](docs/RepositoryExternalConnectionInfo.md)
 - [CodeArtifact.RepositorySummary](docs/RepositorySummary.md)
 - [CodeArtifact.ResourcePolicy](docs/ResourcePolicy.md)
 - [CodeArtifact.SuccessfulPackageVersionInfo](docs/SuccessfulPackageVersionInfo.md)
 - [CodeArtifact.Tag](docs/Tag.md)
 - [CodeArtifact.TagResourceRequest](docs/TagResourceRequest.md)
 - [CodeArtifact.UntagResourceRequest](docs/UntagResourceRequest.md)
 - [CodeArtifact.UpdatePackageVersionsStatusRequest](docs/UpdatePackageVersionsStatusRequest.md)
 - [CodeArtifact.UpdatePackageVersionsStatusResult](docs/UpdatePackageVersionsStatusResult.md)
 - [CodeArtifact.UpdateRepositoryRequest](docs/UpdateRepositoryRequest.md)
 - [CodeArtifact.UpdateRepositoryResult](docs/UpdateRepositoryResult.md)
 - [CodeArtifact.UpdateRepositoryResultRepository](docs/UpdateRepositoryResultRepository.md)
 - [CodeArtifact.UpstreamRepository](docs/UpstreamRepository.md)
 - [CodeArtifact.UpstreamRepositoryInfo](docs/UpstreamRepositoryInfo.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

