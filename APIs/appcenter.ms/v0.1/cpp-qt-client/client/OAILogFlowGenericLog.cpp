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

#include "OAILogFlowGenericLog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILogFlowGenericLog::OAILogFlowGenericLog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILogFlowGenericLog::OAILogFlowGenericLog() {
    this->initializeModel();
}

OAILogFlowGenericLog::~OAILogFlowGenericLog() {}

void OAILogFlowGenericLog::initializeModel() {

    m_account_id_isSet = false;
    m_account_id_isValid = false;

    m_auth_provider_isSet = false;
    m_auth_provider_isValid = false;

    m_device_isSet = false;
    m_device_isValid = false;

    m_event_id_isSet = false;
    m_event_id_isValid = false;

    m_event_name_isSet = false;
    m_event_name_isValid = false;

    m_install_id_isSet = false;
    m_install_id_isValid = false;

    m_message_id_isSet = false;
    m_message_id_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_session_id_isSet = false;
    m_session_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAILogFlowGenericLog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILogFlowGenericLog::fromJsonObject(QJsonObject json) {

    m_account_id_isValid = ::OpenAPI::fromJsonValue(m_account_id, json[QString("account_id")]);
    m_account_id_isSet = !json[QString("account_id")].isNull() && m_account_id_isValid;

    m_auth_provider_isValid = ::OpenAPI::fromJsonValue(m_auth_provider, json[QString("auth_provider")]);
    m_auth_provider_isSet = !json[QString("auth_provider")].isNull() && m_auth_provider_isValid;

    m_device_isValid = ::OpenAPI::fromJsonValue(m_device, json[QString("device")]);
    m_device_isSet = !json[QString("device")].isNull() && m_device_isValid;

    m_event_id_isValid = ::OpenAPI::fromJsonValue(m_event_id, json[QString("event_id")]);
    m_event_id_isSet = !json[QString("event_id")].isNull() && m_event_id_isValid;

    m_event_name_isValid = ::OpenAPI::fromJsonValue(m_event_name, json[QString("event_name")]);
    m_event_name_isSet = !json[QString("event_name")].isNull() && m_event_name_isValid;

    m_install_id_isValid = ::OpenAPI::fromJsonValue(m_install_id, json[QString("install_id")]);
    m_install_id_isSet = !json[QString("install_id")].isNull() && m_install_id_isValid;

    m_message_id_isValid = ::OpenAPI::fromJsonValue(m_message_id, json[QString("message_id")]);
    m_message_id_isSet = !json[QString("message_id")].isNull() && m_message_id_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_session_id_isValid = ::OpenAPI::fromJsonValue(m_session_id, json[QString("session_id")]);
    m_session_id_isSet = !json[QString("session_id")].isNull() && m_session_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAILogFlowGenericLog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILogFlowGenericLog::asJsonObject() const {
    QJsonObject obj;
    if (m_account_id_isSet) {
        obj.insert(QString("account_id"), ::OpenAPI::toJsonValue(m_account_id));
    }
    if (m_auth_provider_isSet) {
        obj.insert(QString("auth_provider"), ::OpenAPI::toJsonValue(m_auth_provider));
    }
    if (m_device.isSet()) {
        obj.insert(QString("device"), ::OpenAPI::toJsonValue(m_device));
    }
    if (m_event_id_isSet) {
        obj.insert(QString("event_id"), ::OpenAPI::toJsonValue(m_event_id));
    }
    if (m_event_name_isSet) {
        obj.insert(QString("event_name"), ::OpenAPI::toJsonValue(m_event_name));
    }
    if (m_install_id_isSet) {
        obj.insert(QString("install_id"), ::OpenAPI::toJsonValue(m_install_id));
    }
    if (m_message_id_isSet) {
        obj.insert(QString("message_id"), ::OpenAPI::toJsonValue(m_message_id));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_session_id_isSet) {
        obj.insert(QString("session_id"), ::OpenAPI::toJsonValue(m_session_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAILogFlowGenericLog::getAccountId() const {
    return m_account_id;
}
void OAILogFlowGenericLog::setAccountId(const QString &account_id) {
    m_account_id = account_id;
    m_account_id_isSet = true;
}

bool OAILogFlowGenericLog::is_account_id_Set() const{
    return m_account_id_isSet;
}

bool OAILogFlowGenericLog::is_account_id_Valid() const{
    return m_account_id_isValid;
}

QString OAILogFlowGenericLog::getAuthProvider() const {
    return m_auth_provider;
}
void OAILogFlowGenericLog::setAuthProvider(const QString &auth_provider) {
    m_auth_provider = auth_provider;
    m_auth_provider_isSet = true;
}

bool OAILogFlowGenericLog::is_auth_provider_Set() const{
    return m_auth_provider_isSet;
}

bool OAILogFlowGenericLog::is_auth_provider_Valid() const{
    return m_auth_provider_isValid;
}

OAIAnalytics_GenericLogFlow_200_response_logs_inner_device OAILogFlowGenericLog::getDevice() const {
    return m_device;
}
void OAILogFlowGenericLog::setDevice(const OAIAnalytics_GenericLogFlow_200_response_logs_inner_device &device) {
    m_device = device;
    m_device_isSet = true;
}

bool OAILogFlowGenericLog::is_device_Set() const{
    return m_device_isSet;
}

bool OAILogFlowGenericLog::is_device_Valid() const{
    return m_device_isValid;
}

QString OAILogFlowGenericLog::getEventId() const {
    return m_event_id;
}
void OAILogFlowGenericLog::setEventId(const QString &event_id) {
    m_event_id = event_id;
    m_event_id_isSet = true;
}

bool OAILogFlowGenericLog::is_event_id_Set() const{
    return m_event_id_isSet;
}

bool OAILogFlowGenericLog::is_event_id_Valid() const{
    return m_event_id_isValid;
}

QString OAILogFlowGenericLog::getEventName() const {
    return m_event_name;
}
void OAILogFlowGenericLog::setEventName(const QString &event_name) {
    m_event_name = event_name;
    m_event_name_isSet = true;
}

bool OAILogFlowGenericLog::is_event_name_Set() const{
    return m_event_name_isSet;
}

bool OAILogFlowGenericLog::is_event_name_Valid() const{
    return m_event_name_isValid;
}

QString OAILogFlowGenericLog::getInstallId() const {
    return m_install_id;
}
void OAILogFlowGenericLog::setInstallId(const QString &install_id) {
    m_install_id = install_id;
    m_install_id_isSet = true;
}

bool OAILogFlowGenericLog::is_install_id_Set() const{
    return m_install_id_isSet;
}

bool OAILogFlowGenericLog::is_install_id_Valid() const{
    return m_install_id_isValid;
}

QString OAILogFlowGenericLog::getMessageId() const {
    return m_message_id;
}
void OAILogFlowGenericLog::setMessageId(const QString &message_id) {
    m_message_id = message_id;
    m_message_id_isSet = true;
}

bool OAILogFlowGenericLog::is_message_id_Set() const{
    return m_message_id_isSet;
}

bool OAILogFlowGenericLog::is_message_id_Valid() const{
    return m_message_id_isValid;
}

QMap<QString, QString> OAILogFlowGenericLog::getProperties() const {
    return m_properties;
}
void OAILogFlowGenericLog::setProperties(const QMap<QString, QString> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAILogFlowGenericLog::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAILogFlowGenericLog::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAILogFlowGenericLog::getSessionId() const {
    return m_session_id;
}
void OAILogFlowGenericLog::setSessionId(const QString &session_id) {
    m_session_id = session_id;
    m_session_id_isSet = true;
}

bool OAILogFlowGenericLog::is_session_id_Set() const{
    return m_session_id_isSet;
}

bool OAILogFlowGenericLog::is_session_id_Valid() const{
    return m_session_id_isValid;
}

QDateTime OAILogFlowGenericLog::getTimestamp() const {
    return m_timestamp;
}
void OAILogFlowGenericLog::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAILogFlowGenericLog::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAILogFlowGenericLog::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAILogFlowGenericLog::getType() const {
    return m_type;
}
void OAILogFlowGenericLog::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAILogFlowGenericLog::is_type_Set() const{
    return m_type_isSet;
}

bool OAILogFlowGenericLog::is_type_Valid() const{
    return m_type_isValid;
}

bool OAILogFlowGenericLog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auth_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_device.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_install_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_session_id_isSet) {
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

bool OAILogFlowGenericLog::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_device_isValid && m_install_id_isValid && m_timestamp_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
