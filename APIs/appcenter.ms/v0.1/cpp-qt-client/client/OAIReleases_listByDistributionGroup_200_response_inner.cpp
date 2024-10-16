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

#include "OAIReleases_listByDistributionGroup_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReleases_listByDistributionGroup_200_response_inner::OAIReleases_listByDistributionGroup_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReleases_listByDistributionGroup_200_response_inner::OAIReleases_listByDistributionGroup_200_response_inner() {
    this->initializeModel();
}

OAIReleases_listByDistributionGroup_200_response_inner::~OAIReleases_listByDistributionGroup_200_response_inner() {}

void OAIReleases_listByDistributionGroup_200_response_inner::initializeModel() {

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
}

void OAIReleases_listByDistributionGroup_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReleases_listByDistributionGroup_200_response_inner::fromJsonObject(QJsonObject json) {

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
}

QString OAIReleases_listByDistributionGroup_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReleases_listByDistributionGroup_200_response_inner::asJsonObject() const {
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
    return obj;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::isEnabled() const {
    return m_enabled;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_enabled_Valid() const{
    return m_enabled_isValid;
}

qint32 OAIReleases_listByDistributionGroup_200_response_inner::getId() const {
    return m_id;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::isIsExternalBuild() const {
    return m_is_external_build;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setIsExternalBuild(const bool &is_external_build) {
    m_is_external_build = is_external_build;
    m_is_external_build_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_is_external_build_Set() const{
    return m_is_external_build_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_is_external_build_Valid() const{
    return m_is_external_build_isValid;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::isMandatoryUpdate() const {
    return m_mandatory_update;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setMandatoryUpdate(const bool &mandatory_update) {
    m_mandatory_update = mandatory_update;
    m_mandatory_update_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_mandatory_update_Set() const{
    return m_mandatory_update_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_mandatory_update_Valid() const{
    return m_mandatory_update_isValid;
}

QString OAIReleases_listByDistributionGroup_200_response_inner::getOrigin() const {
    return m_origin;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setOrigin(const QString &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_origin_Valid() const{
    return m_origin_isValid;
}

QString OAIReleases_listByDistributionGroup_200_response_inner::getShortVersion() const {
    return m_short_version;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setShortVersion(const QString &short_version) {
    m_short_version = short_version;
    m_short_version_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_short_version_Set() const{
    return m_short_version_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_short_version_Valid() const{
    return m_short_version_isValid;
}

QString OAIReleases_listByDistributionGroup_200_response_inner::getUploadedAt() const {
    return m_uploaded_at;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setUploadedAt(const QString &uploaded_at) {
    m_uploaded_at = uploaded_at;
    m_uploaded_at_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_uploaded_at_Set() const{
    return m_uploaded_at_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_uploaded_at_Valid() const{
    return m_uploaded_at_isValid;
}

QString OAIReleases_listByDistributionGroup_200_response_inner::getVersion() const {
    return m_version;
}
void OAIReleases_listByDistributionGroup_200_response_inner::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_version_Set() const{
    return m_version_isSet;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::isSet() const {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIReleases_listByDistributionGroup_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_enabled_isValid && m_id_isValid && m_mandatory_update_isValid && m_short_version_isValid && m_uploaded_at_isValid && m_version_isValid && true;
}

} // namespace OpenAPI
