/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITag.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITag::OAITag(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITag::OAITag() {
    this->initializeModel();
}

OAITag::~OAITag() {}

void OAITag::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_count_isSet = false;
    m_image_count_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAITag::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITag::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_count_isValid = ::OpenAPI::fromJsonValue(m_image_count, json[QString("imageCount")]);
    m_image_count_isSet = !json[QString("imageCount")].isNull() && m_image_count_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAITag::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITag::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_count_isSet) {
        obj.insert(QString("imageCount"), ::OpenAPI::toJsonValue(m_image_count));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAITag::getDescription() const {
    return m_description;
}
void OAITag::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAITag::is_description_Set() const{
    return m_description_isSet;
}

bool OAITag::is_description_Valid() const{
    return m_description_isValid;
}

QString OAITag::getId() const {
    return m_id;
}
void OAITag::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITag::is_id_Set() const{
    return m_id_isSet;
}

bool OAITag::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAITag::getImageCount() const {
    return m_image_count;
}
void OAITag::setImageCount(const qint32 &image_count) {
    m_image_count = image_count;
    m_image_count_isSet = true;
}

bool OAITag::is_image_count_Set() const{
    return m_image_count_isSet;
}

bool OAITag::is_image_count_Valid() const{
    return m_image_count_isValid;
}

QString OAITag::getName() const {
    return m_name;
}
void OAITag::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITag::is_name_Set() const{
    return m_name_isSet;
}

bool OAITag::is_name_Valid() const{
    return m_name_isValid;
}

QString OAITag::getType() const {
    return m_type;
}
void OAITag::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITag::is_type_Set() const{
    return m_type_isSet;
}

bool OAITag::is_type_Valid() const{
    return m_type_isValid;
}

bool OAITag::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITag::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_description_isValid && m_name_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
