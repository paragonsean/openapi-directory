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

#include "OAIFreeBookingLinksResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFreeBookingLinksResult::OAIFreeBookingLinksResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFreeBookingLinksResult::OAIFreeBookingLinksResult() {
    this->initializeModel();
}

OAIFreeBookingLinksResult::~OAIFreeBookingLinksResult() {}

void OAIFreeBookingLinksResult::initializeModel() {

    m_click_count_isSet = false;
    m_click_count_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_device_type_isSet = false;
    m_device_type_isValid = false;

    m_partner_hotel_display_name_isSet = false;
    m_partner_hotel_display_name_isValid = false;

    m_partner_hotel_id_isSet = false;
    m_partner_hotel_id_isValid = false;

    m_user_region_code_isSet = false;
    m_user_region_code_isValid = false;
}

void OAIFreeBookingLinksResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFreeBookingLinksResult::fromJsonObject(QJsonObject json) {

    m_click_count_isValid = ::OpenAPI::fromJsonValue(m_click_count, json[QString("clickCount")]);
    m_click_count_isSet = !json[QString("clickCount")].isNull() && m_click_count_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_device_type_isValid = ::OpenAPI::fromJsonValue(m_device_type, json[QString("deviceType")]);
    m_device_type_isSet = !json[QString("deviceType")].isNull() && m_device_type_isValid;

    m_partner_hotel_display_name_isValid = ::OpenAPI::fromJsonValue(m_partner_hotel_display_name, json[QString("partnerHotelDisplayName")]);
    m_partner_hotel_display_name_isSet = !json[QString("partnerHotelDisplayName")].isNull() && m_partner_hotel_display_name_isValid;

    m_partner_hotel_id_isValid = ::OpenAPI::fromJsonValue(m_partner_hotel_id, json[QString("partnerHotelId")]);
    m_partner_hotel_id_isSet = !json[QString("partnerHotelId")].isNull() && m_partner_hotel_id_isValid;

    m_user_region_code_isValid = ::OpenAPI::fromJsonValue(m_user_region_code, json[QString("userRegionCode")]);
    m_user_region_code_isSet = !json[QString("userRegionCode")].isNull() && m_user_region_code_isValid;
}

QString OAIFreeBookingLinksResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFreeBookingLinksResult::asJsonObject() const {
    QJsonObject obj;
    if (m_click_count_isSet) {
        obj.insert(QString("clickCount"), ::OpenAPI::toJsonValue(m_click_count));
    }
    if (m_date.isSet()) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_device_type_isSet) {
        obj.insert(QString("deviceType"), ::OpenAPI::toJsonValue(m_device_type));
    }
    if (m_partner_hotel_display_name_isSet) {
        obj.insert(QString("partnerHotelDisplayName"), ::OpenAPI::toJsonValue(m_partner_hotel_display_name));
    }
    if (m_partner_hotel_id_isSet) {
        obj.insert(QString("partnerHotelId"), ::OpenAPI::toJsonValue(m_partner_hotel_id));
    }
    if (m_user_region_code_isSet) {
        obj.insert(QString("userRegionCode"), ::OpenAPI::toJsonValue(m_user_region_code));
    }
    return obj;
}

QString OAIFreeBookingLinksResult::getClickCount() const {
    return m_click_count;
}
void OAIFreeBookingLinksResult::setClickCount(const QString &click_count) {
    m_click_count = click_count;
    m_click_count_isSet = true;
}

bool OAIFreeBookingLinksResult::is_click_count_Set() const{
    return m_click_count_isSet;
}

bool OAIFreeBookingLinksResult::is_click_count_Valid() const{
    return m_click_count_isValid;
}

OAIDate OAIFreeBookingLinksResult::getDate() const {
    return m_date;
}
void OAIFreeBookingLinksResult::setDate(const OAIDate &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIFreeBookingLinksResult::is_date_Set() const{
    return m_date_isSet;
}

bool OAIFreeBookingLinksResult::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIFreeBookingLinksResult::getDeviceType() const {
    return m_device_type;
}
void OAIFreeBookingLinksResult::setDeviceType(const QString &device_type) {
    m_device_type = device_type;
    m_device_type_isSet = true;
}

bool OAIFreeBookingLinksResult::is_device_type_Set() const{
    return m_device_type_isSet;
}

bool OAIFreeBookingLinksResult::is_device_type_Valid() const{
    return m_device_type_isValid;
}

QString OAIFreeBookingLinksResult::getPartnerHotelDisplayName() const {
    return m_partner_hotel_display_name;
}
void OAIFreeBookingLinksResult::setPartnerHotelDisplayName(const QString &partner_hotel_display_name) {
    m_partner_hotel_display_name = partner_hotel_display_name;
    m_partner_hotel_display_name_isSet = true;
}

bool OAIFreeBookingLinksResult::is_partner_hotel_display_name_Set() const{
    return m_partner_hotel_display_name_isSet;
}

bool OAIFreeBookingLinksResult::is_partner_hotel_display_name_Valid() const{
    return m_partner_hotel_display_name_isValid;
}

QString OAIFreeBookingLinksResult::getPartnerHotelId() const {
    return m_partner_hotel_id;
}
void OAIFreeBookingLinksResult::setPartnerHotelId(const QString &partner_hotel_id) {
    m_partner_hotel_id = partner_hotel_id;
    m_partner_hotel_id_isSet = true;
}

bool OAIFreeBookingLinksResult::is_partner_hotel_id_Set() const{
    return m_partner_hotel_id_isSet;
}

bool OAIFreeBookingLinksResult::is_partner_hotel_id_Valid() const{
    return m_partner_hotel_id_isValid;
}

QString OAIFreeBookingLinksResult::getUserRegionCode() const {
    return m_user_region_code;
}
void OAIFreeBookingLinksResult::setUserRegionCode(const QString &user_region_code) {
    m_user_region_code = user_region_code;
    m_user_region_code_isSet = true;
}

bool OAIFreeBookingLinksResult::is_user_region_code_Set() const{
    return m_user_region_code_isSet;
}

bool OAIFreeBookingLinksResult::is_user_region_code_Valid() const{
    return m_user_region_code_isValid;
}

bool OAIFreeBookingLinksResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_click_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_partner_hotel_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_partner_hotel_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_region_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFreeBookingLinksResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
