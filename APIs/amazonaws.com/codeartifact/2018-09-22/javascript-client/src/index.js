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


import ApiClient from './ApiClient';
import AllowPublish from './model/AllowPublish';
import AllowUpstream from './model/AllowUpstream';
import AssetSummary from './model/AssetSummary';
import AssociateExternalConnectionResult from './model/AssociateExternalConnectionResult';
import AssociateExternalConnectionResultRepository from './model/AssociateExternalConnectionResultRepository';
import CopyPackageVersionsRequest from './model/CopyPackageVersionsRequest';
import CopyPackageVersionsResult from './model/CopyPackageVersionsResult';
import CreateDomainRequest from './model/CreateDomainRequest';
import CreateDomainResult from './model/CreateDomainResult';
import CreateDomainResultDomain from './model/CreateDomainResultDomain';
import CreateRepositoryRequest from './model/CreateRepositoryRequest';
import CreateRepositoryResult from './model/CreateRepositoryResult';
import CreateRepositoryResultRepository from './model/CreateRepositoryResultRepository';
import DeleteDomainPermissionsPolicyResult from './model/DeleteDomainPermissionsPolicyResult';
import DeleteDomainPermissionsPolicyResultPolicy from './model/DeleteDomainPermissionsPolicyResultPolicy';
import DeleteDomainResult from './model/DeleteDomainResult';
import DeleteDomainResultDomain from './model/DeleteDomainResultDomain';
import DeletePackageResult from './model/DeletePackageResult';
import DeletePackageVersionsRequest from './model/DeletePackageVersionsRequest';
import DeletePackageVersionsResult from './model/DeletePackageVersionsResult';
import DeleteRepositoryPermissionsPolicyResult from './model/DeleteRepositoryPermissionsPolicyResult';
import DeleteRepositoryPermissionsPolicyResultPolicy from './model/DeleteRepositoryPermissionsPolicyResultPolicy';
import DeleteRepositoryResult from './model/DeleteRepositoryResult';
import DeleteRepositoryResultRepository from './model/DeleteRepositoryResultRepository';
import DescribeDomainResult from './model/DescribeDomainResult';
import DescribePackageResult from './model/DescribePackageResult';
import DescribePackageResultPackage from './model/DescribePackageResultPackage';
import DescribePackageVersionResult from './model/DescribePackageVersionResult';
import DescribePackageVersionResultPackageVersion from './model/DescribePackageVersionResultPackageVersion';
import DescribeRepositoryResult from './model/DescribeRepositoryResult';
import DescribeRepositoryResultRepository from './model/DescribeRepositoryResultRepository';
import DisassociateExternalConnectionResult from './model/DisassociateExternalConnectionResult';
import DisassociateExternalConnectionResultRepository from './model/DisassociateExternalConnectionResultRepository';
import DisposePackageVersionsRequest from './model/DisposePackageVersionsRequest';
import DisposePackageVersionsResult from './model/DisposePackageVersionsResult';
import DomainDescription from './model/DomainDescription';
import DomainEntryPoint from './model/DomainEntryPoint';
import DomainStatus from './model/DomainStatus';
import DomainSummary from './model/DomainSummary';
import ExternalConnectionStatus from './model/ExternalConnectionStatus';
import GetAuthorizationTokenResult from './model/GetAuthorizationTokenResult';
import GetDomainPermissionsPolicyResult from './model/GetDomainPermissionsPolicyResult';
import GetDomainPermissionsPolicyResultPolicy from './model/GetDomainPermissionsPolicyResultPolicy';
import GetPackageVersionAssetResult from './model/GetPackageVersionAssetResult';
import GetPackageVersionReadmeResult from './model/GetPackageVersionReadmeResult';
import GetRepositoryEndpointResult from './model/GetRepositoryEndpointResult';
import GetRepositoryPermissionsPolicyResult from './model/GetRepositoryPermissionsPolicyResult';
import HashAlgorithm from './model/HashAlgorithm';
import LicenseInfo from './model/LicenseInfo';
import ListDomainsRequest from './model/ListDomainsRequest';
import ListDomainsResult from './model/ListDomainsResult';
import ListPackageVersionAssetsResult from './model/ListPackageVersionAssetsResult';
import ListPackageVersionDependenciesResult from './model/ListPackageVersionDependenciesResult';
import ListPackageVersionsResult from './model/ListPackageVersionsResult';
import ListPackagesResult from './model/ListPackagesResult';
import ListRepositoriesInDomainResult from './model/ListRepositoriesInDomainResult';
import ListRepositoriesResult from './model/ListRepositoriesResult';
import ListTagsForResourceResult from './model/ListTagsForResourceResult';
import PackageDependency from './model/PackageDependency';
import PackageDescription from './model/PackageDescription';
import PackageDescriptionOriginConfiguration from './model/PackageDescriptionOriginConfiguration';
import PackageFormat from './model/PackageFormat';
import PackageOriginConfiguration from './model/PackageOriginConfiguration';
import PackageOriginConfigurationRestrictions from './model/PackageOriginConfigurationRestrictions';
import PackageOriginRestrictions from './model/PackageOriginRestrictions';
import PackageSummary from './model/PackageSummary';
import PackageSummaryOriginConfiguration from './model/PackageSummaryOriginConfiguration';
import PackageVersionDescription from './model/PackageVersionDescription';
import PackageVersionDescriptionOrigin from './model/PackageVersionDescriptionOrigin';
import PackageVersionError from './model/PackageVersionError';
import PackageVersionErrorCode from './model/PackageVersionErrorCode';
import PackageVersionOrigin from './model/PackageVersionOrigin';
import PackageVersionOriginDomainEntryPoint from './model/PackageVersionOriginDomainEntryPoint';
import PackageVersionOriginType from './model/PackageVersionOriginType';
import PackageVersionSortType from './model/PackageVersionSortType';
import PackageVersionStatus from './model/PackageVersionStatus';
import PackageVersionSummary from './model/PackageVersionSummary';
import PublishPackageVersionRequest from './model/PublishPackageVersionRequest';
import PublishPackageVersionResult from './model/PublishPackageVersionResult';
import PublishPackageVersionResultAsset from './model/PublishPackageVersionResultAsset';
import PutDomainPermissionsPolicyRequest from './model/PutDomainPermissionsPolicyRequest';
import PutDomainPermissionsPolicyResult from './model/PutDomainPermissionsPolicyResult';
import PutDomainPermissionsPolicyResultPolicy from './model/PutDomainPermissionsPolicyResultPolicy';
import PutPackageOriginConfigurationRequest from './model/PutPackageOriginConfigurationRequest';
import PutPackageOriginConfigurationRequestRestrictions from './model/PutPackageOriginConfigurationRequestRestrictions';
import PutPackageOriginConfigurationResult from './model/PutPackageOriginConfigurationResult';
import PutPackageOriginConfigurationResultOriginConfiguration from './model/PutPackageOriginConfigurationResultOriginConfiguration';
import PutRepositoryPermissionsPolicyRequest from './model/PutRepositoryPermissionsPolicyRequest';
import PutRepositoryPermissionsPolicyResult from './model/PutRepositoryPermissionsPolicyResult';
import RepositoryDescription from './model/RepositoryDescription';
import RepositoryExternalConnectionInfo from './model/RepositoryExternalConnectionInfo';
import RepositorySummary from './model/RepositorySummary';
import ResourcePolicy from './model/ResourcePolicy';
import SuccessfulPackageVersionInfo from './model/SuccessfulPackageVersionInfo';
import Tag from './model/Tag';
import TagResourceRequest from './model/TagResourceRequest';
import UntagResourceRequest from './model/UntagResourceRequest';
import UpdatePackageVersionsStatusRequest from './model/UpdatePackageVersionsStatusRequest';
import UpdatePackageVersionsStatusResult from './model/UpdatePackageVersionsStatusResult';
import UpdateRepositoryRequest from './model/UpdateRepositoryRequest';
import UpdateRepositoryResult from './model/UpdateRepositoryResult';
import UpdateRepositoryResultRepository from './model/UpdateRepositoryResultRepository';
import UpstreamRepository from './model/UpstreamRepository';
import UpstreamRepositoryInfo from './model/UpstreamRepositoryInfo';
import DefaultApi from './api/DefaultApi';


/**
* &lt;p&gt; CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. &lt;/p&gt; &lt;p&gt; &lt;b&gt;CodeArtifact Components&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Use the information in this guide to help you work with the following CodeArtifact components:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Repository&lt;/b&gt;: A CodeArtifact repository contains a set of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\&quot;&gt;package versions&lt;/a&gt;, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the &lt;b&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/b&gt; CLI, the Maven CLI (&lt;b&gt; &lt;code&gt;mvn&lt;/code&gt; &lt;/b&gt;), Python CLIs (&lt;b&gt; &lt;code&gt;pip&lt;/code&gt; &lt;/b&gt; and &lt;code&gt;twine&lt;/code&gt;), and NuGet CLIs (&lt;code&gt;nuget&lt;/code&gt; and &lt;code&gt;dotnet&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Domain&lt;/b&gt;: Repositories are aggregated into a higher-level entity known as a &lt;i&gt;domain&lt;/i&gt;. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it&#39;s present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in Key Management Service (KMS).&lt;/p&gt; &lt;p&gt;Each repository is a member of a single domain and can&#39;t be moved to a different domain.&lt;/p&gt; &lt;p&gt;The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.&lt;/p&gt; &lt;p&gt;Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Package&lt;/b&gt;: A &lt;i&gt;package&lt;/i&gt; is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\&quot;&gt;npm&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\&quot;&gt;PyPI&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\&quot;&gt;Maven&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget\&quot;&gt;NuGet&lt;/a&gt; package formats.&lt;/p&gt; &lt;p&gt;In CodeArtifact, a package consists of:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;i&gt;name&lt;/i&gt; (for example, &lt;code&gt;webpack&lt;/code&gt; is the name of a popular npm package)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An optional namespace (for example, &lt;code&gt;@types&lt;/code&gt; in &lt;code&gt;@types/node&lt;/code&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A set of versions (for example, &lt;code&gt;1.0.0&lt;/code&gt;, &lt;code&gt;1.0.1&lt;/code&gt;, &lt;code&gt;1.0.2&lt;/code&gt;, etc.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Package-level metadata (for example, npm tags)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Package version&lt;/b&gt;: A version of a package, such as &lt;code&gt;@types/node 12.6.9&lt;/code&gt;. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the &lt;a href&#x3D;\&quot;https://semver.org/\&quot;&gt;Semantic Versioning specification&lt;/a&gt;. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Upstream repository&lt;/b&gt;: One repository is &lt;i&gt;upstream&lt;/i&gt; of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Asset&lt;/b&gt;: An individual file stored in CodeArtifact associated with a package version, such as an npm &lt;code&gt;.tgz&lt;/code&gt; file or Maven POM and JAR files.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;CodeArtifact supports these operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AssociateExternalConnection&lt;/code&gt;: Adds an existing external connection to a repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CopyPackageVersions&lt;/code&gt;: Copies package versions from one repository to another repository in the same domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreateDomain&lt;/code&gt;: Creates a domain&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreateRepository&lt;/code&gt;: Creates a CodeArtifact repository in a domain. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteDomain&lt;/code&gt;: Deletes a domain. You cannot delete a domain that contains repositories. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteDomainPermissionsPolicy&lt;/code&gt;: Deletes the resource policy that is set on a domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeletePackage&lt;/code&gt;: Deletes a package and all associated package versions.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeletePackageVersions&lt;/code&gt;: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteRepository&lt;/code&gt;: Deletes a repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt;: Deletes the resource policy that is set on a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeDomain&lt;/code&gt;: Returns a &lt;code&gt;DomainDescription&lt;/code&gt; object that contains information about the requested domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribePackage&lt;/code&gt;: Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains details about a package. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribePackageVersion&lt;/code&gt;: Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains details about a package version. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeRepository&lt;/code&gt;: Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DisposePackageVersions&lt;/code&gt;: Disposes versions of a package. A package version with the status &lt;code&gt;Disposed&lt;/code&gt; cannot be restored because they have been permanently removed from storage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DisassociateExternalConnection&lt;/code&gt;: Removes an existing external connection from a repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetAuthorizationToken&lt;/code&gt;: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetDomainPermissionsPolicy&lt;/code&gt;: Returns the policy of a resource that is attached to the specified domain. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetPackageVersionAsset&lt;/code&gt;: Returns the contents of an asset that is in a package version. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetPackageVersionReadme&lt;/code&gt;: Gets the readme file or descriptive text for a package version.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetRepositoryEndpoint&lt;/code&gt;: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetRepositoryPermissionsPolicy&lt;/code&gt;: Returns the resource policy that is set on a repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListDomains&lt;/code&gt;: Returns a list of &lt;code&gt;DomainSummary&lt;/code&gt; objects. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListPackages&lt;/code&gt;: Lists the packages in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListPackageVersionAssets&lt;/code&gt;: Lists the assets for a given package version.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListPackageVersionDependencies&lt;/code&gt;: Returns a list of the direct dependencies for a package version. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListPackageVersions&lt;/code&gt;: Returns a list of package versions for a specified package in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListRepositories&lt;/code&gt;: Returns a list of repositories owned by the Amazon Web Services account that called this method.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListRepositoriesInDomain&lt;/code&gt;: Returns a list of the repositories in a domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PublishPackageVersion&lt;/code&gt;: Creates a new package version containing one or more assets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;: Attaches a resource policy to a domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt;: Sets the package origin configuration for a package, which determine how new versions of the package can be added to a specific repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;: Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;: Updates the status of one or more versions of a package.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdateRepository&lt;/code&gt;: Updates the properties of a repository.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var CodeArtifact = require('index'); // See note below*.
* var xxxSvc = new CodeArtifact.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new CodeArtifact.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new CodeArtifact.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new CodeArtifact.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2018-09-22
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AllowPublish model constructor.
     * @property {module:model/AllowPublish}
     */
    AllowPublish,

    /**
     * The AllowUpstream model constructor.
     * @property {module:model/AllowUpstream}
     */
    AllowUpstream,

    /**
     * The AssetSummary model constructor.
     * @property {module:model/AssetSummary}
     */
    AssetSummary,

    /**
     * The AssociateExternalConnectionResult model constructor.
     * @property {module:model/AssociateExternalConnectionResult}
     */
    AssociateExternalConnectionResult,

    /**
     * The AssociateExternalConnectionResultRepository model constructor.
     * @property {module:model/AssociateExternalConnectionResultRepository}
     */
    AssociateExternalConnectionResultRepository,

    /**
     * The CopyPackageVersionsRequest model constructor.
     * @property {module:model/CopyPackageVersionsRequest}
     */
    CopyPackageVersionsRequest,

    /**
     * The CopyPackageVersionsResult model constructor.
     * @property {module:model/CopyPackageVersionsResult}
     */
    CopyPackageVersionsResult,

    /**
     * The CreateDomainRequest model constructor.
     * @property {module:model/CreateDomainRequest}
     */
    CreateDomainRequest,

    /**
     * The CreateDomainResult model constructor.
     * @property {module:model/CreateDomainResult}
     */
    CreateDomainResult,

    /**
     * The CreateDomainResultDomain model constructor.
     * @property {module:model/CreateDomainResultDomain}
     */
    CreateDomainResultDomain,

    /**
     * The CreateRepositoryRequest model constructor.
     * @property {module:model/CreateRepositoryRequest}
     */
    CreateRepositoryRequest,

    /**
     * The CreateRepositoryResult model constructor.
     * @property {module:model/CreateRepositoryResult}
     */
    CreateRepositoryResult,

    /**
     * The CreateRepositoryResultRepository model constructor.
     * @property {module:model/CreateRepositoryResultRepository}
     */
    CreateRepositoryResultRepository,

    /**
     * The DeleteDomainPermissionsPolicyResult model constructor.
     * @property {module:model/DeleteDomainPermissionsPolicyResult}
     */
    DeleteDomainPermissionsPolicyResult,

    /**
     * The DeleteDomainPermissionsPolicyResultPolicy model constructor.
     * @property {module:model/DeleteDomainPermissionsPolicyResultPolicy}
     */
    DeleteDomainPermissionsPolicyResultPolicy,

    /**
     * The DeleteDomainResult model constructor.
     * @property {module:model/DeleteDomainResult}
     */
    DeleteDomainResult,

    /**
     * The DeleteDomainResultDomain model constructor.
     * @property {module:model/DeleteDomainResultDomain}
     */
    DeleteDomainResultDomain,

    /**
     * The DeletePackageResult model constructor.
     * @property {module:model/DeletePackageResult}
     */
    DeletePackageResult,

    /**
     * The DeletePackageVersionsRequest model constructor.
     * @property {module:model/DeletePackageVersionsRequest}
     */
    DeletePackageVersionsRequest,

    /**
     * The DeletePackageVersionsResult model constructor.
     * @property {module:model/DeletePackageVersionsResult}
     */
    DeletePackageVersionsResult,

    /**
     * The DeleteRepositoryPermissionsPolicyResult model constructor.
     * @property {module:model/DeleteRepositoryPermissionsPolicyResult}
     */
    DeleteRepositoryPermissionsPolicyResult,

    /**
     * The DeleteRepositoryPermissionsPolicyResultPolicy model constructor.
     * @property {module:model/DeleteRepositoryPermissionsPolicyResultPolicy}
     */
    DeleteRepositoryPermissionsPolicyResultPolicy,

    /**
     * The DeleteRepositoryResult model constructor.
     * @property {module:model/DeleteRepositoryResult}
     */
    DeleteRepositoryResult,

    /**
     * The DeleteRepositoryResultRepository model constructor.
     * @property {module:model/DeleteRepositoryResultRepository}
     */
    DeleteRepositoryResultRepository,

    /**
     * The DescribeDomainResult model constructor.
     * @property {module:model/DescribeDomainResult}
     */
    DescribeDomainResult,

    /**
     * The DescribePackageResult model constructor.
     * @property {module:model/DescribePackageResult}
     */
    DescribePackageResult,

    /**
     * The DescribePackageResultPackage model constructor.
     * @property {module:model/DescribePackageResultPackage}
     */
    DescribePackageResultPackage,

    /**
     * The DescribePackageVersionResult model constructor.
     * @property {module:model/DescribePackageVersionResult}
     */
    DescribePackageVersionResult,

    /**
     * The DescribePackageVersionResultPackageVersion model constructor.
     * @property {module:model/DescribePackageVersionResultPackageVersion}
     */
    DescribePackageVersionResultPackageVersion,

    /**
     * The DescribeRepositoryResult model constructor.
     * @property {module:model/DescribeRepositoryResult}
     */
    DescribeRepositoryResult,

    /**
     * The DescribeRepositoryResultRepository model constructor.
     * @property {module:model/DescribeRepositoryResultRepository}
     */
    DescribeRepositoryResultRepository,

    /**
     * The DisassociateExternalConnectionResult model constructor.
     * @property {module:model/DisassociateExternalConnectionResult}
     */
    DisassociateExternalConnectionResult,

    /**
     * The DisassociateExternalConnectionResultRepository model constructor.
     * @property {module:model/DisassociateExternalConnectionResultRepository}
     */
    DisassociateExternalConnectionResultRepository,

    /**
     * The DisposePackageVersionsRequest model constructor.
     * @property {module:model/DisposePackageVersionsRequest}
     */
    DisposePackageVersionsRequest,

    /**
     * The DisposePackageVersionsResult model constructor.
     * @property {module:model/DisposePackageVersionsResult}
     */
    DisposePackageVersionsResult,

    /**
     * The DomainDescription model constructor.
     * @property {module:model/DomainDescription}
     */
    DomainDescription,

    /**
     * The DomainEntryPoint model constructor.
     * @property {module:model/DomainEntryPoint}
     */
    DomainEntryPoint,

    /**
     * The DomainStatus model constructor.
     * @property {module:model/DomainStatus}
     */
    DomainStatus,

    /**
     * The DomainSummary model constructor.
     * @property {module:model/DomainSummary}
     */
    DomainSummary,

    /**
     * The ExternalConnectionStatus model constructor.
     * @property {module:model/ExternalConnectionStatus}
     */
    ExternalConnectionStatus,

    /**
     * The GetAuthorizationTokenResult model constructor.
     * @property {module:model/GetAuthorizationTokenResult}
     */
    GetAuthorizationTokenResult,

    /**
     * The GetDomainPermissionsPolicyResult model constructor.
     * @property {module:model/GetDomainPermissionsPolicyResult}
     */
    GetDomainPermissionsPolicyResult,

    /**
     * The GetDomainPermissionsPolicyResultPolicy model constructor.
     * @property {module:model/GetDomainPermissionsPolicyResultPolicy}
     */
    GetDomainPermissionsPolicyResultPolicy,

    /**
     * The GetPackageVersionAssetResult model constructor.
     * @property {module:model/GetPackageVersionAssetResult}
     */
    GetPackageVersionAssetResult,

    /**
     * The GetPackageVersionReadmeResult model constructor.
     * @property {module:model/GetPackageVersionReadmeResult}
     */
    GetPackageVersionReadmeResult,

    /**
     * The GetRepositoryEndpointResult model constructor.
     * @property {module:model/GetRepositoryEndpointResult}
     */
    GetRepositoryEndpointResult,

    /**
     * The GetRepositoryPermissionsPolicyResult model constructor.
     * @property {module:model/GetRepositoryPermissionsPolicyResult}
     */
    GetRepositoryPermissionsPolicyResult,

    /**
     * The HashAlgorithm model constructor.
     * @property {module:model/HashAlgorithm}
     */
    HashAlgorithm,

    /**
     * The LicenseInfo model constructor.
     * @property {module:model/LicenseInfo}
     */
    LicenseInfo,

    /**
     * The ListDomainsRequest model constructor.
     * @property {module:model/ListDomainsRequest}
     */
    ListDomainsRequest,

    /**
     * The ListDomainsResult model constructor.
     * @property {module:model/ListDomainsResult}
     */
    ListDomainsResult,

    /**
     * The ListPackageVersionAssetsResult model constructor.
     * @property {module:model/ListPackageVersionAssetsResult}
     */
    ListPackageVersionAssetsResult,

    /**
     * The ListPackageVersionDependenciesResult model constructor.
     * @property {module:model/ListPackageVersionDependenciesResult}
     */
    ListPackageVersionDependenciesResult,

    /**
     * The ListPackageVersionsResult model constructor.
     * @property {module:model/ListPackageVersionsResult}
     */
    ListPackageVersionsResult,

    /**
     * The ListPackagesResult model constructor.
     * @property {module:model/ListPackagesResult}
     */
    ListPackagesResult,

    /**
     * The ListRepositoriesInDomainResult model constructor.
     * @property {module:model/ListRepositoriesInDomainResult}
     */
    ListRepositoriesInDomainResult,

    /**
     * The ListRepositoriesResult model constructor.
     * @property {module:model/ListRepositoriesResult}
     */
    ListRepositoriesResult,

    /**
     * The ListTagsForResourceResult model constructor.
     * @property {module:model/ListTagsForResourceResult}
     */
    ListTagsForResourceResult,

    /**
     * The PackageDependency model constructor.
     * @property {module:model/PackageDependency}
     */
    PackageDependency,

    /**
     * The PackageDescription model constructor.
     * @property {module:model/PackageDescription}
     */
    PackageDescription,

    /**
     * The PackageDescriptionOriginConfiguration model constructor.
     * @property {module:model/PackageDescriptionOriginConfiguration}
     */
    PackageDescriptionOriginConfiguration,

    /**
     * The PackageFormat model constructor.
     * @property {module:model/PackageFormat}
     */
    PackageFormat,

    /**
     * The PackageOriginConfiguration model constructor.
     * @property {module:model/PackageOriginConfiguration}
     */
    PackageOriginConfiguration,

    /**
     * The PackageOriginConfigurationRestrictions model constructor.
     * @property {module:model/PackageOriginConfigurationRestrictions}
     */
    PackageOriginConfigurationRestrictions,

    /**
     * The PackageOriginRestrictions model constructor.
     * @property {module:model/PackageOriginRestrictions}
     */
    PackageOriginRestrictions,

    /**
     * The PackageSummary model constructor.
     * @property {module:model/PackageSummary}
     */
    PackageSummary,

    /**
     * The PackageSummaryOriginConfiguration model constructor.
     * @property {module:model/PackageSummaryOriginConfiguration}
     */
    PackageSummaryOriginConfiguration,

    /**
     * The PackageVersionDescription model constructor.
     * @property {module:model/PackageVersionDescription}
     */
    PackageVersionDescription,

    /**
     * The PackageVersionDescriptionOrigin model constructor.
     * @property {module:model/PackageVersionDescriptionOrigin}
     */
    PackageVersionDescriptionOrigin,

    /**
     * The PackageVersionError model constructor.
     * @property {module:model/PackageVersionError}
     */
    PackageVersionError,

    /**
     * The PackageVersionErrorCode model constructor.
     * @property {module:model/PackageVersionErrorCode}
     */
    PackageVersionErrorCode,

    /**
     * The PackageVersionOrigin model constructor.
     * @property {module:model/PackageVersionOrigin}
     */
    PackageVersionOrigin,

    /**
     * The PackageVersionOriginDomainEntryPoint model constructor.
     * @property {module:model/PackageVersionOriginDomainEntryPoint}
     */
    PackageVersionOriginDomainEntryPoint,

    /**
     * The PackageVersionOriginType model constructor.
     * @property {module:model/PackageVersionOriginType}
     */
    PackageVersionOriginType,

    /**
     * The PackageVersionSortType model constructor.
     * @property {module:model/PackageVersionSortType}
     */
    PackageVersionSortType,

    /**
     * The PackageVersionStatus model constructor.
     * @property {module:model/PackageVersionStatus}
     */
    PackageVersionStatus,

    /**
     * The PackageVersionSummary model constructor.
     * @property {module:model/PackageVersionSummary}
     */
    PackageVersionSummary,

    /**
     * The PublishPackageVersionRequest model constructor.
     * @property {module:model/PublishPackageVersionRequest}
     */
    PublishPackageVersionRequest,

    /**
     * The PublishPackageVersionResult model constructor.
     * @property {module:model/PublishPackageVersionResult}
     */
    PublishPackageVersionResult,

    /**
     * The PublishPackageVersionResultAsset model constructor.
     * @property {module:model/PublishPackageVersionResultAsset}
     */
    PublishPackageVersionResultAsset,

    /**
     * The PutDomainPermissionsPolicyRequest model constructor.
     * @property {module:model/PutDomainPermissionsPolicyRequest}
     */
    PutDomainPermissionsPolicyRequest,

    /**
     * The PutDomainPermissionsPolicyResult model constructor.
     * @property {module:model/PutDomainPermissionsPolicyResult}
     */
    PutDomainPermissionsPolicyResult,

    /**
     * The PutDomainPermissionsPolicyResultPolicy model constructor.
     * @property {module:model/PutDomainPermissionsPolicyResultPolicy}
     */
    PutDomainPermissionsPolicyResultPolicy,

    /**
     * The PutPackageOriginConfigurationRequest model constructor.
     * @property {module:model/PutPackageOriginConfigurationRequest}
     */
    PutPackageOriginConfigurationRequest,

    /**
     * The PutPackageOriginConfigurationRequestRestrictions model constructor.
     * @property {module:model/PutPackageOriginConfigurationRequestRestrictions}
     */
    PutPackageOriginConfigurationRequestRestrictions,

    /**
     * The PutPackageOriginConfigurationResult model constructor.
     * @property {module:model/PutPackageOriginConfigurationResult}
     */
    PutPackageOriginConfigurationResult,

    /**
     * The PutPackageOriginConfigurationResultOriginConfiguration model constructor.
     * @property {module:model/PutPackageOriginConfigurationResultOriginConfiguration}
     */
    PutPackageOriginConfigurationResultOriginConfiguration,

    /**
     * The PutRepositoryPermissionsPolicyRequest model constructor.
     * @property {module:model/PutRepositoryPermissionsPolicyRequest}
     */
    PutRepositoryPermissionsPolicyRequest,

    /**
     * The PutRepositoryPermissionsPolicyResult model constructor.
     * @property {module:model/PutRepositoryPermissionsPolicyResult}
     */
    PutRepositoryPermissionsPolicyResult,

    /**
     * The RepositoryDescription model constructor.
     * @property {module:model/RepositoryDescription}
     */
    RepositoryDescription,

    /**
     * The RepositoryExternalConnectionInfo model constructor.
     * @property {module:model/RepositoryExternalConnectionInfo}
     */
    RepositoryExternalConnectionInfo,

    /**
     * The RepositorySummary model constructor.
     * @property {module:model/RepositorySummary}
     */
    RepositorySummary,

    /**
     * The ResourcePolicy model constructor.
     * @property {module:model/ResourcePolicy}
     */
    ResourcePolicy,

    /**
     * The SuccessfulPackageVersionInfo model constructor.
     * @property {module:model/SuccessfulPackageVersionInfo}
     */
    SuccessfulPackageVersionInfo,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TagResourceRequest model constructor.
     * @property {module:model/TagResourceRequest}
     */
    TagResourceRequest,

    /**
     * The UntagResourceRequest model constructor.
     * @property {module:model/UntagResourceRequest}
     */
    UntagResourceRequest,

    /**
     * The UpdatePackageVersionsStatusRequest model constructor.
     * @property {module:model/UpdatePackageVersionsStatusRequest}
     */
    UpdatePackageVersionsStatusRequest,

    /**
     * The UpdatePackageVersionsStatusResult model constructor.
     * @property {module:model/UpdatePackageVersionsStatusResult}
     */
    UpdatePackageVersionsStatusResult,

    /**
     * The UpdateRepositoryRequest model constructor.
     * @property {module:model/UpdateRepositoryRequest}
     */
    UpdateRepositoryRequest,

    /**
     * The UpdateRepositoryResult model constructor.
     * @property {module:model/UpdateRepositoryResult}
     */
    UpdateRepositoryResult,

    /**
     * The UpdateRepositoryResultRepository model constructor.
     * @property {module:model/UpdateRepositoryResultRepository}
     */
    UpdateRepositoryResultRepository,

    /**
     * The UpstreamRepository model constructor.
     * @property {module:model/UpstreamRepository}
     */
    UpstreamRepository,

    /**
     * The UpstreamRepositoryInfo model constructor.
     * @property {module:model/UpstreamRepositoryInfo}
     */
    UpstreamRepositoryInfo,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
