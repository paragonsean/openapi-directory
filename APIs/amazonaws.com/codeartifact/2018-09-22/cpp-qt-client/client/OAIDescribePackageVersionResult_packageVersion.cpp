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

#include "OAIDescribePackageVersionResult_packageVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDescribePackageVersionResult_packageVersion::OAIDescribePackageVersionResult_packageVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDescribePackageVersionResult_packageVersion::OAIDescribePackageVersionResult_packageVersion() {
    this->initializeModel();
}

OAIDescribePackageVersionResult_packageVersion::~OAIDescribePackageVersionResult_packageVersion() {}

void OAIDescribePackageVersionResult_packageVersion::initializeModel() {

    m_format_isSet = false;
    m_format_isValid = false;

    m_r_namespace_isSet = false;
    m_r_namespace_isValid = false;

    m_package_name_isSet = false;
    m_package_name_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_home_page_isSet = false;
    m_home_page_isValid = false;

    m_source_code_repository_isSet = false;
    m_source_code_repository_isValid = false;

    m_published_time_isSet = false;
    m_published_time_isValid = false;

    m_licenses_isSet = false;
    m_licenses_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_origin_isSet = false;
    m_origin_isValid = false;
}

void OAIDescribePackageVersionResult_packageVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDescribePackageVersionResult_packageVersion::fromJsonObject(QJsonObject json) {

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_r_namespace_isValid = ::OpenAPI::fromJsonValue(m_r_namespace, json[QString("namespace")]);
    m_r_namespace_isSet = !json[QString("namespace")].isNull() && m_r_namespace_isValid;

    m_package_name_isValid = ::OpenAPI::fromJsonValue(m_package_name, json[QString("packageName")]);
    m_package_name_isSet = !json[QString("packageName")].isNull() && m_package_name_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_home_page_isValid = ::OpenAPI::fromJsonValue(m_home_page, json[QString("homePage")]);
    m_home_page_isSet = !json[QString("homePage")].isNull() && m_home_page_isValid;

    m_source_code_repository_isValid = ::OpenAPI::fromJsonValue(m_source_code_repository, json[QString("sourceCodeRepository")]);
    m_source_code_repository_isSet = !json[QString("sourceCodeRepository")].isNull() && m_source_code_repository_isValid;

    m_published_time_isValid = ::OpenAPI::fromJsonValue(m_published_time, json[QString("publishedTime")]);
    m_published_time_isSet = !json[QString("publishedTime")].isNull() && m_published_time_isValid;

    m_licenses_isValid = ::OpenAPI::fromJsonValue(m_licenses, json[QString("licenses")]);
    m_licenses_isSet = !json[QString("licenses")].isNull() && m_licenses_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_origin_isValid = ::OpenAPI::fromJsonValue(m_origin, json[QString("origin")]);
    m_origin_isSet = !json[QString("origin")].isNull() && m_origin_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDescribePackageVersionResult_packageVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_format.isSet()) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_r_namespace_isSet) {
        obj.insert(QString("namespace"), ::OpenAPI::toJsonValue(m_r_namespace));
    }
    if (m_package_name_isSet) {
        obj.insert(QString("packageName"), ::OpenAPI::toJsonValue(m_package_name));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_home_page_isSet) {
        obj.insert(QString("homePage"), ::OpenAPI::toJsonValue(m_home_page));
    }
    if (m_source_code_repository_isSet) {
        obj.insert(QString("sourceCodeRepository"), ::OpenAPI::toJsonValue(m_source_code_repository));
    }
    if (m_published_time_isSet) {
        obj.insert(QString("publishedTime"), ::OpenAPI::toJsonValue(m_published_time));
    }
    if (m_licenses.isSet()) {
        obj.insert(QString("licenses"), ::OpenAPI::toJsonValue(m_licenses));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_origin.isSet()) {
        obj.insert(QString("origin"), ::OpenAPI::toJsonValue(m_origin));
    }
    return obj;
}

OAIPackageFormat OAIDescribePackageVersionResult_packageVersion::getFormat() const {
    return m_format;
}
void OAIDescribePackageVersionResult_packageVersion::setFormat(const OAIPackageFormat &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_format_Set() const{
    return m_format_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_format_Valid() const{
    return m_format_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getRNamespace() const {
    return m_r_namespace;
}
void OAIDescribePackageVersionResult_packageVersion::setRNamespace(const QString &r_namespace) {
    m_r_namespace = r_namespace;
    m_r_namespace_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_r_namespace_Set() const{
    return m_r_namespace_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_r_namespace_Valid() const{
    return m_r_namespace_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getPackageName() const {
    return m_package_name;
}
void OAIDescribePackageVersionResult_packageVersion::setPackageName(const QString &package_name) {
    m_package_name = package_name;
    m_package_name_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_package_name_Set() const{
    return m_package_name_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_package_name_Valid() const{
    return m_package_name_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getDisplayName() const {
    return m_display_name;
}
void OAIDescribePackageVersionResult_packageVersion::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getVersion() const {
    return m_version;
}
void OAIDescribePackageVersionResult_packageVersion::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_version_Set() const{
    return m_version_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_version_Valid() const{
    return m_version_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getSummary() const {
    return m_summary;
}
void OAIDescribePackageVersionResult_packageVersion::setSummary(const QString &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_summary_Valid() const{
    return m_summary_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getHomePage() const {
    return m_home_page;
}
void OAIDescribePackageVersionResult_packageVersion::setHomePage(const QString &home_page) {
    m_home_page = home_page;
    m_home_page_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_home_page_Set() const{
    return m_home_page_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_home_page_Valid() const{
    return m_home_page_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getSourceCodeRepository() const {
    return m_source_code_repository;
}
void OAIDescribePackageVersionResult_packageVersion::setSourceCodeRepository(const QString &source_code_repository) {
    m_source_code_repository = source_code_repository;
    m_source_code_repository_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_source_code_repository_Set() const{
    return m_source_code_repository_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_source_code_repository_Valid() const{
    return m_source_code_repository_isValid;
}

QDateTime OAIDescribePackageVersionResult_packageVersion::getPublishedTime() const {
    return m_published_time;
}
void OAIDescribePackageVersionResult_packageVersion::setPublishedTime(const QDateTime &published_time) {
    m_published_time = published_time;
    m_published_time_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_published_time_Set() const{
    return m_published_time_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_published_time_Valid() const{
    return m_published_time_isValid;
}

QList OAIDescribePackageVersionResult_packageVersion::getLicenses() const {
    return m_licenses;
}
void OAIDescribePackageVersionResult_packageVersion::setLicenses(const QList &licenses) {
    m_licenses = licenses;
    m_licenses_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_licenses_Set() const{
    return m_licenses_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_licenses_Valid() const{
    return m_licenses_isValid;
}

QString OAIDescribePackageVersionResult_packageVersion::getRevision() const {
    return m_revision;
}
void OAIDescribePackageVersionResult_packageVersion::setRevision(const QString &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_revision_Valid() const{
    return m_revision_isValid;
}

OAIPackageVersionStatus OAIDescribePackageVersionResult_packageVersion::getStatus() const {
    return m_status;
}
void OAIDescribePackageVersionResult_packageVersion::setStatus(const OAIPackageVersionStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_status_Set() const{
    return m_status_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_status_Valid() const{
    return m_status_isValid;
}

OAIPackageVersionDescription_origin OAIDescribePackageVersionResult_packageVersion::getOrigin() const {
    return m_origin;
}
void OAIDescribePackageVersionResult_packageVersion::setOrigin(const OAIPackageVersionDescription_origin &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAIDescribePackageVersionResult_packageVersion::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAIDescribePackageVersionResult_packageVersion::is_origin_Valid() const{
    return m_origin_isValid;
}

bool OAIDescribePackageVersionResult_packageVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_format.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_namespace_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_code_repository_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_published_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_licenses.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDescribePackageVersionResult_packageVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
