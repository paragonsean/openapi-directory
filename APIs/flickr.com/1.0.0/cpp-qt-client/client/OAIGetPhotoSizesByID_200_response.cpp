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

#include "OAIGetPhotoSizesByID_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPhotoSizesByID_200_response::OAIGetPhotoSizesByID_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPhotoSizesByID_200_response::OAIGetPhotoSizesByID_200_response() {
    this->initializeModel();
}

OAIGetPhotoSizesByID_200_response::~OAIGetPhotoSizesByID_200_response() {}

void OAIGetPhotoSizesByID_200_response::initializeModel() {

    m_sizes_isSet = false;
    m_sizes_isValid = false;

    m_stat_isSet = false;
    m_stat_isValid = false;
}

void OAIGetPhotoSizesByID_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPhotoSizesByID_200_response::fromJsonObject(QJsonObject json) {

    m_sizes_isValid = ::OpenAPI::fromJsonValue(m_sizes, json[QString("sizes")]);
    m_sizes_isSet = !json[QString("sizes")].isNull() && m_sizes_isValid;

    m_stat_isValid = ::OpenAPI::fromJsonValue(m_stat, json[QString("stat")]);
    m_stat_isSet = !json[QString("stat")].isNull() && m_stat_isValid;
}

QString OAIGetPhotoSizesByID_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPhotoSizesByID_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_sizes.isSet()) {
        obj.insert(QString("sizes"), ::OpenAPI::toJsonValue(m_sizes));
    }
    if (m_stat_isSet) {
        obj.insert(QString("stat"), ::OpenAPI::toJsonValue(m_stat));
    }
    return obj;
}

OAIGetPhotoSizesByID_200_response_sizes OAIGetPhotoSizesByID_200_response::getSizes() const {
    return m_sizes;
}
void OAIGetPhotoSizesByID_200_response::setSizes(const OAIGetPhotoSizesByID_200_response_sizes &sizes) {
    m_sizes = sizes;
    m_sizes_isSet = true;
}

bool OAIGetPhotoSizesByID_200_response::is_sizes_Set() const{
    return m_sizes_isSet;
}

bool OAIGetPhotoSizesByID_200_response::is_sizes_Valid() const{
    return m_sizes_isValid;
}

QString OAIGetPhotoSizesByID_200_response::getStat() const {
    return m_stat;
}
void OAIGetPhotoSizesByID_200_response::setStat(const QString &stat) {
    m_stat = stat;
    m_stat_isSet = true;
}

bool OAIGetPhotoSizesByID_200_response::is_stat_Set() const{
    return m_stat_isSet;
}

bool OAIGetPhotoSizesByID_200_response::is_stat_Valid() const{
    return m_stat_isValid;
}

bool OAIGetPhotoSizesByID_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_sizes.isSet()) {
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

bool OAIGetPhotoSizesByID_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
