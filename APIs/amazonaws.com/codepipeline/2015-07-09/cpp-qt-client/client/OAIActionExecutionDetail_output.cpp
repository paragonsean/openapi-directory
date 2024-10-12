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

#include "OAIActionExecutionDetail_output.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActionExecutionDetail_output::OAIActionExecutionDetail_output(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActionExecutionDetail_output::OAIActionExecutionDetail_output() {
    this->initializeModel();
}

OAIActionExecutionDetail_output::~OAIActionExecutionDetail_output() {}

void OAIActionExecutionDetail_output::initializeModel() {

    m_output_artifacts_isSet = false;
    m_output_artifacts_isValid = false;

    m_execution_result_isSet = false;
    m_execution_result_isValid = false;

    m_output_variables_isSet = false;
    m_output_variables_isValid = false;
}

void OAIActionExecutionDetail_output::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActionExecutionDetail_output::fromJsonObject(QJsonObject json) {

    m_output_artifacts_isValid = ::OpenAPI::fromJsonValue(m_output_artifacts, json[QString("outputArtifacts")]);
    m_output_artifacts_isSet = !json[QString("outputArtifacts")].isNull() && m_output_artifacts_isValid;

    m_execution_result_isValid = ::OpenAPI::fromJsonValue(m_execution_result, json[QString("executionResult")]);
    m_execution_result_isSet = !json[QString("executionResult")].isNull() && m_execution_result_isValid;

    m_output_variables_isValid = ::OpenAPI::fromJsonValue(m_output_variables, json[QString("outputVariables")]);
    m_output_variables_isSet = !json[QString("outputVariables")].isNull() && m_output_variables_isValid;
}

QString OAIActionExecutionDetail_output::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActionExecutionDetail_output::asJsonObject() const {
    QJsonObject obj;
    if (m_output_artifacts.isSet()) {
        obj.insert(QString("outputArtifacts"), ::OpenAPI::toJsonValue(m_output_artifacts));
    }
    if (m_execution_result.isSet()) {
        obj.insert(QString("executionResult"), ::OpenAPI::toJsonValue(m_execution_result));
    }
    if (m_output_variables.isSet()) {
        obj.insert(QString("outputVariables"), ::OpenAPI::toJsonValue(m_output_variables));
    }
    return obj;
}

QList OAIActionExecutionDetail_output::getOutputArtifacts() const {
    return m_output_artifacts;
}
void OAIActionExecutionDetail_output::setOutputArtifacts(const QList &output_artifacts) {
    m_output_artifacts = output_artifacts;
    m_output_artifacts_isSet = true;
}

bool OAIActionExecutionDetail_output::is_output_artifacts_Set() const{
    return m_output_artifacts_isSet;
}

bool OAIActionExecutionDetail_output::is_output_artifacts_Valid() const{
    return m_output_artifacts_isValid;
}

OAIActionExecutionOutput_executionResult OAIActionExecutionDetail_output::getExecutionResult() const {
    return m_execution_result;
}
void OAIActionExecutionDetail_output::setExecutionResult(const OAIActionExecutionOutput_executionResult &execution_result) {
    m_execution_result = execution_result;
    m_execution_result_isSet = true;
}

bool OAIActionExecutionDetail_output::is_execution_result_Set() const{
    return m_execution_result_isSet;
}

bool OAIActionExecutionDetail_output::is_execution_result_Valid() const{
    return m_execution_result_isValid;
}

QMap OAIActionExecutionDetail_output::getOutputVariables() const {
    return m_output_variables;
}
void OAIActionExecutionDetail_output::setOutputVariables(const QMap &output_variables) {
    m_output_variables = output_variables;
    m_output_variables_isSet = true;
}

bool OAIActionExecutionDetail_output::is_output_variables_Set() const{
    return m_output_variables_isSet;
}

bool OAIActionExecutionDetail_output::is_output_variables_Valid() const{
    return m_output_variables_isValid;
}

bool OAIActionExecutionDetail_output::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_output_artifacts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_result.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_variables.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActionExecutionDetail_output::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
