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

#include "OAIUpdateNetworkSnmp_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSnmp_request::OAIUpdateNetworkSnmp_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSnmp_request::OAIUpdateNetworkSnmp_request() {
    this->initializeModel();
}

OAIUpdateNetworkSnmp_request::~OAIUpdateNetworkSnmp_request() {}

void OAIUpdateNetworkSnmp_request::initializeModel() {

    m_access_isSet = false;
    m_access_isValid = false;

    m_community_string_isSet = false;
    m_community_string_isValid = false;

    m_users_isSet = false;
    m_users_isValid = false;
}

void OAIUpdateNetworkSnmp_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSnmp_request::fromJsonObject(QJsonObject json) {

    m_access_isValid = ::OpenAPI::fromJsonValue(m_access, json[QString("access")]);
    m_access_isSet = !json[QString("access")].isNull() && m_access_isValid;

    m_community_string_isValid = ::OpenAPI::fromJsonValue(m_community_string, json[QString("communityString")]);
    m_community_string_isSet = !json[QString("communityString")].isNull() && m_community_string_isValid;

    m_users_isValid = ::OpenAPI::fromJsonValue(m_users, json[QString("users")]);
    m_users_isSet = !json[QString("users")].isNull() && m_users_isValid;
}

QString OAIUpdateNetworkSnmp_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSnmp_request::asJsonObject() const {
    QJsonObject obj;
    if (m_access_isSet) {
        obj.insert(QString("access"), ::OpenAPI::toJsonValue(m_access));
    }
    if (m_community_string_isSet) {
        obj.insert(QString("communityString"), ::OpenAPI::toJsonValue(m_community_string));
    }
    if (m_users.size() > 0) {
        obj.insert(QString("users"), ::OpenAPI::toJsonValue(m_users));
    }
    return obj;
}

QString OAIUpdateNetworkSnmp_request::getAccess() const {
    return m_access;
}
void OAIUpdateNetworkSnmp_request::setAccess(const QString &access) {
    m_access = access;
    m_access_isSet = true;
}

bool OAIUpdateNetworkSnmp_request::is_access_Set() const{
    return m_access_isSet;
}

bool OAIUpdateNetworkSnmp_request::is_access_Valid() const{
    return m_access_isValid;
}

QString OAIUpdateNetworkSnmp_request::getCommunityString() const {
    return m_community_string;
}
void OAIUpdateNetworkSnmp_request::setCommunityString(const QString &community_string) {
    m_community_string = community_string;
    m_community_string_isSet = true;
}

bool OAIUpdateNetworkSnmp_request::is_community_string_Set() const{
    return m_community_string_isSet;
}

bool OAIUpdateNetworkSnmp_request::is_community_string_Valid() const{
    return m_community_string_isValid;
}

QList<OAIUpdateNetworkSnmp_request_users_inner> OAIUpdateNetworkSnmp_request::getUsers() const {
    return m_users;
}
void OAIUpdateNetworkSnmp_request::setUsers(const QList<OAIUpdateNetworkSnmp_request_users_inner> &users) {
    m_users = users;
    m_users_isSet = true;
}

bool OAIUpdateNetworkSnmp_request::is_users_Set() const{
    return m_users_isSet;
}

bool OAIUpdateNetworkSnmp_request::is_users_Valid() const{
    return m_users_isValid;
}

bool OAIUpdateNetworkSnmp_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_community_string_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_users.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSnmp_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
