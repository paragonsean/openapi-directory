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

#include "OAIDefaultApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIDefaultApi::OAIDefaultApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIDefaultApi::~OAIDefaultApi() {
}

void OAIDefaultApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://codeartifact.{region}.amazonaws.com"),
    "The CodeArtifact multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://codeartifact.{region}.amazonaws.com"),
    "The CodeArtifact multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://codeartifact.{region}.amazonaws.com.cn"),
    "The CodeArtifact endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://codeartifact.{region}.amazonaws.com.cn"),
    "The CodeArtifact endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    _serverConfigs.insert("associateExternalConnection", defaultConf);
    _serverIndices.insert("associateExternalConnection", 0);
    _serverConfigs.insert("copyPackageVersions", defaultConf);
    _serverIndices.insert("copyPackageVersions", 0);
    _serverConfigs.insert("createDomain", defaultConf);
    _serverIndices.insert("createDomain", 0);
    _serverConfigs.insert("createRepository", defaultConf);
    _serverIndices.insert("createRepository", 0);
    _serverConfigs.insert("deleteDomain", defaultConf);
    _serverIndices.insert("deleteDomain", 0);
    _serverConfigs.insert("deleteDomainPermissionsPolicy", defaultConf);
    _serverIndices.insert("deleteDomainPermissionsPolicy", 0);
    _serverConfigs.insert("deletePackage", defaultConf);
    _serverIndices.insert("deletePackage", 0);
    _serverConfigs.insert("deletePackageVersions", defaultConf);
    _serverIndices.insert("deletePackageVersions", 0);
    _serverConfigs.insert("deleteRepository", defaultConf);
    _serverIndices.insert("deleteRepository", 0);
    _serverConfigs.insert("deleteRepositoryPermissionsPolicy", defaultConf);
    _serverIndices.insert("deleteRepositoryPermissionsPolicy", 0);
    _serverConfigs.insert("describeDomain", defaultConf);
    _serverIndices.insert("describeDomain", 0);
    _serverConfigs.insert("describePackage", defaultConf);
    _serverIndices.insert("describePackage", 0);
    _serverConfigs.insert("describePackageVersion", defaultConf);
    _serverIndices.insert("describePackageVersion", 0);
    _serverConfigs.insert("describeRepository", defaultConf);
    _serverIndices.insert("describeRepository", 0);
    _serverConfigs.insert("disassociateExternalConnection", defaultConf);
    _serverIndices.insert("disassociateExternalConnection", 0);
    _serverConfigs.insert("disposePackageVersions", defaultConf);
    _serverIndices.insert("disposePackageVersions", 0);
    _serverConfigs.insert("getAuthorizationToken", defaultConf);
    _serverIndices.insert("getAuthorizationToken", 0);
    _serverConfigs.insert("getDomainPermissionsPolicy", defaultConf);
    _serverIndices.insert("getDomainPermissionsPolicy", 0);
    _serverConfigs.insert("getPackageVersionAsset", defaultConf);
    _serverIndices.insert("getPackageVersionAsset", 0);
    _serverConfigs.insert("getPackageVersionReadme", defaultConf);
    _serverIndices.insert("getPackageVersionReadme", 0);
    _serverConfigs.insert("getRepositoryEndpoint", defaultConf);
    _serverIndices.insert("getRepositoryEndpoint", 0);
    _serverConfigs.insert("getRepositoryPermissionsPolicy", defaultConf);
    _serverIndices.insert("getRepositoryPermissionsPolicy", 0);
    _serverConfigs.insert("listDomains", defaultConf);
    _serverIndices.insert("listDomains", 0);
    _serverConfigs.insert("listPackageVersionAssets", defaultConf);
    _serverIndices.insert("listPackageVersionAssets", 0);
    _serverConfigs.insert("listPackageVersionDependencies", defaultConf);
    _serverIndices.insert("listPackageVersionDependencies", 0);
    _serverConfigs.insert("listPackageVersions", defaultConf);
    _serverIndices.insert("listPackageVersions", 0);
    _serverConfigs.insert("listPackages", defaultConf);
    _serverIndices.insert("listPackages", 0);
    _serverConfigs.insert("listRepositories", defaultConf);
    _serverIndices.insert("listRepositories", 0);
    _serverConfigs.insert("listRepositoriesInDomain", defaultConf);
    _serverIndices.insert("listRepositoriesInDomain", 0);
    _serverConfigs.insert("listTagsForResource", defaultConf);
    _serverIndices.insert("listTagsForResource", 0);
    _serverConfigs.insert("publishPackageVersion", defaultConf);
    _serverIndices.insert("publishPackageVersion", 0);
    _serverConfigs.insert("putDomainPermissionsPolicy", defaultConf);
    _serverIndices.insert("putDomainPermissionsPolicy", 0);
    _serverConfigs.insert("putPackageOriginConfiguration", defaultConf);
    _serverIndices.insert("putPackageOriginConfiguration", 0);
    _serverConfigs.insert("putRepositoryPermissionsPolicy", defaultConf);
    _serverIndices.insert("putRepositoryPermissionsPolicy", 0);
    _serverConfigs.insert("tagResource", defaultConf);
    _serverIndices.insert("tagResource", 0);
    _serverConfigs.insert("untagResource", defaultConf);
    _serverIndices.insert("untagResource", 0);
    _serverConfigs.insert("updatePackageVersionsStatus", defaultConf);
    _serverIndices.insert("updatePackageVersionsStatus", 0);
    _serverConfigs.insert("updateRepository", defaultConf);
    _serverIndices.insert("updateRepository", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIDefaultApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIDefaultApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIDefaultApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIDefaultApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIDefaultApi::setUsername(const QString &username) {
    _username = username;
}

void OAIDefaultApi::setPassword(const QString &password) {
    _password = password;
}


void OAIDefaultApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIDefaultApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIDefaultApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAIDefaultApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIDefaultApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIDefaultApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIDefaultApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIDefaultApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIDefaultApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIDefaultApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIDefaultApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAIDefaultApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAIDefaultApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAIDefaultApi::associateExternalConnection(const QString &domain, const QString &repository, const QString &external_connection, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["associateExternalConnection"][_serverIndices.value("associateExternalConnection")].URL()+"/v1/repository/external-connection#domain&repository&external-connection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "external-connection", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("external-connection")).append(querySuffix).append(QUrl::toPercentEncoding(external_connection));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::associateExternalConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::associateExternalConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAssociateExternalConnectionResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT associateExternalConnectionSignal(output);
        Q_EMIT associateExternalConnectionSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT associateExternalConnectionSignalE(output, error_type, error_str);
        Q_EMIT associateExternalConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT associateExternalConnectionSignalError(output, error_type, error_str);
        Q_EMIT associateExternalConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::copyPackageVersions(const QString &domain, const QString &source_repository, const QString &destination_repository, const QString &format, const QString &package, const OAICopyPackageVersions_request &oai_copy_package_versions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["copyPackageVersions"][_serverIndices.value("copyPackageVersions")].URL()+"/v1/package/versions/copy#domain&source-repository&destination-repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "source-repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("source-repository")).append(querySuffix).append(QUrl::toPercentEncoding(source_repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "destination-repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("destination-repository")).append(querySuffix).append(QUrl::toPercentEncoding(destination_repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_copy_package_versions_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::copyPackageVersionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::copyPackageVersionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICopyPackageVersionsResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT copyPackageVersionsSignal(output);
        Q_EMIT copyPackageVersionsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT copyPackageVersionsSignalE(output, error_type, error_str);
        Q_EMIT copyPackageVersionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT copyPackageVersionsSignalError(output, error_type, error_str);
        Q_EMIT copyPackageVersionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createDomain(const QString &domain, const OAICreateDomain_request &oai_create_domain_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createDomain"][_serverIndices.value("createDomain")].URL()+"/v1/domain#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_domain_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createDomainCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createDomainCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateDomainResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createDomainSignal(output);
        Q_EMIT createDomainSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createDomainSignalE(output, error_type, error_str);
        Q_EMIT createDomainSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createDomainSignalError(output, error_type, error_str);
        Q_EMIT createDomainSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createRepository(const QString &domain, const QString &repository, const OAICreateRepository_request &oai_create_repository_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["createRepository"][_serverIndices.value("createRepository")].URL()+"/v1/repository#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_repository_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createRepositoryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createRepositoryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateRepositoryResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createRepositorySignal(output);
        Q_EMIT createRepositorySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createRepositorySignalE(output, error_type, error_str);
        Q_EMIT createRepositorySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createRepositorySignalError(output, error_type, error_str);
        Q_EMIT createRepositorySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteDomain(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["deleteDomain"][_serverIndices.value("deleteDomain")].URL()+"/v1/domain#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteDomainCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteDomainCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteDomainResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteDomainSignal(output);
        Q_EMIT deleteDomainSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteDomainSignalE(output, error_type, error_str);
        Q_EMIT deleteDomainSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteDomainSignalError(output, error_type, error_str);
        Q_EMIT deleteDomainSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteDomainPermissionsPolicy(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &policy_revision) {
    QString fullPath = QString(_serverConfigs["deleteDomainPermissionsPolicy"][_serverIndices.value("deleteDomainPermissionsPolicy")].URL()+"/v1/domain/permissions/policy#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    if (policy_revision.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "policy-revision", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("policy-revision")).append(querySuffix).append(QUrl::toPercentEncoding(policy_revision.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteDomainPermissionsPolicyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteDomainPermissionsPolicyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteDomainPermissionsPolicyResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteDomainPermissionsPolicySignal(output);
        Q_EMIT deleteDomainPermissionsPolicySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteDomainPermissionsPolicySignalE(output, error_type, error_str);
        Q_EMIT deleteDomainPermissionsPolicySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteDomainPermissionsPolicySignalError(output, error_type, error_str);
        Q_EMIT deleteDomainPermissionsPolicySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deletePackage(const QString &domain, const QString &repository, const QString &format, const QString &package, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["deletePackage"][_serverIndices.value("deletePackage")].URL()+"/v1/package#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deletePackageCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deletePackageCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeletePackageResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deletePackageSignal(output);
        Q_EMIT deletePackageSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deletePackageSignalE(output, error_type, error_str);
        Q_EMIT deletePackageSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deletePackageSignalError(output, error_type, error_str);
        Q_EMIT deletePackageSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deletePackageVersions(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIDeletePackageVersions_request &oai_delete_package_versions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["deletePackageVersions"][_serverIndices.value("deletePackageVersions")].URL()+"/v1/package/versions/delete#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_package_versions_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deletePackageVersionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deletePackageVersionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeletePackageVersionsResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deletePackageVersionsSignal(output);
        Q_EMIT deletePackageVersionsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deletePackageVersionsSignalE(output, error_type, error_str);
        Q_EMIT deletePackageVersionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deletePackageVersionsSignalError(output, error_type, error_str);
        Q_EMIT deletePackageVersionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteRepository(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["deleteRepository"][_serverIndices.value("deleteRepository")].URL()+"/v1/repository#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteRepositoryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteRepositoryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteRepositoryResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteRepositorySignal(output);
        Q_EMIT deleteRepositorySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteRepositorySignalE(output, error_type, error_str);
        Q_EMIT deleteRepositorySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteRepositorySignalError(output, error_type, error_str);
        Q_EMIT deleteRepositorySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteRepositoryPermissionsPolicy(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &policy_revision) {
    QString fullPath = QString(_serverConfigs["deleteRepositoryPermissionsPolicy"][_serverIndices.value("deleteRepositoryPermissionsPolicy")].URL()+"/v1/repository/permissions/policies#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    if (policy_revision.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "policy-revision", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("policy-revision")).append(querySuffix).append(QUrl::toPercentEncoding(policy_revision.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteRepositoryPermissionsPolicyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteRepositoryPermissionsPolicyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteRepositoryPermissionsPolicyResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteRepositoryPermissionsPolicySignal(output);
        Q_EMIT deleteRepositoryPermissionsPolicySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteRepositoryPermissionsPolicySignalE(output, error_type, error_str);
        Q_EMIT deleteRepositoryPermissionsPolicySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteRepositoryPermissionsPolicySignalError(output, error_type, error_str);
        Q_EMIT deleteRepositoryPermissionsPolicySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::describeDomain(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["describeDomain"][_serverIndices.value("describeDomain")].URL()+"/v1/domain#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::describeDomainCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::describeDomainCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDescribeDomainResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT describeDomainSignal(output);
        Q_EMIT describeDomainSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT describeDomainSignalE(output, error_type, error_str);
        Q_EMIT describeDomainSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT describeDomainSignalError(output, error_type, error_str);
        Q_EMIT describeDomainSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::describePackage(const QString &domain, const QString &repository, const QString &format, const QString &package, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["describePackage"][_serverIndices.value("describePackage")].URL()+"/v1/package#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::describePackageCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::describePackageCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDescribePackageResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT describePackageSignal(output);
        Q_EMIT describePackageSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT describePackageSignalE(output, error_type, error_str);
        Q_EMIT describePackageSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT describePackageSignalError(output, error_type, error_str);
        Q_EMIT describePackageSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::describePackageVersion(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["describePackageVersion"][_serverIndices.value("describePackageVersion")].URL()+"/v1/package/version#domain&repository&format&package&version");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "version", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("version")).append(querySuffix).append(QUrl::toPercentEncoding(version));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::describePackageVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::describePackageVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDescribePackageVersionResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT describePackageVersionSignal(output);
        Q_EMIT describePackageVersionSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT describePackageVersionSignalE(output, error_type, error_str);
        Q_EMIT describePackageVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT describePackageVersionSignalError(output, error_type, error_str);
        Q_EMIT describePackageVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::describeRepository(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["describeRepository"][_serverIndices.value("describeRepository")].URL()+"/v1/repository#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::describeRepositoryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::describeRepositoryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDescribeRepositoryResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT describeRepositorySignal(output);
        Q_EMIT describeRepositorySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT describeRepositorySignalE(output, error_type, error_str);
        Q_EMIT describeRepositorySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT describeRepositorySignalError(output, error_type, error_str);
        Q_EMIT describeRepositorySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::disassociateExternalConnection(const QString &domain, const QString &repository, const QString &external_connection, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["disassociateExternalConnection"][_serverIndices.value("disassociateExternalConnection")].URL()+"/v1/repository/external-connection#domain&repository&external-connection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "external-connection", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("external-connection")).append(querySuffix).append(QUrl::toPercentEncoding(external_connection));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::disassociateExternalConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::disassociateExternalConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDisassociateExternalConnectionResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT disassociateExternalConnectionSignal(output);
        Q_EMIT disassociateExternalConnectionSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT disassociateExternalConnectionSignalE(output, error_type, error_str);
        Q_EMIT disassociateExternalConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT disassociateExternalConnectionSignalError(output, error_type, error_str);
        Q_EMIT disassociateExternalConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::disposePackageVersions(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIDisposePackageVersions_request &oai_dispose_package_versions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["disposePackageVersions"][_serverIndices.value("disposePackageVersions")].URL()+"/v1/package/versions/dispose#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_dispose_package_versions_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::disposePackageVersionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::disposePackageVersionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDisposePackageVersionsResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT disposePackageVersionsSignal(output);
        Q_EMIT disposePackageVersionsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT disposePackageVersionsSignalE(output, error_type, error_str);
        Q_EMIT disposePackageVersionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT disposePackageVersionsSignalError(output, error_type, error_str);
        Q_EMIT disposePackageVersionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getAuthorizationToken(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<qint32> &duration) {
    QString fullPath = QString(_serverConfigs["getAuthorizationToken"][_serverIndices.value("getAuthorizationToken")].URL()+"/v1/authorization-token#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    if (duration.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "duration", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("duration")).append(querySuffix).append(QUrl::toPercentEncoding(duration.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getAuthorizationTokenCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getAuthorizationTokenCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetAuthorizationTokenResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getAuthorizationTokenSignal(output);
        Q_EMIT getAuthorizationTokenSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getAuthorizationTokenSignalE(output, error_type, error_str);
        Q_EMIT getAuthorizationTokenSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getAuthorizationTokenSignalError(output, error_type, error_str);
        Q_EMIT getAuthorizationTokenSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getDomainPermissionsPolicy(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["getDomainPermissionsPolicy"][_serverIndices.value("getDomainPermissionsPolicy")].URL()+"/v1/domain/permissions/policy#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getDomainPermissionsPolicyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getDomainPermissionsPolicyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetDomainPermissionsPolicyResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getDomainPermissionsPolicySignal(output);
        Q_EMIT getDomainPermissionsPolicySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getDomainPermissionsPolicySignalE(output, error_type, error_str);
        Q_EMIT getDomainPermissionsPolicySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getDomainPermissionsPolicySignalError(output, error_type, error_str);
        Q_EMIT getDomainPermissionsPolicySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getPackageVersionAsset(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const QString &asset, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace, const ::OpenAPI::OptionalParam<QString> &revision) {
    QString fullPath = QString(_serverConfigs["getPackageVersionAsset"][_serverIndices.value("getPackageVersionAsset")].URL()+"/v1/package/version/asset#domain&repository&format&package&version&asset");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "version", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("version")).append(querySuffix).append(QUrl::toPercentEncoding(version));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "asset", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("asset")).append(querySuffix).append(QUrl::toPercentEncoding(asset));
    }
    if (revision.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "revision", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("revision")).append(querySuffix).append(QUrl::toPercentEncoding(revision.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getPackageVersionAssetCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getPackageVersionAssetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetPackageVersionAssetResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getPackageVersionAssetSignal(output);
        Q_EMIT getPackageVersionAssetSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getPackageVersionAssetSignalE(output, error_type, error_str);
        Q_EMIT getPackageVersionAssetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getPackageVersionAssetSignalError(output, error_type, error_str);
        Q_EMIT getPackageVersionAssetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getPackageVersionReadme(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["getPackageVersionReadme"][_serverIndices.value("getPackageVersionReadme")].URL()+"/v1/package/version/readme#domain&repository&format&package&version");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "version", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("version")).append(querySuffix).append(QUrl::toPercentEncoding(version));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getPackageVersionReadmeCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getPackageVersionReadmeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetPackageVersionReadmeResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getPackageVersionReadmeSignal(output);
        Q_EMIT getPackageVersionReadmeSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getPackageVersionReadmeSignalE(output, error_type, error_str);
        Q_EMIT getPackageVersionReadmeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getPackageVersionReadmeSignalError(output, error_type, error_str);
        Q_EMIT getPackageVersionReadmeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getRepositoryEndpoint(const QString &domain, const QString &repository, const QString &format, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["getRepositoryEndpoint"][_serverIndices.value("getRepositoryEndpoint")].URL()+"/v1/repository/endpoint#domain&repository&format");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getRepositoryEndpointCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getRepositoryEndpointCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetRepositoryEndpointResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getRepositoryEndpointSignal(output);
        Q_EMIT getRepositoryEndpointSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getRepositoryEndpointSignalE(output, error_type, error_str);
        Q_EMIT getRepositoryEndpointSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getRepositoryEndpointSignalError(output, error_type, error_str);
        Q_EMIT getRepositoryEndpointSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getRepositoryPermissionsPolicy(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["getRepositoryPermissionsPolicy"][_serverIndices.value("getRepositoryPermissionsPolicy")].URL()+"/v1/repository/permissions/policy#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getRepositoryPermissionsPolicyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getRepositoryPermissionsPolicyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetRepositoryPermissionsPolicyResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getRepositoryPermissionsPolicySignal(output);
        Q_EMIT getRepositoryPermissionsPolicySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getRepositoryPermissionsPolicySignalE(output, error_type, error_str);
        Q_EMIT getRepositoryPermissionsPolicySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getRepositoryPermissionsPolicySignalError(output, error_type, error_str);
        Q_EMIT getRepositoryPermissionsPolicySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listDomains(const OAIListDomains_request &oai_list_domains_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listDomains"][_serverIndices.value("listDomains")].URL()+"/v1/domains");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_domains_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listDomainsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listDomainsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListDomainsResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listDomainsSignal(output);
        Q_EMIT listDomainsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listDomainsSignalE(output, error_type, error_str);
        Q_EMIT listDomainsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listDomainsSignalError(output, error_type, error_str);
        Q_EMIT listDomainsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPackageVersionAssets(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace, const ::OpenAPI::OptionalParam<qint32> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token, const ::OpenAPI::OptionalParam<QString> &max_results2, const ::OpenAPI::OptionalParam<QString> &next_token2) {
    QString fullPath = QString(_serverConfigs["listPackageVersionAssets"][_serverIndices.value("listPackageVersionAssets")].URL()+"/v1/package/version/assets#domain&repository&format&package&version");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "version", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("version")).append(querySuffix).append(QUrl::toPercentEncoding(version));
    }
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "max-results", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("max-results")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "next-token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("next-token")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    if (max_results2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results2.stringValue()));
    }
    if (next_token2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token2.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPackageVersionAssetsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPackageVersionAssetsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPackageVersionAssetsResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPackageVersionAssetsSignal(output);
        Q_EMIT listPackageVersionAssetsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listPackageVersionAssetsSignalE(output, error_type, error_str);
        Q_EMIT listPackageVersionAssetsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPackageVersionAssetsSignalError(output, error_type, error_str);
        Q_EMIT listPackageVersionAssetsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPackageVersionDependencies(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listPackageVersionDependencies"][_serverIndices.value("listPackageVersionDependencies")].URL()+"/v1/package/version/dependencies#domain&repository&format&package&version");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "version", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("version")).append(querySuffix).append(QUrl::toPercentEncoding(version));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "next-token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("next-token")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPackageVersionDependenciesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPackageVersionDependenciesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPackageVersionDependenciesResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPackageVersionDependenciesSignal(output);
        Q_EMIT listPackageVersionDependenciesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listPackageVersionDependenciesSignalE(output, error_type, error_str);
        Q_EMIT listPackageVersionDependenciesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPackageVersionDependenciesSignalError(output, error_type, error_str);
        Q_EMIT listPackageVersionDependenciesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPackageVersions(const QString &domain, const QString &repository, const QString &format, const QString &package, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace, const ::OpenAPI::OptionalParam<QString> &status, const ::OpenAPI::OptionalParam<QString> &sort_by, const ::OpenAPI::OptionalParam<qint32> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token, const ::OpenAPI::OptionalParam<QString> &origin_type, const ::OpenAPI::OptionalParam<QString> &max_results2, const ::OpenAPI::OptionalParam<QString> &next_token2) {
    QString fullPath = QString(_serverConfigs["listPackageVersions"][_serverIndices.value("listPackageVersions")].URL()+"/v1/package/versions#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    if (status.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "status", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("status")).append(querySuffix).append(QUrl::toPercentEncoding(status.stringValue()));
    }
    if (sort_by.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sortBy", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sortBy")).append(querySuffix).append(QUrl::toPercentEncoding(sort_by.stringValue()));
    }
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "max-results", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("max-results")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "next-token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("next-token")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    if (origin_type.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "originType", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("originType")).append(querySuffix).append(QUrl::toPercentEncoding(origin_type.stringValue()));
    }
    if (max_results2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results2.stringValue()));
    }
    if (next_token2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token2.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPackageVersionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPackageVersionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPackageVersionsResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPackageVersionsSignal(output);
        Q_EMIT listPackageVersionsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listPackageVersionsSignalE(output, error_type, error_str);
        Q_EMIT listPackageVersionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPackageVersionsSignalError(output, error_type, error_str);
        Q_EMIT listPackageVersionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPackages(const QString &domain, const QString &repository, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &format, const ::OpenAPI::OptionalParam<QString> &r_namespace, const ::OpenAPI::OptionalParam<QString> &package_prefix, const ::OpenAPI::OptionalParam<qint32> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token, const ::OpenAPI::OptionalParam<QString> &publish, const ::OpenAPI::OptionalParam<QString> &upstream, const ::OpenAPI::OptionalParam<QString> &max_results2, const ::OpenAPI::OptionalParam<QString> &next_token2) {
    QString fullPath = QString(_serverConfigs["listPackages"][_serverIndices.value("listPackages")].URL()+"/v1/packages#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    if (format.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format.stringValue()));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    if (package_prefix.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package-prefix", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package-prefix")).append(querySuffix).append(QUrl::toPercentEncoding(package_prefix.stringValue()));
    }
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "max-results", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("max-results")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "next-token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("next-token")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    if (publish.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "publish", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("publish")).append(querySuffix).append(QUrl::toPercentEncoding(publish.stringValue()));
    }
    if (upstream.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "upstream", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("upstream")).append(querySuffix).append(QUrl::toPercentEncoding(upstream.stringValue()));
    }
    if (max_results2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results2.stringValue()));
    }
    if (next_token2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token2.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPackagesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPackagesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPackagesResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPackagesSignal(output);
        Q_EMIT listPackagesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listPackagesSignalE(output, error_type, error_str);
        Q_EMIT listPackagesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPackagesSignalError(output, error_type, error_str);
        Q_EMIT listPackagesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listRepositories(const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &repository_prefix, const ::OpenAPI::OptionalParam<qint32> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token, const ::OpenAPI::OptionalParam<QString> &max_results2, const ::OpenAPI::OptionalParam<QString> &next_token2) {
    QString fullPath = QString(_serverConfigs["listRepositories"][_serverIndices.value("listRepositories")].URL()+"/v1/repositories");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (repository_prefix.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository-prefix", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository-prefix")).append(querySuffix).append(QUrl::toPercentEncoding(repository_prefix.stringValue()));
    }
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "max-results", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("max-results")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "next-token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("next-token")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    if (max_results2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results2.stringValue()));
    }
    if (next_token2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token2.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listRepositoriesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listRepositoriesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListRepositoriesResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listRepositoriesSignal(output);
        Q_EMIT listRepositoriesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listRepositoriesSignalE(output, error_type, error_str);
        Q_EMIT listRepositoriesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listRepositoriesSignalError(output, error_type, error_str);
        Q_EMIT listRepositoriesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listRepositoriesInDomain(const QString &domain, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &administrator_account, const ::OpenAPI::OptionalParam<QString> &repository_prefix, const ::OpenAPI::OptionalParam<qint32> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token, const ::OpenAPI::OptionalParam<QString> &max_results2, const ::OpenAPI::OptionalParam<QString> &next_token2) {
    QString fullPath = QString(_serverConfigs["listRepositoriesInDomain"][_serverIndices.value("listRepositoriesInDomain")].URL()+"/v1/domain/repositories#domain");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    if (administrator_account.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "administrator-account", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("administrator-account")).append(querySuffix).append(QUrl::toPercentEncoding(administrator_account.stringValue()));
    }
    if (repository_prefix.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository-prefix", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository-prefix")).append(querySuffix).append(QUrl::toPercentEncoding(repository_prefix.stringValue()));
    }
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "max-results", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("max-results")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "next-token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("next-token")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    if (max_results2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results2.stringValue()));
    }
    if (next_token2.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token2.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listRepositoriesInDomainCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listRepositoriesInDomainCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListRepositoriesInDomainResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listRepositoriesInDomainSignal(output);
        Q_EMIT listRepositoriesInDomainSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listRepositoriesInDomainSignalE(output, error_type, error_str);
        Q_EMIT listRepositoriesInDomainSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listRepositoriesInDomainSignalError(output, error_type, error_str);
        Q_EMIT listRepositoriesInDomainSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listTagsForResource(const QString &resource_arn, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["listTagsForResource"][_serverIndices.value("listTagsForResource")].URL()+"/v1/tags#resourceArn");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resourceArn", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resourceArn")).append(querySuffix).append(QUrl::toPercentEncoding(resource_arn));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listTagsForResourceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listTagsForResourceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListTagsForResourceResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listTagsForResourceSignal(output);
        Q_EMIT listTagsForResourceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listTagsForResourceSignalE(output, error_type, error_str);
        Q_EMIT listTagsForResourceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listTagsForResourceSignalError(output, error_type, error_str);
        Q_EMIT listTagsForResourceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::publishPackageVersion(const QString &domain, const QString &repository, const QString &format, const QString &package, const QString &version, const QString &asset, const QString &x_amz_content_sha257, const OAIPublishPackageVersion_request &oai_publish_package_version_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace, const ::OpenAPI::OptionalParam<bool> &unfinished) {
    QString fullPath = QString(_serverConfigs["publishPackageVersion"][_serverIndices.value("publishPackageVersion")].URL()+"/v1/package/version/publish#domain&repository&format&package&version&asset&x-amz-content-sha256");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "version", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("version")).append(querySuffix).append(QUrl::toPercentEncoding(version));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "asset", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("asset")).append(querySuffix).append(QUrl::toPercentEncoding(asset));
    }
    if (unfinished.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "unfinished", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("unfinished")).append(querySuffix).append(QUrl::toPercentEncoding(unfinished.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_publish_package_version_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha257).isEmpty()) {
            input.headers.insert("x-amz-content-sha256", ::OpenAPI::toStringValue(x_amz_content_sha257));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::publishPackageVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::publishPackageVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPublishPackageVersionResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT publishPackageVersionSignal(output);
        Q_EMIT publishPackageVersionSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT publishPackageVersionSignalE(output, error_type, error_str);
        Q_EMIT publishPackageVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT publishPackageVersionSignalError(output, error_type, error_str);
        Q_EMIT publishPackageVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putDomainPermissionsPolicy(const OAIPutDomainPermissionsPolicy_request &oai_put_domain_permissions_policy_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putDomainPermissionsPolicy"][_serverIndices.value("putDomainPermissionsPolicy")].URL()+"/v1/domain/permissions/policy");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_put_domain_permissions_policy_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putDomainPermissionsPolicyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putDomainPermissionsPolicyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPutDomainPermissionsPolicyResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putDomainPermissionsPolicySignal(output);
        Q_EMIT putDomainPermissionsPolicySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT putDomainPermissionsPolicySignalE(output, error_type, error_str);
        Q_EMIT putDomainPermissionsPolicySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putDomainPermissionsPolicySignalError(output, error_type, error_str);
        Q_EMIT putDomainPermissionsPolicySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putPackageOriginConfiguration(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIPutPackageOriginConfiguration_request &oai_put_package_origin_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["putPackageOriginConfiguration"][_serverIndices.value("putPackageOriginConfiguration")].URL()+"/v1/package#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_package_origin_configuration_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putPackageOriginConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putPackageOriginConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPutPackageOriginConfigurationResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putPackageOriginConfigurationSignal(output);
        Q_EMIT putPackageOriginConfigurationSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT putPackageOriginConfigurationSignalE(output, error_type, error_str);
        Q_EMIT putPackageOriginConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putPackageOriginConfigurationSignalError(output, error_type, error_str);
        Q_EMIT putPackageOriginConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putRepositoryPermissionsPolicy(const QString &domain, const QString &repository, const OAIPutRepositoryPermissionsPolicy_request &oai_put_repository_permissions_policy_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["putRepositoryPermissionsPolicy"][_serverIndices.value("putRepositoryPermissionsPolicy")].URL()+"/v1/repository/permissions/policy#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_put_repository_permissions_policy_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putRepositoryPermissionsPolicyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putRepositoryPermissionsPolicyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPutRepositoryPermissionsPolicyResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putRepositoryPermissionsPolicySignal(output);
        Q_EMIT putRepositoryPermissionsPolicySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT putRepositoryPermissionsPolicySignalE(output, error_type, error_str);
        Q_EMIT putRepositoryPermissionsPolicySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putRepositoryPermissionsPolicySignalError(output, error_type, error_str);
        Q_EMIT putRepositoryPermissionsPolicySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tagResource(const QString &resource_arn, const OAITagResource_request &oai_tag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["tagResource"][_serverIndices.value("tagResource")].URL()+"/v1/tag#resourceArn");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resourceArn", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resourceArn")).append(querySuffix).append(QUrl::toPercentEncoding(resource_arn));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_tag_resource_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::tagResourceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::tagResourceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT tagResourceSignal(output);
        Q_EMIT tagResourceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT tagResourceSignalE(output, error_type, error_str);
        Q_EMIT tagResourceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT tagResourceSignalError(output, error_type, error_str);
        Q_EMIT tagResourceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::untagResource(const QString &resource_arn, const OAIUntagResource_request &oai_untag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["untagResource"][_serverIndices.value("untagResource")].URL()+"/v1/untag#resourceArn");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resourceArn", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resourceArn")).append(querySuffix).append(QUrl::toPercentEncoding(resource_arn));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_untag_resource_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::untagResourceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::untagResourceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT untagResourceSignal(output);
        Q_EMIT untagResourceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT untagResourceSignalE(output, error_type, error_str);
        Q_EMIT untagResourceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT untagResourceSignalError(output, error_type, error_str);
        Q_EMIT untagResourceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updatePackageVersionsStatus(const QString &domain, const QString &repository, const QString &format, const QString &package, const OAIUpdatePackageVersionsStatus_request &oai_update_package_versions_status_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner, const ::OpenAPI::OptionalParam<QString> &r_namespace) {
    QString fullPath = QString(_serverConfigs["updatePackageVersionsStatus"][_serverIndices.value("updatePackageVersionsStatus")].URL()+"/v1/package/versions/update_status#domain&repository&format&package");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "format", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("format")).append(querySuffix).append(QUrl::toPercentEncoding(format));
    }
    if (r_namespace.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "namespace", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("namespace")).append(querySuffix).append(QUrl::toPercentEncoding(r_namespace.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "package", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("package")).append(querySuffix).append(QUrl::toPercentEncoding(package));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_package_versions_status_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updatePackageVersionsStatusCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updatePackageVersionsStatusCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdatePackageVersionsStatusResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updatePackageVersionsStatusSignal(output);
        Q_EMIT updatePackageVersionsStatusSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT updatePackageVersionsStatusSignalE(output, error_type, error_str);
        Q_EMIT updatePackageVersionsStatusSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updatePackageVersionsStatusSignalError(output, error_type, error_str);
        Q_EMIT updatePackageVersionsStatusSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateRepository(const QString &domain, const QString &repository, const OAIUpdateRepository_request &oai_update_repository_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &domain_owner) {
    QString fullPath = QString(_serverConfigs["updateRepository"][_serverIndices.value("updateRepository")].URL()+"/v1/repository#domain&repository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain")).append(querySuffix).append(QUrl::toPercentEncoding(domain));
    }
    if (domain_owner.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "domain-owner", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("domain-owner")).append(querySuffix).append(QUrl::toPercentEncoding(domain_owner.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "repository", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("repository")).append(querySuffix).append(QUrl::toPercentEncoding(repository));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_update_repository_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateRepositoryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateRepositoryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateRepositoryResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateRepositorySignal(output);
        Q_EMIT updateRepositorySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT updateRepositorySignalE(output, error_type, error_str);
        Q_EMIT updateRepositorySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateRepositorySignalError(output, error_type, error_str);
        Q_EMIT updateRepositorySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
