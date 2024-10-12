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

#include "OAIUploadInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUploadInfo::OAIUploadInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUploadInfo::OAIUploadInfo() {
    this->initializeModel();
}

OAIUploadInfo::~OAIUploadInfo() {}

void OAIUploadInfo::initializeModel() {

    m_md5_isSet = false;
    m_md5_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parts_isSet = false;
    m_parts_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIUploadInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUploadInfo::fromJsonObject(QJsonObject json) {

    m_md5_isValid = ::OpenAPI::fromJsonValue(m_md5, json[QString("md5")]);
    m_md5_isSet = !json[QString("md5")].isNull() && m_md5_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parts_isValid = ::OpenAPI::fromJsonValue(m_parts, json[QString("parts")]);
    m_parts_isSet = !json[QString("parts")].isNull() && m_parts_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIUploadInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUploadInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_md5_isSet) {
        obj.insert(QString("md5"), ::OpenAPI::toJsonValue(m_md5));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parts.size() > 0) {
        obj.insert(QString("parts"), ::OpenAPI::toJsonValue(m_parts));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QString OAIUploadInfo::getMd5() const {
    return m_md5;
}
void OAIUploadInfo::setMd5(const QString &md5) {
    m_md5 = md5;
    m_md5_isSet = true;
}

bool OAIUploadInfo::is_md5_Set() const{
    return m_md5_isSet;
}

bool OAIUploadInfo::is_md5_Valid() const{
    return m_md5_isValid;
}

QString OAIUploadInfo::getName() const {
    return m_name;
}
void OAIUploadInfo::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUploadInfo::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUploadInfo::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIUploadFilePart> OAIUploadInfo::getParts() const {
    return m_parts;
}
void OAIUploadInfo::setParts(const QList<OAIUploadFilePart> &parts) {
    m_parts = parts;
    m_parts_isSet = true;
}

bool OAIUploadInfo::is_parts_Set() const{
    return m_parts_isSet;
}

bool OAIUploadInfo::is_parts_Valid() const{
    return m_parts_isValid;
}

qint64 OAIUploadInfo::getSize() const {
    return m_size;
}
void OAIUploadInfo::setSize(const qint64 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIUploadInfo::is_size_Set() const{
    return m_size_isSet;
}

bool OAIUploadInfo::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIUploadInfo::getStatus() const {
    return m_status;
}
void OAIUploadInfo::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUploadInfo::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUploadInfo::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIUploadInfo::getToken() const {
    return m_token;
}
void OAIUploadInfo::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIUploadInfo::is_token_Set() const{
    return m_token_isSet;
}

bool OAIUploadInfo::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIUploadInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_md5_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUploadInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
