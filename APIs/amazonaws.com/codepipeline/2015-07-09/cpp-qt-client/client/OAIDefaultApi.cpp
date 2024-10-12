/**
 * AWS CodePipeline
 * <fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2015-07-09
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
    QUrl("http://codepipeline.{region}.amazonaws.com"),
    "The CodePipeline multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://codepipeline.{region}.amazonaws.com"),
    "The CodePipeline multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://codepipeline.{region}.amazonaws.com.cn"),
    "The CodePipeline endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://codepipeline.{region}.amazonaws.com.cn"),
    "The CodePipeline endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    _serverConfigs.insert("acknowledgeJob", defaultConf);
    _serverIndices.insert("acknowledgeJob", 0);
    _serverConfigs.insert("acknowledgeThirdPartyJob", defaultConf);
    _serverIndices.insert("acknowledgeThirdPartyJob", 0);
    _serverConfigs.insert("createCustomActionType", defaultConf);
    _serverIndices.insert("createCustomActionType", 0);
    _serverConfigs.insert("createPipeline", defaultConf);
    _serverIndices.insert("createPipeline", 0);
    _serverConfigs.insert("deleteCustomActionType", defaultConf);
    _serverIndices.insert("deleteCustomActionType", 0);
    _serverConfigs.insert("deletePipeline", defaultConf);
    _serverIndices.insert("deletePipeline", 0);
    _serverConfigs.insert("deleteWebhook", defaultConf);
    _serverIndices.insert("deleteWebhook", 0);
    _serverConfigs.insert("deregisterWebhookWithThirdParty", defaultConf);
    _serverIndices.insert("deregisterWebhookWithThirdParty", 0);
    _serverConfigs.insert("disableStageTransition", defaultConf);
    _serverIndices.insert("disableStageTransition", 0);
    _serverConfigs.insert("enableStageTransition", defaultConf);
    _serverIndices.insert("enableStageTransition", 0);
    _serverConfigs.insert("getActionType", defaultConf);
    _serverIndices.insert("getActionType", 0);
    _serverConfigs.insert("getJobDetails", defaultConf);
    _serverIndices.insert("getJobDetails", 0);
    _serverConfigs.insert("getPipeline", defaultConf);
    _serverIndices.insert("getPipeline", 0);
    _serverConfigs.insert("getPipelineExecution", defaultConf);
    _serverIndices.insert("getPipelineExecution", 0);
    _serverConfigs.insert("getPipelineState", defaultConf);
    _serverIndices.insert("getPipelineState", 0);
    _serverConfigs.insert("getThirdPartyJobDetails", defaultConf);
    _serverIndices.insert("getThirdPartyJobDetails", 0);
    _serverConfigs.insert("listActionExecutions", defaultConf);
    _serverIndices.insert("listActionExecutions", 0);
    _serverConfigs.insert("listActionTypes", defaultConf);
    _serverIndices.insert("listActionTypes", 0);
    _serverConfigs.insert("listPipelineExecutions", defaultConf);
    _serverIndices.insert("listPipelineExecutions", 0);
    _serverConfigs.insert("listPipelines", defaultConf);
    _serverIndices.insert("listPipelines", 0);
    _serverConfigs.insert("listTagsForResource", defaultConf);
    _serverIndices.insert("listTagsForResource", 0);
    _serverConfigs.insert("listWebhooks", defaultConf);
    _serverIndices.insert("listWebhooks", 0);
    _serverConfigs.insert("pollForJobs", defaultConf);
    _serverIndices.insert("pollForJobs", 0);
    _serverConfigs.insert("pollForThirdPartyJobs", defaultConf);
    _serverIndices.insert("pollForThirdPartyJobs", 0);
    _serverConfigs.insert("putActionRevision", defaultConf);
    _serverIndices.insert("putActionRevision", 0);
    _serverConfigs.insert("putApprovalResult", defaultConf);
    _serverIndices.insert("putApprovalResult", 0);
    _serverConfigs.insert("putJobFailureResult", defaultConf);
    _serverIndices.insert("putJobFailureResult", 0);
    _serverConfigs.insert("putJobSuccessResult", defaultConf);
    _serverIndices.insert("putJobSuccessResult", 0);
    _serverConfigs.insert("putThirdPartyJobFailureResult", defaultConf);
    _serverIndices.insert("putThirdPartyJobFailureResult", 0);
    _serverConfigs.insert("putThirdPartyJobSuccessResult", defaultConf);
    _serverIndices.insert("putThirdPartyJobSuccessResult", 0);
    _serverConfigs.insert("putWebhook", defaultConf);
    _serverIndices.insert("putWebhook", 0);
    _serverConfigs.insert("registerWebhookWithThirdParty", defaultConf);
    _serverIndices.insert("registerWebhookWithThirdParty", 0);
    _serverConfigs.insert("retryStageExecution", defaultConf);
    _serverIndices.insert("retryStageExecution", 0);
    _serverConfigs.insert("startPipelineExecution", defaultConf);
    _serverIndices.insert("startPipelineExecution", 0);
    _serverConfigs.insert("stopPipelineExecution", defaultConf);
    _serverIndices.insert("stopPipelineExecution", 0);
    _serverConfigs.insert("tagResource", defaultConf);
    _serverIndices.insert("tagResource", 0);
    _serverConfigs.insert("untagResource", defaultConf);
    _serverIndices.insert("untagResource", 0);
    _serverConfigs.insert("updateActionType", defaultConf);
    _serverIndices.insert("updateActionType", 0);
    _serverConfigs.insert("updatePipeline", defaultConf);
    _serverIndices.insert("updatePipeline", 0);
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

void OAIDefaultApi::acknowledgeJob(const QString &x_amz_target, const OAIAcknowledgeJobInput &oai_acknowledge_job_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["acknowledgeJob"][_serverIndices.value("acknowledgeJob")].URL()+"/#X-Amz-Target=CodePipeline_20150709.AcknowledgeJob");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_acknowledge_job_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::acknowledgeJobCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::acknowledgeJobCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAcknowledgeJobOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acknowledgeJobSignal(output);
        Q_EMIT acknowledgeJobSignalFull(worker, output);
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

        Q_EMIT acknowledgeJobSignalE(output, error_type, error_str);
        Q_EMIT acknowledgeJobSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acknowledgeJobSignalError(output, error_type, error_str);
        Q_EMIT acknowledgeJobSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::acknowledgeThirdPartyJob(const QString &x_amz_target, const OAIAcknowledgeThirdPartyJobInput &oai_acknowledge_third_party_job_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["acknowledgeThirdPartyJob"][_serverIndices.value("acknowledgeThirdPartyJob")].URL()+"/#X-Amz-Target=CodePipeline_20150709.AcknowledgeThirdPartyJob");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_acknowledge_third_party_job_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::acknowledgeThirdPartyJobCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::acknowledgeThirdPartyJobCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAcknowledgeThirdPartyJobOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acknowledgeThirdPartyJobSignal(output);
        Q_EMIT acknowledgeThirdPartyJobSignalFull(worker, output);
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

        Q_EMIT acknowledgeThirdPartyJobSignalE(output, error_type, error_str);
        Q_EMIT acknowledgeThirdPartyJobSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acknowledgeThirdPartyJobSignalError(output, error_type, error_str);
        Q_EMIT acknowledgeThirdPartyJobSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createCustomActionType(const QString &x_amz_target, const OAICreateCustomActionTypeInput &oai_create_custom_action_type_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createCustomActionType"][_serverIndices.value("createCustomActionType")].URL()+"/#X-Amz-Target=CodePipeline_20150709.CreateCustomActionType");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_custom_action_type_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createCustomActionTypeCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createCustomActionTypeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateCustomActionTypeOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createCustomActionTypeSignal(output);
        Q_EMIT createCustomActionTypeSignalFull(worker, output);
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

        Q_EMIT createCustomActionTypeSignalE(output, error_type, error_str);
        Q_EMIT createCustomActionTypeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createCustomActionTypeSignalError(output, error_type, error_str);
        Q_EMIT createCustomActionTypeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createPipeline(const QString &x_amz_target, const OAICreatePipelineInput &oai_create_pipeline_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createPipeline"][_serverIndices.value("createPipeline")].URL()+"/#X-Amz-Target=CodePipeline_20150709.CreatePipeline");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_pipeline_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createPipelineCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createPipelineCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreatePipelineOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createPipelineSignal(output);
        Q_EMIT createPipelineSignalFull(worker, output);
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

        Q_EMIT createPipelineSignalE(output, error_type, error_str);
        Q_EMIT createPipelineSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createPipelineSignalError(output, error_type, error_str);
        Q_EMIT createPipelineSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteCustomActionType(const QString &x_amz_target, const OAIDeleteCustomActionTypeInput &oai_delete_custom_action_type_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteCustomActionType"][_serverIndices.value("deleteCustomActionType")].URL()+"/#X-Amz-Target=CodePipeline_20150709.DeleteCustomActionType");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_custom_action_type_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteCustomActionTypeCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteCustomActionTypeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteCustomActionTypeSignal();
        Q_EMIT deleteCustomActionTypeSignalFull(worker);
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

        Q_EMIT deleteCustomActionTypeSignalE(error_type, error_str);
        Q_EMIT deleteCustomActionTypeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteCustomActionTypeSignalError(error_type, error_str);
        Q_EMIT deleteCustomActionTypeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deletePipeline(const QString &x_amz_target, const OAIDeletePipelineInput &oai_delete_pipeline_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deletePipeline"][_serverIndices.value("deletePipeline")].URL()+"/#X-Amz-Target=CodePipeline_20150709.DeletePipeline");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_pipeline_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deletePipelineCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deletePipelineCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deletePipelineSignal();
        Q_EMIT deletePipelineSignalFull(worker);
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

        Q_EMIT deletePipelineSignalE(error_type, error_str);
        Q_EMIT deletePipelineSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deletePipelineSignalError(error_type, error_str);
        Q_EMIT deletePipelineSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteWebhook(const QString &x_amz_target, const OAIDeleteWebhookInput &oai_delete_webhook_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteWebhook"][_serverIndices.value("deleteWebhook")].URL()+"/#X-Amz-Target=CodePipeline_20150709.DeleteWebhook");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_webhook_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteWebhookCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteWebhookCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteWebhookSignal(output);
        Q_EMIT deleteWebhookSignalFull(worker, output);
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

        Q_EMIT deleteWebhookSignalE(output, error_type, error_str);
        Q_EMIT deleteWebhookSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteWebhookSignalError(output, error_type, error_str);
        Q_EMIT deleteWebhookSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deregisterWebhookWithThirdParty(const QString &x_amz_target, const OAIDeregisterWebhookWithThirdPartyInput &oai_deregister_webhook_with_third_party_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deregisterWebhookWithThirdParty"][_serverIndices.value("deregisterWebhookWithThirdParty")].URL()+"/#X-Amz-Target=CodePipeline_20150709.DeregisterWebhookWithThirdParty");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_deregister_webhook_with_third_party_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deregisterWebhookWithThirdPartyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deregisterWebhookWithThirdPartyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deregisterWebhookWithThirdPartySignal(output);
        Q_EMIT deregisterWebhookWithThirdPartySignalFull(worker, output);
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

        Q_EMIT deregisterWebhookWithThirdPartySignalE(output, error_type, error_str);
        Q_EMIT deregisterWebhookWithThirdPartySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deregisterWebhookWithThirdPartySignalError(output, error_type, error_str);
        Q_EMIT deregisterWebhookWithThirdPartySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::disableStageTransition(const QString &x_amz_target, const OAIDisableStageTransitionInput &oai_disable_stage_transition_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["disableStageTransition"][_serverIndices.value("disableStageTransition")].URL()+"/#X-Amz-Target=CodePipeline_20150709.DisableStageTransition");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_disable_stage_transition_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::disableStageTransitionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::disableStageTransitionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT disableStageTransitionSignal();
        Q_EMIT disableStageTransitionSignalFull(worker);
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

        Q_EMIT disableStageTransitionSignalE(error_type, error_str);
        Q_EMIT disableStageTransitionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT disableStageTransitionSignalError(error_type, error_str);
        Q_EMIT disableStageTransitionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::enableStageTransition(const QString &x_amz_target, const OAIEnableStageTransitionInput &oai_enable_stage_transition_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["enableStageTransition"][_serverIndices.value("enableStageTransition")].URL()+"/#X-Amz-Target=CodePipeline_20150709.EnableStageTransition");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_enable_stage_transition_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::enableStageTransitionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::enableStageTransitionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT enableStageTransitionSignal();
        Q_EMIT enableStageTransitionSignalFull(worker);
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

        Q_EMIT enableStageTransitionSignalE(error_type, error_str);
        Q_EMIT enableStageTransitionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT enableStageTransitionSignalError(error_type, error_str);
        Q_EMIT enableStageTransitionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getActionType(const QString &x_amz_target, const OAIGetActionTypeInput &oai_get_action_type_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getActionType"][_serverIndices.value("getActionType")].URL()+"/#X-Amz-Target=CodePipeline_20150709.GetActionType");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_action_type_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getActionTypeCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getActionTypeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetActionTypeOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getActionTypeSignal(output);
        Q_EMIT getActionTypeSignalFull(worker, output);
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

        Q_EMIT getActionTypeSignalE(output, error_type, error_str);
        Q_EMIT getActionTypeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getActionTypeSignalError(output, error_type, error_str);
        Q_EMIT getActionTypeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getJobDetails(const QString &x_amz_target, const OAIGetJobDetailsInput &oai_get_job_details_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getJobDetails"][_serverIndices.value("getJobDetails")].URL()+"/#X-Amz-Target=CodePipeline_20150709.GetJobDetails");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_job_details_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getJobDetailsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getJobDetailsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetJobDetailsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getJobDetailsSignal(output);
        Q_EMIT getJobDetailsSignalFull(worker, output);
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

        Q_EMIT getJobDetailsSignalE(output, error_type, error_str);
        Q_EMIT getJobDetailsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getJobDetailsSignalError(output, error_type, error_str);
        Q_EMIT getJobDetailsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getPipeline(const QString &x_amz_target, const OAIGetPipelineInput &oai_get_pipeline_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getPipeline"][_serverIndices.value("getPipeline")].URL()+"/#X-Amz-Target=CodePipeline_20150709.GetPipeline");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_pipeline_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getPipelineCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getPipelineCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetPipelineOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getPipelineSignal(output);
        Q_EMIT getPipelineSignalFull(worker, output);
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

        Q_EMIT getPipelineSignalE(output, error_type, error_str);
        Q_EMIT getPipelineSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getPipelineSignalError(output, error_type, error_str);
        Q_EMIT getPipelineSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getPipelineExecution(const QString &x_amz_target, const OAIGetPipelineExecutionInput &oai_get_pipeline_execution_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getPipelineExecution"][_serverIndices.value("getPipelineExecution")].URL()+"/#X-Amz-Target=CodePipeline_20150709.GetPipelineExecution");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_pipeline_execution_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getPipelineExecutionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getPipelineExecutionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetPipelineExecutionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getPipelineExecutionSignal(output);
        Q_EMIT getPipelineExecutionSignalFull(worker, output);
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

        Q_EMIT getPipelineExecutionSignalE(output, error_type, error_str);
        Q_EMIT getPipelineExecutionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getPipelineExecutionSignalError(output, error_type, error_str);
        Q_EMIT getPipelineExecutionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getPipelineState(const QString &x_amz_target, const OAIGetPipelineStateInput &oai_get_pipeline_state_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getPipelineState"][_serverIndices.value("getPipelineState")].URL()+"/#X-Amz-Target=CodePipeline_20150709.GetPipelineState");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_pipeline_state_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getPipelineStateCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getPipelineStateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetPipelineStateOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getPipelineStateSignal(output);
        Q_EMIT getPipelineStateSignalFull(worker, output);
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

        Q_EMIT getPipelineStateSignalE(output, error_type, error_str);
        Q_EMIT getPipelineStateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getPipelineStateSignalError(output, error_type, error_str);
        Q_EMIT getPipelineStateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getThirdPartyJobDetails(const QString &x_amz_target, const OAIGetThirdPartyJobDetailsInput &oai_get_third_party_job_details_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getThirdPartyJobDetails"][_serverIndices.value("getThirdPartyJobDetails")].URL()+"/#X-Amz-Target=CodePipeline_20150709.GetThirdPartyJobDetails");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_third_party_job_details_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getThirdPartyJobDetailsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getThirdPartyJobDetailsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetThirdPartyJobDetailsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getThirdPartyJobDetailsSignal(output);
        Q_EMIT getThirdPartyJobDetailsSignalFull(worker, output);
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

        Q_EMIT getThirdPartyJobDetailsSignalE(output, error_type, error_str);
        Q_EMIT getThirdPartyJobDetailsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getThirdPartyJobDetailsSignalError(output, error_type, error_str);
        Q_EMIT getThirdPartyJobDetailsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listActionExecutions(const QString &x_amz_target, const OAIListActionExecutionsInput &oai_list_action_executions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listActionExecutions"][_serverIndices.value("listActionExecutions")].URL()+"/#X-Amz-Target=CodePipeline_20150709.ListActionExecutions");
    
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

        
        QByteArray output = oai_list_action_executions_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listActionExecutionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listActionExecutionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListActionExecutionsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listActionExecutionsSignal(output);
        Q_EMIT listActionExecutionsSignalFull(worker, output);
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

        Q_EMIT listActionExecutionsSignalE(output, error_type, error_str);
        Q_EMIT listActionExecutionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listActionExecutionsSignalError(output, error_type, error_str);
        Q_EMIT listActionExecutionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listActionTypes(const QString &x_amz_target, const OAIListActionTypesInput &oai_list_action_types_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listActionTypes"][_serverIndices.value("listActionTypes")].URL()+"/#X-Amz-Target=CodePipeline_20150709.ListActionTypes");
    
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

        
        QByteArray output = oai_list_action_types_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listActionTypesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listActionTypesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListActionTypesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listActionTypesSignal(output);
        Q_EMIT listActionTypesSignalFull(worker, output);
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

        Q_EMIT listActionTypesSignalE(output, error_type, error_str);
        Q_EMIT listActionTypesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listActionTypesSignalError(output, error_type, error_str);
        Q_EMIT listActionTypesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPipelineExecutions(const QString &x_amz_target, const OAIListPipelineExecutionsInput &oai_list_pipeline_executions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listPipelineExecutions"][_serverIndices.value("listPipelineExecutions")].URL()+"/#X-Amz-Target=CodePipeline_20150709.ListPipelineExecutions");
    
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

        
        QByteArray output = oai_list_pipeline_executions_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPipelineExecutionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPipelineExecutionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPipelineExecutionsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPipelineExecutionsSignal(output);
        Q_EMIT listPipelineExecutionsSignalFull(worker, output);
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

        Q_EMIT listPipelineExecutionsSignalE(output, error_type, error_str);
        Q_EMIT listPipelineExecutionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPipelineExecutionsSignalError(output, error_type, error_str);
        Q_EMIT listPipelineExecutionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPipelines(const QString &x_amz_target, const OAIListPipelinesInput &oai_list_pipelines_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listPipelines"][_serverIndices.value("listPipelines")].URL()+"/#X-Amz-Target=CodePipeline_20150709.ListPipelines");
    
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

        
        QByteArray output = oai_list_pipelines_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPipelinesCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPipelinesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPipelinesOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPipelinesSignal(output);
        Q_EMIT listPipelinesSignalFull(worker, output);
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

        Q_EMIT listPipelinesSignalE(output, error_type, error_str);
        Q_EMIT listPipelinesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPipelinesSignalError(output, error_type, error_str);
        Q_EMIT listPipelinesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listTagsForResource(const QString &x_amz_target, const OAIListTagsForResourceInput &oai_list_tags_for_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listTagsForResource"][_serverIndices.value("listTagsForResource")].URL()+"/#X-Amz-Target=CodePipeline_20150709.ListTagsForResource");
    
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

void OAIDefaultApi::listWebhooks(const QString &x_amz_target, const OAIListWebhooksInput &oai_list_webhooks_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listWebhooks"][_serverIndices.value("listWebhooks")].URL()+"/#X-Amz-Target=CodePipeline_20150709.ListWebhooks");
    
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
        queryDelimiter = getParamStyleDelimiter(queryStyle, "MaxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("MaxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "NextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("NextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_webhooks_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listWebhooksCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listWebhooksCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListWebhooksOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listWebhooksSignal(output);
        Q_EMIT listWebhooksSignalFull(worker, output);
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

        Q_EMIT listWebhooksSignalE(output, error_type, error_str);
        Q_EMIT listWebhooksSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listWebhooksSignalError(output, error_type, error_str);
        Q_EMIT listWebhooksSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::pollForJobs(const QString &x_amz_target, const OAIPollForJobsInput &oai_poll_for_jobs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["pollForJobs"][_serverIndices.value("pollForJobs")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PollForJobs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_poll_for_jobs_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::pollForJobsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::pollForJobsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPollForJobsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT pollForJobsSignal(output);
        Q_EMIT pollForJobsSignalFull(worker, output);
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

        Q_EMIT pollForJobsSignalE(output, error_type, error_str);
        Q_EMIT pollForJobsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT pollForJobsSignalError(output, error_type, error_str);
        Q_EMIT pollForJobsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::pollForThirdPartyJobs(const QString &x_amz_target, const OAIPollForThirdPartyJobsInput &oai_poll_for_third_party_jobs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["pollForThirdPartyJobs"][_serverIndices.value("pollForThirdPartyJobs")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PollForThirdPartyJobs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_poll_for_third_party_jobs_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::pollForThirdPartyJobsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::pollForThirdPartyJobsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPollForThirdPartyJobsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT pollForThirdPartyJobsSignal(output);
        Q_EMIT pollForThirdPartyJobsSignalFull(worker, output);
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

        Q_EMIT pollForThirdPartyJobsSignalE(output, error_type, error_str);
        Q_EMIT pollForThirdPartyJobsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT pollForThirdPartyJobsSignalError(output, error_type, error_str);
        Q_EMIT pollForThirdPartyJobsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putActionRevision(const QString &x_amz_target, const OAIPutActionRevisionInput &oai_put_action_revision_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putActionRevision"][_serverIndices.value("putActionRevision")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutActionRevision");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_action_revision_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putActionRevisionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putActionRevisionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPutActionRevisionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putActionRevisionSignal(output);
        Q_EMIT putActionRevisionSignalFull(worker, output);
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

        Q_EMIT putActionRevisionSignalE(output, error_type, error_str);
        Q_EMIT putActionRevisionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putActionRevisionSignalError(output, error_type, error_str);
        Q_EMIT putActionRevisionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putApprovalResult(const QString &x_amz_target, const OAIPutApprovalResultInput &oai_put_approval_result_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putApprovalResult"][_serverIndices.value("putApprovalResult")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutApprovalResult");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_approval_result_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putApprovalResultCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putApprovalResultCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPutApprovalResultOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putApprovalResultSignal(output);
        Q_EMIT putApprovalResultSignalFull(worker, output);
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

        Q_EMIT putApprovalResultSignalE(output, error_type, error_str);
        Q_EMIT putApprovalResultSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putApprovalResultSignalError(output, error_type, error_str);
        Q_EMIT putApprovalResultSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putJobFailureResult(const QString &x_amz_target, const OAIPutJobFailureResultInput &oai_put_job_failure_result_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putJobFailureResult"][_serverIndices.value("putJobFailureResult")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutJobFailureResult");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_job_failure_result_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putJobFailureResultCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putJobFailureResultCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putJobFailureResultSignal();
        Q_EMIT putJobFailureResultSignalFull(worker);
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

        Q_EMIT putJobFailureResultSignalE(error_type, error_str);
        Q_EMIT putJobFailureResultSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putJobFailureResultSignalError(error_type, error_str);
        Q_EMIT putJobFailureResultSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putJobSuccessResult(const QString &x_amz_target, const OAIPutJobSuccessResultInput &oai_put_job_success_result_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putJobSuccessResult"][_serverIndices.value("putJobSuccessResult")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutJobSuccessResult");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_job_success_result_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putJobSuccessResultCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putJobSuccessResultCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putJobSuccessResultSignal();
        Q_EMIT putJobSuccessResultSignalFull(worker);
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

        Q_EMIT putJobSuccessResultSignalE(error_type, error_str);
        Q_EMIT putJobSuccessResultSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putJobSuccessResultSignalError(error_type, error_str);
        Q_EMIT putJobSuccessResultSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putThirdPartyJobFailureResult(const QString &x_amz_target, const OAIPutThirdPartyJobFailureResultInput &oai_put_third_party_job_failure_result_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putThirdPartyJobFailureResult"][_serverIndices.value("putThirdPartyJobFailureResult")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutThirdPartyJobFailureResult");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_third_party_job_failure_result_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putThirdPartyJobFailureResultCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putThirdPartyJobFailureResultCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putThirdPartyJobFailureResultSignal();
        Q_EMIT putThirdPartyJobFailureResultSignalFull(worker);
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

        Q_EMIT putThirdPartyJobFailureResultSignalE(error_type, error_str);
        Q_EMIT putThirdPartyJobFailureResultSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putThirdPartyJobFailureResultSignalError(error_type, error_str);
        Q_EMIT putThirdPartyJobFailureResultSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putThirdPartyJobSuccessResult(const QString &x_amz_target, const OAIPutThirdPartyJobSuccessResultInput &oai_put_third_party_job_success_result_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putThirdPartyJobSuccessResult"][_serverIndices.value("putThirdPartyJobSuccessResult")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutThirdPartyJobSuccessResult");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_third_party_job_success_result_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putThirdPartyJobSuccessResultCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putThirdPartyJobSuccessResultCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putThirdPartyJobSuccessResultSignal();
        Q_EMIT putThirdPartyJobSuccessResultSignalFull(worker);
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

        Q_EMIT putThirdPartyJobSuccessResultSignalE(error_type, error_str);
        Q_EMIT putThirdPartyJobSuccessResultSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putThirdPartyJobSuccessResultSignalError(error_type, error_str);
        Q_EMIT putThirdPartyJobSuccessResultSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putWebhook(const QString &x_amz_target, const OAIPutWebhookInput &oai_put_webhook_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putWebhook"][_serverIndices.value("putWebhook")].URL()+"/#X-Amz-Target=CodePipeline_20150709.PutWebhook");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_webhook_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putWebhookCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putWebhookCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPutWebhookOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putWebhookSignal(output);
        Q_EMIT putWebhookSignalFull(worker, output);
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

        Q_EMIT putWebhookSignalE(output, error_type, error_str);
        Q_EMIT putWebhookSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putWebhookSignalError(output, error_type, error_str);
        Q_EMIT putWebhookSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::registerWebhookWithThirdParty(const QString &x_amz_target, const OAIRegisterWebhookWithThirdPartyInput &oai_register_webhook_with_third_party_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["registerWebhookWithThirdParty"][_serverIndices.value("registerWebhookWithThirdParty")].URL()+"/#X-Amz-Target=CodePipeline_20150709.RegisterWebhookWithThirdParty");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_register_webhook_with_third_party_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::registerWebhookWithThirdPartyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::registerWebhookWithThirdPartyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT registerWebhookWithThirdPartySignal(output);
        Q_EMIT registerWebhookWithThirdPartySignalFull(worker, output);
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

        Q_EMIT registerWebhookWithThirdPartySignalE(output, error_type, error_str);
        Q_EMIT registerWebhookWithThirdPartySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT registerWebhookWithThirdPartySignalError(output, error_type, error_str);
        Q_EMIT registerWebhookWithThirdPartySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::retryStageExecution(const QString &x_amz_target, const OAIRetryStageExecutionInput &oai_retry_stage_execution_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["retryStageExecution"][_serverIndices.value("retryStageExecution")].URL()+"/#X-Amz-Target=CodePipeline_20150709.RetryStageExecution");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_retry_stage_execution_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::retryStageExecutionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::retryStageExecutionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIRetryStageExecutionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT retryStageExecutionSignal(output);
        Q_EMIT retryStageExecutionSignalFull(worker, output);
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

        Q_EMIT retryStageExecutionSignalE(output, error_type, error_str);
        Q_EMIT retryStageExecutionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT retryStageExecutionSignalError(output, error_type, error_str);
        Q_EMIT retryStageExecutionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::startPipelineExecution(const QString &x_amz_target, const OAIStartPipelineExecutionInput &oai_start_pipeline_execution_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["startPipelineExecution"][_serverIndices.value("startPipelineExecution")].URL()+"/#X-Amz-Target=CodePipeline_20150709.StartPipelineExecution");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_start_pipeline_execution_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::startPipelineExecutionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::startPipelineExecutionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIStartPipelineExecutionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT startPipelineExecutionSignal(output);
        Q_EMIT startPipelineExecutionSignalFull(worker, output);
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

        Q_EMIT startPipelineExecutionSignalE(output, error_type, error_str);
        Q_EMIT startPipelineExecutionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT startPipelineExecutionSignalError(output, error_type, error_str);
        Q_EMIT startPipelineExecutionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::stopPipelineExecution(const QString &x_amz_target, const OAIStopPipelineExecutionInput &oai_stop_pipeline_execution_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["stopPipelineExecution"][_serverIndices.value("stopPipelineExecution")].URL()+"/#X-Amz-Target=CodePipeline_20150709.StopPipelineExecution");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_stop_pipeline_execution_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::stopPipelineExecutionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::stopPipelineExecutionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIStopPipelineExecutionOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT stopPipelineExecutionSignal(output);
        Q_EMIT stopPipelineExecutionSignalFull(worker, output);
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

        Q_EMIT stopPipelineExecutionSignalE(output, error_type, error_str);
        Q_EMIT stopPipelineExecutionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT stopPipelineExecutionSignalError(output, error_type, error_str);
        Q_EMIT stopPipelineExecutionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tagResource(const QString &x_amz_target, const OAITagResourceInput &oai_tag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["tagResource"][_serverIndices.value("tagResource")].URL()+"/#X-Amz-Target=CodePipeline_20150709.TagResource");
    
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
    QString fullPath = QString(_serverConfigs["untagResource"][_serverIndices.value("untagResource")].URL()+"/#X-Amz-Target=CodePipeline_20150709.UntagResource");
    
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

void OAIDefaultApi::updateActionType(const QString &x_amz_target, const OAIUpdateActionTypeInput &oai_update_action_type_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateActionType"][_serverIndices.value("updateActionType")].URL()+"/#X-Amz-Target=CodePipeline_20150709.UpdateActionType");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_action_type_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateActionTypeCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateActionTypeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateActionTypeSignal();
        Q_EMIT updateActionTypeSignalFull(worker);
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

        Q_EMIT updateActionTypeSignalE(error_type, error_str);
        Q_EMIT updateActionTypeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateActionTypeSignalError(error_type, error_str);
        Q_EMIT updateActionTypeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updatePipeline(const QString &x_amz_target, const OAIUpdatePipelineInput &oai_update_pipeline_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updatePipeline"][_serverIndices.value("updatePipeline")].URL()+"/#X-Amz-Target=CodePipeline_20150709.UpdatePipeline");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_pipeline_input.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updatePipelineCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updatePipelineCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdatePipelineOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updatePipelineSignal(output);
        Q_EMIT updatePipelineSignalFull(worker, output);
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

        Q_EMIT updatePipelineSignalE(output, error_type, error_str);
        Q_EMIT updatePipelineSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updatePipelineSignalError(output, error_type, error_str);
        Q_EMIT updatePipelineSignalErrorFull(worker, error_type, error_str);
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
