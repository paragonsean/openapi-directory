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

#include "OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate() {
    this->initializeModel();
}

OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::~OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate() {}

void OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

bool OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::isEnabled() const {
    return m_enabled;
}
void OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkApplianceTrafficShapingUplinkSelection_200_response_failoverAndFailback_immediate::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_enabled_isValid && true;
}

} // namespace OpenAPI
