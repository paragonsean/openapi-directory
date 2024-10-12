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
 * OAIFlightSegment.h
 *
 * defining a flight segment; including both operating and marketing details when applicable
 */

#ifndef OAIFlightSegment_H
#define OAIFlightSegment_H

#include <QJsonObject>

#include "OAIAircraftEquipment.h"
#include "OAIFlightEndPoint.h"
#include "OAIFlightStop.h"
#include "OAIOperatingFlight.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAircraftEquipment;
class OAIFlightEndPoint;
class OAIOperatingFlight;
class OAIFlightStop;

class OAIFlightSegment : public OAIObject {
public:
    OAIFlightSegment();
    OAIFlightSegment(QString json);
    ~OAIFlightSegment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAircraftEquipment getAircraft() const;
    void setAircraft(const OAIAircraftEquipment &aircraft);
    bool is_aircraft_Set() const;
    bool is_aircraft_Valid() const;

    OAIFlightEndPoint getArrival() const;
    void setArrival(const OAIFlightEndPoint &arrival);
    bool is_arrival_Set() const;
    bool is_arrival_Valid() const;

    QString getCarrierCode() const;
    void setCarrierCode(const QString &carrier_code);
    bool is_carrier_code_Set() const;
    bool is_carrier_code_Valid() const;

    OAIFlightEndPoint getDeparture() const;
    void setDeparture(const OAIFlightEndPoint &departure);
    bool is_departure_Set() const;
    bool is_departure_Valid() const;

    QString getDuration() const;
    void setDuration(const QString &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getNumber() const;
    void setNumber(const QString &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    OAIOperatingFlight getOperating() const;
    void setOperating(const OAIOperatingFlight &operating);
    bool is_operating_Set() const;
    bool is_operating_Valid() const;

    QList<OAIFlightStop> getStops() const;
    void setStops(const QList<OAIFlightStop> &stops);
    bool is_stops_Set() const;
    bool is_stops_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAircraftEquipment m_aircraft;
    bool m_aircraft_isSet;
    bool m_aircraft_isValid;

    OAIFlightEndPoint m_arrival;
    bool m_arrival_isSet;
    bool m_arrival_isValid;

    QString m_carrier_code;
    bool m_carrier_code_isSet;
    bool m_carrier_code_isValid;

    OAIFlightEndPoint m_departure;
    bool m_departure_isSet;
    bool m_departure_isValid;

    QString m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    OAIOperatingFlight m_operating;
    bool m_operating_isSet;
    bool m_operating_isValid;

    QList<OAIFlightStop> m_stops;
    bool m_stops_isSet;
    bool m_stops_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightSegment)

#endif // OAIFlightSegment_H
