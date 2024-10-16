/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthority.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthority::OAIAuthority(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthority::OAIAuthority() {
    this->initializeModel();
}

OAIAuthority::~OAIAuthority() {}

void OAIAuthority::initializeModel() {

    m_client_isSet = false;
    m_client_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_user_isSet = false;
    m_user_isValid = false;
}

void OAIAuthority::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthority::fromJsonObject(QJsonObject json) {

    m_client_isValid = ::OpenAPI::fromJsonValue(m_client, json[QString("client")]);
    m_client_isSet = !json[QString("client")].isNull() && m_client_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_user_isValid = ::OpenAPI::fromJsonValue(m_user, json[QString("user")]);
    m_user_isSet = !json[QString("user")].isNull() && m_user_isValid;
}

QString OAIAuthority::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthority::asJsonObject() const {
    QJsonObject obj;
    if (m_client.isSet()) {
        obj.insert(QString("client"), ::OpenAPI::toJsonValue(m_client));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_user.isSet()) {
        obj.insert(QString("user"), ::OpenAPI::toJsonValue(m_user));
    }
    return obj;
}

OAIClient OAIAuthority::getClient() const {
    return m_client;
}
void OAIAuthority::setClient(const OAIClient &client) {
    m_client = client;
    m_client_isSet = true;
}

bool OAIAuthority::is_client_Set() const{
    return m_client_isSet;
}

bool OAIAuthority::is_client_Valid() const{
    return m_client_isValid;
}

QString OAIAuthority::getId() const {
    return m_id;
}
void OAIAuthority::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAuthority::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAuthority::is_id_Valid() const{
    return m_id_isValid;
}

OAIUser OAIAuthority::getUser() const {
    return m_user;
}
void OAIAuthority::setUser(const OAIUser &user) {
    m_user = user;
    m_user_isSet = true;
}

bool OAIAuthority::is_user_Set() const{
    return m_user_isSet;
}

bool OAIAuthority::is_user_Valid() const{
    return m_user_isValid;
}

bool OAIAuthority::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthority::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
