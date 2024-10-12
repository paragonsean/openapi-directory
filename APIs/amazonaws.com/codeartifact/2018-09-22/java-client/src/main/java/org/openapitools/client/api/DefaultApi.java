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

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


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

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for associateExternalConnection
     * @param domain The name of the domain that contains the repository. (required)
     * @param repository  The name of the repository to which the external connection is added.  (required)
     * @param externalConnection &lt;p&gt; The name of the external connection to add to the repository. The following values are supported: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:npmjs&lt;/code&gt; - for the npm public repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:nuget-org&lt;/code&gt; - for the NuGet Gallery. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:pypi&lt;/code&gt; - for the Python Package Index. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-central&lt;/code&gt; - for Maven Central. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-googleandroid&lt;/code&gt; - for the Google Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-gradleplugins&lt;/code&gt; - for the Gradle plugins repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-commonsware&lt;/code&gt; - for the CommonsWare Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-clojars&lt;/code&gt; - for the Clojars repository. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call associateExternalConnectionCall(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository/external-connection#domain&repository&external-connection";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (externalConnection != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("external-connection", externalConnection));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call associateExternalConnectionValidateBeforeCall(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling associateExternalConnection(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling associateExternalConnection(Async)");
        }

        // verify the required parameter 'externalConnection' is set
        if (externalConnection == null) {
            throw new ApiException("Missing the required parameter 'externalConnection' when calling associateExternalConnection(Async)");
        }

        return associateExternalConnectionCall(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     * &lt;p&gt;Adds an existing external connection to a repository. One external connection is allowed per repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository can have one or more upstream repositories, or an external connection.&lt;/p&gt; &lt;/note&gt;
     * @param domain The name of the domain that contains the repository. (required)
     * @param repository  The name of the repository to which the external connection is added.  (required)
     * @param externalConnection &lt;p&gt; The name of the external connection to add to the repository. The following values are supported: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:npmjs&lt;/code&gt; - for the npm public repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:nuget-org&lt;/code&gt; - for the NuGet Gallery. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:pypi&lt;/code&gt; - for the Python Package Index. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-central&lt;/code&gt; - for Maven Central. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-googleandroid&lt;/code&gt; - for the Google Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-gradleplugins&lt;/code&gt; - for the Gradle plugins repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-commonsware&lt;/code&gt; - for the CommonsWare Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-clojars&lt;/code&gt; - for the Clojars repository. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return AssociateExternalConnectionResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public AssociateExternalConnectionResult associateExternalConnection(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<AssociateExternalConnectionResult> localVarResp = associateExternalConnectionWithHttpInfo(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Adds an existing external connection to a repository. One external connection is allowed per repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository can have one or more upstream repositories, or an external connection.&lt;/p&gt; &lt;/note&gt;
     * @param domain The name of the domain that contains the repository. (required)
     * @param repository  The name of the repository to which the external connection is added.  (required)
     * @param externalConnection &lt;p&gt; The name of the external connection to add to the repository. The following values are supported: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:npmjs&lt;/code&gt; - for the npm public repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:nuget-org&lt;/code&gt; - for the NuGet Gallery. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:pypi&lt;/code&gt; - for the Python Package Index. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-central&lt;/code&gt; - for Maven Central. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-googleandroid&lt;/code&gt; - for the Google Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-gradleplugins&lt;/code&gt; - for the Gradle plugins repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-commonsware&lt;/code&gt; - for the CommonsWare Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-clojars&lt;/code&gt; - for the Clojars repository. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;AssociateExternalConnectionResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AssociateExternalConnectionResult> associateExternalConnectionWithHttpInfo(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = associateExternalConnectionValidateBeforeCall(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<AssociateExternalConnectionResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Adds an existing external connection to a repository. One external connection is allowed per repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository can have one or more upstream repositories, or an external connection.&lt;/p&gt; &lt;/note&gt;
     * @param domain The name of the domain that contains the repository. (required)
     * @param repository  The name of the repository to which the external connection is added.  (required)
     * @param externalConnection &lt;p&gt; The name of the external connection to add to the repository. The following values are supported: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:npmjs&lt;/code&gt; - for the npm public repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:nuget-org&lt;/code&gt; - for the NuGet Gallery. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:pypi&lt;/code&gt; - for the Python Package Index. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-central&lt;/code&gt; - for Maven Central. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-googleandroid&lt;/code&gt; - for the Google Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-gradleplugins&lt;/code&gt; - for the Gradle plugins repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-commonsware&lt;/code&gt; - for the CommonsWare Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-clojars&lt;/code&gt; - for the Clojars repository. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call associateExternalConnectionAsync(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<AssociateExternalConnectionResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = associateExternalConnectionValidateBeforeCall(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<AssociateExternalConnectionResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for copyPackageVersions
     * @param domain  The name of the domain that contains the source and destination repositories.  (required)
     * @param sourceRepository  The name of the repository that contains the package versions to be copied.  (required)
     * @param destinationRepository  The name of the repository into which package versions are copied.  (required)
     * @param format  The format of the package versions to be copied.  (required)
     * @param _package  The name of the package that contains the versions to be copied.  (required)
     * @param copyPackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when copying Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call copyPackageVersionsCall(String domain, String sourceRepository, String destinationRepository, String format, String _package, CopyPackageVersionsRequest copyPackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = copyPackageVersionsRequest;

        // create path and map variables
        String localVarPath = "/v1/package/versions/copy#domain&source-repository&destination-repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (sourceRepository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("source-repository", sourceRepository));
        }

        if (destinationRepository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("destination-repository", destinationRepository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call copyPackageVersionsValidateBeforeCall(String domain, String sourceRepository, String destinationRepository, String format, String _package, CopyPackageVersionsRequest copyPackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling copyPackageVersions(Async)");
        }

        // verify the required parameter 'sourceRepository' is set
        if (sourceRepository == null) {
            throw new ApiException("Missing the required parameter 'sourceRepository' when calling copyPackageVersions(Async)");
        }

        // verify the required parameter 'destinationRepository' is set
        if (destinationRepository == null) {
            throw new ApiException("Missing the required parameter 'destinationRepository' when calling copyPackageVersions(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling copyPackageVersions(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling copyPackageVersions(Async)");
        }

        // verify the required parameter 'copyPackageVersionsRequest' is set
        if (copyPackageVersionsRequest == null) {
            throw new ApiException("Missing the required parameter 'copyPackageVersionsRequest' when calling copyPackageVersions(Async)");
        }

        return copyPackageVersionsCall(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     * &lt;p&gt; Copies package versions from one repository to another repository in the same domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain that contains the source and destination repositories.  (required)
     * @param sourceRepository  The name of the repository that contains the package versions to be copied.  (required)
     * @param destinationRepository  The name of the repository into which package versions are copied.  (required)
     * @param format  The format of the package versions to be copied.  (required)
     * @param _package  The name of the package that contains the versions to be copied.  (required)
     * @param copyPackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when copying Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return CopyPackageVersionsResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public CopyPackageVersionsResult copyPackageVersions(String domain, String sourceRepository, String destinationRepository, String format, String _package, CopyPackageVersionsRequest copyPackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<CopyPackageVersionsResult> localVarResp = copyPackageVersionsWithHttpInfo(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Copies package versions from one repository to another repository in the same domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain that contains the source and destination repositories.  (required)
     * @param sourceRepository  The name of the repository that contains the package versions to be copied.  (required)
     * @param destinationRepository  The name of the repository into which package versions are copied.  (required)
     * @param format  The format of the package versions to be copied.  (required)
     * @param _package  The name of the package that contains the versions to be copied.  (required)
     * @param copyPackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when copying Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;CopyPackageVersionsResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CopyPackageVersionsResult> copyPackageVersionsWithHttpInfo(String domain, String sourceRepository, String destinationRepository, String format, String _package, CopyPackageVersionsRequest copyPackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = copyPackageVersionsValidateBeforeCall(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<CopyPackageVersionsResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Copies package versions from one repository to another repository in the same domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain that contains the source and destination repositories.  (required)
     * @param sourceRepository  The name of the repository that contains the package versions to be copied.  (required)
     * @param destinationRepository  The name of the repository into which package versions are copied.  (required)
     * @param format  The format of the package versions to be copied.  (required)
     * @param _package  The name of the package that contains the versions to be copied.  (required)
     * @param copyPackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when copying Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call copyPackageVersionsAsync(String domain, String sourceRepository, String destinationRepository, String format, String _package, CopyPackageVersionsRequest copyPackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<CopyPackageVersionsResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = copyPackageVersionsValidateBeforeCall(domain, sourceRepository, destinationRepository, format, _package, copyPackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<CopyPackageVersionsResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createDomain
     * @param domain  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable.  (required)
     * @param createDomainRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDomainCall(String domain, CreateDomainRequest createDomainRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createDomainRequest;

        // create path and map variables
        String localVarPath = "/v1/domain#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createDomainValidateBeforeCall(String domain, CreateDomainRequest createDomainRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling createDomain(Async)");
        }

        // verify the required parameter 'createDomainRequest' is set
        if (createDomainRequest == null) {
            throw new ApiException("Missing the required parameter 'createDomainRequest' when calling createDomain(Async)");
        }

        return createDomainCall(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt; Creates a domain. CodeArtifact &lt;i&gt;domains&lt;/i&gt; make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it&#39;s in multiple repositories. &lt;/p&gt; &lt;p&gt;Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. &lt;/p&gt;
     * @param domain  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable.  (required)
     * @param createDomainRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateDomainResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public CreateDomainResult createDomain(String domain, CreateDomainRequest createDomainRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateDomainResult> localVarResp = createDomainWithHttpInfo(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Creates a domain. CodeArtifact &lt;i&gt;domains&lt;/i&gt; make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it&#39;s in multiple repositories. &lt;/p&gt; &lt;p&gt;Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. &lt;/p&gt;
     * @param domain  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable.  (required)
     * @param createDomainRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateDomainResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateDomainResult> createDomainWithHttpInfo(String domain, CreateDomainRequest createDomainRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createDomainValidateBeforeCall(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateDomainResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Creates a domain. CodeArtifact &lt;i&gt;domains&lt;/i&gt; make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it&#39;s in multiple repositories. &lt;/p&gt; &lt;p&gt;Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. &lt;/p&gt;
     * @param domain  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable.  (required)
     * @param createDomainRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDomainAsync(String domain, CreateDomainRequest createDomainRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateDomainResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = createDomainValidateBeforeCall(domain, createDomainRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateDomainResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createRepository
     * @param domain  The name of the domain that contains the created repository.  (required)
     * @param repository  The name of the repository to create.  (required)
     * @param createRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRepositoryCall(String domain, String repository, CreateRepositoryRequest createRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createRepositoryRequest;

        // create path and map variables
        String localVarPath = "/v1/repository#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createRepositoryValidateBeforeCall(String domain, String repository, CreateRepositoryRequest createRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling createRepository(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling createRepository(Async)");
        }

        // verify the required parameter 'createRepositoryRequest' is set
        if (createRepositoryRequest == null) {
            throw new ApiException("Missing the required parameter 'createRepositoryRequest' when calling createRepository(Async)");
        }

        return createRepositoryCall(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Creates a repository. 
     * @param domain  The name of the domain that contains the created repository.  (required)
     * @param repository  The name of the repository to create.  (required)
     * @param createRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return CreateRepositoryResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public CreateRepositoryResult createRepository(String domain, String repository, CreateRepositoryRequest createRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<CreateRepositoryResult> localVarResp = createRepositoryWithHttpInfo(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Creates a repository. 
     * @param domain  The name of the domain that contains the created repository.  (required)
     * @param repository  The name of the repository to create.  (required)
     * @param createRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;CreateRepositoryResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateRepositoryResult> createRepositoryWithHttpInfo(String domain, String repository, CreateRepositoryRequest createRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = createRepositoryValidateBeforeCall(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<CreateRepositoryResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Creates a repository. 
     * @param domain  The name of the domain that contains the created repository.  (required)
     * @param repository  The name of the repository to create.  (required)
     * @param createRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRepositoryAsync(String domain, String repository, CreateRepositoryRequest createRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<CreateRepositoryResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = createRepositoryValidateBeforeCall(domain, repository, createRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<CreateRepositoryResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDomain
     * @param domain  The name of the domain to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/domain#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDomainValidateBeforeCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling deleteDomain(Async)");
        }

        return deleteDomainCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 
     * @param domain  The name of the domain to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return DeleteDomainResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteDomainResult deleteDomain(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<DeleteDomainResult> localVarResp = deleteDomainWithHttpInfo(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 
     * @param domain  The name of the domain to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;DeleteDomainResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteDomainResult> deleteDomainWithHttpInfo(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = deleteDomainValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<DeleteDomainResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 
     * @param domain  The name of the domain to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainAsync(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<DeleteDomainResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDomainValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<DeleteDomainResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDomainPermissionsPolicy
     * @param domain  The name of the domain associated with the resource policy to be deleted.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainPermissionsPolicyCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/domain/permissions/policy#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (policyRevision != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("policy-revision", policyRevision));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDomainPermissionsPolicyValidateBeforeCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling deleteDomainPermissionsPolicy(Async)");
        }

        return deleteDomainPermissionsPolicyCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision, _callback);

    }

    /**
     * 
     *  Deletes the resource policy set on a domain. 
     * @param domain  The name of the domain associated with the resource policy to be deleted.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy.  (optional)
     * @return DeleteDomainPermissionsPolicyResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteDomainPermissionsPolicyResult deleteDomainPermissionsPolicy(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision) throws ApiException {
        ApiResponse<DeleteDomainPermissionsPolicyResult> localVarResp = deleteDomainPermissionsPolicyWithHttpInfo(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision);
        return localVarResp.getData();
    }

    /**
     * 
     *  Deletes the resource policy set on a domain. 
     * @param domain  The name of the domain associated with the resource policy to be deleted.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy.  (optional)
     * @return ApiResponse&lt;DeleteDomainPermissionsPolicyResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteDomainPermissionsPolicyResult> deleteDomainPermissionsPolicyWithHttpInfo(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision) throws ApiException {
        okhttp3.Call localVarCall = deleteDomainPermissionsPolicyValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision, null);
        Type localVarReturnType = new TypeToken<DeleteDomainPermissionsPolicyResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Deletes the resource policy set on a domain. 
     * @param domain  The name of the domain associated with the resource policy to be deleted.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainPermissionsPolicyAsync(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision, final ApiCallback<DeleteDomainPermissionsPolicyResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDomainPermissionsPolicyValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision, _callback);
        Type localVarReturnType = new TypeToken<DeleteDomainPermissionsPolicyResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deletePackage
     * @param domain The name of the domain that contains the package to delete. (required)
     * @param repository The name of the repository that contains the package to delete. (required)
     * @param format The format of the requested package to delete. (required)
     * @param _package The name of the package to delete. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePackageCall(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deletePackageValidateBeforeCall(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling deletePackage(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling deletePackage(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling deletePackage(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling deletePackage(Async)");
        }

        return deletePackageCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     * Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\&quot;&gt;DeletePackageVersions&lt;/a&gt; API.
     * @param domain The name of the domain that contains the package to delete. (required)
     * @param repository The name of the repository that contains the package to delete. (required)
     * @param format The format of the requested package to delete. (required)
     * @param _package The name of the package to delete. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return DeletePackageResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeletePackageResult deletePackage(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<DeletePackageResult> localVarResp = deletePackageWithHttpInfo(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     * Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\&quot;&gt;DeletePackageVersions&lt;/a&gt; API.
     * @param domain The name of the domain that contains the package to delete. (required)
     * @param repository The name of the repository that contains the package to delete. (required)
     * @param format The format of the requested package to delete. (required)
     * @param _package The name of the package to delete. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;DeletePackageResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeletePackageResult> deletePackageWithHttpInfo(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = deletePackageValidateBeforeCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<DeletePackageResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\&quot;&gt;DeletePackageVersions&lt;/a&gt; API.
     * @param domain The name of the domain that contains the package to delete. (required)
     * @param repository The name of the repository that contains the package to delete. (required)
     * @param format The format of the requested package to delete. (required)
     * @param _package The name of the package to delete. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePackageAsync(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<DeletePackageResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = deletePackageValidateBeforeCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<DeletePackageResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deletePackageVersions
     * @param domain  The name of the domain that contains the package to delete.  (required)
     * @param repository  The name of the repository that contains the package versions to delete.  (required)
     * @param format  The format of the package versions to delete.  (required)
     * @param _package  The name of the package with the versions to delete.  (required)
     * @param deletePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePackageVersionsCall(String domain, String repository, String format, String _package, DeletePackageVersionsRequest deletePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deletePackageVersionsRequest;

        // create path and map variables
        String localVarPath = "/v1/package/versions/delete#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deletePackageVersionsValidateBeforeCall(String domain, String repository, String format, String _package, DeletePackageVersionsRequest deletePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling deletePackageVersions(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling deletePackageVersions(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling deletePackageVersions(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling deletePackageVersions(Async)");
        }

        // verify the required parameter 'deletePackageVersionsRequest' is set
        if (deletePackageVersionsRequest == null) {
            throw new ApiException("Missing the required parameter 'deletePackageVersionsRequest' when calling deletePackageVersions(Async)");
        }

        return deletePackageVersionsCall(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     *  Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to &lt;code&gt;Archived&lt;/code&gt;. Archived packages cannot be downloaded from a repository and don&#39;t show up with list package APIs (for example, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt;), but you can restore them using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionsStatus&lt;/a&gt;. 
     * @param domain  The name of the domain that contains the package to delete.  (required)
     * @param repository  The name of the repository that contains the package versions to delete.  (required)
     * @param format  The format of the package versions to delete.  (required)
     * @param _package  The name of the package with the versions to delete.  (required)
     * @param deletePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return DeletePackageVersionsResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeletePackageVersionsResult deletePackageVersions(String domain, String repository, String format, String _package, DeletePackageVersionsRequest deletePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<DeletePackageVersionsResult> localVarResp = deletePackageVersionsWithHttpInfo(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     *  Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to &lt;code&gt;Archived&lt;/code&gt;. Archived packages cannot be downloaded from a repository and don&#39;t show up with list package APIs (for example, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt;), but you can restore them using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionsStatus&lt;/a&gt;. 
     * @param domain  The name of the domain that contains the package to delete.  (required)
     * @param repository  The name of the repository that contains the package versions to delete.  (required)
     * @param format  The format of the package versions to delete.  (required)
     * @param _package  The name of the package with the versions to delete.  (required)
     * @param deletePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;DeletePackageVersionsResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeletePackageVersionsResult> deletePackageVersionsWithHttpInfo(String domain, String repository, String format, String _package, DeletePackageVersionsRequest deletePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = deletePackageVersionsValidateBeforeCall(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<DeletePackageVersionsResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to &lt;code&gt;Archived&lt;/code&gt;. Archived packages cannot be downloaded from a repository and don&#39;t show up with list package APIs (for example, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt;), but you can restore them using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionsStatus&lt;/a&gt;. 
     * @param domain  The name of the domain that contains the package to delete.  (required)
     * @param repository  The name of the repository that contains the package versions to delete.  (required)
     * @param format  The format of the package versions to delete.  (required)
     * @param _package  The name of the package with the versions to delete.  (required)
     * @param deletePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePackageVersionsAsync(String domain, String repository, String format, String _package, DeletePackageVersionsRequest deletePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<DeletePackageVersionsResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = deletePackageVersionsValidateBeforeCall(domain, repository, format, _package, deletePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<DeletePackageVersionsResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRepository
     * @param domain  The name of the domain that contains the repository to delete.  (required)
     * @param repository  The name of the repository to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRepositoryCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteRepositoryValidateBeforeCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling deleteRepository(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling deleteRepository(Async)");
        }

        return deleteRepositoryCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Deletes a repository. 
     * @param domain  The name of the domain that contains the repository to delete.  (required)
     * @param repository  The name of the repository to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return DeleteRepositoryResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteRepositoryResult deleteRepository(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<DeleteRepositoryResult> localVarResp = deleteRepositoryWithHttpInfo(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Deletes a repository. 
     * @param domain  The name of the domain that contains the repository to delete.  (required)
     * @param repository  The name of the repository to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;DeleteRepositoryResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteRepositoryResult> deleteRepositoryWithHttpInfo(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = deleteRepositoryValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<DeleteRepositoryResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Deletes a repository. 
     * @param domain  The name of the domain that contains the repository to delete.  (required)
     * @param repository  The name of the repository to delete.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRepositoryAsync(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<DeleteRepositoryResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRepositoryValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<DeleteRepositoryResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRepositoryPermissionsPolicy
     * @param domain  The name of the domain that contains the repository associated with the resource policy to be deleted.  (required)
     * @param repository  The name of the repository that is associated with the resource policy to be deleted  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The revision of the repository&#39;s resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository&#39;s resource policy.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRepositoryPermissionsPolicyCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository/permissions/policies#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (policyRevision != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("policy-revision", policyRevision));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteRepositoryPermissionsPolicyValidateBeforeCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling deleteRepositoryPermissionsPolicy(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling deleteRepositoryPermissionsPolicy(Async)");
        }

        return deleteRepositoryPermissionsPolicyCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision, _callback);

    }

    /**
     * 
     * &lt;p&gt; Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. &lt;/p&gt; &lt;important&gt; &lt;p&gt; Use &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt; with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. &lt;/p&gt; &lt;/important&gt;
     * @param domain  The name of the domain that contains the repository associated with the resource policy to be deleted.  (required)
     * @param repository  The name of the repository that is associated with the resource policy to be deleted  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The revision of the repository&#39;s resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository&#39;s resource policy.  (optional)
     * @return DeleteRepositoryPermissionsPolicyResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteRepositoryPermissionsPolicyResult deleteRepositoryPermissionsPolicy(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision) throws ApiException {
        ApiResponse<DeleteRepositoryPermissionsPolicyResult> localVarResp = deleteRepositoryPermissionsPolicyWithHttpInfo(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. &lt;/p&gt; &lt;important&gt; &lt;p&gt; Use &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt; with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. &lt;/p&gt; &lt;/important&gt;
     * @param domain  The name of the domain that contains the repository associated with the resource policy to be deleted.  (required)
     * @param repository  The name of the repository that is associated with the resource policy to be deleted  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The revision of the repository&#39;s resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository&#39;s resource policy.  (optional)
     * @return ApiResponse&lt;DeleteRepositoryPermissionsPolicyResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteRepositoryPermissionsPolicyResult> deleteRepositoryPermissionsPolicyWithHttpInfo(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision) throws ApiException {
        okhttp3.Call localVarCall = deleteRepositoryPermissionsPolicyValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision, null);
        Type localVarReturnType = new TypeToken<DeleteRepositoryPermissionsPolicyResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. &lt;/p&gt; &lt;important&gt; &lt;p&gt; Use &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt; with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. &lt;/p&gt; &lt;/important&gt;
     * @param domain  The name of the domain that contains the repository associated with the resource policy to be deleted.  (required)
     * @param repository  The name of the repository that is associated with the resource policy to be deleted  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param policyRevision  The revision of the repository&#39;s resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository&#39;s resource policy.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRepositoryPermissionsPolicyAsync(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String policyRevision, final ApiCallback<DeleteRepositoryPermissionsPolicyResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRepositoryPermissionsPolicyValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, policyRevision, _callback);
        Type localVarReturnType = new TypeToken<DeleteRepositoryPermissionsPolicyResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for describeDomain
     * @param domain  A string that specifies the name of the requested domain.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describeDomainCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/domain#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call describeDomainValidateBeforeCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling describeDomain(Async)");
        }

        return describeDomainCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\&quot;&gt;DomainDescription&lt;/a&gt; object that contains information about the requested domain. 
     * @param domain  A string that specifies the name of the requested domain.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return DescribeDomainResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DescribeDomainResult describeDomain(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<DescribeDomainResult> localVarResp = describeDomainWithHttpInfo(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\&quot;&gt;DomainDescription&lt;/a&gt; object that contains information about the requested domain. 
     * @param domain  A string that specifies the name of the requested domain.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;DescribeDomainResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DescribeDomainResult> describeDomainWithHttpInfo(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = describeDomainValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<DescribeDomainResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\&quot;&gt;DomainDescription&lt;/a&gt; object that contains information about the requested domain. 
     * @param domain  A string that specifies the name of the requested domain.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describeDomainAsync(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<DescribeDomainResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = describeDomainValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<DescribeDomainResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for describePackage
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the requested package.  (required)
     * @param format A format that specifies the type of the requested package. (required)
     * @param _package The name of the requested package. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when requesting Maven packages. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describePackageCall(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call describePackageValidateBeforeCall(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling describePackage(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling describePackage(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling describePackage(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling describePackage(Async)");
        }

        return describePackageCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains information about the requested package.
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the requested package.  (required)
     * @param format A format that specifies the type of the requested package. (required)
     * @param _package The name of the requested package. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when requesting Maven packages. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return DescribePackageResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DescribePackageResult describePackage(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<DescribePackageResult> localVarResp = describePackageWithHttpInfo(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains information about the requested package.
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the requested package.  (required)
     * @param format A format that specifies the type of the requested package. (required)
     * @param _package The name of the requested package. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when requesting Maven packages. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;DescribePackageResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DescribePackageResult> describePackageWithHttpInfo(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = describePackageValidateBeforeCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<DescribePackageResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains information about the requested package.
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the requested package.  (required)
     * @param format A format that specifies the type of the requested package. (required)
     * @param _package The name of the requested package. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when requesting Maven packages. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describePackageAsync(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<DescribePackageResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = describePackageValidateBeforeCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<DescribePackageResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for describePackageVersion
     * @param domain  The name of the domain that contains the repository that contains the package version.  (required)
     * @param repository  The name of the repository that contains the package version.  (required)
     * @param format  A format that specifies the type of the requested package version.  (required)
     * @param _package  The name of the requested package version.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describePackageVersionCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package/version#domain&repository&format&package&version";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call describePackageVersionValidateBeforeCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling describePackageVersion(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling describePackageVersion(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling describePackageVersion(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling describePackageVersion(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling describePackageVersion(Async)");
        }

        return describePackageVersionCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains information about the requested package version. 
     * @param domain  The name of the domain that contains the repository that contains the package version.  (required)
     * @param repository  The name of the repository that contains the package version.  (required)
     * @param format  A format that specifies the type of the requested package version.  (required)
     * @param _package  The name of the requested package version.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return DescribePackageVersionResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DescribePackageVersionResult describePackageVersion(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<DescribePackageVersionResult> localVarResp = describePackageVersionWithHttpInfo(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains information about the requested package version. 
     * @param domain  The name of the domain that contains the repository that contains the package version.  (required)
     * @param repository  The name of the repository that contains the package version.  (required)
     * @param format  A format that specifies the type of the requested package version.  (required)
     * @param _package  The name of the requested package version.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;DescribePackageVersionResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DescribePackageVersionResult> describePackageVersionWithHttpInfo(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = describePackageVersionValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<DescribePackageVersionResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains information about the requested package version. 
     * @param domain  The name of the domain that contains the repository that contains the package version.  (required)
     * @param repository  The name of the repository that contains the package version.  (required)
     * @param format  A format that specifies the type of the requested package version.  (required)
     * @param _package  The name of the requested package version.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describePackageVersionAsync(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<DescribePackageVersionResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = describePackageVersionValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<DescribePackageVersionResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for describeRepository
     * @param domain  The name of the domain that contains the repository to describe.  (required)
     * @param repository  A string that specifies the name of the requested repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describeRepositoryCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call describeRepositoryValidateBeforeCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling describeRepository(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling describeRepository(Async)");
        }

        return describeRepositoryCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. 
     * @param domain  The name of the domain that contains the repository to describe.  (required)
     * @param repository  A string that specifies the name of the requested repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return DescribeRepositoryResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DescribeRepositoryResult describeRepository(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<DescribeRepositoryResult> localVarResp = describeRepositoryWithHttpInfo(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. 
     * @param domain  The name of the domain that contains the repository to describe.  (required)
     * @param repository  A string that specifies the name of the requested repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;DescribeRepositoryResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DescribeRepositoryResult> describeRepositoryWithHttpInfo(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = describeRepositoryValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<DescribeRepositoryResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. 
     * @param domain  The name of the domain that contains the repository to describe.  (required)
     * @param repository  A string that specifies the name of the requested repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call describeRepositoryAsync(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<DescribeRepositoryResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = describeRepositoryValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<DescribeRepositoryResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for disassociateExternalConnection
     * @param domain The name of the domain that contains the repository from which to remove the external repository.  (required)
     * @param repository The name of the repository from which the external connection will be removed.  (required)
     * @param externalConnection The name of the external connection to be removed from the repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disassociateExternalConnectionCall(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository/external-connection#domain&repository&external-connection";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (externalConnection != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("external-connection", externalConnection));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call disassociateExternalConnectionValidateBeforeCall(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling disassociateExternalConnection(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling disassociateExternalConnection(Async)");
        }

        // verify the required parameter 'externalConnection' is set
        if (externalConnection == null) {
            throw new ApiException("Missing the required parameter 'externalConnection' when calling disassociateExternalConnection(Async)");
        }

        return disassociateExternalConnectionCall(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Removes an existing external connection from a repository. 
     * @param domain The name of the domain that contains the repository from which to remove the external repository.  (required)
     * @param repository The name of the repository from which the external connection will be removed.  (required)
     * @param externalConnection The name of the external connection to be removed from the repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return DisassociateExternalConnectionResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DisassociateExternalConnectionResult disassociateExternalConnection(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<DisassociateExternalConnectionResult> localVarResp = disassociateExternalConnectionWithHttpInfo(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Removes an existing external connection from a repository. 
     * @param domain The name of the domain that contains the repository from which to remove the external repository.  (required)
     * @param repository The name of the repository from which the external connection will be removed.  (required)
     * @param externalConnection The name of the external connection to be removed from the repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;DisassociateExternalConnectionResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DisassociateExternalConnectionResult> disassociateExternalConnectionWithHttpInfo(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = disassociateExternalConnectionValidateBeforeCall(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<DisassociateExternalConnectionResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Removes an existing external connection from a repository. 
     * @param domain The name of the domain that contains the repository from which to remove the external repository.  (required)
     * @param repository The name of the repository from which the external connection will be removed.  (required)
     * @param externalConnection The name of the external connection to be removed from the repository.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disassociateExternalConnectionAsync(String domain, String repository, String externalConnection, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<DisassociateExternalConnectionResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = disassociateExternalConnectionValidateBeforeCall(domain, repository, externalConnection, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<DisassociateExternalConnectionResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for disposePackageVersions
     * @param domain  The name of the domain that contains the repository you want to dispose.  (required)
     * @param repository  The name of the repository that contains the package versions you want to dispose.  (required)
     * @param format  A format that specifies the type of package versions you want to dispose.  (required)
     * @param _package  The name of the package with the versions you want to dispose.  (required)
     * @param disposePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disposePackageVersionsCall(String domain, String repository, String format, String _package, DisposePackageVersionsRequest disposePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = disposePackageVersionsRequest;

        // create path and map variables
        String localVarPath = "/v1/package/versions/dispose#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call disposePackageVersionsValidateBeforeCall(String domain, String repository, String format, String _package, DisposePackageVersionsRequest disposePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling disposePackageVersions(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling disposePackageVersions(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling disposePackageVersions(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling disposePackageVersions(Async)");
        }

        // verify the required parameter 'disposePackageVersionsRequest' is set
        if (disposePackageVersionsRequest == null) {
            throw new ApiException("Missing the required parameter 'disposePackageVersionsRequest' when calling disposePackageVersions(Async)");
        }

        return disposePackageVersionsCall(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     * &lt;p&gt; Deletes the assets in package versions and sets the package versions&#39; status to &lt;code&gt;Disposed&lt;/code&gt;. A disposed package version cannot be restored in your repository because its assets are deleted. &lt;/p&gt; &lt;p&gt; To view all disposed package versions in a repository, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt; and set the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\&quot;&gt;status&lt;/a&gt; parameter to &lt;code&gt;Disposed&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; To view information about a disposed package version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\&quot;&gt;DescribePackageVersion&lt;/a&gt;. &lt;/p&gt;
     * @param domain  The name of the domain that contains the repository you want to dispose.  (required)
     * @param repository  The name of the repository that contains the package versions you want to dispose.  (required)
     * @param format  A format that specifies the type of package versions you want to dispose.  (required)
     * @param _package  The name of the package with the versions you want to dispose.  (required)
     * @param disposePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return DisposePackageVersionsResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DisposePackageVersionsResult disposePackageVersions(String domain, String repository, String format, String _package, DisposePackageVersionsRequest disposePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<DisposePackageVersionsResult> localVarResp = disposePackageVersionsWithHttpInfo(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Deletes the assets in package versions and sets the package versions&#39; status to &lt;code&gt;Disposed&lt;/code&gt;. A disposed package version cannot be restored in your repository because its assets are deleted. &lt;/p&gt; &lt;p&gt; To view all disposed package versions in a repository, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt; and set the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\&quot;&gt;status&lt;/a&gt; parameter to &lt;code&gt;Disposed&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; To view information about a disposed package version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\&quot;&gt;DescribePackageVersion&lt;/a&gt;. &lt;/p&gt;
     * @param domain  The name of the domain that contains the repository you want to dispose.  (required)
     * @param repository  The name of the repository that contains the package versions you want to dispose.  (required)
     * @param format  A format that specifies the type of package versions you want to dispose.  (required)
     * @param _package  The name of the package with the versions you want to dispose.  (required)
     * @param disposePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;DisposePackageVersionsResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DisposePackageVersionsResult> disposePackageVersionsWithHttpInfo(String domain, String repository, String format, String _package, DisposePackageVersionsRequest disposePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = disposePackageVersionsValidateBeforeCall(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<DisposePackageVersionsResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Deletes the assets in package versions and sets the package versions&#39; status to &lt;code&gt;Disposed&lt;/code&gt;. A disposed package version cannot be restored in your repository because its assets are deleted. &lt;/p&gt; &lt;p&gt; To view all disposed package versions in a repository, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt; and set the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\&quot;&gt;status&lt;/a&gt; parameter to &lt;code&gt;Disposed&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; To view information about a disposed package version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\&quot;&gt;DescribePackageVersion&lt;/a&gt;. &lt;/p&gt;
     * @param domain  The name of the domain that contains the repository you want to dispose.  (required)
     * @param repository  The name of the repository that contains the package versions you want to dispose.  (required)
     * @param format  A format that specifies the type of package versions you want to dispose.  (required)
     * @param _package  The name of the package with the versions you want to dispose.  (required)
     * @param disposePackageVersionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disposePackageVersionsAsync(String domain, String repository, String format, String _package, DisposePackageVersionsRequest disposePackageVersionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<DisposePackageVersionsResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = disposePackageVersionsValidateBeforeCall(domain, repository, format, _package, disposePackageVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<DisposePackageVersionsResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAuthorizationToken
     * @param domain  The name of the domain that is in scope for the generated authorization token.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param duration The time, in seconds, that the generated authorization token is valid. Valid values are &lt;code&gt;0&lt;/code&gt; and any number between &lt;code&gt;900&lt;/code&gt; (15 minutes) and &lt;code&gt;43200&lt;/code&gt; (12 hours). A value of &lt;code&gt;0&lt;/code&gt; will set the expiration of the authorization token to the same expiration of the user&#39;s role&#39;s temporary credentials. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAuthorizationTokenCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, Integer duration, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/authorization-token#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (duration != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("duration", duration));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAuthorizationTokenValidateBeforeCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, Integer duration, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling getAuthorizationToken(Async)");
        }

        return getAuthorizationTokenCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration, _callback);

    }

    /**
     * 
     * &lt;p&gt; Generates a temporary authorization token for accessing repositories in the domain. This API requires the &lt;code&gt;codeartifact:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions. For more information about authorization tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\&quot;&gt;CodeArtifact authentication and tokens&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CodeArtifact authorization tokens are valid for a period of 12 hours when created with the &lt;code&gt;login&lt;/code&gt; command. You can call &lt;code&gt;login&lt;/code&gt; periodically to refresh the token. When you create an authorization token with the &lt;code&gt;GetAuthorizationToken&lt;/code&gt; API, you can set a custom authorization period, up to a maximum of 12 hours, with the &lt;code&gt;durationSeconds&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The authorization period begins after &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called. If &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call &lt;code&gt;sts assume-role&lt;/code&gt; and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.&lt;/p&gt; &lt;p&gt;See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\&quot;&gt;Using IAM Roles&lt;/a&gt; for more information on controlling session duration. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain that is in scope for the generated authorization token.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param duration The time, in seconds, that the generated authorization token is valid. Valid values are &lt;code&gt;0&lt;/code&gt; and any number between &lt;code&gt;900&lt;/code&gt; (15 minutes) and &lt;code&gt;43200&lt;/code&gt; (12 hours). A value of &lt;code&gt;0&lt;/code&gt; will set the expiration of the authorization token to the same expiration of the user&#39;s role&#39;s temporary credentials. (optional)
     * @return GetAuthorizationTokenResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetAuthorizationTokenResult getAuthorizationToken(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, Integer duration) throws ApiException {
        ApiResponse<GetAuthorizationTokenResult> localVarResp = getAuthorizationTokenWithHttpInfo(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Generates a temporary authorization token for accessing repositories in the domain. This API requires the &lt;code&gt;codeartifact:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions. For more information about authorization tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\&quot;&gt;CodeArtifact authentication and tokens&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CodeArtifact authorization tokens are valid for a period of 12 hours when created with the &lt;code&gt;login&lt;/code&gt; command. You can call &lt;code&gt;login&lt;/code&gt; periodically to refresh the token. When you create an authorization token with the &lt;code&gt;GetAuthorizationToken&lt;/code&gt; API, you can set a custom authorization period, up to a maximum of 12 hours, with the &lt;code&gt;durationSeconds&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The authorization period begins after &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called. If &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call &lt;code&gt;sts assume-role&lt;/code&gt; and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.&lt;/p&gt; &lt;p&gt;See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\&quot;&gt;Using IAM Roles&lt;/a&gt; for more information on controlling session duration. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain that is in scope for the generated authorization token.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param duration The time, in seconds, that the generated authorization token is valid. Valid values are &lt;code&gt;0&lt;/code&gt; and any number between &lt;code&gt;900&lt;/code&gt; (15 minutes) and &lt;code&gt;43200&lt;/code&gt; (12 hours). A value of &lt;code&gt;0&lt;/code&gt; will set the expiration of the authorization token to the same expiration of the user&#39;s role&#39;s temporary credentials. (optional)
     * @return ApiResponse&lt;GetAuthorizationTokenResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAuthorizationTokenResult> getAuthorizationTokenWithHttpInfo(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, Integer duration) throws ApiException {
        okhttp3.Call localVarCall = getAuthorizationTokenValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration, null);
        Type localVarReturnType = new TypeToken<GetAuthorizationTokenResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Generates a temporary authorization token for accessing repositories in the domain. This API requires the &lt;code&gt;codeartifact:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions. For more information about authorization tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\&quot;&gt;CodeArtifact authentication and tokens&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CodeArtifact authorization tokens are valid for a period of 12 hours when created with the &lt;code&gt;login&lt;/code&gt; command. You can call &lt;code&gt;login&lt;/code&gt; periodically to refresh the token. When you create an authorization token with the &lt;code&gt;GetAuthorizationToken&lt;/code&gt; API, you can set a custom authorization period, up to a maximum of 12 hours, with the &lt;code&gt;durationSeconds&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The authorization period begins after &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called. If &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call &lt;code&gt;sts assume-role&lt;/code&gt; and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.&lt;/p&gt; &lt;p&gt;See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\&quot;&gt;Using IAM Roles&lt;/a&gt; for more information on controlling session duration. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain that is in scope for the generated authorization token.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param duration The time, in seconds, that the generated authorization token is valid. Valid values are &lt;code&gt;0&lt;/code&gt; and any number between &lt;code&gt;900&lt;/code&gt; (15 minutes) and &lt;code&gt;43200&lt;/code&gt; (12 hours). A value of &lt;code&gt;0&lt;/code&gt; will set the expiration of the authorization token to the same expiration of the user&#39;s role&#39;s temporary credentials. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAuthorizationTokenAsync(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, Integer duration, final ApiCallback<GetAuthorizationTokenResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAuthorizationTokenValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, duration, _callback);
        Type localVarReturnType = new TypeToken<GetAuthorizationTokenResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomainPermissionsPolicy
     * @param domain  The name of the domain to which the resource policy is attached.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainPermissionsPolicyCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/domain/permissions/policy#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getDomainPermissionsPolicyValidateBeforeCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling getDomainPermissionsPolicy(Async)");
        }

        return getDomainPermissionsPolicyCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     * &lt;p&gt; Returns the resource policy attached to the specified domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; The policy is a resource-based policy, not an identity-based policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\&quot;&gt;Identity-based policies and resource-based policies &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain to which the resource policy is attached.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return GetDomainPermissionsPolicyResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetDomainPermissionsPolicyResult getDomainPermissionsPolicy(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<GetDomainPermissionsPolicyResult> localVarResp = getDomainPermissionsPolicyWithHttpInfo(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Returns the resource policy attached to the specified domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; The policy is a resource-based policy, not an identity-based policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\&quot;&gt;Identity-based policies and resource-based policies &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain to which the resource policy is attached.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;GetDomainPermissionsPolicyResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDomainPermissionsPolicyResult> getDomainPermissionsPolicyWithHttpInfo(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = getDomainPermissionsPolicyValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<GetDomainPermissionsPolicyResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Returns the resource policy attached to the specified domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; The policy is a resource-based policy, not an identity-based policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\&quot;&gt;Identity-based policies and resource-based policies &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;
     * @param domain  The name of the domain to which the resource policy is attached.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainPermissionsPolicyAsync(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<GetDomainPermissionsPolicyResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainPermissionsPolicyValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<GetDomainPermissionsPolicyResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPackageVersionAsset
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested asset.  (required)
     * @param repository  The repository that contains the package version with the requested asset.  (required)
     * @param format  A format that specifies the type of the package version with the requested asset file.  (required)
     * @param _package  The name of the package that contains the requested asset.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param asset  The name of the requested asset.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param revision  The name of the package version revision that contains the requested asset.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPackageVersionAssetCall(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String revision, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package/version/asset#domain&repository&format&package&version&asset";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (asset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("asset", asset));
        }

        if (revision != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("revision", revision));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPackageVersionAssetValidateBeforeCall(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String revision, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling getPackageVersionAsset(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling getPackageVersionAsset(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling getPackageVersionAsset(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling getPackageVersionAsset(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling getPackageVersionAsset(Async)");
        }

        // verify the required parameter 'asset' is set
        if (asset == null) {
            throw new ApiException("Missing the required parameter 'asset' when calling getPackageVersionAsset(Async)");
        }

        return getPackageVersionAssetCall(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision, _callback);

    }

    /**
     * 
     *  Returns an asset (or file) that is in a package. For example, for a Maven package version, use &lt;code&gt;GetPackageVersionAsset&lt;/code&gt; to download a &lt;code&gt;JAR&lt;/code&gt; file, a &lt;code&gt;POM&lt;/code&gt; file, or any other assets in the package version. 
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested asset.  (required)
     * @param repository  The repository that contains the package version with the requested asset.  (required)
     * @param format  A format that specifies the type of the package version with the requested asset file.  (required)
     * @param _package  The name of the package that contains the requested asset.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param asset  The name of the requested asset.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param revision  The name of the package version revision that contains the requested asset.  (optional)
     * @return GetPackageVersionAssetResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public GetPackageVersionAssetResult getPackageVersionAsset(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String revision) throws ApiException {
        ApiResponse<GetPackageVersionAssetResult> localVarResp = getPackageVersionAssetWithHttpInfo(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns an asset (or file) that is in a package. For example, for a Maven package version, use &lt;code&gt;GetPackageVersionAsset&lt;/code&gt; to download a &lt;code&gt;JAR&lt;/code&gt; file, a &lt;code&gt;POM&lt;/code&gt; file, or any other assets in the package version. 
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested asset.  (required)
     * @param repository  The repository that contains the package version with the requested asset.  (required)
     * @param format  A format that specifies the type of the package version with the requested asset file.  (required)
     * @param _package  The name of the package that contains the requested asset.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param asset  The name of the requested asset.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param revision  The name of the package version revision that contains the requested asset.  (optional)
     * @return ApiResponse&lt;GetPackageVersionAssetResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetPackageVersionAssetResult> getPackageVersionAssetWithHttpInfo(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String revision) throws ApiException {
        okhttp3.Call localVarCall = getPackageVersionAssetValidateBeforeCall(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision, null);
        Type localVarReturnType = new TypeToken<GetPackageVersionAssetResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns an asset (or file) that is in a package. For example, for a Maven package version, use &lt;code&gt;GetPackageVersionAsset&lt;/code&gt; to download a &lt;code&gt;JAR&lt;/code&gt; file, a &lt;code&gt;POM&lt;/code&gt; file, or any other assets in the package version. 
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested asset.  (required)
     * @param repository  The repository that contains the package version with the requested asset.  (required)
     * @param format  A format that specifies the type of the package version with the requested asset file.  (required)
     * @param _package  The name of the package that contains the requested asset.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param asset  The name of the requested asset.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param revision  The name of the package version revision that contains the requested asset.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPackageVersionAssetAsync(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String revision, final ApiCallback<GetPackageVersionAssetResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPackageVersionAssetValidateBeforeCall(domain, repository, format, _package, version, asset, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, revision, _callback);
        Type localVarReturnType = new TypeToken<GetPackageVersionAssetResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPackageVersionReadme
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested readme file.  (required)
     * @param repository  The repository that contains the package with the requested readme file.  (required)
     * @param format  A format that specifies the type of the package version with the requested readme file.  (required)
     * @param _package  The name of the package version that contains the requested readme file.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPackageVersionReadmeCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package/version/readme#domain&repository&format&package&version";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPackageVersionReadmeValidateBeforeCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling getPackageVersionReadme(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling getPackageVersionReadme(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling getPackageVersionReadme(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling getPackageVersionReadme(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling getPackageVersionReadme(Async)");
        }

        return getPackageVersionReadmeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     * &lt;p&gt; Gets the readme file or descriptive text for a package version. &lt;/p&gt; &lt;p&gt; The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. &lt;/p&gt;
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested readme file.  (required)
     * @param repository  The repository that contains the package with the requested readme file.  (required)
     * @param format  A format that specifies the type of the package version with the requested readme file.  (required)
     * @param _package  The name of the package version that contains the requested readme file.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return GetPackageVersionReadmeResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetPackageVersionReadmeResult getPackageVersionReadme(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<GetPackageVersionReadmeResult> localVarResp = getPackageVersionReadmeWithHttpInfo(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Gets the readme file or descriptive text for a package version. &lt;/p&gt; &lt;p&gt; The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. &lt;/p&gt;
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested readme file.  (required)
     * @param repository  The repository that contains the package with the requested readme file.  (required)
     * @param format  A format that specifies the type of the package version with the requested readme file.  (required)
     * @param _package  The name of the package version that contains the requested readme file.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;GetPackageVersionReadmeResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetPackageVersionReadmeResult> getPackageVersionReadmeWithHttpInfo(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = getPackageVersionReadmeValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<GetPackageVersionReadmeResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Gets the readme file or descriptive text for a package version. &lt;/p&gt; &lt;p&gt; The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. &lt;/p&gt;
     * @param domain  The name of the domain that contains the repository that contains the package version with the requested readme file.  (required)
     * @param repository  The repository that contains the package with the requested readme file.  (required)
     * @param format  A format that specifies the type of the package version with the requested readme file.  (required)
     * @param _package  The name of the package version that contains the requested readme file.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPackageVersionReadmeAsync(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<GetPackageVersionReadmeResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPackageVersionReadmeValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<GetPackageVersionReadmeResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRepositoryEndpoint
     * @param domain  The name of the domain that contains the repository.  (required)
     * @param repository  The name of the repository.  (required)
     * @param format  Returns which endpoint of a repository to return. A repository has one endpoint for each package format.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRepositoryEndpointCall(String domain, String repository, String format, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository/endpoint#domain&repository&format";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getRepositoryEndpointValidateBeforeCall(String domain, String repository, String format, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling getRepositoryEndpoint(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling getRepositoryEndpoint(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling getRepositoryEndpoint(Async)");
        }

        return getRepositoryEndpointCall(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     * &lt;p&gt; Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     * @param domain  The name of the domain that contains the repository.  (required)
     * @param repository  The name of the repository.  (required)
     * @param format  Returns which endpoint of a repository to return. A repository has one endpoint for each package format.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.  (optional)
     * @return GetRepositoryEndpointResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetRepositoryEndpointResult getRepositoryEndpoint(String domain, String repository, String format, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<GetRepositoryEndpointResult> localVarResp = getRepositoryEndpointWithHttpInfo(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     * @param domain  The name of the domain that contains the repository.  (required)
     * @param repository  The name of the repository.  (required)
     * @param format  Returns which endpoint of a repository to return. A repository has one endpoint for each package format.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;GetRepositoryEndpointResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRepositoryEndpointResult> getRepositoryEndpointWithHttpInfo(String domain, String repository, String format, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = getRepositoryEndpointValidateBeforeCall(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<GetRepositoryEndpointResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     * @param domain  The name of the domain that contains the repository.  (required)
     * @param repository  The name of the repository.  (required)
     * @param format  Returns which endpoint of a repository to return. A repository has one endpoint for each package format.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRepositoryEndpointAsync(String domain, String repository, String format, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<GetRepositoryEndpointResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRepositoryEndpointValidateBeforeCall(domain, repository, format, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<GetRepositoryEndpointResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRepositoryPermissionsPolicy
     * @param domain  The name of the domain containing the repository whose associated resource policy is to be retrieved.  (required)
     * @param repository  The name of the repository whose associated resource policy is to be retrieved.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRepositoryPermissionsPolicyCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repository/permissions/policy#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getRepositoryPermissionsPolicyValidateBeforeCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling getRepositoryPermissionsPolicy(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling getRepositoryPermissionsPolicy(Async)");
        }

        return getRepositoryPermissionsPolicyCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Returns the resource policy that is set on a repository. 
     * @param domain  The name of the domain containing the repository whose associated resource policy is to be retrieved.  (required)
     * @param repository  The name of the repository whose associated resource policy is to be retrieved.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return GetRepositoryPermissionsPolicyResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetRepositoryPermissionsPolicyResult getRepositoryPermissionsPolicy(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<GetRepositoryPermissionsPolicyResult> localVarResp = getRepositoryPermissionsPolicyWithHttpInfo(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns the resource policy that is set on a repository. 
     * @param domain  The name of the domain containing the repository whose associated resource policy is to be retrieved.  (required)
     * @param repository  The name of the repository whose associated resource policy is to be retrieved.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;GetRepositoryPermissionsPolicyResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRepositoryPermissionsPolicyResult> getRepositoryPermissionsPolicyWithHttpInfo(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = getRepositoryPermissionsPolicyValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<GetRepositoryPermissionsPolicyResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns the resource policy that is set on a repository. 
     * @param domain  The name of the domain containing the repository whose associated resource policy is to be retrieved.  (required)
     * @param repository  The name of the repository whose associated resource policy is to be retrieved.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRepositoryPermissionsPolicyAsync(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<GetRepositoryPermissionsPolicyResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRepositoryPermissionsPolicyValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<GetRepositoryPermissionsPolicyResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listDomains
     * @param listDomainsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listDomainsCall(ListDomainsRequest listDomainsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listDomainsRequest;

        // create path and map variables
        String localVarPath = "/v1/domains";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listDomainsValidateBeforeCall(ListDomainsRequest listDomainsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listDomainsRequest' is set
        if (listDomainsRequest == null) {
            throw new ApiException("Missing the required parameter 'listDomainsRequest' when calling listDomains(Async)");
        }

        return listDomainsCall(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;DomainSummary&lt;/a&gt; objects for all domains owned by the Amazon Web Services account that makes this call. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain. 
     * @param listDomainsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListDomainsResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListDomainsResult listDomains(ListDomainsRequest listDomainsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListDomainsResult> localVarResp = listDomainsWithHttpInfo(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;DomainSummary&lt;/a&gt; objects for all domains owned by the Amazon Web Services account that makes this call. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain. 
     * @param listDomainsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListDomainsResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListDomainsResult> listDomainsWithHttpInfo(ListDomainsRequest listDomainsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listDomainsValidateBeforeCall(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListDomainsResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;DomainSummary&lt;/a&gt; objects for all domains owned by the Amazon Web Services account that makes this call. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain. 
     * @param listDomainsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listDomainsAsync(ListDomainsRequest listDomainsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListDomainsResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listDomainsValidateBeforeCall(listDomainsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListDomainsResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPackageVersionAssets
     * @param domain  The name of the domain that contains the repository associated with the package version assets.  (required)
     * @param repository  The name of the repository that contains the package that contains the requested package version assets.  (required)
     * @param format  The format of the package that contains the requested package version assets.  (required)
     * @param _package  The name of the package that contains the requested package version assets.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackageVersionAssetsCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package/version/assets#domain&repository&format&package&version";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("max-results", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next-token", nextToken));
        }

        if (maxResults2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults2));
        }

        if (nextToken2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken2));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPackageVersionAssetsValidateBeforeCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling listPackageVersionAssets(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling listPackageVersionAssets(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling listPackageVersionAssets(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling listPackageVersionAssets(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling listPackageVersionAssets(Async)");
        }

        return listPackageVersionAssetsCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2, _callback);

    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\&quot;&gt;AssetSummary&lt;/a&gt; objects for assets in a package version. 
     * @param domain  The name of the domain that contains the repository associated with the package version assets.  (required)
     * @param repository  The name of the repository that contains the package that contains the requested package version assets.  (required)
     * @param format  The format of the package that contains the requested package version assets.  (required)
     * @param _package  The name of the package that contains the requested package version assets.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ListPackageVersionAssetsResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListPackageVersionAssetsResult listPackageVersionAssets(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Integer maxResults, String nextToken, String maxResults2, String nextToken2) throws ApiException {
        ApiResponse<ListPackageVersionAssetsResult> localVarResp = listPackageVersionAssetsWithHttpInfo(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\&quot;&gt;AssetSummary&lt;/a&gt; objects for assets in a package version. 
     * @param domain  The name of the domain that contains the repository associated with the package version assets.  (required)
     * @param repository  The name of the repository that contains the package that contains the requested package version assets.  (required)
     * @param format  The format of the package that contains the requested package version assets.  (required)
     * @param _package  The name of the package that contains the requested package version assets.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ApiResponse&lt;ListPackageVersionAssetsResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPackageVersionAssetsResult> listPackageVersionAssetsWithHttpInfo(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Integer maxResults, String nextToken, String maxResults2, String nextToken2) throws ApiException {
        okhttp3.Call localVarCall = listPackageVersionAssetsValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2, null);
        Type localVarReturnType = new TypeToken<ListPackageVersionAssetsResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\&quot;&gt;AssetSummary&lt;/a&gt; objects for assets in a package version. 
     * @param domain  The name of the domain that contains the repository associated with the package version assets.  (required)
     * @param repository  The name of the repository that contains the package that contains the requested package version assets.  (required)
     * @param format  The format of the package that contains the requested package version assets.  (required)
     * @param _package  The name of the package that contains the requested package version assets.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackageVersionAssetsAsync(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback<ListPackageVersionAssetsResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPackageVersionAssetsValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, maxResults, nextToken, maxResults2, nextToken2, _callback);
        Type localVarReturnType = new TypeToken<ListPackageVersionAssetsResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPackageVersionDependencies
     * @param domain  The name of the domain that contains the repository that contains the requested package version dependencies.  (required)
     * @param repository  The name of the repository that contains the requested package version.  (required)
     * @param format  The format of the package with the requested dependencies.  (required)
     * @param _package  The name of the package versions&#39; package.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackageVersionDependenciesCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package/version/dependencies#domain&repository&format&package&version";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next-token", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPackageVersionDependenciesValidateBeforeCall(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling listPackageVersionDependencies(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling listPackageVersionDependencies(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling listPackageVersionDependencies(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling listPackageVersionDependencies(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling listPackageVersionDependencies(Async)");
        }

        return listPackageVersionDependenciesCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken, _callback);

    }

    /**
     * 
     *  Returns the direct dependencies for a package version. The dependencies are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\&quot;&gt;PackageDependency&lt;/a&gt; objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the &lt;code&gt;package.json&lt;/code&gt; file for npm packages and the &lt;code&gt;pom.xml&lt;/code&gt; file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 
     * @param domain  The name of the domain that contains the repository that contains the requested package version dependencies.  (required)
     * @param repository  The name of the repository that contains the requested package version.  (required)
     * @param format  The format of the package with the requested dependencies.  (required)
     * @param _package  The name of the package versions&#39; package.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @return ListPackageVersionDependenciesResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListPackageVersionDependenciesResult listPackageVersionDependencies(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String nextToken) throws ApiException {
        ApiResponse<ListPackageVersionDependenciesResult> localVarResp = listPackageVersionDependenciesWithHttpInfo(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns the direct dependencies for a package version. The dependencies are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\&quot;&gt;PackageDependency&lt;/a&gt; objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the &lt;code&gt;package.json&lt;/code&gt; file for npm packages and the &lt;code&gt;pom.xml&lt;/code&gt; file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 
     * @param domain  The name of the domain that contains the repository that contains the requested package version dependencies.  (required)
     * @param repository  The name of the repository that contains the requested package version.  (required)
     * @param format  The format of the package with the requested dependencies.  (required)
     * @param _package  The name of the package versions&#39; package.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @return ApiResponse&lt;ListPackageVersionDependenciesResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPackageVersionDependenciesResult> listPackageVersionDependenciesWithHttpInfo(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listPackageVersionDependenciesValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken, null);
        Type localVarReturnType = new TypeToken<ListPackageVersionDependenciesResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns the direct dependencies for a package version. The dependencies are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\&quot;&gt;PackageDependency&lt;/a&gt; objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the &lt;code&gt;package.json&lt;/code&gt; file for npm packages and the &lt;code&gt;pom.xml&lt;/code&gt; file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 
     * @param domain  The name of the domain that contains the repository that contains the requested package version dependencies.  (required)
     * @param repository  The name of the repository that contains the requested package version.  (required)
     * @param format  The format of the package with the requested dependencies.  (required)
     * @param _package  The name of the package versions&#39; package.  (required)
     * @param version  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;).  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackageVersionDependenciesAsync(String domain, String repository, String format, String _package, String version, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String nextToken, final ApiCallback<ListPackageVersionDependenciesResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPackageVersionDependenciesValidateBeforeCall(domain, repository, format, _package, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListPackageVersionDependenciesResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPackageVersions
     * @param domain  The name of the domain that contains the repository that contains the requested package versions.  (required)
     * @param repository  The name of the repository that contains the requested package versions.  (required)
     * @param format  The format of the package versions you want to list.  (required)
     * @param _package  The name of the package for which you want to request package versions.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param status  A string that filters the requested package versions by status.  (optional)
     * @param sortBy  How to sort the requested list of package versions.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param originType The &lt;code&gt;originType&lt;/code&gt; used to filter package versions. Only package versions with the provided &lt;code&gt;originType&lt;/code&gt; will be returned. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackageVersionsCall(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String status, String sortBy, Integer maxResults, String nextToken, String originType, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/package/versions#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (status != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("status", status));
        }

        if (sortBy != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sortBy", sortBy));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("max-results", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next-token", nextToken));
        }

        if (originType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("originType", originType));
        }

        if (maxResults2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults2));
        }

        if (nextToken2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken2));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPackageVersionsValidateBeforeCall(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String status, String sortBy, Integer maxResults, String nextToken, String originType, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling listPackageVersions(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling listPackageVersions(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling listPackageVersions(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling listPackageVersions(Async)");
        }

        return listPackageVersionsCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2, _callback);

    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\&quot;&gt;PackageVersionSummary&lt;/a&gt; objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling &lt;code&gt;list-package-versions&lt;/code&gt; with no &lt;code&gt;--status&lt;/code&gt; parameter. 
     * @param domain  The name of the domain that contains the repository that contains the requested package versions.  (required)
     * @param repository  The name of the repository that contains the requested package versions.  (required)
     * @param format  The format of the package versions you want to list.  (required)
     * @param _package  The name of the package for which you want to request package versions.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param status  A string that filters the requested package versions by status.  (optional)
     * @param sortBy  How to sort the requested list of package versions.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param originType The &lt;code&gt;originType&lt;/code&gt; used to filter package versions. Only package versions with the provided &lt;code&gt;originType&lt;/code&gt; will be returned. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ListPackageVersionsResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListPackageVersionsResult listPackageVersions(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String status, String sortBy, Integer maxResults, String nextToken, String originType, String maxResults2, String nextToken2) throws ApiException {
        ApiResponse<ListPackageVersionsResult> localVarResp = listPackageVersionsWithHttpInfo(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\&quot;&gt;PackageVersionSummary&lt;/a&gt; objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling &lt;code&gt;list-package-versions&lt;/code&gt; with no &lt;code&gt;--status&lt;/code&gt; parameter. 
     * @param domain  The name of the domain that contains the repository that contains the requested package versions.  (required)
     * @param repository  The name of the repository that contains the requested package versions.  (required)
     * @param format  The format of the package versions you want to list.  (required)
     * @param _package  The name of the package for which you want to request package versions.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param status  A string that filters the requested package versions by status.  (optional)
     * @param sortBy  How to sort the requested list of package versions.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param originType The &lt;code&gt;originType&lt;/code&gt; used to filter package versions. Only package versions with the provided &lt;code&gt;originType&lt;/code&gt; will be returned. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ApiResponse&lt;ListPackageVersionsResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPackageVersionsResult> listPackageVersionsWithHttpInfo(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String status, String sortBy, Integer maxResults, String nextToken, String originType, String maxResults2, String nextToken2) throws ApiException {
        okhttp3.Call localVarCall = listPackageVersionsValidateBeforeCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2, null);
        Type localVarReturnType = new TypeToken<ListPackageVersionsResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\&quot;&gt;PackageVersionSummary&lt;/a&gt; objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling &lt;code&gt;list-package-versions&lt;/code&gt; with no &lt;code&gt;--status&lt;/code&gt; parameter. 
     * @param domain  The name of the domain that contains the repository that contains the requested package versions.  (required)
     * @param repository  The name of the repository that contains the requested package versions.  (required)
     * @param format  The format of the package versions you want to list.  (required)
     * @param _package  The name of the package for which you want to request package versions.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param status  A string that filters the requested package versions by status.  (optional)
     * @param sortBy  How to sort the requested list of package versions.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param originType The &lt;code&gt;originType&lt;/code&gt; used to filter package versions. Only package versions with the provided &lt;code&gt;originType&lt;/code&gt; will be returned. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackageVersionsAsync(String domain, String repository, String format, String _package, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, String status, String sortBy, Integer maxResults, String nextToken, String originType, String maxResults2, String nextToken2, final ApiCallback<ListPackageVersionsResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPackageVersionsValidateBeforeCall(domain, repository, format, _package, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, status, sortBy, maxResults, nextToken, originType, maxResults2, nextToken2, _callback);
        Type localVarReturnType = new TypeToken<ListPackageVersionsResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPackages
     * @param domain  The name of the domain that contains the repository that contains the requested packages.  (required)
     * @param repository  The name of the repository that contains the requested packages.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param format The format used to filter requested packages. Only packages from the provided format will be returned. (optional)
     * @param namespace &lt;p&gt;The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called &lt;code&gt;--namespace&lt;/code&gt; and not &lt;code&gt;--namespace-prefix&lt;/code&gt;, it has prefix-matching behavior.&lt;/p&gt; &lt;p&gt;Each package format uses namespace as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param packagePrefix  A prefix used to filter requested packages. Only packages with names that start with &lt;code&gt;packagePrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param publish The value of the &lt;code&gt;Publish&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param upstream The value of the &lt;code&gt;Upstream&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackagesCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String format, String namespace, String packagePrefix, Integer maxResults, String nextToken, String publish, String upstream, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/packages#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (packagePrefix != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package-prefix", packagePrefix));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("max-results", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next-token", nextToken));
        }

        if (publish != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("publish", publish));
        }

        if (upstream != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("upstream", upstream));
        }

        if (maxResults2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults2));
        }

        if (nextToken2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken2));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPackagesValidateBeforeCall(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String format, String namespace, String packagePrefix, Integer maxResults, String nextToken, String publish, String upstream, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling listPackages(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling listPackages(Async)");
        }

        return listPackagesCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2, _callback);

    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\&quot;&gt;PackageSummary&lt;/a&gt; objects for packages in a repository that match the request parameters. 
     * @param domain  The name of the domain that contains the repository that contains the requested packages.  (required)
     * @param repository  The name of the repository that contains the requested packages.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param format The format used to filter requested packages. Only packages from the provided format will be returned. (optional)
     * @param namespace &lt;p&gt;The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called &lt;code&gt;--namespace&lt;/code&gt; and not &lt;code&gt;--namespace-prefix&lt;/code&gt;, it has prefix-matching behavior.&lt;/p&gt; &lt;p&gt;Each package format uses namespace as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param packagePrefix  A prefix used to filter requested packages. Only packages with names that start with &lt;code&gt;packagePrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param publish The value of the &lt;code&gt;Publish&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param upstream The value of the &lt;code&gt;Upstream&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ListPackagesResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListPackagesResult listPackages(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String format, String namespace, String packagePrefix, Integer maxResults, String nextToken, String publish, String upstream, String maxResults2, String nextToken2) throws ApiException {
        ApiResponse<ListPackagesResult> localVarResp = listPackagesWithHttpInfo(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\&quot;&gt;PackageSummary&lt;/a&gt; objects for packages in a repository that match the request parameters. 
     * @param domain  The name of the domain that contains the repository that contains the requested packages.  (required)
     * @param repository  The name of the repository that contains the requested packages.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param format The format used to filter requested packages. Only packages from the provided format will be returned. (optional)
     * @param namespace &lt;p&gt;The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called &lt;code&gt;--namespace&lt;/code&gt; and not &lt;code&gt;--namespace-prefix&lt;/code&gt;, it has prefix-matching behavior.&lt;/p&gt; &lt;p&gt;Each package format uses namespace as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param packagePrefix  A prefix used to filter requested packages. Only packages with names that start with &lt;code&gt;packagePrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param publish The value of the &lt;code&gt;Publish&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param upstream The value of the &lt;code&gt;Upstream&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ApiResponse&lt;ListPackagesResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPackagesResult> listPackagesWithHttpInfo(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String format, String namespace, String packagePrefix, Integer maxResults, String nextToken, String publish, String upstream, String maxResults2, String nextToken2) throws ApiException {
        okhttp3.Call localVarCall = listPackagesValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2, null);
        Type localVarReturnType = new TypeToken<ListPackagesResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\&quot;&gt;PackageSummary&lt;/a&gt; objects for packages in a repository that match the request parameters. 
     * @param domain  The name of the domain that contains the repository that contains the requested packages.  (required)
     * @param repository  The name of the repository that contains the requested packages.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param format The format used to filter requested packages. Only packages from the provided format will be returned. (optional)
     * @param namespace &lt;p&gt;The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called &lt;code&gt;--namespace&lt;/code&gt; and not &lt;code&gt;--namespace-prefix&lt;/code&gt;, it has prefix-matching behavior.&lt;/p&gt; &lt;p&gt;Each package format uses namespace as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param packagePrefix  A prefix used to filter requested packages. Only packages with names that start with &lt;code&gt;packagePrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param publish The value of the &lt;code&gt;Publish&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param upstream The value of the &lt;code&gt;Upstream&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;. (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPackagesAsync(String domain, String repository, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String format, String namespace, String packagePrefix, Integer maxResults, String nextToken, String publish, String upstream, String maxResults2, String nextToken2, final ApiCallback<ListPackagesResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPackagesValidateBeforeCall(domain, repository, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, format, namespace, packagePrefix, maxResults, nextToken, publish, upstream, maxResults2, nextToken2, _callback);
        Type localVarReturnType = new TypeToken<ListPackagesResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listRepositories
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned. (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRepositoriesCall(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/repositories";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (repositoryPrefix != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository-prefix", repositoryPrefix));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("max-results", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next-token", nextToken));
        }

        if (maxResults2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults2));
        }

        if (nextToken2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken2));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listRepositoriesValidateBeforeCall(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        return listRepositoriesCall(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2, _callback);

    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned. (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ListRepositoriesResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListRepositoriesResult listRepositories(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2) throws ApiException {
        ApiResponse<ListRepositoriesResult> localVarResp = listRepositoriesWithHttpInfo(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned. (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ApiResponse&lt;ListRepositoriesResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListRepositoriesResult> listRepositoriesWithHttpInfo(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2) throws ApiException {
        okhttp3.Call localVarCall = listRepositoriesValidateBeforeCall(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2, null);
        Type localVarReturnType = new TypeToken<ListRepositoriesResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned. (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRepositoriesAsync(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback<ListRepositoriesResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listRepositoriesValidateBeforeCall(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2, _callback);
        Type localVarReturnType = new TypeToken<ListRepositoriesResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listRepositoriesInDomain
     * @param domain  The name of the domain that contains the returned list of repositories.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param administratorAccount  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID.  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRepositoriesInDomainCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String administratorAccount, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/domain/repositories#domain";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (administratorAccount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("administrator-account", administratorAccount));
        }

        if (repositoryPrefix != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository-prefix", repositoryPrefix));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("max-results", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next-token", nextToken));
        }

        if (maxResults2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults2));
        }

        if (nextToken2 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken2));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listRepositoriesInDomainValidateBeforeCall(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String administratorAccount, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling listRepositoriesInDomain(Async)");
        }

        return listRepositoriesInDomainCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2, _callback);

    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified domain and that matches the input parameters. 
     * @param domain  The name of the domain that contains the returned list of repositories.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param administratorAccount  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID.  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ListRepositoriesInDomainResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListRepositoriesInDomainResult listRepositoriesInDomain(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String administratorAccount, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2) throws ApiException {
        ApiResponse<ListRepositoriesInDomainResult> localVarResp = listRepositoriesInDomainWithHttpInfo(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2);
        return localVarResp.getData();
    }

    /**
     * 
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified domain and that matches the input parameters. 
     * @param domain  The name of the domain that contains the returned list of repositories.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param administratorAccount  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID.  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @return ApiResponse&lt;ListRepositoriesInDomainResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListRepositoriesInDomainResult> listRepositoriesInDomainWithHttpInfo(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String administratorAccount, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2) throws ApiException {
        okhttp3.Call localVarCall = listRepositoriesInDomainValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2, null);
        Type localVarReturnType = new TypeToken<ListRepositoriesInDomainResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified domain and that matches the input parameters. 
     * @param domain  The name of the domain that contains the returned list of repositories.  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param administratorAccount  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID.  (optional)
     * @param repositoryPrefix  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned.  (optional)
     * @param maxResults  The maximum number of results to return per page.  (optional)
     * @param nextToken  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  (optional)
     * @param maxResults2 Pagination limit (optional)
     * @param nextToken2 Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRepositoriesInDomainAsync(String domain, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String administratorAccount, String repositoryPrefix, Integer maxResults, String nextToken, String maxResults2, String nextToken2, final ApiCallback<ListRepositoriesInDomainResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listRepositoriesInDomainValidateBeforeCall(domain, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, administratorAccount, repositoryPrefix, maxResults, nextToken, maxResults2, nextToken2, _callback);
        Type localVarReturnType = new TypeToken<ListRepositoriesInDomainResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTagsForResource
     * @param resourceArn The Amazon Resource Name (ARN) of the resource to get tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceCall(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/tags#resourceArn";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (resourceArn != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("resourceArn", resourceArn));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listTagsForResourceValidateBeforeCall(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling listTagsForResource(Async)");
        }

        return listTagsForResourceCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource to get tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ListTagsForResourceResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListTagsForResourceResult listTagsForResource(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<ListTagsForResourceResult> localVarResp = listTagsForResourceWithHttpInfo(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource to get tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;ListTagsForResourceResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTagsForResourceResult> listTagsForResourceWithHttpInfo(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<ListTagsForResourceResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource to get tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceAsync(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<ListTagsForResourceResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<ListTagsForResourceResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for publishPackageVersion
     * @param domain The name of the domain that contains the repository that contains the package version to publish. (required)
     * @param repository The name of the repository that the package version will be published to. (required)
     * @param format &lt;p&gt;A format that specifies the type of the package version with the requested asset file.&lt;/p&gt; &lt;p&gt;The only supported value is &lt;code&gt;generic&lt;/code&gt;.&lt;/p&gt; (required)
     * @param _package The name of the package version to publish. (required)
     * @param version The package version to publish (for example, &lt;code&gt;3.5.2&lt;/code&gt;). (required)
     * @param asset The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: &lt;code&gt;~ ! @ ^ &amp;amp; ( ) - &#x60; _ + [ ] { } ; , . &#x60;&lt;/code&gt;  (required)
     * @param xAmzContentSha257 &lt;p&gt;The SHA256 hash of the &lt;code&gt;assetContent&lt;/code&gt; to publish. This value must be calculated by the caller and provided with the request (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\&quot;&gt;Publishing a generic package&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;This value is used as an integrity check to verify that the &lt;code&gt;assetContent&lt;/code&gt; has not changed after it was originally sent.&lt;/p&gt; (required)
     * @param publishPackageVersionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces. (optional)
     * @param namespace The namespace of the package version to publish. (optional)
     * @param unfinished &lt;p&gt;Specifies whether the package version should remain in the &lt;code&gt;unfinished&lt;/code&gt; state. If omitted, the package version status will be set to &lt;code&gt;Published&lt;/code&gt; (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;unfinished&lt;/code&gt; &lt;/p&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call publishPackageVersionCall(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha257, PublishPackageVersionRequest publishPackageVersionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Boolean unfinished, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = publishPackageVersionRequest;

        // create path and map variables
        String localVarPath = "/v1/package/version/publish#domain&repository&format&package&version&asset&x-amz-content-sha256";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (asset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("asset", asset));
        }

        if (unfinished != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("unfinished", unfinished));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        if (xAmzContentSha257 != null) {
            localVarHeaderParams.put("x-amz-content-sha256", localVarApiClient.parameterToString(xAmzContentSha257));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call publishPackageVersionValidateBeforeCall(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha257, PublishPackageVersionRequest publishPackageVersionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Boolean unfinished, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter 'asset' is set
        if (asset == null) {
            throw new ApiException("Missing the required parameter 'asset' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter 'xAmzContentSha257' is set
        if (xAmzContentSha257 == null) {
            throw new ApiException("Missing the required parameter 'xAmzContentSha257' when calling publishPackageVersion(Async)");
        }

        // verify the required parameter 'publishPackageVersionRequest' is set
        if (publishPackageVersionRequest == null) {
            throw new ApiException("Missing the required parameter 'publishPackageVersionRequest' when calling publishPackageVersion(Async)");
        }

        return publishPackageVersionCall(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished, _callback);

    }

    /**
     * 
     * &lt;p&gt;Creates a new package version containing one or more assets (or files).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;unfinished&lt;/code&gt; flag can be used to keep the package version in the &lt;code&gt;Unfinished&lt;/code&gt; state until all of its assets have been uploaded (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact user guide&lt;/i&gt;). To set the package version’s status to &lt;code&gt;Published&lt;/code&gt;, omit the &lt;code&gt;unfinished&lt;/code&gt; flag when uploading the final asset, or set the status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionStatus&lt;/a&gt;. Once a package version’s status is set to &lt;code&gt;Published&lt;/code&gt;, it cannot change back to &lt;code&gt;Unfinished&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only generic packages can be published using this API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\&quot;&gt;Using generic packages&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     * @param domain The name of the domain that contains the repository that contains the package version to publish. (required)
     * @param repository The name of the repository that the package version will be published to. (required)
     * @param format &lt;p&gt;A format that specifies the type of the package version with the requested asset file.&lt;/p&gt; &lt;p&gt;The only supported value is &lt;code&gt;generic&lt;/code&gt;.&lt;/p&gt; (required)
     * @param _package The name of the package version to publish. (required)
     * @param version The package version to publish (for example, &lt;code&gt;3.5.2&lt;/code&gt;). (required)
     * @param asset The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: &lt;code&gt;~ ! @ ^ &amp;amp; ( ) - &#x60; _ + [ ] { } ; , . &#x60;&lt;/code&gt;  (required)
     * @param xAmzContentSha257 &lt;p&gt;The SHA256 hash of the &lt;code&gt;assetContent&lt;/code&gt; to publish. This value must be calculated by the caller and provided with the request (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\&quot;&gt;Publishing a generic package&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;This value is used as an integrity check to verify that the &lt;code&gt;assetContent&lt;/code&gt; has not changed after it was originally sent.&lt;/p&gt; (required)
     * @param publishPackageVersionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces. (optional)
     * @param namespace The namespace of the package version to publish. (optional)
     * @param unfinished &lt;p&gt;Specifies whether the package version should remain in the &lt;code&gt;unfinished&lt;/code&gt; state. If omitted, the package version status will be set to &lt;code&gt;Published&lt;/code&gt; (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;unfinished&lt;/code&gt; &lt;/p&gt; (optional)
     * @return PublishPackageVersionResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PublishPackageVersionResult publishPackageVersion(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha257, PublishPackageVersionRequest publishPackageVersionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Boolean unfinished) throws ApiException {
        ApiResponse<PublishPackageVersionResult> localVarResp = publishPackageVersionWithHttpInfo(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Creates a new package version containing one or more assets (or files).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;unfinished&lt;/code&gt; flag can be used to keep the package version in the &lt;code&gt;Unfinished&lt;/code&gt; state until all of its assets have been uploaded (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact user guide&lt;/i&gt;). To set the package version’s status to &lt;code&gt;Published&lt;/code&gt;, omit the &lt;code&gt;unfinished&lt;/code&gt; flag when uploading the final asset, or set the status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionStatus&lt;/a&gt;. Once a package version’s status is set to &lt;code&gt;Published&lt;/code&gt;, it cannot change back to &lt;code&gt;Unfinished&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only generic packages can be published using this API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\&quot;&gt;Using generic packages&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     * @param domain The name of the domain that contains the repository that contains the package version to publish. (required)
     * @param repository The name of the repository that the package version will be published to. (required)
     * @param format &lt;p&gt;A format that specifies the type of the package version with the requested asset file.&lt;/p&gt; &lt;p&gt;The only supported value is &lt;code&gt;generic&lt;/code&gt;.&lt;/p&gt; (required)
     * @param _package The name of the package version to publish. (required)
     * @param version The package version to publish (for example, &lt;code&gt;3.5.2&lt;/code&gt;). (required)
     * @param asset The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: &lt;code&gt;~ ! @ ^ &amp;amp; ( ) - &#x60; _ + [ ] { } ; , . &#x60;&lt;/code&gt;  (required)
     * @param xAmzContentSha257 &lt;p&gt;The SHA256 hash of the &lt;code&gt;assetContent&lt;/code&gt; to publish. This value must be calculated by the caller and provided with the request (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\&quot;&gt;Publishing a generic package&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;This value is used as an integrity check to verify that the &lt;code&gt;assetContent&lt;/code&gt; has not changed after it was originally sent.&lt;/p&gt; (required)
     * @param publishPackageVersionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces. (optional)
     * @param namespace The namespace of the package version to publish. (optional)
     * @param unfinished &lt;p&gt;Specifies whether the package version should remain in the &lt;code&gt;unfinished&lt;/code&gt; state. If omitted, the package version status will be set to &lt;code&gt;Published&lt;/code&gt; (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;unfinished&lt;/code&gt; &lt;/p&gt; (optional)
     * @return ApiResponse&lt;PublishPackageVersionResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PublishPackageVersionResult> publishPackageVersionWithHttpInfo(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha257, PublishPackageVersionRequest publishPackageVersionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Boolean unfinished) throws ApiException {
        okhttp3.Call localVarCall = publishPackageVersionValidateBeforeCall(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished, null);
        Type localVarReturnType = new TypeToken<PublishPackageVersionResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Creates a new package version containing one or more assets (or files).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;unfinished&lt;/code&gt; flag can be used to keep the package version in the &lt;code&gt;Unfinished&lt;/code&gt; state until all of its assets have been uploaded (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact user guide&lt;/i&gt;). To set the package version’s status to &lt;code&gt;Published&lt;/code&gt;, omit the &lt;code&gt;unfinished&lt;/code&gt; flag when uploading the final asset, or set the status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionStatus&lt;/a&gt;. Once a package version’s status is set to &lt;code&gt;Published&lt;/code&gt;, it cannot change back to &lt;code&gt;Unfinished&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only generic packages can be published using this API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\&quot;&gt;Using generic packages&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     * @param domain The name of the domain that contains the repository that contains the package version to publish. (required)
     * @param repository The name of the repository that the package version will be published to. (required)
     * @param format &lt;p&gt;A format that specifies the type of the package version with the requested asset file.&lt;/p&gt; &lt;p&gt;The only supported value is &lt;code&gt;generic&lt;/code&gt;.&lt;/p&gt; (required)
     * @param _package The name of the package version to publish. (required)
     * @param version The package version to publish (for example, &lt;code&gt;3.5.2&lt;/code&gt;). (required)
     * @param asset The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: &lt;code&gt;~ ! @ ^ &amp;amp; ( ) - &#x60; _ + [ ] { } ; , . &#x60;&lt;/code&gt;  (required)
     * @param xAmzContentSha257 &lt;p&gt;The SHA256 hash of the &lt;code&gt;assetContent&lt;/code&gt; to publish. This value must be calculated by the caller and provided with the request (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\&quot;&gt;Publishing a generic package&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;This value is used as an integrity check to verify that the &lt;code&gt;assetContent&lt;/code&gt; has not changed after it was originally sent.&lt;/p&gt; (required)
     * @param publishPackageVersionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces. (optional)
     * @param namespace The namespace of the package version to publish. (optional)
     * @param unfinished &lt;p&gt;Specifies whether the package version should remain in the &lt;code&gt;unfinished&lt;/code&gt; state. If omitted, the package version status will be set to &lt;code&gt;Published&lt;/code&gt; (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;unfinished&lt;/code&gt; &lt;/p&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call publishPackageVersionAsync(String domain, String repository, String format, String _package, String version, String asset, String xAmzContentSha257, PublishPackageVersionRequest publishPackageVersionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, Boolean unfinished, final ApiCallback<PublishPackageVersionResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = publishPackageVersionValidateBeforeCall(domain, repository, format, _package, version, asset, xAmzContentSha257, publishPackageVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, unfinished, _callback);
        Type localVarReturnType = new TypeToken<PublishPackageVersionResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putDomainPermissionsPolicy
     * @param putDomainPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDomainPermissionsPolicyCall(PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putDomainPermissionsPolicyRequest;

        // create path and map variables
        String localVarPath = "/v1/domain/permissions/policy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putDomainPermissionsPolicyValidateBeforeCall(PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'putDomainPermissionsPolicyRequest' is set
        if (putDomainPermissionsPolicyRequest == null) {
            throw new ApiException("Missing the required parameter 'putDomainPermissionsPolicyRequest' when calling putDomainPermissionsPolicy(Async)");
        }

        return putDomainPermissionsPolicyCall(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt; Sets a resource policy on a domain that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     * @param putDomainPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return PutDomainPermissionsPolicyResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PutDomainPermissionsPolicyResult putDomainPermissionsPolicy(PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<PutDomainPermissionsPolicyResult> localVarResp = putDomainPermissionsPolicyWithHttpInfo(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Sets a resource policy on a domain that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     * @param putDomainPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;PutDomainPermissionsPolicyResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutDomainPermissionsPolicyResult> putDomainPermissionsPolicyWithHttpInfo(PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putDomainPermissionsPolicyValidateBeforeCall(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<PutDomainPermissionsPolicyResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Sets a resource policy on a domain that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     * @param putDomainPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDomainPermissionsPolicyAsync(PutDomainPermissionsPolicyRequest putDomainPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<PutDomainPermissionsPolicyResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = putDomainPermissionsPolicyValidateBeforeCall(putDomainPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<PutDomainPermissionsPolicyResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putPackageOriginConfiguration
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the package. (required)
     * @param format A format that specifies the type of the package to be updated. (required)
     * @param _package The name of the package to be updated. (required)
     * @param putPackageOriginConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putPackageOriginConfigurationCall(String domain, String repository, String format, String _package, PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putPackageOriginConfigurationRequest;

        // create path and map variables
        String localVarPath = "/v1/package#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putPackageOriginConfigurationValidateBeforeCall(String domain, String repository, String format, String _package, PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling putPackageOriginConfiguration(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling putPackageOriginConfiguration(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling putPackageOriginConfiguration(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling putPackageOriginConfiguration(Async)");
        }

        // verify the required parameter 'putPackageOriginConfigurationRequest' is set
        if (putPackageOriginConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'putPackageOriginConfigurationRequest' when calling putPackageOriginConfiguration(Async)");
        }

        return putPackageOriginConfigurationCall(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     * &lt;p&gt;Sets the package origin configuration for a package.&lt;/p&gt; &lt;p&gt;The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\&quot;&gt;Editing package origin controls&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt; can be called on a package that doesn&#39;t yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.&lt;/p&gt;
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the package. (required)
     * @param format A format that specifies the type of the package to be updated. (required)
     * @param _package The name of the package to be updated. (required)
     * @param putPackageOriginConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return PutPackageOriginConfigurationResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PutPackageOriginConfigurationResult putPackageOriginConfiguration(String domain, String repository, String format, String _package, PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<PutPackageOriginConfigurationResult> localVarResp = putPackageOriginConfigurationWithHttpInfo(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Sets the package origin configuration for a package.&lt;/p&gt; &lt;p&gt;The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\&quot;&gt;Editing package origin controls&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt; can be called on a package that doesn&#39;t yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.&lt;/p&gt;
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the package. (required)
     * @param format A format that specifies the type of the package to be updated. (required)
     * @param _package The name of the package to be updated. (required)
     * @param putPackageOriginConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;PutPackageOriginConfigurationResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutPackageOriginConfigurationResult> putPackageOriginConfigurationWithHttpInfo(String domain, String repository, String format, String _package, PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = putPackageOriginConfigurationValidateBeforeCall(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<PutPackageOriginConfigurationResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Sets the package origin configuration for a package.&lt;/p&gt; &lt;p&gt;The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\&quot;&gt;Editing package origin controls&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt; can be called on a package that doesn&#39;t yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.&lt;/p&gt;
     * @param domain The name of the domain that contains the repository that contains the package. (required)
     * @param repository The name of the repository that contains the package. (required)
     * @param format A format that specifies the type of the package to be updated. (required)
     * @param _package The name of the package to be updated. (required)
     * @param putPackageOriginConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putPackageOriginConfigurationAsync(String domain, String repository, String format, String _package, PutPackageOriginConfigurationRequest putPackageOriginConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<PutPackageOriginConfigurationResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = putPackageOriginConfigurationValidateBeforeCall(domain, repository, format, _package, putPackageOriginConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<PutPackageOriginConfigurationResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putRepositoryPermissionsPolicy
     * @param domain  The name of the domain containing the repository to set the resource policy on.  (required)
     * @param repository  The name of the repository to set the resource policy on.  (required)
     * @param putRepositoryPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putRepositoryPermissionsPolicyCall(String domain, String repository, PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putRepositoryPermissionsPolicyRequest;

        // create path and map variables
        String localVarPath = "/v1/repository/permissions/policy#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putRepositoryPermissionsPolicyValidateBeforeCall(String domain, String repository, PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling putRepositoryPermissionsPolicy(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling putRepositoryPermissionsPolicy(Async)");
        }

        // verify the required parameter 'putRepositoryPermissionsPolicyRequest' is set
        if (putRepositoryPermissionsPolicyRequest == null) {
            throw new ApiException("Missing the required parameter 'putRepositoryPermissionsPolicyRequest' when calling putRepositoryPermissionsPolicy(Async)");
        }

        return putRepositoryPermissionsPolicyCall(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     * &lt;p&gt; Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     * @param domain  The name of the domain containing the repository to set the resource policy on.  (required)
     * @param repository  The name of the repository to set the resource policy on.  (required)
     * @param putRepositoryPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return PutRepositoryPermissionsPolicyResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public PutRepositoryPermissionsPolicyResult putRepositoryPermissionsPolicy(String domain, String repository, PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<PutRepositoryPermissionsPolicyResult> localVarResp = putRepositoryPermissionsPolicyWithHttpInfo(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt; Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     * @param domain  The name of the domain containing the repository to set the resource policy on.  (required)
     * @param repository  The name of the repository to set the resource policy on.  (required)
     * @param putRepositoryPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;PutRepositoryPermissionsPolicyResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutRepositoryPermissionsPolicyResult> putRepositoryPermissionsPolicyWithHttpInfo(String domain, String repository, PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = putRepositoryPermissionsPolicyValidateBeforeCall(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<PutRepositoryPermissionsPolicyResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt; Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. &lt;/p&gt;
     * @param domain  The name of the domain containing the repository to set the resource policy on.  (required)
     * @param repository  The name of the repository to set the resource policy on.  (required)
     * @param putRepositoryPermissionsPolicyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putRepositoryPermissionsPolicyAsync(String domain, String repository, PutRepositoryPermissionsPolicyRequest putRepositoryPermissionsPolicyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<PutRepositoryPermissionsPolicyResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = putRepositoryPermissionsPolicyValidateBeforeCall(domain, repository, putRepositoryPermissionsPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<PutRepositoryPermissionsPolicyResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for tagResource
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to add or update tags for. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceCall(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = tagResourceRequest;

        // create path and map variables
        String localVarPath = "/v1/tag#resourceArn";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (resourceArn != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("resourceArn", resourceArn));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call tagResourceValidateBeforeCall(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling tagResource(Async)");
        }

        // verify the required parameter 'tagResourceRequest' is set
        if (tagResourceRequest == null) {
            throw new ApiException("Missing the required parameter 'tagResourceRequest' when calling tagResource(Async)");
        }

        return tagResourceCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Adds or updates tags for a resource in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to add or update tags for. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public Object tagResource(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = tagResourceWithHttpInfo(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Adds or updates tags for a resource in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to add or update tags for. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> tagResourceWithHttpInfo(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Adds or updates tags for a resource in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to add or update tags for. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceAsync(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for untagResource
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to remove tags from. (required)
     * @param untagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceCall(String resourceArn, UntagResourceRequest untagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = untagResourceRequest;

        // create path and map variables
        String localVarPath = "/v1/untag#resourceArn";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (resourceArn != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("resourceArn", resourceArn));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call untagResourceValidateBeforeCall(String resourceArn, UntagResourceRequest untagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling untagResource(Async)");
        }

        // verify the required parameter 'untagResourceRequest' is set
        if (untagResourceRequest == null) {
            throw new ApiException("Missing the required parameter 'untagResourceRequest' when calling untagResource(Async)");
        }

        return untagResourceCall(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Removes tags from a resource in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to remove tags from. (required)
     * @param untagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public Object untagResource(String resourceArn, UntagResourceRequest untagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = untagResourceWithHttpInfo(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Removes tags from a resource in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to remove tags from. (required)
     * @param untagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> untagResourceWithHttpInfo(String resourceArn, UntagResourceRequest untagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Removes tags from a resource in CodeArtifact.
     * @param resourceArn The Amazon Resource Name (ARN) of the resource that you want to remove tags from. (required)
     * @param untagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceAsync(String resourceArn, UntagResourceRequest untagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updatePackageVersionsStatus
     * @param domain  The name of the domain that contains the repository that contains the package versions with a status to be updated.  (required)
     * @param repository  The repository that contains the package versions with the status you want to update.  (required)
     * @param format  A format that specifies the type of the package with the statuses to update.  (required)
     * @param _package  The name of the package with the version statuses to update.  (required)
     * @param updatePackageVersionsStatusRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePackageVersionsStatusCall(String domain, String repository, String format, String _package, UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updatePackageVersionsStatusRequest;

        // create path and map variables
        String localVarPath = "/v1/package/versions/update_status#domain&repository&format&package";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (namespace != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("namespace", namespace));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updatePackageVersionsStatusValidateBeforeCall(String domain, String repository, String format, String _package, UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling updatePackageVersionsStatus(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling updatePackageVersionsStatus(Async)");
        }

        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling updatePackageVersionsStatus(Async)");
        }

        // verify the required parameter '_package' is set
        if (_package == null) {
            throw new ApiException("Missing the required parameter '_package' when calling updatePackageVersionsStatus(Async)");
        }

        // verify the required parameter 'updatePackageVersionsStatusRequest' is set
        if (updatePackageVersionsStatusRequest == null) {
            throw new ApiException("Missing the required parameter 'updatePackageVersionsStatusRequest' when calling updatePackageVersionsStatus(Async)");
        }

        return updatePackageVersionsStatusCall(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);

    }

    /**
     * 
     *  Updates the status of one or more versions of a package. Using &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;, you can update the status of package versions to &lt;code&gt;Archived&lt;/code&gt;, &lt;code&gt;Published&lt;/code&gt;, or &lt;code&gt;Unlisted&lt;/code&gt;. To set the status of a package version to &lt;code&gt;Disposed&lt;/code&gt;, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\&quot;&gt;DisposePackageVersions&lt;/a&gt;. 
     * @param domain  The name of the domain that contains the repository that contains the package versions with a status to be updated.  (required)
     * @param repository  The repository that contains the package versions with the status you want to update.  (required)
     * @param format  A format that specifies the type of the package with the statuses to update.  (required)
     * @param _package  The name of the package with the version statuses to update.  (required)
     * @param updatePackageVersionsStatusRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return UpdatePackageVersionsStatusResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public UpdatePackageVersionsStatusResult updatePackageVersionsStatus(String domain, String repository, String format, String _package, UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        ApiResponse<UpdatePackageVersionsStatusResult> localVarResp = updatePackageVersionsStatusWithHttpInfo(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace);
        return localVarResp.getData();
    }

    /**
     * 
     *  Updates the status of one or more versions of a package. Using &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;, you can update the status of package versions to &lt;code&gt;Archived&lt;/code&gt;, &lt;code&gt;Published&lt;/code&gt;, or &lt;code&gt;Unlisted&lt;/code&gt;. To set the status of a package version to &lt;code&gt;Disposed&lt;/code&gt;, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\&quot;&gt;DisposePackageVersions&lt;/a&gt;. 
     * @param domain  The name of the domain that contains the repository that contains the package versions with a status to be updated.  (required)
     * @param repository  The repository that contains the package versions with the status you want to update.  (required)
     * @param format  A format that specifies the type of the package with the statuses to update.  (required)
     * @param _package  The name of the package with the version statuses to update.  (required)
     * @param updatePackageVersionsStatusRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @return ApiResponse&lt;UpdatePackageVersionsStatusResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdatePackageVersionsStatusResult> updatePackageVersionsStatusWithHttpInfo(String domain, String repository, String format, String _package, UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace) throws ApiException {
        okhttp3.Call localVarCall = updatePackageVersionsStatusValidateBeforeCall(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, null);
        Type localVarReturnType = new TypeToken<UpdatePackageVersionsStatusResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Updates the status of one or more versions of a package. Using &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;, you can update the status of package versions to &lt;code&gt;Archived&lt;/code&gt;, &lt;code&gt;Published&lt;/code&gt;, or &lt;code&gt;Unlisted&lt;/code&gt;. To set the status of a package version to &lt;code&gt;Disposed&lt;/code&gt;, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\&quot;&gt;DisposePackageVersions&lt;/a&gt;. 
     * @param domain  The name of the domain that contains the repository that contains the package versions with a status to be updated.  (required)
     * @param repository  The repository that contains the package versions with the status you want to update.  (required)
     * @param format  A format that specifies the type of the package with the statuses to update.  (required)
     * @param _package  The name of the package with the version statuses to update.  (required)
     * @param updatePackageVersionsStatusRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param namespace &lt;p&gt;The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePackageVersionsStatusAsync(String domain, String repository, String format, String _package, UpdatePackageVersionsStatusRequest updatePackageVersionsStatusRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, String namespace, final ApiCallback<UpdatePackageVersionsStatusResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = updatePackageVersionsStatusValidateBeforeCall(domain, repository, format, _package, updatePackageVersionsStatusRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, namespace, _callback);
        Type localVarReturnType = new TypeToken<UpdatePackageVersionsStatusResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateRepository
     * @param domain  The name of the domain associated with the repository to update.  (required)
     * @param repository  The name of the repository to update.  (required)
     * @param updateRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRepositoryCall(String domain, String repository, UpdateRepositoryRequest updateRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateRepositoryRequest;

        // create path and map variables
        String localVarPath = "/v1/repository#domain&repository";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (domainOwner != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain-owner", domainOwner));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateRepositoryValidateBeforeCall(String domain, String repository, UpdateRepositoryRequest updateRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling updateRepository(Async)");
        }

        // verify the required parameter 'repository' is set
        if (repository == null) {
            throw new ApiException("Missing the required parameter 'repository' when calling updateRepository(Async)");
        }

        // verify the required parameter 'updateRepositoryRequest' is set
        if (updateRepositoryRequest == null) {
            throw new ApiException("Missing the required parameter 'updateRepositoryRequest' when calling updateRepository(Async)");
        }

        return updateRepositoryCall(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);

    }

    /**
     * 
     *  Update the properties of a repository. 
     * @param domain  The name of the domain associated with the repository to update.  (required)
     * @param repository  The name of the repository to update.  (required)
     * @param updateRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return UpdateRepositoryResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public UpdateRepositoryResult updateRepository(String domain, String repository, UpdateRepositoryRequest updateRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        ApiResponse<UpdateRepositoryResult> localVarResp = updateRepositoryWithHttpInfo(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner);
        return localVarResp.getData();
    }

    /**
     * 
     *  Update the properties of a repository. 
     * @param domain  The name of the domain associated with the repository to update.  (required)
     * @param repository  The name of the repository to update.  (required)
     * @param updateRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @return ApiResponse&lt;UpdateRepositoryResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateRepositoryResult> updateRepositoryWithHttpInfo(String domain, String repository, UpdateRepositoryRequest updateRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner) throws ApiException {
        okhttp3.Call localVarCall = updateRepositoryValidateBeforeCall(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, null);
        Type localVarReturnType = new TypeToken<UpdateRepositoryResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     *  Update the properties of a repository. 
     * @param domain  The name of the domain associated with the repository to update.  (required)
     * @param repository  The name of the repository to update.  (required)
     * @param updateRepositoryRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param domainOwner  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRepositoryAsync(String domain, String repository, UpdateRepositoryRequest updateRepositoryRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String domainOwner, final ApiCallback<UpdateRepositoryResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateRepositoryValidateBeforeCall(domain, repository, updateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, domainOwner, _callback);
        Type localVarReturnType = new TypeToken<UpdateRepositoryResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
