/**
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
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
    QUrl("http://proton.{region}.amazonaws.com"),
    "The AWS Proton multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://proton.{region}.amazonaws.com"),
    "The AWS Proton multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://proton.{region}.amazonaws.com.cn"),
    "The AWS Proton endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://proton.{region}.amazonaws.com.cn"),
    "The AWS Proton endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    _serverConfigs.insert("acceptEnvironmentAccountConnection", defaultConf);
    _serverIndices.insert("acceptEnvironmentAccountConnection", 0);
    _serverConfigs.insert("cancelComponentDeployment", defaultConf);
    _serverIndices.insert("cancelComponentDeployment", 0);
    _serverConfigs.insert("cancelEnvironmentDeployment", defaultConf);
    _serverIndices.insert("cancelEnvironmentDeployment", 0);
    _serverConfigs.insert("cancelServiceInstanceDeployment", defaultConf);
    _serverIndices.insert("cancelServiceInstanceDeployment", 0);
    _serverConfigs.insert("cancelServicePipelineDeployment", defaultConf);
    _serverIndices.insert("cancelServicePipelineDeployment", 0);
    _serverConfigs.insert("createComponent", defaultConf);
    _serverIndices.insert("createComponent", 0);
    _serverConfigs.insert("createEnvironment", defaultConf);
    _serverIndices.insert("createEnvironment", 0);
    _serverConfigs.insert("createEnvironmentAccountConnection", defaultConf);
    _serverIndices.insert("createEnvironmentAccountConnection", 0);
    _serverConfigs.insert("createEnvironmentTemplate", defaultConf);
    _serverIndices.insert("createEnvironmentTemplate", 0);
    _serverConfigs.insert("createEnvironmentTemplateVersion", defaultConf);
    _serverIndices.insert("createEnvironmentTemplateVersion", 0);
    _serverConfigs.insert("createRepository", defaultConf);
    _serverIndices.insert("createRepository", 0);
    _serverConfigs.insert("createService", defaultConf);
    _serverIndices.insert("createService", 0);
    _serverConfigs.insert("createServiceInstance", defaultConf);
    _serverIndices.insert("createServiceInstance", 0);
    _serverConfigs.insert("createServiceSyncConfig", defaultConf);
    _serverIndices.insert("createServiceSyncConfig", 0);
    _serverConfigs.insert("createServiceTemplate", defaultConf);
    _serverIndices.insert("createServiceTemplate", 0);
    _serverConfigs.insert("createServiceTemplateVersion", defaultConf);
    _serverIndices.insert("createServiceTemplateVersion", 0);
    _serverConfigs.insert("createTemplateSyncConfig", defaultConf);
    _serverIndices.insert("createTemplateSyncConfig", 0);
    _serverConfigs.insert("deleteComponent", defaultConf);
    _serverIndices.insert("deleteComponent", 0);
    _serverConfigs.insert("deleteDeployment", defaultConf);
    _serverIndices.insert("deleteDeployment", 0);
    _serverConfigs.insert("deleteEnvironment", defaultConf);
    _serverIndices.insert("deleteEnvironment", 0);
    _serverConfigs.insert("deleteEnvironmentAccountConnection", defaultConf);
    _serverIndices.insert("deleteEnvironmentAccountConnection", 0);
    _serverConfigs.insert("deleteEnvironmentTemplate", defaultConf);
    _serverIndices.insert("deleteEnvironmentTemplate", 0);
    _serverConfigs.insert("deleteEnvironmentTemplateVersion", defaultConf);
    _serverIndices.insert("deleteEnvironmentTemplateVersion", 0);
    _serverConfigs.insert("deleteRepository", defaultConf);
    _serverIndices.insert("deleteRepository", 0);
    _serverConfigs.insert("deleteService", defaultConf);
    _serverIndices.insert("deleteService", 0);
    _serverConfigs.insert("deleteServiceSyncConfig", defaultConf);
    _serverIndices.insert("deleteServiceSyncConfig", 0);
    _serverConfigs.insert("deleteServiceTemplate", defaultConf);
    _serverIndices.insert("deleteServiceTemplate", 0);
    _serverConfigs.insert("deleteServiceTemplateVersion", defaultConf);
    _serverIndices.insert("deleteServiceTemplateVersion", 0);
    _serverConfigs.insert("deleteTemplateSyncConfig", defaultConf);
    _serverIndices.insert("deleteTemplateSyncConfig", 0);
    _serverConfigs.insert("getAccountSettings", defaultConf);
    _serverIndices.insert("getAccountSettings", 0);
    _serverConfigs.insert("getComponent", defaultConf);
    _serverIndices.insert("getComponent", 0);
    _serverConfigs.insert("getDeployment", defaultConf);
    _serverIndices.insert("getDeployment", 0);
    _serverConfigs.insert("getEnvironment", defaultConf);
    _serverIndices.insert("getEnvironment", 0);
    _serverConfigs.insert("getEnvironmentAccountConnection", defaultConf);
    _serverIndices.insert("getEnvironmentAccountConnection", 0);
    _serverConfigs.insert("getEnvironmentTemplate", defaultConf);
    _serverIndices.insert("getEnvironmentTemplate", 0);
    _serverConfigs.insert("getEnvironmentTemplateVersion", defaultConf);
    _serverIndices.insert("getEnvironmentTemplateVersion", 0);
    _serverConfigs.insert("getRepository", defaultConf);
    _serverIndices.insert("getRepository", 0);
    _serverConfigs.insert("getRepositorySyncStatus", defaultConf);
    _serverIndices.insert("getRepositorySyncStatus", 0);
    _serverConfigs.insert("getResourcesSummary", defaultConf);
    _serverIndices.insert("getResourcesSummary", 0);
    _serverConfigs.insert("getService", defaultConf);
    _serverIndices.insert("getService", 0);
    _serverConfigs.insert("getServiceInstance", defaultConf);
    _serverIndices.insert("getServiceInstance", 0);
    _serverConfigs.insert("getServiceInstanceSyncStatus", defaultConf);
    _serverIndices.insert("getServiceInstanceSyncStatus", 0);
    _serverConfigs.insert("getServiceSyncBlockerSummary", defaultConf);
    _serverIndices.insert("getServiceSyncBlockerSummary", 0);
    _serverConfigs.insert("getServiceSyncConfig", defaultConf);
    _serverIndices.insert("getServiceSyncConfig", 0);
    _serverConfigs.insert("getServiceTemplate", defaultConf);
    _serverIndices.insert("getServiceTemplate", 0);
    _serverConfigs.insert("getServiceTemplateVersion", defaultConf);
    _serverIndices.insert("getServiceTemplateVersion", 0);
    _serverConfigs.insert("getTemplateSyncConfig", defaultConf);
    _serverIndices.insert("getTemplateSyncConfig", 0);
    _serverConfigs.insert("getTemplateSyncStatus", defaultConf);
    _serverIndices.insert("getTemplateSyncStatus", 0);
    _serverConfigs.insert("listComponentOutputs", defaultConf);
    _serverIndices.insert("listComponentOutputs", 0);
    _serverConfigs.insert("listComponentProvisionedResources", defaultConf);
    _serverIndices.insert("listComponentProvisionedResources", 0);
    _serverConfigs.insert("listComponents", defaultConf);
    _serverIndices.insert("listComponents", 0);
    _serverConfigs.insert("listDeployments", defaultConf);
    _serverIndices.insert("listDeployments", 0);
    _serverConfigs.insert("listEnvironmentAccountConnections", defaultConf);
    _serverIndices.insert("listEnvironmentAccountConnections", 0);
    _serverConfigs.insert("listEnvironmentOutputs", defaultConf);
    _serverIndices.insert("listEnvironmentOutputs", 0);
    _serverConfigs.insert("listEnvironmentProvisionedResources", defaultConf);
    _serverIndices.insert("listEnvironmentProvisionedResources", 0);
    _serverConfigs.insert("listEnvironmentTemplateVersions", defaultConf);
    _serverIndices.insert("listEnvironmentTemplateVersions", 0);
    _serverConfigs.insert("listEnvironmentTemplates", defaultConf);
    _serverIndices.insert("listEnvironmentTemplates", 0);
    _serverConfigs.insert("listEnvironments", defaultConf);
    _serverIndices.insert("listEnvironments", 0);
    _serverConfigs.insert("listRepositories", defaultConf);
    _serverIndices.insert("listRepositories", 0);
    _serverConfigs.insert("listRepositorySyncDefinitions", defaultConf);
    _serverIndices.insert("listRepositorySyncDefinitions", 0);
    _serverConfigs.insert("listServiceInstanceOutputs", defaultConf);
    _serverIndices.insert("listServiceInstanceOutputs", 0);
    _serverConfigs.insert("listServiceInstanceProvisionedResources", defaultConf);
    _serverIndices.insert("listServiceInstanceProvisionedResources", 0);
    _serverConfigs.insert("listServiceInstances", defaultConf);
    _serverIndices.insert("listServiceInstances", 0);
    _serverConfigs.insert("listServicePipelineOutputs", defaultConf);
    _serverIndices.insert("listServicePipelineOutputs", 0);
    _serverConfigs.insert("listServicePipelineProvisionedResources", defaultConf);
    _serverIndices.insert("listServicePipelineProvisionedResources", 0);
    _serverConfigs.insert("listServiceTemplateVersions", defaultConf);
    _serverIndices.insert("listServiceTemplateVersions", 0);
    _serverConfigs.insert("listServiceTemplates", defaultConf);
    _serverIndices.insert("listServiceTemplates", 0);
    _serverConfigs.insert("listServices", defaultConf);
    _serverIndices.insert("listServices", 0);
    _serverConfigs.insert("listTagsForResource", defaultConf);
    _serverIndices.insert("listTagsForResource", 0);
    _serverConfigs.insert("notifyResourceDeploymentStatusChange", defaultConf);
    _serverIndices.insert("notifyResourceDeploymentStatusChange", 0);
    _serverConfigs.insert("rejectEnvironmentAccountConnection", defaultConf);
    _serverIndices.insert("rejectEnvironmentAccountConnection", 0);
    _serverConfigs.insert("tagResource", defaultConf);
    _serverIndices.insert("tagResource", 0);
    _serverConfigs.insert("untagResource", defaultConf);
    _serverIndices.insert("untagResource", 0);
    _serverConfigs.insert("updateAccountSettings", defaultConf);
    _serverIndices.insert("updateAccountSettings", 0);
    _serverConfigs.insert("updateComponent", defaultConf);
    _serverIndices.insert("updateComponent", 0);
    _serverConfigs.insert("updateEnvironment", defaultConf);
    _serverIndices.insert("updateEnvironment", 0);
    _serverConfigs.insert("updateEnvironmentAccountConnection", defaultConf);
    _serverIndices.insert("updateEnvironmentAccountConnection", 0);
    _serverConfigs.insert("updateEnvironmentTemplate", defaultConf);
    _serverIndices.insert("updateEnvironmentTemplate", 0);
    _serverConfigs.insert("updateEnvironmentTemplateVersion", defaultConf);
    _serverIndices.insert("updateEnvironmentTemplateVersion", 0);
    _serverConfigs.insert("updateService", defaultConf);
    _serverIndices.insert("updateService", 0);
    _serverConfigs.insert("updateServiceInstance", defaultConf);
    _serverIndices.insert("updateServiceInstance", 0);
    _serverConfigs.insert("updateServicePipeline", defaultConf);
    _serverIndices.insert("updateServicePipeline", 0);
    _serverConfigs.insert("updateServiceSyncBlocker", defaultConf);
    _serverIndices.insert("updateServiceSyncBlocker", 0);
    _serverConfigs.insert("updateServiceSyncConfig", defaultConf);
    _serverIndices.insert("updateServiceSyncConfig", 0);
    _serverConfigs.insert("updateServiceTemplate", defaultConf);
    _serverIndices.insert("updateServiceTemplate", 0);
    _serverConfigs.insert("updateServiceTemplateVersion", defaultConf);
    _serverIndices.insert("updateServiceTemplateVersion", 0);
    _serverConfigs.insert("updateTemplateSyncConfig", defaultConf);
    _serverIndices.insert("updateTemplateSyncConfig", 0);
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

void OAIDefaultApi::acceptEnvironmentAccountConnection(const QString &x_amz_target, const OAIAcceptEnvironmentAccountConnectionInput &oai_accept_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["acceptEnvironmentAccountConnection"][_serverIndices.value("acceptEnvironmentAccountConnection")].URL()+"/#X-Amz-Target=AwsProton20200720.AcceptEnvironmentAccountConnection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_accept_environment_account_connection_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::acceptEnvironmentAccountConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::acceptEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAcceptEnvironmentAccountConnectionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acceptEnvironmentAccountConnectionSignal(output);
        Q_EMIT acceptEnvironmentAccountConnectionSignalFull(worker, output);
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

        Q_EMIT acceptEnvironmentAccountConnectionSignalE(output, error_type, error_str);
        Q_EMIT acceptEnvironmentAccountConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acceptEnvironmentAccountConnectionSignalError(output, error_type, error_str);
        Q_EMIT acceptEnvironmentAccountConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::cancelComponentDeployment(const QString &x_amz_target, const OAICancelComponentDeploymentInput &oai_cancel_component_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["cancelComponentDeployment"][_serverIndices.value("cancelComponentDeployment")].URL()+"/#X-Amz-Target=AwsProton20200720.CancelComponentDeployment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_cancel_component_deployment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::cancelComponentDeploymentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::cancelComponentDeploymentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICancelComponentDeploymentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT cancelComponentDeploymentSignal(output);
        Q_EMIT cancelComponentDeploymentSignalFull(worker, output);
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

        Q_EMIT cancelComponentDeploymentSignalE(output, error_type, error_str);
        Q_EMIT cancelComponentDeploymentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT cancelComponentDeploymentSignalError(output, error_type, error_str);
        Q_EMIT cancelComponentDeploymentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::cancelEnvironmentDeployment(const QString &x_amz_target, const OAICancelEnvironmentDeploymentInput &oai_cancel_environment_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["cancelEnvironmentDeployment"][_serverIndices.value("cancelEnvironmentDeployment")].URL()+"/#X-Amz-Target=AwsProton20200720.CancelEnvironmentDeployment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_cancel_environment_deployment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::cancelEnvironmentDeploymentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::cancelEnvironmentDeploymentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICancelEnvironmentDeploymentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT cancelEnvironmentDeploymentSignal(output);
        Q_EMIT cancelEnvironmentDeploymentSignalFull(worker, output);
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

        Q_EMIT cancelEnvironmentDeploymentSignalE(output, error_type, error_str);
        Q_EMIT cancelEnvironmentDeploymentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT cancelEnvironmentDeploymentSignalError(output, error_type, error_str);
        Q_EMIT cancelEnvironmentDeploymentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::cancelServiceInstanceDeployment(const QString &x_amz_target, const OAICancelServiceInstanceDeploymentInput &oai_cancel_service_instance_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["cancelServiceInstanceDeployment"][_serverIndices.value("cancelServiceInstanceDeployment")].URL()+"/#X-Amz-Target=AwsProton20200720.CancelServiceInstanceDeployment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_cancel_service_instance_deployment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::cancelServiceInstanceDeploymentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::cancelServiceInstanceDeploymentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICancelServiceInstanceDeploymentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT cancelServiceInstanceDeploymentSignal(output);
        Q_EMIT cancelServiceInstanceDeploymentSignalFull(worker, output);
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

        Q_EMIT cancelServiceInstanceDeploymentSignalE(output, error_type, error_str);
        Q_EMIT cancelServiceInstanceDeploymentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT cancelServiceInstanceDeploymentSignalError(output, error_type, error_str);
        Q_EMIT cancelServiceInstanceDeploymentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::cancelServicePipelineDeployment(const QString &x_amz_target, const OAICancelServicePipelineDeploymentInput &oai_cancel_service_pipeline_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["cancelServicePipelineDeployment"][_serverIndices.value("cancelServicePipelineDeployment")].URL()+"/#X-Amz-Target=AwsProton20200720.CancelServicePipelineDeployment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_cancel_service_pipeline_deployment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::cancelServicePipelineDeploymentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::cancelServicePipelineDeploymentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICancelServicePipelineDeploymentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT cancelServicePipelineDeploymentSignal(output);
        Q_EMIT cancelServicePipelineDeploymentSignalFull(worker, output);
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

        Q_EMIT cancelServicePipelineDeploymentSignalE(output, error_type, error_str);
        Q_EMIT cancelServicePipelineDeploymentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT cancelServicePipelineDeploymentSignalError(output, error_type, error_str);
        Q_EMIT cancelServicePipelineDeploymentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createComponent(const QString &x_amz_target, const OAICreateComponentInput &oai_create_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createComponent"][_serverIndices.value("createComponent")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateComponent");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_component_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createComponentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createComponentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateComponentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createComponentSignal(output);
        Q_EMIT createComponentSignalFull(worker, output);
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

        Q_EMIT createComponentSignalE(output, error_type, error_str);
        Q_EMIT createComponentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createComponentSignalError(output, error_type, error_str);
        Q_EMIT createComponentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createEnvironment(const QString &x_amz_target, const OAICreateEnvironmentInput &oai_create_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createEnvironment"][_serverIndices.value("createEnvironment")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateEnvironment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_environment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createEnvironmentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createEnvironmentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateEnvironmentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createEnvironmentSignal(output);
        Q_EMIT createEnvironmentSignalFull(worker, output);
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

        Q_EMIT createEnvironmentSignalE(output, error_type, error_str);
        Q_EMIT createEnvironmentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createEnvironmentSignalError(output, error_type, error_str);
        Q_EMIT createEnvironmentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createEnvironmentAccountConnection(const QString &x_amz_target, const OAICreateEnvironmentAccountConnectionInput &oai_create_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createEnvironmentAccountConnection"][_serverIndices.value("createEnvironmentAccountConnection")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateEnvironmentAccountConnection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_environment_account_connection_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createEnvironmentAccountConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateEnvironmentAccountConnectionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createEnvironmentAccountConnectionSignal(output);
        Q_EMIT createEnvironmentAccountConnectionSignalFull(worker, output);
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

        Q_EMIT createEnvironmentAccountConnectionSignalE(output, error_type, error_str);
        Q_EMIT createEnvironmentAccountConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createEnvironmentAccountConnectionSignalError(output, error_type, error_str);
        Q_EMIT createEnvironmentAccountConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createEnvironmentTemplate(const QString &x_amz_target, const OAICreateEnvironmentTemplateInput &oai_create_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createEnvironmentTemplate"][_serverIndices.value("createEnvironmentTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateEnvironmentTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_environment_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createEnvironmentTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createEnvironmentTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateEnvironmentTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createEnvironmentTemplateSignal(output);
        Q_EMIT createEnvironmentTemplateSignalFull(worker, output);
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

        Q_EMIT createEnvironmentTemplateSignalE(output, error_type, error_str);
        Q_EMIT createEnvironmentTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createEnvironmentTemplateSignalError(output, error_type, error_str);
        Q_EMIT createEnvironmentTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createEnvironmentTemplateVersion(const QString &x_amz_target, const OAICreateEnvironmentTemplateVersionInput &oai_create_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createEnvironmentTemplateVersion"][_serverIndices.value("createEnvironmentTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateEnvironmentTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_environment_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createEnvironmentTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateEnvironmentTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createEnvironmentTemplateVersionSignal(output);
        Q_EMIT createEnvironmentTemplateVersionSignalFull(worker, output);
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

        Q_EMIT createEnvironmentTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT createEnvironmentTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createEnvironmentTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT createEnvironmentTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createRepository(const QString &x_amz_target, const OAICreateRepositoryInput &oai_create_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createRepository"][_serverIndices.value("createRepository")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateRepository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_repository_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
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
    OAICreateRepositoryOutput output(QString(worker->response));
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

void OAIDefaultApi::createService(const QString &x_amz_target, const OAICreateServiceInput &oai_create_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createService"][_serverIndices.value("createService")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateService");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_service_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createServiceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createServiceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateServiceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createServiceSignal(output);
        Q_EMIT createServiceSignalFull(worker, output);
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

        Q_EMIT createServiceSignalE(output, error_type, error_str);
        Q_EMIT createServiceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createServiceSignalError(output, error_type, error_str);
        Q_EMIT createServiceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createServiceInstance(const QString &x_amz_target, const OAICreateServiceInstanceInput &oai_create_service_instance_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createServiceInstance"][_serverIndices.value("createServiceInstance")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateServiceInstance");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_service_instance_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createServiceInstanceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createServiceInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateServiceInstanceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createServiceInstanceSignal(output);
        Q_EMIT createServiceInstanceSignalFull(worker, output);
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

        Q_EMIT createServiceInstanceSignalE(output, error_type, error_str);
        Q_EMIT createServiceInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createServiceInstanceSignalError(output, error_type, error_str);
        Q_EMIT createServiceInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createServiceSyncConfig(const QString &x_amz_target, const OAICreateServiceSyncConfigInput &oai_create_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createServiceSyncConfig"][_serverIndices.value("createServiceSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateServiceSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_service_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createServiceSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createServiceSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateServiceSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createServiceSyncConfigSignal(output);
        Q_EMIT createServiceSyncConfigSignalFull(worker, output);
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

        Q_EMIT createServiceSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT createServiceSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createServiceSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT createServiceSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createServiceTemplate(const QString &x_amz_target, const OAICreateServiceTemplateInput &oai_create_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createServiceTemplate"][_serverIndices.value("createServiceTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateServiceTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_service_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createServiceTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createServiceTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateServiceTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createServiceTemplateSignal(output);
        Q_EMIT createServiceTemplateSignalFull(worker, output);
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

        Q_EMIT createServiceTemplateSignalE(output, error_type, error_str);
        Q_EMIT createServiceTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createServiceTemplateSignalError(output, error_type, error_str);
        Q_EMIT createServiceTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createServiceTemplateVersion(const QString &x_amz_target, const OAICreateServiceTemplateVersionInput &oai_create_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createServiceTemplateVersion"][_serverIndices.value("createServiceTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateServiceTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_service_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createServiceTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createServiceTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateServiceTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createServiceTemplateVersionSignal(output);
        Q_EMIT createServiceTemplateVersionSignalFull(worker, output);
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

        Q_EMIT createServiceTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT createServiceTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createServiceTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT createServiceTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createTemplateSyncConfig(const QString &x_amz_target, const OAICreateTemplateSyncConfigInput &oai_create_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createTemplateSyncConfig"][_serverIndices.value("createTemplateSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.CreateTemplateSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_template_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createTemplateSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createTemplateSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateTemplateSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createTemplateSyncConfigSignal(output);
        Q_EMIT createTemplateSyncConfigSignalFull(worker, output);
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

        Q_EMIT createTemplateSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT createTemplateSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createTemplateSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT createTemplateSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteComponent(const QString &x_amz_target, const OAIDeleteComponentInput &oai_delete_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteComponent"][_serverIndices.value("deleteComponent")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteComponent");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_component_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteComponentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteComponentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteComponentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteComponentSignal(output);
        Q_EMIT deleteComponentSignalFull(worker, output);
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

        Q_EMIT deleteComponentSignalE(output, error_type, error_str);
        Q_EMIT deleteComponentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteComponentSignalError(output, error_type, error_str);
        Q_EMIT deleteComponentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteDeployment(const QString &x_amz_target, const OAIDeleteDeploymentInput &oai_delete_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteDeployment"][_serverIndices.value("deleteDeployment")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteDeployment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_deployment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteDeploymentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteDeploymentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteDeploymentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteDeploymentSignal(output);
        Q_EMIT deleteDeploymentSignalFull(worker, output);
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

        Q_EMIT deleteDeploymentSignalE(output, error_type, error_str);
        Q_EMIT deleteDeploymentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteDeploymentSignalError(output, error_type, error_str);
        Q_EMIT deleteDeploymentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteEnvironment(const QString &x_amz_target, const OAIDeleteEnvironmentInput &oai_delete_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteEnvironment"][_serverIndices.value("deleteEnvironment")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteEnvironment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_environment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteEnvironmentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteEnvironmentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteEnvironmentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteEnvironmentSignal(output);
        Q_EMIT deleteEnvironmentSignalFull(worker, output);
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

        Q_EMIT deleteEnvironmentSignalE(output, error_type, error_str);
        Q_EMIT deleteEnvironmentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteEnvironmentSignalError(output, error_type, error_str);
        Q_EMIT deleteEnvironmentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteEnvironmentAccountConnection(const QString &x_amz_target, const OAIDeleteEnvironmentAccountConnectionInput &oai_delete_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteEnvironmentAccountConnection"][_serverIndices.value("deleteEnvironmentAccountConnection")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteEnvironmentAccountConnection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_environment_account_connection_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteEnvironmentAccountConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteEnvironmentAccountConnectionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteEnvironmentAccountConnectionSignal(output);
        Q_EMIT deleteEnvironmentAccountConnectionSignalFull(worker, output);
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

        Q_EMIT deleteEnvironmentAccountConnectionSignalE(output, error_type, error_str);
        Q_EMIT deleteEnvironmentAccountConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteEnvironmentAccountConnectionSignalError(output, error_type, error_str);
        Q_EMIT deleteEnvironmentAccountConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteEnvironmentTemplate(const QString &x_amz_target, const OAIDeleteEnvironmentTemplateInput &oai_delete_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteEnvironmentTemplate"][_serverIndices.value("deleteEnvironmentTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteEnvironmentTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_environment_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteEnvironmentTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteEnvironmentTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteEnvironmentTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteEnvironmentTemplateSignal(output);
        Q_EMIT deleteEnvironmentTemplateSignalFull(worker, output);
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

        Q_EMIT deleteEnvironmentTemplateSignalE(output, error_type, error_str);
        Q_EMIT deleteEnvironmentTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteEnvironmentTemplateSignalError(output, error_type, error_str);
        Q_EMIT deleteEnvironmentTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteEnvironmentTemplateVersion(const QString &x_amz_target, const OAIDeleteEnvironmentTemplateVersionInput &oai_delete_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteEnvironmentTemplateVersion"][_serverIndices.value("deleteEnvironmentTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteEnvironmentTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_environment_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteEnvironmentTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteEnvironmentTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteEnvironmentTemplateVersionSignal(output);
        Q_EMIT deleteEnvironmentTemplateVersionSignalFull(worker, output);
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

        Q_EMIT deleteEnvironmentTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT deleteEnvironmentTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteEnvironmentTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT deleteEnvironmentTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteRepository(const QString &x_amz_target, const OAIDeleteRepositoryInput &oai_delete_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteRepository"][_serverIndices.value("deleteRepository")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteRepository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_repository_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
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
    OAIDeleteRepositoryOutput output(QString(worker->response));
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

void OAIDefaultApi::deleteService(const QString &x_amz_target, const OAIDeleteServiceInput &oai_delete_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteService"][_serverIndices.value("deleteService")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteService");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_service_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteServiceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteServiceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteServiceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteServiceSignal(output);
        Q_EMIT deleteServiceSignalFull(worker, output);
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

        Q_EMIT deleteServiceSignalE(output, error_type, error_str);
        Q_EMIT deleteServiceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteServiceSignalError(output, error_type, error_str);
        Q_EMIT deleteServiceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteServiceSyncConfig(const QString &x_amz_target, const OAIDeleteServiceSyncConfigInput &oai_delete_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteServiceSyncConfig"][_serverIndices.value("deleteServiceSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteServiceSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_service_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteServiceSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteServiceSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteServiceSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteServiceSyncConfigSignal(output);
        Q_EMIT deleteServiceSyncConfigSignalFull(worker, output);
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

        Q_EMIT deleteServiceSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT deleteServiceSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteServiceSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT deleteServiceSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteServiceTemplate(const QString &x_amz_target, const OAIDeleteServiceTemplateInput &oai_delete_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteServiceTemplate"][_serverIndices.value("deleteServiceTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteServiceTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_service_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteServiceTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteServiceTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteServiceTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteServiceTemplateSignal(output);
        Q_EMIT deleteServiceTemplateSignalFull(worker, output);
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

        Q_EMIT deleteServiceTemplateSignalE(output, error_type, error_str);
        Q_EMIT deleteServiceTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteServiceTemplateSignalError(output, error_type, error_str);
        Q_EMIT deleteServiceTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteServiceTemplateVersion(const QString &x_amz_target, const OAIDeleteServiceTemplateVersionInput &oai_delete_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteServiceTemplateVersion"][_serverIndices.value("deleteServiceTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteServiceTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_service_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteServiceTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteServiceTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteServiceTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteServiceTemplateVersionSignal(output);
        Q_EMIT deleteServiceTemplateVersionSignalFull(worker, output);
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

        Q_EMIT deleteServiceTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT deleteServiceTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteServiceTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT deleteServiceTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteTemplateSyncConfig(const QString &x_amz_target, const OAIDeleteTemplateSyncConfigInput &oai_delete_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteTemplateSyncConfig"][_serverIndices.value("deleteTemplateSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.DeleteTemplateSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_template_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteTemplateSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteTemplateSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteTemplateSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteTemplateSyncConfigSignal(output);
        Q_EMIT deleteTemplateSyncConfigSignalFull(worker, output);
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

        Q_EMIT deleteTemplateSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT deleteTemplateSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteTemplateSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT deleteTemplateSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getAccountSettings(const QString &x_amz_target, const OAIObject &body, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getAccountSettings"][_serverIndices.value("getAccountSettings")].URL()+"/#X-Amz-Target=AwsProton20200720.GetAccountSettings");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = body.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getAccountSettingsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getAccountSettingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetAccountSettingsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getAccountSettingsSignal(output);
        Q_EMIT getAccountSettingsSignalFull(worker, output);
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

        Q_EMIT getAccountSettingsSignalE(output, error_type, error_str);
        Q_EMIT getAccountSettingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getAccountSettingsSignalError(output, error_type, error_str);
        Q_EMIT getAccountSettingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getComponent(const QString &x_amz_target, const OAIGetComponentInput &oai_get_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getComponent"][_serverIndices.value("getComponent")].URL()+"/#X-Amz-Target=AwsProton20200720.GetComponent");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_component_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getComponentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getComponentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetComponentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getComponentSignal(output);
        Q_EMIT getComponentSignalFull(worker, output);
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

        Q_EMIT getComponentSignalE(output, error_type, error_str);
        Q_EMIT getComponentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getComponentSignalError(output, error_type, error_str);
        Q_EMIT getComponentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getDeployment(const QString &x_amz_target, const OAIGetDeploymentInput &oai_get_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getDeployment"][_serverIndices.value("getDeployment")].URL()+"/#X-Amz-Target=AwsProton20200720.GetDeployment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_deployment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getDeploymentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getDeploymentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetDeploymentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getDeploymentSignal(output);
        Q_EMIT getDeploymentSignalFull(worker, output);
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

        Q_EMIT getDeploymentSignalE(output, error_type, error_str);
        Q_EMIT getDeploymentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getDeploymentSignalError(output, error_type, error_str);
        Q_EMIT getDeploymentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getEnvironment(const QString &x_amz_target, const OAIGetEnvironmentInput &oai_get_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getEnvironment"][_serverIndices.value("getEnvironment")].URL()+"/#X-Amz-Target=AwsProton20200720.GetEnvironment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_environment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getEnvironmentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getEnvironmentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetEnvironmentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getEnvironmentSignal(output);
        Q_EMIT getEnvironmentSignalFull(worker, output);
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

        Q_EMIT getEnvironmentSignalE(output, error_type, error_str);
        Q_EMIT getEnvironmentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getEnvironmentSignalError(output, error_type, error_str);
        Q_EMIT getEnvironmentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getEnvironmentAccountConnection(const QString &x_amz_target, const OAIGetEnvironmentAccountConnectionInput &oai_get_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getEnvironmentAccountConnection"][_serverIndices.value("getEnvironmentAccountConnection")].URL()+"/#X-Amz-Target=AwsProton20200720.GetEnvironmentAccountConnection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_environment_account_connection_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getEnvironmentAccountConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetEnvironmentAccountConnectionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getEnvironmentAccountConnectionSignal(output);
        Q_EMIT getEnvironmentAccountConnectionSignalFull(worker, output);
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

        Q_EMIT getEnvironmentAccountConnectionSignalE(output, error_type, error_str);
        Q_EMIT getEnvironmentAccountConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getEnvironmentAccountConnectionSignalError(output, error_type, error_str);
        Q_EMIT getEnvironmentAccountConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getEnvironmentTemplate(const QString &x_amz_target, const OAIGetEnvironmentTemplateInput &oai_get_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getEnvironmentTemplate"][_serverIndices.value("getEnvironmentTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.GetEnvironmentTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_environment_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getEnvironmentTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getEnvironmentTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetEnvironmentTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getEnvironmentTemplateSignal(output);
        Q_EMIT getEnvironmentTemplateSignalFull(worker, output);
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

        Q_EMIT getEnvironmentTemplateSignalE(output, error_type, error_str);
        Q_EMIT getEnvironmentTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getEnvironmentTemplateSignalError(output, error_type, error_str);
        Q_EMIT getEnvironmentTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getEnvironmentTemplateVersion(const QString &x_amz_target, const OAIGetEnvironmentTemplateVersionInput &oai_get_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getEnvironmentTemplateVersion"][_serverIndices.value("getEnvironmentTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.GetEnvironmentTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_environment_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getEnvironmentTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetEnvironmentTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getEnvironmentTemplateVersionSignal(output);
        Q_EMIT getEnvironmentTemplateVersionSignalFull(worker, output);
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

        Q_EMIT getEnvironmentTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT getEnvironmentTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getEnvironmentTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT getEnvironmentTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getRepository(const QString &x_amz_target, const OAIGetRepositoryInput &oai_get_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getRepository"][_serverIndices.value("getRepository")].URL()+"/#X-Amz-Target=AwsProton20200720.GetRepository");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_repository_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getRepositoryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getRepositoryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetRepositoryOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getRepositorySignal(output);
        Q_EMIT getRepositorySignalFull(worker, output);
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

        Q_EMIT getRepositorySignalE(output, error_type, error_str);
        Q_EMIT getRepositorySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getRepositorySignalError(output, error_type, error_str);
        Q_EMIT getRepositorySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getRepositorySyncStatus(const QString &x_amz_target, const OAIGetRepositorySyncStatusInput &oai_get_repository_sync_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getRepositorySyncStatus"][_serverIndices.value("getRepositorySyncStatus")].URL()+"/#X-Amz-Target=AwsProton20200720.GetRepositorySyncStatus");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_repository_sync_status_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getRepositorySyncStatusCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getRepositorySyncStatusCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetRepositorySyncStatusOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getRepositorySyncStatusSignal(output);
        Q_EMIT getRepositorySyncStatusSignalFull(worker, output);
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

        Q_EMIT getRepositorySyncStatusSignalE(output, error_type, error_str);
        Q_EMIT getRepositorySyncStatusSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getRepositorySyncStatusSignalError(output, error_type, error_str);
        Q_EMIT getRepositorySyncStatusSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getResourcesSummary(const QString &x_amz_target, const OAIObject &body, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getResourcesSummary"][_serverIndices.value("getResourcesSummary")].URL()+"/#X-Amz-Target=AwsProton20200720.GetResourcesSummary");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = body.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getResourcesSummaryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getResourcesSummaryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetResourcesSummaryOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getResourcesSummarySignal(output);
        Q_EMIT getResourcesSummarySignalFull(worker, output);
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

        Q_EMIT getResourcesSummarySignalE(output, error_type, error_str);
        Q_EMIT getResourcesSummarySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getResourcesSummarySignalError(output, error_type, error_str);
        Q_EMIT getResourcesSummarySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getService(const QString &x_amz_target, const OAIGetServiceInput &oai_get_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getService"][_serverIndices.value("getService")].URL()+"/#X-Amz-Target=AwsProton20200720.GetService");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceSignal(output);
        Q_EMIT getServiceSignalFull(worker, output);
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

        Q_EMIT getServiceSignalE(output, error_type, error_str);
        Q_EMIT getServiceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceSignalError(output, error_type, error_str);
        Q_EMIT getServiceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getServiceInstance(const QString &x_amz_target, const OAIGetServiceInstanceInput &oai_get_service_instance_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getServiceInstance"][_serverIndices.value("getServiceInstance")].URL()+"/#X-Amz-Target=AwsProton20200720.GetServiceInstance");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_instance_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceInstanceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceInstanceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceInstanceSignal(output);
        Q_EMIT getServiceInstanceSignalFull(worker, output);
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

        Q_EMIT getServiceInstanceSignalE(output, error_type, error_str);
        Q_EMIT getServiceInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceInstanceSignalError(output, error_type, error_str);
        Q_EMIT getServiceInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getServiceInstanceSyncStatus(const QString &x_amz_target, const OAIGetServiceInstanceSyncStatusInput &oai_get_service_instance_sync_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getServiceInstanceSyncStatus"][_serverIndices.value("getServiceInstanceSyncStatus")].URL()+"/#X-Amz-Target=AwsProton20200720.GetServiceInstanceSyncStatus");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_instance_sync_status_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceInstanceSyncStatusCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceInstanceSyncStatusCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceInstanceSyncStatusOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceInstanceSyncStatusSignal(output);
        Q_EMIT getServiceInstanceSyncStatusSignalFull(worker, output);
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

        Q_EMIT getServiceInstanceSyncStatusSignalE(output, error_type, error_str);
        Q_EMIT getServiceInstanceSyncStatusSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceInstanceSyncStatusSignalError(output, error_type, error_str);
        Q_EMIT getServiceInstanceSyncStatusSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getServiceSyncBlockerSummary(const QString &x_amz_target, const OAIGetServiceSyncBlockerSummaryInput &oai_get_service_sync_blocker_summary_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getServiceSyncBlockerSummary"][_serverIndices.value("getServiceSyncBlockerSummary")].URL()+"/#X-Amz-Target=AwsProton20200720.GetServiceSyncBlockerSummary");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_sync_blocker_summary_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceSyncBlockerSummaryCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceSyncBlockerSummaryCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceSyncBlockerSummaryOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceSyncBlockerSummarySignal(output);
        Q_EMIT getServiceSyncBlockerSummarySignalFull(worker, output);
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

        Q_EMIT getServiceSyncBlockerSummarySignalE(output, error_type, error_str);
        Q_EMIT getServiceSyncBlockerSummarySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceSyncBlockerSummarySignalError(output, error_type, error_str);
        Q_EMIT getServiceSyncBlockerSummarySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getServiceSyncConfig(const QString &x_amz_target, const OAIGetServiceSyncConfigInput &oai_get_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getServiceSyncConfig"][_serverIndices.value("getServiceSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.GetServiceSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceSyncConfigSignal(output);
        Q_EMIT getServiceSyncConfigSignalFull(worker, output);
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

        Q_EMIT getServiceSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT getServiceSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT getServiceSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getServiceTemplate(const QString &x_amz_target, const OAIGetServiceTemplateInput &oai_get_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getServiceTemplate"][_serverIndices.value("getServiceTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.GetServiceTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceTemplateSignal(output);
        Q_EMIT getServiceTemplateSignalFull(worker, output);
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

        Q_EMIT getServiceTemplateSignalE(output, error_type, error_str);
        Q_EMIT getServiceTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceTemplateSignalError(output, error_type, error_str);
        Q_EMIT getServiceTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getServiceTemplateVersion(const QString &x_amz_target, const OAIGetServiceTemplateVersionInput &oai_get_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getServiceTemplateVersion"][_serverIndices.value("getServiceTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.GetServiceTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_service_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getServiceTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getServiceTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetServiceTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getServiceTemplateVersionSignal(output);
        Q_EMIT getServiceTemplateVersionSignalFull(worker, output);
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

        Q_EMIT getServiceTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT getServiceTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getServiceTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT getServiceTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getTemplateSyncConfig(const QString &x_amz_target, const OAIGetTemplateSyncConfigInput &oai_get_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getTemplateSyncConfig"][_serverIndices.value("getTemplateSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.GetTemplateSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_template_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getTemplateSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getTemplateSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetTemplateSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTemplateSyncConfigSignal(output);
        Q_EMIT getTemplateSyncConfigSignalFull(worker, output);
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

        Q_EMIT getTemplateSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT getTemplateSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTemplateSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT getTemplateSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getTemplateSyncStatus(const QString &x_amz_target, const OAIGetTemplateSyncStatusInput &oai_get_template_sync_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getTemplateSyncStatus"][_serverIndices.value("getTemplateSyncStatus")].URL()+"/#X-Amz-Target=AwsProton20200720.GetTemplateSyncStatus");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_template_sync_status_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getTemplateSyncStatusCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getTemplateSyncStatusCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetTemplateSyncStatusOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTemplateSyncStatusSignal(output);
        Q_EMIT getTemplateSyncStatusSignalFull(worker, output);
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

        Q_EMIT getTemplateSyncStatusSignalE(output, error_type, error_str);
        Q_EMIT getTemplateSyncStatusSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTemplateSyncStatusSignalError(output, error_type, error_str);
        Q_EMIT getTemplateSyncStatusSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listComponentOutputs(const QString &x_amz_target, const OAIListComponentOutputsInput &oai_list_component_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listComponentOutputs"][_serverIndices.value("listComponentOutputs")].URL()+"/#X-Amz-Target=AwsProton20200720.ListComponentOutputs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_component_outputs_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listComponentOutputsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listComponentOutputsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListComponentOutputsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listComponentOutputsSignal(output);
        Q_EMIT listComponentOutputsSignalFull(worker, output);
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

        Q_EMIT listComponentOutputsSignalE(output, error_type, error_str);
        Q_EMIT listComponentOutputsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listComponentOutputsSignalError(output, error_type, error_str);
        Q_EMIT listComponentOutputsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listComponentProvisionedResources(const QString &x_amz_target, const OAIListComponentProvisionedResourcesInput &oai_list_component_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listComponentProvisionedResources"][_serverIndices.value("listComponentProvisionedResources")].URL()+"/#X-Amz-Target=AwsProton20200720.ListComponentProvisionedResources");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_component_provisioned_resources_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listComponentProvisionedResourcesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listComponentProvisionedResourcesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListComponentProvisionedResourcesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listComponentProvisionedResourcesSignal(output);
        Q_EMIT listComponentProvisionedResourcesSignalFull(worker, output);
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

        Q_EMIT listComponentProvisionedResourcesSignalE(output, error_type, error_str);
        Q_EMIT listComponentProvisionedResourcesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listComponentProvisionedResourcesSignalError(output, error_type, error_str);
        Q_EMIT listComponentProvisionedResourcesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listComponents(const QString &x_amz_target, const OAIListComponentsInput &oai_list_components_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listComponents"][_serverIndices.value("listComponents")].URL()+"/#X-Amz-Target=AwsProton20200720.ListComponents");
    
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

        
        QByteArray output = oai_list_components_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listComponentsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listComponentsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListComponentsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listComponentsSignal(output);
        Q_EMIT listComponentsSignalFull(worker, output);
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

        Q_EMIT listComponentsSignalE(output, error_type, error_str);
        Q_EMIT listComponentsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listComponentsSignalError(output, error_type, error_str);
        Q_EMIT listComponentsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listDeployments(const QString &x_amz_target, const OAIListDeploymentsInput &oai_list_deployments_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listDeployments"][_serverIndices.value("listDeployments")].URL()+"/#X-Amz-Target=AwsProton20200720.ListDeployments");
    
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

        
        QByteArray output = oai_list_deployments_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listDeploymentsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listDeploymentsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListDeploymentsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listDeploymentsSignal(output);
        Q_EMIT listDeploymentsSignalFull(worker, output);
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

        Q_EMIT listDeploymentsSignalE(output, error_type, error_str);
        Q_EMIT listDeploymentsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listDeploymentsSignalError(output, error_type, error_str);
        Q_EMIT listDeploymentsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listEnvironmentAccountConnections(const QString &x_amz_target, const OAIListEnvironmentAccountConnectionsInput &oai_list_environment_account_connections_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listEnvironmentAccountConnections"][_serverIndices.value("listEnvironmentAccountConnections")].URL()+"/#X-Amz-Target=AwsProton20200720.ListEnvironmentAccountConnections");
    
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

        
        QByteArray output = oai_list_environment_account_connections_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listEnvironmentAccountConnectionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listEnvironmentAccountConnectionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListEnvironmentAccountConnectionsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listEnvironmentAccountConnectionsSignal(output);
        Q_EMIT listEnvironmentAccountConnectionsSignalFull(worker, output);
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

        Q_EMIT listEnvironmentAccountConnectionsSignalE(output, error_type, error_str);
        Q_EMIT listEnvironmentAccountConnectionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listEnvironmentAccountConnectionsSignalError(output, error_type, error_str);
        Q_EMIT listEnvironmentAccountConnectionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listEnvironmentOutputs(const QString &x_amz_target, const OAIListEnvironmentOutputsInput &oai_list_environment_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listEnvironmentOutputs"][_serverIndices.value("listEnvironmentOutputs")].URL()+"/#X-Amz-Target=AwsProton20200720.ListEnvironmentOutputs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_environment_outputs_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listEnvironmentOutputsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listEnvironmentOutputsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListEnvironmentOutputsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listEnvironmentOutputsSignal(output);
        Q_EMIT listEnvironmentOutputsSignalFull(worker, output);
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

        Q_EMIT listEnvironmentOutputsSignalE(output, error_type, error_str);
        Q_EMIT listEnvironmentOutputsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listEnvironmentOutputsSignalError(output, error_type, error_str);
        Q_EMIT listEnvironmentOutputsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listEnvironmentProvisionedResources(const QString &x_amz_target, const OAIListEnvironmentProvisionedResourcesInput &oai_list_environment_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listEnvironmentProvisionedResources"][_serverIndices.value("listEnvironmentProvisionedResources")].URL()+"/#X-Amz-Target=AwsProton20200720.ListEnvironmentProvisionedResources");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_environment_provisioned_resources_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listEnvironmentProvisionedResourcesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listEnvironmentProvisionedResourcesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListEnvironmentProvisionedResourcesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listEnvironmentProvisionedResourcesSignal(output);
        Q_EMIT listEnvironmentProvisionedResourcesSignalFull(worker, output);
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

        Q_EMIT listEnvironmentProvisionedResourcesSignalE(output, error_type, error_str);
        Q_EMIT listEnvironmentProvisionedResourcesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listEnvironmentProvisionedResourcesSignalError(output, error_type, error_str);
        Q_EMIT listEnvironmentProvisionedResourcesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listEnvironmentTemplateVersions(const QString &x_amz_target, const OAIListEnvironmentTemplateVersionsInput &oai_list_environment_template_versions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listEnvironmentTemplateVersions"][_serverIndices.value("listEnvironmentTemplateVersions")].URL()+"/#X-Amz-Target=AwsProton20200720.ListEnvironmentTemplateVersions");
    
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

        
        QByteArray output = oai_list_environment_template_versions_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listEnvironmentTemplateVersionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listEnvironmentTemplateVersionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListEnvironmentTemplateVersionsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listEnvironmentTemplateVersionsSignal(output);
        Q_EMIT listEnvironmentTemplateVersionsSignalFull(worker, output);
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

        Q_EMIT listEnvironmentTemplateVersionsSignalE(output, error_type, error_str);
        Q_EMIT listEnvironmentTemplateVersionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listEnvironmentTemplateVersionsSignalError(output, error_type, error_str);
        Q_EMIT listEnvironmentTemplateVersionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listEnvironmentTemplates(const QString &x_amz_target, const OAIListEnvironmentTemplatesInput &oai_list_environment_templates_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listEnvironmentTemplates"][_serverIndices.value("listEnvironmentTemplates")].URL()+"/#X-Amz-Target=AwsProton20200720.ListEnvironmentTemplates");
    
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

        
        QByteArray output = oai_list_environment_templates_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listEnvironmentTemplatesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listEnvironmentTemplatesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListEnvironmentTemplatesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listEnvironmentTemplatesSignal(output);
        Q_EMIT listEnvironmentTemplatesSignalFull(worker, output);
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

        Q_EMIT listEnvironmentTemplatesSignalE(output, error_type, error_str);
        Q_EMIT listEnvironmentTemplatesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listEnvironmentTemplatesSignalError(output, error_type, error_str);
        Q_EMIT listEnvironmentTemplatesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listEnvironments(const QString &x_amz_target, const OAIListEnvironmentsInput &oai_list_environments_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listEnvironments"][_serverIndices.value("listEnvironments")].URL()+"/#X-Amz-Target=AwsProton20200720.ListEnvironments");
    
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

        
        QByteArray output = oai_list_environments_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listEnvironmentsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listEnvironmentsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListEnvironmentsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listEnvironmentsSignal(output);
        Q_EMIT listEnvironmentsSignalFull(worker, output);
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

        Q_EMIT listEnvironmentsSignalE(output, error_type, error_str);
        Q_EMIT listEnvironmentsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listEnvironmentsSignalError(output, error_type, error_str);
        Q_EMIT listEnvironmentsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listRepositories(const QString &x_amz_target, const OAIListRepositoriesInput &oai_list_repositories_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listRepositories"][_serverIndices.value("listRepositories")].URL()+"/#X-Amz-Target=AwsProton20200720.ListRepositories");
    
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

        
        QByteArray output = oai_list_repositories_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
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
    OAIListRepositoriesOutput output(QString(worker->response));
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

void OAIDefaultApi::listRepositorySyncDefinitions(const QString &x_amz_target, const OAIListRepositorySyncDefinitionsInput &oai_list_repository_sync_definitions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listRepositorySyncDefinitions"][_serverIndices.value("listRepositorySyncDefinitions")].URL()+"/#X-Amz-Target=AwsProton20200720.ListRepositorySyncDefinitions");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_repository_sync_definitions_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listRepositorySyncDefinitionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listRepositorySyncDefinitionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListRepositorySyncDefinitionsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listRepositorySyncDefinitionsSignal(output);
        Q_EMIT listRepositorySyncDefinitionsSignalFull(worker, output);
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

        Q_EMIT listRepositorySyncDefinitionsSignalE(output, error_type, error_str);
        Q_EMIT listRepositorySyncDefinitionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listRepositorySyncDefinitionsSignalError(output, error_type, error_str);
        Q_EMIT listRepositorySyncDefinitionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServiceInstanceOutputs(const QString &x_amz_target, const OAIListServiceInstanceOutputsInput &oai_list_service_instance_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServiceInstanceOutputs"][_serverIndices.value("listServiceInstanceOutputs")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServiceInstanceOutputs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_service_instance_outputs_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServiceInstanceOutputsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServiceInstanceOutputsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServiceInstanceOutputsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServiceInstanceOutputsSignal(output);
        Q_EMIT listServiceInstanceOutputsSignalFull(worker, output);
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

        Q_EMIT listServiceInstanceOutputsSignalE(output, error_type, error_str);
        Q_EMIT listServiceInstanceOutputsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServiceInstanceOutputsSignalError(output, error_type, error_str);
        Q_EMIT listServiceInstanceOutputsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServiceInstanceProvisionedResources(const QString &x_amz_target, const OAIListServiceInstanceProvisionedResourcesInput &oai_list_service_instance_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServiceInstanceProvisionedResources"][_serverIndices.value("listServiceInstanceProvisionedResources")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServiceInstanceProvisionedResources");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_service_instance_provisioned_resources_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServiceInstanceProvisionedResourcesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServiceInstanceProvisionedResourcesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServiceInstanceProvisionedResourcesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServiceInstanceProvisionedResourcesSignal(output);
        Q_EMIT listServiceInstanceProvisionedResourcesSignalFull(worker, output);
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

        Q_EMIT listServiceInstanceProvisionedResourcesSignalE(output, error_type, error_str);
        Q_EMIT listServiceInstanceProvisionedResourcesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServiceInstanceProvisionedResourcesSignalError(output, error_type, error_str);
        Q_EMIT listServiceInstanceProvisionedResourcesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServiceInstances(const QString &x_amz_target, const OAIListServiceInstancesInput &oai_list_service_instances_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServiceInstances"][_serverIndices.value("listServiceInstances")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServiceInstances");
    
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

        
        QByteArray output = oai_list_service_instances_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServiceInstancesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServiceInstancesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServiceInstancesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServiceInstancesSignal(output);
        Q_EMIT listServiceInstancesSignalFull(worker, output);
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

        Q_EMIT listServiceInstancesSignalE(output, error_type, error_str);
        Q_EMIT listServiceInstancesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServiceInstancesSignalError(output, error_type, error_str);
        Q_EMIT listServiceInstancesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServicePipelineOutputs(const QString &x_amz_target, const OAIListServicePipelineOutputsInput &oai_list_service_pipeline_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServicePipelineOutputs"][_serverIndices.value("listServicePipelineOutputs")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServicePipelineOutputs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_service_pipeline_outputs_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServicePipelineOutputsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServicePipelineOutputsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServicePipelineOutputsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServicePipelineOutputsSignal(output);
        Q_EMIT listServicePipelineOutputsSignalFull(worker, output);
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

        Q_EMIT listServicePipelineOutputsSignalE(output, error_type, error_str);
        Q_EMIT listServicePipelineOutputsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServicePipelineOutputsSignalError(output, error_type, error_str);
        Q_EMIT listServicePipelineOutputsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServicePipelineProvisionedResources(const QString &x_amz_target, const OAIListServicePipelineProvisionedResourcesInput &oai_list_service_pipeline_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServicePipelineProvisionedResources"][_serverIndices.value("listServicePipelineProvisionedResources")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServicePipelineProvisionedResources");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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

        
        QByteArray output = oai_list_service_pipeline_provisioned_resources_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServicePipelineProvisionedResourcesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServicePipelineProvisionedResourcesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServicePipelineProvisionedResourcesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServicePipelineProvisionedResourcesSignal(output);
        Q_EMIT listServicePipelineProvisionedResourcesSignalFull(worker, output);
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

        Q_EMIT listServicePipelineProvisionedResourcesSignalE(output, error_type, error_str);
        Q_EMIT listServicePipelineProvisionedResourcesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServicePipelineProvisionedResourcesSignalError(output, error_type, error_str);
        Q_EMIT listServicePipelineProvisionedResourcesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServiceTemplateVersions(const QString &x_amz_target, const OAIListServiceTemplateVersionsInput &oai_list_service_template_versions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServiceTemplateVersions"][_serverIndices.value("listServiceTemplateVersions")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServiceTemplateVersions");
    
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

        
        QByteArray output = oai_list_service_template_versions_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServiceTemplateVersionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServiceTemplateVersionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServiceTemplateVersionsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServiceTemplateVersionsSignal(output);
        Q_EMIT listServiceTemplateVersionsSignalFull(worker, output);
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

        Q_EMIT listServiceTemplateVersionsSignalE(output, error_type, error_str);
        Q_EMIT listServiceTemplateVersionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServiceTemplateVersionsSignalError(output, error_type, error_str);
        Q_EMIT listServiceTemplateVersionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServiceTemplates(const QString &x_amz_target, const OAIListServiceTemplatesInput &oai_list_service_templates_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServiceTemplates"][_serverIndices.value("listServiceTemplates")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServiceTemplates");
    
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

        
        QByteArray output = oai_list_service_templates_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServiceTemplatesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServiceTemplatesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServiceTemplatesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServiceTemplatesSignal(output);
        Q_EMIT listServiceTemplatesSignalFull(worker, output);
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

        Q_EMIT listServiceTemplatesSignalE(output, error_type, error_str);
        Q_EMIT listServiceTemplatesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServiceTemplatesSignalError(output, error_type, error_str);
        Q_EMIT listServiceTemplatesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listServices(const QString &x_amz_target, const OAIListServicesInput &oai_list_services_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listServices"][_serverIndices.value("listServices")].URL()+"/#X-Amz-Target=AwsProton20200720.ListServices");
    
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

        
        QByteArray output = oai_list_services_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listServicesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listServicesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListServicesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listServicesSignal(output);
        Q_EMIT listServicesSignalFull(worker, output);
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

        Q_EMIT listServicesSignalE(output, error_type, error_str);
        Q_EMIT listServicesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listServicesSignalError(output, error_type, error_str);
        Q_EMIT listServicesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listTagsForResource(const QString &x_amz_target, const OAIListTagsForResourceInput &oai_list_tags_for_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listTagsForResource"][_serverIndices.value("listTagsForResource")].URL()+"/#X-Amz-Target=AwsProton20200720.ListTagsForResource");
    
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

        
        QByteArray output = oai_list_tags_for_resource_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
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
    OAIListTagsForResourceOutput output(QString(worker->response));
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

void OAIDefaultApi::notifyResourceDeploymentStatusChange(const QString &x_amz_target, const OAINotifyResourceDeploymentStatusChangeInput &oai_notify_resource_deployment_status_change_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["notifyResourceDeploymentStatusChange"][_serverIndices.value("notifyResourceDeploymentStatusChange")].URL()+"/#X-Amz-Target=AwsProton20200720.NotifyResourceDeploymentStatusChange");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_notify_resource_deployment_status_change_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::notifyResourceDeploymentStatusChangeCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::notifyResourceDeploymentStatusChangeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT notifyResourceDeploymentStatusChangeSignal(output);
        Q_EMIT notifyResourceDeploymentStatusChangeSignalFull(worker, output);
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

        Q_EMIT notifyResourceDeploymentStatusChangeSignalE(output, error_type, error_str);
        Q_EMIT notifyResourceDeploymentStatusChangeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT notifyResourceDeploymentStatusChangeSignalError(output, error_type, error_str);
        Q_EMIT notifyResourceDeploymentStatusChangeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::rejectEnvironmentAccountConnection(const QString &x_amz_target, const OAIRejectEnvironmentAccountConnectionInput &oai_reject_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["rejectEnvironmentAccountConnection"][_serverIndices.value("rejectEnvironmentAccountConnection")].URL()+"/#X-Amz-Target=AwsProton20200720.RejectEnvironmentAccountConnection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_reject_environment_account_connection_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::rejectEnvironmentAccountConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::rejectEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIRejectEnvironmentAccountConnectionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT rejectEnvironmentAccountConnectionSignal(output);
        Q_EMIT rejectEnvironmentAccountConnectionSignalFull(worker, output);
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

        Q_EMIT rejectEnvironmentAccountConnectionSignalE(output, error_type, error_str);
        Q_EMIT rejectEnvironmentAccountConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT rejectEnvironmentAccountConnectionSignalError(output, error_type, error_str);
        Q_EMIT rejectEnvironmentAccountConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tagResource(const QString &x_amz_target, const OAITagResourceInput &oai_tag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["tagResource"][_serverIndices.value("tagResource")].URL()+"/#X-Amz-Target=AwsProton20200720.TagResource");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_tag_resource_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
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

void OAIDefaultApi::untagResource(const QString &x_amz_target, const OAIUntagResourceInput &oai_untag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["untagResource"][_serverIndices.value("untagResource")].URL()+"/#X-Amz-Target=AwsProton20200720.UntagResource");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_untag_resource_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
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

void OAIDefaultApi::updateAccountSettings(const QString &x_amz_target, const OAIUpdateAccountSettingsInput &oai_update_account_settings_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateAccountSettings"][_serverIndices.value("updateAccountSettings")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateAccountSettings");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_account_settings_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateAccountSettingsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateAccountSettingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateAccountSettingsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateAccountSettingsSignal(output);
        Q_EMIT updateAccountSettingsSignalFull(worker, output);
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

        Q_EMIT updateAccountSettingsSignalE(output, error_type, error_str);
        Q_EMIT updateAccountSettingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateAccountSettingsSignalError(output, error_type, error_str);
        Q_EMIT updateAccountSettingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateComponent(const QString &x_amz_target, const OAIUpdateComponentInput &oai_update_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateComponent"][_serverIndices.value("updateComponent")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateComponent");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_component_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateComponentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateComponentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateComponentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateComponentSignal(output);
        Q_EMIT updateComponentSignalFull(worker, output);
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

        Q_EMIT updateComponentSignalE(output, error_type, error_str);
        Q_EMIT updateComponentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateComponentSignalError(output, error_type, error_str);
        Q_EMIT updateComponentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateEnvironment(const QString &x_amz_target, const OAIUpdateEnvironmentInput &oai_update_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateEnvironment"][_serverIndices.value("updateEnvironment")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateEnvironment");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_environment_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateEnvironmentCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateEnvironmentCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateEnvironmentOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateEnvironmentSignal(output);
        Q_EMIT updateEnvironmentSignalFull(worker, output);
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

        Q_EMIT updateEnvironmentSignalE(output, error_type, error_str);
        Q_EMIT updateEnvironmentSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateEnvironmentSignalError(output, error_type, error_str);
        Q_EMIT updateEnvironmentSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateEnvironmentAccountConnection(const QString &x_amz_target, const OAIUpdateEnvironmentAccountConnectionInput &oai_update_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateEnvironmentAccountConnection"][_serverIndices.value("updateEnvironmentAccountConnection")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateEnvironmentAccountConnection");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_environment_account_connection_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateEnvironmentAccountConnectionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateEnvironmentAccountConnectionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateEnvironmentAccountConnectionSignal(output);
        Q_EMIT updateEnvironmentAccountConnectionSignalFull(worker, output);
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

        Q_EMIT updateEnvironmentAccountConnectionSignalE(output, error_type, error_str);
        Q_EMIT updateEnvironmentAccountConnectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateEnvironmentAccountConnectionSignalError(output, error_type, error_str);
        Q_EMIT updateEnvironmentAccountConnectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateEnvironmentTemplate(const QString &x_amz_target, const OAIUpdateEnvironmentTemplateInput &oai_update_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateEnvironmentTemplate"][_serverIndices.value("updateEnvironmentTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateEnvironmentTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_environment_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateEnvironmentTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateEnvironmentTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateEnvironmentTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateEnvironmentTemplateSignal(output);
        Q_EMIT updateEnvironmentTemplateSignalFull(worker, output);
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

        Q_EMIT updateEnvironmentTemplateSignalE(output, error_type, error_str);
        Q_EMIT updateEnvironmentTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateEnvironmentTemplateSignalError(output, error_type, error_str);
        Q_EMIT updateEnvironmentTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateEnvironmentTemplateVersion(const QString &x_amz_target, const OAIUpdateEnvironmentTemplateVersionInput &oai_update_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateEnvironmentTemplateVersion"][_serverIndices.value("updateEnvironmentTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateEnvironmentTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_environment_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateEnvironmentTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateEnvironmentTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateEnvironmentTemplateVersionSignal(output);
        Q_EMIT updateEnvironmentTemplateVersionSignalFull(worker, output);
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

        Q_EMIT updateEnvironmentTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT updateEnvironmentTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateEnvironmentTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT updateEnvironmentTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateService(const QString &x_amz_target, const OAIUpdateServiceInput &oai_update_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateService"][_serverIndices.value("updateService")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateService");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServiceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServiceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServiceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServiceSignal(output);
        Q_EMIT updateServiceSignalFull(worker, output);
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

        Q_EMIT updateServiceSignalE(output, error_type, error_str);
        Q_EMIT updateServiceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServiceSignalError(output, error_type, error_str);
        Q_EMIT updateServiceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateServiceInstance(const QString &x_amz_target, const OAIUpdateServiceInstanceInput &oai_update_service_instance_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateServiceInstance"][_serverIndices.value("updateServiceInstance")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateServiceInstance");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_instance_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServiceInstanceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServiceInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServiceInstanceOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServiceInstanceSignal(output);
        Q_EMIT updateServiceInstanceSignalFull(worker, output);
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

        Q_EMIT updateServiceInstanceSignalE(output, error_type, error_str);
        Q_EMIT updateServiceInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServiceInstanceSignalError(output, error_type, error_str);
        Q_EMIT updateServiceInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateServicePipeline(const QString &x_amz_target, const OAIUpdateServicePipelineInput &oai_update_service_pipeline_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateServicePipeline"][_serverIndices.value("updateServicePipeline")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateServicePipeline");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_pipeline_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServicePipelineCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServicePipelineCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServicePipelineOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServicePipelineSignal(output);
        Q_EMIT updateServicePipelineSignalFull(worker, output);
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

        Q_EMIT updateServicePipelineSignalE(output, error_type, error_str);
        Q_EMIT updateServicePipelineSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServicePipelineSignalError(output, error_type, error_str);
        Q_EMIT updateServicePipelineSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateServiceSyncBlocker(const QString &x_amz_target, const OAIUpdateServiceSyncBlockerInput &oai_update_service_sync_blocker_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateServiceSyncBlocker"][_serverIndices.value("updateServiceSyncBlocker")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateServiceSyncBlocker");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_sync_blocker_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServiceSyncBlockerCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServiceSyncBlockerCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServiceSyncBlockerOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServiceSyncBlockerSignal(output);
        Q_EMIT updateServiceSyncBlockerSignalFull(worker, output);
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

        Q_EMIT updateServiceSyncBlockerSignalE(output, error_type, error_str);
        Q_EMIT updateServiceSyncBlockerSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServiceSyncBlockerSignalError(output, error_type, error_str);
        Q_EMIT updateServiceSyncBlockerSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateServiceSyncConfig(const QString &x_amz_target, const OAIUpdateServiceSyncConfigInput &oai_update_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateServiceSyncConfig"][_serverIndices.value("updateServiceSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateServiceSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServiceSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServiceSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServiceSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServiceSyncConfigSignal(output);
        Q_EMIT updateServiceSyncConfigSignalFull(worker, output);
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

        Q_EMIT updateServiceSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT updateServiceSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServiceSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT updateServiceSyncConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateServiceTemplate(const QString &x_amz_target, const OAIUpdateServiceTemplateInput &oai_update_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateServiceTemplate"][_serverIndices.value("updateServiceTemplate")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateServiceTemplate");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_template_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServiceTemplateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServiceTemplateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServiceTemplateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServiceTemplateSignal(output);
        Q_EMIT updateServiceTemplateSignalFull(worker, output);
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

        Q_EMIT updateServiceTemplateSignalE(output, error_type, error_str);
        Q_EMIT updateServiceTemplateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServiceTemplateSignalError(output, error_type, error_str);
        Q_EMIT updateServiceTemplateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateServiceTemplateVersion(const QString &x_amz_target, const OAIUpdateServiceTemplateVersionInput &oai_update_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateServiceTemplateVersion"][_serverIndices.value("updateServiceTemplateVersion")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateServiceTemplateVersion");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_service_template_version_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateServiceTemplateVersionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateServiceTemplateVersionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateServiceTemplateVersionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateServiceTemplateVersionSignal(output);
        Q_EMIT updateServiceTemplateVersionSignalFull(worker, output);
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

        Q_EMIT updateServiceTemplateVersionSignalE(output, error_type, error_str);
        Q_EMIT updateServiceTemplateVersionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateServiceTemplateVersionSignalError(output, error_type, error_str);
        Q_EMIT updateServiceTemplateVersionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateTemplateSyncConfig(const QString &x_amz_target, const OAIUpdateTemplateSyncConfigInput &oai_update_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateTemplateSyncConfig"][_serverIndices.value("updateTemplateSyncConfig")].URL()+"/#X-Amz-Target=AwsProton20200720.UpdateTemplateSyncConfig");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_template_sync_config_input.asJson().toUtf8();
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
        if (!::OpenAPI::toStringValue(x_amz_target).isEmpty()) {
            input.headers.insert("X-Amz-Target", ::OpenAPI::toStringValue(x_amz_target));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateTemplateSyncConfigCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateTemplateSyncConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateTemplateSyncConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateTemplateSyncConfigSignal(output);
        Q_EMIT updateTemplateSyncConfigSignalFull(worker, output);
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

        Q_EMIT updateTemplateSyncConfigSignalE(output, error_type, error_str);
        Q_EMIT updateTemplateSyncConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateTemplateSyncConfigSignalError(output, error_type, error_str);
        Q_EMIT updateTemplateSyncConfigSignalErrorFull(worker, error_type, error_str);
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
