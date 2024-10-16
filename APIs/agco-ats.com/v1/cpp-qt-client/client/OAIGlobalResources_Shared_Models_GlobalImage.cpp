/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGlobalResources_Shared_Models_GlobalImage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGlobalResources_Shared_Models_GlobalImage::OAIGlobalResources_Shared_Models_GlobalImage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGlobalResources_Shared_Models_GlobalImage::OAIGlobalResources_Shared_Models_GlobalImage() {
    this->initializeModel();
}

OAIGlobalResources_Shared_Models_GlobalImage::~OAIGlobalResources_Shared_Models_GlobalImage() {}

void OAIGlobalResources_Shared_Models_GlobalImage::initializeModel() {

    m_crc_isSet = false;
    m_crc_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_publisher_isSet = false;
    m_publisher_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_thumbnail_crc_isSet = false;
    m_thumbnail_crc_isValid = false;

    m_thumbnail_size_isSet = false;
    m_thumbnail_size_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIGlobalResources_Shared_Models_GlobalImage::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGlobalResources_Shared_Models_GlobalImage::fromJsonObject(QJsonObject json) {

    m_crc_isValid = ::OpenAPI::fromJsonValue(m_crc, json[QString("CRC")]);
    m_crc_isSet = !json[QString("CRC")].isNull() && m_crc_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("Categories")]);
    m_categories_isSet = !json[QString("Categories")].isNull() && m_categories_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("Date")]);
    m_date_isSet = !json[QString("Date")].isNull() && m_date_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("Height")]);
    m_height_isSet = !json[QString("Height")].isNull() && m_height_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_publisher_isValid = ::OpenAPI::fromJsonValue(m_publisher, json[QString("Publisher")]);
    m_publisher_isSet = !json[QString("Publisher")].isNull() && m_publisher_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("Size")]);
    m_size_isSet = !json[QString("Size")].isNull() && m_size_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("State")]);
    m_state_isSet = !json[QString("State")].isNull() && m_state_isValid;

    m_thumbnail_crc_isValid = ::OpenAPI::fromJsonValue(m_thumbnail_crc, json[QString("ThumbnailCRC")]);
    m_thumbnail_crc_isSet = !json[QString("ThumbnailCRC")].isNull() && m_thumbnail_crc_isValid;

    m_thumbnail_size_isValid = ::OpenAPI::fromJsonValue(m_thumbnail_size, json[QString("ThumbnailSize")]);
    m_thumbnail_size_isSet = !json[QString("ThumbnailSize")].isNull() && m_thumbnail_size_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("Width")]);
    m_width_isSet = !json[QString("Width")].isNull() && m_width_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGlobalResources_Shared_Models_GlobalImage::asJsonObject() const {
    QJsonObject obj;
    if (m_crc_isSet) {
        obj.insert(QString("CRC"), ::OpenAPI::toJsonValue(m_crc));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("Categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_date_isSet) {
        obj.insert(QString("Date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_height_isSet) {
        obj.insert(QString("Height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_publisher_isSet) {
        obj.insert(QString("Publisher"), ::OpenAPI::toJsonValue(m_publisher));
    }
    if (m_size_isSet) {
        obj.insert(QString("Size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_state_isSet) {
        obj.insert(QString("State"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_thumbnail_crc_isSet) {
        obj.insert(QString("ThumbnailCRC"), ::OpenAPI::toJsonValue(m_thumbnail_crc));
    }
    if (m_thumbnail_size_isSet) {
        obj.insert(QString("ThumbnailSize"), ::OpenAPI::toJsonValue(m_thumbnail_size));
    }
    if (m_width_isSet) {
        obj.insert(QString("Width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getCrc() const {
    return m_crc;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setCrc(const QString &crc) {
    m_crc = crc;
    m_crc_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_crc_Set() const{
    return m_crc_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_crc_Valid() const{
    return m_crc_isValid;
}

QList<OAIGlobalResources_Shared_Models_GlobalImageCategory> OAIGlobalResources_Shared_Models_GlobalImage::getCategories() const {
    return m_categories;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setCategories(const QList<OAIGlobalResources_Shared_Models_GlobalImageCategory> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_categories_Valid() const{
    return m_categories_isValid;
}

QDateTime OAIGlobalResources_Shared_Models_GlobalImage::getDate() const {
    return m_date;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setDate(const QDateTime &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_date_Set() const{
    return m_date_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getDescription() const {
    return m_description;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_description_Set() const{
    return m_description_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIGlobalResources_Shared_Models_GlobalImage::getHeight() const {
    return m_height;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_height_Set() const{
    return m_height_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getId() const {
    return m_id;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getName() const {
    return m_name;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getPublisher() const {
    return m_publisher;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setPublisher(const QString &publisher) {
    m_publisher = publisher;
    m_publisher_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_publisher_Set() const{
    return m_publisher_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_publisher_Valid() const{
    return m_publisher_isValid;
}

qint64 OAIGlobalResources_Shared_Models_GlobalImage::getSize() const {
    return m_size;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setSize(const qint64 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_size_Set() const{
    return m_size_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getState() const {
    return m_state;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_state_Set() const{
    return m_state_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIGlobalResources_Shared_Models_GlobalImage::getThumbnailCrc() const {
    return m_thumbnail_crc;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setThumbnailCrc(const QString &thumbnail_crc) {
    m_thumbnail_crc = thumbnail_crc;
    m_thumbnail_crc_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_thumbnail_crc_Set() const{
    return m_thumbnail_crc_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_thumbnail_crc_Valid() const{
    return m_thumbnail_crc_isValid;
}

qint64 OAIGlobalResources_Shared_Models_GlobalImage::getThumbnailSize() const {
    return m_thumbnail_size;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setThumbnailSize(const qint64 &thumbnail_size) {
    m_thumbnail_size = thumbnail_size;
    m_thumbnail_size_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_thumbnail_size_Set() const{
    return m_thumbnail_size_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_thumbnail_size_Valid() const{
    return m_thumbnail_size_isValid;
}

qint32 OAIGlobalResources_Shared_Models_GlobalImage::getWidth() const {
    return m_width;
}
void OAIGlobalResources_Shared_Models_GlobalImage::setWidth(const qint32 &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_width_Set() const{
    return m_width_isSet;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_crc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_crc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGlobalResources_Shared_Models_GlobalImage::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_crc_isValid && m_description_isValid && m_height_isValid && m_name_isValid && m_state_isValid && m_thumbnail_crc_isValid && m_width_isValid && true;
}

} // namespace OpenAPI
