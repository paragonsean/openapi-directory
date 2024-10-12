/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDictionaries.h
 *
 * 
 */

#ifndef OAIDictionaries_H
#define OAIDictionaries_H

#include <QJsonObject>

#include "OAILocationValue.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILocationValue;

class OAIDictionaries : public OAIObject {
public:
    OAIDictionaries();
    OAIDictionaries(QString json);
    ~OAIDictionaries() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QString> getAircraft() const;
    void setAircraft(const QMap<QString, QString> &aircraft);
    bool is_aircraft_Set() const;
    bool is_aircraft_Valid() const;

    QMap<QString, QString> getCarriers() const;
    void setCarriers(const QMap<QString, QString> &carriers);
    bool is_carriers_Set() const;
    bool is_carriers_Valid() const;

    QMap<QString, QString> getCurrencies() const;
    void setCurrencies(const QMap<QString, QString> &currencies);
    bool is_currencies_Set() const;
    bool is_currencies_Valid() const;

    QMap<QString, OAILocationValue> getLocations() const;
    void setLocations(const QMap<QString, OAILocationValue> &locations);
    bool is_locations_Set() const;
    bool is_locations_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QString> m_aircraft;
    bool m_aircraft_isSet;
    bool m_aircraft_isValid;

    QMap<QString, QString> m_carriers;
    bool m_carriers_isSet;
    bool m_carriers_isValid;

    QMap<QString, QString> m_currencies;
    bool m_currencies_isSet;
    bool m_currencies_isValid;

    QMap<QString, OAILocationValue> m_locations;
    bool m_locations_isSet;
    bool m_locations_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDictionaries)

#endif // OAIDictionaries_H
