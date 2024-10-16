/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInteractions_interactions_inner_user.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInteractions_interactions_inner_user::OAIInteractions_interactions_inner_user(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInteractions_interactions_inner_user::OAIInteractions_interactions_inner_user() {
    this->initializeModel();
}

OAIInteractions_interactions_inner_user::~OAIInteractions_interactions_inner_user() {}

void OAIInteractions_interactions_inner_user::initializeModel() {

    m_avatar_isSet = false;
    m_avatar_isValid = false;

    m_avatar_https_isSet = false;
    m_avatar_https_isValid = false;

    m_followers_isSet = false;
    m_followers_isValid = false;

    m_twitter_id_isSet = false;
    m_twitter_id_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIInteractions_interactions_inner_user::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInteractions_interactions_inner_user::fromJsonObject(QJsonObject json) {

    m_avatar_isValid = ::OpenAPI::fromJsonValue(m_avatar, json[QString("avatar")]);
    m_avatar_isSet = !json[QString("avatar")].isNull() && m_avatar_isValid;

    m_avatar_https_isValid = ::OpenAPI::fromJsonValue(m_avatar_https, json[QString("avatar_https")]);
    m_avatar_https_isSet = !json[QString("avatar_https")].isNull() && m_avatar_https_isValid;

    m_followers_isValid = ::OpenAPI::fromJsonValue(m_followers, json[QString("followers")]);
    m_followers_isSet = !json[QString("followers")].isNull() && m_followers_isValid;

    m_twitter_id_isValid = ::OpenAPI::fromJsonValue(m_twitter_id, json[QString("twitter_id")]);
    m_twitter_id_isSet = !json[QString("twitter_id")].isNull() && m_twitter_id_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIInteractions_interactions_inner_user::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInteractions_interactions_inner_user::asJsonObject() const {
    QJsonObject obj;
    if (m_avatar_isSet) {
        obj.insert(QString("avatar"), ::OpenAPI::toJsonValue(m_avatar));
    }
    if (m_avatar_https_isSet) {
        obj.insert(QString("avatar_https"), ::OpenAPI::toJsonValue(m_avatar_https));
    }
    if (m_followers_isSet) {
        obj.insert(QString("followers"), ::OpenAPI::toJsonValue(m_followers));
    }
    if (m_twitter_id_isSet) {
        obj.insert(QString("twitter_id"), ::OpenAPI::toJsonValue(m_twitter_id));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIInteractions_interactions_inner_user::getAvatar() const {
    return m_avatar;
}
void OAIInteractions_interactions_inner_user::setAvatar(const QString &avatar) {
    m_avatar = avatar;
    m_avatar_isSet = true;
}

bool OAIInteractions_interactions_inner_user::is_avatar_Set() const{
    return m_avatar_isSet;
}

bool OAIInteractions_interactions_inner_user::is_avatar_Valid() const{
    return m_avatar_isValid;
}

QString OAIInteractions_interactions_inner_user::getAvatarHttps() const {
    return m_avatar_https;
}
void OAIInteractions_interactions_inner_user::setAvatarHttps(const QString &avatar_https) {
    m_avatar_https = avatar_https;
    m_avatar_https_isSet = true;
}

bool OAIInteractions_interactions_inner_user::is_avatar_https_Set() const{
    return m_avatar_https_isSet;
}

bool OAIInteractions_interactions_inner_user::is_avatar_https_Valid() const{
    return m_avatar_https_isValid;
}

double OAIInteractions_interactions_inner_user::getFollowers() const {
    return m_followers;
}
void OAIInteractions_interactions_inner_user::setFollowers(const double &followers) {
    m_followers = followers;
    m_followers_isSet = true;
}

bool OAIInteractions_interactions_inner_user::is_followers_Set() const{
    return m_followers_isSet;
}

bool OAIInteractions_interactions_inner_user::is_followers_Valid() const{
    return m_followers_isValid;
}

QString OAIInteractions_interactions_inner_user::getTwitterId() const {
    return m_twitter_id;
}
void OAIInteractions_interactions_inner_user::setTwitterId(const QString &twitter_id) {
    m_twitter_id = twitter_id;
    m_twitter_id_isSet = true;
}

bool OAIInteractions_interactions_inner_user::is_twitter_id_Set() const{
    return m_twitter_id_isSet;
}

bool OAIInteractions_interactions_inner_user::is_twitter_id_Valid() const{
    return m_twitter_id_isValid;
}

QString OAIInteractions_interactions_inner_user::getUsername() const {
    return m_username;
}
void OAIInteractions_interactions_inner_user::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIInteractions_interactions_inner_user::is_username_Set() const{
    return m_username_isSet;
}

bool OAIInteractions_interactions_inner_user::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIInteractions_interactions_inner_user::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_avatar_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_avatar_https_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_followers_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_twitter_id_isSet) {
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

bool OAIInteractions_interactions_inner_user::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
