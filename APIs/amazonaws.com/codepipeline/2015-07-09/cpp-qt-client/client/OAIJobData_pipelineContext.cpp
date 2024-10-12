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

#include "OAIJobData_pipelineContext.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJobData_pipelineContext::OAIJobData_pipelineContext(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJobData_pipelineContext::OAIJobData_pipelineContext() {
    this->initializeModel();
}

OAIJobData_pipelineContext::~OAIJobData_pipelineContext() {}

void OAIJobData_pipelineContext::initializeModel() {

    m_pipeline_name_isSet = false;
    m_pipeline_name_isValid = false;

    m_stage_isSet = false;
    m_stage_isValid = false;

    m_action_isSet = false;
    m_action_isValid = false;

    m_pipeline_arn_isSet = false;
    m_pipeline_arn_isValid = false;

    m_pipeline_execution_id_isSet = false;
    m_pipeline_execution_id_isValid = false;
}

void OAIJobData_pipelineContext::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJobData_pipelineContext::fromJsonObject(QJsonObject json) {

    m_pipeline_name_isValid = ::OpenAPI::fromJsonValue(m_pipeline_name, json[QString("pipelineName")]);
    m_pipeline_name_isSet = !json[QString("pipelineName")].isNull() && m_pipeline_name_isValid;

    m_stage_isValid = ::OpenAPI::fromJsonValue(m_stage, json[QString("stage")]);
    m_stage_isSet = !json[QString("stage")].isNull() && m_stage_isValid;

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_pipeline_arn_isValid = ::OpenAPI::fromJsonValue(m_pipeline_arn, json[QString("pipelineArn")]);
    m_pipeline_arn_isSet = !json[QString("pipelineArn")].isNull() && m_pipeline_arn_isValid;

    m_pipeline_execution_id_isValid = ::OpenAPI::fromJsonValue(m_pipeline_execution_id, json[QString("pipelineExecutionId")]);
    m_pipeline_execution_id_isSet = !json[QString("pipelineExecutionId")].isNull() && m_pipeline_execution_id_isValid;
}

QString OAIJobData_pipelineContext::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJobData_pipelineContext::asJsonObject() const {
    QJsonObject obj;
    if (m_pipeline_name_isSet) {
        obj.insert(QString("pipelineName"), ::OpenAPI::toJsonValue(m_pipeline_name));
    }
    if (m_stage.isSet()) {
        obj.insert(QString("stage"), ::OpenAPI::toJsonValue(m_stage));
    }
    if (m_action.isSet()) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_pipeline_arn_isSet) {
        obj.insert(QString("pipelineArn"), ::OpenAPI::toJsonValue(m_pipeline_arn));
    }
    if (m_pipeline_execution_id_isSet) {
        obj.insert(QString("pipelineExecutionId"), ::OpenAPI::toJsonValue(m_pipeline_execution_id));
    }
    return obj;
}

QString OAIJobData_pipelineContext::getPipelineName() const {
    return m_pipeline_name;
}
void OAIJobData_pipelineContext::setPipelineName(const QString &pipeline_name) {
    m_pipeline_name = pipeline_name;
    m_pipeline_name_isSet = true;
}

bool OAIJobData_pipelineContext::is_pipeline_name_Set() const{
    return m_pipeline_name_isSet;
}

bool OAIJobData_pipelineContext::is_pipeline_name_Valid() const{
    return m_pipeline_name_isValid;
}

OAIPipelineContext_stage OAIJobData_pipelineContext::getStage() const {
    return m_stage;
}
void OAIJobData_pipelineContext::setStage(const OAIPipelineContext_stage &stage) {
    m_stage = stage;
    m_stage_isSet = true;
}

bool OAIJobData_pipelineContext::is_stage_Set() const{
    return m_stage_isSet;
}

bool OAIJobData_pipelineContext::is_stage_Valid() const{
    return m_stage_isValid;
}

OAIPipelineContext_action OAIJobData_pipelineContext::getAction() const {
    return m_action;
}
void OAIJobData_pipelineContext::setAction(const OAIPipelineContext_action &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIJobData_pipelineContext::is_action_Set() const{
    return m_action_isSet;
}

bool OAIJobData_pipelineContext::is_action_Valid() const{
    return m_action_isValid;
}

QString OAIJobData_pipelineContext::getPipelineArn() const {
    return m_pipeline_arn;
}
void OAIJobData_pipelineContext::setPipelineArn(const QString &pipeline_arn) {
    m_pipeline_arn = pipeline_arn;
    m_pipeline_arn_isSet = true;
}

bool OAIJobData_pipelineContext::is_pipeline_arn_Set() const{
    return m_pipeline_arn_isSet;
}

bool OAIJobData_pipelineContext::is_pipeline_arn_Valid() const{
    return m_pipeline_arn_isValid;
}

QString OAIJobData_pipelineContext::getPipelineExecutionId() const {
    return m_pipeline_execution_id;
}
void OAIJobData_pipelineContext::setPipelineExecutionId(const QString &pipeline_execution_id) {
    m_pipeline_execution_id = pipeline_execution_id;
    m_pipeline_execution_id_isSet = true;
}

bool OAIJobData_pipelineContext::is_pipeline_execution_id_Set() const{
    return m_pipeline_execution_id_isSet;
}

bool OAIJobData_pipelineContext::is_pipeline_execution_id_Valid() const{
    return m_pipeline_execution_id_isValid;
}

bool OAIJobData_pipelineContext::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_pipeline_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stage.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_action.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pipeline_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pipeline_execution_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJobData_pipelineContext::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
