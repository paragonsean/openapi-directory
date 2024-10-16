/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISetLiveOnGoogleResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISetLiveOnGoogleResponse::OAISetLiveOnGoogleResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISetLiveOnGoogleResponse::OAISetLiveOnGoogleResponse() {
    this->initializeModel();
}

OAISetLiveOnGoogleResponse::~OAISetLiveOnGoogleResponse() {}

void OAISetLiveOnGoogleResponse::initializeModel() {

    m_failed_hotel_ids_isSet = false;
    m_failed_hotel_ids_isValid = false;

    m_updated_hotel_ids_isSet = false;
    m_updated_hotel_ids_isValid = false;
}

void OAISetLiveOnGoogleResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISetLiveOnGoogleResponse::fromJsonObject(QJsonObject json) {

    m_failed_hotel_ids_isValid = ::OpenAPI::fromJsonValue(m_failed_hotel_ids, json[QString("failedHotelIds")]);
    m_failed_hotel_ids_isSet = !json[QString("failedHotelIds")].isNull() && m_failed_hotel_ids_isValid;

    m_updated_hotel_ids_isValid = ::OpenAPI::fromJsonValue(m_updated_hotel_ids, json[QString("updatedHotelIds")]);
    m_updated_hotel_ids_isSet = !json[QString("updatedHotelIds")].isNull() && m_updated_hotel_ids_isValid;
}

QString OAISetLiveOnGoogleResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISetLiveOnGoogleResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_failed_hotel_ids.size() > 0) {
        obj.insert(QString("failedHotelIds"), ::OpenAPI::toJsonValue(m_failed_hotel_ids));
    }
    if (m_updated_hotel_ids.size() > 0) {
        obj.insert(QString("updatedHotelIds"), ::OpenAPI::toJsonValue(m_updated_hotel_ids));
    }
    return obj;
}

QList<QString> OAISetLiveOnGoogleResponse::getFailedHotelIds() const {
    return m_failed_hotel_ids;
}
void OAISetLiveOnGoogleResponse::setFailedHotelIds(const QList<QString> &failed_hotel_ids) {
    m_failed_hotel_ids = failed_hotel_ids;
    m_failed_hotel_ids_isSet = true;
}

bool OAISetLiveOnGoogleResponse::is_failed_hotel_ids_Set() const{
    return m_failed_hotel_ids_isSet;
}

bool OAISetLiveOnGoogleResponse::is_failed_hotel_ids_Valid() const{
    return m_failed_hotel_ids_isValid;
}

QList<QString> OAISetLiveOnGoogleResponse::getUpdatedHotelIds() const {
    return m_updated_hotel_ids;
}
void OAISetLiveOnGoogleResponse::setUpdatedHotelIds(const QList<QString> &updated_hotel_ids) {
    m_updated_hotel_ids = updated_hotel_ids;
    m_updated_hotel_ids_isSet = true;
}

bool OAISetLiveOnGoogleResponse::is_updated_hotel_ids_Set() const{
    return m_updated_hotel_ids_isSet;
}

bool OAISetLiveOnGoogleResponse::is_updated_hotel_ids_Valid() const{
    return m_updated_hotel_ids_isValid;
}

bool OAISetLiveOnGoogleResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_failed_hotel_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_hotel_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISetLiveOnGoogleResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
