/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAmenity_Media.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAmenity_Media::OAIAmenity_Media(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAmenity_Media::OAIAmenity_Media() {
    this->initializeModel();
}

OAIAmenity_Media::~OAIAmenity_Media() {}

void OAIAmenity_Media::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_media_type_isSet = false;
    m_media_type_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIAmenity_Media::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAmenity_Media::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_media_type_isValid = ::OpenAPI::fromJsonValue(m_media_type, json[QString("mediaType")]);
    m_media_type_isSet = !json[QString("mediaType")].isNull() && m_media_type_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIAmenity_Media::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAmenity_Media::asJsonObject() const {
    QJsonObject obj;
    if (m_description.isSet()) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_media_type_isSet) {
        obj.insert(QString("mediaType"), ::OpenAPI::toJsonValue(m_media_type));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

OAIQualifiedFreeText OAIAmenity_Media::getDescription() const {
    return m_description;
}
void OAIAmenity_Media::setDescription(const OAIQualifiedFreeText &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAmenity_Media::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAmenity_Media::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIAmenity_Media::getHref() const {
    return m_href;
}
void OAIAmenity_Media::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIAmenity_Media::is_href_Set() const{
    return m_href_isSet;
}

bool OAIAmenity_Media::is_href_Valid() const{
    return m_href_isValid;
}

QString OAIAmenity_Media::getMediaType() const {
    return m_media_type;
}
void OAIAmenity_Media::setMediaType(const QString &media_type) {
    m_media_type = media_type;
    m_media_type_isSet = true;
}

bool OAIAmenity_Media::is_media_type_Set() const{
    return m_media_type_isSet;
}

bool OAIAmenity_Media::is_media_type_Valid() const{
    return m_media_type_isValid;
}

QString OAIAmenity_Media::getTitle() const {
    return m_title;
}
void OAIAmenity_Media::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIAmenity_Media::is_title_Set() const{
    return m_title_isSet;
}

bool OAIAmenity_Media::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIAmenity_Media::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAmenity_Media::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
