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
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAssociateExternalConnectionResult.h"
#include "OAICopyPackageVersionsResult.h"
#include "OAICopyPackageVersions_request.h"
#include "OAICreateDomainResult.h"
#include "OAICreateDomain_request.h"
#include "OAICreateRepositoryResult.h"
#include "OAICreateRepository_request.h"
#include "OAIDeleteDomainPermissionsPolicyResult.h"
#include "OAIDeleteDomainResult.h"
#include "OAIDeletePackageResult.h"
#include "OAIDeletePackageVersionsResult.h"
#include "OAIDeletePackageVersions_request.h"
#include "OAIDeleteRepositoryPermissionsPolicyResult.h"
#include "OAIDeleteRepositoryResult.h"
#include "OAIDescribeDomainResult.h"
#include "OAIDescribePackageResult.h"
#include "OAIDescribePackageVersionResult.h"
#include "OAIDescribeRepositoryResult.h"
#include "OAIDisassociateExternalConnectionResult.h"
#include "OAIDisposePackageVersionsResult.h"
#include "OAIDisposePackageVersions_request.h"
#include "OAIGetAuthorizationTokenResult.h"
#include "OAIGetDomainPermissionsPolicyResult.h"
#include "OAIGetPackageVersionAssetResult.h"
#include "OAIGetPackageVersionReadmeResult.h"
#include "OAIGetRepositoryEndpointResult.h"
#include "OAIGetRepositoryPermissionsPolicyResult.h"
#include "OAIListDomainsResult.h"
#include "OAIListDomains_request.h"
#include "OAIListPackageVersionAssetsResult.h"
#include "OAIListPackageVersionDependenciesResult.h"
#include "OAIListPackageVersionsResult.h"
#include "OAIListPackagesResult.h"
#include "OAIListRepositoriesInDomainResult.h"
#include "OAIListRepositoriesResult.h"
#include "OAIListTagsForResourceResult.h"
#include "OAIObject.h"
#include "OAIPublishPackageVersionResult.h"
#include "OAIPublishPackageVersion_request.h"
#include "OAIPutDomainPermissionsPolicyResult.h"
#include "OAIPutDomainPermissionsPolicy_request.h"
#include "OAIPutPackageOriginConfigurationResult.h"
#include "OAIPutPackageOriginConfiguration_request.h"
#include "OAIPutRepositoryPermissionsPolicyResult.h"
#include "OAIPutRepositoryPermissionsPolicy_request.h"
#include "OAITagResource_request.h"
#include "OAIUntagResource_request.h"
#include "OAIUpdatePackageVersionsStatusResult.h"
#include "OAIUpdatePackageVersionsStatus_request.h"
#include "OAIUpdateRepositoryResult.h"
#include "OAIUpdateRepository_request.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  external_connection QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void associateExternalConnection(const QString &domain, const QString &repository, const QString &external_connection, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  source_repository QString [required]
    * @param[in]  destination_repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  oai_copy_package_versions_request OAICopyPackageVersions_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void copyPackageVersions(const QString &domain, const QString &source_repository, const QString &destination_repository, const QString &format, const QString &package, const OAICopyPackageVersions_request &oai_copy_package_versions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  oai_create_domain_request OAICreateDomain_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createDomain(const QString &domain, const OAICreateDomain_request &oai_create_domain_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  oai_create_repository_request OAICreateRepository_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void createRepository(const QString &domain, const QString &repository, const OAICreateRepository_request &oai_create_repository_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void deleteDomain(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  policy_revision QString [optional]
    */
    virtual void deleteDomainPermissionsPolicy(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &policy_revision = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void deletePackage(const QString &domain, const QString &repository, const QString &format, const QString &package, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  oai_delete_package_versions_request OAIDeletePackageVersions_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void deletePackageVersions(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIDeletePackageVersions_request &oai_delete_package_versions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void deleteRepository(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  policy_revision QString [optional]
    */
    virtual void deleteRepositoryPermissionsPolicy(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &policy_revision = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void describeDomain(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void describePackage(const QString &domain, const QString &repository, const QString &format, const QString &package, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  version QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void describePackageVersion(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void describeRepository(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  external_connection QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void disassociateExternalConnection(const QString &domain, const QString &repository, const QString &external_connection, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  oai_dispose_package_versions_request OAIDisposePackageVersions_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void disposePackageVersions(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIDisposePackageVersions_request &oai_dispose_package_versions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  duration qint32 [optional]
    */
    virtual void getAuthorizationToken(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &duration = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void getDomainPermissionsPolicy(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  version QString [required]
    * @param[in]  asset QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    * @param[in]  revision QString [optional]
    */
    virtual void getPackageVersionAsset(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const QString &asset, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &revision = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  version QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void getPackageVersionReadme(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void getRepositoryEndpoint(const QString &domain, const QString &repository, const QString &format, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void getRepositoryPermissionsPolicy(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_domains_request OAIListDomains_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listDomains(const OAIListDomains_request &oai_list_domains_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  version QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  max_results2 QString [optional]
    * @param[in]  next_token2 QString [optional]
    */
    virtual void listPackageVersionAssets(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results2 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token2 = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  version QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listPackageVersionDependencies(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    * @param[in]  status QString [optional]
    * @param[in]  sort_by QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  origin_type QString [optional]
    * @param[in]  max_results2 QString [optional]
    * @param[in]  next_token2 QString [optional]
    */
    virtual void listPackageVersions(const QString &domain, const QString &repository, const QString &format, const QString &package, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort_by = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &origin_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results2 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token2 = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  format QString [optional]
    * @param[in]  r_namespace QString [optional]
    * @param[in]  package_prefix QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  publish QString [optional]
    * @param[in]  upstream QString [optional]
    * @param[in]  max_results2 QString [optional]
    * @param[in]  next_token2 QString [optional]
    */
    virtual void listPackages(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &package_prefix = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &publish = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upstream = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results2 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token2 = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  repository_prefix QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  max_results2 QString [optional]
    * @param[in]  next_token2 QString [optional]
    */
    virtual void listRepositories(const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &repository_prefix = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results2 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token2 = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  administrator_account QString [optional]
    * @param[in]  repository_prefix QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  next_token QString [optional]
    * @param[in]  max_results2 QString [optional]
    * @param[in]  next_token2 QString [optional]
    */
    virtual void listRepositoriesInDomain(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &administrator_account = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &repository_prefix = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results2 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token2 = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void listTagsForResource(const QString &resource_arn, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  version QString [required]
    * @param[in]  asset QString [required]
    * @param[in]  x_amz_content_sha257 QString [required]
    * @param[in]  oai_publish_package_version_request OAIPublishPackageVersion_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    * @param[in]  unfinished bool [optional]
    */
    virtual void publishPackageVersion(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const QString &asset, const QString &x_amz_content_sha257, const OAIPublishPackageVersion_request &oai_publish_package_version_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &unfinished = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  oai_put_domain_permissions_policy_request OAIPutDomainPermissionsPolicy_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void putDomainPermissionsPolicy(const OAIPutDomainPermissionsPolicy_request &oai_put_domain_permissions_policy_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  oai_put_package_origin_configuration_request OAIPutPackageOriginConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void putPackageOriginConfiguration(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIPutPackageOriginConfiguration_request &oai_put_package_origin_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  oai_put_repository_permissions_policy_request OAIPutRepositoryPermissionsPolicy_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void putRepositoryPermissionsPolicy(const QString &domain, const QString &repository, const OAIPutRepositoryPermissionsPolicy_request &oai_put_repository_permissions_policy_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  oai_tag_resource_request OAITagResource_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void tagResource(const QString &resource_arn, const OAITagResource_request &oai_tag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  oai_untag_resource_request OAIUntagResource_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void untagResource(const QString &resource_arn, const OAIUntagResource_request &oai_untag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  format QString [required]
    * @param[in]  package QString [required]
    * @param[in]  oai_update_package_versions_status_request OAIUpdatePackageVersionsStatus_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    * @param[in]  r_namespace QString [optional]
    */
    virtual void updatePackageVersionsStatus(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIUpdatePackageVersionsStatus_request &oai_update_package_versions_status_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &r_namespace = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain QString [required]
    * @param[in]  repository QString [required]
    * @param[in]  oai_update_repository_request OAIUpdateRepository_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  domain_owner QString [optional]
    */
    virtual void updateRepository(const QString &domain, const QString &repository, const OAIUpdateRepository_request &oai_update_repository_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &domain_owner = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void associateExternalConnectionCallback(OAIHttpRequestWorker *worker);
    void copyPackageVersionsCallback(OAIHttpRequestWorker *worker);
    void createDomainCallback(OAIHttpRequestWorker *worker);
    void createRepositoryCallback(OAIHttpRequestWorker *worker);
    void deleteDomainCallback(OAIHttpRequestWorker *worker);
    void deleteDomainPermissionsPolicyCallback(OAIHttpRequestWorker *worker);
    void deletePackageCallback(OAIHttpRequestWorker *worker);
    void deletePackageVersionsCallback(OAIHttpRequestWorker *worker);
    void deleteRepositoryCallback(OAIHttpRequestWorker *worker);
    void deleteRepositoryPermissionsPolicyCallback(OAIHttpRequestWorker *worker);
    void describeDomainCallback(OAIHttpRequestWorker *worker);
    void describePackageCallback(OAIHttpRequestWorker *worker);
    void describePackageVersionCallback(OAIHttpRequestWorker *worker);
    void describeRepositoryCallback(OAIHttpRequestWorker *worker);
    void disassociateExternalConnectionCallback(OAIHttpRequestWorker *worker);
    void disposePackageVersionsCallback(OAIHttpRequestWorker *worker);
    void getAuthorizationTokenCallback(OAIHttpRequestWorker *worker);
    void getDomainPermissionsPolicyCallback(OAIHttpRequestWorker *worker);
    void getPackageVersionAssetCallback(OAIHttpRequestWorker *worker);
    void getPackageVersionReadmeCallback(OAIHttpRequestWorker *worker);
    void getRepositoryEndpointCallback(OAIHttpRequestWorker *worker);
    void getRepositoryPermissionsPolicyCallback(OAIHttpRequestWorker *worker);
    void listDomainsCallback(OAIHttpRequestWorker *worker);
    void listPackageVersionAssetsCallback(OAIHttpRequestWorker *worker);
    void listPackageVersionDependenciesCallback(OAIHttpRequestWorker *worker);
    void listPackageVersionsCallback(OAIHttpRequestWorker *worker);
    void listPackagesCallback(OAIHttpRequestWorker *worker);
    void listRepositoriesCallback(OAIHttpRequestWorker *worker);
    void listRepositoriesInDomainCallback(OAIHttpRequestWorker *worker);
    void listTagsForResourceCallback(OAIHttpRequestWorker *worker);
    void publishPackageVersionCallback(OAIHttpRequestWorker *worker);
    void putDomainPermissionsPolicyCallback(OAIHttpRequestWorker *worker);
    void putPackageOriginConfigurationCallback(OAIHttpRequestWorker *worker);
    void putRepositoryPermissionsPolicyCallback(OAIHttpRequestWorker *worker);
    void tagResourceCallback(OAIHttpRequestWorker *worker);
    void untagResourceCallback(OAIHttpRequestWorker *worker);
    void updatePackageVersionsStatusCallback(OAIHttpRequestWorker *worker);
    void updateRepositoryCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void associateExternalConnectionSignal(OAIAssociateExternalConnectionResult summary);
    void copyPackageVersionsSignal(OAICopyPackageVersionsResult summary);
    void createDomainSignal(OAICreateDomainResult summary);
    void createRepositorySignal(OAICreateRepositoryResult summary);
    void deleteDomainSignal(OAIDeleteDomainResult summary);
    void deleteDomainPermissionsPolicySignal(OAIDeleteDomainPermissionsPolicyResult summary);
    void deletePackageSignal(OAIDeletePackageResult summary);
    void deletePackageVersionsSignal(OAIDeletePackageVersionsResult summary);
    void deleteRepositorySignal(OAIDeleteRepositoryResult summary);
    void deleteRepositoryPermissionsPolicySignal(OAIDeleteRepositoryPermissionsPolicyResult summary);
    void describeDomainSignal(OAIDescribeDomainResult summary);
    void describePackageSignal(OAIDescribePackageResult summary);
    void describePackageVersionSignal(OAIDescribePackageVersionResult summary);
    void describeRepositorySignal(OAIDescribeRepositoryResult summary);
    void disassociateExternalConnectionSignal(OAIDisassociateExternalConnectionResult summary);
    void disposePackageVersionsSignal(OAIDisposePackageVersionsResult summary);
    void getAuthorizationTokenSignal(OAIGetAuthorizationTokenResult summary);
    void getDomainPermissionsPolicySignal(OAIGetDomainPermissionsPolicyResult summary);
    void getPackageVersionAssetSignal(OAIGetPackageVersionAssetResult summary);
    void getPackageVersionReadmeSignal(OAIGetPackageVersionReadmeResult summary);
    void getRepositoryEndpointSignal(OAIGetRepositoryEndpointResult summary);
    void getRepositoryPermissionsPolicySignal(OAIGetRepositoryPermissionsPolicyResult summary);
    void listDomainsSignal(OAIListDomainsResult summary);
    void listPackageVersionAssetsSignal(OAIListPackageVersionAssetsResult summary);
    void listPackageVersionDependenciesSignal(OAIListPackageVersionDependenciesResult summary);
    void listPackageVersionsSignal(OAIListPackageVersionsResult summary);
    void listPackagesSignal(OAIListPackagesResult summary);
    void listRepositoriesSignal(OAIListRepositoriesResult summary);
    void listRepositoriesInDomainSignal(OAIListRepositoriesInDomainResult summary);
    void listTagsForResourceSignal(OAIListTagsForResourceResult summary);
    void publishPackageVersionSignal(OAIPublishPackageVersionResult summary);
    void putDomainPermissionsPolicySignal(OAIPutDomainPermissionsPolicyResult summary);
    void putPackageOriginConfigurationSignal(OAIPutPackageOriginConfigurationResult summary);
    void putRepositoryPermissionsPolicySignal(OAIPutRepositoryPermissionsPolicyResult summary);
    void tagResourceSignal(OAIObject summary);
    void untagResourceSignal(OAIObject summary);
    void updatePackageVersionsStatusSignal(OAIUpdatePackageVersionsStatusResult summary);
    void updateRepositorySignal(OAIUpdateRepositoryResult summary);


    void associateExternalConnectionSignalFull(OAIHttpRequestWorker *worker, OAIAssociateExternalConnectionResult summary);
    void copyPackageVersionsSignalFull(OAIHttpRequestWorker *worker, OAICopyPackageVersionsResult summary);
    void createDomainSignalFull(OAIHttpRequestWorker *worker, OAICreateDomainResult summary);
    void createRepositorySignalFull(OAIHttpRequestWorker *worker, OAICreateRepositoryResult summary);
    void deleteDomainSignalFull(OAIHttpRequestWorker *worker, OAIDeleteDomainResult summary);
    void deleteDomainPermissionsPolicySignalFull(OAIHttpRequestWorker *worker, OAIDeleteDomainPermissionsPolicyResult summary);
    void deletePackageSignalFull(OAIHttpRequestWorker *worker, OAIDeletePackageResult summary);
    void deletePackageVersionsSignalFull(OAIHttpRequestWorker *worker, OAIDeletePackageVersionsResult summary);
    void deleteRepositorySignalFull(OAIHttpRequestWorker *worker, OAIDeleteRepositoryResult summary);
    void deleteRepositoryPermissionsPolicySignalFull(OAIHttpRequestWorker *worker, OAIDeleteRepositoryPermissionsPolicyResult summary);
    void describeDomainSignalFull(OAIHttpRequestWorker *worker, OAIDescribeDomainResult summary);
    void describePackageSignalFull(OAIHttpRequestWorker *worker, OAIDescribePackageResult summary);
    void describePackageVersionSignalFull(OAIHttpRequestWorker *worker, OAIDescribePackageVersionResult summary);
    void describeRepositorySignalFull(OAIHttpRequestWorker *worker, OAIDescribeRepositoryResult summary);
    void disassociateExternalConnectionSignalFull(OAIHttpRequestWorker *worker, OAIDisassociateExternalConnectionResult summary);
    void disposePackageVersionsSignalFull(OAIHttpRequestWorker *worker, OAIDisposePackageVersionsResult summary);
    void getAuthorizationTokenSignalFull(OAIHttpRequestWorker *worker, OAIGetAuthorizationTokenResult summary);
    void getDomainPermissionsPolicySignalFull(OAIHttpRequestWorker *worker, OAIGetDomainPermissionsPolicyResult summary);
    void getPackageVersionAssetSignalFull(OAIHttpRequestWorker *worker, OAIGetPackageVersionAssetResult summary);
    void getPackageVersionReadmeSignalFull(OAIHttpRequestWorker *worker, OAIGetPackageVersionReadmeResult summary);
    void getRepositoryEndpointSignalFull(OAIHttpRequestWorker *worker, OAIGetRepositoryEndpointResult summary);
    void getRepositoryPermissionsPolicySignalFull(OAIHttpRequestWorker *worker, OAIGetRepositoryPermissionsPolicyResult summary);
    void listDomainsSignalFull(OAIHttpRequestWorker *worker, OAIListDomainsResult summary);
    void listPackageVersionAssetsSignalFull(OAIHttpRequestWorker *worker, OAIListPackageVersionAssetsResult summary);
    void listPackageVersionDependenciesSignalFull(OAIHttpRequestWorker *worker, OAIListPackageVersionDependenciesResult summary);
    void listPackageVersionsSignalFull(OAIHttpRequestWorker *worker, OAIListPackageVersionsResult summary);
    void listPackagesSignalFull(OAIHttpRequestWorker *worker, OAIListPackagesResult summary);
    void listRepositoriesSignalFull(OAIHttpRequestWorker *worker, OAIListRepositoriesResult summary);
    void listRepositoriesInDomainSignalFull(OAIHttpRequestWorker *worker, OAIListRepositoriesInDomainResult summary);
    void listTagsForResourceSignalFull(OAIHttpRequestWorker *worker, OAIListTagsForResourceResult summary);
    void publishPackageVersionSignalFull(OAIHttpRequestWorker *worker, OAIPublishPackageVersionResult summary);
    void putDomainPermissionsPolicySignalFull(OAIHttpRequestWorker *worker, OAIPutDomainPermissionsPolicyResult summary);
    void putPackageOriginConfigurationSignalFull(OAIHttpRequestWorker *worker, OAIPutPackageOriginConfigurationResult summary);
    void putRepositoryPermissionsPolicySignalFull(OAIHttpRequestWorker *worker, OAIPutRepositoryPermissionsPolicyResult summary);
    void tagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void untagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updatePackageVersionsStatusSignalFull(OAIHttpRequestWorker *worker, OAIUpdatePackageVersionsStatusResult summary);
    void updateRepositorySignalFull(OAIHttpRequestWorker *worker, OAIUpdateRepositoryResult summary);

    Q_DECL_DEPRECATED_X("Use associateExternalConnectionSignalError() instead")
    void associateExternalConnectionSignalE(OAIAssociateExternalConnectionResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void associateExternalConnectionSignalError(OAIAssociateExternalConnectionResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use copyPackageVersionsSignalError() instead")
    void copyPackageVersionsSignalE(OAICopyPackageVersionsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void copyPackageVersionsSignalError(OAICopyPackageVersionsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createDomainSignalError() instead")
    void createDomainSignalE(OAICreateDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createDomainSignalError(OAICreateDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRepositorySignalError() instead")
    void createRepositorySignalE(OAICreateRepositoryResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createRepositorySignalError(OAICreateRepositoryResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDomainSignalError() instead")
    void deleteDomainSignalE(OAIDeleteDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDomainSignalError(OAIDeleteDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDomainPermissionsPolicySignalError() instead")
    void deleteDomainPermissionsPolicySignalE(OAIDeleteDomainPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDomainPermissionsPolicySignalError(OAIDeleteDomainPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePackageSignalError() instead")
    void deletePackageSignalE(OAIDeletePackageResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePackageSignalError(OAIDeletePackageResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePackageVersionsSignalError() instead")
    void deletePackageVersionsSignalE(OAIDeletePackageVersionsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePackageVersionsSignalError(OAIDeletePackageVersionsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositorySignalError() instead")
    void deleteRepositorySignalE(OAIDeleteRepositoryResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositorySignalError(OAIDeleteRepositoryResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositoryPermissionsPolicySignalError() instead")
    void deleteRepositoryPermissionsPolicySignalE(OAIDeleteRepositoryPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositoryPermissionsPolicySignalError(OAIDeleteRepositoryPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describeDomainSignalError() instead")
    void describeDomainSignalE(OAIDescribeDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void describeDomainSignalError(OAIDescribeDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describePackageSignalError() instead")
    void describePackageSignalE(OAIDescribePackageResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void describePackageSignalError(OAIDescribePackageResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describePackageVersionSignalError() instead")
    void describePackageVersionSignalE(OAIDescribePackageVersionResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void describePackageVersionSignalError(OAIDescribePackageVersionResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describeRepositorySignalError() instead")
    void describeRepositorySignalE(OAIDescribeRepositoryResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void describeRepositorySignalError(OAIDescribeRepositoryResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disassociateExternalConnectionSignalError() instead")
    void disassociateExternalConnectionSignalE(OAIDisassociateExternalConnectionResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void disassociateExternalConnectionSignalError(OAIDisassociateExternalConnectionResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disposePackageVersionsSignalError() instead")
    void disposePackageVersionsSignalE(OAIDisposePackageVersionsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void disposePackageVersionsSignalError(OAIDisposePackageVersionsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAuthorizationTokenSignalError() instead")
    void getAuthorizationTokenSignalE(OAIGetAuthorizationTokenResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAuthorizationTokenSignalError(OAIGetAuthorizationTokenResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDomainPermissionsPolicySignalError() instead")
    void getDomainPermissionsPolicySignalE(OAIGetDomainPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDomainPermissionsPolicySignalError(OAIGetDomainPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPackageVersionAssetSignalError() instead")
    void getPackageVersionAssetSignalE(OAIGetPackageVersionAssetResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPackageVersionAssetSignalError(OAIGetPackageVersionAssetResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPackageVersionReadmeSignalError() instead")
    void getPackageVersionReadmeSignalE(OAIGetPackageVersionReadmeResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPackageVersionReadmeSignalError(OAIGetPackageVersionReadmeResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositoryEndpointSignalError() instead")
    void getRepositoryEndpointSignalE(OAIGetRepositoryEndpointResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositoryEndpointSignalError(OAIGetRepositoryEndpointResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositoryPermissionsPolicySignalError() instead")
    void getRepositoryPermissionsPolicySignalE(OAIGetRepositoryPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositoryPermissionsPolicySignalError(OAIGetRepositoryPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDomainsSignalError() instead")
    void listDomainsSignalE(OAIListDomainsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listDomainsSignalError(OAIListDomainsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackageVersionAssetsSignalError() instead")
    void listPackageVersionAssetsSignalE(OAIListPackageVersionAssetsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackageVersionAssetsSignalError(OAIListPackageVersionAssetsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackageVersionDependenciesSignalError() instead")
    void listPackageVersionDependenciesSignalE(OAIListPackageVersionDependenciesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackageVersionDependenciesSignalError(OAIListPackageVersionDependenciesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackageVersionsSignalError() instead")
    void listPackageVersionsSignalE(OAIListPackageVersionsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackageVersionsSignalError(OAIListPackageVersionsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackagesSignalError() instead")
    void listPackagesSignalE(OAIListPackagesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackagesSignalError(OAIListPackagesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesSignalError() instead")
    void listRepositoriesSignalE(OAIListRepositoriesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesSignalError(OAIListRepositoriesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesInDomainSignalError() instead")
    void listRepositoriesInDomainSignalE(OAIListRepositoriesInDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesInDomainSignalError(OAIListRepositoriesInDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalError() instead")
    void listTagsForResourceSignalE(OAIListTagsForResourceResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalError(OAIListTagsForResourceResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use publishPackageVersionSignalError() instead")
    void publishPackageVersionSignalE(OAIPublishPackageVersionResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void publishPackageVersionSignalError(OAIPublishPackageVersionResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDomainPermissionsPolicySignalError() instead")
    void putDomainPermissionsPolicySignalE(OAIPutDomainPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putDomainPermissionsPolicySignalError(OAIPutDomainPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putPackageOriginConfigurationSignalError() instead")
    void putPackageOriginConfigurationSignalE(OAIPutPackageOriginConfigurationResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putPackageOriginConfigurationSignalError(OAIPutPackageOriginConfigurationResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putRepositoryPermissionsPolicySignalError() instead")
    void putRepositoryPermissionsPolicySignalE(OAIPutRepositoryPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putRepositoryPermissionsPolicySignalError(OAIPutRepositoryPermissionsPolicyResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalError() instead")
    void tagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalError() instead")
    void untagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePackageVersionsStatusSignalError() instead")
    void updatePackageVersionsStatusSignalE(OAIUpdatePackageVersionsStatusResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePackageVersionsStatusSignalError(OAIUpdatePackageVersionsStatusResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRepositorySignalError() instead")
    void updateRepositorySignalE(OAIUpdateRepositoryResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateRepositorySignalError(OAIUpdateRepositoryResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use associateExternalConnectionSignalErrorFull() instead")
    void associateExternalConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void associateExternalConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use copyPackageVersionsSignalErrorFull() instead")
    void copyPackageVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void copyPackageVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createDomainSignalErrorFull() instead")
    void createDomainSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createDomainSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRepositorySignalErrorFull() instead")
    void createRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDomainSignalErrorFull() instead")
    void deleteDomainSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDomainSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDomainPermissionsPolicySignalErrorFull() instead")
    void deleteDomainPermissionsPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDomainPermissionsPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePackageSignalErrorFull() instead")
    void deletePackageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePackageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePackageVersionsSignalErrorFull() instead")
    void deletePackageVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePackageVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositorySignalErrorFull() instead")
    void deleteRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositoryPermissionsPolicySignalErrorFull() instead")
    void deleteRepositoryPermissionsPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositoryPermissionsPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describeDomainSignalErrorFull() instead")
    void describeDomainSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void describeDomainSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describePackageSignalErrorFull() instead")
    void describePackageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void describePackageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describePackageVersionSignalErrorFull() instead")
    void describePackageVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void describePackageVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describeRepositorySignalErrorFull() instead")
    void describeRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void describeRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disassociateExternalConnectionSignalErrorFull() instead")
    void disassociateExternalConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void disassociateExternalConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disposePackageVersionsSignalErrorFull() instead")
    void disposePackageVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void disposePackageVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAuthorizationTokenSignalErrorFull() instead")
    void getAuthorizationTokenSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAuthorizationTokenSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDomainPermissionsPolicySignalErrorFull() instead")
    void getDomainPermissionsPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDomainPermissionsPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPackageVersionAssetSignalErrorFull() instead")
    void getPackageVersionAssetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPackageVersionAssetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPackageVersionReadmeSignalErrorFull() instead")
    void getPackageVersionReadmeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPackageVersionReadmeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositoryEndpointSignalErrorFull() instead")
    void getRepositoryEndpointSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositoryEndpointSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositoryPermissionsPolicySignalErrorFull() instead")
    void getRepositoryPermissionsPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositoryPermissionsPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDomainsSignalErrorFull() instead")
    void listDomainsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listDomainsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackageVersionAssetsSignalErrorFull() instead")
    void listPackageVersionAssetsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackageVersionAssetsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackageVersionDependenciesSignalErrorFull() instead")
    void listPackageVersionDependenciesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackageVersionDependenciesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackageVersionsSignalErrorFull() instead")
    void listPackageVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackageVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPackagesSignalErrorFull() instead")
    void listPackagesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listPackagesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesSignalErrorFull() instead")
    void listRepositoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesInDomainSignalErrorFull() instead")
    void listRepositoriesInDomainSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesInDomainSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalErrorFull() instead")
    void listTagsForResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use publishPackageVersionSignalErrorFull() instead")
    void publishPackageVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void publishPackageVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDomainPermissionsPolicySignalErrorFull() instead")
    void putDomainPermissionsPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putDomainPermissionsPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putPackageOriginConfigurationSignalErrorFull() instead")
    void putPackageOriginConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putPackageOriginConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putRepositoryPermissionsPolicySignalErrorFull() instead")
    void putRepositoryPermissionsPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putRepositoryPermissionsPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalErrorFull() instead")
    void tagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalErrorFull() instead")
    void untagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePackageVersionsStatusSignalErrorFull() instead")
    void updatePackageVersionsStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePackageVersionsStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRepositorySignalErrorFull() instead")
    void updateRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
