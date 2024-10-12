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

#include "OAIGet_multiple_shows_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGet_multiple_shows_200_response::OAIGet_multiple_shows_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGet_multiple_shows_200_response::OAIGet_multiple_shows_200_response() {
    this->initializeModel();
}

OAIGet_multiple_shows_200_response::~OAIGet_multiple_shows_200_response() {}

void OAIGet_multiple_shows_200_response::initializeModel() {

    m_shows_isSet = false;
    m_shows_isValid = false;
}

void OAIGet_multiple_shows_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGet_multiple_shows_200_response::fromJsonObject(QJsonObject json) {

    m_shows_isValid = ::OpenAPI::fromJsonValue(m_shows, json[QString("shows")]);
    m_shows_isSet = !json[QString("shows")].isNull() && m_shows_isValid;
}

QString OAIGet_multiple_shows_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGet_multiple_shows_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_shows.size() > 0) {
        obj.insert(QString("shows"), ::OpenAPI::toJsonValue(m_shows));
    }
    return obj;
}

QList<OAISimplifiedShowObject> OAIGet_multiple_shows_200_response::getShows() const {
    return m_shows;
}
void OAIGet_multiple_shows_200_response::setShows(const QList<OAISimplifiedShowObject> &shows) {
    m_shows = shows;
    m_shows_isSet = true;
}

bool OAIGet_multiple_shows_200_response::is_shows_Set() const{
    return m_shows_isSet;
}

bool OAIGet_multiple_shows_200_response::is_shows_Valid() const{
    return m_shows_isValid;
}

bool OAIGet_multiple_shows_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_shows.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGet_multiple_shows_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_shows_isValid && true;
}

} // namespace OpenAPI
