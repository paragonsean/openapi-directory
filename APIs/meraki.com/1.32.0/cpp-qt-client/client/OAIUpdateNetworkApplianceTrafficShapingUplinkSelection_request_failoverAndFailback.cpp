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

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::~OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback() {}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::initializeModel() {

    m_immediate_isSet = false;
    m_immediate_isValid = false;
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::fromJsonObject(QJsonObject json) {

    m_immediate_isValid = ::OpenAPI::fromJsonValue(m_immediate, json[QString("immediate")]);
    m_immediate_isSet = !json[QString("immediate")].isNull() && m_immediate_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::asJsonObject() const {
    QJsonObject obj;
    if (m_immediate.isSet()) {
        obj.insert(QString("immediate"), ::OpenAPI::toJsonValue(m_immediate));
    }
    return obj;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback_immediate OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::getImmediate() const {
    return m_immediate;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::setImmediate(const OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback_immediate &immediate) {
    m_immediate = immediate;
    m_immediate_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::is_immediate_Set() const{
    return m_immediate_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::is_immediate_Valid() const{
    return m_immediate_isValid;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_immediate.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_failoverAndFailback::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
