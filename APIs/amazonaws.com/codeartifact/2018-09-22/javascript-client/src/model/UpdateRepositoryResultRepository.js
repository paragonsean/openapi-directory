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

import ApiClient from '../ApiClient';
import RepositoryDescription from './RepositoryDescription';

/**
 * The UpdateRepositoryResultRepository model module.
 * @module model/UpdateRepositoryResultRepository
 * @version 2018-09-22
 */
class UpdateRepositoryResultRepository {
    /**
     * Constructs a new <code>UpdateRepositoryResultRepository</code>.
     * @alias module:model/UpdateRepositoryResultRepository
     * @implements module:model/RepositoryDescription
     */
    constructor() { 
        RepositoryDescription.initialize(this);
        UpdateRepositoryResultRepository.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateRepositoryResultRepository</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateRepositoryResultRepository} obj Optional instance to populate.
     * @return {module:model/UpdateRepositoryResultRepository} The populated <code>UpdateRepositoryResultRepository</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateRepositoryResultRepository();
            RepositoryDescription.constructFromObject(data, obj);

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('administratorAccount')) {
                obj['administratorAccount'] = ApiClient.convertToType(data['administratorAccount'], 'String');
            }
            if (data.hasOwnProperty('domainName')) {
                obj['domainName'] = ApiClient.convertToType(data['domainName'], 'String');
            }
            if (data.hasOwnProperty('domainOwner')) {
                obj['domainOwner'] = ApiClient.convertToType(data['domainOwner'], 'String');
            }
            if (data.hasOwnProperty('arn')) {
                obj['arn'] = ApiClient.convertToType(data['arn'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('upstreams')) {
                obj['upstreams'] = ApiClient.convertToType(data['upstreams'], Array);
            }
            if (data.hasOwnProperty('externalConnections')) {
                obj['externalConnections'] = ApiClient.convertToType(data['externalConnections'], Array);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateRepositoryResultRepository</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateRepositoryResultRepository</code>.
     */
    static validateJSON(data) {
        // validate the optional field `name`
        if (data['name']) { // data not null
          String.validateJSON(data['name']);
        }
        // validate the optional field `administratorAccount`
        if (data['administratorAccount']) { // data not null
          String.validateJSON(data['administratorAccount']);
        }
        // validate the optional field `domainName`
        if (data['domainName']) { // data not null
          String.validateJSON(data['domainName']);
        }
        // validate the optional field `domainOwner`
        if (data['domainOwner']) { // data not null
          String.validateJSON(data['domainOwner']);
        }
        // validate the optional field `arn`
        if (data['arn']) { // data not null
          String.validateJSON(data['arn']);
        }
        // validate the optional field `description`
        if (data['description']) { // data not null
          String.validateJSON(data['description']);
        }
        // validate the optional field `upstreams`
        if (data['upstreams']) { // data not null
          Array.validateJSON(data['upstreams']);
        }
        // validate the optional field `externalConnections`
        if (data['externalConnections']) { // data not null
          Array.validateJSON(data['externalConnections']);
        }
        // validate the optional field `createdTime`
        if (data['createdTime']) { // data not null
          Date.validateJSON(data['createdTime']);
        }

        return true;
    }


}



/**
 * @member {String} name
 */
UpdateRepositoryResultRepository.prototype['name'] = undefined;

/**
 * @member {String} administratorAccount
 */
UpdateRepositoryResultRepository.prototype['administratorAccount'] = undefined;

/**
 * @member {String} domainName
 */
UpdateRepositoryResultRepository.prototype['domainName'] = undefined;

/**
 * @member {String} domainOwner
 */
UpdateRepositoryResultRepository.prototype['domainOwner'] = undefined;

/**
 * @member {String} arn
 */
UpdateRepositoryResultRepository.prototype['arn'] = undefined;

/**
 * @member {String} description
 */
UpdateRepositoryResultRepository.prototype['description'] = undefined;

/**
 * @member {Array} upstreams
 */
UpdateRepositoryResultRepository.prototype['upstreams'] = undefined;

/**
 * @member {Array} externalConnections
 */
UpdateRepositoryResultRepository.prototype['externalConnections'] = undefined;

/**
 * @member {Date} createdTime
 */
UpdateRepositoryResultRepository.prototype['createdTime'] = undefined;


// Implement RepositoryDescription interface:
/**
 * @member {String} name
 */
RepositoryDescription.prototype['name'] = undefined;
/**
 * @member {String} administratorAccount
 */
RepositoryDescription.prototype['administratorAccount'] = undefined;
/**
 * @member {String} domainName
 */
RepositoryDescription.prototype['domainName'] = undefined;
/**
 * @member {String} domainOwner
 */
RepositoryDescription.prototype['domainOwner'] = undefined;
/**
 * @member {String} arn
 */
RepositoryDescription.prototype['arn'] = undefined;
/**
 * @member {String} description
 */
RepositoryDescription.prototype['description'] = undefined;
/**
 * @member {Array} upstreams
 */
RepositoryDescription.prototype['upstreams'] = undefined;
/**
 * @member {Array} externalConnections
 */
RepositoryDescription.prototype['externalConnections'] = undefined;
/**
 * @member {Date} createdTime
 */
RepositoryDescription.prototype['createdTime'] = undefined;




export default UpdateRepositoryResultRepository;

