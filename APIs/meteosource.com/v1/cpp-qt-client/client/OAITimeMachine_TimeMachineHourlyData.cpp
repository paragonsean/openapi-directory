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

#include "OAITimeMachine_TimeMachineHourlyData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITimeMachine_TimeMachineHourlyData::OAITimeMachine_TimeMachineHourlyData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITimeMachine_TimeMachineHourlyData::OAITimeMachine_TimeMachineHourlyData() {
    this->initializeModel();
}

OAITimeMachine_TimeMachineHourlyData::~OAITimeMachine_TimeMachineHourlyData() {}

void OAITimeMachine_TimeMachineHourlyData::initializeModel() {

    m_cape_isSet = false;
    m_cape_isValid = false;

    m_cloud_cover_isSet = false;
    m_cloud_cover_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_dew_point_isSet = false;
    m_dew_point_isValid = false;

    m_evaporation_isSet = false;
    m_evaporation_isValid = false;

    m_feels_like_isSet = false;
    m_feels_like_isValid = false;

    m_humidity_isSet = false;
    m_humidity_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_irradiance_isSet = false;
    m_irradiance_isValid = false;

    m_ozone_isSet = false;
    m_ozone_isValid = false;

    m_precipitation_isSet = false;
    m_precipitation_isValid = false;

    m_pressure_isSet = false;
    m_pressure_isValid = false;

    m_soil_temperature_isSet = false;
    m_soil_temperature_isValid = false;

    m_surface_temperature_isSet = false;
    m_surface_temperature_isValid = false;

    m_temperature_isSet = false;
    m_temperature_isValid = false;

    m_weather_isSet = false;
    m_weather_isValid = false;

    m_wind_isSet = false;
    m_wind_isValid = false;

    m_wind_chill_isSet = false;
    m_wind_chill_isValid = false;
}

void OAITimeMachine_TimeMachineHourlyData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITimeMachine_TimeMachineHourlyData::fromJsonObject(QJsonObject json) {

    m_cape_isValid = ::OpenAPI::fromJsonValue(m_cape, json[QString("cape")]);
    m_cape_isSet = !json[QString("cape")].isNull() && m_cape_isValid;

    m_cloud_cover_isValid = ::OpenAPI::fromJsonValue(m_cloud_cover, json[QString("cloud_cover")]);
    m_cloud_cover_isSet = !json[QString("cloud_cover")].isNull() && m_cloud_cover_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_dew_point_isValid = ::OpenAPI::fromJsonValue(m_dew_point, json[QString("dew_point")]);
    m_dew_point_isSet = !json[QString("dew_point")].isNull() && m_dew_point_isValid;

    m_evaporation_isValid = ::OpenAPI::fromJsonValue(m_evaporation, json[QString("evaporation")]);
    m_evaporation_isSet = !json[QString("evaporation")].isNull() && m_evaporation_isValid;

    m_feels_like_isValid = ::OpenAPI::fromJsonValue(m_feels_like, json[QString("feels_like")]);
    m_feels_like_isSet = !json[QString("feels_like")].isNull() && m_feels_like_isValid;

    m_humidity_isValid = ::OpenAPI::fromJsonValue(m_humidity, json[QString("humidity")]);
    m_humidity_isSet = !json[QString("humidity")].isNull() && m_humidity_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_irradiance_isValid = ::OpenAPI::fromJsonValue(m_irradiance, json[QString("irradiance")]);
    m_irradiance_isSet = !json[QString("irradiance")].isNull() && m_irradiance_isValid;

    m_ozone_isValid = ::OpenAPI::fromJsonValue(m_ozone, json[QString("ozone")]);
    m_ozone_isSet = !json[QString("ozone")].isNull() && m_ozone_isValid;

    m_precipitation_isValid = ::OpenAPI::fromJsonValue(m_precipitation, json[QString("precipitation")]);
    m_precipitation_isSet = !json[QString("precipitation")].isNull() && m_precipitation_isValid;

    m_pressure_isValid = ::OpenAPI::fromJsonValue(m_pressure, json[QString("pressure")]);
    m_pressure_isSet = !json[QString("pressure")].isNull() && m_pressure_isValid;

    m_soil_temperature_isValid = ::OpenAPI::fromJsonValue(m_soil_temperature, json[QString("soil_temperature")]);
    m_soil_temperature_isSet = !json[QString("soil_temperature")].isNull() && m_soil_temperature_isValid;

    m_surface_temperature_isValid = ::OpenAPI::fromJsonValue(m_surface_temperature, json[QString("surface_temperature")]);
    m_surface_temperature_isSet = !json[QString("surface_temperature")].isNull() && m_surface_temperature_isValid;

    m_temperature_isValid = ::OpenAPI::fromJsonValue(m_temperature, json[QString("temperature")]);
    m_temperature_isSet = !json[QString("temperature")].isNull() && m_temperature_isValid;

    m_weather_isValid = ::OpenAPI::fromJsonValue(m_weather, json[QString("weather")]);
    m_weather_isSet = !json[QString("weather")].isNull() && m_weather_isValid;

    m_wind_isValid = ::OpenAPI::fromJsonValue(m_wind, json[QString("wind")]);
    m_wind_isSet = !json[QString("wind")].isNull() && m_wind_isValid;

    m_wind_chill_isValid = ::OpenAPI::fromJsonValue(m_wind_chill, json[QString("wind_chill")]);
    m_wind_chill_isSet = !json[QString("wind_chill")].isNull() && m_wind_chill_isValid;
}

QString OAITimeMachine_TimeMachineHourlyData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITimeMachine_TimeMachineHourlyData::asJsonObject() const {
    QJsonObject obj;
    if (m_cape_isSet) {
        obj.insert(QString("cape"), ::OpenAPI::toJsonValue(m_cape));
    }
    if (m_cloud_cover.isSet()) {
        obj.insert(QString("cloud_cover"), ::OpenAPI::toJsonValue(m_cloud_cover));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_dew_point_isSet) {
        obj.insert(QString("dew_point"), ::OpenAPI::toJsonValue(m_dew_point));
    }
    if (m_evaporation_isSet) {
        obj.insert(QString("evaporation"), ::OpenAPI::toJsonValue(m_evaporation));
    }
    if (m_feels_like_isSet) {
        obj.insert(QString("feels_like"), ::OpenAPI::toJsonValue(m_feels_like));
    }
    if (m_humidity_isSet) {
        obj.insert(QString("humidity"), ::OpenAPI::toJsonValue(m_humidity));
    }
    if (m_icon_isSet) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_irradiance_isSet) {
        obj.insert(QString("irradiance"), ::OpenAPI::toJsonValue(m_irradiance));
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
    if (m_soil_temperature_isSet) {
        obj.insert(QString("soil_temperature"), ::OpenAPI::toJsonValue(m_soil_temperature));
    }
    if (m_surface_temperature_isSet) {
        obj.insert(QString("surface_temperature"), ::OpenAPI::toJsonValue(m_surface_temperature));
    }
    if (m_temperature_isSet) {
        obj.insert(QString("temperature"), ::OpenAPI::toJsonValue(m_temperature));
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
    return obj;
}

qint32 OAITimeMachine_TimeMachineHourlyData::getCape() const {
    return m_cape;
}
void OAITimeMachine_TimeMachineHourlyData::setCape(const qint32 &cape) {
    m_cape = cape;
    m_cape_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_cape_Set() const{
    return m_cape_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_cape_Valid() const{
    return m_cape_isValid;
}

OAITimeMachine_TimeMachineCloudCoverData OAITimeMachine_TimeMachineHourlyData::getCloudCover() const {
    return m_cloud_cover;
}
void OAITimeMachine_TimeMachineHourlyData::setCloudCover(const OAITimeMachine_TimeMachineCloudCoverData &cloud_cover) {
    m_cloud_cover = cloud_cover;
    m_cloud_cover_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_cloud_cover_Set() const{
    return m_cloud_cover_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_cloud_cover_Valid() const{
    return m_cloud_cover_isValid;
}

QDateTime OAITimeMachine_TimeMachineHourlyData::getDate() const {
    return m_date;
}
void OAITimeMachine_TimeMachineHourlyData::setDate(const QDateTime &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_date_Set() const{
    return m_date_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_date_Valid() const{
    return m_date_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getDewPoint() const {
    return m_dew_point;
}
void OAITimeMachine_TimeMachineHourlyData::setDewPoint(const double &dew_point) {
    m_dew_point = dew_point;
    m_dew_point_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_dew_point_Set() const{
    return m_dew_point_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_dew_point_Valid() const{
    return m_dew_point_isValid;
}

qint32 OAITimeMachine_TimeMachineHourlyData::getEvaporation() const {
    return m_evaporation;
}
void OAITimeMachine_TimeMachineHourlyData::setEvaporation(const qint32 &evaporation) {
    m_evaporation = evaporation;
    m_evaporation_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_evaporation_Set() const{
    return m_evaporation_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_evaporation_Valid() const{
    return m_evaporation_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getFeelsLike() const {
    return m_feels_like;
}
void OAITimeMachine_TimeMachineHourlyData::setFeelsLike(const double &feels_like) {
    m_feels_like = feels_like;
    m_feels_like_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_feels_like_Set() const{
    return m_feels_like_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_feels_like_Valid() const{
    return m_feels_like_isValid;
}

qint32 OAITimeMachine_TimeMachineHourlyData::getHumidity() const {
    return m_humidity;
}
void OAITimeMachine_TimeMachineHourlyData::setHumidity(const qint32 &humidity) {
    m_humidity = humidity;
    m_humidity_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_humidity_Set() const{
    return m_humidity_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_humidity_Valid() const{
    return m_humidity_isValid;
}

qint32 OAITimeMachine_TimeMachineHourlyData::getIcon() const {
    return m_icon;
}
void OAITimeMachine_TimeMachineHourlyData::setIcon(const qint32 &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_icon_Valid() const{
    return m_icon_isValid;
}

qint32 OAITimeMachine_TimeMachineHourlyData::getIrradiance() const {
    return m_irradiance;
}
void OAITimeMachine_TimeMachineHourlyData::setIrradiance(const qint32 &irradiance) {
    m_irradiance = irradiance;
    m_irradiance_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_irradiance_Set() const{
    return m_irradiance_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_irradiance_Valid() const{
    return m_irradiance_isValid;
}

qint32 OAITimeMachine_TimeMachineHourlyData::getOzone() const {
    return m_ozone;
}
void OAITimeMachine_TimeMachineHourlyData::setOzone(const qint32 &ozone) {
    m_ozone = ozone;
    m_ozone_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_ozone_Set() const{
    return m_ozone_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_ozone_Valid() const{
    return m_ozone_isValid;
}

OAITimeMachine_TimeMachinePrecipitationData OAITimeMachine_TimeMachineHourlyData::getPrecipitation() const {
    return m_precipitation;
}
void OAITimeMachine_TimeMachineHourlyData::setPrecipitation(const OAITimeMachine_TimeMachinePrecipitationData &precipitation) {
    m_precipitation = precipitation;
    m_precipitation_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_precipitation_Set() const{
    return m_precipitation_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_precipitation_Valid() const{
    return m_precipitation_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getPressure() const {
    return m_pressure;
}
void OAITimeMachine_TimeMachineHourlyData::setPressure(const double &pressure) {
    m_pressure = pressure;
    m_pressure_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_pressure_Set() const{
    return m_pressure_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_pressure_Valid() const{
    return m_pressure_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getSoilTemperature() const {
    return m_soil_temperature;
}
void OAITimeMachine_TimeMachineHourlyData::setSoilTemperature(const double &soil_temperature) {
    m_soil_temperature = soil_temperature;
    m_soil_temperature_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_soil_temperature_Set() const{
    return m_soil_temperature_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_soil_temperature_Valid() const{
    return m_soil_temperature_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getSurfaceTemperature() const {
    return m_surface_temperature;
}
void OAITimeMachine_TimeMachineHourlyData::setSurfaceTemperature(const double &surface_temperature) {
    m_surface_temperature = surface_temperature;
    m_surface_temperature_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_surface_temperature_Set() const{
    return m_surface_temperature_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_surface_temperature_Valid() const{
    return m_surface_temperature_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getTemperature() const {
    return m_temperature;
}
void OAITimeMachine_TimeMachineHourlyData::setTemperature(const double &temperature) {
    m_temperature = temperature;
    m_temperature_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_temperature_Set() const{
    return m_temperature_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_temperature_Valid() const{
    return m_temperature_isValid;
}

QString OAITimeMachine_TimeMachineHourlyData::getWeather() const {
    return m_weather;
}
void OAITimeMachine_TimeMachineHourlyData::setWeather(const QString &weather) {
    m_weather = weather;
    m_weather_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_weather_Set() const{
    return m_weather_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_weather_Valid() const{
    return m_weather_isValid;
}

OAITimeMachine_TimeMachineWindData OAITimeMachine_TimeMachineHourlyData::getWind() const {
    return m_wind;
}
void OAITimeMachine_TimeMachineHourlyData::setWind(const OAITimeMachine_TimeMachineWindData &wind) {
    m_wind = wind;
    m_wind_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_wind_Set() const{
    return m_wind_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_wind_Valid() const{
    return m_wind_isValid;
}

double OAITimeMachine_TimeMachineHourlyData::getWindChill() const {
    return m_wind_chill;
}
void OAITimeMachine_TimeMachineHourlyData::setWindChill(const double &wind_chill) {
    m_wind_chill = wind_chill;
    m_wind_chill_isSet = true;
}

bool OAITimeMachine_TimeMachineHourlyData::is_wind_chill_Set() const{
    return m_wind_chill_isSet;
}

bool OAITimeMachine_TimeMachineHourlyData::is_wind_chill_Valid() const{
    return m_wind_chill_isValid;
}

bool OAITimeMachine_TimeMachineHourlyData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cape_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cloud_cover.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dew_point_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_evaporation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feels_like_isSet) {
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

        if (m_irradiance_isSet) {
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

        if (m_soil_temperature_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surface_temperature_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_temperature_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAITimeMachine_TimeMachineHourlyData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_cloud_cover_isValid && m_precipitation_isValid && m_wind_isValid && true;
}

} // namespace OpenAPI
