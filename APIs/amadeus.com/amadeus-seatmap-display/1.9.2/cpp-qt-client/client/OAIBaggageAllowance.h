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
 * OAIBaggageAllowance.h
 *
 * baggageAllowance
 */

#ifndef OAIBaggageAllowance_H
#define OAIBaggageAllowance_H

#include <QJsonObject>

#include "OAIElementaryPrice.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIElementaryPrice;

class OAIBaggageAllowance : public OAIObject {
public:
    OAIBaggageAllowance();
    OAIBaggageAllowance(QString json);
    ~OAIBaggageAllowance() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIElementaryPrice getExcessRate() const;
    void setExcessRate(const OAIElementaryPrice &excess_rate);
    bool is_excess_rate_Set() const;
    bool is_excess_rate_Valid() const;

    qint32 getQuantity() const;
    void setQuantity(const qint32 &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    qint32 getWeight() const;
    void setWeight(const qint32 &weight);
    bool is_weight_Set() const;
    bool is_weight_Valid() const;

    QString getWeightUnit() const;
    void setWeightUnit(const QString &weight_unit);
    bool is_weight_unit_Set() const;
    bool is_weight_unit_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIElementaryPrice m_excess_rate;
    bool m_excess_rate_isSet;
    bool m_excess_rate_isValid;

    qint32 m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    qint32 m_weight;
    bool m_weight_isSet;
    bool m_weight_isValid;

    QString m_weight_unit;
    bool m_weight_unit_isSet;
    bool m_weight_unit_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBaggageAllowance)

#endif // OAIBaggageAllowance_H
