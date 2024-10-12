/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOverrideTaskStepProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOverrideTaskStepProperties::OAIOverrideTaskStepProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOverrideTaskStepProperties::OAIOverrideTaskStepProperties() {
    this->initializeModel();
}

OAIOverrideTaskStepProperties::~OAIOverrideTaskStepProperties() {}

void OAIOverrideTaskStepProperties::initializeModel() {

    m_arguments_isSet = false;
    m_arguments_isValid = false;

    m_context_path_isSet = false;
    m_context_path_isValid = false;

    m_file_isSet = false;
    m_file_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;

    m_update_trigger_token_isSet = false;
    m_update_trigger_token_isValid = false;

    m_values_isSet = false;
    m_values_isValid = false;
}

void OAIOverrideTaskStepProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOverrideTaskStepProperties::fromJsonObject(QJsonObject json) {

    m_arguments_isValid = ::OpenAPI::fromJsonValue(m_arguments, json[QString("arguments")]);
    m_arguments_isSet = !json[QString("arguments")].isNull() && m_arguments_isValid;

    m_context_path_isValid = ::OpenAPI::fromJsonValue(m_context_path, json[QString("contextPath")]);
    m_context_path_isSet = !json[QString("contextPath")].isNull() && m_context_path_isValid;

    m_file_isValid = ::OpenAPI::fromJsonValue(m_file, json[QString("file")]);
    m_file_isSet = !json[QString("file")].isNull() && m_file_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;

    m_update_trigger_token_isValid = ::OpenAPI::fromJsonValue(m_update_trigger_token, json[QString("updateTriggerToken")]);
    m_update_trigger_token_isSet = !json[QString("updateTriggerToken")].isNull() && m_update_trigger_token_isValid;

    m_values_isValid = ::OpenAPI::fromJsonValue(m_values, json[QString("values")]);
    m_values_isSet = !json[QString("values")].isNull() && m_values_isValid;
}

QString OAIOverrideTaskStepProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOverrideTaskStepProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_arguments.size() > 0) {
        obj.insert(QString("arguments"), ::OpenAPI::toJsonValue(m_arguments));
    }
    if (m_context_path_isSet) {
        obj.insert(QString("contextPath"), ::OpenAPI::toJsonValue(m_context_path));
    }
    if (m_file_isSet) {
        obj.insert(QString("file"), ::OpenAPI::toJsonValue(m_file));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    if (m_update_trigger_token_isSet) {
        obj.insert(QString("updateTriggerToken"), ::OpenAPI::toJsonValue(m_update_trigger_token));
    }
    if (m_values.size() > 0) {
        obj.insert(QString("values"), ::OpenAPI::toJsonValue(m_values));
    }
    return obj;
}

QList<OAIArgument> OAIOverrideTaskStepProperties::getArguments() const {
    return m_arguments;
}
void OAIOverrideTaskStepProperties::setArguments(const QList<OAIArgument> &arguments) {
    m_arguments = arguments;
    m_arguments_isSet = true;
}

bool OAIOverrideTaskStepProperties::is_arguments_Set() const{
    return m_arguments_isSet;
}

bool OAIOverrideTaskStepProperties::is_arguments_Valid() const{
    return m_arguments_isValid;
}

QString OAIOverrideTaskStepProperties::getContextPath() const {
    return m_context_path;
}
void OAIOverrideTaskStepProperties::setContextPath(const QString &context_path) {
    m_context_path = context_path;
    m_context_path_isSet = true;
}

bool OAIOverrideTaskStepProperties::is_context_path_Set() const{
    return m_context_path_isSet;
}

bool OAIOverrideTaskStepProperties::is_context_path_Valid() const{
    return m_context_path_isValid;
}

QString OAIOverrideTaskStepProperties::getFile() const {
    return m_file;
}
void OAIOverrideTaskStepProperties::setFile(const QString &file) {
    m_file = file;
    m_file_isSet = true;
}

bool OAIOverrideTaskStepProperties::is_file_Set() const{
    return m_file_isSet;
}

bool OAIOverrideTaskStepProperties::is_file_Valid() const{
    return m_file_isValid;
}

QString OAIOverrideTaskStepProperties::getTarget() const {
    return m_target;
}
void OAIOverrideTaskStepProperties::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIOverrideTaskStepProperties::is_target_Set() const{
    return m_target_isSet;
}

bool OAIOverrideTaskStepProperties::is_target_Valid() const{
    return m_target_isValid;
}

QString OAIOverrideTaskStepProperties::getUpdateTriggerToken() const {
    return m_update_trigger_token;
}
void OAIOverrideTaskStepProperties::setUpdateTriggerToken(const QString &update_trigger_token) {
    m_update_trigger_token = update_trigger_token;
    m_update_trigger_token_isSet = true;
}

bool OAIOverrideTaskStepProperties::is_update_trigger_token_Set() const{
    return m_update_trigger_token_isSet;
}

bool OAIOverrideTaskStepProperties::is_update_trigger_token_Valid() const{
    return m_update_trigger_token_isValid;
}

QList<OAISetValue> OAIOverrideTaskStepProperties::getValues() const {
    return m_values;
}
void OAIOverrideTaskStepProperties::setValues(const QList<OAISetValue> &values) {
    m_values = values;
    m_values_isSet = true;
}

bool OAIOverrideTaskStepProperties::is_values_Set() const{
    return m_values_isSet;
}

bool OAIOverrideTaskStepProperties::is_values_Valid() const{
    return m_values_isValid;
}

bool OAIOverrideTaskStepProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arguments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_context_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_trigger_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_values.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOverrideTaskStepProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
