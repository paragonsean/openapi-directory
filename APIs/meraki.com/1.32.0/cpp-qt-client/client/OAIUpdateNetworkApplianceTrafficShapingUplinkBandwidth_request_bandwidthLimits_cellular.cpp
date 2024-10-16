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

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::~OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular() {}

void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::initializeModel() {

    m_limit_down_isSet = false;
    m_limit_down_isValid = false;

    m_limit_up_isSet = false;
    m_limit_up_isValid = false;
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::fromJsonObject(QJsonObject json) {

    m_limit_down_isValid = ::OpenAPI::fromJsonValue(m_limit_down, json[QString("limitDown")]);
    m_limit_down_isSet = !json[QString("limitDown")].isNull() && m_limit_down_isValid;

    m_limit_up_isValid = ::OpenAPI::fromJsonValue(m_limit_up, json[QString("limitUp")]);
    m_limit_up_isSet = !json[QString("limitUp")].isNull() && m_limit_up_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::asJsonObject() const {
    QJsonObject obj;
    if (m_limit_down_isSet) {
        obj.insert(QString("limitDown"), ::OpenAPI::toJsonValue(m_limit_down));
    }
    if (m_limit_up_isSet) {
        obj.insert(QString("limitUp"), ::OpenAPI::toJsonValue(m_limit_up));
    }
    return obj;
}

qint32 OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::getLimitDown() const {
    return m_limit_down;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::setLimitDown(const qint32 &limit_down) {
    m_limit_down = limit_down;
    m_limit_down_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::is_limit_down_Set() const{
    return m_limit_down_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::is_limit_down_Valid() const{
    return m_limit_down_isValid;
}

qint32 OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::getLimitUp() const {
    return m_limit_up;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::setLimitUp(const qint32 &limit_up) {
    m_limit_up = limit_up;
    m_limit_up_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::is_limit_up_Set() const{
    return m_limit_up_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::is_limit_up_Valid() const{
    return m_limit_up_isValid;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_limit_down_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_limit_up_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_cellular::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
