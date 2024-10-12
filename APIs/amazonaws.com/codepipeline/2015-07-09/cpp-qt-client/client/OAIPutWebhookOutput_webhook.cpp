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

#include "OAIPutWebhookOutput_webhook.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPutWebhookOutput_webhook::OAIPutWebhookOutput_webhook(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPutWebhookOutput_webhook::OAIPutWebhookOutput_webhook() {
    this->initializeModel();
}

OAIPutWebhookOutput_webhook::~OAIPutWebhookOutput_webhook() {}

void OAIPutWebhookOutput_webhook::initializeModel() {

    m_definition_isSet = false;
    m_definition_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_error_message_isSet = false;
    m_error_message_isValid = false;

    m_error_code_isSet = false;
    m_error_code_isValid = false;

    m_last_triggered_isSet = false;
    m_last_triggered_isValid = false;

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAIPutWebhookOutput_webhook::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPutWebhookOutput_webhook::fromJsonObject(QJsonObject json) {

    m_definition_isValid = ::OpenAPI::fromJsonValue(m_definition, json[QString("definition")]);
    m_definition_isSet = !json[QString("definition")].isNull() && m_definition_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_error_message_isValid = ::OpenAPI::fromJsonValue(m_error_message, json[QString("errorMessage")]);
    m_error_message_isSet = !json[QString("errorMessage")].isNull() && m_error_message_isValid;

    m_error_code_isValid = ::OpenAPI::fromJsonValue(m_error_code, json[QString("errorCode")]);
    m_error_code_isSet = !json[QString("errorCode")].isNull() && m_error_code_isValid;

    m_last_triggered_isValid = ::OpenAPI::fromJsonValue(m_last_triggered, json[QString("lastTriggered")]);
    m_last_triggered_isSet = !json[QString("lastTriggered")].isNull() && m_last_triggered_isValid;

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAIPutWebhookOutput_webhook::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPutWebhookOutput_webhook::asJsonObject() const {
    QJsonObject obj;
    if (m_definition.isSet()) {
        obj.insert(QString("definition"), ::OpenAPI::toJsonValue(m_definition));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_error_message_isSet) {
        obj.insert(QString("errorMessage"), ::OpenAPI::toJsonValue(m_error_message));
    }
    if (m_error_code_isSet) {
        obj.insert(QString("errorCode"), ::OpenAPI::toJsonValue(m_error_code));
    }
    if (m_last_triggered_isSet) {
        obj.insert(QString("lastTriggered"), ::OpenAPI::toJsonValue(m_last_triggered));
    }
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_tags.isSet()) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

OAIListWebhookItem_definition OAIPutWebhookOutput_webhook::getDefinition() const {
    return m_definition;
}
void OAIPutWebhookOutput_webhook::setDefinition(const OAIListWebhookItem_definition &definition) {
    m_definition = definition;
    m_definition_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_definition_Set() const{
    return m_definition_isSet;
}

bool OAIPutWebhookOutput_webhook::is_definition_Valid() const{
    return m_definition_isValid;
}

QString OAIPutWebhookOutput_webhook::getUrl() const {
    return m_url;
}
void OAIPutWebhookOutput_webhook::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_url_Set() const{
    return m_url_isSet;
}

bool OAIPutWebhookOutput_webhook::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIPutWebhookOutput_webhook::getErrorMessage() const {
    return m_error_message;
}
void OAIPutWebhookOutput_webhook::setErrorMessage(const QString &error_message) {
    m_error_message = error_message;
    m_error_message_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_error_message_Set() const{
    return m_error_message_isSet;
}

bool OAIPutWebhookOutput_webhook::is_error_message_Valid() const{
    return m_error_message_isValid;
}

QString OAIPutWebhookOutput_webhook::getErrorCode() const {
    return m_error_code;
}
void OAIPutWebhookOutput_webhook::setErrorCode(const QString &error_code) {
    m_error_code = error_code;
    m_error_code_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_error_code_Set() const{
    return m_error_code_isSet;
}

bool OAIPutWebhookOutput_webhook::is_error_code_Valid() const{
    return m_error_code_isValid;
}

QDateTime OAIPutWebhookOutput_webhook::getLastTriggered() const {
    return m_last_triggered;
}
void OAIPutWebhookOutput_webhook::setLastTriggered(const QDateTime &last_triggered) {
    m_last_triggered = last_triggered;
    m_last_triggered_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_last_triggered_Set() const{
    return m_last_triggered_isSet;
}

bool OAIPutWebhookOutput_webhook::is_last_triggered_Valid() const{
    return m_last_triggered_isValid;
}

QString OAIPutWebhookOutput_webhook::getArn() const {
    return m_arn;
}
void OAIPutWebhookOutput_webhook::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAIPutWebhookOutput_webhook::is_arn_Valid() const{
    return m_arn_isValid;
}

QList OAIPutWebhookOutput_webhook::getTags() const {
    return m_tags;
}
void OAIPutWebhookOutput_webhook::setTags(const QList &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIPutWebhookOutput_webhook::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIPutWebhookOutput_webhook::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAIPutWebhookOutput_webhook::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_definition.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_triggered_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPutWebhookOutput_webhook::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_definition_isValid && m_url_isValid && true;
}

} // namespace OpenAPI
