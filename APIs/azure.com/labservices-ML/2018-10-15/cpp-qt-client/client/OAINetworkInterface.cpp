/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINetworkInterface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINetworkInterface::OAINetworkInterface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINetworkInterface::OAINetworkInterface() {
    this->initializeModel();
}

OAINetworkInterface::~OAINetworkInterface() {}

void OAINetworkInterface::initializeModel() {

    m_private_ip_address_isSet = false;
    m_private_ip_address_isValid = false;

    m_rdp_authority_isSet = false;
    m_rdp_authority_isValid = false;

    m_ssh_authority_isSet = false;
    m_ssh_authority_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAINetworkInterface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINetworkInterface::fromJsonObject(QJsonObject json) {

    m_private_ip_address_isValid = ::OpenAPI::fromJsonValue(m_private_ip_address, json[QString("privateIpAddress")]);
    m_private_ip_address_isSet = !json[QString("privateIpAddress")].isNull() && m_private_ip_address_isValid;

    m_rdp_authority_isValid = ::OpenAPI::fromJsonValue(m_rdp_authority, json[QString("rdpAuthority")]);
    m_rdp_authority_isSet = !json[QString("rdpAuthority")].isNull() && m_rdp_authority_isValid;

    m_ssh_authority_isValid = ::OpenAPI::fromJsonValue(m_ssh_authority, json[QString("sshAuthority")]);
    m_ssh_authority_isSet = !json[QString("sshAuthority")].isNull() && m_ssh_authority_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAINetworkInterface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINetworkInterface::asJsonObject() const {
    QJsonObject obj;
    if (m_private_ip_address_isSet) {
        obj.insert(QString("privateIpAddress"), ::OpenAPI::toJsonValue(m_private_ip_address));
    }
    if (m_rdp_authority_isSet) {
        obj.insert(QString("rdpAuthority"), ::OpenAPI::toJsonValue(m_rdp_authority));
    }
    if (m_ssh_authority_isSet) {
        obj.insert(QString("sshAuthority"), ::OpenAPI::toJsonValue(m_ssh_authority));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAINetworkInterface::getPrivateIpAddress() const {
    return m_private_ip_address;
}
void OAINetworkInterface::setPrivateIpAddress(const QString &private_ip_address) {
    m_private_ip_address = private_ip_address;
    m_private_ip_address_isSet = true;
}

bool OAINetworkInterface::is_private_ip_address_Set() const{
    return m_private_ip_address_isSet;
}

bool OAINetworkInterface::is_private_ip_address_Valid() const{
    return m_private_ip_address_isValid;
}

QString OAINetworkInterface::getRdpAuthority() const {
    return m_rdp_authority;
}
void OAINetworkInterface::setRdpAuthority(const QString &rdp_authority) {
    m_rdp_authority = rdp_authority;
    m_rdp_authority_isSet = true;
}

bool OAINetworkInterface::is_rdp_authority_Set() const{
    return m_rdp_authority_isSet;
}

bool OAINetworkInterface::is_rdp_authority_Valid() const{
    return m_rdp_authority_isValid;
}

QString OAINetworkInterface::getSshAuthority() const {
    return m_ssh_authority;
}
void OAINetworkInterface::setSshAuthority(const QString &ssh_authority) {
    m_ssh_authority = ssh_authority;
    m_ssh_authority_isSet = true;
}

bool OAINetworkInterface::is_ssh_authority_Set() const{
    return m_ssh_authority_isSet;
}

bool OAINetworkInterface::is_ssh_authority_Valid() const{
    return m_ssh_authority_isValid;
}

QString OAINetworkInterface::getUsername() const {
    return m_username;
}
void OAINetworkInterface::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAINetworkInterface::is_username_Set() const{
    return m_username_isSet;
}

bool OAINetworkInterface::is_username_Valid() const{
    return m_username_isValid;
}

bool OAINetworkInterface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_private_ip_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rdp_authority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssh_authority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINetworkInterface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
