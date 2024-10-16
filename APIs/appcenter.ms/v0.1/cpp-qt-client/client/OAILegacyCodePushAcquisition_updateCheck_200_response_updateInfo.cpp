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

#include "OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo() {
    this->initializeModel();
}

OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::~OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo() {}

void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::initializeModel() {

    m_app_version_isSet = false;
    m_app_version_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_is_disabled_isSet = false;
    m_is_disabled_isValid = false;

    m_is_mandatory_isSet = false;
    m_is_mandatory_isValid = false;

    m_rollout_isSet = false;
    m_rollout_isValid = false;

    m_download_url_isSet = false;
    m_download_url_isValid = false;

    m_is_available_isSet = false;
    m_is_available_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_package_hash_isSet = false;
    m_package_hash_isValid = false;

    m_package_size_isSet = false;
    m_package_size_isValid = false;

    m_should_run_binary_version_isSet = false;
    m_should_run_binary_version_isValid = false;

    m_update_app_version_isSet = false;
    m_update_app_version_isValid = false;
}

void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::fromJsonObject(QJsonObject json) {

    m_app_version_isValid = ::OpenAPI::fromJsonValue(m_app_version, json[QString("appVersion")]);
    m_app_version_isSet = !json[QString("appVersion")].isNull() && m_app_version_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_is_disabled_isValid = ::OpenAPI::fromJsonValue(m_is_disabled, json[QString("isDisabled")]);
    m_is_disabled_isSet = !json[QString("isDisabled")].isNull() && m_is_disabled_isValid;

    m_is_mandatory_isValid = ::OpenAPI::fromJsonValue(m_is_mandatory, json[QString("isMandatory")]);
    m_is_mandatory_isSet = !json[QString("isMandatory")].isNull() && m_is_mandatory_isValid;

    m_rollout_isValid = ::OpenAPI::fromJsonValue(m_rollout, json[QString("rollout")]);
    m_rollout_isSet = !json[QString("rollout")].isNull() && m_rollout_isValid;

    m_download_url_isValid = ::OpenAPI::fromJsonValue(m_download_url, json[QString("downloadURL")]);
    m_download_url_isSet = !json[QString("downloadURL")].isNull() && m_download_url_isValid;

    m_is_available_isValid = ::OpenAPI::fromJsonValue(m_is_available, json[QString("isAvailable")]);
    m_is_available_isSet = !json[QString("isAvailable")].isNull() && m_is_available_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_package_hash_isValid = ::OpenAPI::fromJsonValue(m_package_hash, json[QString("packageHash")]);
    m_package_hash_isSet = !json[QString("packageHash")].isNull() && m_package_hash_isValid;

    m_package_size_isValid = ::OpenAPI::fromJsonValue(m_package_size, json[QString("packageSize")]);
    m_package_size_isSet = !json[QString("packageSize")].isNull() && m_package_size_isValid;

    m_should_run_binary_version_isValid = ::OpenAPI::fromJsonValue(m_should_run_binary_version, json[QString("shouldRunBinaryVersion")]);
    m_should_run_binary_version_isSet = !json[QString("shouldRunBinaryVersion")].isNull() && m_should_run_binary_version_isValid;

    m_update_app_version_isValid = ::OpenAPI::fromJsonValue(m_update_app_version, json[QString("updateAppVersion")]);
    m_update_app_version_isSet = !json[QString("updateAppVersion")].isNull() && m_update_app_version_isValid;
}

QString OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_app_version_isSet) {
        obj.insert(QString("appVersion"), ::OpenAPI::toJsonValue(m_app_version));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_is_disabled_isSet) {
        obj.insert(QString("isDisabled"), ::OpenAPI::toJsonValue(m_is_disabled));
    }
    if (m_is_mandatory_isSet) {
        obj.insert(QString("isMandatory"), ::OpenAPI::toJsonValue(m_is_mandatory));
    }
    if (m_rollout_isSet) {
        obj.insert(QString("rollout"), ::OpenAPI::toJsonValue(m_rollout));
    }
    if (m_download_url_isSet) {
        obj.insert(QString("downloadURL"), ::OpenAPI::toJsonValue(m_download_url));
    }
    if (m_is_available_isSet) {
        obj.insert(QString("isAvailable"), ::OpenAPI::toJsonValue(m_is_available));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_package_hash_isSet) {
        obj.insert(QString("packageHash"), ::OpenAPI::toJsonValue(m_package_hash));
    }
    if (m_package_size_isSet) {
        obj.insert(QString("packageSize"), ::OpenAPI::toJsonValue(m_package_size));
    }
    if (m_should_run_binary_version_isSet) {
        obj.insert(QString("shouldRunBinaryVersion"), ::OpenAPI::toJsonValue(m_should_run_binary_version));
    }
    if (m_update_app_version_isSet) {
        obj.insert(QString("updateAppVersion"), ::OpenAPI::toJsonValue(m_update_app_version));
    }
    return obj;
}

QString OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getAppVersion() const {
    return m_app_version;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setAppVersion(const QString &app_version) {
    m_app_version = app_version;
    m_app_version_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_app_version_Set() const{
    return m_app_version_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_app_version_Valid() const{
    return m_app_version_isValid;
}

QString OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getDescription() const {
    return m_description;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_description_Set() const{
    return m_description_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_description_Valid() const{
    return m_description_isValid;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isIsDisabled() const {
    return m_is_disabled;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setIsDisabled(const bool &is_disabled) {
    m_is_disabled = is_disabled;
    m_is_disabled_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_is_disabled_Set() const{
    return m_is_disabled_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_is_disabled_Valid() const{
    return m_is_disabled_isValid;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isIsMandatory() const {
    return m_is_mandatory;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setIsMandatory(const bool &is_mandatory) {
    m_is_mandatory = is_mandatory;
    m_is_mandatory_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_is_mandatory_Set() const{
    return m_is_mandatory_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_is_mandatory_Valid() const{
    return m_is_mandatory_isValid;
}

qint32 OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getRollout() const {
    return m_rollout;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setRollout(const qint32 &rollout) {
    m_rollout = rollout;
    m_rollout_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_rollout_Set() const{
    return m_rollout_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_rollout_Valid() const{
    return m_rollout_isValid;
}

QString OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getDownloadUrl() const {
    return m_download_url;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setDownloadUrl(const QString &download_url) {
    m_download_url = download_url;
    m_download_url_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_download_url_Set() const{
    return m_download_url_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_download_url_Valid() const{
    return m_download_url_isValid;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isIsAvailable() const {
    return m_is_available;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setIsAvailable(const bool &is_available) {
    m_is_available = is_available;
    m_is_available_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_is_available_Set() const{
    return m_is_available_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_is_available_Valid() const{
    return m_is_available_isValid;
}

QString OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getLabel() const {
    return m_label;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_label_Set() const{
    return m_label_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_label_Valid() const{
    return m_label_isValid;
}

QString OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getPackageHash() const {
    return m_package_hash;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setPackageHash(const QString &package_hash) {
    m_package_hash = package_hash;
    m_package_hash_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_package_hash_Set() const{
    return m_package_hash_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_package_hash_Valid() const{
    return m_package_hash_isValid;
}

double OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::getPackageSize() const {
    return m_package_size;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setPackageSize(const double &package_size) {
    m_package_size = package_size;
    m_package_size_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_package_size_Set() const{
    return m_package_size_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_package_size_Valid() const{
    return m_package_size_isValid;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isShouldRunBinaryVersion() const {
    return m_should_run_binary_version;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setShouldRunBinaryVersion(const bool &should_run_binary_version) {
    m_should_run_binary_version = should_run_binary_version;
    m_should_run_binary_version_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_should_run_binary_version_Set() const{
    return m_should_run_binary_version_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_should_run_binary_version_Valid() const{
    return m_should_run_binary_version_isValid;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isUpdateAppVersion() const {
    return m_update_app_version;
}
void OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::setUpdateAppVersion(const bool &update_app_version) {
    m_update_app_version = update_app_version;
    m_update_app_version_isSet = true;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_update_app_version_Set() const{
    return m_update_app_version_isSet;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::is_update_app_version_Valid() const{
    return m_update_app_version_isValid;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_disabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_mandatory_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rollout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_download_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_should_run_binary_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_app_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILegacyCodePushAcquisition_updateCheck_200_response_updateInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_is_available_isValid && true;
}

} // namespace OpenAPI
