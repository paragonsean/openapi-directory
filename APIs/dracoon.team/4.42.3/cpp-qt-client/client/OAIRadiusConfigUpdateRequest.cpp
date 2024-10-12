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

#include "OAIRadiusConfigUpdateRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRadiusConfigUpdateRequest::OAIRadiusConfigUpdateRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRadiusConfigUpdateRequest::OAIRadiusConfigUpdateRequest() {
    this->initializeModel();
}

OAIRadiusConfigUpdateRequest::~OAIRadiusConfigUpdateRequest() {}

void OAIRadiusConfigUpdateRequest::initializeModel() {

    m_failover_server_isSet = false;
    m_failover_server_isValid = false;

    m_ip_address_isSet = false;
    m_ip_address_isValid = false;

    m_otp_pin_first_isSet = false;
    m_otp_pin_first_isValid = false;

    m_port_isSet = false;
    m_port_isValid = false;

    m_shared_secret_isSet = false;
    m_shared_secret_isValid = false;
}

void OAIRadiusConfigUpdateRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRadiusConfigUpdateRequest::fromJsonObject(QJsonObject json) {

    m_failover_server_isValid = ::OpenAPI::fromJsonValue(m_failover_server, json[QString("failoverServer")]);
    m_failover_server_isSet = !json[QString("failoverServer")].isNull() && m_failover_server_isValid;

    m_ip_address_isValid = ::OpenAPI::fromJsonValue(m_ip_address, json[QString("ipAddress")]);
    m_ip_address_isSet = !json[QString("ipAddress")].isNull() && m_ip_address_isValid;

    m_otp_pin_first_isValid = ::OpenAPI::fromJsonValue(m_otp_pin_first, json[QString("otpPinFirst")]);
    m_otp_pin_first_isSet = !json[QString("otpPinFirst")].isNull() && m_otp_pin_first_isValid;

    m_port_isValid = ::OpenAPI::fromJsonValue(m_port, json[QString("port")]);
    m_port_isSet = !json[QString("port")].isNull() && m_port_isValid;

    m_shared_secret_isValid = ::OpenAPI::fromJsonValue(m_shared_secret, json[QString("sharedSecret")]);
    m_shared_secret_isSet = !json[QString("sharedSecret")].isNull() && m_shared_secret_isValid;
}

QString OAIRadiusConfigUpdateRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRadiusConfigUpdateRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_failover_server.isSet()) {
        obj.insert(QString("failoverServer"), ::OpenAPI::toJsonValue(m_failover_server));
    }
    if (m_ip_address_isSet) {
        obj.insert(QString("ipAddress"), ::OpenAPI::toJsonValue(m_ip_address));
    }
    if (m_otp_pin_first_isSet) {
        obj.insert(QString("otpPinFirst"), ::OpenAPI::toJsonValue(m_otp_pin_first));
    }
    if (m_port_isSet) {
        obj.insert(QString("port"), ::OpenAPI::toJsonValue(m_port));
    }
    if (m_shared_secret_isSet) {
        obj.insert(QString("sharedSecret"), ::OpenAPI::toJsonValue(m_shared_secret));
    }
    return obj;
}

OAIFailoverServer OAIRadiusConfigUpdateRequest::getFailoverServer() const {
    return m_failover_server;
}
void OAIRadiusConfigUpdateRequest::setFailoverServer(const OAIFailoverServer &failover_server) {
    m_failover_server = failover_server;
    m_failover_server_isSet = true;
}

bool OAIRadiusConfigUpdateRequest::is_failover_server_Set() const{
    return m_failover_server_isSet;
}

bool OAIRadiusConfigUpdateRequest::is_failover_server_Valid() const{
    return m_failover_server_isValid;
}

QString OAIRadiusConfigUpdateRequest::getIpAddress() const {
    return m_ip_address;
}
void OAIRadiusConfigUpdateRequest::setIpAddress(const QString &ip_address) {
    m_ip_address = ip_address;
    m_ip_address_isSet = true;
}

bool OAIRadiusConfigUpdateRequest::is_ip_address_Set() const{
    return m_ip_address_isSet;
}

bool OAIRadiusConfigUpdateRequest::is_ip_address_Valid() const{
    return m_ip_address_isValid;
}

bool OAIRadiusConfigUpdateRequest::isOtpPinFirst() const {
    return m_otp_pin_first;
}
void OAIRadiusConfigUpdateRequest::setOtpPinFirst(const bool &otp_pin_first) {
    m_otp_pin_first = otp_pin_first;
    m_otp_pin_first_isSet = true;
}

bool OAIRadiusConfigUpdateRequest::is_otp_pin_first_Set() const{
    return m_otp_pin_first_isSet;
}

bool OAIRadiusConfigUpdateRequest::is_otp_pin_first_Valid() const{
    return m_otp_pin_first_isValid;
}

qint32 OAIRadiusConfigUpdateRequest::getPort() const {
    return m_port;
}
void OAIRadiusConfigUpdateRequest::setPort(const qint32 &port) {
    m_port = port;
    m_port_isSet = true;
}

bool OAIRadiusConfigUpdateRequest::is_port_Set() const{
    return m_port_isSet;
}

bool OAIRadiusConfigUpdateRequest::is_port_Valid() const{
    return m_port_isValid;
}

QString OAIRadiusConfigUpdateRequest::getSharedSecret() const {
    return m_shared_secret;
}
void OAIRadiusConfigUpdateRequest::setSharedSecret(const QString &shared_secret) {
    m_shared_secret = shared_secret;
    m_shared_secret_isSet = true;
}

bool OAIRadiusConfigUpdateRequest::is_shared_secret_Set() const{
    return m_shared_secret_isSet;
}

bool OAIRadiusConfigUpdateRequest::is_shared_secret_Valid() const{
    return m_shared_secret_isValid;
}

bool OAIRadiusConfigUpdateRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_failover_server.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_otp_pin_first_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_port_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shared_secret_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRadiusConfigUpdateRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
