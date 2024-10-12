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

#include "OAIActionExecutionDetail.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActionExecutionDetail::OAIActionExecutionDetail(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActionExecutionDetail::OAIActionExecutionDetail() {
    this->initializeModel();
}

OAIActionExecutionDetail::~OAIActionExecutionDetail() {}

void OAIActionExecutionDetail::initializeModel() {

    m_pipeline_execution_id_isSet = false;
    m_pipeline_execution_id_isValid = false;

    m_action_execution_id_isSet = false;
    m_action_execution_id_isValid = false;

    m_pipeline_version_isSet = false;
    m_pipeline_version_isValid = false;

    m_stage_name_isSet = false;
    m_stage_name_isValid = false;

    m_action_name_isSet = false;
    m_action_name_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_last_update_time_isSet = false;
    m_last_update_time_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_input_isSet = false;
    m_input_isValid = false;

    m_output_isSet = false;
    m_output_isValid = false;
}

void OAIActionExecutionDetail::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActionExecutionDetail::fromJsonObject(QJsonObject json) {

    m_pipeline_execution_id_isValid = ::OpenAPI::fromJsonValue(m_pipeline_execution_id, json[QString("pipelineExecutionId")]);
    m_pipeline_execution_id_isSet = !json[QString("pipelineExecutionId")].isNull() && m_pipeline_execution_id_isValid;

    m_action_execution_id_isValid = ::OpenAPI::fromJsonValue(m_action_execution_id, json[QString("actionExecutionId")]);
    m_action_execution_id_isSet = !json[QString("actionExecutionId")].isNull() && m_action_execution_id_isValid;

    m_pipeline_version_isValid = ::OpenAPI::fromJsonValue(m_pipeline_version, json[QString("pipelineVersion")]);
    m_pipeline_version_isSet = !json[QString("pipelineVersion")].isNull() && m_pipeline_version_isValid;

    m_stage_name_isValid = ::OpenAPI::fromJsonValue(m_stage_name, json[QString("stageName")]);
    m_stage_name_isSet = !json[QString("stageName")].isNull() && m_stage_name_isValid;

    m_action_name_isValid = ::OpenAPI::fromJsonValue(m_action_name, json[QString("actionName")]);
    m_action_name_isSet = !json[QString("actionName")].isNull() && m_action_name_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_last_update_time_isValid = ::OpenAPI::fromJsonValue(m_last_update_time, json[QString("lastUpdateTime")]);
    m_last_update_time_isSet = !json[QString("lastUpdateTime")].isNull() && m_last_update_time_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;

    m_output_isValid = ::OpenAPI::fromJsonValue(m_output, json[QString("output")]);
    m_output_isSet = !json[QString("output")].isNull() && m_output_isValid;
}

QString OAIActionExecutionDetail::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActionExecutionDetail::asJsonObject() const {
    QJsonObject obj;
    if (m_pipeline_execution_id_isSet) {
        obj.insert(QString("pipelineExecutionId"), ::OpenAPI::toJsonValue(m_pipeline_execution_id));
    }
    if (m_action_execution_id_isSet) {
        obj.insert(QString("actionExecutionId"), ::OpenAPI::toJsonValue(m_action_execution_id));
    }
    if (m_pipeline_version_isSet) {
        obj.insert(QString("pipelineVersion"), ::OpenAPI::toJsonValue(m_pipeline_version));
    }
    if (m_stage_name_isSet) {
        obj.insert(QString("stageName"), ::OpenAPI::toJsonValue(m_stage_name));
    }
    if (m_action_name_isSet) {
        obj.insert(QString("actionName"), ::OpenAPI::toJsonValue(m_action_name));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_last_update_time_isSet) {
        obj.insert(QString("lastUpdateTime"), ::OpenAPI::toJsonValue(m_last_update_time));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_input.isSet()) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    if (m_output.isSet()) {
        obj.insert(QString("output"), ::OpenAPI::toJsonValue(m_output));
    }
    return obj;
}

QString OAIActionExecutionDetail::getPipelineExecutionId() const {
    return m_pipeline_execution_id;
}
void OAIActionExecutionDetail::setPipelineExecutionId(const QString &pipeline_execution_id) {
    m_pipeline_execution_id = pipeline_execution_id;
    m_pipeline_execution_id_isSet = true;
}

bool OAIActionExecutionDetail::is_pipeline_execution_id_Set() const{
    return m_pipeline_execution_id_isSet;
}

bool OAIActionExecutionDetail::is_pipeline_execution_id_Valid() const{
    return m_pipeline_execution_id_isValid;
}

QString OAIActionExecutionDetail::getActionExecutionId() const {
    return m_action_execution_id;
}
void OAIActionExecutionDetail::setActionExecutionId(const QString &action_execution_id) {
    m_action_execution_id = action_execution_id;
    m_action_execution_id_isSet = true;
}

bool OAIActionExecutionDetail::is_action_execution_id_Set() const{
    return m_action_execution_id_isSet;
}

bool OAIActionExecutionDetail::is_action_execution_id_Valid() const{
    return m_action_execution_id_isValid;
}

qint32 OAIActionExecutionDetail::getPipelineVersion() const {
    return m_pipeline_version;
}
void OAIActionExecutionDetail::setPipelineVersion(const qint32 &pipeline_version) {
    m_pipeline_version = pipeline_version;
    m_pipeline_version_isSet = true;
}

bool OAIActionExecutionDetail::is_pipeline_version_Set() const{
    return m_pipeline_version_isSet;
}

bool OAIActionExecutionDetail::is_pipeline_version_Valid() const{
    return m_pipeline_version_isValid;
}

QString OAIActionExecutionDetail::getStageName() const {
    return m_stage_name;
}
void OAIActionExecutionDetail::setStageName(const QString &stage_name) {
    m_stage_name = stage_name;
    m_stage_name_isSet = true;
}

bool OAIActionExecutionDetail::is_stage_name_Set() const{
    return m_stage_name_isSet;
}

bool OAIActionExecutionDetail::is_stage_name_Valid() const{
    return m_stage_name_isValid;
}

QString OAIActionExecutionDetail::getActionName() const {
    return m_action_name;
}
void OAIActionExecutionDetail::setActionName(const QString &action_name) {
    m_action_name = action_name;
    m_action_name_isSet = true;
}

bool OAIActionExecutionDetail::is_action_name_Set() const{
    return m_action_name_isSet;
}

bool OAIActionExecutionDetail::is_action_name_Valid() const{
    return m_action_name_isValid;
}

QDateTime OAIActionExecutionDetail::getStartTime() const {
    return m_start_time;
}
void OAIActionExecutionDetail::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIActionExecutionDetail::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIActionExecutionDetail::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QDateTime OAIActionExecutionDetail::getLastUpdateTime() const {
    return m_last_update_time;
}
void OAIActionExecutionDetail::setLastUpdateTime(const QDateTime &last_update_time) {
    m_last_update_time = last_update_time;
    m_last_update_time_isSet = true;
}

bool OAIActionExecutionDetail::is_last_update_time_Set() const{
    return m_last_update_time_isSet;
}

bool OAIActionExecutionDetail::is_last_update_time_Valid() const{
    return m_last_update_time_isValid;
}

OAIActionExecutionStatus OAIActionExecutionDetail::getStatus() const {
    return m_status;
}
void OAIActionExecutionDetail::setStatus(const OAIActionExecutionStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIActionExecutionDetail::is_status_Set() const{
    return m_status_isSet;
}

bool OAIActionExecutionDetail::is_status_Valid() const{
    return m_status_isValid;
}

OAIActionExecutionDetail_input OAIActionExecutionDetail::getInput() const {
    return m_input;
}
void OAIActionExecutionDetail::setInput(const OAIActionExecutionDetail_input &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIActionExecutionDetail::is_input_Set() const{
    return m_input_isSet;
}

bool OAIActionExecutionDetail::is_input_Valid() const{
    return m_input_isValid;
}

OAIActionExecutionDetail_output OAIActionExecutionDetail::getOutput() const {
    return m_output;
}
void OAIActionExecutionDetail::setOutput(const OAIActionExecutionDetail_output &output) {
    m_output = output;
    m_output_isSet = true;
}

bool OAIActionExecutionDetail::is_output_Set() const{
    return m_output_isSet;
}

bool OAIActionExecutionDetail::is_output_Valid() const{
    return m_output_isValid;
}

bool OAIActionExecutionDetail::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_pipeline_execution_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_action_execution_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pipeline_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stage_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_action_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_update_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_input.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_output.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActionExecutionDetail::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
