/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPoint_PointDailyData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPoint_PointDailyData::OAIPoint_PointDailyData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPoint_PointDailyData::OAIPoint_PointDailyData() {
    this->initializeModel();
}

OAIPoint_PointDailyData::~OAIPoint_PointDailyData() {}

void OAIPoint_PointDailyData::initializeModel() {

    m_afternoon_isSet = false;
    m_afternoon_isValid = false;

    m_all_day_isSet = false;
    m_all_day_isValid = false;

    m_astro_isSet = false;
    m_astro_isValid = false;

    m_day_isSet = false;
    m_day_isValid = false;

    m_evening_isSet = false;
    m_evening_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_morning_isSet = false;
    m_morning_isValid = false;

    m_predictability_isSet = false;
    m_predictability_isValid = false;

    m_statistics_isSet = false;
    m_statistics_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_weather_isSet = false;
    m_weather_isValid = false;
}

void OAIPoint_PointDailyData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPoint_PointDailyData::fromJsonObject(QJsonObject json) {

    m_afternoon_isValid = ::OpenAPI::fromJsonValue(m_afternoon, json[QString("afternoon")]);
    m_afternoon_isSet = !json[QString("afternoon")].isNull() && m_afternoon_isValid;

    m_all_day_isValid = ::OpenAPI::fromJsonValue(m_all_day, json[QString("all_day")]);
    m_all_day_isSet = !json[QString("all_day")].isNull() && m_all_day_isValid;

    m_astro_isValid = ::OpenAPI::fromJsonValue(m_astro, json[QString("astro")]);
    m_astro_isSet = !json[QString("astro")].isNull() && m_astro_isValid;

    m_day_isValid = ::OpenAPI::fromJsonValue(m_day, json[QString("day")]);
    m_day_isSet = !json[QString("day")].isNull() && m_day_isValid;

    m_evening_isValid = ::OpenAPI::fromJsonValue(m_evening, json[QString("evening")]);
    m_evening_isSet = !json[QString("evening")].isNull() && m_evening_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_morning_isValid = ::OpenAPI::fromJsonValue(m_morning, json[QString("morning")]);
    m_morning_isSet = !json[QString("morning")].isNull() && m_morning_isValid;

    m_predictability_isValid = ::OpenAPI::fromJsonValue(m_predictability, json[QString("predictability")]);
    m_predictability_isSet = !json[QString("predictability")].isNull() && m_predictability_isValid;

    m_statistics_isValid = ::OpenAPI::fromJsonValue(m_statistics, json[QString("statistics")]);
    m_statistics_isSet = !json[QString("statistics")].isNull() && m_statistics_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_weather_isValid = ::OpenAPI::fromJsonValue(m_weather, json[QString("weather")]);
    m_weather_isSet = !json[QString("weather")].isNull() && m_weather_isValid;
}

QString OAIPoint_PointDailyData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPoint_PointDailyData::asJsonObject() const {
    QJsonObject obj;
    if (m_afternoon.isSet()) {
        obj.insert(QString("afternoon"), ::OpenAPI::toJsonValue(m_afternoon));
    }
    if (m_all_day.isSet()) {
        obj.insert(QString("all_day"), ::OpenAPI::toJsonValue(m_all_day));
    }
    if (m_astro.isSet()) {
        obj.insert(QString("astro"), ::OpenAPI::toJsonValue(m_astro));
    }
    if (m_day.isSet()) {
        obj.insert(QString("day"), ::OpenAPI::toJsonValue(m_day));
    }
    if (m_evening.isSet()) {
        obj.insert(QString("evening"), ::OpenAPI::toJsonValue(m_evening));
    }
    if (m_icon_isSet) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_morning.isSet()) {
        obj.insert(QString("morning"), ::OpenAPI::toJsonValue(m_morning));
    }
    if (m_predictability_isSet) {
        obj.insert(QString("predictability"), ::OpenAPI::toJsonValue(m_predictability));
    }
    if (m_statistics.isSet()) {
        obj.insert(QString("statistics"), ::OpenAPI::toJsonValue(m_statistics));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_weather_isSet) {
        obj.insert(QString("weather"), ::OpenAPI::toJsonValue(m_weather));
    }
    return obj;
}

OAIPoint_PointDailyAfternoonData OAIPoint_PointDailyData::getAfternoon() const {
    return m_afternoon;
}
void OAIPoint_PointDailyData::setAfternoon(const OAIPoint_PointDailyAfternoonData &afternoon) {
    m_afternoon = afternoon;
    m_afternoon_isSet = true;
}

bool OAIPoint_PointDailyData::is_afternoon_Set() const{
    return m_afternoon_isSet;
}

bool OAIPoint_PointDailyData::is_afternoon_Valid() const{
    return m_afternoon_isValid;
}

OAIPoint_PointDailyAllDayData OAIPoint_PointDailyData::getAllDay() const {
    return m_all_day;
}
void OAIPoint_PointDailyData::setAllDay(const OAIPoint_PointDailyAllDayData &all_day) {
    m_all_day = all_day;
    m_all_day_isSet = true;
}

bool OAIPoint_PointDailyData::is_all_day_Set() const{
    return m_all_day_isSet;
}

bool OAIPoint_PointDailyData::is_all_day_Valid() const{
    return m_all_day_isValid;
}

OAIPoint_PointDailyAstroData OAIPoint_PointDailyData::getAstro() const {
    return m_astro;
}
void OAIPoint_PointDailyData::setAstro(const OAIPoint_PointDailyAstroData &astro) {
    m_astro = astro;
    m_astro_isSet = true;
}

bool OAIPoint_PointDailyData::is_astro_Set() const{
    return m_astro_isSet;
}

bool OAIPoint_PointDailyData::is_astro_Valid() const{
    return m_astro_isValid;
}

OAIHttpFileElement OAIPoint_PointDailyData::getDay() const {
    return m_day;
}
void OAIPoint_PointDailyData::setDay(const OAIHttpFileElement &day) {
    m_day = day;
    m_day_isSet = true;
}

bool OAIPoint_PointDailyData::is_day_Set() const{
    return m_day_isSet;
}

bool OAIPoint_PointDailyData::is_day_Valid() const{
    return m_day_isValid;
}

OAIPoint_PointDailyEveningData OAIPoint_PointDailyData::getEvening() const {
    return m_evening;
}
void OAIPoint_PointDailyData::setEvening(const OAIPoint_PointDailyEveningData &evening) {
    m_evening = evening;
    m_evening_isSet = true;
}

bool OAIPoint_PointDailyData::is_evening_Set() const{
    return m_evening_isSet;
}

bool OAIPoint_PointDailyData::is_evening_Valid() const{
    return m_evening_isValid;
}

qint32 OAIPoint_PointDailyData::getIcon() const {
    return m_icon;
}
void OAIPoint_PointDailyData::setIcon(const qint32 &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAIPoint_PointDailyData::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAIPoint_PointDailyData::is_icon_Valid() const{
    return m_icon_isValid;
}

OAIPoint_PointDailyMorningData OAIPoint_PointDailyData::getMorning() const {
    return m_morning;
}
void OAIPoint_PointDailyData::setMorning(const OAIPoint_PointDailyMorningData &morning) {
    m_morning = morning;
    m_morning_isSet = true;
}

bool OAIPoint_PointDailyData::is_morning_Set() const{
    return m_morning_isSet;
}

bool OAIPoint_PointDailyData::is_morning_Valid() const{
    return m_morning_isValid;
}

qint32 OAIPoint_PointDailyData::getPredictability() const {
    return m_predictability;
}
void OAIPoint_PointDailyData::setPredictability(const qint32 &predictability) {
    m_predictability = predictability;
    m_predictability_isSet = true;
}

bool OAIPoint_PointDailyData::is_predictability_Set() const{
    return m_predictability_isSet;
}

bool OAIPoint_PointDailyData::is_predictability_Valid() const{
    return m_predictability_isValid;
}

OAIPoint_PointDailyStatsData OAIPoint_PointDailyData::getStatistics() const {
    return m_statistics;
}
void OAIPoint_PointDailyData::setStatistics(const OAIPoint_PointDailyStatsData &statistics) {
    m_statistics = statistics;
    m_statistics_isSet = true;
}

bool OAIPoint_PointDailyData::is_statistics_Set() const{
    return m_statistics_isSet;
}

bool OAIPoint_PointDailyData::is_statistics_Valid() const{
    return m_statistics_isValid;
}

QString OAIPoint_PointDailyData::getSummary() const {
    return m_summary;
}
void OAIPoint_PointDailyData::setSummary(const QString &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAIPoint_PointDailyData::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAIPoint_PointDailyData::is_summary_Valid() const{
    return m_summary_isValid;
}

QString OAIPoint_PointDailyData::getWeather() const {
    return m_weather;
}
void OAIPoint_PointDailyData::setWeather(const QString &weather) {
    m_weather = weather;
    m_weather_isSet = true;
}

bool OAIPoint_PointDailyData::is_weather_Set() const{
    return m_weather_isSet;
}

bool OAIPoint_PointDailyData::is_weather_Valid() const{
    return m_weather_isValid;
}

bool OAIPoint_PointDailyData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_afternoon.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_all_day.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_astro.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_day.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_evening.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_morning.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_predictability_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_statistics.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weather_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPoint_PointDailyData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_all_day_isValid && m_astro_isValid && m_statistics_isValid && true;
}

} // namespace OpenAPI
