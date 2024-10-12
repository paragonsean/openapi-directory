/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExtended_OriginDestinationLight.h
 *
 * 
 */

#ifndef OAIExtended_OriginDestinationLight_H
#define OAIExtended_OriginDestinationLight_H

#include <QJsonObject>

#include "OAIDateTimeType.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDateTimeType;

class OAIExtended_OriginDestinationLight : public OAIObject {
public:
    OAIExtended_OriginDestinationLight();
    OAIExtended_OriginDestinationLight(QString json);
    ~OAIExtended_OriginDestinationLight() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDestinationLocationCode() const;
    void setDestinationLocationCode(const QString &destination_location_code);
    bool is_destination_location_code_Set() const;
    bool is_destination_location_code_Valid() const;

    QList<QString> getExcludedConnectionPoints() const;
    void setExcludedConnectionPoints(const QList<QString> &excluded_connection_points);
    bool is_excluded_connection_points_Set() const;
    bool is_excluded_connection_points_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<QString> getIncludedConnectionPoints() const;
    void setIncludedConnectionPoints(const QList<QString> &included_connection_points);
    bool is_included_connection_points_Set() const;
    bool is_included_connection_points_Valid() const;

    QString getOriginLocationCode() const;
    void setOriginLocationCode(const QString &origin_location_code);
    bool is_origin_location_code_Set() const;
    bool is_origin_location_code_Valid() const;

    OAIDateTimeType getArrivalDateTime() const;
    void setArrivalDateTime(const OAIDateTimeType &arrival_date_time);
    bool is_arrival_date_time_Set() const;
    bool is_arrival_date_time_Valid() const;

    OAIDateTimeType getDepartureDateTime() const;
    void setDepartureDateTime(const OAIDateTimeType &departure_date_time);
    bool is_departure_date_time_Set() const;
    bool is_departure_date_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_destination_location_code;
    bool m_destination_location_code_isSet;
    bool m_destination_location_code_isValid;

    QList<QString> m_excluded_connection_points;
    bool m_excluded_connection_points_isSet;
    bool m_excluded_connection_points_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<QString> m_included_connection_points;
    bool m_included_connection_points_isSet;
    bool m_included_connection_points_isValid;

    QString m_origin_location_code;
    bool m_origin_location_code_isSet;
    bool m_origin_location_code_isValid;

    OAIDateTimeType m_arrival_date_time;
    bool m_arrival_date_time_isSet;
    bool m_arrival_date_time_isValid;

    OAIDateTimeType m_departure_date_time;
    bool m_departure_date_time_isSet;
    bool m_departure_date_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExtended_OriginDestinationLight)

#endif // OAIExtended_OriginDestinationLight_H
