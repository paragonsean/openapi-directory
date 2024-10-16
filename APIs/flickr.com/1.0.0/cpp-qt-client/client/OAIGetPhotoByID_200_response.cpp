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

#include "OAIGetPhotoByID_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPhotoByID_200_response::OAIGetPhotoByID_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPhotoByID_200_response::OAIGetPhotoByID_200_response() {
    this->initializeModel();
}

OAIGetPhotoByID_200_response::~OAIGetPhotoByID_200_response() {}

void OAIGetPhotoByID_200_response::initializeModel() {

    m_photo_isSet = false;
    m_photo_isValid = false;

    m_stat_isSet = false;
    m_stat_isValid = false;
}

void OAIGetPhotoByID_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPhotoByID_200_response::fromJsonObject(QJsonObject json) {

    m_photo_isValid = ::OpenAPI::fromJsonValue(m_photo, json[QString("photo")]);
    m_photo_isSet = !json[QString("photo")].isNull() && m_photo_isValid;

    m_stat_isValid = ::OpenAPI::fromJsonValue(m_stat, json[QString("stat")]);
    m_stat_isSet = !json[QString("stat")].isNull() && m_stat_isValid;
}

QString OAIGetPhotoByID_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPhotoByID_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_photo.isSet()) {
        obj.insert(QString("photo"), ::OpenAPI::toJsonValue(m_photo));
    }
    if (m_stat_isSet) {
        obj.insert(QString("stat"), ::OpenAPI::toJsonValue(m_stat));
    }
    return obj;
}

OAIPhoto OAIGetPhotoByID_200_response::getPhoto() const {
    return m_photo;
}
void OAIGetPhotoByID_200_response::setPhoto(const OAIPhoto &photo) {
    m_photo = photo;
    m_photo_isSet = true;
}

bool OAIGetPhotoByID_200_response::is_photo_Set() const{
    return m_photo_isSet;
}

bool OAIGetPhotoByID_200_response::is_photo_Valid() const{
    return m_photo_isValid;
}

QString OAIGetPhotoByID_200_response::getStat() const {
    return m_stat;
}
void OAIGetPhotoByID_200_response::setStat(const QString &stat) {
    m_stat = stat;
    m_stat_isSet = true;
}

bool OAIGetPhotoByID_200_response::is_stat_Set() const{
    return m_stat_isSet;
}

bool OAIGetPhotoByID_200_response::is_stat_Valid() const{
    return m_stat_isValid;
}

bool OAIGetPhotoByID_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_photo.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_stat_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetPhotoByID_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
