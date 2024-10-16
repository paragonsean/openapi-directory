/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPersonalisedMusicPlaylistVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPersonalisedMusicPlaylistVersion::OAIPersonalisedMusicPlaylistVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPersonalisedMusicPlaylistVersion::OAIPersonalisedMusicPlaylistVersion() {
    this->initializeModel();
}

OAIPersonalisedMusicPlaylistVersion::~OAIPersonalisedMusicPlaylistVersion() {}

void OAIPersonalisedMusicPlaylistVersion::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_expires_at_isSet = false;
    m_expires_at_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_starts_at_isSet = false;
    m_starts_at_isValid = false;

    m_warnings_isSet = false;
    m_warnings_isValid = false;
}

void OAIPersonalisedMusicPlaylistVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPersonalisedMusicPlaylistVersion::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_expires_at_isValid = ::OpenAPI::fromJsonValue(m_expires_at, json[QString("expires_at")]);
    m_expires_at_isSet = !json[QString("expires_at")].isNull() && m_expires_at_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_starts_at_isValid = ::OpenAPI::fromJsonValue(m_starts_at, json[QString("starts_at")]);
    m_starts_at_isSet = !json[QString("starts_at")].isNull() && m_starts_at_isValid;

    m_warnings_isValid = ::OpenAPI::fromJsonValue(m_warnings, json[QString("warnings")]);
    m_warnings_isSet = !json[QString("warnings")].isNull() && m_warnings_isValid;
}

QString OAIPersonalisedMusicPlaylistVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPersonalisedMusicPlaylistVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_expires_at_isSet) {
        obj.insert(QString("expires_at"), ::OpenAPI::toJsonValue(m_expires_at));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_starts_at_isSet) {
        obj.insert(QString("starts_at"), ::OpenAPI::toJsonValue(m_starts_at));
    }
    if (m_warnings.size() > 0) {
        obj.insert(QString("warnings"), ::OpenAPI::toJsonValue(m_warnings));
    }
    return obj;
}

QString OAIPersonalisedMusicPlaylistVersion::getDuration() const {
    return m_duration;
}
void OAIPersonalisedMusicPlaylistVersion::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIPersonalisedMusicPlaylistVersion::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIPersonalisedMusicPlaylistVersion::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIPersonalisedMusicPlaylistVersion::getExpiresAt() const {
    return m_expires_at;
}
void OAIPersonalisedMusicPlaylistVersion::setExpiresAt(const QString &expires_at) {
    m_expires_at = expires_at;
    m_expires_at_isSet = true;
}

bool OAIPersonalisedMusicPlaylistVersion::is_expires_at_Set() const{
    return m_expires_at_isSet;
}

bool OAIPersonalisedMusicPlaylistVersion::is_expires_at_Valid() const{
    return m_expires_at_isValid;
}

QString OAIPersonalisedMusicPlaylistVersion::getId() const {
    return m_id;
}
void OAIPersonalisedMusicPlaylistVersion::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPersonalisedMusicPlaylistVersion::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPersonalisedMusicPlaylistVersion::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPersonalisedMusicPlaylistVersion::getStartsAt() const {
    return m_starts_at;
}
void OAIPersonalisedMusicPlaylistVersion::setStartsAt(const QString &starts_at) {
    m_starts_at = starts_at;
    m_starts_at_isSet = true;
}

bool OAIPersonalisedMusicPlaylistVersion::is_starts_at_Set() const{
    return m_starts_at_isSet;
}

bool OAIPersonalisedMusicPlaylistVersion::is_starts_at_Valid() const{
    return m_starts_at_isValid;
}

QList<QString> OAIPersonalisedMusicPlaylistVersion::getWarnings() const {
    return m_warnings;
}
void OAIPersonalisedMusicPlaylistVersion::setWarnings(const QList<QString> &warnings) {
    m_warnings = warnings;
    m_warnings_isSet = true;
}

bool OAIPersonalisedMusicPlaylistVersion::is_warnings_Set() const{
    return m_warnings_isSet;
}

bool OAIPersonalisedMusicPlaylistVersion::is_warnings_Valid() const{
    return m_warnings_isValid;
}

bool OAIPersonalisedMusicPlaylistVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_starts_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_warnings.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPersonalisedMusicPlaylistVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_warnings_isValid && true;
}

} // namespace OpenAPI
