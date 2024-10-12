/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDimensions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDimensions::OAIDimensions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDimensions::OAIDimensions() {
    this->initializeModel();
}

OAIDimensions::~OAIDimensions() {}

void OAIDimensions::initializeModel() {

    m_height_isSet = false;
    m_height_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIDimensions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDimensions::fromJsonObject(QJsonObject json) {

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIDimensions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDimensions::asJsonObject() const {
    QJsonObject obj;
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

qint32 OAIDimensions::getHeight() const {
    return m_height;
}
void OAIDimensions::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIDimensions::is_height_Set() const{
    return m_height_isSet;
}

bool OAIDimensions::is_height_Valid() const{
    return m_height_isValid;
}

qint32 OAIDimensions::getWidth() const {
    return m_width;
}
void OAIDimensions::setWidth(const qint32 &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIDimensions::is_width_Set() const{
    return m_width_isSet;
}

bool OAIDimensions::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIDimensions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_height_isSet) {
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

bool OAIDimensions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
