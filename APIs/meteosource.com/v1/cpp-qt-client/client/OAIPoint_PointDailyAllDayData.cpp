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

#include "OAIPoint_PointDailyAllDayData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPoint_PointDailyAllDayData::OAIPoint_PointDailyAllDayData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPoint_PointDailyAllDayData::OAIPoint_PointDailyAllDayData() {
    this->initializeModel();
}

OAIPoint_PointDailyAllDayData::~OAIPoint_PointDailyAllDayData() {}

void OAIPoint_PointDailyAllDayData::initializeModel() {

    m_cloud_cover_isSet = false;
    m_cloud_cover_isValid = false;

    m_dew_point_isSet = false;
    m_dew_point_isValid = false;

    m_dew_point_max_isSet = false;
    m_dew_point_max_isValid = false;

    m_dew_point_min_isSet = false;
    m_dew_point_min_isValid = false;

    m_feels_like_isSet = false;
    m_feels_like_isValid = false;

    m_feels_like_max_isSet = false;
    m_feels_like_max_isValid = false;

    m_feels_like_min_isSet = false;
    m_feels_like_min_isValid = false;

    m_humidity_isSet = false;
    m_humidity_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_ozone_isSet = false;
    m_ozone_isValid = false;

    m_precipitation_isSet = false;
    m_precipitation_isValid = false;

    m_pressure_isSet = false;
    m_pressure_isValid = false;

    m_probability_isSet = false;
    m_probability_isValid = false;

    m_snow_depth_isSet = false;
    m_snow_depth_isValid = false;

    m_soil_temperature_isSet = false;
    m_soil_temperature_isValid = false;

    m_soil_temperature_max_isSet = false;
    m_soil_temperature_max_isValid = false;

    m_soil_temperature_min_isSet = false;
    m_soil_temperature_min_isValid = false;

    m_surface_temperature_isSet = false;
    m_surface_temperature_isValid = false;

    m_surface_temperature_max_isSet = false;
    m_surface_temperature_max_isValid = false;

    m_surface_temperature_min_isSet = false;
    m_surface_temperature_min_isValid = false;

    m_temperature_isSet = false;
    m_temperature_isValid = false;

    m_temperature_max_isSet = false;
    m_temperature_max_isValid = false;

    m_temperature_min_isSet = false;
    m_temperature_min_isValid = false;

    m_visibility_isSet = false;
    m_visibility_isValid = false;

    m_weather_isSet = false;
    m_weather_isValid = false;

    m_wind_isSet = false;
    m_wind_isValid = false;

    m_wind_chill_isSet = false;
    m_wind_chill_isValid = false;

    m_wind_chill_max_isSet = false;
    m_wind_chill_max_isValid = false;

    m_wind_chill_min_isSet = false;
    m_wind_chill_min_isValid = false;
}

void OAIPoint_PointDailyAllDayData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPoint_PointDailyAllDayData::fromJsonObject(QJsonObject json) {

    m_cloud_cover_isValid = ::OpenAPI::fromJsonValue(m_cloud_cover, json[QString("cloud_cover")]);
    m_cloud_cover_isSet = !json[QString("cloud_cover")].isNull() && m_cloud_cover_isValid;

    m_dew_point_isValid = ::OpenAPI::fromJsonValue(m_dew_point, json[QString("dew_point")]);
    m_dew_point_isSet = !json[QString("dew_point")].isNull() && m_dew_point_isValid;

    m_dew_point_max_isValid = ::OpenAPI::fromJsonValue(m_dew_point_max, json[QString("dew_point_max")]);
    m_dew_point_max_isSet = !json[QString("dew_point_max")].isNull() && m_dew_point_max_isValid;

    m_dew_point_min_isValid = ::OpenAPI::fromJsonValue(m_dew_point_min, json[QString("dew_point_min")]);
    m_dew_point_min_isSet = !json[QString("dew_point_min")].isNull() && m_dew_point_min_isValid;

    m_feels_like_isValid = ::OpenAPI::fromJsonValue(m_feels_like, json[QString("feels_like")]);
    m_feels_like_isSet = !json[QString("feels_like")].isNull() && m_feels_like_isValid;

    m_feels_like_max_isValid = ::OpenAPI::fromJsonValue(m_feels_like_max, json[QString("feels_like_max")]);
    m_feels_like_max_isSet = !json[QString("feels_like_max")].isNull() && m_feels_like_max_isValid;

    m_feels_like_min_isValid = ::OpenAPI::fromJsonValue(m_feels_like_min, json[QString("feels_like_min")]);
    m_feels_like_min_isSet = !json[QString("feels_like_min")].isNull() && m_feels_like_min_isValid;

    m_humidity_isValid = ::OpenAPI::fromJsonValue(m_humidity, json[QString("humidity")]);
    m_humidity_isSet = !json[QString("humidity")].isNull() && m_humidity_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_ozone_isValid = ::OpenAPI::fromJsonValue(m_ozone, json[QString("ozone")]);
    m_ozone_isSet = !json[QString("ozone")].isNull() && m_ozone_isValid;

    m_precipitation_isValid = ::OpenAPI::fromJsonValue(m_precipitation, json[QString("precipitation")]);
    m_precipitation_isSet = !json[QString("precipitation")].isNull() && m_precipitation_isValid;

    m_pressure_isValid = ::OpenAPI::fromJsonValue(m_pressure, json[QString("pressure")]);
    m_pressure_isSet = !json[QString("pressure")].isNull() && m_pressure_isValid;

    m_probability_isValid = ::OpenAPI::fromJsonValue(m_probability, json[QString("probability")]);
    m_probability_isSet = !json[QString("probability")].isNull() && m_probability_isValid;

    m_snow_depth_isValid = ::OpenAPI::fromJsonValue(m_snow_depth, json[QString("snow_depth")]);
    m_snow_depth_isSet = !json[QString("snow_depth")].isNull() && m_snow_depth_isValid;

    m_soil_temperature_isValid = ::OpenAPI::fromJsonValue(m_soil_temperature, json[QString("soil_temperature")]);
    m_soil_temperature_isSet = !json[QString("soil_temperature")].isNull() && m_soil_temperature_isValid;

    m_soil_temperature_max_isValid = ::OpenAPI::fromJsonValue(m_soil_temperature_max, json[QString("soil_temperature_max")]);
    m_soil_temperature_max_isSet = !json[QString("soil_temperature_max")].isNull() && m_soil_temperature_max_isValid;

    m_soil_temperature_min_isValid = ::OpenAPI::fromJsonValue(m_soil_temperature_min, json[QString("soil_temperature_min")]);
    m_soil_temperature_min_isSet = !json[QString("soil_temperature_min")].isNull() && m_soil_temperature_min_isValid;

    m_surface_temperature_isValid = ::OpenAPI::fromJsonValue(m_surface_temperature, json[QString("surface_temperature")]);
    m_surface_temperature_isSet = !json[QString("surface_temperature")].isNull() && m_surface_temperature_isValid;

    m_surface_temperature_max_isValid = ::OpenAPI::fromJsonValue(m_surface_temperature_max, json[QString("surface_temperature_max")]);
    m_surface_temperature_max_isSet = !json[QString("surface_temperature_max")].isNull() && m_surface_temperature_max_isValid;

    m_surface_temperature_min_isValid = ::OpenAPI::fromJsonValue(m_surface_temperature_min, json[QString("surface_temperature_min")]);
    m_surface_temperature_min_isSet = !json[QString("surface_temperature_min")].isNull() && m_surface_temperature_min_isValid;

    m_temperature_isValid = ::OpenAPI::fromJsonValue(m_temperature, json[QString("temperature")]);
    m_temperature_isSet = !json[QString("temperature")].isNull() && m_temperature_isValid;

    m_temperature_max_isValid = ::OpenAPI::fromJsonValue(m_temperature_max, json[QString("temperature_max")]);
    m_temperature_max_isSet = !json[QString("temperature_max")].isNull() && m_temperature_max_isValid;

    m_temperature_min_isValid = ::OpenAPI::fromJsonValue(m_temperature_min, json[QString("temperature_min")]);
    m_temperature_min_isSet = !json[QString("temperature_min")].isNull() && m_temperature_min_isValid;

    m_visibility_isValid = ::OpenAPI::fromJsonValue(m_visibility, json[QString("visibility")]);
    m_visibility_isSet = !json[QString("visibility")].isNull() && m_visibility_isValid;

    m_weather_isValid = ::OpenAPI::fromJsonValue(m_weather, json[QString("weather")]);
    m_weather_isSet = !json[QString("weather")].isNull() && m_weather_isValid;

    m_wind_isValid = ::OpenAPI::fromJsonValue(m_wind, json[QString("wind")]);
    m_wind_isSet = !json[QString("wind")].isNull() && m_wind_isValid;

    m_wind_chill_isValid = ::OpenAPI::fromJsonValue(m_wind_chill, json[QString("wind_chill")]);
    m_wind_chill_isSet = !json[QString("wind_chill")].isNull() && m_wind_chill_isValid;

    m_wind_chill_max_isValid = ::OpenAPI::fromJsonValue(m_wind_chill_max, json[QString("wind_chill_max")]);
    m_wind_chill_max_isSet = !json[QString("wind_chill_max")].isNull() && m_wind_chill_max_isValid;

    m_wind_chill_min_isValid = ::OpenAPI::fromJsonValue(m_wind_chill_min, json[QString("wind_chill_min")]);
    m_wind_chill_min_isSet = !json[QString("wind_chill_min")].isNull() && m_wind_chill_min_isValid;
}

QString OAIPoint_PointDailyAllDayData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPoint_PointDailyAllDayData::asJsonObject() const {
    QJsonObject obj;
    if (m_cloud_cover.isSet()) {
        obj.insert(QString("cloud_cover"), ::OpenAPI::toJsonValue(m_cloud_cover));
    }
    if (m_dew_point_isSet) {
        obj.insert(QString("dew_point"), ::OpenAPI::toJsonValue(m_dew_point));
    }
    if (m_dew_point_max_isSet) {
        obj.insert(QString("dew_point_max"), ::OpenAPI::toJsonValue(m_dew_point_max));
    }
    if (m_dew_point_min_isSet) {
        obj.insert(QString("dew_point_min"), ::OpenAPI::toJsonValue(m_dew_point_min));
    }
    if (m_feels_like_isSet) {
        obj.insert(QString("feels_like"), ::OpenAPI::toJsonValue(m_feels_like));
    }
    if (m_feels_like_max_isSet) {
        obj.insert(QString("feels_like_max"), ::OpenAPI::toJsonValue(m_feels_like_max));
    }
    if (m_feels_like_min_isSet) {
        obj.insert(QString("feels_like_min"), ::OpenAPI::toJsonValue(m_feels_like_min));
    }
    if (m_humidity_isSet) {
        obj.insert(QString("humidity"), ::OpenAPI::toJsonValue(m_humidity));
    }
    if (m_icon_isSet) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_ozone_isSet) {
        obj.insert(QString("ozone"), ::OpenAPI::toJsonValue(m_ozone));
    }
    if (m_precipitation.isSet()) {
        obj.insert(QString("precipitation"), ::OpenAPI::toJsonValue(m_precipitation));
    }
    if (m_pressure_isSet) {
        obj.insert(QString("pressure"), ::OpenAPI::toJsonValue(m_pressure));
    }
    if (m_probability.isSet()) {
        obj.insert(QString("probability"), ::OpenAPI::toJsonValue(m_probability));
    }
    if (m_snow_depth_isSet) {
        obj.insert(QString("snow_depth"), ::OpenAPI::toJsonValue(m_snow_depth));
    }
    if (m_soil_temperature_isSet) {
        obj.insert(QString("soil_temperature"), ::OpenAPI::toJsonValue(m_soil_temperature));
    }
    if (m_soil_temperature_max_isSet) {
        obj.insert(QString("soil_temperature_max"), ::OpenAPI::toJsonValue(m_soil_temperature_max));
    }
    if (m_soil_temperature_min_isSet) {
        obj.insert(QString("soil_temperature_min"), ::OpenAPI::toJsonValue(m_soil_temperature_min));
    }
    if (m_surface_temperature_isSet) {
        obj.insert(QString("surface_temperature"), ::OpenAPI::toJsonValue(m_surface_temperature));
    }
    if (m_surface_temperature_max_isSet) {
        obj.insert(QString("surface_temperature_max"), ::OpenAPI::toJsonValue(m_surface_temperature_max));
    }
    if (m_surface_temperature_min_isSet) {
        obj.insert(QString("surface_temperature_min"), ::OpenAPI::toJsonValue(m_surface_temperature_min));
    }
    if (m_temperature_isSet) {
        obj.insert(QString("temperature"), ::OpenAPI::toJsonValue(m_temperature));
    }
    if (m_temperature_max_isSet) {
        obj.insert(QString("temperature_max"), ::OpenAPI::toJsonValue(m_temperature_max));
    }
    if (m_temperature_min_isSet) {
        obj.insert(QString("temperature_min"), ::OpenAPI::toJsonValue(m_temperature_min));
    }
    if (m_visibility_isSet) {
        obj.insert(QString("visibility"), ::OpenAPI::toJsonValue(m_visibility));
    }
    if (m_weather_isSet) {
        obj.insert(QString("weather"), ::OpenAPI::toJsonValue(m_weather));
    }
    if (m_wind.isSet()) {
        obj.insert(QString("wind"), ::OpenAPI::toJsonValue(m_wind));
    }
    if (m_wind_chill_isSet) {
        obj.insert(QString("wind_chill"), ::OpenAPI::toJsonValue(m_wind_chill));
    }
    if (m_wind_chill_max_isSet) {
        obj.insert(QString("wind_chill_max"), ::OpenAPI::toJsonValue(m_wind_chill_max));
    }
    if (m_wind_chill_min_isSet) {
        obj.insert(QString("wind_chill_min"), ::OpenAPI::toJsonValue(m_wind_chill_min));
    }
    return obj;
}

OAIPoint_PointDailyAllDayCloudCoverData OAIPoint_PointDailyAllDayData::getCloudCover() const {
    return m_cloud_cover;
}
void OAIPoint_PointDailyAllDayData::setCloudCover(const OAIPoint_PointDailyAllDayCloudCoverData &cloud_cover) {
    m_cloud_cover = cloud_cover;
    m_cloud_cover_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_cloud_cover_Set() const{
    return m_cloud_cover_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_cloud_cover_Valid() const{
    return m_cloud_cover_isValid;
}

double OAIPoint_PointDailyAllDayData::getDewPoint() const {
    return m_dew_point;
}
void OAIPoint_PointDailyAllDayData::setDewPoint(const double &dew_point) {
    m_dew_point = dew_point;
    m_dew_point_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_dew_point_Set() const{
    return m_dew_point_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_dew_point_Valid() const{
    return m_dew_point_isValid;
}

double OAIPoint_PointDailyAllDayData::getDewPointMax() const {
    return m_dew_point_max;
}
void OAIPoint_PointDailyAllDayData::setDewPointMax(const double &dew_point_max) {
    m_dew_point_max = dew_point_max;
    m_dew_point_max_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_dew_point_max_Set() const{
    return m_dew_point_max_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_dew_point_max_Valid() const{
    return m_dew_point_max_isValid;
}

double OAIPoint_PointDailyAllDayData::getDewPointMin() const {
    return m_dew_point_min;
}
void OAIPoint_PointDailyAllDayData::setDewPointMin(const double &dew_point_min) {
    m_dew_point_min = dew_point_min;
    m_dew_point_min_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_dew_point_min_Set() const{
    return m_dew_point_min_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_dew_point_min_Valid() const{
    return m_dew_point_min_isValid;
}

double OAIPoint_PointDailyAllDayData::getFeelsLike() const {
    return m_feels_like;
}
void OAIPoint_PointDailyAllDayData::setFeelsLike(const double &feels_like) {
    m_feels_like = feels_like;
    m_feels_like_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_feels_like_Set() const{
    return m_feels_like_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_feels_like_Valid() const{
    return m_feels_like_isValid;
}

double OAIPoint_PointDailyAllDayData::getFeelsLikeMax() const {
    return m_feels_like_max;
}
void OAIPoint_PointDailyAllDayData::setFeelsLikeMax(const double &feels_like_max) {
    m_feels_like_max = feels_like_max;
    m_feels_like_max_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_feels_like_max_Set() const{
    return m_feels_like_max_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_feels_like_max_Valid() const{
    return m_feels_like_max_isValid;
}

double OAIPoint_PointDailyAllDayData::getFeelsLikeMin() const {
    return m_feels_like_min;
}
void OAIPoint_PointDailyAllDayData::setFeelsLikeMin(const double &feels_like_min) {
    m_feels_like_min = feels_like_min;
    m_feels_like_min_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_feels_like_min_Set() const{
    return m_feels_like_min_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_feels_like_min_Valid() const{
    return m_feels_like_min_isValid;
}

qint32 OAIPoint_PointDailyAllDayData::getHumidity() const {
    return m_humidity;
}
void OAIPoint_PointDailyAllDayData::setHumidity(const qint32 &humidity) {
    m_humidity = humidity;
    m_humidity_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_humidity_Set() const{
    return m_humidity_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_humidity_Valid() const{
    return m_humidity_isValid;
}

qint32 OAIPoint_PointDailyAllDayData::getIcon() const {
    return m_icon;
}
void OAIPoint_PointDailyAllDayData::setIcon(const qint32 &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_icon_Valid() const{
    return m_icon_isValid;
}

double OAIPoint_PointDailyAllDayData::getOzone() const {
    return m_ozone;
}
void OAIPoint_PointDailyAllDayData::setOzone(const double &ozone) {
    m_ozone = ozone;
    m_ozone_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_ozone_Set() const{
    return m_ozone_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_ozone_Valid() const{
    return m_ozone_isValid;
}

OAIPoint_PointDailyAllDayPrecipitationData OAIPoint_PointDailyAllDayData::getPrecipitation() const {
    return m_precipitation;
}
void OAIPoint_PointDailyAllDayData::setPrecipitation(const OAIPoint_PointDailyAllDayPrecipitationData &precipitation) {
    m_precipitation = precipitation;
    m_precipitation_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_precipitation_Set() const{
    return m_precipitation_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_precipitation_Valid() const{
    return m_precipitation_isValid;
}

double OAIPoint_PointDailyAllDayData::getPressure() const {
    return m_pressure;
}
void OAIPoint_PointDailyAllDayData::setPressure(const double &pressure) {
    m_pressure = pressure;
    m_pressure_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_pressure_Set() const{
    return m_pressure_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_pressure_Valid() const{
    return m_pressure_isValid;
}

OAIPoint_PointDailyAllDayProbData OAIPoint_PointDailyAllDayData::getProbability() const {
    return m_probability;
}
void OAIPoint_PointDailyAllDayData::setProbability(const OAIPoint_PointDailyAllDayProbData &probability) {
    m_probability = probability;
    m_probability_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_probability_Set() const{
    return m_probability_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_probability_Valid() const{
    return m_probability_isValid;
}

double OAIPoint_PointDailyAllDayData::getSnowDepth() const {
    return m_snow_depth;
}
void OAIPoint_PointDailyAllDayData::setSnowDepth(const double &snow_depth) {
    m_snow_depth = snow_depth;
    m_snow_depth_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_snow_depth_Set() const{
    return m_snow_depth_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_snow_depth_Valid() const{
    return m_snow_depth_isValid;
}

double OAIPoint_PointDailyAllDayData::getSoilTemperature() const {
    return m_soil_temperature;
}
void OAIPoint_PointDailyAllDayData::setSoilTemperature(const double &soil_temperature) {
    m_soil_temperature = soil_temperature;
    m_soil_temperature_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_soil_temperature_Set() const{
    return m_soil_temperature_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_soil_temperature_Valid() const{
    return m_soil_temperature_isValid;
}

double OAIPoint_PointDailyAllDayData::getSoilTemperatureMax() const {
    return m_soil_temperature_max;
}
void OAIPoint_PointDailyAllDayData::setSoilTemperatureMax(const double &soil_temperature_max) {
    m_soil_temperature_max = soil_temperature_max;
    m_soil_temperature_max_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_soil_temperature_max_Set() const{
    return m_soil_temperature_max_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_soil_temperature_max_Valid() const{
    return m_soil_temperature_max_isValid;
}

double OAIPoint_PointDailyAllDayData::getSoilTemperatureMin() const {
    return m_soil_temperature_min;
}
void OAIPoint_PointDailyAllDayData::setSoilTemperatureMin(const double &soil_temperature_min) {
    m_soil_temperature_min = soil_temperature_min;
    m_soil_temperature_min_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_soil_temperature_min_Set() const{
    return m_soil_temperature_min_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_soil_temperature_min_Valid() const{
    return m_soil_temperature_min_isValid;
}

double OAIPoint_PointDailyAllDayData::getSurfaceTemperature() const {
    return m_surface_temperature;
}
void OAIPoint_PointDailyAllDayData::setSurfaceTemperature(const double &surface_temperature) {
    m_surface_temperature = surface_temperature;
    m_surface_temperature_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_surface_temperature_Set() const{
    return m_surface_temperature_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_surface_temperature_Valid() const{
    return m_surface_temperature_isValid;
}

double OAIPoint_PointDailyAllDayData::getSurfaceTemperatureMax() const {
    return m_surface_temperature_max;
}
void OAIPoint_PointDailyAllDayData::setSurfaceTemperatureMax(const double &surface_temperature_max) {
    m_surface_temperature_max = surface_temperature_max;
    m_surface_temperature_max_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_surface_temperature_max_Set() const{
    return m_surface_temperature_max_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_surface_temperature_max_Valid() const{
    return m_surface_temperature_max_isValid;
}

double OAIPoint_PointDailyAllDayData::getSurfaceTemperatureMin() const {
    return m_surface_temperature_min;
}
void OAIPoint_PointDailyAllDayData::setSurfaceTemperatureMin(const double &surface_temperature_min) {
    m_surface_temperature_min = surface_temperature_min;
    m_surface_temperature_min_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_surface_temperature_min_Set() const{
    return m_surface_temperature_min_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_surface_temperature_min_Valid() const{
    return m_surface_temperature_min_isValid;
}

double OAIPoint_PointDailyAllDayData::getTemperature() const {
    return m_temperature;
}
void OAIPoint_PointDailyAllDayData::setTemperature(const double &temperature) {
    m_temperature = temperature;
    m_temperature_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_temperature_Set() const{
    return m_temperature_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_temperature_Valid() const{
    return m_temperature_isValid;
}

double OAIPoint_PointDailyAllDayData::getTemperatureMax() const {
    return m_temperature_max;
}
void OAIPoint_PointDailyAllDayData::setTemperatureMax(const double &temperature_max) {
    m_temperature_max = temperature_max;
    m_temperature_max_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_temperature_max_Set() const{
    return m_temperature_max_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_temperature_max_Valid() const{
    return m_temperature_max_isValid;
}

double OAIPoint_PointDailyAllDayData::getTemperatureMin() const {
    return m_temperature_min;
}
void OAIPoint_PointDailyAllDayData::setTemperatureMin(const double &temperature_min) {
    m_temperature_min = temperature_min;
    m_temperature_min_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_temperature_min_Set() const{
    return m_temperature_min_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_temperature_min_Valid() const{
    return m_temperature_min_isValid;
}

double OAIPoint_PointDailyAllDayData::getVisibility() const {
    return m_visibility;
}
void OAIPoint_PointDailyAllDayData::setVisibility(const double &visibility) {
    m_visibility = visibility;
    m_visibility_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_visibility_Set() const{
    return m_visibility_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_visibility_Valid() const{
    return m_visibility_isValid;
}

QString OAIPoint_PointDailyAllDayData::getWeather() const {
    return m_weather;
}
void OAIPoint_PointDailyAllDayData::setWeather(const QString &weather) {
    m_weather = weather;
    m_weather_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_weather_Set() const{
    return m_weather_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_weather_Valid() const{
    return m_weather_isValid;
}

OAIPoint_PointDailyAllDayWindData OAIPoint_PointDailyAllDayData::getWind() const {
    return m_wind;
}
void OAIPoint_PointDailyAllDayData::setWind(const OAIPoint_PointDailyAllDayWindData &wind) {
    m_wind = wind;
    m_wind_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_wind_Set() const{
    return m_wind_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_wind_Valid() const{
    return m_wind_isValid;
}

double OAIPoint_PointDailyAllDayData::getWindChill() const {
    return m_wind_chill;
}
void OAIPoint_PointDailyAllDayData::setWindChill(const double &wind_chill) {
    m_wind_chill = wind_chill;
    m_wind_chill_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_wind_chill_Set() const{
    return m_wind_chill_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_wind_chill_Valid() const{
    return m_wind_chill_isValid;
}

double OAIPoint_PointDailyAllDayData::getWindChillMax() const {
    return m_wind_chill_max;
}
void OAIPoint_PointDailyAllDayData::setWindChillMax(const double &wind_chill_max) {
    m_wind_chill_max = wind_chill_max;
    m_wind_chill_max_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_wind_chill_max_Set() const{
    return m_wind_chill_max_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_wind_chill_max_Valid() const{
    return m_wind_chill_max_isValid;
}

double OAIPoint_PointDailyAllDayData::getWindChillMin() const {
    return m_wind_chill_min;
}
void OAIPoint_PointDailyAllDayData::setWindChillMin(const double &wind_chill_min) {
    m_wind_chill_min = wind_chill_min;
    m_wind_chill_min_isSet = true;
}

bool OAIPoint_PointDailyAllDayData::is_wind_chill_min_Set() const{
    return m_wind_chill_min_isSet;
}

bool OAIPoint_PointDailyAllDayData::is_wind_chill_min_Valid() const{
    return m_wind_chill_min_isValid;
}

bool OAIPoint_PointDailyAllDayData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cloud_cover.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dew_point_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dew_point_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dew_point_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feels_like_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feels_like_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feels_like_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_humidity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ozone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_precipitation.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pressure_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_probability.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_snow_depth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_soil_temperature_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_soil_temperature_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_soil_temperature_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surface_temperature_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surface_temperature_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surface_temperature_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_temperature_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_temperature_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_temperature_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_visibility_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weather_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wind.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_wind_chill_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wind_chill_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wind_chill_min_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPoint_PointDailyAllDayData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_cloud_cover_isValid && m_precipitation_isValid && m_probability_isValid && m_wind_isValid && true;
}

} // namespace OpenAPI
