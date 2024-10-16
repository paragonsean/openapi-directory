/**
 * Moon API
 * # Moon-API.com Postman Collection  Welcome to the Moon Phase API Postman Collection! This collection contains a set of pre-configured API requests to interact with the Moon Phase API endpoints provided by [moon-api.com](https://moon-api.com). Explore the enchanting world of the moon and its ever-changing phases with ease using this collection.  ## Getting Started  To start using this Postman collection, follow these steps:  1. [Download and install Postman](https://www.postman.com/downloads/) if you haven't already. 2. Import the Moon API Postman Collection into your Postman app. 3. Set your RapidAPI key in the collection's environment variables. 4. Begin making requests to explore the moon phase data and retrieve lunar information.       ## Collection Structure  The Moon-API.com Postman Collection consists of the following requests:  - **Basic Moon Phase**: Retrieve the main moon phase data. - **Advanced Moon Phase**: Get detailed moon phase data based on a specific timezone and coordinates. - **Plain Text Moon Phase**: Get a plain text description of the current moon phase. - **Emoji Moon Phase**: Get the relevant emoji of the current moon phase. - **Lunar Calender**: Get the current year's moon phases in a markdown calender.       ## Environment Variables  The collection uses environment variables to store your RapidAPI key. To use this collection effectively, ensure you set the `X-Rapidapi-Key` variable in the collection's environment with your actual RapidAPI key.  ## How to Use  1. Select the desired request from the Moon API collection. 2. Click on the request to open it. 3. Send the request and view the response to retrieve the moon phase data.       ## Documentation  For more information on the Moon Phase API endpoints and their response formats, refer to the [official Moon API documentation](https://rapidapi.com/MoonAPIcom/api/moon-phase/details). Visit [moon-api.com](https://moon-api.com) to learn more about the Moon Phase API and the services provided.  Happy moon exploration with the Moon Phase API Postman Collection provided by [moon-api.com](https://moon-api.com)!
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetAdvancedMoonPhaseData_200_response_sun.h
 *
 * 
 */

#ifndef OAIGetAdvancedMoonPhaseData_200_response_sun_H
#define OAIGetAdvancedMoonPhaseData_200_response_sun_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetAdvancedMoonPhaseData_200_response_sun : public OAIObject {
public:
    OAIGetAdvancedMoonPhaseData_200_response_sun();
    OAIGetAdvancedMoonPhaseData_200_response_sun(QString json);
    ~OAIGetAdvancedMoonPhaseData_200_response_sun() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDayLength() const;
    void setDayLength(const QString &day_length);
    bool is_day_length_Set() const;
    bool is_day_length_Valid() const;

    QString getSolarNoon() const;
    void setSolarNoon(const QString &solar_noon);
    bool is_solar_noon_Set() const;
    bool is_solar_noon_Valid() const;

    double getSunAltitude() const;
    void setSunAltitude(const double &sun_altitude);
    bool is_sun_altitude_Set() const;
    bool is_sun_altitude_Valid() const;

    double getSunAzimuth() const;
    void setSunAzimuth(const double &sun_azimuth);
    bool is_sun_azimuth_Set() const;
    bool is_sun_azimuth_Valid() const;

    double getSunDistance() const;
    void setSunDistance(const double &sun_distance);
    bool is_sun_distance_Set() const;
    bool is_sun_distance_Valid() const;

    double getSunrise() const;
    void setSunrise(const double &sunrise);
    bool is_sunrise_Set() const;
    bool is_sunrise_Valid() const;

    QString getSunriseTimestamp() const;
    void setSunriseTimestamp(const QString &sunrise_timestamp);
    bool is_sunrise_timestamp_Set() const;
    bool is_sunrise_timestamp_Valid() const;

    double getSunset() const;
    void setSunset(const double &sunset);
    bool is_sunset_Set() const;
    bool is_sunset_Valid() const;

    QString getSunsetTimestamp() const;
    void setSunsetTimestamp(const QString &sunset_timestamp);
    bool is_sunset_timestamp_Set() const;
    bool is_sunset_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_day_length;
    bool m_day_length_isSet;
    bool m_day_length_isValid;

    QString m_solar_noon;
    bool m_solar_noon_isSet;
    bool m_solar_noon_isValid;

    double m_sun_altitude;
    bool m_sun_altitude_isSet;
    bool m_sun_altitude_isValid;

    double m_sun_azimuth;
    bool m_sun_azimuth_isSet;
    bool m_sun_azimuth_isValid;

    double m_sun_distance;
    bool m_sun_distance_isSet;
    bool m_sun_distance_isValid;

    double m_sunrise;
    bool m_sunrise_isSet;
    bool m_sunrise_isValid;

    QString m_sunrise_timestamp;
    bool m_sunrise_timestamp_isSet;
    bool m_sunrise_timestamp_isValid;

    double m_sunset;
    bool m_sunset_isSet;
    bool m_sunset_isValid;

    QString m_sunset_timestamp;
    bool m_sunset_timestamp_isSet;
    bool m_sunset_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetAdvancedMoonPhaseData_200_response_sun)

#endif // OAIGetAdvancedMoonPhaseData_200_response_sun_H
