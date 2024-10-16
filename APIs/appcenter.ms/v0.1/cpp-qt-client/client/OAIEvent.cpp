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

#include "OAIEvent.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEvent::OAIEvent(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEvent::OAIEvent() {
    this->initializeModel();
}

OAIEvent::~OAIEvent() {}

void OAIEvent::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_count_per_device_isSet = false;
    m_count_per_device_isValid = false;

    m_count_per_session_isSet = false;
    m_count_per_session_isValid = false;

    m_device_count_isSet = false;
    m_device_count_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_previous_count_isSet = false;
    m_previous_count_isValid = false;

    m_previous_device_count_isSet = false;
    m_previous_device_count_isValid = false;
}

void OAIEvent::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEvent::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_count_per_device_isValid = ::OpenAPI::fromJsonValue(m_count_per_device, json[QString("count_per_device")]);
    m_count_per_device_isSet = !json[QString("count_per_device")].isNull() && m_count_per_device_isValid;

    m_count_per_session_isValid = ::OpenAPI::fromJsonValue(m_count_per_session, json[QString("count_per_session")]);
    m_count_per_session_isSet = !json[QString("count_per_session")].isNull() && m_count_per_session_isValid;

    m_device_count_isValid = ::OpenAPI::fromJsonValue(m_device_count, json[QString("device_count")]);
    m_device_count_isSet = !json[QString("device_count")].isNull() && m_device_count_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_previous_count_isValid = ::OpenAPI::fromJsonValue(m_previous_count, json[QString("previous_count")]);
    m_previous_count_isSet = !json[QString("previous_count")].isNull() && m_previous_count_isValid;

    m_previous_device_count_isValid = ::OpenAPI::fromJsonValue(m_previous_device_count, json[QString("previous_device_count")]);
    m_previous_device_count_isSet = !json[QString("previous_device_count")].isNull() && m_previous_device_count_isValid;
}

QString OAIEvent::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEvent::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_count_per_device_isSet) {
        obj.insert(QString("count_per_device"), ::OpenAPI::toJsonValue(m_count_per_device));
    }
    if (m_count_per_session_isSet) {
        obj.insert(QString("count_per_session"), ::OpenAPI::toJsonValue(m_count_per_session));
    }
    if (m_device_count_isSet) {
        obj.insert(QString("device_count"), ::OpenAPI::toJsonValue(m_device_count));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_previous_count_isSet) {
        obj.insert(QString("previous_count"), ::OpenAPI::toJsonValue(m_previous_count));
    }
    if (m_previous_device_count_isSet) {
        obj.insert(QString("previous_device_count"), ::OpenAPI::toJsonValue(m_previous_device_count));
    }
    return obj;
}

qint64 OAIEvent::getCount() const {
    return m_count;
}
void OAIEvent::setCount(const qint64 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIEvent::is_count_Set() const{
    return m_count_isSet;
}

bool OAIEvent::is_count_Valid() const{
    return m_count_isValid;
}

double OAIEvent::getCountPerDevice() const {
    return m_count_per_device;
}
void OAIEvent::setCountPerDevice(const double &count_per_device) {
    m_count_per_device = count_per_device;
    m_count_per_device_isSet = true;
}

bool OAIEvent::is_count_per_device_Set() const{
    return m_count_per_device_isSet;
}

bool OAIEvent::is_count_per_device_Valid() const{
    return m_count_per_device_isValid;
}

double OAIEvent::getCountPerSession() const {
    return m_count_per_session;
}
void OAIEvent::setCountPerSession(const double &count_per_session) {
    m_count_per_session = count_per_session;
    m_count_per_session_isSet = true;
}

bool OAIEvent::is_count_per_session_Set() const{
    return m_count_per_session_isSet;
}

bool OAIEvent::is_count_per_session_Valid() const{
    return m_count_per_session_isValid;
}

qint64 OAIEvent::getDeviceCount() const {
    return m_device_count;
}
void OAIEvent::setDeviceCount(const qint64 &device_count) {
    m_device_count = device_count;
    m_device_count_isSet = true;
}

bool OAIEvent::is_device_count_Set() const{
    return m_device_count_isSet;
}

bool OAIEvent::is_device_count_Valid() const{
    return m_device_count_isValid;
}

QString OAIEvent::getId() const {
    return m_id;
}
void OAIEvent::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEvent::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEvent::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIEvent::getName() const {
    return m_name;
}
void OAIEvent::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIEvent::is_name_Set() const{
    return m_name_isSet;
}

bool OAIEvent::is_name_Valid() const{
    return m_name_isValid;
}

qint64 OAIEvent::getPreviousCount() const {
    return m_previous_count;
}
void OAIEvent::setPreviousCount(const qint64 &previous_count) {
    m_previous_count = previous_count;
    m_previous_count_isSet = true;
}

bool OAIEvent::is_previous_count_Set() const{
    return m_previous_count_isSet;
}

bool OAIEvent::is_previous_count_Valid() const{
    return m_previous_count_isValid;
}

qint64 OAIEvent::getPreviousDeviceCount() const {
    return m_previous_device_count;
}
void OAIEvent::setPreviousDeviceCount(const qint64 &previous_device_count) {
    m_previous_device_count = previous_device_count;
    m_previous_device_count_isSet = true;
}

bool OAIEvent::is_previous_device_count_Set() const{
    return m_previous_device_count_isSet;
}

bool OAIEvent::is_previous_device_count_Valid() const{
    return m_previous_device_count_isValid;
}

bool OAIEvent::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_per_device_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_per_session_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_previous_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_previous_device_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEvent::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
