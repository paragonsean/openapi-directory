/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAzureFirewallFqdnTagPropertiesFormat.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAzureFirewallFqdnTagPropertiesFormat::OAIAzureFirewallFqdnTagPropertiesFormat(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAzureFirewallFqdnTagPropertiesFormat::OAIAzureFirewallFqdnTagPropertiesFormat() {
    this->initializeModel();
}

OAIAzureFirewallFqdnTagPropertiesFormat::~OAIAzureFirewallFqdnTagPropertiesFormat() {}

void OAIAzureFirewallFqdnTagPropertiesFormat::initializeModel() {

    m_fqdn_tag_name_isSet = false;
    m_fqdn_tag_name_isValid = false;

    m_provisioning_state_isSet = false;
    m_provisioning_state_isValid = false;
}

void OAIAzureFirewallFqdnTagPropertiesFormat::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAzureFirewallFqdnTagPropertiesFormat::fromJsonObject(QJsonObject json) {

    m_fqdn_tag_name_isValid = ::OpenAPI::fromJsonValue(m_fqdn_tag_name, json[QString("fqdnTagName")]);
    m_fqdn_tag_name_isSet = !json[QString("fqdnTagName")].isNull() && m_fqdn_tag_name_isValid;

    m_provisioning_state_isValid = ::OpenAPI::fromJsonValue(m_provisioning_state, json[QString("provisioningState")]);
    m_provisioning_state_isSet = !json[QString("provisioningState")].isNull() && m_provisioning_state_isValid;
}

QString OAIAzureFirewallFqdnTagPropertiesFormat::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAzureFirewallFqdnTagPropertiesFormat::asJsonObject() const {
    QJsonObject obj;
    if (m_fqdn_tag_name_isSet) {
        obj.insert(QString("fqdnTagName"), ::OpenAPI::toJsonValue(m_fqdn_tag_name));
    }
    if (m_provisioning_state_isSet) {
        obj.insert(QString("provisioningState"), ::OpenAPI::toJsonValue(m_provisioning_state));
    }
    return obj;
}

QString OAIAzureFirewallFqdnTagPropertiesFormat::getFqdnTagName() const {
    return m_fqdn_tag_name;
}
void OAIAzureFirewallFqdnTagPropertiesFormat::setFqdnTagName(const QString &fqdn_tag_name) {
    m_fqdn_tag_name = fqdn_tag_name;
    m_fqdn_tag_name_isSet = true;
}

bool OAIAzureFirewallFqdnTagPropertiesFormat::is_fqdn_tag_name_Set() const{
    return m_fqdn_tag_name_isSet;
}

bool OAIAzureFirewallFqdnTagPropertiesFormat::is_fqdn_tag_name_Valid() const{
    return m_fqdn_tag_name_isValid;
}

QString OAIAzureFirewallFqdnTagPropertiesFormat::getProvisioningState() const {
    return m_provisioning_state;
}
void OAIAzureFirewallFqdnTagPropertiesFormat::setProvisioningState(const QString &provisioning_state) {
    m_provisioning_state = provisioning_state;
    m_provisioning_state_isSet = true;
}

bool OAIAzureFirewallFqdnTagPropertiesFormat::is_provisioning_state_Set() const{
    return m_provisioning_state_isSet;
}

bool OAIAzureFirewallFqdnTagPropertiesFormat::is_provisioning_state_Valid() const{
    return m_provisioning_state_isValid;
}

bool OAIAzureFirewallFqdnTagPropertiesFormat::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fqdn_tag_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAzureFirewallFqdnTagPropertiesFormat::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
