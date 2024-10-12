/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRedisFirewallRuleCreateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRedisFirewallRuleCreateParameters::OAIRedisFirewallRuleCreateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRedisFirewallRuleCreateParameters::OAIRedisFirewallRuleCreateParameters() {
    this->initializeModel();
}

OAIRedisFirewallRuleCreateParameters::~OAIRedisFirewallRuleCreateParameters() {}

void OAIRedisFirewallRuleCreateParameters::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIRedisFirewallRuleCreateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRedisFirewallRuleCreateParameters::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIRedisFirewallRuleCreateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRedisFirewallRuleCreateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIRedisFirewallRuleProperties OAIRedisFirewallRuleCreateParameters::getProperties() const {
    return m_properties;
}
void OAIRedisFirewallRuleCreateParameters::setProperties(const OAIRedisFirewallRuleProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIRedisFirewallRuleCreateParameters::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIRedisFirewallRuleCreateParameters::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIRedisFirewallRuleCreateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRedisFirewallRuleCreateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_properties_isValid && true;
}

} // namespace OpenAPI
