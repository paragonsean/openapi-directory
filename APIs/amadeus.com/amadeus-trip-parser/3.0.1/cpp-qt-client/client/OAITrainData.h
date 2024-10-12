/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITrainData.h
 *
 * Train Product
 */

#ifndef OAITrainData_H
#define OAITrainData_H

#include <QJsonObject>

#include "OAIArrival.h"
#include "OAIDeparture.h"
#include "OAISeats.h"
#include "OAIVehicle.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIArrival;
class OAIDeparture;
class OAISeats;
class OAIVehicle;

class OAITrainData : public OAIObject {
public:
    OAITrainData();
    OAITrainData(QString json);
    ~OAITrainData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIArrival getArrival() const;
    void setArrival(const OAIArrival &arrival);
    bool is_arrival_Set() const;
    bool is_arrival_Valid() const;

    QString getArrivalDateTime() const;
    void setArrivalDateTime(const QString &arrival_date_time);
    bool is_arrival_date_time_Set() const;
    bool is_arrival_date_time_Valid() const;

    QString getArrivalTrack() const;
    void setArrivalTrack(const QString &arrival_track);
    bool is_arrival_track_Set() const;
    bool is_arrival_track_Valid() const;

    QString getBookingClass() const;
    void setBookingClass(const QString &booking_class);
    bool is_booking_class_Set() const;
    bool is_booking_class_Valid() const;

    QString getConfirmNbr() const;
    void setConfirmNbr(const QString &confirm_nbr);
    bool is_confirm_nbr_Set() const;
    bool is_confirm_nbr_Valid() const;

    OAIDeparture getDeparture() const;
    void setDeparture(const OAIDeparture &departure);
    bool is_departure_Set() const;
    bool is_departure_Valid() const;

    QString getDepartureDateTime() const;
    void setDepartureDateTime(const QString &departure_date_time);
    bool is_departure_date_time_Set() const;
    bool is_departure_date_time_Valid() const;

    QString getDepartureTrack() const;
    void setDepartureTrack(const QString &departure_track);
    bool is_departure_track_Set() const;
    bool is_departure_track_Valid() const;

    QString getDuration() const;
    void setDuration(const QString &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QList<OAISeats> getSeats() const;
    void setSeats(const QList<OAISeats> &seats);
    bool is_seats_Set() const;
    bool is_seats_Valid() const;

    QString getServiceProviderName() const;
    void setServiceProviderName(const QString &service_provider_name);
    bool is_service_provider_name_Set() const;
    bool is_service_provider_name_Valid() const;

    OAIVehicle getVehicle() const;
    void setVehicle(const OAIVehicle &vehicle);
    bool is_vehicle_Set() const;
    bool is_vehicle_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIArrival m_arrival;
    bool m_arrival_isSet;
    bool m_arrival_isValid;

    QString m_arrival_date_time;
    bool m_arrival_date_time_isSet;
    bool m_arrival_date_time_isValid;

    QString m_arrival_track;
    bool m_arrival_track_isSet;
    bool m_arrival_track_isValid;

    QString m_booking_class;
    bool m_booking_class_isSet;
    bool m_booking_class_isValid;

    QString m_confirm_nbr;
    bool m_confirm_nbr_isSet;
    bool m_confirm_nbr_isValid;

    OAIDeparture m_departure;
    bool m_departure_isSet;
    bool m_departure_isValid;

    QString m_departure_date_time;
    bool m_departure_date_time_isSet;
    bool m_departure_date_time_isValid;

    QString m_departure_track;
    bool m_departure_track_isSet;
    bool m_departure_track_isValid;

    QString m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QList<OAISeats> m_seats;
    bool m_seats_isSet;
    bool m_seats_isValid;

    QString m_service_provider_name;
    bool m_service_provider_name_isSet;
    bool m_service_provider_name_isValid;

    OAIVehicle m_vehicle;
    bool m_vehicle_isSet;
    bool m_vehicle_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITrainData)

#endif // OAITrainData_H
