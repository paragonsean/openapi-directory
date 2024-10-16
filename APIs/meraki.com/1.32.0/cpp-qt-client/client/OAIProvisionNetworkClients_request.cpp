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

#include "OAIProvisionNetworkClients_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProvisionNetworkClients_request::OAIProvisionNetworkClients_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProvisionNetworkClients_request::OAIProvisionNetworkClients_request() {
    this->initializeModel();
}

OAIProvisionNetworkClients_request::~OAIProvisionNetworkClients_request() {}

void OAIProvisionNetworkClients_request::initializeModel() {

    m_clients_isSet = false;
    m_clients_isValid = false;

    m_device_policy_isSet = false;
    m_device_policy_isValid = false;

    m_group_policy_id_isSet = false;
    m_group_policy_id_isValid = false;

    m_policies_by_security_appliance_isSet = false;
    m_policies_by_security_appliance_isValid = false;

    m_policies_by_ssid_isSet = false;
    m_policies_by_ssid_isValid = false;
}

void OAIProvisionNetworkClients_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProvisionNetworkClients_request::fromJsonObject(QJsonObject json) {

    m_clients_isValid = ::OpenAPI::fromJsonValue(m_clients, json[QString("clients")]);
    m_clients_isSet = !json[QString("clients")].isNull() && m_clients_isValid;

    m_device_policy_isValid = ::OpenAPI::fromJsonValue(m_device_policy, json[QString("devicePolicy")]);
    m_device_policy_isSet = !json[QString("devicePolicy")].isNull() && m_device_policy_isValid;

    m_group_policy_id_isValid = ::OpenAPI::fromJsonValue(m_group_policy_id, json[QString("groupPolicyId")]);
    m_group_policy_id_isSet = !json[QString("groupPolicyId")].isNull() && m_group_policy_id_isValid;

    m_policies_by_security_appliance_isValid = ::OpenAPI::fromJsonValue(m_policies_by_security_appliance, json[QString("policiesBySecurityAppliance")]);
    m_policies_by_security_appliance_isSet = !json[QString("policiesBySecurityAppliance")].isNull() && m_policies_by_security_appliance_isValid;

    m_policies_by_ssid_isValid = ::OpenAPI::fromJsonValue(m_policies_by_ssid, json[QString("policiesBySsid")]);
    m_policies_by_ssid_isSet = !json[QString("policiesBySsid")].isNull() && m_policies_by_ssid_isValid;
}

QString OAIProvisionNetworkClients_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProvisionNetworkClients_request::asJsonObject() const {
    QJsonObject obj;
    if (m_clients.size() > 0) {
        obj.insert(QString("clients"), ::OpenAPI::toJsonValue(m_clients));
    }
    if (m_device_policy_isSet) {
        obj.insert(QString("devicePolicy"), ::OpenAPI::toJsonValue(m_device_policy));
    }
    if (m_group_policy_id_isSet) {
        obj.insert(QString("groupPolicyId"), ::OpenAPI::toJsonValue(m_group_policy_id));
    }
    if (m_policies_by_security_appliance.isSet()) {
        obj.insert(QString("policiesBySecurityAppliance"), ::OpenAPI::toJsonValue(m_policies_by_security_appliance));
    }
    if (m_policies_by_ssid.isSet()) {
        obj.insert(QString("policiesBySsid"), ::OpenAPI::toJsonValue(m_policies_by_ssid));
    }
    return obj;
}

QList<OAIProvisionNetworkClients_request_clients_inner> OAIProvisionNetworkClients_request::getClients() const {
    return m_clients;
}
void OAIProvisionNetworkClients_request::setClients(const QList<OAIProvisionNetworkClients_request_clients_inner> &clients) {
    m_clients = clients;
    m_clients_isSet = true;
}

bool OAIProvisionNetworkClients_request::is_clients_Set() const{
    return m_clients_isSet;
}

bool OAIProvisionNetworkClients_request::is_clients_Valid() const{
    return m_clients_isValid;
}

QString OAIProvisionNetworkClients_request::getDevicePolicy() const {
    return m_device_policy;
}
void OAIProvisionNetworkClients_request::setDevicePolicy(const QString &device_policy) {
    m_device_policy = device_policy;
    m_device_policy_isSet = true;
}

bool OAIProvisionNetworkClients_request::is_device_policy_Set() const{
    return m_device_policy_isSet;
}

bool OAIProvisionNetworkClients_request::is_device_policy_Valid() const{
    return m_device_policy_isValid;
}

QString OAIProvisionNetworkClients_request::getGroupPolicyId() const {
    return m_group_policy_id;
}
void OAIProvisionNetworkClients_request::setGroupPolicyId(const QString &group_policy_id) {
    m_group_policy_id = group_policy_id;
    m_group_policy_id_isSet = true;
}

bool OAIProvisionNetworkClients_request::is_group_policy_id_Set() const{
    return m_group_policy_id_isSet;
}

bool OAIProvisionNetworkClients_request::is_group_policy_id_Valid() const{
    return m_group_policy_id_isValid;
}

OAIProvisionNetworkClients_request_policiesBySecurityAppliance OAIProvisionNetworkClients_request::getPoliciesBySecurityAppliance() const {
    return m_policies_by_security_appliance;
}
void OAIProvisionNetworkClients_request::setPoliciesBySecurityAppliance(const OAIProvisionNetworkClients_request_policiesBySecurityAppliance &policies_by_security_appliance) {
    m_policies_by_security_appliance = policies_by_security_appliance;
    m_policies_by_security_appliance_isSet = true;
}

bool OAIProvisionNetworkClients_request::is_policies_by_security_appliance_Set() const{
    return m_policies_by_security_appliance_isSet;
}

bool OAIProvisionNetworkClients_request::is_policies_by_security_appliance_Valid() const{
    return m_policies_by_security_appliance_isValid;
}

OAIProvisionNetworkClients_request_policiesBySsid OAIProvisionNetworkClients_request::getPoliciesBySsid() const {
    return m_policies_by_ssid;
}
void OAIProvisionNetworkClients_request::setPoliciesBySsid(const OAIProvisionNetworkClients_request_policiesBySsid &policies_by_ssid) {
    m_policies_by_ssid = policies_by_ssid;
    m_policies_by_ssid_isSet = true;
}

bool OAIProvisionNetworkClients_request::is_policies_by_ssid_Set() const{
    return m_policies_by_ssid_isSet;
}

bool OAIProvisionNetworkClients_request::is_policies_by_ssid_Valid() const{
    return m_policies_by_ssid_isValid;
}

bool OAIProvisionNetworkClients_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_clients.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_policy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_policy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_policies_by_security_appliance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_policies_by_ssid.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProvisionNetworkClients_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_clients_isValid && m_device_policy_isValid && true;
}

} // namespace OpenAPI
