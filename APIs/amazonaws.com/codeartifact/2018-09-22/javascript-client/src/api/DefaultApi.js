/**
 * CodeArtifact
 * <p> CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. </p> <p> <b>CodeArtifact Components</b> </p> <p>Use the information in this guide to help you work with the following CodeArtifact components:</p> <ul> <li> <p> <b>Repository</b>: A CodeArtifact repository contains a set of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\">package versions</a>, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <b> <code>npm</code> </b> CLI, the Maven CLI (<b> <code>mvn</code> </b>), Python CLIs (<b> <code>pip</code> </b> and <code>twine</code>), and NuGet CLIs (<code>nuget</code> and <code>dotnet</code>).</p> </li> <li> <p> <b>Domain</b>: Repositories are aggregated into a higher-level entity known as a <i>domain</i>. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it's present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in Key Management Service (KMS).</p> <p>Each repository is a member of a single domain and can't be moved to a different domain.</p> <p>The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.</p> <p>Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.</p> </li> <li> <p> <b>Package</b>: A <i>package</i> is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\">npm</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\">PyPI</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\">Maven</a>, and <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget\">NuGet</a> package formats.</p> <p>In CodeArtifact, a package consists of:</p> <ul> <li> <p>A <i>name</i> (for example, <code>webpack</code> is the name of a popular npm package)</p> </li> <li> <p>An optional namespace (for example, <code>@types</code> in <code>@types/node</code>)</p> </li> <li> <p>A set of versions (for example, <code>1.0.0</code>, <code>1.0.1</code>, <code>1.0.2</code>, etc.)</p> </li> <li> <p> Package-level metadata (for example, npm tags)</p> </li> </ul> </li> <li> <p> <b>Package version</b>: A version of a package, such as <code>@types/node 12.6.9</code>. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the <a href=\"https://semver.org/\">Semantic Versioning specification</a>. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.</p> </li> <li> <p> <b>Upstream repository</b>: One repository is <i>upstream</i> of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.</p> </li> <li> <p> <b>Asset</b>: An individual file stored in CodeArtifact associated with a package version, such as an npm <code>.tgz</code> file or Maven POM and JAR files.</p> </li> </ul> <p>CodeArtifact supports these operations:</p> <ul> <li> <p> <code>AssociateExternalConnection</code>: Adds an existing external connection to a repository. </p> </li> <li> <p> <code>CopyPackageVersions</code>: Copies package versions from one repository to another repository in the same domain.</p> </li> <li> <p> <code>CreateDomain</code>: Creates a domain</p> </li> <li> <p> <code>CreateRepository</code>: Creates a CodeArtifact repository in a domain. </p> </li> <li> <p> <code>DeleteDomain</code>: Deletes a domain. You cannot delete a domain that contains repositories. </p> </li> <li> <p> <code>DeleteDomainPermissionsPolicy</code>: Deletes the resource policy that is set on a domain.</p> </li> <li> <p> <code>DeletePackage</code>: Deletes a package and all associated package versions.</p> </li> <li> <p> <code>DeletePackageVersions</code>: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DeleteRepository</code>: Deletes a repository. </p> </li> <li> <p> <code>DeleteRepositoryPermissionsPolicy</code>: Deletes the resource policy that is set on a repository.</p> </li> <li> <p> <code>DescribeDomain</code>: Returns a <code>DomainDescription</code> object that contains information about the requested domain.</p> </li> <li> <p> <code>DescribePackage</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains details about a package. </p> </li> <li> <p> <code>DescribePackageVersion</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains details about a package version. </p> </li> <li> <p> <code>DescribeRepository</code>: Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p> </li> <li> <p> <code>DisposePackageVersions</code>: Disposes versions of a package. A package version with the status <code>Disposed</code> cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DisassociateExternalConnection</code>: Removes an existing external connection from a repository. </p> </li> <li> <p> <code>GetAuthorizationToken</code>: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.</p> </li> <li> <p> <code>GetDomainPermissionsPolicy</code>: Returns the policy of a resource that is attached to the specified domain. </p> </li> <li> <p> <code>GetPackageVersionAsset</code>: Returns the contents of an asset that is in a package version. </p> </li> <li> <p> <code>GetPackageVersionReadme</code>: Gets the readme file or descriptive text for a package version.</p> </li> <li> <p> <code>GetRepositoryEndpoint</code>: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> </ul> </li> <li> <p> <code>GetRepositoryPermissionsPolicy</code>: Returns the resource policy that is set on a repository. </p> </li> <li> <p> <code>ListDomains</code>: Returns a list of <code>DomainSummary</code> objects. Each returned <code>DomainSummary</code> object contains information about a domain.</p> </li> <li> <p> <code>ListPackages</code>: Lists the packages in a repository.</p> </li> <li> <p> <code>ListPackageVersionAssets</code>: Lists the assets for a given package version.</p> </li> <li> <p> <code>ListPackageVersionDependencies</code>: Returns a list of the direct dependencies for a package version. </p> </li> <li> <p> <code>ListPackageVersions</code>: Returns a list of package versions for a specified package in a repository.</p> </li> <li> <p> <code>ListRepositories</code>: Returns a list of repositories owned by the Amazon Web Services account that called this method.</p> </li> <li> <p> <code>ListRepositoriesInDomain</code>: Returns a list of the repositories in a domain.</p> </li> <li> <p> <code>PublishPackageVersion</code>: Creates a new package version containing one or more assets.</p> </li> <li> <p> <code>PutDomainPermissionsPolicy</code>: Attaches a resource policy to a domain.</p> </li> <li> <p> <code>PutPackageOriginConfiguration</code>: Sets the package origin configuration for a package, which determine how new versions of the package can be added to a specific repository.</p> </li> <li> <p> <code>PutRepositoryPermissionsPolicy</code>: Sets the resource policy on a repository that specifies permissions to access it. </p> </li> <li> <p> <code>UpdatePackageVersionsStatus</code>: Updates the status of one or more versions of a package.</p> </li> <li> <p> <code>UpdateRepository</code>: Updates the properties of a repository.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2018-09-22
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AssociateExternalConnectionResult from '../model/AssociateExternalConnectionResult';
import CopyPackageVersionsRequest from '../model/CopyPackageVersionsRequest';
import CopyPackageVersionsResult from '../model/CopyPackageVersionsResult';
import CreateDomainRequest from '../model/CreateDomainRequest';
import CreateDomainResult from '../model/CreateDomainResult';
import CreateRepositoryRequest from '../model/CreateRepositoryRequest';
import CreateRepositoryResult from '../model/CreateRepositoryResult';
import DeleteDomainPermissionsPolicyResult from '../model/DeleteDomainPermissionsPolicyResult';
import DeleteDomainResult from '../model/DeleteDomainResult';
import DeletePackageResult from '../model/DeletePackageResult';
import DeletePackageVersionsRequest from '../model/DeletePackageVersionsRequest';
import DeletePackageVersionsResult from '../model/DeletePackageVersionsResult';
import DeleteRepositoryPermissionsPolicyResult from '../model/DeleteRepositoryPermissionsPolicyResult';
import DeleteRepositoryResult from '../model/DeleteRepositoryResult';
import DescribeDomainResult from '../model/DescribeDomainResult';
import DescribePackageResult from '../model/DescribePackageResult';
import DescribePackageVersionResult from '../model/DescribePackageVersionResult';
import DescribeRepositoryResult from '../model/DescribeRepositoryResult';
import DisassociateExternalConnectionResult from '../model/DisassociateExternalConnectionResult';
import DisposePackageVersionsRequest from '../model/DisposePackageVersionsRequest';
import DisposePackageVersionsResult from '../model/DisposePackageVersionsResult';
import GetAuthorizationTokenResult from '../model/GetAuthorizationTokenResult';
import GetDomainPermissionsPolicyResult from '../model/GetDomainPermissionsPolicyResult';
import GetPackageVersionAssetResult from '../model/GetPackageVersionAssetResult';
import GetPackageVersionReadmeResult from '../model/GetPackageVersionReadmeResult';
import GetRepositoryEndpointResult from '../model/GetRepositoryEndpointResult';
import GetRepositoryPermissionsPolicyResult from '../model/GetRepositoryPermissionsPolicyResult';
import ListDomainsRequest from '../model/ListDomainsRequest';
import ListDomainsResult from '../model/ListDomainsResult';
import ListPackageVersionAssetsResult from '../model/ListPackageVersionAssetsResult';
import ListPackageVersionDependenciesResult from '../model/ListPackageVersionDependenciesResult';
import ListPackageVersionsResult from '../model/ListPackageVersionsResult';
import ListPackagesResult from '../model/ListPackagesResult';
import ListRepositoriesInDomainResult from '../model/ListRepositoriesInDomainResult';
import ListRepositoriesResult from '../model/ListRepositoriesResult';
import ListTagsForResourceResult from '../model/ListTagsForResourceResult';
import PublishPackageVersionRequest from '../model/PublishPackageVersionRequest';
import PublishPackageVersionResult from '../model/PublishPackageVersionResult';
import PutDomainPermissionsPolicyRequest from '../model/PutDomainPermissionsPolicyRequest';
import PutDomainPermissionsPolicyResult from '../model/PutDomainPermissionsPolicyResult';
import PutPackageOriginConfigurationRequest from '../model/PutPackageOriginConfigurationRequest';
import PutPackageOriginConfigurationResult from '../model/PutPackageOriginConfigurationResult';
import PutRepositoryPermissionsPolicyRequest from '../model/PutRepositoryPermissionsPolicyRequest';
import PutRepositoryPermissionsPolicyResult from '../model/PutRepositoryPermissionsPolicyResult';
import TagResourceRequest from '../model/TagResourceRequest';
import UntagResourceRequest from '../model/UntagResourceRequest';
import UpdatePackageVersionsStatusRequest from '../model/UpdatePackageVersionsStatusRequest';
import UpdatePackageVersionsStatusResult from '../model/UpdatePackageVersionsStatusResult';
import UpdateRepositoryRequest from '../model/UpdateRepositoryRequest';
import UpdateRepositoryResult from '../model/UpdateRepositoryResult';

/**
* Default service.
* @module api/DefaultApi
* @version 2018-09-22
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the associateExternalConnection operation.
     * @callback module:api/DefaultApi~associateExternalConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AssociateExternalConnectionResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Adds an existing external connection to a repository. One external connection is allowed per repository.</p> <note> <p>A repository can have one or more upstream repositories, or an external connection.</p> </note>
     * @param {String} domain The name of the domain that contains the repository.
     * @param {String} repository  The name of the repository to which the external connection is added. 
     * @param {String} externalConnection <p> The name of the external connection to add to the repository. The following values are supported: </p> <ul> <li> <p> <code>public:npmjs</code> - for the npm public repository. </p> </li> <li> <p> <code>public:nuget-org</code> - for the NuGet Gallery. </p> </li> <li> <p> <code>public:pypi</code> - for the Python Package Index. </p> </li> <li> <p> <code>public:maven-central</code> - for Maven Central. </p> </li> <li> <p> <code>public:maven-googleandroid</code> - for the Google Android repository. </p> </li> <li> <p> <code>public:maven-gradleplugins</code> - for the Gradle plugins repository. </p> </li> <li> <p> <code>public:maven-commonsware</code> - for the CommonsWare Android repository. </p> </li> <li> <p> <code>public:maven-clojars</code> - for the Clojars repository. </p> </li> </ul>
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~associateExternalConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AssociateExternalConnectionResult}
     */
    associateExternalConnection(domain, repository, externalConnection, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling associateExternalConnection");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling associateExternalConnection");
      }
      // verify the required parameter 'externalConnection' is set
      if (externalConnection === undefined || externalConnection === null) {
        throw new Error("Missing the required parameter 'externalConnection' when calling associateExternalConnection");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'external-connection': externalConnection
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AssociateExternalConnectionResult;
      return this.apiClient.callApi(
        '/v1/repository/external-connection#domain&repository&external-connection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the copyPackageVersions operation.
     * @callback module:api/DefaultApi~copyPackageVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CopyPackageVersionsResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Copies package versions from one repository to another repository in the same domain. </p> <note> <p> You must specify <code>versions</code> or <code>versionRevisions</code>. You cannot specify both. </p> </note>
     * @param {String} domain  The name of the domain that contains the source and destination repositories. 
     * @param {String} sourceRepository  The name of the repository that contains the package versions to be copied. 
     * @param {String} destinationRepository  The name of the repository into which package versions are copied. 
     * @param {module:model/String} format  The format of the package versions to be copied. 
     * @param {String} _package  The name of the package that contains the versions to be copied. 
     * @param {module:model/CopyPackageVersionsRequest} copyPackageVersionsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. The namespace is required when copying Maven package versions. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~copyPackageVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CopyPackageVersionsResult}
     */
    copyPackageVersions(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, opts, callback) {
      opts = opts || {};
      let postBody = copyPackageVersionsRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling copyPackageVersions");
      }
      // verify the required parameter 'sourceRepository' is set
      if (sourceRepository === undefined || sourceRepository === null) {
        throw new Error("Missing the required parameter 'sourceRepository' when calling copyPackageVersions");
      }
      // verify the required parameter 'destinationRepository' is set
      if (destinationRepository === undefined || destinationRepository === null) {
        throw new Error("Missing the required parameter 'destinationRepository' when calling copyPackageVersions");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling copyPackageVersions");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling copyPackageVersions");
      }
      // verify the required parameter 'copyPackageVersionsRequest' is set
      if (copyPackageVersionsRequest === undefined || copyPackageVersionsRequest === null) {
        throw new Error("Missing the required parameter 'copyPackageVersionsRequest' when calling copyPackageVersions");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'source-repository': sourceRepository,
        'destination-repository': destinationRepository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CopyPackageVersionsResult;
      return this.apiClient.callApi(
        '/v1/package/versions/copy#domain&source-repository&destination-repository&format&package', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createDomain operation.
     * @callback module:api/DefaultApi~createDomainCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateDomainResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Creates a domain. CodeArtifact <i>domains</i> make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it's in multiple repositories. </p> <p>Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. </p>
     * @param {String} domain  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable. 
     * @param {module:model/CreateDomainRequest} createDomainRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createDomainCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateDomainResult}
     */
    createDomain(domain, createDomainRequest, opts, callback) {
      opts = opts || {};
      let postBody = createDomainRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling createDomain");
      }
      // verify the required parameter 'createDomainRequest' is set
      if (createDomainRequest === undefined || createDomainRequest === null) {
        throw new Error("Missing the required parameter 'createDomainRequest' when calling createDomain");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateDomainResult;
      return this.apiClient.callApi(
        '/v1/domain#domain', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createRepository operation.
     * @callback module:api/DefaultApi~createRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRepositoryResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Creates a repository. 
     * @param {String} domain  The name of the domain that contains the created repository. 
     * @param {String} repository  The name of the repository to create. 
     * @param {module:model/CreateRepositoryRequest} createRepositoryRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~createRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRepositoryResult}
     */
    createRepository(domain, repository, createRepositoryRequest, opts, callback) {
      opts = opts || {};
      let postBody = createRepositoryRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling createRepository");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling createRepository");
      }
      // verify the required parameter 'createRepositoryRequest' is set
      if (createRepositoryRequest === undefined || createRepositoryRequest === null) {
        throw new Error("Missing the required parameter 'createRepositoryRequest' when calling createRepository");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateRepositoryResult;
      return this.apiClient.callApi(
        '/v1/repository#domain&repository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDomain operation.
     * @callback module:api/DefaultApi~deleteDomainCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteDomainResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 
     * @param {String} domain  The name of the domain to delete. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~deleteDomainCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteDomainResult}
     */
    deleteDomain(domain, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling deleteDomain");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteDomainResult;
      return this.apiClient.callApi(
        '/v1/domain#domain', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDomainPermissionsPolicy operation.
     * @callback module:api/DefaultApi~deleteDomainPermissionsPolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteDomainPermissionsPolicyResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Deletes the resource policy set on a domain. 
     * @param {String} domain  The name of the domain associated with the resource policy to be deleted. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [policyRevision]  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. 
     * @param {module:api/DefaultApi~deleteDomainPermissionsPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteDomainPermissionsPolicyResult}
     */
    deleteDomainPermissionsPolicy(domain, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling deleteDomainPermissionsPolicy");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'policy-revision': opts['policyRevision']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteDomainPermissionsPolicyResult;
      return this.apiClient.callApi(
        '/v1/domain/permissions/policy#domain', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePackage operation.
     * @callback module:api/DefaultApi~deletePackageCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeletePackageResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\">DeletePackageVersions</a> API.
     * @param {String} domain The name of the domain that contains the package to delete.
     * @param {String} repository The name of the repository that contains the package to delete.
     * @param {module:model/String} format The format of the requested package to delete.
     * @param {String} _package The name of the package to delete.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. The namespace is required when deleting Maven package versions. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>.</p> </li> <li> <p> Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~deletePackageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeletePackageResult}
     */
    deletePackage(domain, repository, format, _package, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling deletePackage");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling deletePackage");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling deletePackage");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling deletePackage");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeletePackageResult;
      return this.apiClient.callApi(
        '/v1/package#domain&repository&format&package', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePackageVersions operation.
     * @callback module:api/DefaultApi~deletePackageVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeletePackageVersionsResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to <code>Archived</code>. Archived packages cannot be downloaded from a repository and don't show up with list package APIs (for example, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\">ListPackageVersions</a>), but you can restore them using <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\">UpdatePackageVersionsStatus</a>. 
     * @param {String} domain  The name of the domain that contains the package to delete. 
     * @param {String} repository  The name of the repository that contains the package versions to delete. 
     * @param {module:model/String} format  The format of the package versions to delete. 
     * @param {String} _package  The name of the package with the versions to delete. 
     * @param {module:model/DeletePackageVersionsRequest} deletePackageVersionsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. The namespace is required when deleting Maven package versions. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~deletePackageVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeletePackageVersionsResult}
     */
    deletePackageVersions(domain, repository, format, _package, deletePackageVersionsRequest, opts, callback) {
      opts = opts || {};
      let postBody = deletePackageVersionsRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling deletePackageVersions");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling deletePackageVersions");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling deletePackageVersions");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling deletePackageVersions");
      }
      // verify the required parameter 'deletePackageVersionsRequest' is set
      if (deletePackageVersionsRequest === undefined || deletePackageVersionsRequest === null) {
        throw new Error("Missing the required parameter 'deletePackageVersionsRequest' when calling deletePackageVersions");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeletePackageVersionsResult;
      return this.apiClient.callApi(
        '/v1/package/versions/delete#domain&repository&format&package', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRepository operation.
     * @callback module:api/DefaultApi~deleteRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteRepositoryResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Deletes a repository. 
     * @param {String} domain  The name of the domain that contains the repository to delete. 
     * @param {String} repository  The name of the repository to delete. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~deleteRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteRepositoryResult}
     */
    deleteRepository(domain, repository, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling deleteRepository");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling deleteRepository");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteRepositoryResult;
      return this.apiClient.callApi(
        '/v1/repository#domain&repository', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRepositoryPermissionsPolicy operation.
     * @callback module:api/DefaultApi~deleteRepositoryPermissionsPolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteRepositoryPermissionsPolicyResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. </p> <important> <p> Use <code>DeleteRepositoryPermissionsPolicy</code> with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. </p> </important>
     * @param {String} domain  The name of the domain that contains the repository associated with the resource policy to be deleted. 
     * @param {String} repository  The name of the repository that is associated with the resource policy to be deleted 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [policyRevision]  The revision of the repository's resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository's resource policy. 
     * @param {module:api/DefaultApi~deleteRepositoryPermissionsPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteRepositoryPermissionsPolicyResult}
     */
    deleteRepositoryPermissionsPolicy(domain, repository, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling deleteRepositoryPermissionsPolicy");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling deleteRepositoryPermissionsPolicy");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'policy-revision': opts['policyRevision']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteRepositoryPermissionsPolicyResult;
      return this.apiClient.callApi(
        '/v1/repository/permissions/policies#domain&repository', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the describeDomain operation.
     * @callback module:api/DefaultApi~describeDomainCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DescribeDomainResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\">DomainDescription</a> object that contains information about the requested domain. 
     * @param {String} domain  A string that specifies the name of the requested domain. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~describeDomainCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DescribeDomainResult}
     */
    describeDomain(domain, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling describeDomain");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DescribeDomainResult;
      return this.apiClient.callApi(
        '/v1/domain#domain', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the describePackage operation.
     * @callback module:api/DefaultApi~describePackageCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DescribePackageResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains information about the requested package.
     * @param {String} domain The name of the domain that contains the repository that contains the package.
     * @param {String} repository The name of the repository that contains the requested package. 
     * @param {module:model/String} format A format that specifies the type of the requested package.
     * @param {String} _package The name of the requested package.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. The namespace is required when requesting Maven packages. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~describePackageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DescribePackageResult}
     */
    describePackage(domain, repository, format, _package, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling describePackage");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling describePackage");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling describePackage");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling describePackage");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DescribePackageResult;
      return this.apiClient.callApi(
        '/v1/package#domain&repository&format&package', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the describePackageVersion operation.
     * @callback module:api/DefaultApi~describePackageVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DescribePackageVersionResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains information about the requested package version. 
     * @param {String} domain  The name of the domain that contains the repository that contains the package version. 
     * @param {String} repository  The name of the repository that contains the package version. 
     * @param {module:model/String} format  A format that specifies the type of the requested package version. 
     * @param {String} _package  The name of the requested package version. 
     * @param {String} version  A string that contains the package version (for example, <code>3.5.2</code>). 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~describePackageVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DescribePackageVersionResult}
     */
    describePackageVersion(domain, repository, format, _package, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling describePackageVersion");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling describePackageVersion");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling describePackageVersion");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling describePackageVersion");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling describePackageVersion");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'version': version
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DescribePackageVersionResult;
      return this.apiClient.callApi(
        '/v1/package/version#domain&repository&format&package&version', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the describeRepository operation.
     * @callback module:api/DefaultApi~describeRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DescribeRepositoryResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. 
     * @param {String} domain  The name of the domain that contains the repository to describe. 
     * @param {String} repository  A string that specifies the name of the requested repository. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~describeRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DescribeRepositoryResult}
     */
    describeRepository(domain, repository, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling describeRepository");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling describeRepository");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DescribeRepositoryResult;
      return this.apiClient.callApi(
        '/v1/repository#domain&repository', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disassociateExternalConnection operation.
     * @callback module:api/DefaultApi~disassociateExternalConnectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DisassociateExternalConnectionResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Removes an existing external connection from a repository. 
     * @param {String} domain The name of the domain that contains the repository from which to remove the external repository. 
     * @param {String} repository The name of the repository from which the external connection will be removed. 
     * @param {String} externalConnection The name of the external connection to be removed from the repository. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~disassociateExternalConnectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DisassociateExternalConnectionResult}
     */
    disassociateExternalConnection(domain, repository, externalConnection, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling disassociateExternalConnection");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling disassociateExternalConnection");
      }
      // verify the required parameter 'externalConnection' is set
      if (externalConnection === undefined || externalConnection === null) {
        throw new Error("Missing the required parameter 'externalConnection' when calling disassociateExternalConnection");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'external-connection': externalConnection
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DisassociateExternalConnectionResult;
      return this.apiClient.callApi(
        '/v1/repository/external-connection#domain&repository&external-connection', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disposePackageVersions operation.
     * @callback module:api/DefaultApi~disposePackageVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DisposePackageVersionsResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Deletes the assets in package versions and sets the package versions' status to <code>Disposed</code>. A disposed package version cannot be restored in your repository because its assets are deleted. </p> <p> To view all disposed package versions in a repository, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\">ListPackageVersions</a> and set the <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\">status</a> parameter to <code>Disposed</code>. </p> <p> To view information about a disposed package version, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\">DescribePackageVersion</a>. </p>
     * @param {String} domain  The name of the domain that contains the repository you want to dispose. 
     * @param {String} repository  The name of the repository that contains the package versions you want to dispose. 
     * @param {module:model/String} format  A format that specifies the type of package versions you want to dispose. 
     * @param {String} _package  The name of the package with the versions you want to dispose. 
     * @param {module:model/DisposePackageVersionsRequest} disposePackageVersionsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~disposePackageVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DisposePackageVersionsResult}
     */
    disposePackageVersions(domain, repository, format, _package, disposePackageVersionsRequest, opts, callback) {
      opts = opts || {};
      let postBody = disposePackageVersionsRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling disposePackageVersions");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling disposePackageVersions");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling disposePackageVersions");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling disposePackageVersions");
      }
      // verify the required parameter 'disposePackageVersionsRequest' is set
      if (disposePackageVersionsRequest === undefined || disposePackageVersionsRequest === null) {
        throw new Error("Missing the required parameter 'disposePackageVersionsRequest' when calling disposePackageVersions");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DisposePackageVersionsResult;
      return this.apiClient.callApi(
        '/v1/package/versions/dispose#domain&repository&format&package', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAuthorizationToken operation.
     * @callback module:api/DefaultApi~getAuthorizationTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAuthorizationTokenResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Generates a temporary authorization token for accessing repositories in the domain. This API requires the <code>codeartifact:GetAuthorizationToken</code> and <code>sts:GetServiceBearerToken</code> permissions. For more information about authorization tokens, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\">CodeArtifact authentication and tokens</a>. </p> <note> <p>CodeArtifact authorization tokens are valid for a period of 12 hours when created with the <code>login</code> command. You can call <code>login</code> periodically to refresh the token. When you create an authorization token with the <code>GetAuthorizationToken</code> API, you can set a custom authorization period, up to a maximum of 12 hours, with the <code>durationSeconds</code> parameter.</p> <p>The authorization period begins after <code>login</code> or <code>GetAuthorizationToken</code> is called. If <code>login</code> or <code>GetAuthorizationToken</code> is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call <code>sts assume-role</code> and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.</p> <p>See <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\">Using IAM Roles</a> for more information on controlling session duration. </p> </note>
     * @param {String} domain  The name of the domain that is in scope for the generated authorization token. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {Number} [duration] The time, in seconds, that the generated authorization token is valid. Valid values are <code>0</code> and any number between <code>900</code> (15 minutes) and <code>43200</code> (12 hours). A value of <code>0</code> will set the expiration of the authorization token to the same expiration of the user's role's temporary credentials.
     * @param {module:api/DefaultApi~getAuthorizationTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAuthorizationTokenResult}
     */
    getAuthorizationToken(domain, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling getAuthorizationToken");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'duration': opts['duration']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetAuthorizationTokenResult;
      return this.apiClient.callApi(
        '/v1/authorization-token#domain', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDomainPermissionsPolicy operation.
     * @callback module:api/DefaultApi~getDomainPermissionsPolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDomainPermissionsPolicyResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Returns the resource policy attached to the specified domain. </p> <note> <p> The policy is a resource-based policy, not an identity-based policy. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\">Identity-based policies and resource-based policies </a> in the <i>IAM User Guide</i>. </p> </note>
     * @param {String} domain  The name of the domain to which the resource policy is attached. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~getDomainPermissionsPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDomainPermissionsPolicyResult}
     */
    getDomainPermissionsPolicy(domain, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling getDomainPermissionsPolicy");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDomainPermissionsPolicyResult;
      return this.apiClient.callApi(
        '/v1/domain/permissions/policy#domain', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPackageVersionAsset operation.
     * @callback module:api/DefaultApi~getPackageVersionAssetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPackageVersionAssetResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns an asset (or file) that is in a package. For example, for a Maven package version, use <code>GetPackageVersionAsset</code> to download a <code>JAR</code> file, a <code>POM</code> file, or any other assets in the package version. 
     * @param {String} domain  The name of the domain that contains the repository that contains the package version with the requested asset. 
     * @param {String} repository  The repository that contains the package version with the requested asset. 
     * @param {module:model/String} format  A format that specifies the type of the package version with the requested asset file. 
     * @param {String} _package  The name of the package that contains the requested asset. 
     * @param {String} version  A string that contains the package version (for example, <code>3.5.2</code>). 
     * @param {String} asset  The name of the requested asset. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {String} [revision]  The name of the package version revision that contains the requested asset. 
     * @param {module:api/DefaultApi~getPackageVersionAssetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPackageVersionAssetResult}
     */
    getPackageVersionAsset(domain, repository, format, _package, version, asset, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling getPackageVersionAsset");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling getPackageVersionAsset");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling getPackageVersionAsset");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling getPackageVersionAsset");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling getPackageVersionAsset");
      }
      // verify the required parameter 'asset' is set
      if (asset === undefined || asset === null) {
        throw new Error("Missing the required parameter 'asset' when calling getPackageVersionAsset");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'version': version,
        'asset': asset,
        'revision': opts['revision']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetPackageVersionAssetResult;
      return this.apiClient.callApi(
        '/v1/package/version/asset#domain&repository&format&package&version&asset', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPackageVersionReadme operation.
     * @callback module:api/DefaultApi~getPackageVersionReadmeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPackageVersionReadmeResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Gets the readme file or descriptive text for a package version. </p> <p> The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. </p>
     * @param {String} domain  The name of the domain that contains the repository that contains the package version with the requested readme file. 
     * @param {String} repository  The repository that contains the package with the requested readme file. 
     * @param {module:model/String} format  A format that specifies the type of the package version with the requested readme file. 
     * @param {String} _package  The name of the package version that contains the requested readme file. 
     * @param {String} version  A string that contains the package version (for example, <code>3.5.2</code>). 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
     * @param {module:api/DefaultApi~getPackageVersionReadmeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPackageVersionReadmeResult}
     */
    getPackageVersionReadme(domain, repository, format, _package, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling getPackageVersionReadme");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling getPackageVersionReadme");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling getPackageVersionReadme");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling getPackageVersionReadme");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling getPackageVersionReadme");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'version': version
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetPackageVersionReadmeResult;
      return this.apiClient.callApi(
        '/v1/package/version/readme#domain&repository&format&package&version', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRepositoryEndpoint operation.
     * @callback module:api/DefaultApi~getRepositoryEndpointCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRepositoryEndpointResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> </ul>
     * @param {String} domain  The name of the domain that contains the repository. 
     * @param {String} repository  The name of the repository. 
     * @param {module:model/String} format  Returns which endpoint of a repository to return. A repository has one endpoint for each package format. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~getRepositoryEndpointCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRepositoryEndpointResult}
     */
    getRepositoryEndpoint(domain, repository, format, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling getRepositoryEndpoint");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling getRepositoryEndpoint");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling getRepositoryEndpoint");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetRepositoryEndpointResult;
      return this.apiClient.callApi(
        '/v1/repository/endpoint#domain&repository&format', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRepositoryPermissionsPolicy operation.
     * @callback module:api/DefaultApi~getRepositoryPermissionsPolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRepositoryPermissionsPolicyResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns the resource policy that is set on a repository. 
     * @param {String} domain  The name of the domain containing the repository whose associated resource policy is to be retrieved. 
     * @param {String} repository  The name of the repository whose associated resource policy is to be retrieved. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~getRepositoryPermissionsPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRepositoryPermissionsPolicyResult}
     */
    getRepositoryPermissionsPolicy(domain, repository, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling getRepositoryPermissionsPolicy");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling getRepositoryPermissionsPolicy");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetRepositoryPermissionsPolicyResult;
      return this.apiClient.callApi(
        '/v1/repository/permissions/policy#domain&repository', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listDomains operation.
     * @callback module:api/DefaultApi~listDomainsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListDomainsResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">DomainSummary</a> objects for all domains owned by the Amazon Web Services account that makes this call. Each returned <code>DomainSummary</code> object contains information about a domain. 
     * @param {module:model/ListDomainsRequest} listDomainsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listDomainsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListDomainsResult}
     */
    listDomains(listDomainsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listDomainsRequest;
      // verify the required parameter 'listDomainsRequest' is set
      if (listDomainsRequest === undefined || listDomainsRequest === null) {
        throw new Error("Missing the required parameter 'listDomainsRequest' when calling listDomains");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListDomainsResult;
      return this.apiClient.callApi(
        '/v1/domains', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPackageVersionAssets operation.
     * @callback module:api/DefaultApi~listPackageVersionAssetsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPackageVersionAssetsResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\">AssetSummary</a> objects for assets in a package version. 
     * @param {String} domain  The name of the domain that contains the repository associated with the package version assets. 
     * @param {String} repository  The name of the repository that contains the package that contains the requested package version assets. 
     * @param {module:model/String} format  The format of the package that contains the requested package version assets. 
     * @param {String} _package  The name of the package that contains the requested package version assets. 
     * @param {String} version  A string that contains the package version (for example, <code>3.5.2</code>). 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {Number} [maxResults]  The maximum number of results to return per page. 
     * @param {String} [nextToken]  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
     * @param {String} [maxResults2] Pagination limit
     * @param {String} [nextToken2] Pagination token
     * @param {module:api/DefaultApi~listPackageVersionAssetsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPackageVersionAssetsResult}
     */
    listPackageVersionAssets(domain, repository, format, _package, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling listPackageVersionAssets");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling listPackageVersionAssets");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling listPackageVersionAssets");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling listPackageVersionAssets");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling listPackageVersionAssets");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'version': version,
        'max-results': opts['maxResults'],
        'next-token': opts['nextToken'],
        'maxResults': opts['maxResults2'],
        'nextToken': opts['nextToken2']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListPackageVersionAssetsResult;
      return this.apiClient.callApi(
        '/v1/package/version/assets#domain&repository&format&package&version', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPackageVersionDependencies operation.
     * @callback module:api/DefaultApi~listPackageVersionDependenciesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPackageVersionDependenciesResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns the direct dependencies for a package version. The dependencies are returned as <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\">PackageDependency</a> objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the <code>package.json</code> file for npm packages and the <code>pom.xml</code> file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 
     * @param {String} domain  The name of the domain that contains the repository that contains the requested package version dependencies. 
     * @param {String} repository  The name of the repository that contains the requested package version. 
     * @param {module:model/String} format  The format of the package with the requested dependencies. 
     * @param {String} _package  The name of the package versions' package. 
     * @param {String} version  A string that contains the package version (for example, <code>3.5.2</code>). 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {String} [nextToken]  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
     * @param {module:api/DefaultApi~listPackageVersionDependenciesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPackageVersionDependenciesResult}
     */
    listPackageVersionDependencies(domain, repository, format, _package, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling listPackageVersionDependencies");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling listPackageVersionDependencies");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling listPackageVersionDependencies");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling listPackageVersionDependencies");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling listPackageVersionDependencies");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'version': version,
        'next-token': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListPackageVersionDependenciesResult;
      return this.apiClient.callApi(
        '/v1/package/version/dependencies#domain&repository&format&package&version', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPackageVersions operation.
     * @callback module:api/DefaultApi~listPackageVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPackageVersionsResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\">PackageVersionSummary</a> objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling <code>list-package-versions</code> with no <code>--status</code> parameter. 
     * @param {String} domain  The name of the domain that contains the repository that contains the requested package versions. 
     * @param {String} repository  The name of the repository that contains the requested package versions. 
     * @param {module:model/String} format  The format of the package versions you want to list. 
     * @param {String} _package  The name of the package for which you want to request package versions. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:model/String} [status]  A string that filters the requested package versions by status. 
     * @param {module:model/String} [sortBy]  How to sort the requested list of package versions. 
     * @param {Number} [maxResults]  The maximum number of results to return per page. 
     * @param {String} [nextToken]  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
     * @param {module:model/String} [originType] The <code>originType</code> used to filter package versions. Only package versions with the provided <code>originType</code> will be returned.
     * @param {String} [maxResults2] Pagination limit
     * @param {String} [nextToken2] Pagination token
     * @param {module:api/DefaultApi~listPackageVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPackageVersionsResult}
     */
    listPackageVersions(domain, repository, format, _package, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling listPackageVersions");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling listPackageVersions");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling listPackageVersions");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling listPackageVersions");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'status': opts['status'],
        'sortBy': opts['sortBy'],
        'max-results': opts['maxResults'],
        'next-token': opts['nextToken'],
        'originType': opts['originType'],
        'maxResults': opts['maxResults2'],
        'nextToken': opts['nextToken2']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListPackageVersionsResult;
      return this.apiClient.callApi(
        '/v1/package/versions#domain&repository&format&package', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPackages operation.
     * @callback module:api/DefaultApi~listPackagesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPackagesResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\">PackageSummary</a> objects for packages in a repository that match the request parameters. 
     * @param {String} domain  The name of the domain that contains the repository that contains the requested packages. 
     * @param {String} repository  The name of the repository that contains the requested packages. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:model/String} [format] The format used to filter requested packages. Only packages from the provided format will be returned.
     * @param {String} [namespace] <p>The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called <code>--namespace</code> and not <code>--namespace-prefix</code>, it has prefix-matching behavior.</p> <p>Each package format uses namespace as follows:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {String} [packagePrefix]  A prefix used to filter requested packages. Only packages with names that start with <code>packagePrefix</code> are returned. 
     * @param {Number} [maxResults]  The maximum number of results to return per page. 
     * @param {String} [nextToken]  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
     * @param {module:model/String} [publish] The value of the <code>Publish</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a>.
     * @param {module:model/String} [upstream] The value of the <code>Upstream</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a>.
     * @param {String} [maxResults2] Pagination limit
     * @param {String} [nextToken2] Pagination token
     * @param {module:api/DefaultApi~listPackagesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPackagesResult}
     */
    listPackages(domain, repository, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling listPackages");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling listPackages");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': opts['format'],
        'namespace': opts['namespace'],
        'package-prefix': opts['packagePrefix'],
        'max-results': opts['maxResults'],
        'next-token': opts['nextToken'],
        'publish': opts['publish'],
        'upstream': opts['upstream'],
        'maxResults': opts['maxResults2'],
        'nextToken': opts['nextToken2']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListPackagesResult;
      return this.apiClient.callApi(
        '/v1/packages#domain&repository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRepositories operation.
     * @callback module:api/DefaultApi~listRepositoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRepositoriesResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\">RepositorySummary</a> objects. Each <code>RepositorySummary</code> contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [repositoryPrefix]  A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned.
     * @param {Number} [maxResults]  The maximum number of results to return per page. 
     * @param {String} [nextToken]  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
     * @param {String} [maxResults2] Pagination limit
     * @param {String} [nextToken2] Pagination token
     * @param {module:api/DefaultApi~listRepositoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRepositoriesResult}
     */
    listRepositories(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'repository-prefix': opts['repositoryPrefix'],
        'max-results': opts['maxResults'],
        'next-token': opts['nextToken'],
        'maxResults': opts['maxResults2'],
        'nextToken': opts['nextToken2']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListRepositoriesResult;
      return this.apiClient.callApi(
        '/v1/repositories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRepositoriesInDomain operation.
     * @callback module:api/DefaultApi~listRepositoriesInDomainCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRepositoriesInDomainResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\">RepositorySummary</a> objects. Each <code>RepositorySummary</code> contains information about a repository in the specified domain and that matches the input parameters. 
     * @param {String} domain  The name of the domain that contains the returned list of repositories. 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [administratorAccount]  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID. 
     * @param {String} [repositoryPrefix]  A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned. 
     * @param {Number} [maxResults]  The maximum number of results to return per page. 
     * @param {String} [nextToken]  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
     * @param {String} [maxResults2] Pagination limit
     * @param {String} [nextToken2] Pagination token
     * @param {module:api/DefaultApi~listRepositoriesInDomainCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRepositoriesInDomainResult}
     */
    listRepositoriesInDomain(domain, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling listRepositoriesInDomain");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'administrator-account': opts['administratorAccount'],
        'repository-prefix': opts['repositoryPrefix'],
        'max-results': opts['maxResults'],
        'next-token': opts['nextToken'],
        'maxResults': opts['maxResults2'],
        'nextToken': opts['nextToken2']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListRepositoriesInDomainResult;
      return this.apiClient.callApi(
        '/v1/domain/repositories#domain', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listTagsForResource operation.
     * @callback module:api/DefaultApi~listTagsForResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTagsForResourceResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.
     * @param {String} resourceArn The Amazon Resource Name (ARN) of the resource to get tags for.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~listTagsForResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTagsForResourceResult}
     */
    listTagsForResource(resourceArn, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling listTagsForResource");
      }

      let pathParams = {
      };
      let queryParams = {
        'resourceArn': resourceArn
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListTagsForResourceResult;
      return this.apiClient.callApi(
        '/v1/tags#resourceArn', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the publishPackageVersion operation.
     * @callback module:api/DefaultApi~publishPackageVersionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PublishPackageVersionResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates a new package version containing one or more assets (or files).</p> <p>The <code>unfinished</code> flag can be used to keep the package version in the <code>Unfinished</code> state until all of its assets have been uploaded (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\">Package version status</a> in the <i>CodeArtifact user guide</i>). To set the package version’s status to <code>Published</code>, omit the <code>unfinished</code> flag when uploading the final asset, or set the status using <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\">UpdatePackageVersionStatus</a>. Once a package version’s status is set to <code>Published</code>, it cannot change back to <code>Unfinished</code>.</p> <note> <p>Only generic packages can be published using this API. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\">Using generic packages</a> in the <i>CodeArtifact User Guide</i>.</p> </note>
     * @param {String} domain The name of the domain that contains the repository that contains the package version to publish.
     * @param {String} repository The name of the repository that the package version will be published to.
     * @param {module:model/String} format <p>A format that specifies the type of the package version with the requested asset file.</p> <p>The only supported value is <code>generic</code>.</p>
     * @param {String} _package The name of the package version to publish.
     * @param {String} version The package version to publish (for example, <code>3.5.2</code>).
     * @param {String} asset The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: <code>~ ! @ ^ &amp; ( ) - ` _ + [ ] { } ; , . `</code> 
     * @param {String} xAmzContentSha257 <p>The SHA256 hash of the <code>assetContent</code> to publish. This value must be calculated by the caller and provided with the request (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\">Publishing a generic package</a> in the <i>CodeArtifact User Guide</i>).</p> <p>This value is used as an integrity check to verify that the <code>assetContent</code> has not changed after it was originally sent.</p>
     * @param {module:model/PublishPackageVersionRequest} publishPackageVersionRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner] The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
     * @param {String} [namespace] The namespace of the package version to publish.
     * @param {Boolean} [unfinished] <p>Specifies whether the package version should remain in the <code>unfinished</code> state. If omitted, the package version status will be set to <code>Published</code> (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\">Package version status</a> in the <i>CodeArtifact User Guide</i>).</p> <p>Valid values: <code>unfinished</code> </p>
     * @param {module:api/DefaultApi~publishPackageVersionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PublishPackageVersionResult}
     */
    publishPackageVersion(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, opts, callback) {
      opts = opts || {};
      let postBody = publishPackageVersionRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling publishPackageVersion");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling publishPackageVersion");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling publishPackageVersion");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling publishPackageVersion");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling publishPackageVersion");
      }
      // verify the required parameter 'asset' is set
      if (asset === undefined || asset === null) {
        throw new Error("Missing the required parameter 'asset' when calling publishPackageVersion");
      }
      // verify the required parameter 'xAmzContentSha257' is set
      if (xAmzContentSha257 === undefined || xAmzContentSha257 === null) {
        throw new Error("Missing the required parameter 'xAmzContentSha257' when calling publishPackageVersion");
      }
      // verify the required parameter 'publishPackageVersionRequest' is set
      if (publishPackageVersionRequest === undefined || publishPackageVersionRequest === null) {
        throw new Error("Missing the required parameter 'publishPackageVersionRequest' when calling publishPackageVersion");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package,
        'version': version,
        'asset': asset,
        'unfinished': opts['unfinished']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'x-amz-content-sha256': xAmzContentSha257
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PublishPackageVersionResult;
      return this.apiClient.callApi(
        '/v1/package/version/publish#domain&repository&format&package&version&asset&x-amz-content-sha256', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putDomainPermissionsPolicy operation.
     * @callback module:api/DefaultApi~putDomainPermissionsPolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutDomainPermissionsPolicyResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Sets a resource policy on a domain that specifies permissions to access it. </p> <p> When you call <code>PutDomainPermissionsPolicy</code>, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. </p>
     * @param {module:model/PutDomainPermissionsPolicyRequest} putDomainPermissionsPolicyRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putDomainPermissionsPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutDomainPermissionsPolicyResult}
     */
    putDomainPermissionsPolicy(putDomainPermissionsPolicyRequest, opts, callback) {
      opts = opts || {};
      let postBody = putDomainPermissionsPolicyRequest;
      // verify the required parameter 'putDomainPermissionsPolicyRequest' is set
      if (putDomainPermissionsPolicyRequest === undefined || putDomainPermissionsPolicyRequest === null) {
        throw new Error("Missing the required parameter 'putDomainPermissionsPolicyRequest' when calling putDomainPermissionsPolicy");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PutDomainPermissionsPolicyResult;
      return this.apiClient.callApi(
        '/v1/domain/permissions/policy', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putPackageOriginConfiguration operation.
     * @callback module:api/DefaultApi~putPackageOriginConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutPackageOriginConfigurationResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Sets the package origin configuration for a package.</p> <p>The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\">Editing package origin controls</a> in the <i>CodeArtifact User Guide</i>.</p> <p> <code>PutPackageOriginConfiguration</code> can be called on a package that doesn't yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.</p>
     * @param {String} domain The name of the domain that contains the repository that contains the package.
     * @param {String} repository The name of the repository that contains the package.
     * @param {module:model/String} format A format that specifies the type of the package to be updated.
     * @param {String} _package The name of the package to be updated.
     * @param {module:model/PutPackageOriginConfigurationRequest} putPackageOriginConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~putPackageOriginConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutPackageOriginConfigurationResult}
     */
    putPackageOriginConfiguration(domain, repository, format, _package, putPackageOriginConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = putPackageOriginConfigurationRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling putPackageOriginConfiguration");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling putPackageOriginConfiguration");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling putPackageOriginConfiguration");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling putPackageOriginConfiguration");
      }
      // verify the required parameter 'putPackageOriginConfigurationRequest' is set
      if (putPackageOriginConfigurationRequest === undefined || putPackageOriginConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'putPackageOriginConfigurationRequest' when calling putPackageOriginConfiguration");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PutPackageOriginConfigurationResult;
      return this.apiClient.callApi(
        '/v1/package#domain&repository&format&package', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putRepositoryPermissionsPolicy operation.
     * @callback module:api/DefaultApi~putRepositoryPermissionsPolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutRepositoryPermissionsPolicyResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p> Sets the resource policy on a repository that specifies permissions to access it. </p> <p> When you call <code>PutRepositoryPermissionsPolicy</code>, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. </p>
     * @param {String} domain  The name of the domain containing the repository to set the resource policy on. 
     * @param {String} repository  The name of the repository to set the resource policy on. 
     * @param {module:model/PutRepositoryPermissionsPolicyRequest} putRepositoryPermissionsPolicyRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~putRepositoryPermissionsPolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutRepositoryPermissionsPolicyResult}
     */
    putRepositoryPermissionsPolicy(domain, repository, putRepositoryPermissionsPolicyRequest, opts, callback) {
      opts = opts || {};
      let postBody = putRepositoryPermissionsPolicyRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling putRepositoryPermissionsPolicy");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling putRepositoryPermissionsPolicy");
      }
      // verify the required parameter 'putRepositoryPermissionsPolicyRequest' is set
      if (putRepositoryPermissionsPolicyRequest === undefined || putRepositoryPermissionsPolicyRequest === null) {
        throw new Error("Missing the required parameter 'putRepositoryPermissionsPolicyRequest' when calling putRepositoryPermissionsPolicy");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PutRepositoryPermissionsPolicyResult;
      return this.apiClient.callApi(
        '/v1/repository/permissions/policy#domain&repository', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tagResource operation.
     * @callback module:api/DefaultApi~tagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds or updates tags for a resource in CodeArtifact.
     * @param {String} resourceArn The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.
     * @param {module:model/TagResourceRequest} tagResourceRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~tagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    tagResource(resourceArn, tagResourceRequest, opts, callback) {
      opts = opts || {};
      let postBody = tagResourceRequest;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling tagResource");
      }
      // verify the required parameter 'tagResourceRequest' is set
      if (tagResourceRequest === undefined || tagResourceRequest === null) {
        throw new Error("Missing the required parameter 'tagResourceRequest' when calling tagResource");
      }

      let pathParams = {
      };
      let queryParams = {
        'resourceArn': resourceArn
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v1/tag#resourceArn', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the untagResource operation.
     * @callback module:api/DefaultApi~untagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes tags from a resource in CodeArtifact.
     * @param {String} resourceArn The Amazon Resource Name (ARN) of the resource that you want to remove tags from.
     * @param {module:model/UntagResourceRequest} untagResourceRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~untagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    untagResource(resourceArn, untagResourceRequest, opts, callback) {
      opts = opts || {};
      let postBody = untagResourceRequest;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling untagResource");
      }
      // verify the required parameter 'untagResourceRequest' is set
      if (untagResourceRequest === undefined || untagResourceRequest === null) {
        throw new Error("Missing the required parameter 'untagResourceRequest' when calling untagResource");
      }

      let pathParams = {
      };
      let queryParams = {
        'resourceArn': resourceArn
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v1/untag#resourceArn', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePackageVersionsStatus operation.
     * @callback module:api/DefaultApi~updatePackageVersionsStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdatePackageVersionsStatusResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Updates the status of one or more versions of a package. Using <code>UpdatePackageVersionsStatus</code>, you can update the status of package versions to <code>Archived</code>, <code>Published</code>, or <code>Unlisted</code>. To set the status of a package version to <code>Disposed</code>, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\">DisposePackageVersions</a>. 
     * @param {String} domain  The name of the domain that contains the repository that contains the package versions with a status to be updated. 
     * @param {String} repository  The repository that contains the package versions with the status you want to update. 
     * @param {module:model/String} format  A format that specifies the type of the package with the statuses to update. 
     * @param {String} _package  The name of the package with the version statuses to update. 
     * @param {module:model/UpdatePackageVersionsStatusRequest} updatePackageVersionsStatusRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {String} [namespace] <p>The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> <li> <p> The namespace of a generic package is its <code>namespace</code>. </p> </li> </ul>
     * @param {module:api/DefaultApi~updatePackageVersionsStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdatePackageVersionsStatusResult}
     */
    updatePackageVersionsStatus(domain, repository, format, _package, updatePackageVersionsStatusRequest, opts, callback) {
      opts = opts || {};
      let postBody = updatePackageVersionsStatusRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling updatePackageVersionsStatus");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling updatePackageVersionsStatus");
      }
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling updatePackageVersionsStatus");
      }
      // verify the required parameter '_package' is set
      if (_package === undefined || _package === null) {
        throw new Error("Missing the required parameter '_package' when calling updatePackageVersionsStatus");
      }
      // verify the required parameter 'updatePackageVersionsStatusRequest' is set
      if (updatePackageVersionsStatusRequest === undefined || updatePackageVersionsStatusRequest === null) {
        throw new Error("Missing the required parameter 'updatePackageVersionsStatusRequest' when calling updatePackageVersionsStatus");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository,
        'format': format,
        'namespace': opts['namespace'],
        'package': _package
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdatePackageVersionsStatusResult;
      return this.apiClient.callApi(
        '/v1/package/versions/update_status#domain&repository&format&package', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateRepository operation.
     * @callback module:api/DefaultApi~updateRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateRepositoryResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Update the properties of a repository. 
     * @param {String} domain  The name of the domain associated with the repository to update. 
     * @param {String} repository  The name of the repository to update. 
     * @param {module:model/UpdateRepositoryRequest} updateRepositoryRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [domainOwner]  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
     * @param {module:api/DefaultApi~updateRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateRepositoryResult}
     */
    updateRepository(domain, repository, updateRepositoryRequest, opts, callback) {
      opts = opts || {};
      let postBody = updateRepositoryRequest;
      // verify the required parameter 'domain' is set
      if (domain === undefined || domain === null) {
        throw new Error("Missing the required parameter 'domain' when calling updateRepository");
      }
      // verify the required parameter 'repository' is set
      if (repository === undefined || repository === null) {
        throw new Error("Missing the required parameter 'repository' when calling updateRepository");
      }
      // verify the required parameter 'updateRepositoryRequest' is set
      if (updateRepositoryRequest === undefined || updateRepositoryRequest === null) {
        throw new Error("Missing the required parameter 'updateRepositoryRequest' when calling updateRepository");
      }

      let pathParams = {
      };
      let queryParams = {
        'domain': domain,
        'domain-owner': opts['domainOwner'],
        'repository': repository
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateRepositoryResult;
      return this.apiClient.callApi(
        '/v1/repository#domain&repository', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
