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

#include "OAIFeaturedOAuthClient.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeaturedOAuthClient::OAIFeaturedOAuthClient(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeaturedOAuthClient::OAIFeaturedOAuthClient() {
    this->initializeModel();
}

OAIFeaturedOAuthClient::~OAIFeaturedOAuthClient() {}

void OAIFeaturedOAuthClient::initializeModel() {

    m_is_available_isSet = false;
    m_is_available_isValid = false;

    m_oauth_client_name_isSet = false;
    m_oauth_client_name_isValid = false;
}

void OAIFeaturedOAuthClient::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFeaturedOAuthClient::fromJsonObject(QJsonObject json) {

    m_is_available_isValid = ::OpenAPI::fromJsonValue(m_is_available, json[QString("isAvailable")]);
    m_is_available_isSet = !json[QString("isAvailable")].isNull() && m_is_available_isValid;

    m_oauth_client_name_isValid = ::OpenAPI::fromJsonValue(m_oauth_client_name, json[QString("oauthClientName")]);
    m_oauth_client_name_isSet = !json[QString("oauthClientName")].isNull() && m_oauth_client_name_isValid;
}

QString OAIFeaturedOAuthClient::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFeaturedOAuthClient::asJsonObject() const {
    QJsonObject obj;
    if (m_is_available_isSet) {
        obj.insert(QString("isAvailable"), ::OpenAPI::toJsonValue(m_is_available));
    }
    if (m_oauth_client_name_isSet) {
        obj.insert(QString("oauthClientName"), ::OpenAPI::toJsonValue(m_oauth_client_name));
    }
    return obj;
}

bool OAIFeaturedOAuthClient::isIsAvailable() const {
    return m_is_available;
}
void OAIFeaturedOAuthClient::setIsAvailable(const bool &is_available) {
    m_is_available = is_available;
    m_is_available_isSet = true;
}

bool OAIFeaturedOAuthClient::is_is_available_Set() const{
    return m_is_available_isSet;
}

bool OAIFeaturedOAuthClient::is_is_available_Valid() const{
    return m_is_available_isValid;
}

QString OAIFeaturedOAuthClient::getOauthClientName() const {
    return m_oauth_client_name;
}
void OAIFeaturedOAuthClient::setOauthClientName(const QString &oauth_client_name) {
    m_oauth_client_name = oauth_client_name;
    m_oauth_client_name_isSet = true;
}

bool OAIFeaturedOAuthClient::is_oauth_client_name_Set() const{
    return m_oauth_client_name_isSet;
}

bool OAIFeaturedOAuthClient::is_oauth_client_name_Valid() const{
    return m_oauth_client_name_isValid;
}

bool OAIFeaturedOAuthClient::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oauth_client_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFeaturedOAuthClient::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_is_available_isValid && true;
}

} // namespace OpenAPI
