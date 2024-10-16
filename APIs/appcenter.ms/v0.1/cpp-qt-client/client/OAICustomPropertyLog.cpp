/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomPropertyLog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomPropertyLog::OAICustomPropertyLog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomPropertyLog::OAICustomPropertyLog() {
    this->initializeModel();
}

OAICustomPropertyLog::~OAICustomPropertyLog() {}

void OAICustomPropertyLog::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_device_isSet = false;
    m_device_isValid = false;

    m_install_id_isSet = false;
    m_install_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAICustomPropertyLog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomPropertyLog::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_device_isValid = ::OpenAPI::fromJsonValue(m_device, json[QString("device")]);
    m_device_isSet = !json[QString("device")].isNull() && m_device_isValid;

    m_install_id_isValid = ::OpenAPI::fromJsonValue(m_install_id, json[QString("install_id")]);
    m_install_id_isSet = !json[QString("install_id")].isNull() && m_install_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAICustomPropertyLog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomPropertyLog::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_device.isSet()) {
        obj.insert(QString("device"), ::OpenAPI::toJsonValue(m_device));
    }
    if (m_install_id_isSet) {
        obj.insert(QString("install_id"), ::OpenAPI::toJsonValue(m_install_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<OAIObject> OAICustomPropertyLog::getProperties() const {
    return m_properties;
}
void OAICustomPropertyLog::setProperties(const QList<OAIObject> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAICustomPropertyLog::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAICustomPropertyLog::is_properties_Valid() const{
    return m_properties_isValid;
}

OAIAnalytics_GenericLogFlow_200_response_logs_inner_device OAICustomPropertyLog::getDevice() const {
    return m_device;
}
void OAICustomPropertyLog::setDevice(const OAIAnalytics_GenericLogFlow_200_response_logs_inner_device &device) {
    m_device = device;
    m_device_isSet = true;
}

bool OAICustomPropertyLog::is_device_Set() const{
    return m_device_isSet;
}

bool OAICustomPropertyLog::is_device_Valid() const{
    return m_device_isValid;
}

QString OAICustomPropertyLog::getInstallId() const {
    return m_install_id;
}
void OAICustomPropertyLog::setInstallId(const QString &install_id) {
    m_install_id = install_id;
    m_install_id_isSet = true;
}

bool OAICustomPropertyLog::is_install_id_Set() const{
    return m_install_id_isSet;
}

bool OAICustomPropertyLog::is_install_id_Valid() const{
    return m_install_id_isValid;
}

QDateTime OAICustomPropertyLog::getTimestamp() const {
    return m_timestamp;
}
void OAICustomPropertyLog::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAICustomPropertyLog::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAICustomPropertyLog::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAICustomPropertyLog::getType() const {
    return m_type;
}
void OAICustomPropertyLog::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICustomPropertyLog::is_type_Set() const{
    return m_type_isSet;
}

bool OAICustomPropertyLog::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICustomPropertyLog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_device.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_install_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomPropertyLog::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_device_isValid && m_install_id_isValid && m_timestamp_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
