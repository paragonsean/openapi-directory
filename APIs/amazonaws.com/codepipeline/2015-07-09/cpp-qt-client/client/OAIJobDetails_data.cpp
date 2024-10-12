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

#include "OAIJobDetails_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJobDetails_data::OAIJobDetails_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJobDetails_data::OAIJobDetails_data() {
    this->initializeModel();
}

OAIJobDetails_data::~OAIJobDetails_data() {}

void OAIJobDetails_data::initializeModel() {

    m_action_type_id_isSet = false;
    m_action_type_id_isValid = false;

    m_action_configuration_isSet = false;
    m_action_configuration_isValid = false;

    m_pipeline_context_isSet = false;
    m_pipeline_context_isValid = false;

    m_input_artifacts_isSet = false;
    m_input_artifacts_isValid = false;

    m_output_artifacts_isSet = false;
    m_output_artifacts_isValid = false;

    m_artifact_credentials_isSet = false;
    m_artifact_credentials_isValid = false;

    m_continuation_token_isSet = false;
    m_continuation_token_isValid = false;

    m_encryption_key_isSet = false;
    m_encryption_key_isValid = false;
}

void OAIJobDetails_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJobDetails_data::fromJsonObject(QJsonObject json) {

    m_action_type_id_isValid = ::OpenAPI::fromJsonValue(m_action_type_id, json[QString("actionTypeId")]);
    m_action_type_id_isSet = !json[QString("actionTypeId")].isNull() && m_action_type_id_isValid;

    m_action_configuration_isValid = ::OpenAPI::fromJsonValue(m_action_configuration, json[QString("actionConfiguration")]);
    m_action_configuration_isSet = !json[QString("actionConfiguration")].isNull() && m_action_configuration_isValid;

    m_pipeline_context_isValid = ::OpenAPI::fromJsonValue(m_pipeline_context, json[QString("pipelineContext")]);
    m_pipeline_context_isSet = !json[QString("pipelineContext")].isNull() && m_pipeline_context_isValid;

    m_input_artifacts_isValid = ::OpenAPI::fromJsonValue(m_input_artifacts, json[QString("inputArtifacts")]);
    m_input_artifacts_isSet = !json[QString("inputArtifacts")].isNull() && m_input_artifacts_isValid;

    m_output_artifacts_isValid = ::OpenAPI::fromJsonValue(m_output_artifacts, json[QString("outputArtifacts")]);
    m_output_artifacts_isSet = !json[QString("outputArtifacts")].isNull() && m_output_artifacts_isValid;

    m_artifact_credentials_isValid = ::OpenAPI::fromJsonValue(m_artifact_credentials, json[QString("artifactCredentials")]);
    m_artifact_credentials_isSet = !json[QString("artifactCredentials")].isNull() && m_artifact_credentials_isValid;

    m_continuation_token_isValid = ::OpenAPI::fromJsonValue(m_continuation_token, json[QString("continuationToken")]);
    m_continuation_token_isSet = !json[QString("continuationToken")].isNull() && m_continuation_token_isValid;

    m_encryption_key_isValid = ::OpenAPI::fromJsonValue(m_encryption_key, json[QString("encryptionKey")]);
    m_encryption_key_isSet = !json[QString("encryptionKey")].isNull() && m_encryption_key_isValid;
}

QString OAIJobDetails_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJobDetails_data::asJsonObject() const {
    QJsonObject obj;
    if (m_action_type_id.isSet()) {
        obj.insert(QString("actionTypeId"), ::OpenAPI::toJsonValue(m_action_type_id));
    }
    if (m_action_configuration.isSet()) {
        obj.insert(QString("actionConfiguration"), ::OpenAPI::toJsonValue(m_action_configuration));
    }
    if (m_pipeline_context.isSet()) {
        obj.insert(QString("pipelineContext"), ::OpenAPI::toJsonValue(m_pipeline_context));
    }
    if (m_input_artifacts.isSet()) {
        obj.insert(QString("inputArtifacts"), ::OpenAPI::toJsonValue(m_input_artifacts));
    }
    if (m_output_artifacts.isSet()) {
        obj.insert(QString("outputArtifacts"), ::OpenAPI::toJsonValue(m_output_artifacts));
    }
    if (m_artifact_credentials.isSet()) {
        obj.insert(QString("artifactCredentials"), ::OpenAPI::toJsonValue(m_artifact_credentials));
    }
    if (m_continuation_token_isSet) {
        obj.insert(QString("continuationToken"), ::OpenAPI::toJsonValue(m_continuation_token));
    }
    if (m_encryption_key.isSet()) {
        obj.insert(QString("encryptionKey"), ::OpenAPI::toJsonValue(m_encryption_key));
    }
    return obj;
}

OAIPollForJobsInput_actionTypeId OAIJobDetails_data::getActionTypeId() const {
    return m_action_type_id;
}
void OAIJobDetails_data::setActionTypeId(const OAIPollForJobsInput_actionTypeId &action_type_id) {
    m_action_type_id = action_type_id;
    m_action_type_id_isSet = true;
}

bool OAIJobDetails_data::is_action_type_id_Set() const{
    return m_action_type_id_isSet;
}

bool OAIJobDetails_data::is_action_type_id_Valid() const{
    return m_action_type_id_isValid;
}

OAIJobData_actionConfiguration OAIJobDetails_data::getActionConfiguration() const {
    return m_action_configuration;
}
void OAIJobDetails_data::setActionConfiguration(const OAIJobData_actionConfiguration &action_configuration) {
    m_action_configuration = action_configuration;
    m_action_configuration_isSet = true;
}

bool OAIJobDetails_data::is_action_configuration_Set() const{
    return m_action_configuration_isSet;
}

bool OAIJobDetails_data::is_action_configuration_Valid() const{
    return m_action_configuration_isValid;
}

OAIJobData_pipelineContext OAIJobDetails_data::getPipelineContext() const {
    return m_pipeline_context;
}
void OAIJobDetails_data::setPipelineContext(const OAIJobData_pipelineContext &pipeline_context) {
    m_pipeline_context = pipeline_context;
    m_pipeline_context_isSet = true;
}

bool OAIJobDetails_data::is_pipeline_context_Set() const{
    return m_pipeline_context_isSet;
}

bool OAIJobDetails_data::is_pipeline_context_Valid() const{
    return m_pipeline_context_isValid;
}

QList OAIJobDetails_data::getInputArtifacts() const {
    return m_input_artifacts;
}
void OAIJobDetails_data::setInputArtifacts(const QList &input_artifacts) {
    m_input_artifacts = input_artifacts;
    m_input_artifacts_isSet = true;
}

bool OAIJobDetails_data::is_input_artifacts_Set() const{
    return m_input_artifacts_isSet;
}

bool OAIJobDetails_data::is_input_artifacts_Valid() const{
    return m_input_artifacts_isValid;
}

QList OAIJobDetails_data::getOutputArtifacts() const {
    return m_output_artifacts;
}
void OAIJobDetails_data::setOutputArtifacts(const QList &output_artifacts) {
    m_output_artifacts = output_artifacts;
    m_output_artifacts_isSet = true;
}

bool OAIJobDetails_data::is_output_artifacts_Set() const{
    return m_output_artifacts_isSet;
}

bool OAIJobDetails_data::is_output_artifacts_Valid() const{
    return m_output_artifacts_isValid;
}

OAIJobData_artifactCredentials OAIJobDetails_data::getArtifactCredentials() const {
    return m_artifact_credentials;
}
void OAIJobDetails_data::setArtifactCredentials(const OAIJobData_artifactCredentials &artifact_credentials) {
    m_artifact_credentials = artifact_credentials;
    m_artifact_credentials_isSet = true;
}

bool OAIJobDetails_data::is_artifact_credentials_Set() const{
    return m_artifact_credentials_isSet;
}

bool OAIJobDetails_data::is_artifact_credentials_Valid() const{
    return m_artifact_credentials_isValid;
}

QString OAIJobDetails_data::getContinuationToken() const {
    return m_continuation_token;
}
void OAIJobDetails_data::setContinuationToken(const QString &continuation_token) {
    m_continuation_token = continuation_token;
    m_continuation_token_isSet = true;
}

bool OAIJobDetails_data::is_continuation_token_Set() const{
    return m_continuation_token_isSet;
}

bool OAIJobDetails_data::is_continuation_token_Valid() const{
    return m_continuation_token_isValid;
}

OAIJobData_encryptionKey OAIJobDetails_data::getEncryptionKey() const {
    return m_encryption_key;
}
void OAIJobDetails_data::setEncryptionKey(const OAIJobData_encryptionKey &encryption_key) {
    m_encryption_key = encryption_key;
    m_encryption_key_isSet = true;
}

bool OAIJobDetails_data::is_encryption_key_Set() const{
    return m_encryption_key_isSet;
}

bool OAIJobDetails_data::is_encryption_key_Valid() const{
    return m_encryption_key_isValid;
}

bool OAIJobDetails_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_type_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_action_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pipeline_context.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_artifacts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_artifacts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_artifact_credentials.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_continuation_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_encryption_key.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJobDetails_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
