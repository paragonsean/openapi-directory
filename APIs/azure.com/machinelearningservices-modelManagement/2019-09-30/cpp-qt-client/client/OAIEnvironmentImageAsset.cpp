/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEnvironmentImageAsset.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEnvironmentImageAsset::OAIEnvironmentImageAsset(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEnvironmentImageAsset::OAIEnvironmentImageAsset() {
    this->initializeModel();
}

OAIEnvironmentImageAsset::~OAIEnvironmentImageAsset() {}

void OAIEnvironmentImageAsset::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_mime_type_isSet = false;
    m_mime_type_isValid = false;

    m_unpack_isSet = false;
    m_unpack_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIEnvironmentImageAsset::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEnvironmentImageAsset::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_mime_type_isValid = ::OpenAPI::fromJsonValue(m_mime_type, json[QString("mimeType")]);
    m_mime_type_isSet = !json[QString("mimeType")].isNull() && m_mime_type_isValid;

    m_unpack_isValid = ::OpenAPI::fromJsonValue(m_unpack, json[QString("unpack")]);
    m_unpack_isSet = !json[QString("unpack")].isNull() && m_unpack_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIEnvironmentImageAsset::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEnvironmentImageAsset::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_mime_type_isSet) {
        obj.insert(QString("mimeType"), ::OpenAPI::toJsonValue(m_mime_type));
    }
    if (m_unpack_isSet) {
        obj.insert(QString("unpack"), ::OpenAPI::toJsonValue(m_unpack));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QString OAIEnvironmentImageAsset::getId() const {
    return m_id;
}
void OAIEnvironmentImageAsset::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEnvironmentImageAsset::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEnvironmentImageAsset::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIEnvironmentImageAsset::getMimeType() const {
    return m_mime_type;
}
void OAIEnvironmentImageAsset::setMimeType(const QString &mime_type) {
    m_mime_type = mime_type;
    m_mime_type_isSet = true;
}

bool OAIEnvironmentImageAsset::is_mime_type_Set() const{
    return m_mime_type_isSet;
}

bool OAIEnvironmentImageAsset::is_mime_type_Valid() const{
    return m_mime_type_isValid;
}

bool OAIEnvironmentImageAsset::isUnpack() const {
    return m_unpack;
}
void OAIEnvironmentImageAsset::setUnpack(const bool &unpack) {
    m_unpack = unpack;
    m_unpack_isSet = true;
}

bool OAIEnvironmentImageAsset::is_unpack_Set() const{
    return m_unpack_isSet;
}

bool OAIEnvironmentImageAsset::is_unpack_Valid() const{
    return m_unpack_isValid;
}

QString OAIEnvironmentImageAsset::getUrl() const {
    return m_url;
}
void OAIEnvironmentImageAsset::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIEnvironmentImageAsset::is_url_Set() const{
    return m_url_isSet;
}

bool OAIEnvironmentImageAsset::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIEnvironmentImageAsset::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mime_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unpack_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEnvironmentImageAsset::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
