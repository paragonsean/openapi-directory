/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request() {
    this->initializeModel();
}

OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::~OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request() {}

void OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::initializeModel() {

    m_password_isSet = false;
    m_password_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::fromJsonObject(QJsonObject json) {

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::getPassword() const {
    return m_password;
}
void OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::is_password_Set() const{
    return m_password_isSet;
}

bool OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::getUsername() const {
    return m_username;
}
void OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::is_username_Set() const{
    return m_username_isSet;
}

bool OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
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

bool OAIIntegrationAdminTokenServiceV1CreateAdminAccessTokenPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_password_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
