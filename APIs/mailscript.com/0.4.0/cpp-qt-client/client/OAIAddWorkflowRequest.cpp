/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddWorkflowRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddWorkflowRequest::OAIAddWorkflowRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddWorkflowRequest::OAIAddWorkflowRequest() {
    this->initializeModel();
}

OAIAddWorkflowRequest::~OAIAddWorkflowRequest() {}

void OAIAddWorkflowRequest::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_active_isSet = false;
    m_active_isValid = false;

    m_input_isSet = false;
    m_input_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_trigger_isSet = false;
    m_trigger_isValid = false;
}

void OAIAddWorkflowRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddWorkflowRequest::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_trigger_isValid = ::OpenAPI::fromJsonValue(m_trigger, json[QString("trigger")]);
    m_trigger_isSet = !json[QString("trigger")].isNull() && m_trigger_isValid;
}

QString OAIAddWorkflowRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddWorkflowRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_action_isSet) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_input_isSet) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_trigger_isSet) {
        obj.insert(QString("trigger"), ::OpenAPI::toJsonValue(m_trigger));
    }
    return obj;
}

QString OAIAddWorkflowRequest::getAction() const {
    return m_action;
}
void OAIAddWorkflowRequest::setAction(const QString &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIAddWorkflowRequest::is_action_Set() const{
    return m_action_isSet;
}

bool OAIAddWorkflowRequest::is_action_Valid() const{
    return m_action_isValid;
}

bool OAIAddWorkflowRequest::isActive() const {
    return m_active;
}
void OAIAddWorkflowRequest::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIAddWorkflowRequest::is_active_Set() const{
    return m_active_isSet;
}

bool OAIAddWorkflowRequest::is_active_Valid() const{
    return m_active_isValid;
}

QString OAIAddWorkflowRequest::getInput() const {
    return m_input;
}
void OAIAddWorkflowRequest::setInput(const QString &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIAddWorkflowRequest::is_input_Set() const{
    return m_input_isSet;
}

bool OAIAddWorkflowRequest::is_input_Valid() const{
    return m_input_isValid;
}

QString OAIAddWorkflowRequest::getName() const {
    return m_name;
}
void OAIAddWorkflowRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAddWorkflowRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAddWorkflowRequest::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAddWorkflowRequest::getTrigger() const {
    return m_trigger;
}
void OAIAddWorkflowRequest::setTrigger(const QString &trigger) {
    m_trigger = trigger;
    m_trigger_isSet = true;
}

bool OAIAddWorkflowRequest::is_trigger_Set() const{
    return m_trigger_isSet;
}

bool OAIAddWorkflowRequest::is_trigger_Valid() const{
    return m_trigger_isValid;
}

bool OAIAddWorkflowRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trigger_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddWorkflowRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_action_isValid && m_input_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
