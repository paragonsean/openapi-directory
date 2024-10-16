/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIJiraSecretDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJiraSecretDetails::OAIJiraSecretDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJiraSecretDetails::OAIJiraSecretDetails() {
    this->initializeModel();
}

OAIJiraSecretDetails::~OAIJiraSecretDetails() {}

void OAIJiraSecretDetails::initializeModel() {

    m_base_url_isSet = false;
    m_base_url_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIJiraSecretDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJiraSecretDetails::fromJsonObject(QJsonObject json) {

    m_base_url_isValid = ::OpenAPI::fromJsonValue(m_base_url, json[QString("baseUrl")]);
    m_base_url_isSet = !json[QString("baseUrl")].isNull() && m_base_url_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIJiraSecretDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJiraSecretDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_base_url_isSet) {
        obj.insert(QString("baseUrl"), ::OpenAPI::toJsonValue(m_base_url));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIJiraSecretDetails::getBaseUrl() const {
    return m_base_url;
}
void OAIJiraSecretDetails::setBaseUrl(const QString &base_url) {
    m_base_url = base_url;
    m_base_url_isSet = true;
}

bool OAIJiraSecretDetails::is_base_url_Set() const{
    return m_base_url_isSet;
}

bool OAIJiraSecretDetails::is_base_url_Valid() const{
    return m_base_url_isValid;
}

QString OAIJiraSecretDetails::getPassword() const {
    return m_password;
}
void OAIJiraSecretDetails::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIJiraSecretDetails::is_password_Set() const{
    return m_password_isSet;
}

bool OAIJiraSecretDetails::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIJiraSecretDetails::getUsername() const {
    return m_username;
}
void OAIJiraSecretDetails::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIJiraSecretDetails::is_username_Set() const{
    return m_username_isSet;
}

bool OAIJiraSecretDetails::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIJiraSecretDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
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

bool OAIJiraSecretDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_base_url_isValid && m_password_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
