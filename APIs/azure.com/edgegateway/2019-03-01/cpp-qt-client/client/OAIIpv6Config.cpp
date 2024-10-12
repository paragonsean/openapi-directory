/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIpv6Config.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIpv6Config::OAIIpv6Config(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIpv6Config::OAIIpv6Config() {
    this->initializeModel();
}

OAIIpv6Config::~OAIIpv6Config() {}

void OAIIpv6Config::initializeModel() {

    m_gateway_isSet = false;
    m_gateway_isValid = false;

    m_ip_address_isSet = false;
    m_ip_address_isValid = false;

    m_prefix_length_isSet = false;
    m_prefix_length_isValid = false;
}

void OAIIpv6Config::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIpv6Config::fromJsonObject(QJsonObject json) {

    m_gateway_isValid = ::OpenAPI::fromJsonValue(m_gateway, json[QString("gateway")]);
    m_gateway_isSet = !json[QString("gateway")].isNull() && m_gateway_isValid;

    m_ip_address_isValid = ::OpenAPI::fromJsonValue(m_ip_address, json[QString("ipAddress")]);
    m_ip_address_isSet = !json[QString("ipAddress")].isNull() && m_ip_address_isValid;

    m_prefix_length_isValid = ::OpenAPI::fromJsonValue(m_prefix_length, json[QString("prefixLength")]);
    m_prefix_length_isSet = !json[QString("prefixLength")].isNull() && m_prefix_length_isValid;
}

QString OAIIpv6Config::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIpv6Config::asJsonObject() const {
    QJsonObject obj;
    if (m_gateway_isSet) {
        obj.insert(QString("gateway"), ::OpenAPI::toJsonValue(m_gateway));
    }
    if (m_ip_address_isSet) {
        obj.insert(QString("ipAddress"), ::OpenAPI::toJsonValue(m_ip_address));
    }
    if (m_prefix_length_isSet) {
        obj.insert(QString("prefixLength"), ::OpenAPI::toJsonValue(m_prefix_length));
    }
    return obj;
}

QString OAIIpv6Config::getGateway() const {
    return m_gateway;
}
void OAIIpv6Config::setGateway(const QString &gateway) {
    m_gateway = gateway;
    m_gateway_isSet = true;
}

bool OAIIpv6Config::is_gateway_Set() const{
    return m_gateway_isSet;
}

bool OAIIpv6Config::is_gateway_Valid() const{
    return m_gateway_isValid;
}

QString OAIIpv6Config::getIpAddress() const {
    return m_ip_address;
}
void OAIIpv6Config::setIpAddress(const QString &ip_address) {
    m_ip_address = ip_address;
    m_ip_address_isSet = true;
}

bool OAIIpv6Config::is_ip_address_Set() const{
    return m_ip_address_isSet;
}

bool OAIIpv6Config::is_ip_address_Valid() const{
    return m_ip_address_isValid;
}

qint32 OAIIpv6Config::getPrefixLength() const {
    return m_prefix_length;
}
void OAIIpv6Config::setPrefixLength(const qint32 &prefix_length) {
    m_prefix_length = prefix_length;
    m_prefix_length_isSet = true;
}

bool OAIIpv6Config::is_prefix_length_Set() const{
    return m_prefix_length_isSet;
}

bool OAIIpv6Config::is_prefix_length_Valid() const{
    return m_prefix_length_isValid;
}

bool OAIIpv6Config::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gateway_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prefix_length_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIpv6Config::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
