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

#include "OAIActionDeclaration_actionTypeId.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActionDeclaration_actionTypeId::OAIActionDeclaration_actionTypeId(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActionDeclaration_actionTypeId::OAIActionDeclaration_actionTypeId() {
    this->initializeModel();
}

OAIActionDeclaration_actionTypeId::~OAIActionDeclaration_actionTypeId() {}

void OAIActionDeclaration_actionTypeId::initializeModel() {

    m_category_isSet = false;
    m_category_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_provider_isSet = false;
    m_provider_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIActionDeclaration_actionTypeId::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActionDeclaration_actionTypeId::fromJsonObject(QJsonObject json) {

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_provider_isValid = ::OpenAPI::fromJsonValue(m_provider, json[QString("provider")]);
    m_provider_isSet = !json[QString("provider")].isNull() && m_provider_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIActionDeclaration_actionTypeId::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActionDeclaration_actionTypeId::asJsonObject() const {
    QJsonObject obj;
    if (m_category.isSet()) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_owner.isSet()) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
    }
    if (m_provider_isSet) {
        obj.insert(QString("provider"), ::OpenAPI::toJsonValue(m_provider));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

OAIActionCategory OAIActionDeclaration_actionTypeId::getCategory() const {
    return m_category;
}
void OAIActionDeclaration_actionTypeId::setCategory(const OAIActionCategory &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIActionDeclaration_actionTypeId::is_category_Set() const{
    return m_category_isSet;
}

bool OAIActionDeclaration_actionTypeId::is_category_Valid() const{
    return m_category_isValid;
}

OAIActionOwner OAIActionDeclaration_actionTypeId::getOwner() const {
    return m_owner;
}
void OAIActionDeclaration_actionTypeId::setOwner(const OAIActionOwner &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAIActionDeclaration_actionTypeId::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAIActionDeclaration_actionTypeId::is_owner_Valid() const{
    return m_owner_isValid;
}

QString OAIActionDeclaration_actionTypeId::getProvider() const {
    return m_provider;
}
void OAIActionDeclaration_actionTypeId::setProvider(const QString &provider) {
    m_provider = provider;
    m_provider_isSet = true;
}

bool OAIActionDeclaration_actionTypeId::is_provider_Set() const{
    return m_provider_isSet;
}

bool OAIActionDeclaration_actionTypeId::is_provider_Valid() const{
    return m_provider_isValid;
}

QString OAIActionDeclaration_actionTypeId::getVersion() const {
    return m_version;
}
void OAIActionDeclaration_actionTypeId::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIActionDeclaration_actionTypeId::is_version_Set() const{
    return m_version_isSet;
}

bool OAIActionDeclaration_actionTypeId::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIActionDeclaration_actionTypeId::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActionDeclaration_actionTypeId::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_category_isValid && m_owner_isValid && m_provider_isValid && m_version_isValid && true;
}

} // namespace OpenAPI
