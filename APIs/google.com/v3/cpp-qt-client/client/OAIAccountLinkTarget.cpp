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

#include "OAIAccountLinkTarget.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccountLinkTarget::OAIAccountLinkTarget(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccountLinkTarget::OAIAccountLinkTarget() {
    this->initializeModel();
}

OAIAccountLinkTarget::~OAIAccountLinkTarget() {}

void OAIAccountLinkTarget::initializeModel() {

    m_all_hotels_isSet = false;
    m_all_hotels_isValid = false;

    m_hotel_list_isSet = false;
    m_hotel_list_isValid = false;
}

void OAIAccountLinkTarget::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccountLinkTarget::fromJsonObject(QJsonObject json) {

    m_all_hotels_isValid = ::OpenAPI::fromJsonValue(m_all_hotels, json[QString("allHotels")]);
    m_all_hotels_isSet = !json[QString("allHotels")].isNull() && m_all_hotels_isValid;

    m_hotel_list_isValid = ::OpenAPI::fromJsonValue(m_hotel_list, json[QString("hotelList")]);
    m_hotel_list_isSet = !json[QString("hotelList")].isNull() && m_hotel_list_isValid;
}

QString OAIAccountLinkTarget::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccountLinkTarget::asJsonObject() const {
    QJsonObject obj;
    if (m_all_hotels_isSet) {
        obj.insert(QString("allHotels"), ::OpenAPI::toJsonValue(m_all_hotels));
    }
    if (m_hotel_list.isSet()) {
        obj.insert(QString("hotelList"), ::OpenAPI::toJsonValue(m_hotel_list));
    }
    return obj;
}

bool OAIAccountLinkTarget::isAllHotels() const {
    return m_all_hotels;
}
void OAIAccountLinkTarget::setAllHotels(const bool &all_hotels) {
    m_all_hotels = all_hotels;
    m_all_hotels_isSet = true;
}

bool OAIAccountLinkTarget::is_all_hotels_Set() const{
    return m_all_hotels_isSet;
}

bool OAIAccountLinkTarget::is_all_hotels_Valid() const{
    return m_all_hotels_isValid;
}

OAIHotelList OAIAccountLinkTarget::getHotelList() const {
    return m_hotel_list;
}
void OAIAccountLinkTarget::setHotelList(const OAIHotelList &hotel_list) {
    m_hotel_list = hotel_list;
    m_hotel_list_isSet = true;
}

bool OAIAccountLinkTarget::is_hotel_list_Set() const{
    return m_hotel_list_isSet;
}

bool OAIAccountLinkTarget::is_hotel_list_Valid() const{
    return m_hotel_list_isValid;
}

bool OAIAccountLinkTarget::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_all_hotels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hotel_list.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccountLinkTarget::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
