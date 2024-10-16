/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOnlineSettingsUpdateModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOnlineSettingsUpdateModel::OAIOnlineSettingsUpdateModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOnlineSettingsUpdateModel::OAIOnlineSettingsUpdateModel() {
    this->initializeModel();
}

OAIOnlineSettingsUpdateModel::~OAIOnlineSettingsUpdateModel() {}

void OAIOnlineSettingsUpdateModel::initializeModel() {

    m_book_ahead_unit_isSet = false;
    m_book_ahead_unit_isValid = false;

    m_book_ahead_value_isSet = false;
    m_book_ahead_value_isValid = false;

    m_book_in_advance_isSet = false;
    m_book_in_advance_isValid = false;

    m_booking_timer_mins_isSet = false;
    m_booking_timer_mins_isValid = false;

    m_customer_bookings_per_day_isSet = false;
    m_customer_bookings_per_day_isValid = false;

    m_enable_world_timezones_isSet = false;
    m_enable_world_timezones_isValid = false;
}

void OAIOnlineSettingsUpdateModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOnlineSettingsUpdateModel::fromJsonObject(QJsonObject json) {

    m_book_ahead_unit_isValid = ::OpenAPI::fromJsonValue(m_book_ahead_unit, json[QString("bookAheadUnit")]);
    m_book_ahead_unit_isSet = !json[QString("bookAheadUnit")].isNull() && m_book_ahead_unit_isValid;

    m_book_ahead_value_isValid = ::OpenAPI::fromJsonValue(m_book_ahead_value, json[QString("bookAheadValue")]);
    m_book_ahead_value_isSet = !json[QString("bookAheadValue")].isNull() && m_book_ahead_value_isValid;

    m_book_in_advance_isValid = ::OpenAPI::fromJsonValue(m_book_in_advance, json[QString("bookInAdvance")]);
    m_book_in_advance_isSet = !json[QString("bookInAdvance")].isNull() && m_book_in_advance_isValid;

    m_booking_timer_mins_isValid = ::OpenAPI::fromJsonValue(m_booking_timer_mins, json[QString("bookingTimerMins")]);
    m_booking_timer_mins_isSet = !json[QString("bookingTimerMins")].isNull() && m_booking_timer_mins_isValid;

    m_customer_bookings_per_day_isValid = ::OpenAPI::fromJsonValue(m_customer_bookings_per_day, json[QString("customerBookingsPerDay")]);
    m_customer_bookings_per_day_isSet = !json[QString("customerBookingsPerDay")].isNull() && m_customer_bookings_per_day_isValid;

    m_enable_world_timezones_isValid = ::OpenAPI::fromJsonValue(m_enable_world_timezones, json[QString("enableWorldTimezones")]);
    m_enable_world_timezones_isSet = !json[QString("enableWorldTimezones")].isNull() && m_enable_world_timezones_isValid;
}

QString OAIOnlineSettingsUpdateModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOnlineSettingsUpdateModel::asJsonObject() const {
    QJsonObject obj;
    if (m_book_ahead_unit_isSet) {
        obj.insert(QString("bookAheadUnit"), ::OpenAPI::toJsonValue(m_book_ahead_unit));
    }
    if (m_book_ahead_value_isSet) {
        obj.insert(QString("bookAheadValue"), ::OpenAPI::toJsonValue(m_book_ahead_value));
    }
    if (m_book_in_advance_isSet) {
        obj.insert(QString("bookInAdvance"), ::OpenAPI::toJsonValue(m_book_in_advance));
    }
    if (m_booking_timer_mins_isSet) {
        obj.insert(QString("bookingTimerMins"), ::OpenAPI::toJsonValue(m_booking_timer_mins));
    }
    if (m_customer_bookings_per_day_isSet) {
        obj.insert(QString("customerBookingsPerDay"), ::OpenAPI::toJsonValue(m_customer_bookings_per_day));
    }
    if (m_enable_world_timezones_isSet) {
        obj.insert(QString("enableWorldTimezones"), ::OpenAPI::toJsonValue(m_enable_world_timezones));
    }
    return obj;
}

qint32 OAIOnlineSettingsUpdateModel::getBookAheadUnit() const {
    return m_book_ahead_unit;
}
void OAIOnlineSettingsUpdateModel::setBookAheadUnit(const qint32 &book_ahead_unit) {
    m_book_ahead_unit = book_ahead_unit;
    m_book_ahead_unit_isSet = true;
}

bool OAIOnlineSettingsUpdateModel::is_book_ahead_unit_Set() const{
    return m_book_ahead_unit_isSet;
}

bool OAIOnlineSettingsUpdateModel::is_book_ahead_unit_Valid() const{
    return m_book_ahead_unit_isValid;
}

qint32 OAIOnlineSettingsUpdateModel::getBookAheadValue() const {
    return m_book_ahead_value;
}
void OAIOnlineSettingsUpdateModel::setBookAheadValue(const qint32 &book_ahead_value) {
    m_book_ahead_value = book_ahead_value;
    m_book_ahead_value_isSet = true;
}

bool OAIOnlineSettingsUpdateModel::is_book_ahead_value_Set() const{
    return m_book_ahead_value_isSet;
}

bool OAIOnlineSettingsUpdateModel::is_book_ahead_value_Valid() const{
    return m_book_ahead_value_isValid;
}

qint32 OAIOnlineSettingsUpdateModel::getBookInAdvance() const {
    return m_book_in_advance;
}
void OAIOnlineSettingsUpdateModel::setBookInAdvance(const qint32 &book_in_advance) {
    m_book_in_advance = book_in_advance;
    m_book_in_advance_isSet = true;
}

bool OAIOnlineSettingsUpdateModel::is_book_in_advance_Set() const{
    return m_book_in_advance_isSet;
}

bool OAIOnlineSettingsUpdateModel::is_book_in_advance_Valid() const{
    return m_book_in_advance_isValid;
}

qint32 OAIOnlineSettingsUpdateModel::getBookingTimerMins() const {
    return m_booking_timer_mins;
}
void OAIOnlineSettingsUpdateModel::setBookingTimerMins(const qint32 &booking_timer_mins) {
    m_booking_timer_mins = booking_timer_mins;
    m_booking_timer_mins_isSet = true;
}

bool OAIOnlineSettingsUpdateModel::is_booking_timer_mins_Set() const{
    return m_booking_timer_mins_isSet;
}

bool OAIOnlineSettingsUpdateModel::is_booking_timer_mins_Valid() const{
    return m_booking_timer_mins_isValid;
}

qint32 OAIOnlineSettingsUpdateModel::getCustomerBookingsPerDay() const {
    return m_customer_bookings_per_day;
}
void OAIOnlineSettingsUpdateModel::setCustomerBookingsPerDay(const qint32 &customer_bookings_per_day) {
    m_customer_bookings_per_day = customer_bookings_per_day;
    m_customer_bookings_per_day_isSet = true;
}

bool OAIOnlineSettingsUpdateModel::is_customer_bookings_per_day_Set() const{
    return m_customer_bookings_per_day_isSet;
}

bool OAIOnlineSettingsUpdateModel::is_customer_bookings_per_day_Valid() const{
    return m_customer_bookings_per_day_isValid;
}

bool OAIOnlineSettingsUpdateModel::isEnableWorldTimezones() const {
    return m_enable_world_timezones;
}
void OAIOnlineSettingsUpdateModel::setEnableWorldTimezones(const bool &enable_world_timezones) {
    m_enable_world_timezones = enable_world_timezones;
    m_enable_world_timezones_isSet = true;
}

bool OAIOnlineSettingsUpdateModel::is_enable_world_timezones_Set() const{
    return m_enable_world_timezones_isSet;
}

bool OAIOnlineSettingsUpdateModel::is_enable_world_timezones_Valid() const{
    return m_enable_world_timezones_isValid;
}

bool OAIOnlineSettingsUpdateModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_book_ahead_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_book_ahead_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_book_in_advance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_booking_timer_mins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_bookings_per_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_world_timezones_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOnlineSettingsUpdateModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
