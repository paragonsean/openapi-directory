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

#include "OAICreateNetworkVlan_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkVlan_request::OAICreateNetworkVlan_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkVlan_request::OAICreateNetworkVlan_request() {
    this->initializeModel();
}

OAICreateNetworkVlan_request::~OAICreateNetworkVlan_request() {}

void OAICreateNetworkVlan_request::initializeModel() {

    m_appliance_ip_isSet = false;
    m_appliance_ip_isValid = false;

    m_group_policy_id_isSet = false;
    m_group_policy_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_subnet_isSet = false;
    m_subnet_isValid = false;
}

void OAICreateNetworkVlan_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkVlan_request::fromJsonObject(QJsonObject json) {

    m_appliance_ip_isValid = ::OpenAPI::fromJsonValue(m_appliance_ip, json[QString("applianceIp")]);
    m_appliance_ip_isSet = !json[QString("applianceIp")].isNull() && m_appliance_ip_isValid;

    m_group_policy_id_isValid = ::OpenAPI::fromJsonValue(m_group_policy_id, json[QString("groupPolicyId")]);
    m_group_policy_id_isSet = !json[QString("groupPolicyId")].isNull() && m_group_policy_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_subnet_isValid = ::OpenAPI::fromJsonValue(m_subnet, json[QString("subnet")]);
    m_subnet_isSet = !json[QString("subnet")].isNull() && m_subnet_isValid;
}

QString OAICreateNetworkVlan_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkVlan_request::asJsonObject() const {
    QJsonObject obj;
    if (m_appliance_ip_isSet) {
        obj.insert(QString("applianceIp"), ::OpenAPI::toJsonValue(m_appliance_ip));
    }
    if (m_group_policy_id_isSet) {
        obj.insert(QString("groupPolicyId"), ::OpenAPI::toJsonValue(m_group_policy_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_subnet_isSet) {
        obj.insert(QString("subnet"), ::OpenAPI::toJsonValue(m_subnet));
    }
    return obj;
}

QString OAICreateNetworkVlan_request::getApplianceIp() const {
    return m_appliance_ip;
}
void OAICreateNetworkVlan_request::setApplianceIp(const QString &appliance_ip) {
    m_appliance_ip = appliance_ip;
    m_appliance_ip_isSet = true;
}

bool OAICreateNetworkVlan_request::is_appliance_ip_Set() const{
    return m_appliance_ip_isSet;
}

bool OAICreateNetworkVlan_request::is_appliance_ip_Valid() const{
    return m_appliance_ip_isValid;
}

QString OAICreateNetworkVlan_request::getGroupPolicyId() const {
    return m_group_policy_id;
}
void OAICreateNetworkVlan_request::setGroupPolicyId(const QString &group_policy_id) {
    m_group_policy_id = group_policy_id;
    m_group_policy_id_isSet = true;
}

bool OAICreateNetworkVlan_request::is_group_policy_id_Set() const{
    return m_group_policy_id_isSet;
}

bool OAICreateNetworkVlan_request::is_group_policy_id_Valid() const{
    return m_group_policy_id_isValid;
}

QString OAICreateNetworkVlan_request::getId() const {
    return m_id;
}
void OAICreateNetworkVlan_request::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICreateNetworkVlan_request::is_id_Set() const{
    return m_id_isSet;
}

bool OAICreateNetworkVlan_request::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICreateNetworkVlan_request::getName() const {
    return m_name;
}
void OAICreateNetworkVlan_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateNetworkVlan_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateNetworkVlan_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICreateNetworkVlan_request::getSubnet() const {
    return m_subnet;
}
void OAICreateNetworkVlan_request::setSubnet(const QString &subnet) {
    m_subnet = subnet;
    m_subnet_isSet = true;
}

bool OAICreateNetworkVlan_request::is_subnet_Set() const{
    return m_subnet_isSet;
}

bool OAICreateNetworkVlan_request::is_subnet_Valid() const{
    return m_subnet_isValid;
}

bool OAICreateNetworkVlan_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appliance_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_policy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subnet_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNetworkVlan_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_appliance_ip_isValid && m_id_isValid && m_name_isValid && m_subnet_isValid && true;
}

} // namespace OpenAPI
