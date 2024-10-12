/**
 * LH Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAirport.h
 *
 * Array of all available airports or one airport matching the request.
 */

#ifndef OAIAirport_H
#define OAIAirport_H

#include <QJsonObject>

#include "OAIAirport_Names.h"
#include "OAIAirport_Position.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAirport_Names;
class OAIAirport_Position;

class OAIAirport : public OAIObject {
public:
    OAIAirport();
    OAIAirport(QString json);
    ~OAIAirport() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAirportCode() const;
    void setAirportCode(const QString &airport_code);
    bool is_airport_code_Set() const;
    bool is_airport_code_Valid() const;

    QString getCityCode() const;
    void setCityCode(const QString &city_code);
    bool is_city_code_Set() const;
    bool is_city_code_Valid() const;

    QString getCountryCode() const;
    void setCountryCode(const QString &country_code);
    bool is_country_code_Set() const;
    bool is_country_code_Valid() const;

    QString getLocationType() const;
    void setLocationType(const QString &location_type);
    bool is_location_type_Set() const;
    bool is_location_type_Valid() const;

    OAIAirport_Names getNames() const;
    void setNames(const OAIAirport_Names &names);
    bool is_names_Set() const;
    bool is_names_Valid() const;

    OAIAirport_Position getPosition() const;
    void setPosition(const OAIAirport_Position &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getTimeZoneId() const;
    void setTimeZoneId(const QString &time_zone_id);
    bool is_time_zone_id_Set() const;
    bool is_time_zone_id_Valid() const;

    float getUtcOffset() const;
    void setUtcOffset(const float &utc_offset);
    bool is_utc_offset_Set() const;
    bool is_utc_offset_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_airport_code;
    bool m_airport_code_isSet;
    bool m_airport_code_isValid;

    QString m_city_code;
    bool m_city_code_isSet;
    bool m_city_code_isValid;

    QString m_country_code;
    bool m_country_code_isSet;
    bool m_country_code_isValid;

    QString m_location_type;
    bool m_location_type_isSet;
    bool m_location_type_isValid;

    OAIAirport_Names m_names;
    bool m_names_isSet;
    bool m_names_isValid;

    OAIAirport_Position m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_time_zone_id;
    bool m_time_zone_id_isSet;
    bool m_time_zone_id_isValid;

    float m_utc_offset;
    bool m_utc_offset_isSet;
    bool m_utc_offset_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAirport)

#endif // OAIAirport_H
