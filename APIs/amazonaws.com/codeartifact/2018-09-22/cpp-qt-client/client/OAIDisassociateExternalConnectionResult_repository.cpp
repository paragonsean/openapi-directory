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

#include "OAIDisassociateExternalConnectionResult_repository.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDisassociateExternalConnectionResult_repository::OAIDisassociateExternalConnectionResult_repository(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDisassociateExternalConnectionResult_repository::OAIDisassociateExternalConnectionResult_repository() {
    this->initializeModel();
}

OAIDisassociateExternalConnectionResult_repository::~OAIDisassociateExternalConnectionResult_repository() {}

void OAIDisassociateExternalConnectionResult_repository::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_administrator_account_isSet = false;
    m_administrator_account_isValid = false;

    m_domain_name_isSet = false;
    m_domain_name_isValid = false;

    m_domain_owner_isSet = false;
    m_domain_owner_isValid = false;

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_upstreams_isSet = false;
    m_upstreams_isValid = false;

    m_external_connections_isSet = false;
    m_external_connections_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;
}

void OAIDisassociateExternalConnectionResult_repository::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDisassociateExternalConnectionResult_repository::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_administrator_account_isValid = ::OpenAPI::fromJsonValue(m_administrator_account, json[QString("administratorAccount")]);
    m_administrator_account_isSet = !json[QString("administratorAccount")].isNull() && m_administrator_account_isValid;

    m_domain_name_isValid = ::OpenAPI::fromJsonValue(m_domain_name, json[QString("domainName")]);
    m_domain_name_isSet = !json[QString("domainName")].isNull() && m_domain_name_isValid;

    m_domain_owner_isValid = ::OpenAPI::fromJsonValue(m_domain_owner, json[QString("domainOwner")]);
    m_domain_owner_isSet = !json[QString("domainOwner")].isNull() && m_domain_owner_isValid;

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_upstreams_isValid = ::OpenAPI::fromJsonValue(m_upstreams, json[QString("upstreams")]);
    m_upstreams_isSet = !json[QString("upstreams")].isNull() && m_upstreams_isValid;

    m_external_connections_isValid = ::OpenAPI::fromJsonValue(m_external_connections, json[QString("externalConnections")]);
    m_external_connections_isSet = !json[QString("externalConnections")].isNull() && m_external_connections_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;
}

QString OAIDisassociateExternalConnectionResult_repository::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDisassociateExternalConnectionResult_repository::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_administrator_account_isSet) {
        obj.insert(QString("administratorAccount"), ::OpenAPI::toJsonValue(m_administrator_account));
    }
    if (m_domain_name_isSet) {
        obj.insert(QString("domainName"), ::OpenAPI::toJsonValue(m_domain_name));
    }
    if (m_domain_owner_isSet) {
        obj.insert(QString("domainOwner"), ::OpenAPI::toJsonValue(m_domain_owner));
    }
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_upstreams.isSet()) {
        obj.insert(QString("upstreams"), ::OpenAPI::toJsonValue(m_upstreams));
    }
    if (m_external_connections.isSet()) {
        obj.insert(QString("externalConnections"), ::OpenAPI::toJsonValue(m_external_connections));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    return obj;
}

QString OAIDisassociateExternalConnectionResult_repository::getName() const {
    return m_name;
}
void OAIDisassociateExternalConnectionResult_repository::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIDisassociateExternalConnectionResult_repository::getAdministratorAccount() const {
    return m_administrator_account;
}
void OAIDisassociateExternalConnectionResult_repository::setAdministratorAccount(const QString &administrator_account) {
    m_administrator_account = administrator_account;
    m_administrator_account_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_administrator_account_Set() const{
    return m_administrator_account_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_administrator_account_Valid() const{
    return m_administrator_account_isValid;
}

QString OAIDisassociateExternalConnectionResult_repository::getDomainName() const {
    return m_domain_name;
}
void OAIDisassociateExternalConnectionResult_repository::setDomainName(const QString &domain_name) {
    m_domain_name = domain_name;
    m_domain_name_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_domain_name_Set() const{
    return m_domain_name_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_domain_name_Valid() const{
    return m_domain_name_isValid;
}

QString OAIDisassociateExternalConnectionResult_repository::getDomainOwner() const {
    return m_domain_owner;
}
void OAIDisassociateExternalConnectionResult_repository::setDomainOwner(const QString &domain_owner) {
    m_domain_owner = domain_owner;
    m_domain_owner_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_domain_owner_Set() const{
    return m_domain_owner_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_domain_owner_Valid() const{
    return m_domain_owner_isValid;
}

QString OAIDisassociateExternalConnectionResult_repository::getArn() const {
    return m_arn;
}
void OAIDisassociateExternalConnectionResult_repository::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_arn_Valid() const{
    return m_arn_isValid;
}

QString OAIDisassociateExternalConnectionResult_repository::getDescription() const {
    return m_description;
}
void OAIDisassociateExternalConnectionResult_repository::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_description_Set() const{
    return m_description_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_description_Valid() const{
    return m_description_isValid;
}

QList OAIDisassociateExternalConnectionResult_repository::getUpstreams() const {
    return m_upstreams;
}
void OAIDisassociateExternalConnectionResult_repository::setUpstreams(const QList &upstreams) {
    m_upstreams = upstreams;
    m_upstreams_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_upstreams_Set() const{
    return m_upstreams_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_upstreams_Valid() const{
    return m_upstreams_isValid;
}

QList OAIDisassociateExternalConnectionResult_repository::getExternalConnections() const {
    return m_external_connections;
}
void OAIDisassociateExternalConnectionResult_repository::setExternalConnections(const QList &external_connections) {
    m_external_connections = external_connections;
    m_external_connections_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_external_connections_Set() const{
    return m_external_connections_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_external_connections_Valid() const{
    return m_external_connections_isValid;
}

QDateTime OAIDisassociateExternalConnectionResult_repository::getCreatedTime() const {
    return m_created_time;
}
void OAIDisassociateExternalConnectionResult_repository::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIDisassociateExternalConnectionResult_repository::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIDisassociateExternalConnectionResult_repository::is_created_time_Valid() const{
    return m_created_time_isValid;
}

bool OAIDisassociateExternalConnectionResult_repository::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_administrator_account_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_domain_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_domain_owner_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upstreams.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_connections.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDisassociateExternalConnectionResult_repository::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
