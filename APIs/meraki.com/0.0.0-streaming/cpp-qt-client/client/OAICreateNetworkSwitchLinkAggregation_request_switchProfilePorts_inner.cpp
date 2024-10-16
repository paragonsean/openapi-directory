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

#include "OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner() {
    this->initializeModel();
}

OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::~OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner() {}

void OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::initializeModel() {

    m_port_id_isSet = false;
    m_port_id_isValid = false;

    m_profile_isSet = false;
    m_profile_isValid = false;
}

void OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::fromJsonObject(QJsonObject json) {

    m_port_id_isValid = ::OpenAPI::fromJsonValue(m_port_id, json[QString("portId")]);
    m_port_id_isSet = !json[QString("portId")].isNull() && m_port_id_isValid;

    m_profile_isValid = ::OpenAPI::fromJsonValue(m_profile, json[QString("profile")]);
    m_profile_isSet = !json[QString("profile")].isNull() && m_profile_isValid;
}

QString OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_port_id_isSet) {
        obj.insert(QString("portId"), ::OpenAPI::toJsonValue(m_port_id));
    }
    if (m_profile_isSet) {
        obj.insert(QString("profile"), ::OpenAPI::toJsonValue(m_profile));
    }
    return obj;
}

QString OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::getPortId() const {
    return m_port_id;
}
void OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::setPortId(const QString &port_id) {
    m_port_id = port_id;
    m_port_id_isSet = true;
}

bool OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::is_port_id_Set() const{
    return m_port_id_isSet;
}

bool OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::is_port_id_Valid() const{
    return m_port_id_isValid;
}

QString OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::getProfile() const {
    return m_profile;
}
void OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::setProfile(const QString &profile) {
    m_profile = profile;
    m_profile_isSet = true;
}

bool OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::is_profile_Set() const{
    return m_profile_isSet;
}

bool OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::is_profile_Valid() const{
    return m_profile_isValid;
}

bool OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_port_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNetworkSwitchLinkAggregation_request_switchProfilePorts_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_port_id_isValid && m_profile_isValid && true;
}

} // namespace OpenAPI
