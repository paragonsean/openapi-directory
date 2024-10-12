/*
 * CodeArtifact
 * <p> CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. </p> <p> <b>CodeArtifact Components</b> </p> <p>Use the information in this guide to help you work with the following CodeArtifact components:</p> <ul> <li> <p> <b>Repository</b>: A CodeArtifact repository contains a set of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\">package versions</a>, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <b> <code>npm</code> </b> CLI, the Maven CLI (<b> <code>mvn</code> </b>), Python CLIs (<b> <code>pip</code> </b> and <code>twine</code>), and NuGet CLIs (<code>nuget</code> and <code>dotnet</code>).</p> </li> <li> <p> <b>Domain</b>: Repositories are aggregated into a higher-level entity known as a <i>domain</i>. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it's present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in Key Management Service (KMS).</p> <p>Each repository is a member of a single domain and can't be moved to a different domain.</p> <p>The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.</p> <p>Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.</p> </li> <li> <p> <b>Package</b>: A <i>package</i> is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\">npm</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\">PyPI</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\">Maven</a>, and <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget\">NuGet</a> package formats.</p> <p>In CodeArtifact, a package consists of:</p> <ul> <li> <p>A <i>name</i> (for example, <code>webpack</code> is the name of a popular npm package)</p> </li> <li> <p>An optional namespace (for example, <code>@types</code> in <code>@types/node</code>)</p> </li> <li> <p>A set of versions (for example, <code>1.0.0</code>, <code>1.0.1</code>, <code>1.0.2</code>, etc.)</p> </li> <li> <p> Package-level metadata (for example, npm tags)</p> </li> </ul> </li> <li> <p> <b>Package version</b>: A version of a package, such as <code>@types/node 12.6.9</code>. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the <a href=\"https://semver.org/\">Semantic Versioning specification</a>. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.</p> </li> <li> <p> <b>Upstream repository</b>: One repository is <i>upstream</i> of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.</p> </li> <li> <p> <b>Asset</b>: An individual file stored in CodeArtifact associated with a package version, such as an npm <code>.tgz</code> file or Maven POM and JAR files.</p> </li> </ul> <p>CodeArtifact supports these operations:</p> <ul> <li> <p> <code>AssociateExternalConnection</code>: Adds an existing external connection to a repository. </p> </li> <li> <p> <code>CopyPackageVersions</code>: Copies package versions from one repository to another repository in the same domain.</p> </li> <li> <p> <code>CreateDomain</code>: Creates a domain</p> </li> <li> <p> <code>CreateRepository</code>: Creates a CodeArtifact repository in a domain. </p> </li> <li> <p> <code>DeleteDomain</code>: Deletes a domain. You cannot delete a domain that contains repositories. </p> </li> <li> <p> <code>DeleteDomainPermissionsPolicy</code>: Deletes the resource policy that is set on a domain.</p> </li> <li> <p> <code>DeletePackage</code>: Deletes a package and all associated package versions.</p> </li> <li> <p> <code>DeletePackageVersions</code>: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DeleteRepository</code>: Deletes a repository. </p> </li> <li> <p> <code>DeleteRepositoryPermissionsPolicy</code>: Deletes the resource policy that is set on a repository.</p> </li> <li> <p> <code>DescribeDomain</code>: Returns a <code>DomainDescription</code> object that contains information about the requested domain.</p> </li> <li> <p> <code>DescribePackage</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains details about a package. </p> </li> <li> <p> <code>DescribePackageVersion</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains details about a package version. </p> </li> <li> <p> <code>DescribeRepository</code>: Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p> </li> <li> <p> <code>DisposePackageVersions</code>: Disposes versions of a package. A package version with the status <code>Disposed</code> cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DisassociateExternalConnection</code>: Removes an existing external connection from a repository. </p> </li> <li> <p> <code>GetAuthorizationToken</code>: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.</p> </li> <li> <p> <code>GetDomainPermissionsPolicy</code>: Returns the policy of a resource that is attached to the specified domain. </p> </li> <li> <p> <code>GetPackageVersionAsset</code>: Returns the contents of an asset that is in a package version. </p> </li> <li> <p> <code>GetPackageVersionReadme</code>: Gets the readme file or descriptive text for a package version.</p> </li> <li> <p> <code>GetRepositoryEndpoint</code>: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> </ul> </li> <li> <p> <code>GetRepositoryPermissionsPolicy</code>: Returns the resource policy that is set on a repository. </p> </li> <li> <p> <code>ListDomains</code>: Returns a list of <code>DomainSummary</code> objects. Each returned <code>DomainSummary</code> object contains information about a domain.</p> </li> <li> <p> <code>ListPackages</code>: Lists the packages in a repository.</p> </li> <li> <p> <code>ListPackageVersionAssets</code>: Lists the assets for a given package version.</p> </li> <li> <p> <code>ListPackageVersionDependencies</code>: Returns a list of the direct dependencies for a package version. </p> </li> <li> <p> <code>ListPackageVersions</code>: Returns a list of package versions for a specified package in a repository.</p> </li> <li> <p> <code>ListRepositories</code>: Returns a list of repositories owned by the Amazon Web Services account that called this method.</p> </li> <li> <p> <code>ListRepositoriesInDomain</code>: Returns a list of the repositories in a domain.</p> </li> <li> <p> <code>PublishPackageVersion</code>: Creates a new package version containing one or more assets.</p> </li> <li> <p> <code>PutDomainPermissionsPolicy</code>: Attaches a resource policy to a domain.</p> </li> <li> <p> <code>PutPackageOriginConfiguration</code>: Sets the package origin configuration for a package, which determine how new versions of the package can be added to a specific repository.</p> </li> <li> <p> <code>PutRepositoryPermissionsPolicy</code>: Sets the resource policy on a repository that specifies permissions to access it. </p> </li> <li> <p> <code>UpdatePackageVersionsStatus</code>: Updates the status of one or more versions of a package.</p> </li> <li> <p> <code>UpdateRepository</code>: Updates the properties of a repository.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2018-09-22
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AssociateExternalConnectionResult;
import org.openapitools.client.model.CopyPackageVersionsRequest;
import org.openapitools.client.model.CopyPackageVersionsResult;
import org.openapitools.client.model.CreateDomainRequest;
import org.openapitools.client.model.CreateDomainResult;
import org.openapitools.client.model.CreateRepositoryRequest;
import org.openapitools.client.model.CreateRepositoryResult;
import org.openapitools.client.model.DeleteDomainPermissionsPolicyResult;
import org.openapitools.client.model.DeleteDomainResult;
import org.openapitools.client.model.DeletePackageResult;
import org.openapitools.client.model.DeletePackageVersionsRequest;
import org.openapitools.client.model.DeletePackageVersionsResult;
import org.openapitools.client.model.DeleteRepositoryPermissionsPolicyResult;
import org.openapitools.client.model.DeleteRepositoryResult;
import org.openapitools.client.model.DescribeDomainResult;
import org.openapitools.client.model.DescribePackageResult;
import org.openapitools.client.model.DescribePackageVersionResult;
import org.openapitools.client.model.DescribeRepositoryResult;
import org.openapitools.client.model.DisassociateExternalConnectionResult;
import org.openapitools.client.model.DisposePackageVersionsRequest;
import org.openapitools.client.model.DisposePackageVersionsResult;
import org.openapitools.client.model.GetAuthorizationTokenResult;
import org.openapitools.client.model.GetDomainPermissionsPolicyResult;
import org.openapitools.client.model.GetPackageVersionAssetResult;
import org.openapitools.client.model.GetPackageVersionReadmeResult;
import org.openapitools.client.model.GetRepositoryEndpointResult;
import org.openapitools.client.model.GetRepositoryPermissionsPolicyResult;
import org.openapitools.client.model.ListDomainsRequest;
import org.openapitools.client.model.ListDomainsResult;
import org.openapitools.client.model.ListPackageVersionAssetsResult;
import org.openapitools.client.model.ListPackageVersionDependenciesResult;
import org.openapitools.client.model.ListPackageVersionsResult;
import org.openapitools.client.model.ListPackagesResult;
import org.openapitools.client.model.ListRepositoriesInDomainResult;
import org.openapitools.client.model.ListRepositoriesResult;
import org.openapitools.client.model.ListTagsForResourceResult;
import org.openapitools.client.model.PublishPackageVersionRequest;
import org.openapitools.client.model.PublishPackageVersionResult;
import org.openapitools.client.model.PutDomainPermissionsPolicyRequest;
import org.openapitools.client.model.PutDomainPermissionsPolicyResult;
import org.openapitools.client.model.PutPackageOriginConfigurationRequest;
import org.openapitools.client.model.PutPackageOriginConfigurationResult;
import org.openapitools.client.model.PutRepositoryPermissionsPolicyRequest;
import org.openapitools.client.model.PutRepositoryPermissionsPolicyResult;
import org.openapitools.client.model.TagResourceRequest;
import org.openapitools.client.model.UntagResourceRequest;
import org.openapitools.client.model.UpdatePackageVersionsStatusRequest;
import org.openapitools.client.model.UpdatePackageVersionsStatusResult;
import org.openapitools.client.model.UpdateRepositoryRequest;
import org.openapitools.client.model.UpdateRepositoryResult;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * &lt;p&gt;Adds an existing external connection to a repository. One external connection is allowed per repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository can have one or more upstream repositories, or an external connection.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void associateExternalConnectionTest() throws ApiException {
        String domain = null;
        String repository = null;
        String externalConnection = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        AssociateExternalConnectionResult response = api.associateExternalConnection(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Copies package versions from one repository to another repository in the same domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void copyPackageVersionsTest() throws ApiException {
        String domain = null;
        String sourceRepository = null;
        String destinationRepository = null;
        String format = null;
        String _package = null;
        CopyPackageVersionsRequest copyPackageVersionsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        CopyPackageVersionsResult response = api.copyPackageVersions(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Creates a domain. CodeArtifact &lt;i&gt;domains&lt;/i&gt; make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it&#39;s in multiple repositories. &lt;/p&gt; &lt;p&gt;Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createDomainTest() throws ApiException {
        String domain = null;
        CreateDomainRequest createDomainRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateDomainResult response = api.createDomain(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     *  Creates a repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createRepositoryTest() throws ApiException {
        String domain = null;
        String repository = null;
        CreateRepositoryRequest createRepositoryRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        CreateRepositoryResult response = api.createRepository(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDomainTest() throws ApiException {
        String domain = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        DeleteDomainResult response = api.deleteDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Deletes the resource policy set on a domain. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDomainPermissionsPolicyTest() throws ApiException {
        String domain = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String policyRevision = null;
        DeleteDomainPermissionsPolicyResult response = api.deleteDomainPermissionsPolicy(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision);
        // TODO: test validations
    }

    /**
     * Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\&quot;&gt;DeletePackageVersions&lt;/a&gt; API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePackageTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        DeletePackageResult response = api.deletePackage(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     *  Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to &lt;code&gt;Archived&lt;/code&gt;. Archived packages cannot be downloaded from a repository and don&#39;t show up with list package APIs (for example, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt;), but you can restore them using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionsStatus&lt;/a&gt;. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePackageVersionsTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        DeletePackageVersionsRequest deletePackageVersionsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        DeletePackageVersionsResult response = api.deletePackageVersions(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     *  Deletes a repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteRepositoryTest() throws ApiException {
        String domain = null;
        String repository = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        DeleteRepositoryResult response = api.deleteRepository(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. &lt;/p&gt; &lt;important&gt; &lt;p&gt; Use &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt; with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. &lt;/p&gt; &lt;/important&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteRepositoryPermissionsPolicyTest() throws ApiException {
        String domain = null;
        String repository = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String policyRevision = null;
        DeleteRepositoryPermissionsPolicyResult response = api.deleteRepositoryPermissionsPolicy(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision);
        // TODO: test validations
    }

    /**
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\&quot;&gt;DomainDescription&lt;/a&gt; object that contains information about the requested domain. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeDomainTest() throws ApiException {
        String domain = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        DescribeDomainResult response = api.describeDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains information about the requested package.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describePackageTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        DescribePackageResult response = api.describePackage(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains information about the requested package version. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describePackageVersionTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String version = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        DescribePackageVersionResult response = api.describePackageVersion(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     *  Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeRepositoryTest() throws ApiException {
        String domain = null;
        String repository = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        DescribeRepositoryResult response = api.describeRepository(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Removes an existing external connection from a repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disassociateExternalConnectionTest() throws ApiException {
        String domain = null;
        String repository = null;
        String externalConnection = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        DisassociateExternalConnectionResult response = api.disassociateExternalConnection(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Deletes the assets in package versions and sets the package versions&#39; status to &lt;code&gt;Disposed&lt;/code&gt;. A disposed package version cannot be restored in your repository because its assets are deleted. &lt;/p&gt; &lt;p&gt; To view all disposed package versions in a repository, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt; and set the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\&quot;&gt;status&lt;/a&gt; parameter to &lt;code&gt;Disposed&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; To view information about a disposed package version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\&quot;&gt;DescribePackageVersion&lt;/a&gt;. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disposePackageVersionsTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        DisposePackageVersionsRequest disposePackageVersionsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        DisposePackageVersionsResult response = api.disposePackageVersions(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Generates a temporary authorization token for accessing repositories in the domain. This API requires the &lt;code&gt;codeartifact:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions. For more information about authorization tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\&quot;&gt;CodeArtifact authentication and tokens&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CodeArtifact authorization tokens are valid for a period of 12 hours when created with the &lt;code&gt;login&lt;/code&gt; command. You can call &lt;code&gt;login&lt;/code&gt; periodically to refresh the token. When you create an authorization token with the &lt;code&gt;GetAuthorizationToken&lt;/code&gt; API, you can set a custom authorization period, up to a maximum of 12 hours, with the &lt;code&gt;durationSeconds&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The authorization period begins after &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called. If &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call &lt;code&gt;sts assume-role&lt;/code&gt; and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.&lt;/p&gt; &lt;p&gt;See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\&quot;&gt;Using IAM Roles&lt;/a&gt; for more information on controlling session duration. &lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAuthorizationTokenTest() throws ApiException {
        String domain = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        Integer duration = null;
        GetAuthorizationTokenResult response = api.getAuthorizationToken(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Returns the resource policy attached to the specified domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; The policy is a resource-based policy, not an identity-based policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\&quot;&gt;Identity-based policies and resource-based policies &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDomainPermissionsPolicyTest() throws ApiException {
        String domain = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        GetDomainPermissionsPolicyResult response = api.getDomainPermissionsPolicy(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Returns an asset (or file) that is in a package. For example, for a Maven package version, use &lt;code&gt;GetPackageVersionAsset&lt;/code&gt; to download a &lt;code&gt;JAR&lt;/code&gt; file, a &lt;code&gt;POM&lt;/code&gt; file, or any other assets in the package version. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPackageVersionAssetTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String version = null;
        String asset = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        String revision = null;
        GetPackageVersionAssetResult response = api.getPackageVersionAsset(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Gets the readme file or descriptive text for a package version. &lt;/p&gt; &lt;p&gt; The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPackageVersionReadmeTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String version = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        GetPackageVersionReadmeResult response = api.getPackageVersionReadme(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRepositoryEndpointTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        GetRepositoryEndpointResult response = api.getRepositoryEndpoint(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Returns the resource policy that is set on a repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRepositoryPermissionsPolicyTest() throws ApiException {
        String domain = null;
        String repository = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        GetRepositoryPermissionsPolicyResult response = api.getRepositoryPermissionsPolicy(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;DomainSummary&lt;/a&gt; objects for all domains owned by the Amazon Web Services account that makes this call. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listDomainsTest() throws ApiException {
        ListDomainsRequest listDomainsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListDomainsResult response = api.listDomains(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\&quot;&gt;AssetSummary&lt;/a&gt; objects for assets in a package version. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPackageVersionAssetsTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String version = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        Integer maxResults = null;
        String nextToken = null;
        String maxResults2 = null;
        String nextToken2 = null;
        ListPackageVersionAssetsResult response = api.listPackageVersionAssets(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2);
        // TODO: test validations
    }

    /**
     *  Returns the direct dependencies for a package version. The dependencies are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\&quot;&gt;PackageDependency&lt;/a&gt; objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the &lt;code&gt;package.json&lt;/code&gt; file for npm packages and the &lt;code&gt;pom.xml&lt;/code&gt; file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPackageVersionDependenciesTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String version = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        String nextToken = null;
        ListPackageVersionDependenciesResult response = api.listPackageVersionDependencies(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken);
        // TODO: test validations
    }

    /**
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\&quot;&gt;PackageVersionSummary&lt;/a&gt; objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling &lt;code&gt;list-package-versions&lt;/code&gt; with no &lt;code&gt;--status&lt;/code&gt; parameter. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPackageVersionsTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        String status = null;
        String sortBy = null;
        Integer maxResults = null;
        String nextToken = null;
        String originType = null;
        String maxResults2 = null;
        String nextToken2 = null;
        ListPackageVersionsResult response = api.listPackageVersions(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2);
        // TODO: test validations
    }

    /**
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\&quot;&gt;PackageSummary&lt;/a&gt; objects for packages in a repository that match the request parameters. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPackagesTest() throws ApiException {
        String domain = null;
        String repository = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String format = null;
        String namespace = null;
        String packagePrefix = null;
        Integer maxResults = null;
        String nextToken = null;
        String publish = null;
        String upstream = null;
        String maxResults2 = null;
        String nextToken2 = null;
        ListPackagesResult response = api.listPackages(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2);
        // TODO: test validations
    }

    /**
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRepositoriesTest() throws ApiException {
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String repositoryPrefix = null;
        Integer maxResults = null;
        String nextToken = null;
        String maxResults2 = null;
        String nextToken2 = null;
        ListRepositoriesResult response = api.listRepositories(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2);
        // TODO: test validations
    }

    /**
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified domain and that matches the input parameters. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRepositoriesInDomainTest() throws ApiException {
        String domain = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String administratorAccount = null;
        String repositoryPrefix = null;
        Integer maxResults = null;
        String nextToken = null;
        String maxResults2 = null;
        String nextToken2 = null;
        ListRepositoriesInDomainResult response = api.listRepositoriesInDomain(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2);
        // TODO: test validations
    }

    /**
     * Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTagsForResourceTest() throws ApiException {
        String resourceArn = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        ListTagsForResourceResult response = api.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a new package version containing one or more assets (or files).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;unfinished&lt;/code&gt; flag can be used to keep the package version in the &lt;code&gt;Unfinished&lt;/code&gt; state until all of its assets have been uploaded (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact user guide&lt;/i&gt;). To set the package version’s status to &lt;code&gt;Published&lt;/code&gt;, omit the &lt;code&gt;unfinished&lt;/code&gt; flag when uploading the final asset, or set the status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionStatus&lt;/a&gt;. Once a package version’s status is set to &lt;code&gt;Published&lt;/code&gt;, it cannot change back to &lt;code&gt;Unfinished&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only generic packages can be published using this API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\&quot;&gt;Using generic packages&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void publishPackageVersionTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        String version = null;
        String asset = null;
        String xAmzContentSha257 = null;
        PublishPackageVersionRequest publishPackageVersionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        Boolean unfinished = null;
        PublishPackageVersionResult response = api.publishPackageVersion(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Sets a resource policy on a domain that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putDomainPermissionsPolicyTest() throws ApiException {
        PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutDomainPermissionsPolicyResult response = api.putDomainPermissionsPolicy(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Sets the package origin configuration for a package.&lt;/p&gt; &lt;p&gt;The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\&quot;&gt;Editing package origin controls&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt; can be called on a package that doesn&#39;t yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putPackageOriginConfigurationTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        PutPackageOriginConfigurationResult response = api.putPackageOriginConfiguration(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putRepositoryPermissionsPolicyTest() throws ApiException {
        String domain = null;
        String repository = null;
        PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        PutRepositoryPermissionsPolicyResult response = api.putRepositoryPermissionsPolicy(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

    /**
     * Adds or updates tags for a resource in CodeArtifact.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tagResourceTest() throws ApiException {
        String resourceArn = null;
        TagResourceRequest tagResourceRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes tags from a resource in CodeArtifact.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void untagResourceTest() throws ApiException {
        String resourceArn = null;
        UntagResourceRequest untagResourceRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.untagResource(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     *  Updates the status of one or more versions of a package. Using &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;, you can update the status of package versions to &lt;code&gt;Archived&lt;/code&gt;, &lt;code&gt;Published&lt;/code&gt;, or &lt;code&gt;Unlisted&lt;/code&gt;. To set the status of a package version to &lt;code&gt;Disposed&lt;/code&gt;, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\&quot;&gt;DisposePackageVersions&lt;/a&gt;. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePackageVersionsStatusTest() throws ApiException {
        String domain = null;
        String repository = null;
        String format = null;
        String _package = null;
        UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        String namespace = null;
        UpdatePackageVersionsStatusResult response = api.updatePackageVersionsStatus(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        // TODO: test validations
    }

    /**
     *  Update the properties of a repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateRepositoryTest() throws ApiException {
        String domain = null;
        String repository = null;
        UpdateRepositoryRequest updateRepositoryRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String domainOwner = null;
        UpdateRepositoryResult response = api.updateRepository(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        // TODO: test validations
    }

}
