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

#include "OAIActionState_latestExecution.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActionState_latestExecution::OAIActionState_latestExecution(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActionState_latestExecution::OAIActionState_latestExecution() {
    this->initializeModel();
}

OAIActionState_latestExecution::~OAIActionState_latestExecution() {}

void OAIActionState_latestExecution::initializeModel() {

    m_action_execution_id_isSet = false;
    m_action_execution_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_last_status_change_isSet = false;
    m_last_status_change_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;

    m_last_updated_by_isSet = false;
    m_last_updated_by_isValid = false;

    m_external_execution_id_isSet = false;
    m_external_execution_id_isValid = false;

    m_external_execution_url_isSet = false;
    m_external_execution_url_isValid = false;

    m_percent_complete_isSet = false;
    m_percent_complete_isValid = false;

    m_error_details_isSet = false;
    m_error_details_isValid = false;
}

void OAIActionState_latestExecution::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActionState_latestExecution::fromJsonObject(QJsonObject json) {

    m_action_execution_id_isValid = ::OpenAPI::fromJsonValue(m_action_execution_id, json[QString("actionExecutionId")]);
    m_action_execution_id_isSet = !json[QString("actionExecutionId")].isNull() && m_action_execution_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_last_status_change_isValid = ::OpenAPI::fromJsonValue(m_last_status_change, json[QString("lastStatusChange")]);
    m_last_status_change_isSet = !json[QString("lastStatusChange")].isNull() && m_last_status_change_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;

    m_last_updated_by_isValid = ::OpenAPI::fromJsonValue(m_last_updated_by, json[QString("lastUpdatedBy")]);
    m_last_updated_by_isSet = !json[QString("lastUpdatedBy")].isNull() && m_last_updated_by_isValid;

    m_external_execution_id_isValid = ::OpenAPI::fromJsonValue(m_external_execution_id, json[QString("externalExecutionId")]);
    m_external_execution_id_isSet = !json[QString("externalExecutionId")].isNull() && m_external_execution_id_isValid;

    m_external_execution_url_isValid = ::OpenAPI::fromJsonValue(m_external_execution_url, json[QString("externalExecutionUrl")]);
    m_external_execution_url_isSet = !json[QString("externalExecutionUrl")].isNull() && m_external_execution_url_isValid;

    m_percent_complete_isValid = ::OpenAPI::fromJsonValue(m_percent_complete, json[QString("percentComplete")]);
    m_percent_complete_isSet = !json[QString("percentComplete")].isNull() && m_percent_complete_isValid;

    m_error_details_isValid = ::OpenAPI::fromJsonValue(m_error_details, json[QString("errorDetails")]);
    m_error_details_isSet = !json[QString("errorDetails")].isNull() && m_error_details_isValid;
}

QString OAIActionState_latestExecution::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActionState_latestExecution::asJsonObject() const {
    QJsonObject obj;
    if (m_action_execution_id_isSet) {
        obj.insert(QString("actionExecutionId"), ::OpenAPI::toJsonValue(m_action_execution_id));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_last_status_change_isSet) {
        obj.insert(QString("lastStatusChange"), ::OpenAPI::toJsonValue(m_last_status_change));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    if (m_last_updated_by_isSet) {
        obj.insert(QString("lastUpdatedBy"), ::OpenAPI::toJsonValue(m_last_updated_by));
    }
    if (m_external_execution_id_isSet) {
        obj.insert(QString("externalExecutionId"), ::OpenAPI::toJsonValue(m_external_execution_id));
    }
    if (m_external_execution_url_isSet) {
        obj.insert(QString("externalExecutionUrl"), ::OpenAPI::toJsonValue(m_external_execution_url));
    }
    if (m_percent_complete_isSet) {
        obj.insert(QString("percentComplete"), ::OpenAPI::toJsonValue(m_percent_complete));
    }
    if (m_error_details.isSet()) {
        obj.insert(QString("errorDetails"), ::OpenAPI::toJsonValue(m_error_details));
    }
    return obj;
}

QString OAIActionState_latestExecution::getActionExecutionId() const {
    return m_action_execution_id;
}
void OAIActionState_latestExecution::setActionExecutionId(const QString &action_execution_id) {
    m_action_execution_id = action_execution_id;
    m_action_execution_id_isSet = true;
}

bool OAIActionState_latestExecution::is_action_execution_id_Set() const{
    return m_action_execution_id_isSet;
}

bool OAIActionState_latestExecution::is_action_execution_id_Valid() const{
    return m_action_execution_id_isValid;
}

OAIActionExecutionStatus OAIActionState_latestExecution::getStatus() const {
    return m_status;
}
void OAIActionState_latestExecution::setStatus(const OAIActionExecutionStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIActionState_latestExecution::is_status_Set() const{
    return m_status_isSet;
}

bool OAIActionState_latestExecution::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIActionState_latestExecution::getSummary() const {
    return m_summary;
}
void OAIActionState_latestExecution::setSummary(const QString &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAIActionState_latestExecution::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAIActionState_latestExecution::is_summary_Valid() const{
    return m_summary_isValid;
}

QDateTime OAIActionState_latestExecution::getLastStatusChange() const {
    return m_last_status_change;
}
void OAIActionState_latestExecution::setLastStatusChange(const QDateTime &last_status_change) {
    m_last_status_change = last_status_change;
    m_last_status_change_isSet = true;
}

bool OAIActionState_latestExecution::is_last_status_change_Set() const{
    return m_last_status_change_isSet;
}

bool OAIActionState_latestExecution::is_last_status_change_Valid() const{
    return m_last_status_change_isValid;
}

QString OAIActionState_latestExecution::getToken() const {
    return m_token;
}
void OAIActionState_latestExecution::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIActionState_latestExecution::is_token_Set() const{
    return m_token_isSet;
}

bool OAIActionState_latestExecution::is_token_Valid() const{
    return m_token_isValid;
}

QString OAIActionState_latestExecution::getLastUpdatedBy() const {
    return m_last_updated_by;
}
void OAIActionState_latestExecution::setLastUpdatedBy(const QString &last_updated_by) {
    m_last_updated_by = last_updated_by;
    m_last_updated_by_isSet = true;
}

bool OAIActionState_latestExecution::is_last_updated_by_Set() const{
    return m_last_updated_by_isSet;
}

bool OAIActionState_latestExecution::is_last_updated_by_Valid() const{
    return m_last_updated_by_isValid;
}

QString OAIActionState_latestExecution::getExternalExecutionId() const {
    return m_external_execution_id;
}
void OAIActionState_latestExecution::setExternalExecutionId(const QString &external_execution_id) {
    m_external_execution_id = external_execution_id;
    m_external_execution_id_isSet = true;
}

bool OAIActionState_latestExecution::is_external_execution_id_Set() const{
    return m_external_execution_id_isSet;
}

bool OAIActionState_latestExecution::is_external_execution_id_Valid() const{
    return m_external_execution_id_isValid;
}

QString OAIActionState_latestExecution::getExternalExecutionUrl() const {
    return m_external_execution_url;
}
void OAIActionState_latestExecution::setExternalExecutionUrl(const QString &external_execution_url) {
    m_external_execution_url = external_execution_url;
    m_external_execution_url_isSet = true;
}

bool OAIActionState_latestExecution::is_external_execution_url_Set() const{
    return m_external_execution_url_isSet;
}

bool OAIActionState_latestExecution::is_external_execution_url_Valid() const{
    return m_external_execution_url_isValid;
}

qint32 OAIActionState_latestExecution::getPercentComplete() const {
    return m_percent_complete;
}
void OAIActionState_latestExecution::setPercentComplete(const qint32 &percent_complete) {
    m_percent_complete = percent_complete;
    m_percent_complete_isSet = true;
}

bool OAIActionState_latestExecution::is_percent_complete_Set() const{
    return m_percent_complete_isSet;
}

bool OAIActionState_latestExecution::is_percent_complete_Valid() const{
    return m_percent_complete_isValid;
}

OAIActionExecution_errorDetails OAIActionState_latestExecution::getErrorDetails() const {
    return m_error_details;
}
void OAIActionState_latestExecution::setErrorDetails(const OAIActionExecution_errorDetails &error_details) {
    m_error_details = error_details;
    m_error_details_isSet = true;
}

bool OAIActionState_latestExecution::is_error_details_Set() const{
    return m_error_details_isSet;
}

bool OAIActionState_latestExecution::is_error_details_Valid() const{
    return m_error_details_isValid;
}

bool OAIActionState_latestExecution::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_execution_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_status_change_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_updated_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_execution_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_execution_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percent_complete_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_details.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActionState_latestExecution::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
