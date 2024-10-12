/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInfrastructureProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInfrastructureProperties::OAIInfrastructureProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInfrastructureProperties::OAIInfrastructureProperties() {
    this->initializeModel();
}

OAIInfrastructureProperties::~OAIInfrastructureProperties() {}

void OAIInfrastructureProperties::initializeModel() {

    m_is_dracoon_cloud_isSet = false;
    m_is_dracoon_cloud_isValid = false;

    m_media_server_config_enabled_isSet = false;
    m_media_server_config_enabled_isValid = false;

    m_s3_default_region_isSet = false;
    m_s3_default_region_isValid = false;

    m_s3_enforce_direct_upload_isSet = false;
    m_s3_enforce_direct_upload_isValid = false;

    m_sms_config_enabled_isSet = false;
    m_sms_config_enabled_isValid = false;

    m_tenant_uuid_isSet = false;
    m_tenant_uuid_isValid = false;
}

void OAIInfrastructureProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInfrastructureProperties::fromJsonObject(QJsonObject json) {

    m_is_dracoon_cloud_isValid = ::OpenAPI::fromJsonValue(m_is_dracoon_cloud, json[QString("isDracoonCloud")]);
    m_is_dracoon_cloud_isSet = !json[QString("isDracoonCloud")].isNull() && m_is_dracoon_cloud_isValid;

    m_media_server_config_enabled_isValid = ::OpenAPI::fromJsonValue(m_media_server_config_enabled, json[QString("mediaServerConfigEnabled")]);
    m_media_server_config_enabled_isSet = !json[QString("mediaServerConfigEnabled")].isNull() && m_media_server_config_enabled_isValid;

    m_s3_default_region_isValid = ::OpenAPI::fromJsonValue(m_s3_default_region, json[QString("s3DefaultRegion")]);
    m_s3_default_region_isSet = !json[QString("s3DefaultRegion")].isNull() && m_s3_default_region_isValid;

    m_s3_enforce_direct_upload_isValid = ::OpenAPI::fromJsonValue(m_s3_enforce_direct_upload, json[QString("s3EnforceDirectUpload")]);
    m_s3_enforce_direct_upload_isSet = !json[QString("s3EnforceDirectUpload")].isNull() && m_s3_enforce_direct_upload_isValid;

    m_sms_config_enabled_isValid = ::OpenAPI::fromJsonValue(m_sms_config_enabled, json[QString("smsConfigEnabled")]);
    m_sms_config_enabled_isSet = !json[QString("smsConfigEnabled")].isNull() && m_sms_config_enabled_isValid;

    m_tenant_uuid_isValid = ::OpenAPI::fromJsonValue(m_tenant_uuid, json[QString("tenantUuid")]);
    m_tenant_uuid_isSet = !json[QString("tenantUuid")].isNull() && m_tenant_uuid_isValid;
}

QString OAIInfrastructureProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInfrastructureProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_is_dracoon_cloud_isSet) {
        obj.insert(QString("isDracoonCloud"), ::OpenAPI::toJsonValue(m_is_dracoon_cloud));
    }
    if (m_media_server_config_enabled_isSet) {
        obj.insert(QString("mediaServerConfigEnabled"), ::OpenAPI::toJsonValue(m_media_server_config_enabled));
    }
    if (m_s3_default_region_isSet) {
        obj.insert(QString("s3DefaultRegion"), ::OpenAPI::toJsonValue(m_s3_default_region));
    }
    if (m_s3_enforce_direct_upload_isSet) {
        obj.insert(QString("s3EnforceDirectUpload"), ::OpenAPI::toJsonValue(m_s3_enforce_direct_upload));
    }
    if (m_sms_config_enabled_isSet) {
        obj.insert(QString("smsConfigEnabled"), ::OpenAPI::toJsonValue(m_sms_config_enabled));
    }
    if (m_tenant_uuid_isSet) {
        obj.insert(QString("tenantUuid"), ::OpenAPI::toJsonValue(m_tenant_uuid));
    }
    return obj;
}

bool OAIInfrastructureProperties::isIsDracoonCloud() const {
    return m_is_dracoon_cloud;
}
void OAIInfrastructureProperties::setIsDracoonCloud(const bool &is_dracoon_cloud) {
    m_is_dracoon_cloud = is_dracoon_cloud;
    m_is_dracoon_cloud_isSet = true;
}

bool OAIInfrastructureProperties::is_is_dracoon_cloud_Set() const{
    return m_is_dracoon_cloud_isSet;
}

bool OAIInfrastructureProperties::is_is_dracoon_cloud_Valid() const{
    return m_is_dracoon_cloud_isValid;
}

bool OAIInfrastructureProperties::isMediaServerConfigEnabled() const {
    return m_media_server_config_enabled;
}
void OAIInfrastructureProperties::setMediaServerConfigEnabled(const bool &media_server_config_enabled) {
    m_media_server_config_enabled = media_server_config_enabled;
    m_media_server_config_enabled_isSet = true;
}

bool OAIInfrastructureProperties::is_media_server_config_enabled_Set() const{
    return m_media_server_config_enabled_isSet;
}

bool OAIInfrastructureProperties::is_media_server_config_enabled_Valid() const{
    return m_media_server_config_enabled_isValid;
}

QString OAIInfrastructureProperties::getS3DefaultRegion() const {
    return m_s3_default_region;
}
void OAIInfrastructureProperties::setS3DefaultRegion(const QString &s3_default_region) {
    m_s3_default_region = s3_default_region;
    m_s3_default_region_isSet = true;
}

bool OAIInfrastructureProperties::is_s3_default_region_Set() const{
    return m_s3_default_region_isSet;
}

bool OAIInfrastructureProperties::is_s3_default_region_Valid() const{
    return m_s3_default_region_isValid;
}

bool OAIInfrastructureProperties::isS3EnforceDirectUpload() const {
    return m_s3_enforce_direct_upload;
}
void OAIInfrastructureProperties::setS3EnforceDirectUpload(const bool &s3_enforce_direct_upload) {
    m_s3_enforce_direct_upload = s3_enforce_direct_upload;
    m_s3_enforce_direct_upload_isSet = true;
}

bool OAIInfrastructureProperties::is_s3_enforce_direct_upload_Set() const{
    return m_s3_enforce_direct_upload_isSet;
}

bool OAIInfrastructureProperties::is_s3_enforce_direct_upload_Valid() const{
    return m_s3_enforce_direct_upload_isValid;
}

bool OAIInfrastructureProperties::isSmsConfigEnabled() const {
    return m_sms_config_enabled;
}
void OAIInfrastructureProperties::setSmsConfigEnabled(const bool &sms_config_enabled) {
    m_sms_config_enabled = sms_config_enabled;
    m_sms_config_enabled_isSet = true;
}

bool OAIInfrastructureProperties::is_sms_config_enabled_Set() const{
    return m_sms_config_enabled_isSet;
}

bool OAIInfrastructureProperties::is_sms_config_enabled_Valid() const{
    return m_sms_config_enabled_isValid;
}

QString OAIInfrastructureProperties::getTenantUuid() const {
    return m_tenant_uuid;
}
void OAIInfrastructureProperties::setTenantUuid(const QString &tenant_uuid) {
    m_tenant_uuid = tenant_uuid;
    m_tenant_uuid_isSet = true;
}

bool OAIInfrastructureProperties::is_tenant_uuid_Set() const{
    return m_tenant_uuid_isSet;
}

bool OAIInfrastructureProperties::is_tenant_uuid_Valid() const{
    return m_tenant_uuid_isValid;
}

bool OAIInfrastructureProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_dracoon_cloud_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_server_config_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_s3_default_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_s3_enforce_direct_upload_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sms_config_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenant_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInfrastructureProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
