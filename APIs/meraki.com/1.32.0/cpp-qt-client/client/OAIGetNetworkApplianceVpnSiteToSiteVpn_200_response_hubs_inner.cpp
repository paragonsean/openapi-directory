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

#include "OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner() {
    this->initializeModel();
}

OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::~OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner() {}

void OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::initializeModel() {

    m_hub_id_isSet = false;
    m_hub_id_isValid = false;

    m_use_default_route_isSet = false;
    m_use_default_route_isValid = false;
}

void OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::fromJsonObject(QJsonObject json) {

    m_hub_id_isValid = ::OpenAPI::fromJsonValue(m_hub_id, json[QString("hubId")]);
    m_hub_id_isSet = !json[QString("hubId")].isNull() && m_hub_id_isValid;

    m_use_default_route_isValid = ::OpenAPI::fromJsonValue(m_use_default_route, json[QString("useDefaultRoute")]);
    m_use_default_route_isSet = !json[QString("useDefaultRoute")].isNull() && m_use_default_route_isValid;
}

QString OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_hub_id_isSet) {
        obj.insert(QString("hubId"), ::OpenAPI::toJsonValue(m_hub_id));
    }
    if (m_use_default_route_isSet) {
        obj.insert(QString("useDefaultRoute"), ::OpenAPI::toJsonValue(m_use_default_route));
    }
    return obj;
}

QString OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::getHubId() const {
    return m_hub_id;
}
void OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::setHubId(const QString &hub_id) {
    m_hub_id = hub_id;
    m_hub_id_isSet = true;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::is_hub_id_Set() const{
    return m_hub_id_isSet;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::is_hub_id_Valid() const{
    return m_hub_id_isValid;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::isUseDefaultRoute() const {
    return m_use_default_route;
}
void OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::setUseDefaultRoute(const bool &use_default_route) {
    m_use_default_route = use_default_route;
    m_use_default_route_isSet = true;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::is_use_default_route_Set() const{
    return m_use_default_route_isSet;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::is_use_default_route_Valid() const{
    return m_use_default_route_isValid;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hub_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_default_route_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
