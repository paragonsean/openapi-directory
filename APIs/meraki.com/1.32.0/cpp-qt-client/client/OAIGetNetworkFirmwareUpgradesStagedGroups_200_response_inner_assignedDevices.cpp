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

#include "OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices() {
    this->initializeModel();
}

OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::~OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices() {}

void OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::initializeModel() {

    m_devices_isSet = false;
    m_devices_isValid = false;

    m_switch_stacks_isSet = false;
    m_switch_stacks_isValid = false;
}

void OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::fromJsonObject(QJsonObject json) {

    m_devices_isValid = ::OpenAPI::fromJsonValue(m_devices, json[QString("devices")]);
    m_devices_isSet = !json[QString("devices")].isNull() && m_devices_isValid;

    m_switch_stacks_isValid = ::OpenAPI::fromJsonValue(m_switch_stacks, json[QString("switchStacks")]);
    m_switch_stacks_isSet = !json[QString("switchStacks")].isNull() && m_switch_stacks_isValid;
}

QString OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::asJsonObject() const {
    QJsonObject obj;
    if (m_devices.size() > 0) {
        obj.insert(QString("devices"), ::OpenAPI::toJsonValue(m_devices));
    }
    if (m_switch_stacks.size() > 0) {
        obj.insert(QString("switchStacks"), ::OpenAPI::toJsonValue(m_switch_stacks));
    }
    return obj;
}

QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices_devices_inner> OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::getDevices() const {
    return m_devices;
}
void OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::setDevices(const QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices_devices_inner> &devices) {
    m_devices = devices;
    m_devices_isSet = true;
}

bool OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::is_devices_Set() const{
    return m_devices_isSet;
}

bool OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::is_devices_Valid() const{
    return m_devices_isValid;
}

QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices_switchStacks_inner> OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::getSwitchStacks() const {
    return m_switch_stacks;
}
void OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::setSwitchStacks(const QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices_switchStacks_inner> &switch_stacks) {
    m_switch_stacks = switch_stacks;
    m_switch_stacks_isSet = true;
}

bool OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::is_switch_stacks_Set() const{
    return m_switch_stacks_isSet;
}

bool OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::is_switch_stacks_Valid() const{
    return m_switch_stacks_isValid;
}

bool OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_devices.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_switch_stacks.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner_assignedDevices::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
