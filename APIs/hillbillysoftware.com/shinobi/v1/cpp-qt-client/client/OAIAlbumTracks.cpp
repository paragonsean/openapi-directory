/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlbumTracks.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlbumTracks::OAIAlbumTracks(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlbumTracks::OAIAlbumTracks() {
    this->initializeModel();
}

OAIAlbumTracks::~OAIAlbumTracks() {}

void OAIAlbumTracks::initializeModel() {

    m_album_id_isSet = false;
    m_album_id_isValid = false;

    m_artist_id_isSet = false;
    m_artist_id_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_track_name_isSet = false;
    m_track_name_isValid = false;

    m_track_no_isSet = false;
    m_track_no_isValid = false;
}

void OAIAlbumTracks::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlbumTracks::fromJsonObject(QJsonObject json) {

    m_album_id_isValid = ::OpenAPI::fromJsonValue(m_album_id, json[QString("AlbumID")]);
    m_album_id_isSet = !json[QString("AlbumID")].isNull() && m_album_id_isValid;

    m_artist_id_isValid = ::OpenAPI::fromJsonValue(m_artist_id, json[QString("ArtistID")]);
    m_artist_id_isSet = !json[QString("ArtistID")].isNull() && m_artist_id_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("Length")]);
    m_length_isSet = !json[QString("Length")].isNull() && m_length_isValid;

    m_track_name_isValid = ::OpenAPI::fromJsonValue(m_track_name, json[QString("TrackName")]);
    m_track_name_isSet = !json[QString("TrackName")].isNull() && m_track_name_isValid;

    m_track_no_isValid = ::OpenAPI::fromJsonValue(m_track_no, json[QString("TrackNo")]);
    m_track_no_isSet = !json[QString("TrackNo")].isNull() && m_track_no_isValid;
}

QString OAIAlbumTracks::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlbumTracks::asJsonObject() const {
    QJsonObject obj;
    if (m_album_id_isSet) {
        obj.insert(QString("AlbumID"), ::OpenAPI::toJsonValue(m_album_id));
    }
    if (m_artist_id_isSet) {
        obj.insert(QString("ArtistID"), ::OpenAPI::toJsonValue(m_artist_id));
    }
    if (m_length_isSet) {
        obj.insert(QString("Length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_track_name_isSet) {
        obj.insert(QString("TrackName"), ::OpenAPI::toJsonValue(m_track_name));
    }
    if (m_track_no_isSet) {
        obj.insert(QString("TrackNo"), ::OpenAPI::toJsonValue(m_track_no));
    }
    return obj;
}

QString OAIAlbumTracks::getAlbumId() const {
    return m_album_id;
}
void OAIAlbumTracks::setAlbumId(const QString &album_id) {
    m_album_id = album_id;
    m_album_id_isSet = true;
}

bool OAIAlbumTracks::is_album_id_Set() const{
    return m_album_id_isSet;
}

bool OAIAlbumTracks::is_album_id_Valid() const{
    return m_album_id_isValid;
}

QString OAIAlbumTracks::getArtistId() const {
    return m_artist_id;
}
void OAIAlbumTracks::setArtistId(const QString &artist_id) {
    m_artist_id = artist_id;
    m_artist_id_isSet = true;
}

bool OAIAlbumTracks::is_artist_id_Set() const{
    return m_artist_id_isSet;
}

bool OAIAlbumTracks::is_artist_id_Valid() const{
    return m_artist_id_isValid;
}

QString OAIAlbumTracks::getLength() const {
    return m_length;
}
void OAIAlbumTracks::setLength(const QString &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIAlbumTracks::is_length_Set() const{
    return m_length_isSet;
}

bool OAIAlbumTracks::is_length_Valid() const{
    return m_length_isValid;
}

QString OAIAlbumTracks::getTrackName() const {
    return m_track_name;
}
void OAIAlbumTracks::setTrackName(const QString &track_name) {
    m_track_name = track_name;
    m_track_name_isSet = true;
}

bool OAIAlbumTracks::is_track_name_Set() const{
    return m_track_name_isSet;
}

bool OAIAlbumTracks::is_track_name_Valid() const{
    return m_track_name_isValid;
}

QString OAIAlbumTracks::getTrackNo() const {
    return m_track_no;
}
void OAIAlbumTracks::setTrackNo(const QString &track_no) {
    m_track_no = track_no;
    m_track_no_isSet = true;
}

bool OAIAlbumTracks::is_track_no_Set() const{
    return m_track_no_isSet;
}

bool OAIAlbumTracks::is_track_no_Valid() const{
    return m_track_no_isValid;
}

bool OAIAlbumTracks::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_album_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_no_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlbumTracks::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
