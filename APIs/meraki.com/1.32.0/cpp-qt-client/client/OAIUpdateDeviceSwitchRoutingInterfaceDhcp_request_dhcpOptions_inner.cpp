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

#include "OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner() {
    this->initializeModel();
}

OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::~OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner() {}

void OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::getCode() const {
    return m_code;
}
void OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::is_code_Set() const{
    return m_code_isSet;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::getType() const {
    return m_type;
}
void OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::getValue() const {
    return m_value;
}
void OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDeviceSwitchRoutingInterfaceDhcp_request_dhcpOptions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_type_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
