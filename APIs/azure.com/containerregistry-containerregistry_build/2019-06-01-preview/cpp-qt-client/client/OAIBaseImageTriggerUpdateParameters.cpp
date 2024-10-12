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

#include "OAIBaseImageTriggerUpdateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBaseImageTriggerUpdateParameters::OAIBaseImageTriggerUpdateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBaseImageTriggerUpdateParameters::OAIBaseImageTriggerUpdateParameters() {
    this->initializeModel();
}

OAIBaseImageTriggerUpdateParameters::~OAIBaseImageTriggerUpdateParameters() {}

void OAIBaseImageTriggerUpdateParameters::initializeModel() {

    m_base_image_trigger_type_isSet = false;
    m_base_image_trigger_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_update_trigger_endpoint_isSet = false;
    m_update_trigger_endpoint_isValid = false;

    m_update_trigger_payload_type_isSet = false;
    m_update_trigger_payload_type_isValid = false;
}

void OAIBaseImageTriggerUpdateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBaseImageTriggerUpdateParameters::fromJsonObject(QJsonObject json) {

    m_base_image_trigger_type_isValid = ::OpenAPI::fromJsonValue(m_base_image_trigger_type, json[QString("baseImageTriggerType")]);
    m_base_image_trigger_type_isSet = !json[QString("baseImageTriggerType")].isNull() && m_base_image_trigger_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_update_trigger_endpoint_isValid = ::OpenAPI::fromJsonValue(m_update_trigger_endpoint, json[QString("updateTriggerEndpoint")]);
    m_update_trigger_endpoint_isSet = !json[QString("updateTriggerEndpoint")].isNull() && m_update_trigger_endpoint_isValid;

    m_update_trigger_payload_type_isValid = ::OpenAPI::fromJsonValue(m_update_trigger_payload_type, json[QString("updateTriggerPayloadType")]);
    m_update_trigger_payload_type_isSet = !json[QString("updateTriggerPayloadType")].isNull() && m_update_trigger_payload_type_isValid;
}

QString OAIBaseImageTriggerUpdateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBaseImageTriggerUpdateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_base_image_trigger_type_isSet) {
        obj.insert(QString("baseImageTriggerType"), ::OpenAPI::toJsonValue(m_base_image_trigger_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_update_trigger_endpoint_isSet) {
        obj.insert(QString("updateTriggerEndpoint"), ::OpenAPI::toJsonValue(m_update_trigger_endpoint));
    }
    if (m_update_trigger_payload_type_isSet) {
        obj.insert(QString("updateTriggerPayloadType"), ::OpenAPI::toJsonValue(m_update_trigger_payload_type));
    }
    return obj;
}

QString OAIBaseImageTriggerUpdateParameters::getBaseImageTriggerType() const {
    return m_base_image_trigger_type;
}
void OAIBaseImageTriggerUpdateParameters::setBaseImageTriggerType(const QString &base_image_trigger_type) {
    m_base_image_trigger_type = base_image_trigger_type;
    m_base_image_trigger_type_isSet = true;
}

bool OAIBaseImageTriggerUpdateParameters::is_base_image_trigger_type_Set() const{
    return m_base_image_trigger_type_isSet;
}

bool OAIBaseImageTriggerUpdateParameters::is_base_image_trigger_type_Valid() const{
    return m_base_image_trigger_type_isValid;
}

QString OAIBaseImageTriggerUpdateParameters::getName() const {
    return m_name;
}
void OAIBaseImageTriggerUpdateParameters::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBaseImageTriggerUpdateParameters::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBaseImageTriggerUpdateParameters::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBaseImageTriggerUpdateParameters::getStatus() const {
    return m_status;
}
void OAIBaseImageTriggerUpdateParameters::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIBaseImageTriggerUpdateParameters::is_status_Set() const{
    return m_status_isSet;
}

bool OAIBaseImageTriggerUpdateParameters::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIBaseImageTriggerUpdateParameters::getUpdateTriggerEndpoint() const {
    return m_update_trigger_endpoint;
}
void OAIBaseImageTriggerUpdateParameters::setUpdateTriggerEndpoint(const QString &update_trigger_endpoint) {
    m_update_trigger_endpoint = update_trigger_endpoint;
    m_update_trigger_endpoint_isSet = true;
}

bool OAIBaseImageTriggerUpdateParameters::is_update_trigger_endpoint_Set() const{
    return m_update_trigger_endpoint_isSet;
}

bool OAIBaseImageTriggerUpdateParameters::is_update_trigger_endpoint_Valid() const{
    return m_update_trigger_endpoint_isValid;
}

QString OAIBaseImageTriggerUpdateParameters::getUpdateTriggerPayloadType() const {
    return m_update_trigger_payload_type;
}
void OAIBaseImageTriggerUpdateParameters::setUpdateTriggerPayloadType(const QString &update_trigger_payload_type) {
    m_update_trigger_payload_type = update_trigger_payload_type;
    m_update_trigger_payload_type_isSet = true;
}

bool OAIBaseImageTriggerUpdateParameters::is_update_trigger_payload_type_Set() const{
    return m_update_trigger_payload_type_isSet;
}

bool OAIBaseImageTriggerUpdateParameters::is_update_trigger_payload_type_Valid() const{
    return m_update_trigger_payload_type_isValid;
}

bool OAIBaseImageTriggerUpdateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_image_trigger_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_trigger_endpoint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_trigger_payload_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBaseImageTriggerUpdateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
