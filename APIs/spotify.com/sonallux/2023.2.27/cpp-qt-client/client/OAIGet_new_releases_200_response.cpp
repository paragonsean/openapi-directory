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

#include "OAIGet_new_releases_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGet_new_releases_200_response::OAIGet_new_releases_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGet_new_releases_200_response::OAIGet_new_releases_200_response() {
    this->initializeModel();
}

OAIGet_new_releases_200_response::~OAIGet_new_releases_200_response() {}

void OAIGet_new_releases_200_response::initializeModel() {

    m_albums_isSet = false;
    m_albums_isValid = false;
}

void OAIGet_new_releases_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGet_new_releases_200_response::fromJsonObject(QJsonObject json) {

    m_albums_isValid = ::OpenAPI::fromJsonValue(m_albums, json[QString("albums")]);
    m_albums_isSet = !json[QString("albums")].isNull() && m_albums_isValid;
}

QString OAIGet_new_releases_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGet_new_releases_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_albums.isSet()) {
        obj.insert(QString("albums"), ::OpenAPI::toJsonValue(m_albums));
    }
    return obj;
}

OAIPagingSimplifiedAlbumObject OAIGet_new_releases_200_response::getAlbums() const {
    return m_albums;
}
void OAIGet_new_releases_200_response::setAlbums(const OAIPagingSimplifiedAlbumObject &albums) {
    m_albums = albums;
    m_albums_isSet = true;
}

bool OAIGet_new_releases_200_response::is_albums_Set() const{
    return m_albums_isSet;
}

bool OAIGet_new_releases_200_response::is_albums_Valid() const{
    return m_albums_isValid;
}

bool OAIGet_new_releases_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_albums.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGet_new_releases_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_albums_isValid && true;
}

} // namespace OpenAPI
