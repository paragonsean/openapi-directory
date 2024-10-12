/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFlightStop.h
 *
 * details of stops for direct or change of gauge flights
 */

#ifndef OAIFlightStop_H
#define OAIFlightStop_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFlightStop : public OAIObject {
public:
    OAIFlightStop();
    OAIFlightStop(QString json);
    ~OAIFlightStop() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDuration() const;
    void setDuration(const QString &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getIataCode() const;
    void setIataCode(const QString &iata_code);
    bool is_iata_code_Set() const;
    bool is_iata_code_Valid() const;

    QDateTime getArrivalAt() const;
    void setArrivalAt(const QDateTime &arrival_at);
    bool is_arrival_at_Set() const;
    bool is_arrival_at_Valid() const;

    QDateTime getDepartureAt() const;
    void setDepartureAt(const QDateTime &departure_at);
    bool is_departure_at_Set() const;
    bool is_departure_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_iata_code;
    bool m_iata_code_isSet;
    bool m_iata_code_isValid;

    QDateTime m_arrival_at;
    bool m_arrival_at_isSet;
    bool m_arrival_at_isValid;

    QDateTime m_departure_at;
    bool m_departure_at_isSet;
    bool m_departure_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightStop)

#endif // OAIFlightStop_H
