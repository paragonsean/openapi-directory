/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISecret.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISecret::OAISecret(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISecret::OAISecret() {
    this->initializeModel();
}

OAISecret::~OAISecret() {}

void OAISecret::initializeModel() {

    m_ca_cert_pem_isSet = false;
    m_ca_cert_pem_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;

    m_token_header_isSet = false;
    m_token_header_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAISecret::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISecret::fromJsonObject(QJsonObject json) {

    m_ca_cert_pem_isValid = ::OpenAPI::fromJsonValue(m_ca_cert_pem, json[QString("caCertPem")]);
    m_ca_cert_pem_isSet = !json[QString("caCertPem")].isNull() && m_ca_cert_pem_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;

    m_token_header_isValid = ::OpenAPI::fromJsonValue(m_token_header, json[QString("tokenHeader")]);
    m_token_header_isSet = !json[QString("tokenHeader")].isNull() && m_token_header_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAISecret::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISecret::asJsonObject() const {
    QJsonObject obj;
    if (m_ca_cert_pem_isSet) {
        obj.insert(QString("caCertPem"), ::OpenAPI::toJsonValue(m_ca_cert_pem));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    if (m_token_header_isSet) {
        obj.insert(QString("tokenHeader"), ::OpenAPI::toJsonValue(m_token_header));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAISecret::getCaCertPem() const {
    return m_ca_cert_pem;
}
void OAISecret::setCaCertPem(const QString &ca_cert_pem) {
    m_ca_cert_pem = ca_cert_pem;
    m_ca_cert_pem_isSet = true;
}

bool OAISecret::is_ca_cert_pem_Set() const{
    return m_ca_cert_pem_isSet;
}

bool OAISecret::is_ca_cert_pem_Valid() const{
    return m_ca_cert_pem_isValid;
}

QString OAISecret::getDescription() const {
    return m_description;
}
void OAISecret::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISecret::is_description_Set() const{
    return m_description_isSet;
}

bool OAISecret::is_description_Valid() const{
    return m_description_isValid;
}

QString OAISecret::getId() const {
    return m_id;
}
void OAISecret::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISecret::is_id_Set() const{
    return m_id_isSet;
}

bool OAISecret::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISecret::getName() const {
    return m_name;
}
void OAISecret::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISecret::is_name_Set() const{
    return m_name_isSet;
}

bool OAISecret::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISecret::getPassword() const {
    return m_password;
}
void OAISecret::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAISecret::is_password_Set() const{
    return m_password_isSet;
}

bool OAISecret::is_password_Valid() const{
    return m_password_isValid;
}

QString OAISecret::getToken() const {
    return m_token;
}
void OAISecret::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAISecret::is_token_Set() const{
    return m_token_isSet;
}

bool OAISecret::is_token_Valid() const{
    return m_token_isValid;
}

QString OAISecret::getTokenHeader() const {
    return m_token_header;
}
void OAISecret::setTokenHeader(const QString &token_header) {
    m_token_header = token_header;
    m_token_header_isSet = true;
}

bool OAISecret::is_token_header_Set() const{
    return m_token_header_isSet;
}

bool OAISecret::is_token_header_Valid() const{
    return m_token_header_isValid;
}

QString OAISecret::getUsername() const {
    return m_username;
}
void OAISecret::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAISecret::is_username_Set() const{
    return m_username_isSet;
}

bool OAISecret::is_username_Valid() const{
    return m_username_isValid;
}

bool OAISecret::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ca_cert_pem_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_header_isSet) {
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

bool OAISecret::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_description_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
