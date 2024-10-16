/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateDeviceWirelessBluetoothSettings_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDeviceWirelessBluetoothSettings_request::OAIUpdateDeviceWirelessBluetoothSettings_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDeviceWirelessBluetoothSettings_request::OAIUpdateDeviceWirelessBluetoothSettings_request() {
    this->initializeModel();
}

OAIUpdateDeviceWirelessBluetoothSettings_request::~OAIUpdateDeviceWirelessBluetoothSettings_request() {}

void OAIUpdateDeviceWirelessBluetoothSettings_request::initializeModel() {

    m_major_isSet = false;
    m_major_isValid = false;

    m_minor_isSet = false;
    m_minor_isValid = false;

    m_uuid_isSet = false;
    m_uuid_isValid = false;
}

void OAIUpdateDeviceWirelessBluetoothSettings_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDeviceWirelessBluetoothSettings_request::fromJsonObject(QJsonObject json) {

    m_major_isValid = ::OpenAPI::fromJsonValue(m_major, json[QString("major")]);
    m_major_isSet = !json[QString("major")].isNull() && m_major_isValid;

    m_minor_isValid = ::OpenAPI::fromJsonValue(m_minor, json[QString("minor")]);
    m_minor_isSet = !json[QString("minor")].isNull() && m_minor_isValid;

    m_uuid_isValid = ::OpenAPI::fromJsonValue(m_uuid, json[QString("uuid")]);
    m_uuid_isSet = !json[QString("uuid")].isNull() && m_uuid_isValid;
}

QString OAIUpdateDeviceWirelessBluetoothSettings_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDeviceWirelessBluetoothSettings_request::asJsonObject() const {
    QJsonObject obj;
    if (m_major_isSet) {
        obj.insert(QString("major"), ::OpenAPI::toJsonValue(m_major));
    }
    if (m_minor_isSet) {
        obj.insert(QString("minor"), ::OpenAPI::toJsonValue(m_minor));
    }
    if (m_uuid_isSet) {
        obj.insert(QString("uuid"), ::OpenAPI::toJsonValue(m_uuid));
    }
    return obj;
}

qint32 OAIUpdateDeviceWirelessBluetoothSettings_request::getMajor() const {
    return m_major;
}
void OAIUpdateDeviceWirelessBluetoothSettings_request::setMajor(const qint32 &major) {
    m_major = major;
    m_major_isSet = true;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::is_major_Set() const{
    return m_major_isSet;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::is_major_Valid() const{
    return m_major_isValid;
}

qint32 OAIUpdateDeviceWirelessBluetoothSettings_request::getMinor() const {
    return m_minor;
}
void OAIUpdateDeviceWirelessBluetoothSettings_request::setMinor(const qint32 &minor) {
    m_minor = minor;
    m_minor_isSet = true;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::is_minor_Set() const{
    return m_minor_isSet;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::is_minor_Valid() const{
    return m_minor_isValid;
}

QString OAIUpdateDeviceWirelessBluetoothSettings_request::getUuid() const {
    return m_uuid;
}
void OAIUpdateDeviceWirelessBluetoothSettings_request::setUuid(const QString &uuid) {
    m_uuid = uuid;
    m_uuid_isSet = true;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::is_uuid_Set() const{
    return m_uuid_isSet;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::is_uuid_Valid() const{
    return m_uuid_isValid;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_major_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDeviceWirelessBluetoothSettings_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
