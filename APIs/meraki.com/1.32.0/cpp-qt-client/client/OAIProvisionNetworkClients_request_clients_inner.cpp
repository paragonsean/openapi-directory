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

#include "OAIProvisionNetworkClients_request_clients_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProvisionNetworkClients_request_clients_inner::OAIProvisionNetworkClients_request_clients_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProvisionNetworkClients_request_clients_inner::OAIProvisionNetworkClients_request_clients_inner() {
    this->initializeModel();
}

OAIProvisionNetworkClients_request_clients_inner::~OAIProvisionNetworkClients_request_clients_inner() {}

void OAIProvisionNetworkClients_request_clients_inner::initializeModel() {

    m_mac_isSet = false;
    m_mac_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIProvisionNetworkClients_request_clients_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProvisionNetworkClients_request_clients_inner::fromJsonObject(QJsonObject json) {

    m_mac_isValid = ::OpenAPI::fromJsonValue(m_mac, json[QString("mac")]);
    m_mac_isSet = !json[QString("mac")].isNull() && m_mac_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIProvisionNetworkClients_request_clients_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProvisionNetworkClients_request_clients_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_mac_isSet) {
        obj.insert(QString("mac"), ::OpenAPI::toJsonValue(m_mac));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIProvisionNetworkClients_request_clients_inner::getMac() const {
    return m_mac;
}
void OAIProvisionNetworkClients_request_clients_inner::setMac(const QString &mac) {
    m_mac = mac;
    m_mac_isSet = true;
}

bool OAIProvisionNetworkClients_request_clients_inner::is_mac_Set() const{
    return m_mac_isSet;
}

bool OAIProvisionNetworkClients_request_clients_inner::is_mac_Valid() const{
    return m_mac_isValid;
}

QString OAIProvisionNetworkClients_request_clients_inner::getName() const {
    return m_name;
}
void OAIProvisionNetworkClients_request_clients_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProvisionNetworkClients_request_clients_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProvisionNetworkClients_request_clients_inner::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIProvisionNetworkClients_request_clients_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_mac_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProvisionNetworkClients_request_clients_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_mac_isValid && true;
}

} // namespace OpenAPI
