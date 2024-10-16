/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIChange_playlist_details_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIChange_playlist_details_request::OAIChange_playlist_details_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIChange_playlist_details_request::OAIChange_playlist_details_request() {
    this->initializeModel();
}

OAIChange_playlist_details_request::~OAIChange_playlist_details_request() {}

void OAIChange_playlist_details_request::initializeModel() {

    m_collaborative_isSet = false;
    m_collaborative_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_r_public_isSet = false;
    m_r_public_isValid = false;
}

void OAIChange_playlist_details_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIChange_playlist_details_request::fromJsonObject(QJsonObject json) {

    m_collaborative_isValid = ::OpenAPI::fromJsonValue(m_collaborative, json[QString("collaborative")]);
    m_collaborative_isSet = !json[QString("collaborative")].isNull() && m_collaborative_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_r_public_isValid = ::OpenAPI::fromJsonValue(m_r_public, json[QString("public")]);
    m_r_public_isSet = !json[QString("public")].isNull() && m_r_public_isValid;
}

QString OAIChange_playlist_details_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIChange_playlist_details_request::asJsonObject() const {
    QJsonObject obj;
    if (m_collaborative_isSet) {
        obj.insert(QString("collaborative"), ::OpenAPI::toJsonValue(m_collaborative));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_r_public_isSet) {
        obj.insert(QString("public"), ::OpenAPI::toJsonValue(m_r_public));
    }
    return obj;
}

bool OAIChange_playlist_details_request::isCollaborative() const {
    return m_collaborative;
}
void OAIChange_playlist_details_request::setCollaborative(const bool &collaborative) {
    m_collaborative = collaborative;
    m_collaborative_isSet = true;
}

bool OAIChange_playlist_details_request::is_collaborative_Set() const{
    return m_collaborative_isSet;
}

bool OAIChange_playlist_details_request::is_collaborative_Valid() const{
    return m_collaborative_isValid;
}

QString OAIChange_playlist_details_request::getDescription() const {
    return m_description;
}
void OAIChange_playlist_details_request::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIChange_playlist_details_request::is_description_Set() const{
    return m_description_isSet;
}

bool OAIChange_playlist_details_request::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIChange_playlist_details_request::getName() const {
    return m_name;
}
void OAIChange_playlist_details_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIChange_playlist_details_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIChange_playlist_details_request::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIChange_playlist_details_request::isRPublic() const {
    return m_r_public;
}
void OAIChange_playlist_details_request::setRPublic(const bool &r_public) {
    m_r_public = r_public;
    m_r_public_isSet = true;
}

bool OAIChange_playlist_details_request::is_r_public_Set() const{
    return m_r_public_isSet;
}

bool OAIChange_playlist_details_request::is_r_public_Valid() const{
    return m_r_public_isValid;
}

bool OAIChange_playlist_details_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_collaborative_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_public_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIChange_playlist_details_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
