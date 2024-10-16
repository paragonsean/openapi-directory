/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPreviewFile_attributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPreviewFile_attributes::OAIPreviewFile_attributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPreviewFile_attributes::OAIPreviewFile_attributes() {
    this->initializeModel();
}

OAIPreviewFile_attributes::~OAIPreviewFile_attributes() {}

void OAIPreviewFile_attributes::initializeModel() {

    m_image_isSet = false;
    m_image_isValid = false;

    m_image_hash_isSet = false;
    m_image_hash_isValid = false;

    m_page_count_isSet = false;
    m_page_count_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;
}

void OAIPreviewFile_attributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPreviewFile_attributes::fromJsonObject(QJsonObject json) {

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_image_hash_isValid = ::OpenAPI::fromJsonValue(m_image_hash, json[QString("imageHash")]);
    m_image_hash_isSet = !json[QString("imageHash")].isNull() && m_image_hash_isValid;

    m_page_count_isValid = ::OpenAPI::fromJsonValue(m_page_count, json[QString("pageCount")]);
    m_page_count_isSet = !json[QString("pageCount")].isNull() && m_page_count_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;
}

QString OAIPreviewFile_attributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPreviewFile_attributes::asJsonObject() const {
    QJsonObject obj;
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_image_hash_isSet) {
        obj.insert(QString("imageHash"), ::OpenAPI::toJsonValue(m_image_hash));
    }
    if (m_page_count_isSet) {
        obj.insert(QString("pageCount"), ::OpenAPI::toJsonValue(m_page_count));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    return obj;
}

QString OAIPreviewFile_attributes::getImage() const {
    return m_image;
}
void OAIPreviewFile_attributes::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIPreviewFile_attributes::is_image_Set() const{
    return m_image_isSet;
}

bool OAIPreviewFile_attributes::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIPreviewFile_attributes::getImageHash() const {
    return m_image_hash;
}
void OAIPreviewFile_attributes::setImageHash(const QString &image_hash) {
    m_image_hash = image_hash;
    m_image_hash_isSet = true;
}

bool OAIPreviewFile_attributes::is_image_hash_Set() const{
    return m_image_hash_isSet;
}

bool OAIPreviewFile_attributes::is_image_hash_Valid() const{
    return m_image_hash_isValid;
}

qint32 OAIPreviewFile_attributes::getPageCount() const {
    return m_page_count;
}
void OAIPreviewFile_attributes::setPageCount(const qint32 &page_count) {
    m_page_count = page_count;
    m_page_count_isSet = true;
}

bool OAIPreviewFile_attributes::is_page_count_Set() const{
    return m_page_count_isSet;
}

bool OAIPreviewFile_attributes::is_page_count_Valid() const{
    return m_page_count_isValid;
}

qint64 OAIPreviewFile_attributes::getSize() const {
    return m_size;
}
void OAIPreviewFile_attributes::setSize(const qint64 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIPreviewFile_attributes::is_size_Set() const{
    return m_size_isSet;
}

bool OAIPreviewFile_attributes::is_size_Valid() const{
    return m_size_isValid;
}

bool OAIPreviewFile_attributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_count_isSet) {
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

bool OAIPreviewFile_attributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
