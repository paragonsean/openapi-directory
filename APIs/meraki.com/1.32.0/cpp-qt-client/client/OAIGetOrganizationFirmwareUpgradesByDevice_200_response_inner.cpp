/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner() {
    this->initializeModel();
}

OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::~OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner() {}

void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::initializeModel() {

    m_device_status_isSet = false;
    m_device_status_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_serial_isSet = false;
    m_serial_isValid = false;

    m_upgrade_isSet = false;
    m_upgrade_isValid = false;
}

void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::fromJsonObject(QJsonObject json) {

    m_device_status_isValid = ::OpenAPI::fromJsonValue(m_device_status, json[QString("deviceStatus")]);
    m_device_status_isSet = !json[QString("deviceStatus")].isNull() && m_device_status_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_serial_isValid = ::OpenAPI::fromJsonValue(m_serial, json[QString("serial")]);
    m_serial_isSet = !json[QString("serial")].isNull() && m_serial_isValid;

    m_upgrade_isValid = ::OpenAPI::fromJsonValue(m_upgrade, json[QString("upgrade")]);
    m_upgrade_isSet = !json[QString("upgrade")].isNull() && m_upgrade_isValid;
}

QString OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_device_status_isSet) {
        obj.insert(QString("deviceStatus"), ::OpenAPI::toJsonValue(m_device_status));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_serial_isSet) {
        obj.insert(QString("serial"), ::OpenAPI::toJsonValue(m_serial));
    }
    if (m_upgrade.isSet()) {
        obj.insert(QString("upgrade"), ::OpenAPI::toJsonValue(m_upgrade));
    }
    return obj;
}

QString OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::getDeviceStatus() const {
    return m_device_status;
}
void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::setDeviceStatus(const QString &device_status) {
    m_device_status = device_status;
    m_device_status_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_device_status_Set() const{
    return m_device_status_isSet;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_device_status_Valid() const{
    return m_device_status_isValid;
}

QString OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::getName() const {
    return m_name;
}
void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::getSerial() const {
    return m_serial;
}
void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::setSerial(const QString &serial) {
    m_serial = serial;
    m_serial_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_serial_Set() const{
    return m_serial_isSet;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_serial_Valid() const{
    return m_serial_isValid;
}

OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::getUpgrade() const {
    return m_upgrade;
}
void OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::setUpgrade(const OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade &upgrade) {
    m_upgrade = upgrade;
    m_upgrade_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_upgrade_Set() const{
    return m_upgrade_isSet;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::is_upgrade_Valid() const{
    return m_upgrade_isValid;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_device_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serial_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upgrade.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
