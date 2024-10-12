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

#include "OAIActionTypeDeclaration_urls.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActionTypeDeclaration_urls::OAIActionTypeDeclaration_urls(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActionTypeDeclaration_urls::OAIActionTypeDeclaration_urls() {
    this->initializeModel();
}

OAIActionTypeDeclaration_urls::~OAIActionTypeDeclaration_urls() {}

void OAIActionTypeDeclaration_urls::initializeModel() {

    m_configuration_url_isSet = false;
    m_configuration_url_isValid = false;

    m_entity_url_template_isSet = false;
    m_entity_url_template_isValid = false;

    m_execution_url_template_isSet = false;
    m_execution_url_template_isValid = false;

    m_revision_url_template_isSet = false;
    m_revision_url_template_isValid = false;
}

void OAIActionTypeDeclaration_urls::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActionTypeDeclaration_urls::fromJsonObject(QJsonObject json) {

    m_configuration_url_isValid = ::OpenAPI::fromJsonValue(m_configuration_url, json[QString("configurationUrl")]);
    m_configuration_url_isSet = !json[QString("configurationUrl")].isNull() && m_configuration_url_isValid;

    m_entity_url_template_isValid = ::OpenAPI::fromJsonValue(m_entity_url_template, json[QString("entityUrlTemplate")]);
    m_entity_url_template_isSet = !json[QString("entityUrlTemplate")].isNull() && m_entity_url_template_isValid;

    m_execution_url_template_isValid = ::OpenAPI::fromJsonValue(m_execution_url_template, json[QString("executionUrlTemplate")]);
    m_execution_url_template_isSet = !json[QString("executionUrlTemplate")].isNull() && m_execution_url_template_isValid;

    m_revision_url_template_isValid = ::OpenAPI::fromJsonValue(m_revision_url_template, json[QString("revisionUrlTemplate")]);
    m_revision_url_template_isSet = !json[QString("revisionUrlTemplate")].isNull() && m_revision_url_template_isValid;
}

QString OAIActionTypeDeclaration_urls::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActionTypeDeclaration_urls::asJsonObject() const {
    QJsonObject obj;
    if (m_configuration_url_isSet) {
        obj.insert(QString("configurationUrl"), ::OpenAPI::toJsonValue(m_configuration_url));
    }
    if (m_entity_url_template_isSet) {
        obj.insert(QString("entityUrlTemplate"), ::OpenAPI::toJsonValue(m_entity_url_template));
    }
    if (m_execution_url_template_isSet) {
        obj.insert(QString("executionUrlTemplate"), ::OpenAPI::toJsonValue(m_execution_url_template));
    }
    if (m_revision_url_template_isSet) {
        obj.insert(QString("revisionUrlTemplate"), ::OpenAPI::toJsonValue(m_revision_url_template));
    }
    return obj;
}

QString OAIActionTypeDeclaration_urls::getConfigurationUrl() const {
    return m_configuration_url;
}
void OAIActionTypeDeclaration_urls::setConfigurationUrl(const QString &configuration_url) {
    m_configuration_url = configuration_url;
    m_configuration_url_isSet = true;
}

bool OAIActionTypeDeclaration_urls::is_configuration_url_Set() const{
    return m_configuration_url_isSet;
}

bool OAIActionTypeDeclaration_urls::is_configuration_url_Valid() const{
    return m_configuration_url_isValid;
}

QString OAIActionTypeDeclaration_urls::getEntityUrlTemplate() const {
    return m_entity_url_template;
}
void OAIActionTypeDeclaration_urls::setEntityUrlTemplate(const QString &entity_url_template) {
    m_entity_url_template = entity_url_template;
    m_entity_url_template_isSet = true;
}

bool OAIActionTypeDeclaration_urls::is_entity_url_template_Set() const{
    return m_entity_url_template_isSet;
}

bool OAIActionTypeDeclaration_urls::is_entity_url_template_Valid() const{
    return m_entity_url_template_isValid;
}

QString OAIActionTypeDeclaration_urls::getExecutionUrlTemplate() const {
    return m_execution_url_template;
}
void OAIActionTypeDeclaration_urls::setExecutionUrlTemplate(const QString &execution_url_template) {
    m_execution_url_template = execution_url_template;
    m_execution_url_template_isSet = true;
}

bool OAIActionTypeDeclaration_urls::is_execution_url_template_Set() const{
    return m_execution_url_template_isSet;
}

bool OAIActionTypeDeclaration_urls::is_execution_url_template_Valid() const{
    return m_execution_url_template_isValid;
}

QString OAIActionTypeDeclaration_urls::getRevisionUrlTemplate() const {
    return m_revision_url_template;
}
void OAIActionTypeDeclaration_urls::setRevisionUrlTemplate(const QString &revision_url_template) {
    m_revision_url_template = revision_url_template;
    m_revision_url_template_isSet = true;
}

bool OAIActionTypeDeclaration_urls::is_revision_url_template_Set() const{
    return m_revision_url_template_isSet;
}

bool OAIActionTypeDeclaration_urls::is_revision_url_template_Valid() const{
    return m_revision_url_template_isValid;
}

bool OAIActionTypeDeclaration_urls::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_configuration_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_url_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_url_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_url_template_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActionTypeDeclaration_urls::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
