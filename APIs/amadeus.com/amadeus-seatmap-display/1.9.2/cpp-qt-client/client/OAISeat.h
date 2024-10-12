/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISeat.h
 *
 * 
 */

#ifndef OAISeat_H
#define OAISeat_H

#include <QJsonObject>

#include "OAICoordinates.h"
#include "OAISeatmapTravelerPricing.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICoordinates;
class OAISeatmapTravelerPricing;

class OAISeat : public OAIObject {
public:
    OAISeat();
    OAISeat(QString json);
    ~OAISeat() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCabin() const;
    void setCabin(const QString &cabin);
    bool is_cabin_Set() const;
    bool is_cabin_Valid() const;

    QList<QString> getCharacteristicsCodes() const;
    void setCharacteristicsCodes(const QList<QString> &characteristics_codes);
    bool is_characteristics_codes_Set() const;
    bool is_characteristics_codes_Valid() const;

    OAICoordinates getCoordinates() const;
    void setCoordinates(const OAICoordinates &coordinates);
    bool is_coordinates_Set() const;
    bool is_coordinates_Valid() const;

    QString getNumber() const;
    void setNumber(const QString &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    QList<OAISeatmapTravelerPricing> getTravelerPricing() const;
    void setTravelerPricing(const QList<OAISeatmapTravelerPricing> &traveler_pricing);
    bool is_traveler_pricing_Set() const;
    bool is_traveler_pricing_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_cabin;
    bool m_cabin_isSet;
    bool m_cabin_isValid;

    QList<QString> m_characteristics_codes;
    bool m_characteristics_codes_isSet;
    bool m_characteristics_codes_isValid;

    OAICoordinates m_coordinates;
    bool m_coordinates_isSet;
    bool m_coordinates_isValid;

    QString m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    QList<OAISeatmapTravelerPricing> m_traveler_pricing;
    bool m_traveler_pricing_isSet;
    bool m_traveler_pricing_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISeat)

#endif // OAISeat_H
