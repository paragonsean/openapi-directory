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

#include "OAIGetActionTypeOutput_actionType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetActionTypeOutput_actionType::OAIGetActionTypeOutput_actionType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetActionTypeOutput_actionType::OAIGetActionTypeOutput_actionType() {
    this->initializeModel();
}

OAIGetActionTypeOutput_actionType::~OAIGetActionTypeOutput_actionType() {}

void OAIGetActionTypeOutput_actionType::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_executor_isSet = false;
    m_executor_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_input_artifact_details_isSet = false;
    m_input_artifact_details_isValid = false;

    m_output_artifact_details_isSet = false;
    m_output_artifact_details_isValid = false;

    m_permissions_isSet = false;
    m_permissions_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_urls_isSet = false;
    m_urls_isValid = false;
}

void OAIGetActionTypeOutput_actionType::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetActionTypeOutput_actionType::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_executor_isValid = ::OpenAPI::fromJsonValue(m_executor, json[QString("executor")]);
    m_executor_isSet = !json[QString("executor")].isNull() && m_executor_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_input_artifact_details_isValid = ::OpenAPI::fromJsonValue(m_input_artifact_details, json[QString("inputArtifactDetails")]);
    m_input_artifact_details_isSet = !json[QString("inputArtifactDetails")].isNull() && m_input_artifact_details_isValid;

    m_output_artifact_details_isValid = ::OpenAPI::fromJsonValue(m_output_artifact_details, json[QString("outputArtifactDetails")]);
    m_output_artifact_details_isSet = !json[QString("outputArtifactDetails")].isNull() && m_output_artifact_details_isValid;

    m_permissions_isValid = ::OpenAPI::fromJsonValue(m_permissions, json[QString("permissions")]);
    m_permissions_isSet = !json[QString("permissions")].isNull() && m_permissions_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_urls_isValid = ::OpenAPI::fromJsonValue(m_urls, json[QString("urls")]);
    m_urls_isSet = !json[QString("urls")].isNull() && m_urls_isValid;
}

QString OAIGetActionTypeOutput_actionType::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetActionTypeOutput_actionType::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_executor.isSet()) {
        obj.insert(QString("executor"), ::OpenAPI::toJsonValue(m_executor));
    }
    if (m_id.isSet()) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_input_artifact_details.isSet()) {
        obj.insert(QString("inputArtifactDetails"), ::OpenAPI::toJsonValue(m_input_artifact_details));
    }
    if (m_output_artifact_details.isSet()) {
        obj.insert(QString("outputArtifactDetails"), ::OpenAPI::toJsonValue(m_output_artifact_details));
    }
    if (m_permissions.isSet()) {
        obj.insert(QString("permissions"), ::OpenAPI::toJsonValue(m_permissions));
    }
    if (m_properties_isSet) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_urls.isSet()) {
        obj.insert(QString("urls"), ::OpenAPI::toJsonValue(m_urls));
    }
    return obj;
}

QString OAIGetActionTypeOutput_actionType::getDescription() const {
    return m_description;
}
void OAIGetActionTypeOutput_actionType::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_description_Set() const{
    return m_description_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_description_Valid() const{
    return m_description_isValid;
}

OAIActionTypeDeclaration_executor OAIGetActionTypeOutput_actionType::getExecutor() const {
    return m_executor;
}
void OAIGetActionTypeOutput_actionType::setExecutor(const OAIActionTypeDeclaration_executor &executor) {
    m_executor = executor;
    m_executor_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_executor_Set() const{
    return m_executor_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_executor_Valid() const{
    return m_executor_isValid;
}

OAIActionTypeDeclaration_id OAIGetActionTypeOutput_actionType::getId() const {
    return m_id;
}
void OAIGetActionTypeOutput_actionType::setId(const OAIActionTypeDeclaration_id &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_id_Valid() const{
    return m_id_isValid;
}

OAIActionTypeDeclaration_inputArtifactDetails OAIGetActionTypeOutput_actionType::getInputArtifactDetails() const {
    return m_input_artifact_details;
}
void OAIGetActionTypeOutput_actionType::setInputArtifactDetails(const OAIActionTypeDeclaration_inputArtifactDetails &input_artifact_details) {
    m_input_artifact_details = input_artifact_details;
    m_input_artifact_details_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_input_artifact_details_Set() const{
    return m_input_artifact_details_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_input_artifact_details_Valid() const{
    return m_input_artifact_details_isValid;
}

OAIActionTypeDeclaration_outputArtifactDetails OAIGetActionTypeOutput_actionType::getOutputArtifactDetails() const {
    return m_output_artifact_details;
}
void OAIGetActionTypeOutput_actionType::setOutputArtifactDetails(const OAIActionTypeDeclaration_outputArtifactDetails &output_artifact_details) {
    m_output_artifact_details = output_artifact_details;
    m_output_artifact_details_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_output_artifact_details_Set() const{
    return m_output_artifact_details_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_output_artifact_details_Valid() const{
    return m_output_artifact_details_isValid;
}

OAIActionTypeDeclaration_permissions OAIGetActionTypeOutput_actionType::getPermissions() const {
    return m_permissions;
}
void OAIGetActionTypeOutput_actionType::setPermissions(const OAIActionTypeDeclaration_permissions &permissions) {
    m_permissions = permissions;
    m_permissions_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_permissions_Set() const{
    return m_permissions_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_permissions_Valid() const{
    return m_permissions_isValid;
}

QJsonValue OAIGetActionTypeOutput_actionType::getProperties() const {
    return m_properties;
}
void OAIGetActionTypeOutput_actionType::setProperties(const QJsonValue &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_properties_Valid() const{
    return m_properties_isValid;
}

OAIActionTypeDeclaration_urls OAIGetActionTypeOutput_actionType::getUrls() const {
    return m_urls;
}
void OAIGetActionTypeOutput_actionType::setUrls(const OAIActionTypeDeclaration_urls &urls) {
    m_urls = urls;
    m_urls_isSet = true;
}

bool OAIGetActionTypeOutput_actionType::is_urls_Set() const{
    return m_urls_isSet;
}

bool OAIGetActionTypeOutput_actionType::is_urls_Valid() const{
    return m_urls_isValid;
}

bool OAIGetActionTypeOutput_actionType::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_executor.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_artifact_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_artifact_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_permissions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_urls.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetActionTypeOutput_actionType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_executor_isValid && m_id_isValid && m_input_artifact_details_isValid && m_output_artifact_details_isValid && true;
}

} // namespace OpenAPI
