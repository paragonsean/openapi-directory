/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITaskPropertiesUpdateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITaskPropertiesUpdateParameters::OAITaskPropertiesUpdateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITaskPropertiesUpdateParameters::OAITaskPropertiesUpdateParameters() {
    this->initializeModel();
}

OAITaskPropertiesUpdateParameters::~OAITaskPropertiesUpdateParameters() {}

void OAITaskPropertiesUpdateParameters::initializeModel() {

    m_agent_configuration_isSet = false;
    m_agent_configuration_isValid = false;

    m_credentials_isSet = false;
    m_credentials_isValid = false;

    m_platform_isSet = false;
    m_platform_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_step_isSet = false;
    m_step_isValid = false;

    m_timeout_isSet = false;
    m_timeout_isValid = false;

    m_trigger_isSet = false;
    m_trigger_isValid = false;
}

void OAITaskPropertiesUpdateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITaskPropertiesUpdateParameters::fromJsonObject(QJsonObject json) {

    m_agent_configuration_isValid = ::OpenAPI::fromJsonValue(m_agent_configuration, json[QString("agentConfiguration")]);
    m_agent_configuration_isSet = !json[QString("agentConfiguration")].isNull() && m_agent_configuration_isValid;

    m_credentials_isValid = ::OpenAPI::fromJsonValue(m_credentials, json[QString("credentials")]);
    m_credentials_isSet = !json[QString("credentials")].isNull() && m_credentials_isValid;

    m_platform_isValid = ::OpenAPI::fromJsonValue(m_platform, json[QString("platform")]);
    m_platform_isSet = !json[QString("platform")].isNull() && m_platform_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_step_isValid = ::OpenAPI::fromJsonValue(m_step, json[QString("step")]);
    m_step_isSet = !json[QString("step")].isNull() && m_step_isValid;

    m_timeout_isValid = ::OpenAPI::fromJsonValue(m_timeout, json[QString("timeout")]);
    m_timeout_isSet = !json[QString("timeout")].isNull() && m_timeout_isValid;

    m_trigger_isValid = ::OpenAPI::fromJsonValue(m_trigger, json[QString("trigger")]);
    m_trigger_isSet = !json[QString("trigger")].isNull() && m_trigger_isValid;
}

QString OAITaskPropertiesUpdateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITaskPropertiesUpdateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_agent_configuration.isSet()) {
        obj.insert(QString("agentConfiguration"), ::OpenAPI::toJsonValue(m_agent_configuration));
    }
    if (m_credentials.isSet()) {
        obj.insert(QString("credentials"), ::OpenAPI::toJsonValue(m_credentials));
    }
    if (m_platform.isSet()) {
        obj.insert(QString("platform"), ::OpenAPI::toJsonValue(m_platform));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_step.isSet()) {
        obj.insert(QString("step"), ::OpenAPI::toJsonValue(m_step));
    }
    if (m_timeout_isSet) {
        obj.insert(QString("timeout"), ::OpenAPI::toJsonValue(m_timeout));
    }
    if (m_trigger.isSet()) {
        obj.insert(QString("trigger"), ::OpenAPI::toJsonValue(m_trigger));
    }
    return obj;
}

OAIAgentProperties OAITaskPropertiesUpdateParameters::getAgentConfiguration() const {
    return m_agent_configuration;
}
void OAITaskPropertiesUpdateParameters::setAgentConfiguration(const OAIAgentProperties &agent_configuration) {
    m_agent_configuration = agent_configuration;
    m_agent_configuration_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_agent_configuration_Set() const{
    return m_agent_configuration_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_agent_configuration_Valid() const{
    return m_agent_configuration_isValid;
}

OAICredentials OAITaskPropertiesUpdateParameters::getCredentials() const {
    return m_credentials;
}
void OAITaskPropertiesUpdateParameters::setCredentials(const OAICredentials &credentials) {
    m_credentials = credentials;
    m_credentials_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_credentials_Set() const{
    return m_credentials_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_credentials_Valid() const{
    return m_credentials_isValid;
}

OAIPlatformUpdateParameters OAITaskPropertiesUpdateParameters::getPlatform() const {
    return m_platform;
}
void OAITaskPropertiesUpdateParameters::setPlatform(const OAIPlatformUpdateParameters &platform) {
    m_platform = platform;
    m_platform_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_platform_Set() const{
    return m_platform_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_platform_Valid() const{
    return m_platform_isValid;
}

QString OAITaskPropertiesUpdateParameters::getStatus() const {
    return m_status;
}
void OAITaskPropertiesUpdateParameters::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_status_Set() const{
    return m_status_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_status_Valid() const{
    return m_status_isValid;
}

OAITaskStepUpdateParameters OAITaskPropertiesUpdateParameters::getStep() const {
    return m_step;
}
void OAITaskPropertiesUpdateParameters::setStep(const OAITaskStepUpdateParameters &step) {
    m_step = step;
    m_step_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_step_Set() const{
    return m_step_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_step_Valid() const{
    return m_step_isValid;
}

qint32 OAITaskPropertiesUpdateParameters::getTimeout() const {
    return m_timeout;
}
void OAITaskPropertiesUpdateParameters::setTimeout(const qint32 &timeout) {
    m_timeout = timeout;
    m_timeout_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_timeout_Set() const{
    return m_timeout_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_timeout_Valid() const{
    return m_timeout_isValid;
}

OAITriggerUpdateParameters OAITaskPropertiesUpdateParameters::getTrigger() const {
    return m_trigger;
}
void OAITaskPropertiesUpdateParameters::setTrigger(const OAITriggerUpdateParameters &trigger) {
    m_trigger = trigger;
    m_trigger_isSet = true;
}

bool OAITaskPropertiesUpdateParameters::is_trigger_Set() const{
    return m_trigger_isSet;
}

bool OAITaskPropertiesUpdateParameters::is_trigger_Valid() const{
    return m_trigger_isValid;
}

bool OAITaskPropertiesUpdateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agent_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_credentials.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_platform.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_step.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trigger.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITaskPropertiesUpdateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
