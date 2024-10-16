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

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::~OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits() {}

void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::initializeModel() {

    m_cellular_isSet = false;
    m_cellular_isValid = false;

    m_wan1_isSet = false;
    m_wan1_isValid = false;

    m_wan2_isSet = false;
    m_wan2_isValid = false;
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::fromJsonObject(QJsonObject json) {

    m_cellular_isValid = ::OpenAPI::fromJsonValue(m_cellular, json[QString("cellular")]);
    m_cellular_isSet = !json[QString("cellular")].isNull() && m_cellular_isValid;

    m_wan1_isValid = ::OpenAPI::fromJsonValue(m_wan1, json[QString("wan1")]);
    m_wan1_isSet = !json[QString("wan1")].isNull() && m_wan1_isValid;

    m_wan2_isValid = ::OpenAPI::fromJsonValue(m_wan2, json[QString("wan2")]);
    m_wan2_isSet = !json[QString("wan2")].isNull() && m_wan2_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::asJsonObject() const {
    QJsonObject obj;
    if (m_cellular.isSet()) {
        obj.insert(QString("cellular"), ::OpenAPI::toJsonValue(m_cellular));
    }
    if (m_wan1.isSet()) {
        obj.insert(QString("wan1"), ::OpenAPI::toJsonValue(m_wan1));
    }
    if (m_wan2.isSet()) {
        obj.insert(QString("wan2"), ::OpenAPI::toJsonValue(m_wan2));
    }
    return obj;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::getCellular() const {
    return m_cellular;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::setCellular(const OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular &cellular) {
    m_cellular = cellular;
    m_cellular_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::is_cellular_Set() const{
    return m_cellular_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::is_cellular_Valid() const{
    return m_cellular_isValid;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan1 OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::getWan1() const {
    return m_wan1;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::setWan1(const OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan1 &wan1) {
    m_wan1 = wan1;
    m_wan1_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::is_wan1_Set() const{
    return m_wan1_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::is_wan1_Valid() const{
    return m_wan1_isValid;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2 OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::getWan2() const {
    return m_wan2;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::setWan2(const OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2 &wan2) {
    m_wan2 = wan2;
    m_wan2_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::is_wan2_Set() const{
    return m_wan2_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::is_wan2_Valid() const{
    return m_wan2_isValid;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cellular.isSet()) {
            isObjectUpdated = true;
            break;
        }

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

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
