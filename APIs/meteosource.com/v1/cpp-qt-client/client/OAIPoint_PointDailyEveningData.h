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

/*
 * OAIPoint_PointDailyEveningData.h
 *
 * 
 */

#ifndef OAIPoint_PointDailyEveningData_H
#define OAIPoint_PointDailyEveningData_H

#include <QJsonObject>

#include "OAIPoint_PointDailyEveningCloudCoverData.h"
#include "OAIPoint_PointDailyEveningPrecipitationData.h"
#include "OAIPoint_PointDailyEveningProbData.h"
#include "OAIPoint_PointDailyEveningWindData.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPoint_PointDailyEveningCloudCoverData;
class OAIPoint_PointDailyEveningPrecipitationData;
class OAIPoint_PointDailyEveningProbData;
class OAIPoint_PointDailyEveningWindData;

class OAIPoint_PointDailyEveningData : public OAIObject {
public:
    OAIPoint_PointDailyEveningData();
    OAIPoint_PointDailyEveningData(QString json);
    ~OAIPoint_PointDailyEveningData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPoint_PointDailyEveningCloudCoverData getCloudCover() const;
    void setCloudCover(const OAIPoint_PointDailyEveningCloudCoverData &cloud_cover);
    bool is_cloud_cover_Set() const;
    bool is_cloud_cover_Valid() const;

    double getDewPoint() const;
    void setDewPoint(const double &dew_point);
    bool is_dew_point_Set() const;
    bool is_dew_point_Valid() const;

    double getFeelsLike() const;
    void setFeelsLike(const double &feels_like);
    bool is_feels_like_Set() const;
    bool is_feels_like_Valid() const;

    qint32 getHumidity() const;
    void setHumidity(const qint32 &humidity);
    bool is_humidity_Set() const;
    bool is_humidity_Valid() const;

    qint32 getIcon() const;
    void setIcon(const qint32 &icon);
    bool is_icon_Set() const;
    bool is_icon_Valid() const;

    double getOzone() const;
    void setOzone(const double &ozone);
    bool is_ozone_Set() const;
    bool is_ozone_Valid() const;

    OAIPoint_PointDailyEveningPrecipitationData getPrecipitation() const;
    void setPrecipitation(const OAIPoint_PointDailyEveningPrecipitationData &precipitation);
    bool is_precipitation_Set() const;
    bool is_precipitation_Valid() const;

    double getPressure() const;
    void setPressure(const double &pressure);
    bool is_pressure_Set() const;
    bool is_pressure_Valid() const;

    OAIPoint_PointDailyEveningProbData getProbability() const;
    void setProbability(const OAIPoint_PointDailyEveningProbData &probability);
    bool is_probability_Set() const;
    bool is_probability_Valid() const;

    double getSnowDepth() const;
    void setSnowDepth(const double &snow_depth);
    bool is_snow_depth_Set() const;
    bool is_snow_depth_Valid() const;

    double getSoilTemperature() const;
    void setSoilTemperature(const double &soil_temperature);
    bool is_soil_temperature_Set() const;
    bool is_soil_temperature_Valid() const;

    double getSurfaceTemperature() const;
    void setSurfaceTemperature(const double &surface_temperature);
    bool is_surface_temperature_Set() const;
    bool is_surface_temperature_Valid() const;

    double getTemperature() const;
    void setTemperature(const double &temperature);
    bool is_temperature_Set() const;
    bool is_temperature_Valid() const;

    double getVisibility() const;
    void setVisibility(const double &visibility);
    bool is_visibility_Set() const;
    bool is_visibility_Valid() const;

    QString getWeather() const;
    void setWeather(const QString &weather);
    bool is_weather_Set() const;
    bool is_weather_Valid() const;

    OAIPoint_PointDailyEveningWindData getWind() const;
    void setWind(const OAIPoint_PointDailyEveningWindData &wind);
    bool is_wind_Set() const;
    bool is_wind_Valid() const;

    double getWindChill() const;
    void setWindChill(const double &wind_chill);
    bool is_wind_chill_Set() const;
    bool is_wind_chill_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPoint_PointDailyEveningCloudCoverData m_cloud_cover;
    bool m_cloud_cover_isSet;
    bool m_cloud_cover_isValid;

    double m_dew_point;
    bool m_dew_point_isSet;
    bool m_dew_point_isValid;

    double m_feels_like;
    bool m_feels_like_isSet;
    bool m_feels_like_isValid;

    qint32 m_humidity;
    bool m_humidity_isSet;
    bool m_humidity_isValid;

    qint32 m_icon;
    bool m_icon_isSet;
    bool m_icon_isValid;

    double m_ozone;
    bool m_ozone_isSet;
    bool m_ozone_isValid;

    OAIPoint_PointDailyEveningPrecipitationData m_precipitation;
    bool m_precipitation_isSet;
    bool m_precipitation_isValid;

    double m_pressure;
    bool m_pressure_isSet;
    bool m_pressure_isValid;

    OAIPoint_PointDailyEveningProbData m_probability;
    bool m_probability_isSet;
    bool m_probability_isValid;

    double m_snow_depth;
    bool m_snow_depth_isSet;
    bool m_snow_depth_isValid;

    double m_soil_temperature;
    bool m_soil_temperature_isSet;
    bool m_soil_temperature_isValid;

    double m_surface_temperature;
    bool m_surface_temperature_isSet;
    bool m_surface_temperature_isValid;

    double m_temperature;
    bool m_temperature_isSet;
    bool m_temperature_isValid;

    double m_visibility;
    bool m_visibility_isSet;
    bool m_visibility_isValid;

    QString m_weather;
    bool m_weather_isSet;
    bool m_weather_isValid;

    OAIPoint_PointDailyEveningWindData m_wind;
    bool m_wind_isSet;
    bool m_wind_isValid;

    double m_wind_chill;
    bool m_wind_chill_isSet;
    bool m_wind_chill_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPoint_PointDailyEveningData)

#endif // OAIPoint_PointDailyEveningData_H
