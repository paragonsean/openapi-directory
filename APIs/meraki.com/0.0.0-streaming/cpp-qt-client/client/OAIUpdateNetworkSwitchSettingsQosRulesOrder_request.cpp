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

#include "OAIUpdateNetworkSwitchSettingsQosRulesOrder_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::OAIUpdateNetworkSwitchSettingsQosRulesOrder_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::OAIUpdateNetworkSwitchSettingsQosRulesOrder_request() {
    this->initializeModel();
}

OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::~OAIUpdateNetworkSwitchSettingsQosRulesOrder_request() {}

void OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::initializeModel() {

    m_rule_ids_isSet = false;
    m_rule_ids_isValid = false;
}

void OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::fromJsonObject(QJsonObject json) {

    m_rule_ids_isValid = ::OpenAPI::fromJsonValue(m_rule_ids, json[QString("ruleIds")]);
    m_rule_ids_isSet = !json[QString("ruleIds")].isNull() && m_rule_ids_isValid;
}

QString OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::asJsonObject() const {
    QJsonObject obj;
    if (m_rule_ids.size() > 0) {
        obj.insert(QString("ruleIds"), ::OpenAPI::toJsonValue(m_rule_ids));
    }
    return obj;
}

QList<QString> OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::getRuleIds() const {
    return m_rule_ids;
}
void OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::setRuleIds(const QList<QString> &rule_ids) {
    m_rule_ids = rule_ids;
    m_rule_ids_isSet = true;
}

bool OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::is_rule_ids_Set() const{
    return m_rule_ids_isSet;
}

bool OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::is_rule_ids_Valid() const{
    return m_rule_ids_isValid;
}

bool OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_rule_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSwitchSettingsQosRulesOrder_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_rule_ids_isValid && true;
}

} // namespace OpenAPI
