/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserResponseModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserResponseModel::OAIUserResponseModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserResponseModel::OAIUserResponseModel() {
    this->initializeModel();
}

OAIUserResponseModel::~OAIUserResponseModel() {}

void OAIUserResponseModel::initializeModel() {

    m_is_new_user_isSet = false;
    m_is_new_user_isValid = false;

    m_subscription_isSet = false;
    m_subscription_isValid = false;

    m_xi_api_key_isSet = false;
    m_xi_api_key_isValid = false;
}

void OAIUserResponseModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserResponseModel::fromJsonObject(QJsonObject json) {

    m_is_new_user_isValid = ::OpenAPI::fromJsonValue(m_is_new_user, json[QString("is_new_user")]);
    m_is_new_user_isSet = !json[QString("is_new_user")].isNull() && m_is_new_user_isValid;

    m_subscription_isValid = ::OpenAPI::fromJsonValue(m_subscription, json[QString("subscription")]);
    m_subscription_isSet = !json[QString("subscription")].isNull() && m_subscription_isValid;

    m_xi_api_key_isValid = ::OpenAPI::fromJsonValue(m_xi_api_key, json[QString("xi_api_key")]);
    m_xi_api_key_isSet = !json[QString("xi_api_key")].isNull() && m_xi_api_key_isValid;
}

QString OAIUserResponseModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserResponseModel::asJsonObject() const {
    QJsonObject obj;
    if (m_is_new_user_isSet) {
        obj.insert(QString("is_new_user"), ::OpenAPI::toJsonValue(m_is_new_user));
    }
    if (m_subscription.isSet()) {
        obj.insert(QString("subscription"), ::OpenAPI::toJsonValue(m_subscription));
    }
    if (m_xi_api_key_isSet) {
        obj.insert(QString("xi_api_key"), ::OpenAPI::toJsonValue(m_xi_api_key));
    }
    return obj;
}

bool OAIUserResponseModel::isIsNewUser() const {
    return m_is_new_user;
}
void OAIUserResponseModel::setIsNewUser(const bool &is_new_user) {
    m_is_new_user = is_new_user;
    m_is_new_user_isSet = true;
}

bool OAIUserResponseModel::is_is_new_user_Set() const{
    return m_is_new_user_isSet;
}

bool OAIUserResponseModel::is_is_new_user_Valid() const{
    return m_is_new_user_isValid;
}

OAISubscriptionResponseModel OAIUserResponseModel::getSubscription() const {
    return m_subscription;
}
void OAIUserResponseModel::setSubscription(const OAISubscriptionResponseModel &subscription) {
    m_subscription = subscription;
    m_subscription_isSet = true;
}

bool OAIUserResponseModel::is_subscription_Set() const{
    return m_subscription_isSet;
}

bool OAIUserResponseModel::is_subscription_Valid() const{
    return m_subscription_isValid;
}

QString OAIUserResponseModel::getXiApiKey() const {
    return m_xi_api_key;
}
void OAIUserResponseModel::setXiApiKey(const QString &xi_api_key) {
    m_xi_api_key = xi_api_key;
    m_xi_api_key_isSet = true;
}

bool OAIUserResponseModel::is_xi_api_key_Set() const{
    return m_xi_api_key_isSet;
}

bool OAIUserResponseModel::is_xi_api_key_Valid() const{
    return m_xi_api_key_isValid;
}

bool OAIUserResponseModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_new_user_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_xi_api_key_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserResponseModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_is_new_user_isValid && m_subscription_isValid && m_xi_api_key_isValid && true;
}

} // namespace OpenAPI
