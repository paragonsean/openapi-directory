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

#include "OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner() {
    this->initializeModel();
}

OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::~OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner() {}

void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::initializeModel() {

    m_file_id_isSet = false;
    m_file_id_isValid = false;

    m_file_name_isSet = false;
    m_file_name_isValid = false;

    m_target_bundle_identifier_isSet = false;
    m_target_bundle_identifier_isValid = false;

    m_upload_id_isSet = false;
    m_upload_id_isValid = false;
}

void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::fromJsonObject(QJsonObject json) {

    m_file_id_isValid = ::OpenAPI::fromJsonValue(m_file_id, json[QString("fileId")]);
    m_file_id_isSet = !json[QString("fileId")].isNull() && m_file_id_isValid;

    m_file_name_isValid = ::OpenAPI::fromJsonValue(m_file_name, json[QString("fileName")]);
    m_file_name_isSet = !json[QString("fileName")].isNull() && m_file_name_isValid;

    m_target_bundle_identifier_isValid = ::OpenAPI::fromJsonValue(m_target_bundle_identifier, json[QString("targetBundleIdentifier")]);
    m_target_bundle_identifier_isSet = !json[QString("targetBundleIdentifier")].isNull() && m_target_bundle_identifier_isValid;

    m_upload_id_isValid = ::OpenAPI::fromJsonValue(m_upload_id, json[QString("uploadId")]);
    m_upload_id_isSet = !json[QString("uploadId")].isNull() && m_upload_id_isValid;
}

QString OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_file_id_isSet) {
        obj.insert(QString("fileId"), ::OpenAPI::toJsonValue(m_file_id));
    }
    if (m_file_name_isSet) {
        obj.insert(QString("fileName"), ::OpenAPI::toJsonValue(m_file_name));
    }
    if (m_target_bundle_identifier_isSet) {
        obj.insert(QString("targetBundleIdentifier"), ::OpenAPI::toJsonValue(m_target_bundle_identifier));
    }
    if (m_upload_id_isSet) {
        obj.insert(QString("uploadId"), ::OpenAPI::toJsonValue(m_upload_id));
    }
    return obj;
}

QString OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::getFileId() const {
    return m_file_id;
}
void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::setFileId(const QString &file_id) {
    m_file_id = file_id;
    m_file_id_isSet = true;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_file_id_Set() const{
    return m_file_id_isSet;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_file_id_Valid() const{
    return m_file_id_isValid;
}

QString OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::getFileName() const {
    return m_file_name;
}
void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::setFileName(const QString &file_name) {
    m_file_name = file_name;
    m_file_name_isSet = true;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_file_name_Set() const{
    return m_file_name_isSet;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_file_name_Valid() const{
    return m_file_name_isValid;
}

QString OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::getTargetBundleIdentifier() const {
    return m_target_bundle_identifier;
}
void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::setTargetBundleIdentifier(const QString &target_bundle_identifier) {
    m_target_bundle_identifier = target_bundle_identifier;
    m_target_bundle_identifier_isSet = true;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_target_bundle_identifier_Set() const{
    return m_target_bundle_identifier_isSet;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_target_bundle_identifier_Valid() const{
    return m_target_bundle_identifier_isValid;
}

QString OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::getUploadId() const {
    return m_upload_id;
}
void OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::setUploadId(const QString &upload_id) {
    m_upload_id = upload_id;
    m_upload_id_isSet = true;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_upload_id_Set() const{
    return m_upload_id_isSet;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::is_upload_id_Valid() const{
    return m_upload_id_isValid;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_file_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_bundle_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upload_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBranchConfigurations_get_200_response_allOf_toolsets_xcode_appExtensionProvisioningProfileFiles_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
