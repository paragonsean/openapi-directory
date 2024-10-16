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

#include "OAIGetDeviceApplianceUplinksSettings_200_response_interfaces.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::OAIGetDeviceApplianceUplinksSettings_200_response_interfaces(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::OAIGetDeviceApplianceUplinksSettings_200_response_interfaces() {
    this->initializeModel();
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::~OAIGetDeviceApplianceUplinksSettings_200_response_interfaces() {}

void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::initializeModel() {

    m_wan1_isSet = false;
    m_wan1_isValid = false;

    m_wan2_isSet = false;
    m_wan2_isValid = false;
}

void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::fromJsonObject(QJsonObject json) {

    m_wan1_isValid = ::OpenAPI::fromJsonValue(m_wan1, json[QString("wan1")]);
    m_wan1_isSet = !json[QString("wan1")].isNull() && m_wan1_isValid;

    m_wan2_isValid = ::OpenAPI::fromJsonValue(m_wan2, json[QString("wan2")]);
    m_wan2_isSet = !json[QString("wan2")].isNull() && m_wan2_isValid;
}

QString OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::asJsonObject() const {
    QJsonObject obj;
    if (m_wan1.isSet()) {
        obj.insert(QString("wan1"), ::OpenAPI::toJsonValue(m_wan1));
    }
    if (m_wan2.isSet()) {
        obj.insert(QString("wan2"), ::OpenAPI::toJsonValue(m_wan2));
    }
    return obj;
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1 OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::getWan1() const {
    return m_wan1;
}
void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::setWan1(const OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1 &wan1) {
    m_wan1 = wan1;
    m_wan1_isSet = true;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::is_wan1_Set() const{
    return m_wan1_isSet;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::is_wan1_Valid() const{
    return m_wan1_isValid;
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan2 OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::getWan2() const {
    return m_wan2;
}
void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::setWan2(const OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan2 &wan2) {
    m_wan2 = wan2;
    m_wan2_isSet = true;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::is_wan2_Set() const{
    return m_wan2_isSet;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::is_wan2_Valid() const{
    return m_wan2_isValid;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_wan1.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_wan2.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
