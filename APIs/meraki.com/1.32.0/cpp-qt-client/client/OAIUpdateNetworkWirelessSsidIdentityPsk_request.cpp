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

#include "OAIUpdateNetworkWirelessSsidIdentityPsk_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessSsidIdentityPsk_request::OAIUpdateNetworkWirelessSsidIdentityPsk_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessSsidIdentityPsk_request::OAIUpdateNetworkWirelessSsidIdentityPsk_request() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessSsidIdentityPsk_request::~OAIUpdateNetworkWirelessSsidIdentityPsk_request() {}

void OAIUpdateNetworkWirelessSsidIdentityPsk_request::initializeModel() {

    m_group_policy_id_isSet = false;
    m_group_policy_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_passphrase_isSet = false;
    m_passphrase_isValid = false;
}

void OAIUpdateNetworkWirelessSsidIdentityPsk_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessSsidIdentityPsk_request::fromJsonObject(QJsonObject json) {

    m_group_policy_id_isValid = ::OpenAPI::fromJsonValue(m_group_policy_id, json[QString("groupPolicyId")]);
    m_group_policy_id_isSet = !json[QString("groupPolicyId")].isNull() && m_group_policy_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_passphrase_isValid = ::OpenAPI::fromJsonValue(m_passphrase, json[QString("passphrase")]);
    m_passphrase_isSet = !json[QString("passphrase")].isNull() && m_passphrase_isValid;
}

QString OAIUpdateNetworkWirelessSsidIdentityPsk_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessSsidIdentityPsk_request::asJsonObject() const {
    QJsonObject obj;
    if (m_group_policy_id_isSet) {
        obj.insert(QString("groupPolicyId"), ::OpenAPI::toJsonValue(m_group_policy_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_passphrase_isSet) {
        obj.insert(QString("passphrase"), ::OpenAPI::toJsonValue(m_passphrase));
    }
    return obj;
}

QString OAIUpdateNetworkWirelessSsidIdentityPsk_request::getGroupPolicyId() const {
    return m_group_policy_id;
}
void OAIUpdateNetworkWirelessSsidIdentityPsk_request::setGroupPolicyId(const QString &group_policy_id) {
    m_group_policy_id = group_policy_id;
    m_group_policy_id_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::is_group_policy_id_Set() const{
    return m_group_policy_id_isSet;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::is_group_policy_id_Valid() const{
    return m_group_policy_id_isValid;
}

QString OAIUpdateNetworkWirelessSsidIdentityPsk_request::getName() const {
    return m_name;
}
void OAIUpdateNetworkWirelessSsidIdentityPsk_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIUpdateNetworkWirelessSsidIdentityPsk_request::getPassphrase() const {
    return m_passphrase;
}
void OAIUpdateNetworkWirelessSsidIdentityPsk_request::setPassphrase(const QString &passphrase) {
    m_passphrase = passphrase;
    m_passphrase_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::is_passphrase_Set() const{
    return m_passphrase_isSet;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::is_passphrase_Valid() const{
    return m_passphrase_isValid;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_group_policy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passphrase_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWirelessSsidIdentityPsk_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
