/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFailoverServer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFailoverServer::OAIFailoverServer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFailoverServer::OAIFailoverServer() {
    this->initializeModel();
}

OAIFailoverServer::~OAIFailoverServer() {}

void OAIFailoverServer::initializeModel() {

    m_failover_enabled_isSet = false;
    m_failover_enabled_isValid = false;

    m_failover_ip_address_isSet = false;
    m_failover_ip_address_isValid = false;

    m_failover_port_isSet = false;
    m_failover_port_isValid = false;
}

void OAIFailoverServer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFailoverServer::fromJsonObject(QJsonObject json) {

    m_failover_enabled_isValid = ::OpenAPI::fromJsonValue(m_failover_enabled, json[QString("failoverEnabled")]);
    m_failover_enabled_isSet = !json[QString("failoverEnabled")].isNull() && m_failover_enabled_isValid;

    m_failover_ip_address_isValid = ::OpenAPI::fromJsonValue(m_failover_ip_address, json[QString("failoverIpAddress")]);
    m_failover_ip_address_isSet = !json[QString("failoverIpAddress")].isNull() && m_failover_ip_address_isValid;

    m_failover_port_isValid = ::OpenAPI::fromJsonValue(m_failover_port, json[QString("failoverPort")]);
    m_failover_port_isSet = !json[QString("failoverPort")].isNull() && m_failover_port_isValid;
}

QString OAIFailoverServer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFailoverServer::asJsonObject() const {
    QJsonObject obj;
    if (m_failover_enabled_isSet) {
        obj.insert(QString("failoverEnabled"), ::OpenAPI::toJsonValue(m_failover_enabled));
    }
    if (m_failover_ip_address_isSet) {
        obj.insert(QString("failoverIpAddress"), ::OpenAPI::toJsonValue(m_failover_ip_address));
    }
    if (m_failover_port_isSet) {
        obj.insert(QString("failoverPort"), ::OpenAPI::toJsonValue(m_failover_port));
    }
    return obj;
}

bool OAIFailoverServer::isFailoverEnabled() const {
    return m_failover_enabled;
}
void OAIFailoverServer::setFailoverEnabled(const bool &failover_enabled) {
    m_failover_enabled = failover_enabled;
    m_failover_enabled_isSet = true;
}

bool OAIFailoverServer::is_failover_enabled_Set() const{
    return m_failover_enabled_isSet;
}

bool OAIFailoverServer::is_failover_enabled_Valid() const{
    return m_failover_enabled_isValid;
}

QString OAIFailoverServer::getFailoverIpAddress() const {
    return m_failover_ip_address;
}
void OAIFailoverServer::setFailoverIpAddress(const QString &failover_ip_address) {
    m_failover_ip_address = failover_ip_address;
    m_failover_ip_address_isSet = true;
}

bool OAIFailoverServer::is_failover_ip_address_Set() const{
    return m_failover_ip_address_isSet;
}

bool OAIFailoverServer::is_failover_ip_address_Valid() const{
    return m_failover_ip_address_isValid;
}

qint32 OAIFailoverServer::getFailoverPort() const {
    return m_failover_port;
}
void OAIFailoverServer::setFailoverPort(const qint32 &failover_port) {
    m_failover_port = failover_port;
    m_failover_port_isSet = true;
}

bool OAIFailoverServer::is_failover_port_Set() const{
    return m_failover_port_isSet;
}

bool OAIFailoverServer::is_failover_port_Valid() const{
    return m_failover_port_isValid;
}

bool OAIFailoverServer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_failover_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_failover_ip_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_failover_port_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFailoverServer::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_failover_enabled_isValid && m_failover_ip_address_isValid && m_failover_port_isValid && true;
}

} // namespace OpenAPI
