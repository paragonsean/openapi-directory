/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDataDisk.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDataDisk::OAIDataDisk(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDataDisk::OAIDataDisk() {
    this->initializeModel();
}

OAIDataDisk::~OAIDataDisk() {}

void OAIDataDisk::initializeModel() {

    m_caching_isSet = false;
    m_caching_isValid = false;

    m_disk_size_gb_isSet = false;
    m_disk_size_gb_isValid = false;

    m_lun_isSet = false;
    m_lun_isValid = false;

    m_storage_account_type_isSet = false;
    m_storage_account_type_isValid = false;
}

void OAIDataDisk::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDataDisk::fromJsonObject(QJsonObject json) {

    m_caching_isValid = ::OpenAPI::fromJsonValue(m_caching, json[QString("caching")]);
    m_caching_isSet = !json[QString("caching")].isNull() && m_caching_isValid;

    m_disk_size_gb_isValid = ::OpenAPI::fromJsonValue(m_disk_size_gb, json[QString("diskSizeGB")]);
    m_disk_size_gb_isSet = !json[QString("diskSizeGB")].isNull() && m_disk_size_gb_isValid;

    m_lun_isValid = ::OpenAPI::fromJsonValue(m_lun, json[QString("lun")]);
    m_lun_isSet = !json[QString("lun")].isNull() && m_lun_isValid;

    m_storage_account_type_isValid = ::OpenAPI::fromJsonValue(m_storage_account_type, json[QString("storageAccountType")]);
    m_storage_account_type_isSet = !json[QString("storageAccountType")].isNull() && m_storage_account_type_isValid;
}

QString OAIDataDisk::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDataDisk::asJsonObject() const {
    QJsonObject obj;
    if (m_caching.isSet()) {
        obj.insert(QString("caching"), ::OpenAPI::toJsonValue(m_caching));
    }
    if (m_disk_size_gb_isSet) {
        obj.insert(QString("diskSizeGB"), ::OpenAPI::toJsonValue(m_disk_size_gb));
    }
    if (m_lun_isSet) {
        obj.insert(QString("lun"), ::OpenAPI::toJsonValue(m_lun));
    }
    if (m_storage_account_type.isSet()) {
        obj.insert(QString("storageAccountType"), ::OpenAPI::toJsonValue(m_storage_account_type));
    }
    return obj;
}

OAICachingType OAIDataDisk::getCaching() const {
    return m_caching;
}
void OAIDataDisk::setCaching(const OAICachingType &caching) {
    m_caching = caching;
    m_caching_isSet = true;
}

bool OAIDataDisk::is_caching_Set() const{
    return m_caching_isSet;
}

bool OAIDataDisk::is_caching_Valid() const{
    return m_caching_isValid;
}

qint32 OAIDataDisk::getDiskSizeGb() const {
    return m_disk_size_gb;
}
void OAIDataDisk::setDiskSizeGb(const qint32 &disk_size_gb) {
    m_disk_size_gb = disk_size_gb;
    m_disk_size_gb_isSet = true;
}

bool OAIDataDisk::is_disk_size_gb_Set() const{
    return m_disk_size_gb_isSet;
}

bool OAIDataDisk::is_disk_size_gb_Valid() const{
    return m_disk_size_gb_isValid;
}

qint32 OAIDataDisk::getLun() const {
    return m_lun;
}
void OAIDataDisk::setLun(const qint32 &lun) {
    m_lun = lun;
    m_lun_isSet = true;
}

bool OAIDataDisk::is_lun_Set() const{
    return m_lun_isSet;
}

bool OAIDataDisk::is_lun_Valid() const{
    return m_lun_isValid;
}

OAIStorageAccountType OAIDataDisk::getStorageAccountType() const {
    return m_storage_account_type;
}
void OAIDataDisk::setStorageAccountType(const OAIStorageAccountType &storage_account_type) {
    m_storage_account_type = storage_account_type;
    m_storage_account_type_isSet = true;
}

bool OAIDataDisk::is_storage_account_type_Set() const{
    return m_storage_account_type_isSet;
}

bool OAIDataDisk::is_storage_account_type_Valid() const{
    return m_storage_account_type_isValid;
}

bool OAIDataDisk::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_caching.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_disk_size_gb_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lun_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storage_account_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDataDisk::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_disk_size_gb_isValid && m_lun_isValid && true;
}

} // namespace OpenAPI
