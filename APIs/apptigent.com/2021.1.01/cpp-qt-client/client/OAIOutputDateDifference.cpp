/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOutputDateDifference.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOutputDateDifference::OAIOutputDateDifference(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOutputDateDifference::OAIOutputDateDifference() {
    this->initializeModel();
}

OAIOutputDateDifference::~OAIOutputDateDifference() {}

void OAIOutputDateDifference::initializeModel() {

    m_days_isSet = false;
    m_days_isValid = false;

    m_hours_isSet = false;
    m_hours_isValid = false;

    m_milliseconds_isSet = false;
    m_milliseconds_isValid = false;

    m_minutes_isSet = false;
    m_minutes_isValid = false;

    m_months_isSet = false;
    m_months_isValid = false;

    m_ticks_isSet = false;
    m_ticks_isValid = false;

    m_total_days_isSet = false;
    m_total_days_isValid = false;

    m_total_hours_isSet = false;
    m_total_hours_isValid = false;

    m_total_milliseconds_isSet = false;
    m_total_milliseconds_isValid = false;

    m_total_minutes_isSet = false;
    m_total_minutes_isValid = false;

    m_total_months_isSet = false;
    m_total_months_isValid = false;

    m_total_seconds_isSet = false;
    m_total_seconds_isValid = false;

    m_total_years_isSet = false;
    m_total_years_isValid = false;

    m_years_isSet = false;
    m_years_isValid = false;
}

void OAIOutputDateDifference::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOutputDateDifference::fromJsonObject(QJsonObject json) {

    m_days_isValid = ::OpenAPI::fromJsonValue(m_days, json[QString("days")]);
    m_days_isSet = !json[QString("days")].isNull() && m_days_isValid;

    m_hours_isValid = ::OpenAPI::fromJsonValue(m_hours, json[QString("hours")]);
    m_hours_isSet = !json[QString("hours")].isNull() && m_hours_isValid;

    m_milliseconds_isValid = ::OpenAPI::fromJsonValue(m_milliseconds, json[QString("milliseconds")]);
    m_milliseconds_isSet = !json[QString("milliseconds")].isNull() && m_milliseconds_isValid;

    m_minutes_isValid = ::OpenAPI::fromJsonValue(m_minutes, json[QString("minutes")]);
    m_minutes_isSet = !json[QString("minutes")].isNull() && m_minutes_isValid;

    m_months_isValid = ::OpenAPI::fromJsonValue(m_months, json[QString("months")]);
    m_months_isSet = !json[QString("months")].isNull() && m_months_isValid;

    m_ticks_isValid = ::OpenAPI::fromJsonValue(m_ticks, json[QString("ticks")]);
    m_ticks_isSet = !json[QString("ticks")].isNull() && m_ticks_isValid;

    m_total_days_isValid = ::OpenAPI::fromJsonValue(m_total_days, json[QString("totalDays")]);
    m_total_days_isSet = !json[QString("totalDays")].isNull() && m_total_days_isValid;

    m_total_hours_isValid = ::OpenAPI::fromJsonValue(m_total_hours, json[QString("totalHours")]);
    m_total_hours_isSet = !json[QString("totalHours")].isNull() && m_total_hours_isValid;

    m_total_milliseconds_isValid = ::OpenAPI::fromJsonValue(m_total_milliseconds, json[QString("totalMilliseconds")]);
    m_total_milliseconds_isSet = !json[QString("totalMilliseconds")].isNull() && m_total_milliseconds_isValid;

    m_total_minutes_isValid = ::OpenAPI::fromJsonValue(m_total_minutes, json[QString("totalMinutes")]);
    m_total_minutes_isSet = !json[QString("totalMinutes")].isNull() && m_total_minutes_isValid;

    m_total_months_isValid = ::OpenAPI::fromJsonValue(m_total_months, json[QString("totalMonths")]);
    m_total_months_isSet = !json[QString("totalMonths")].isNull() && m_total_months_isValid;

    m_total_seconds_isValid = ::OpenAPI::fromJsonValue(m_total_seconds, json[QString("totalSeconds")]);
    m_total_seconds_isSet = !json[QString("totalSeconds")].isNull() && m_total_seconds_isValid;

    m_total_years_isValid = ::OpenAPI::fromJsonValue(m_total_years, json[QString("totalYears")]);
    m_total_years_isSet = !json[QString("totalYears")].isNull() && m_total_years_isValid;

    m_years_isValid = ::OpenAPI::fromJsonValue(m_years, json[QString("years")]);
    m_years_isSet = !json[QString("years")].isNull() && m_years_isValid;
}

QString OAIOutputDateDifference::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOutputDateDifference::asJsonObject() const {
    QJsonObject obj;
    if (m_days_isSet) {
        obj.insert(QString("days"), ::OpenAPI::toJsonValue(m_days));
    }
    if (m_hours_isSet) {
        obj.insert(QString("hours"), ::OpenAPI::toJsonValue(m_hours));
    }
    if (m_milliseconds_isSet) {
        obj.insert(QString("milliseconds"), ::OpenAPI::toJsonValue(m_milliseconds));
    }
    if (m_minutes_isSet) {
        obj.insert(QString("minutes"), ::OpenAPI::toJsonValue(m_minutes));
    }
    if (m_months_isSet) {
        obj.insert(QString("months"), ::OpenAPI::toJsonValue(m_months));
    }
    if (m_ticks_isSet) {
        obj.insert(QString("ticks"), ::OpenAPI::toJsonValue(m_ticks));
    }
    if (m_total_days_isSet) {
        obj.insert(QString("totalDays"), ::OpenAPI::toJsonValue(m_total_days));
    }
    if (m_total_hours_isSet) {
        obj.insert(QString("totalHours"), ::OpenAPI::toJsonValue(m_total_hours));
    }
    if (m_total_milliseconds_isSet) {
        obj.insert(QString("totalMilliseconds"), ::OpenAPI::toJsonValue(m_total_milliseconds));
    }
    if (m_total_minutes_isSet) {
        obj.insert(QString("totalMinutes"), ::OpenAPI::toJsonValue(m_total_minutes));
    }
    if (m_total_months_isSet) {
        obj.insert(QString("totalMonths"), ::OpenAPI::toJsonValue(m_total_months));
    }
    if (m_total_seconds_isSet) {
        obj.insert(QString("totalSeconds"), ::OpenAPI::toJsonValue(m_total_seconds));
    }
    if (m_total_years_isSet) {
        obj.insert(QString("totalYears"), ::OpenAPI::toJsonValue(m_total_years));
    }
    if (m_years_isSet) {
        obj.insert(QString("years"), ::OpenAPI::toJsonValue(m_years));
    }
    return obj;
}

double OAIOutputDateDifference::getDays() const {
    return m_days;
}
void OAIOutputDateDifference::setDays(const double &days) {
    m_days = days;
    m_days_isSet = true;
}

bool OAIOutputDateDifference::is_days_Set() const{
    return m_days_isSet;
}

bool OAIOutputDateDifference::is_days_Valid() const{
    return m_days_isValid;
}

double OAIOutputDateDifference::getHours() const {
    return m_hours;
}
void OAIOutputDateDifference::setHours(const double &hours) {
    m_hours = hours;
    m_hours_isSet = true;
}

bool OAIOutputDateDifference::is_hours_Set() const{
    return m_hours_isSet;
}

bool OAIOutputDateDifference::is_hours_Valid() const{
    return m_hours_isValid;
}

double OAIOutputDateDifference::getMilliseconds() const {
    return m_milliseconds;
}
void OAIOutputDateDifference::setMilliseconds(const double &milliseconds) {
    m_milliseconds = milliseconds;
    m_milliseconds_isSet = true;
}

bool OAIOutputDateDifference::is_milliseconds_Set() const{
    return m_milliseconds_isSet;
}

bool OAIOutputDateDifference::is_milliseconds_Valid() const{
    return m_milliseconds_isValid;
}

double OAIOutputDateDifference::getMinutes() const {
    return m_minutes;
}
void OAIOutputDateDifference::setMinutes(const double &minutes) {
    m_minutes = minutes;
    m_minutes_isSet = true;
}

bool OAIOutputDateDifference::is_minutes_Set() const{
    return m_minutes_isSet;
}

bool OAIOutputDateDifference::is_minutes_Valid() const{
    return m_minutes_isValid;
}

double OAIOutputDateDifference::getMonths() const {
    return m_months;
}
void OAIOutputDateDifference::setMonths(const double &months) {
    m_months = months;
    m_months_isSet = true;
}

bool OAIOutputDateDifference::is_months_Set() const{
    return m_months_isSet;
}

bool OAIOutputDateDifference::is_months_Valid() const{
    return m_months_isValid;
}

double OAIOutputDateDifference::getTicks() const {
    return m_ticks;
}
void OAIOutputDateDifference::setTicks(const double &ticks) {
    m_ticks = ticks;
    m_ticks_isSet = true;
}

bool OAIOutputDateDifference::is_ticks_Set() const{
    return m_ticks_isSet;
}

bool OAIOutputDateDifference::is_ticks_Valid() const{
    return m_ticks_isValid;
}

double OAIOutputDateDifference::getTotalDays() const {
    return m_total_days;
}
void OAIOutputDateDifference::setTotalDays(const double &total_days) {
    m_total_days = total_days;
    m_total_days_isSet = true;
}

bool OAIOutputDateDifference::is_total_days_Set() const{
    return m_total_days_isSet;
}

bool OAIOutputDateDifference::is_total_days_Valid() const{
    return m_total_days_isValid;
}

double OAIOutputDateDifference::getTotalHours() const {
    return m_total_hours;
}
void OAIOutputDateDifference::setTotalHours(const double &total_hours) {
    m_total_hours = total_hours;
    m_total_hours_isSet = true;
}

bool OAIOutputDateDifference::is_total_hours_Set() const{
    return m_total_hours_isSet;
}

bool OAIOutputDateDifference::is_total_hours_Valid() const{
    return m_total_hours_isValid;
}

double OAIOutputDateDifference::getTotalMilliseconds() const {
    return m_total_milliseconds;
}
void OAIOutputDateDifference::setTotalMilliseconds(const double &total_milliseconds) {
    m_total_milliseconds = total_milliseconds;
    m_total_milliseconds_isSet = true;
}

bool OAIOutputDateDifference::is_total_milliseconds_Set() const{
    return m_total_milliseconds_isSet;
}

bool OAIOutputDateDifference::is_total_milliseconds_Valid() const{
    return m_total_milliseconds_isValid;
}

double OAIOutputDateDifference::getTotalMinutes() const {
    return m_total_minutes;
}
void OAIOutputDateDifference::setTotalMinutes(const double &total_minutes) {
    m_total_minutes = total_minutes;
    m_total_minutes_isSet = true;
}

bool OAIOutputDateDifference::is_total_minutes_Set() const{
    return m_total_minutes_isSet;
}

bool OAIOutputDateDifference::is_total_minutes_Valid() const{
    return m_total_minutes_isValid;
}

double OAIOutputDateDifference::getTotalMonths() const {
    return m_total_months;
}
void OAIOutputDateDifference::setTotalMonths(const double &total_months) {
    m_total_months = total_months;
    m_total_months_isSet = true;
}

bool OAIOutputDateDifference::is_total_months_Set() const{
    return m_total_months_isSet;
}

bool OAIOutputDateDifference::is_total_months_Valid() const{
    return m_total_months_isValid;
}

double OAIOutputDateDifference::getTotalSeconds() const {
    return m_total_seconds;
}
void OAIOutputDateDifference::setTotalSeconds(const double &total_seconds) {
    m_total_seconds = total_seconds;
    m_total_seconds_isSet = true;
}

bool OAIOutputDateDifference::is_total_seconds_Set() const{
    return m_total_seconds_isSet;
}

bool OAIOutputDateDifference::is_total_seconds_Valid() const{
    return m_total_seconds_isValid;
}

double OAIOutputDateDifference::getTotalYears() const {
    return m_total_years;
}
void OAIOutputDateDifference::setTotalYears(const double &total_years) {
    m_total_years = total_years;
    m_total_years_isSet = true;
}

bool OAIOutputDateDifference::is_total_years_Set() const{
    return m_total_years_isSet;
}

bool OAIOutputDateDifference::is_total_years_Valid() const{
    return m_total_years_isValid;
}

double OAIOutputDateDifference::getYears() const {
    return m_years;
}
void OAIOutputDateDifference::setYears(const double &years) {
    m_years = years;
    m_years_isSet = true;
}

bool OAIOutputDateDifference::is_years_Set() const{
    return m_years_isSet;
}

bool OAIOutputDateDifference::is_years_Valid() const{
    return m_years_isValid;
}

bool OAIOutputDateDifference::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_days_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_milliseconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_months_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ticks_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_days_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_milliseconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_months_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_years_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_years_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOutputDateDifference::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
