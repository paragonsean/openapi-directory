/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResponseWithContinuation_GalleryImage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResponseWithContinuation_GalleryImage::OAIResponseWithContinuation_GalleryImage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResponseWithContinuation_GalleryImage::OAIResponseWithContinuation_GalleryImage() {
    this->initializeModel();
}

OAIResponseWithContinuation_GalleryImage::~OAIResponseWithContinuation_GalleryImage() {}

void OAIResponseWithContinuation_GalleryImage::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIResponseWithContinuation_GalleryImage::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResponseWithContinuation_GalleryImage::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIResponseWithContinuation_GalleryImage::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResponseWithContinuation_GalleryImage::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIResponseWithContinuation_GalleryImage::getNextLink() const {
    return m_next_link;
}
void OAIResponseWithContinuation_GalleryImage::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIResponseWithContinuation_GalleryImage::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIResponseWithContinuation_GalleryImage::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIGalleryImage> OAIResponseWithContinuation_GalleryImage::getValue() const {
    return m_value;
}
void OAIResponseWithContinuation_GalleryImage::setValue(const QList<OAIGalleryImage> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIResponseWithContinuation_GalleryImage::is_value_Set() const{
    return m_value_isSet;
}

bool OAIResponseWithContinuation_GalleryImage::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIResponseWithContinuation_GalleryImage::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResponseWithContinuation_GalleryImage::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
