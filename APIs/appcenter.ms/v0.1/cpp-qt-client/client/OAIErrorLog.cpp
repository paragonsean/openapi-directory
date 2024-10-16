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

#include "OAIErrorLog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrorLog::OAIErrorLog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrorLog::OAIErrorLog() {
    this->initializeModel();
}

OAIErrorLog::~OAIErrorLog() {}

void OAIErrorLog::initializeModel() {

    m_app_launch_toffset_isSet = false;
    m_app_launch_toffset_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_session_id_isSet = false;
    m_session_id_isValid = false;

    m_device_isSet = false;
    m_device_isValid = false;

    m_install_id_isSet = false;
    m_install_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIErrorLog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrorLog::fromJsonObject(QJsonObject json) {

    m_app_launch_toffset_isValid = ::OpenAPI::fromJsonValue(m_app_launch_toffset, json[QString("app_launch_toffset")]);
    m_app_launch_toffset_isSet = !json[QString("app_launch_toffset")].isNull() && m_app_launch_toffset_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_session_id_isValid = ::OpenAPI::fromJsonValue(m_session_id, json[QString("session_id")]);
    m_session_id_isSet = !json[QString("session_id")].isNull() && m_session_id_isValid;

    m_device_isValid = ::OpenAPI::fromJsonValue(m_device, json[QString("device")]);
    m_device_isSet = !json[QString("device")].isNull() && m_device_isValid;

    m_install_id_isValid = ::OpenAPI::fromJsonValue(m_install_id, json[QString("install_id")]);
    m_install_id_isSet = !json[QString("install_id")].isNull() && m_install_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIErrorLog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrorLog::asJsonObject() const {
    QJsonObject obj;
    if (m_app_launch_toffset_isSet) {
        obj.insert(QString("app_launch_toffset"), ::OpenAPI::toJsonValue(m_app_launch_toffset));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_session_id_isSet) {
        obj.insert(QString("session_id"), ::OpenAPI::toJsonValue(m_session_id));
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

qint64 OAIErrorLog::getAppLaunchToffset() const {
    return m_app_launch_toffset;
}
void OAIErrorLog::setAppLaunchToffset(const qint64 &app_launch_toffset) {
    m_app_launch_toffset = app_launch_toffset;
    m_app_launch_toffset_isSet = true;
}

bool OAIErrorLog::is_app_launch_toffset_Set() const{
    return m_app_launch_toffset_isSet;
}

bool OAIErrorLog::is_app_launch_toffset_Valid() const{
    return m_app_launch_toffset_isValid;
}

QString OAIErrorLog::getId() const {
    return m_id;
}
void OAIErrorLog::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIErrorLog::is_id_Set() const{
    return m_id_isSet;
}

bool OAIErrorLog::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIErrorLog::getSessionId() const {
    return m_session_id;
}
void OAIErrorLog::setSessionId(const QString &session_id) {
    m_session_id = session_id;
    m_session_id_isSet = true;
}

bool OAIErrorLog::is_session_id_Set() const{
    return m_session_id_isSet;
}

bool OAIErrorLog::is_session_id_Valid() const{
    return m_session_id_isValid;
}

OAIAnalytics_GenericLogFlow_200_response_logs_inner_device OAIErrorLog::getDevice() const {
    return m_device;
}
void OAIErrorLog::setDevice(const OAIAnalytics_GenericLogFlow_200_response_logs_inner_device &device) {
    m_device = device;
    m_device_isSet = true;
}

bool OAIErrorLog::is_device_Set() const{
    return m_device_isSet;
}

bool OAIErrorLog::is_device_Valid() const{
    return m_device_isValid;
}

QString OAIErrorLog::getInstallId() const {
    return m_install_id;
}
void OAIErrorLog::setInstallId(const QString &install_id) {
    m_install_id = install_id;
    m_install_id_isSet = true;
}

bool OAIErrorLog::is_install_id_Set() const{
    return m_install_id_isSet;
}

bool OAIErrorLog::is_install_id_Valid() const{
    return m_install_id_isValid;
}

QDateTime OAIErrorLog::getTimestamp() const {
    return m_timestamp;
}
void OAIErrorLog::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIErrorLog::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIErrorLog::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAIErrorLog::getType() const {
    return m_type;
}
void OAIErrorLog::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIErrorLog::is_type_Set() const{
    return m_type_isSet;
}

bool OAIErrorLog::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIErrorLog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_launch_toffset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_session_id_isSet) {
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

bool OAIErrorLog::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_session_id_isValid && m_device_isValid && m_install_id_isValid && m_timestamp_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
