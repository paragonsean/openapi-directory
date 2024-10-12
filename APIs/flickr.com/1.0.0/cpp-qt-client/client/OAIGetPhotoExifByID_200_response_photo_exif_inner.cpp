/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetPhotoExifByID_200_response_photo_exif_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPhotoExifByID_200_response_photo_exif_inner::OAIGetPhotoExifByID_200_response_photo_exif_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPhotoExifByID_200_response_photo_exif_inner::OAIGetPhotoExifByID_200_response_photo_exif_inner() {
    this->initializeModel();
}

OAIGetPhotoExifByID_200_response_photo_exif_inner::~OAIGetPhotoExifByID_200_response_photo_exif_inner() {}

void OAIGetPhotoExifByID_200_response_photo_exif_inner::initializeModel() {

    m_label_isSet = false;
    m_label_isValid = false;

    m_raw_isSet = false;
    m_raw_isValid = false;

    m_tag_isSet = false;
    m_tag_isValid = false;

    m_tagspace_isSet = false;
    m_tagspace_isValid = false;

    m_tagspaceid_isSet = false;
    m_tagspaceid_isValid = false;
}

void OAIGetPhotoExifByID_200_response_photo_exif_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPhotoExifByID_200_response_photo_exif_inner::fromJsonObject(QJsonObject json) {

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_raw_isValid = ::OpenAPI::fromJsonValue(m_raw, json[QString("raw")]);
    m_raw_isSet = !json[QString("raw")].isNull() && m_raw_isValid;

    m_tag_isValid = ::OpenAPI::fromJsonValue(m_tag, json[QString("tag")]);
    m_tag_isSet = !json[QString("tag")].isNull() && m_tag_isValid;

    m_tagspace_isValid = ::OpenAPI::fromJsonValue(m_tagspace, json[QString("tagspace")]);
    m_tagspace_isSet = !json[QString("tagspace")].isNull() && m_tagspace_isValid;

    m_tagspaceid_isValid = ::OpenAPI::fromJsonValue(m_tagspaceid, json[QString("tagspaceid")]);
    m_tagspaceid_isSet = !json[QString("tagspaceid")].isNull() && m_tagspaceid_isValid;
}

QString OAIGetPhotoExifByID_200_response_photo_exif_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPhotoExifByID_200_response_photo_exif_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_raw.isSet()) {
        obj.insert(QString("raw"), ::OpenAPI::toJsonValue(m_raw));
    }
    if (m_tag_isSet) {
        obj.insert(QString("tag"), ::OpenAPI::toJsonValue(m_tag));
    }
    if (m_tagspace_isSet) {
        obj.insert(QString("tagspace"), ::OpenAPI::toJsonValue(m_tagspace));
    }
    if (m_tagspaceid_isSet) {
        obj.insert(QString("tagspaceid"), ::OpenAPI::toJsonValue(m_tagspaceid));
    }
    return obj;
}

QString OAIGetPhotoExifByID_200_response_photo_exif_inner::getLabel() const {
    return m_label;
}
void OAIGetPhotoExifByID_200_response_photo_exif_inner::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_label_Set() const{
    return m_label_isSet;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_label_Valid() const{
    return m_label_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIGetPhotoExifByID_200_response_photo_exif_inner::getRaw() const {
    return m_raw;
}
void OAIGetPhotoExifByID_200_response_photo_exif_inner::setRaw(const OAIGetFavoritesContextByID_200_response_count &raw) {
    m_raw = raw;
    m_raw_isSet = true;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_raw_Set() const{
    return m_raw_isSet;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_raw_Valid() const{
    return m_raw_isValid;
}

QString OAIGetPhotoExifByID_200_response_photo_exif_inner::getTag() const {
    return m_tag;
}
void OAIGetPhotoExifByID_200_response_photo_exif_inner::setTag(const QString &tag) {
    m_tag = tag;
    m_tag_isSet = true;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_tag_Set() const{
    return m_tag_isSet;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_tag_Valid() const{
    return m_tag_isValid;
}

QString OAIGetPhotoExifByID_200_response_photo_exif_inner::getTagspace() const {
    return m_tagspace;
}
void OAIGetPhotoExifByID_200_response_photo_exif_inner::setTagspace(const QString &tagspace) {
    m_tagspace = tagspace;
    m_tagspace_isSet = true;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_tagspace_Set() const{
    return m_tagspace_isSet;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_tagspace_Valid() const{
    return m_tagspace_isValid;
}

QString OAIGetPhotoExifByID_200_response_photo_exif_inner::getTagspaceid() const {
    return m_tagspaceid;
}
void OAIGetPhotoExifByID_200_response_photo_exif_inner::setTagspaceid(const QString &tagspaceid) {
    m_tagspaceid = tagspaceid;
    m_tagspaceid_isSet = true;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_tagspaceid_Set() const{
    return m_tagspaceid_isSet;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::is_tagspaceid_Valid() const{
    return m_tagspaceid_isValid;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_raw.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tagspace_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tagspaceid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetPhotoExifByID_200_response_photo_exif_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
