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

#include "OAIActionConfigurationProperty.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActionConfigurationProperty::OAIActionConfigurationProperty(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActionConfigurationProperty::OAIActionConfigurationProperty() {
    this->initializeModel();
}

OAIActionConfigurationProperty::~OAIActionConfigurationProperty() {}

void OAIActionConfigurationProperty::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_required_isSet = false;
    m_required_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_secret_isSet = false;
    m_secret_isValid = false;

    m_queryable_isSet = false;
    m_queryable_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIActionConfigurationProperty::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActionConfigurationProperty::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_required_isValid = ::OpenAPI::fromJsonValue(m_required, json[QString("required")]);
    m_required_isSet = !json[QString("required")].isNull() && m_required_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_secret_isValid = ::OpenAPI::fromJsonValue(m_secret, json[QString("secret")]);
    m_secret_isSet = !json[QString("secret")].isNull() && m_secret_isValid;

    m_queryable_isValid = ::OpenAPI::fromJsonValue(m_queryable, json[QString("queryable")]);
    m_queryable_isSet = !json[QString("queryable")].isNull() && m_queryable_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIActionConfigurationProperty::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActionConfigurationProperty::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_required_isSet) {
        obj.insert(QString("required"), ::OpenAPI::toJsonValue(m_required));
    }
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_secret_isSet) {
        obj.insert(QString("secret"), ::OpenAPI::toJsonValue(m_secret));
    }
    if (m_queryable_isSet) {
        obj.insert(QString("queryable"), ::OpenAPI::toJsonValue(m_queryable));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIActionConfigurationProperty::getName() const {
    return m_name;
}
void OAIActionConfigurationProperty::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIActionConfigurationProperty::is_name_Set() const{
    return m_name_isSet;
}

bool OAIActionConfigurationProperty::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIActionConfigurationProperty::getRequired() const {
    return m_required;
}
void OAIActionConfigurationProperty::setRequired(const bool &required) {
    m_required = required;
    m_required_isSet = true;
}

bool OAIActionConfigurationProperty::is_required_Set() const{
    return m_required_isSet;
}

bool OAIActionConfigurationProperty::is_required_Valid() const{
    return m_required_isValid;
}

bool OAIActionConfigurationProperty::getKey() const {
    return m_key;
}
void OAIActionConfigurationProperty::setKey(const bool &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAIActionConfigurationProperty::is_key_Set() const{
    return m_key_isSet;
}

bool OAIActionConfigurationProperty::is_key_Valid() const{
    return m_key_isValid;
}

bool OAIActionConfigurationProperty::getSecret() const {
    return m_secret;
}
void OAIActionConfigurationProperty::setSecret(const bool &secret) {
    m_secret = secret;
    m_secret_isSet = true;
}

bool OAIActionConfigurationProperty::is_secret_Set() const{
    return m_secret_isSet;
}

bool OAIActionConfigurationProperty::is_secret_Valid() const{
    return m_secret_isValid;
}

bool OAIActionConfigurationProperty::getQueryable() const {
    return m_queryable;
}
void OAIActionConfigurationProperty::setQueryable(const bool &queryable) {
    m_queryable = queryable;
    m_queryable_isSet = true;
}

bool OAIActionConfigurationProperty::is_queryable_Set() const{
    return m_queryable_isSet;
}

bool OAIActionConfigurationProperty::is_queryable_Valid() const{
    return m_queryable_isValid;
}

QString OAIActionConfigurationProperty::getDescription() const {
    return m_description;
}
void OAIActionConfigurationProperty::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIActionConfigurationProperty::is_description_Set() const{
    return m_description_isSet;
}

bool OAIActionConfigurationProperty::is_description_Valid() const{
    return m_description_isValid;
}

OAIActionConfigurationPropertyType OAIActionConfigurationProperty::getType() const {
    return m_type;
}
void OAIActionConfigurationProperty::setType(const OAIActionConfigurationPropertyType &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIActionConfigurationProperty::is_type_Set() const{
    return m_type_isSet;
}

bool OAIActionConfigurationProperty::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIActionConfigurationProperty::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secret_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_queryable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActionConfigurationProperty::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_required_isValid && m_key_isValid && m_secret_isValid && true;
}

} // namespace OpenAPI
