/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPublicFile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPublicFile::OAIPublicFile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPublicFile::OAIPublicFile() {
    this->initializeModel();
}

OAIPublicFile::~OAIPublicFile() {}

void OAIPublicFile::initializeModel() {

    m_computed_md5_isSet = false;
    m_computed_md5_isValid = false;

    m_download_url_isSet = false;
    m_download_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_link_only_isSet = false;
    m_is_link_only_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_supplied_md5_isSet = false;
    m_supplied_md5_isValid = false;
}

void OAIPublicFile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPublicFile::fromJsonObject(QJsonObject json) {

    m_computed_md5_isValid = ::OpenAPI::fromJsonValue(m_computed_md5, json[QString("computed_md5")]);
    m_computed_md5_isSet = !json[QString("computed_md5")].isNull() && m_computed_md5_isValid;

    m_download_url_isValid = ::OpenAPI::fromJsonValue(m_download_url, json[QString("download_url")]);
    m_download_url_isSet = !json[QString("download_url")].isNull() && m_download_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_link_only_isValid = ::OpenAPI::fromJsonValue(m_is_link_only, json[QString("is_link_only")]);
    m_is_link_only_isSet = !json[QString("is_link_only")].isNull() && m_is_link_only_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_supplied_md5_isValid = ::OpenAPI::fromJsonValue(m_supplied_md5, json[QString("supplied_md5")]);
    m_supplied_md5_isSet = !json[QString("supplied_md5")].isNull() && m_supplied_md5_isValid;
}

QString OAIPublicFile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPublicFile::asJsonObject() const {
    QJsonObject obj;
    if (m_computed_md5_isSet) {
        obj.insert(QString("computed_md5"), ::OpenAPI::toJsonValue(m_computed_md5));
    }
    if (m_download_url_isSet) {
        obj.insert(QString("download_url"), ::OpenAPI::toJsonValue(m_download_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_link_only_isSet) {
        obj.insert(QString("is_link_only"), ::OpenAPI::toJsonValue(m_is_link_only));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_supplied_md5_isSet) {
        obj.insert(QString("supplied_md5"), ::OpenAPI::toJsonValue(m_supplied_md5));
    }
    return obj;
}

QString OAIPublicFile::getComputedMd5() const {
    return m_computed_md5;
}
void OAIPublicFile::setComputedMd5(const QString &computed_md5) {
    m_computed_md5 = computed_md5;
    m_computed_md5_isSet = true;
}

bool OAIPublicFile::is_computed_md5_Set() const{
    return m_computed_md5_isSet;
}

bool OAIPublicFile::is_computed_md5_Valid() const{
    return m_computed_md5_isValid;
}

QString OAIPublicFile::getDownloadUrl() const {
    return m_download_url;
}
void OAIPublicFile::setDownloadUrl(const QString &download_url) {
    m_download_url = download_url;
    m_download_url_isSet = true;
}

bool OAIPublicFile::is_download_url_Set() const{
    return m_download_url_isSet;
}

bool OAIPublicFile::is_download_url_Valid() const{
    return m_download_url_isValid;
}

qint64 OAIPublicFile::getId() const {
    return m_id;
}
void OAIPublicFile::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPublicFile::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPublicFile::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIPublicFile::isIsLinkOnly() const {
    return m_is_link_only;
}
void OAIPublicFile::setIsLinkOnly(const bool &is_link_only) {
    m_is_link_only = is_link_only;
    m_is_link_only_isSet = true;
}

bool OAIPublicFile::is_is_link_only_Set() const{
    return m_is_link_only_isSet;
}

bool OAIPublicFile::is_is_link_only_Valid() const{
    return m_is_link_only_isValid;
}

QString OAIPublicFile::getName() const {
    return m_name;
}
void OAIPublicFile::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPublicFile::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPublicFile::is_name_Valid() const{
    return m_name_isValid;
}

qint64 OAIPublicFile::getSize() const {
    return m_size;
}
void OAIPublicFile::setSize(const qint64 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIPublicFile::is_size_Set() const{
    return m_size_isSet;
}

bool OAIPublicFile::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIPublicFile::getSuppliedMd5() const {
    return m_supplied_md5;
}
void OAIPublicFile::setSuppliedMd5(const QString &supplied_md5) {
    m_supplied_md5 = supplied_md5;
    m_supplied_md5_isSet = true;
}

bool OAIPublicFile::is_supplied_md5_Set() const{
    return m_supplied_md5_isSet;
}

bool OAIPublicFile::is_supplied_md5_Valid() const{
    return m_supplied_md5_isValid;
}

bool OAIPublicFile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_computed_md5_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_download_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_link_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supplied_md5_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPublicFile::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_computed_md5_isValid && m_download_url_isValid && m_id_isValid && m_is_link_only_isValid && m_name_isValid && m_size_isValid && m_supplied_md5_isValid && true;
}

} // namespace OpenAPI
