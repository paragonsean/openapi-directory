/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBoundingBox.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBoundingBox::OAIBoundingBox(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBoundingBox::OAIBoundingBox() {
    this->initializeModel();
}

OAIBoundingBox::~OAIBoundingBox() {}

void OAIBoundingBox::initializeModel() {

    m_height_isSet = false;
    m_height_isValid = false;

    m_left_isSet = false;
    m_left_isValid = false;

    m_top_isSet = false;
    m_top_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIBoundingBox::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBoundingBox::fromJsonObject(QJsonObject json) {

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_left_isValid = ::OpenAPI::fromJsonValue(m_left, json[QString("left")]);
    m_left_isSet = !json[QString("left")].isNull() && m_left_isValid;

    m_top_isValid = ::OpenAPI::fromJsonValue(m_top, json[QString("top")]);
    m_top_isSet = !json[QString("top")].isNull() && m_top_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIBoundingBox::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBoundingBox::asJsonObject() const {
    QJsonObject obj;
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_left_isSet) {
        obj.insert(QString("left"), ::OpenAPI::toJsonValue(m_left));
    }
    if (m_top_isSet) {
        obj.insert(QString("top"), ::OpenAPI::toJsonValue(m_top));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

float OAIBoundingBox::getHeight() const {
    return m_height;
}
void OAIBoundingBox::setHeight(const float &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIBoundingBox::is_height_Set() const{
    return m_height_isSet;
}

bool OAIBoundingBox::is_height_Valid() const{
    return m_height_isValid;
}

float OAIBoundingBox::getLeft() const {
    return m_left;
}
void OAIBoundingBox::setLeft(const float &left) {
    m_left = left;
    m_left_isSet = true;
}

bool OAIBoundingBox::is_left_Set() const{
    return m_left_isSet;
}

bool OAIBoundingBox::is_left_Valid() const{
    return m_left_isValid;
}

float OAIBoundingBox::getTop() const {
    return m_top;
}
void OAIBoundingBox::setTop(const float &top) {
    m_top = top;
    m_top_isSet = true;
}

bool OAIBoundingBox::is_top_Set() const{
    return m_top_isSet;
}

bool OAIBoundingBox::is_top_Valid() const{
    return m_top_isValid;
}

float OAIBoundingBox::getWidth() const {
    return m_width;
}
void OAIBoundingBox::setWidth(const float &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIBoundingBox::is_width_Set() const{
    return m_width_isSet;
}

bool OAIBoundingBox::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIBoundingBox::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_left_isSet) {
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

bool OAIBoundingBox::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_height_isValid && m_left_isValid && m_top_isValid && m_width_isValid && true;
}

} // namespace OpenAPI
