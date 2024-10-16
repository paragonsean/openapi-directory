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

#include "OAITesterAppRelease.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITesterAppRelease::OAITesterAppRelease(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITesterAppRelease::OAITesterAppRelease() {
    this->initializeModel();
}

OAITesterAppRelease::~OAITesterAppRelease() {}

void OAITesterAppRelease::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_external_build_isSet = false;
    m_is_external_build_isValid = false;

    m_mandatory_update_isSet = false;
    m_mandatory_update_isValid = false;

    m_origin_isSet = false;
    m_origin_isValid = false;

    m_short_version_isSet = false;
    m_short_version_isValid = false;

    m_uploaded_at_isSet = false;
    m_uploaded_at_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;

    m_install_url_isSet = false;
    m_install_url_isValid = false;

    m_release_notes_isSet = false;
    m_release_notes_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;
}

void OAITesterAppRelease::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITesterAppRelease::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_external_build_isValid = ::OpenAPI::fromJsonValue(m_is_external_build, json[QString("is_external_build")]);
    m_is_external_build_isSet = !json[QString("is_external_build")].isNull() && m_is_external_build_isValid;

    m_mandatory_update_isValid = ::OpenAPI::fromJsonValue(m_mandatory_update, json[QString("mandatory_update")]);
    m_mandatory_update_isSet = !json[QString("mandatory_update")].isNull() && m_mandatory_update_isValid;

    m_origin_isValid = ::OpenAPI::fromJsonValue(m_origin, json[QString("origin")]);
    m_origin_isSet = !json[QString("origin")].isNull() && m_origin_isValid;

    m_short_version_isValid = ::OpenAPI::fromJsonValue(m_short_version, json[QString("short_version")]);
    m_short_version_isSet = !json[QString("short_version")].isNull() && m_short_version_isValid;

    m_uploaded_at_isValid = ::OpenAPI::fromJsonValue(m_uploaded_at, json[QString("uploaded_at")]);
    m_uploaded_at_isSet = !json[QString("uploaded_at")].isNull() && m_uploaded_at_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;

    m_install_url_isValid = ::OpenAPI::fromJsonValue(m_install_url, json[QString("install_url")]);
    m_install_url_isSet = !json[QString("install_url")].isNull() && m_install_url_isValid;

    m_release_notes_isValid = ::OpenAPI::fromJsonValue(m_release_notes, json[QString("release_notes")]);
    m_release_notes_isSet = !json[QString("release_notes")].isNull() && m_release_notes_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;
}

QString OAITesterAppRelease::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITesterAppRelease::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_external_build_isSet) {
        obj.insert(QString("is_external_build"), ::OpenAPI::toJsonValue(m_is_external_build));
    }
    if (m_mandatory_update_isSet) {
        obj.insert(QString("mandatory_update"), ::OpenAPI::toJsonValue(m_mandatory_update));
    }
    if (m_origin_isSet) {
        obj.insert(QString("origin"), ::OpenAPI::toJsonValue(m_origin));
    }
    if (m_short_version_isSet) {
        obj.insert(QString("short_version"), ::OpenAPI::toJsonValue(m_short_version));
    }
    if (m_uploaded_at_isSet) {
        obj.insert(QString("uploaded_at"), ::OpenAPI::toJsonValue(m_uploaded_at));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    if (m_install_url_isSet) {
        obj.insert(QString("install_url"), ::OpenAPI::toJsonValue(m_install_url));
    }
    if (m_release_notes_isSet) {
        obj.insert(QString("release_notes"), ::OpenAPI::toJsonValue(m_release_notes));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    return obj;
}

bool OAITesterAppRelease::isEnabled() const {
    return m_enabled;
}
void OAITesterAppRelease::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAITesterAppRelease::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAITesterAppRelease::is_enabled_Valid() const{
    return m_enabled_isValid;
}

qint32 OAITesterAppRelease::getId() const {
    return m_id;
}
void OAITesterAppRelease::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITesterAppRelease::is_id_Set() const{
    return m_id_isSet;
}

bool OAITesterAppRelease::is_id_Valid() const{
    return m_id_isValid;
}

bool OAITesterAppRelease::isIsExternalBuild() const {
    return m_is_external_build;
}
void OAITesterAppRelease::setIsExternalBuild(const bool &is_external_build) {
    m_is_external_build = is_external_build;
    m_is_external_build_isSet = true;
}

bool OAITesterAppRelease::is_is_external_build_Set() const{
    return m_is_external_build_isSet;
}

bool OAITesterAppRelease::is_is_external_build_Valid() const{
    return m_is_external_build_isValid;
}

bool OAITesterAppRelease::isMandatoryUpdate() const {
    return m_mandatory_update;
}
void OAITesterAppRelease::setMandatoryUpdate(const bool &mandatory_update) {
    m_mandatory_update = mandatory_update;
    m_mandatory_update_isSet = true;
}

bool OAITesterAppRelease::is_mandatory_update_Set() const{
    return m_mandatory_update_isSet;
}

bool OAITesterAppRelease::is_mandatory_update_Valid() const{
    return m_mandatory_update_isValid;
}

QString OAITesterAppRelease::getOrigin() const {
    return m_origin;
}
void OAITesterAppRelease::setOrigin(const QString &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAITesterAppRelease::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAITesterAppRelease::is_origin_Valid() const{
    return m_origin_isValid;
}

QString OAITesterAppRelease::getShortVersion() const {
    return m_short_version;
}
void OAITesterAppRelease::setShortVersion(const QString &short_version) {
    m_short_version = short_version;
    m_short_version_isSet = true;
}

bool OAITesterAppRelease::is_short_version_Set() const{
    return m_short_version_isSet;
}

bool OAITesterAppRelease::is_short_version_Valid() const{
    return m_short_version_isValid;
}

QString OAITesterAppRelease::getUploadedAt() const {
    return m_uploaded_at;
}
void OAITesterAppRelease::setUploadedAt(const QString &uploaded_at) {
    m_uploaded_at = uploaded_at;
    m_uploaded_at_isSet = true;
}

bool OAITesterAppRelease::is_uploaded_at_Set() const{
    return m_uploaded_at_isSet;
}

bool OAITesterAppRelease::is_uploaded_at_Valid() const{
    return m_uploaded_at_isValid;
}

QString OAITesterAppRelease::getVersion() const {
    return m_version;
}
void OAITesterAppRelease::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAITesterAppRelease::is_version_Set() const{
    return m_version_isSet;
}

bool OAITesterAppRelease::is_version_Valid() const{
    return m_version_isValid;
}

QString OAITesterAppRelease::getInstallUrl() const {
    return m_install_url;
}
void OAITesterAppRelease::setInstallUrl(const QString &install_url) {
    m_install_url = install_url;
    m_install_url_isSet = true;
}

bool OAITesterAppRelease::is_install_url_Set() const{
    return m_install_url_isSet;
}

bool OAITesterAppRelease::is_install_url_Valid() const{
    return m_install_url_isValid;
}

QString OAITesterAppRelease::getReleaseNotes() const {
    return m_release_notes;
}
void OAITesterAppRelease::setReleaseNotes(const QString &release_notes) {
    m_release_notes = release_notes;
    m_release_notes_isSet = true;
}

bool OAITesterAppRelease::is_release_notes_Set() const{
    return m_release_notes_isSet;
}

bool OAITesterAppRelease::is_release_notes_Valid() const{
    return m_release_notes_isValid;
}

qint32 OAITesterAppRelease::getSize() const {
    return m_size;
}
void OAITesterAppRelease::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAITesterAppRelease::is_size_Set() const{
    return m_size_isSet;
}

bool OAITesterAppRelease::is_size_Valid() const{
    return m_size_isValid;
}

bool OAITesterAppRelease::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_external_build_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mandatory_update_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uploaded_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_install_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITesterAppRelease::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_enabled_isValid && m_id_isValid && m_mandatory_update_isValid && m_short_version_isValid && m_uploaded_at_isValid && m_version_isValid && m_size_isValid && true;
}

} // namespace OpenAPI
