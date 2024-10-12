/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageRegionCreateEntry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageRegionCreateEntry::OAIImageRegionCreateEntry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageRegionCreateEntry::OAIImageRegionCreateEntry() {
    this->initializeModel();
}

OAIImageRegionCreateEntry::~OAIImageRegionCreateEntry() {}

void OAIImageRegionCreateEntry::initializeModel() {

    m_height_isSet = false;
    m_height_isValid = false;

    m_image_id_isSet = false;
    m_image_id_isValid = false;

    m_left_isSet = false;
    m_left_isValid = false;

    m_tag_id_isSet = false;
    m_tag_id_isValid = false;

    m_top_isSet = false;
    m_top_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIImageRegionCreateEntry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageRegionCreateEntry::fromJsonObject(QJsonObject json) {

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_image_id_isValid = ::OpenAPI::fromJsonValue(m_image_id, json[QString("imageId")]);
    m_image_id_isSet = !json[QString("imageId")].isNull() && m_image_id_isValid;

    m_left_isValid = ::OpenAPI::fromJsonValue(m_left, json[QString("left")]);
    m_left_isSet = !json[QString("left")].isNull() && m_left_isValid;

    m_tag_id_isValid = ::OpenAPI::fromJsonValue(m_tag_id, json[QString("tagId")]);
    m_tag_id_isSet = !json[QString("tagId")].isNull() && m_tag_id_isValid;

    m_top_isValid = ::OpenAPI::fromJsonValue(m_top, json[QString("top")]);
    m_top_isSet = !json[QString("top")].isNull() && m_top_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIImageRegionCreateEntry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageRegionCreateEntry::asJsonObject() const {
    QJsonObject obj;
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_image_id_isSet) {
        obj.insert(QString("imageId"), ::OpenAPI::toJsonValue(m_image_id));
    }
    if (m_left_isSet) {
        obj.insert(QString("left"), ::OpenAPI::toJsonValue(m_left));
    }
    if (m_tag_id_isSet) {
        obj.insert(QString("tagId"), ::OpenAPI::toJsonValue(m_tag_id));
    }
    if (m_top_isSet) {
        obj.insert(QString("top"), ::OpenAPI::toJsonValue(m_top));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

float OAIImageRegionCreateEntry::getHeight() const {
    return m_height;
}
void OAIImageRegionCreateEntry::setHeight(const float &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIImageRegionCreateEntry::is_height_Set() const{
    return m_height_isSet;
}

bool OAIImageRegionCreateEntry::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIImageRegionCreateEntry::getImageId() const {
    return m_image_id;
}
void OAIImageRegionCreateEntry::setImageId(const QString &image_id) {
    m_image_id = image_id;
    m_image_id_isSet = true;
}

bool OAIImageRegionCreateEntry::is_image_id_Set() const{
    return m_image_id_isSet;
}

bool OAIImageRegionCreateEntry::is_image_id_Valid() const{
    return m_image_id_isValid;
}

float OAIImageRegionCreateEntry::getLeft() const {
    return m_left;
}
void OAIImageRegionCreateEntry::setLeft(const float &left) {
    m_left = left;
    m_left_isSet = true;
}

bool OAIImageRegionCreateEntry::is_left_Set() const{
    return m_left_isSet;
}

bool OAIImageRegionCreateEntry::is_left_Valid() const{
    return m_left_isValid;
}

QString OAIImageRegionCreateEntry::getTagId() const {
    return m_tag_id;
}
void OAIImageRegionCreateEntry::setTagId(const QString &tag_id) {
    m_tag_id = tag_id;
    m_tag_id_isSet = true;
}

bool OAIImageRegionCreateEntry::is_tag_id_Set() const{
    return m_tag_id_isSet;
}

bool OAIImageRegionCreateEntry::is_tag_id_Valid() const{
    return m_tag_id_isValid;
}

float OAIImageRegionCreateEntry::getTop() const {
    return m_top;
}
void OAIImageRegionCreateEntry::setTop(const float &top) {
    m_top = top;
    m_top_isSet = true;
}

bool OAIImageRegionCreateEntry::is_top_Set() const{
    return m_top_isSet;
}

bool OAIImageRegionCreateEntry::is_top_Valid() const{
    return m_top_isValid;
}

float OAIImageRegionCreateEntry::getWidth() const {
    return m_width;
}
void OAIImageRegionCreateEntry::setWidth(const float &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIImageRegionCreateEntry::is_width_Set() const{
    return m_width_isSet;
}

bool OAIImageRegionCreateEntry::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIImageRegionCreateEntry::isSet() const {
    bool isObjectUpdated = false;
    do {
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

        if (m_tag_id_isSet) {
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

bool OAIImageRegionCreateEntry::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
