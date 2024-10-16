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

#include "OAIApplicationStatusRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationStatusRequest::OAIApplicationStatusRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationStatusRequest::OAIApplicationStatusRequest() {
    this->initializeModel();
}

OAIApplicationStatusRequest::~OAIApplicationStatusRequest() {}

void OAIApplicationStatusRequest::initializeModel() {

    m_build_version_isSet = false;
    m_build_version_isValid = false;

    m_bundle_identifier_isSet = false;
    m_bundle_identifier_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_team_identifier_isSet = false;
    m_team_identifier_isValid = false;

    m_track_identifier_isSet = false;
    m_track_identifier_isValid = false;

    m_train_version_isSet = false;
    m_train_version_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIApplicationStatusRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationStatusRequest::fromJsonObject(QJsonObject json) {

    m_build_version_isValid = ::OpenAPI::fromJsonValue(m_build_version, json[QString("build_version")]);
    m_build_version_isSet = !json[QString("build_version")].isNull() && m_build_version_isValid;

    m_bundle_identifier_isValid = ::OpenAPI::fromJsonValue(m_bundle_identifier, json[QString("bundle_identifier")]);
    m_bundle_identifier_isSet = !json[QString("bundle_identifier")].isNull() && m_bundle_identifier_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_team_identifier_isValid = ::OpenAPI::fromJsonValue(m_team_identifier, json[QString("team_identifier")]);
    m_team_identifier_isSet = !json[QString("team_identifier")].isNull() && m_team_identifier_isValid;

    m_track_identifier_isValid = ::OpenAPI::fromJsonValue(m_track_identifier, json[QString("track_identifier")]);
    m_track_identifier_isSet = !json[QString("track_identifier")].isNull() && m_track_identifier_isValid;

    m_train_version_isValid = ::OpenAPI::fromJsonValue(m_train_version, json[QString("train_version")]);
    m_train_version_isSet = !json[QString("train_version")].isNull() && m_train_version_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIApplicationStatusRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationStatusRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_build_version_isSet) {
        obj.insert(QString("build_version"), ::OpenAPI::toJsonValue(m_build_version));
    }
    if (m_bundle_identifier_isSet) {
        obj.insert(QString("bundle_identifier"), ::OpenAPI::toJsonValue(m_bundle_identifier));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_team_identifier_isSet) {
        obj.insert(QString("team_identifier"), ::OpenAPI::toJsonValue(m_team_identifier));
    }
    if (m_track_identifier_isSet) {
        obj.insert(QString("track_identifier"), ::OpenAPI::toJsonValue(m_track_identifier));
    }
    if (m_train_version_isSet) {
        obj.insert(QString("train_version"), ::OpenAPI::toJsonValue(m_train_version));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIApplicationStatusRequest::getBuildVersion() const {
    return m_build_version;
}
void OAIApplicationStatusRequest::setBuildVersion(const QString &build_version) {
    m_build_version = build_version;
    m_build_version_isSet = true;
}

bool OAIApplicationStatusRequest::is_build_version_Set() const{
    return m_build_version_isSet;
}

bool OAIApplicationStatusRequest::is_build_version_Valid() const{
    return m_build_version_isValid;
}

QString OAIApplicationStatusRequest::getBundleIdentifier() const {
    return m_bundle_identifier;
}
void OAIApplicationStatusRequest::setBundleIdentifier(const QString &bundle_identifier) {
    m_bundle_identifier = bundle_identifier;
    m_bundle_identifier_isSet = true;
}

bool OAIApplicationStatusRequest::is_bundle_identifier_Set() const{
    return m_bundle_identifier_isSet;
}

bool OAIApplicationStatusRequest::is_bundle_identifier_Valid() const{
    return m_bundle_identifier_isValid;
}

QString OAIApplicationStatusRequest::getPassword() const {
    return m_password;
}
void OAIApplicationStatusRequest::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIApplicationStatusRequest::is_password_Set() const{
    return m_password_isSet;
}

bool OAIApplicationStatusRequest::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIApplicationStatusRequest::getTeamIdentifier() const {
    return m_team_identifier;
}
void OAIApplicationStatusRequest::setTeamIdentifier(const QString &team_identifier) {
    m_team_identifier = team_identifier;
    m_team_identifier_isSet = true;
}

bool OAIApplicationStatusRequest::is_team_identifier_Set() const{
    return m_team_identifier_isSet;
}

bool OAIApplicationStatusRequest::is_team_identifier_Valid() const{
    return m_team_identifier_isValid;
}

QString OAIApplicationStatusRequest::getTrackIdentifier() const {
    return m_track_identifier;
}
void OAIApplicationStatusRequest::setTrackIdentifier(const QString &track_identifier) {
    m_track_identifier = track_identifier;
    m_track_identifier_isSet = true;
}

bool OAIApplicationStatusRequest::is_track_identifier_Set() const{
    return m_track_identifier_isSet;
}

bool OAIApplicationStatusRequest::is_track_identifier_Valid() const{
    return m_track_identifier_isValid;
}

QString OAIApplicationStatusRequest::getTrainVersion() const {
    return m_train_version;
}
void OAIApplicationStatusRequest::setTrainVersion(const QString &train_version) {
    m_train_version = train_version;
    m_train_version_isSet = true;
}

bool OAIApplicationStatusRequest::is_train_version_Set() const{
    return m_train_version_isSet;
}

bool OAIApplicationStatusRequest::is_train_version_Valid() const{
    return m_train_version_isValid;
}

QString OAIApplicationStatusRequest::getUsername() const {
    return m_username;
}
void OAIApplicationStatusRequest::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIApplicationStatusRequest::is_username_Set() const{
    return m_username_isSet;
}

bool OAIApplicationStatusRequest::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIApplicationStatusRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_build_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bundle_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_train_version_isSet) {
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

bool OAIApplicationStatusRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_bundle_identifier_isValid && m_password_isValid && m_track_identifier_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
