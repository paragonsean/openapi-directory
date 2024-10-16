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

#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams() {
    this->initializeModel();
}

OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::~OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams() {}

void OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::initializeModel() {

    m_cloud_static_ip_isSet = false;
    m_cloud_static_ip_isValid = false;

    m_tunnel_isSet = false;
    m_tunnel_isValid = false;

    m_user_isSet = false;
    m_user_isValid = false;
}

void OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::fromJsonObject(QJsonObject json) {

    m_cloud_static_ip_isValid = ::OpenAPI::fromJsonValue(m_cloud_static_ip, json[QString("cloudStaticIp")]);
    m_cloud_static_ip_isSet = !json[QString("cloudStaticIp")].isNull() && m_cloud_static_ip_isValid;

    m_tunnel_isValid = ::OpenAPI::fromJsonValue(m_tunnel, json[QString("tunnel")]);
    m_tunnel_isSet = !json[QString("tunnel")].isNull() && m_tunnel_isValid;

    m_user_isValid = ::OpenAPI::fromJsonValue(m_user, json[QString("user")]);
    m_user_isSet = !json[QString("user")].isNull() && m_user_isValid;
}

QString OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::asJsonObject() const {
    QJsonObject obj;
    if (m_cloud_static_ip_isSet) {
        obj.insert(QString("cloudStaticIp"), ::OpenAPI::toJsonValue(m_cloud_static_ip));
    }
    if (m_tunnel.isSet()) {
        obj.insert(QString("tunnel"), ::OpenAPI::toJsonValue(m_tunnel));
    }
    if (m_user.isSet()) {
        obj.insert(QString("user"), ::OpenAPI::toJsonValue(m_user));
    }
    return obj;
}

QString OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::getCloudStaticIp() const {
    return m_cloud_static_ip;
}
void OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::setCloudStaticIp(const QString &cloud_static_ip) {
    m_cloud_static_ip = cloud_static_ip;
    m_cloud_static_ip_isSet = true;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::is_cloud_static_ip_Set() const{
    return m_cloud_static_ip_isSet;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::is_cloud_static_ip_Valid() const{
    return m_cloud_static_ip_isValid;
}

OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::getTunnel() const {
    return m_tunnel;
}
void OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::setTunnel(const OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel &tunnel) {
    m_tunnel = tunnel;
    m_tunnel_isSet = true;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::is_tunnel_Set() const{
    return m_tunnel_isSet;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::is_tunnel_Valid() const{
    return m_tunnel_isValid;
}

OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_user OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::getUser() const {
    return m_user;
}
void OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::setUser(const OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_user &user) {
    m_user = user;
    m_user_isSet = true;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::is_user_Set() const{
    return m_user_isSet;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::is_user_Valid() const{
    return m_user_isValid;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cloud_static_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tunnel.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
