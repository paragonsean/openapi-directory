/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageRegionCreateResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageRegionCreateResult::OAIImageRegionCreateResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageRegionCreateResult::OAIImageRegionCreateResult() {
    this->initializeModel();
}

OAIImageRegionCreateResult::~OAIImageRegionCreateResult() {}

void OAIImageRegionCreateResult::initializeModel() {

    m_created_isSet = false;
    m_created_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_image_id_isSet = false;
    m_image_id_isValid = false;

    m_left_isSet = false;
    m_left_isValid = false;

    m_region_id_isSet = false;
    m_region_id_isValid = false;

    m_tag_id_isSet = false;
    m_tag_id_isValid = false;

    m_tag_name_isSet = false;
    m_tag_name_isValid = false;

    m_top_isSet = false;
    m_top_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIImageRegionCreateResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageRegionCreateResult::fromJsonObject(QJsonObject json) {

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_image_id_isValid = ::OpenAPI::fromJsonValue(m_image_id, json[QString("imageId")]);
    m_image_id_isSet = !json[QString("imageId")].isNull() && m_image_id_isValid;

    m_left_isValid = ::OpenAPI::fromJsonValue(m_left, json[QString("left")]);
    m_left_isSet = !json[QString("left")].isNull() && m_left_isValid;

    m_region_id_isValid = ::OpenAPI::fromJsonValue(m_region_id, json[QString("regionId")]);
    m_region_id_isSet = !json[QString("regionId")].isNull() && m_region_id_isValid;

    m_tag_id_isValid = ::OpenAPI::fromJsonValue(m_tag_id, json[QString("tagId")]);
    m_tag_id_isSet = !json[QString("tagId")].isNull() && m_tag_id_isValid;

    m_tag_name_isValid = ::OpenAPI::fromJsonValue(m_tag_name, json[QString("tagName")]);
    m_tag_name_isSet = !json[QString("tagName")].isNull() && m_tag_name_isValid;

    m_top_isValid = ::OpenAPI::fromJsonValue(m_top, json[QString("top")]);
    m_top_isSet = !json[QString("top")].isNull() && m_top_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIImageRegionCreateResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageRegionCreateResult::asJsonObject() const {
    QJsonObject obj;
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_image_id_isSet) {
        obj.insert(QString("imageId"), ::OpenAPI::toJsonValue(m_image_id));
    }
    if (m_left_isSet) {
        obj.insert(QString("left"), ::OpenAPI::toJsonValue(m_left));
    }
    if (m_region_id_isSet) {
        obj.insert(QString("regionId"), ::OpenAPI::toJsonValue(m_region_id));
    }
    if (m_tag_id_isSet) {
        obj.insert(QString("tagId"), ::OpenAPI::toJsonValue(m_tag_id));
    }
    if (m_tag_name_isSet) {
        obj.insert(QString("tagName"), ::OpenAPI::toJsonValue(m_tag_name));
    }
    if (m_top_isSet) {
        obj.insert(QString("top"), ::OpenAPI::toJsonValue(m_top));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

QDateTime OAIImageRegionCreateResult::getCreated() const {
    return m_created;
}
void OAIImageRegionCreateResult::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIImageRegionCreateResult::is_created_Set() const{
    return m_created_isSet;
}

bool OAIImageRegionCreateResult::is_created_Valid() const{
    return m_created_isValid;
}

float OAIImageRegionCreateResult::getHeight() const {
    return m_height;
}
void OAIImageRegionCreateResult::setHeight(const float &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIImageRegionCreateResult::is_height_Set() const{
    return m_height_isSet;
}

bool OAIImageRegionCreateResult::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIImageRegionCreateResult::getImageId() const {
    return m_image_id;
}
void OAIImageRegionCreateResult::setImageId(const QString &image_id) {
    m_image_id = image_id;
    m_image_id_isSet = true;
}

bool OAIImageRegionCreateResult::is_image_id_Set() const{
    return m_image_id_isSet;
}

bool OAIImageRegionCreateResult::is_image_id_Valid() const{
    return m_image_id_isValid;
}

float OAIImageRegionCreateResult::getLeft() const {
    return m_left;
}
void OAIImageRegionCreateResult::setLeft(const float &left) {
    m_left = left;
    m_left_isSet = true;
}

bool OAIImageRegionCreateResult::is_left_Set() const{
    return m_left_isSet;
}

bool OAIImageRegionCreateResult::is_left_Valid() const{
    return m_left_isValid;
}

QString OAIImageRegionCreateResult::getRegionId() const {
    return m_region_id;
}
void OAIImageRegionCreateResult::setRegionId(const QString &region_id) {
    m_region_id = region_id;
    m_region_id_isSet = true;
}

bool OAIImageRegionCreateResult::is_region_id_Set() const{
    return m_region_id_isSet;
}

bool OAIImageRegionCreateResult::is_region_id_Valid() const{
    return m_region_id_isValid;
}

QString OAIImageRegionCreateResult::getTagId() const {
    return m_tag_id;
}
void OAIImageRegionCreateResult::setTagId(const QString &tag_id) {
    m_tag_id = tag_id;
    m_tag_id_isSet = true;
}

bool OAIImageRegionCreateResult::is_tag_id_Set() const{
    return m_tag_id_isSet;
}

bool OAIImageRegionCreateResult::is_tag_id_Valid() const{
    return m_tag_id_isValid;
}

QString OAIImageRegionCreateResult::getTagName() const {
    return m_tag_name;
}
void OAIImageRegionCreateResult::setTagName(const QString &tag_name) {
    m_tag_name = tag_name;
    m_tag_name_isSet = true;
}

bool OAIImageRegionCreateResult::is_tag_name_Set() const{
    return m_tag_name_isSet;
}

bool OAIImageRegionCreateResult::is_tag_name_Valid() const{
    return m_tag_name_isValid;
}

float OAIImageRegionCreateResult::getTop() const {
    return m_top;
}
void OAIImageRegionCreateResult::setTop(const float &top) {
    m_top = top;
    m_top_isSet = true;
}

bool OAIImageRegionCreateResult::is_top_Set() const{
    return m_top_isSet;
}

bool OAIImageRegionCreateResult::is_top_Valid() const{
    return m_top_isValid;
}

float OAIImageRegionCreateResult::getWidth() const {
    return m_width;
}
void OAIImageRegionCreateResult::setWidth(const float &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIImageRegionCreateResult::is_width_Set() const{
    return m_width_isSet;
}

bool OAIImageRegionCreateResult::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIImageRegionCreateResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_left_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_top_isSet) {
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

bool OAIImageRegionCreateResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
