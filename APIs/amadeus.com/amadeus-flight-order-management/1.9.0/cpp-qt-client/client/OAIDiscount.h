/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDiscount.h
 *
 * traveler discount
 */

#ifndef OAIDiscount_H
#define OAIDiscount_H

#include <QJsonObject>

#include "OAIDiscountTravelerType.h"
#include "OAIDiscountType.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDiscount : public OAIObject {
public:
    OAIDiscount();
    OAIDiscount(QString json);
    ~OAIDiscount() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCardNumber() const;
    void setCardNumber(const QString &card_number);
    bool is_card_number_Set() const;
    bool is_card_number_Valid() const;

    QString getCertificateNumber() const;
    void setCertificateNumber(const QString &certificate_number);
    bool is_certificate_number_Set() const;
    bool is_certificate_number_Valid() const;

    QString getCityName() const;
    void setCityName(const QString &city_name);
    bool is_city_name_Set() const;
    bool is_city_name_Valid() const;

    OAIDiscountType getSubType() const;
    void setSubType(const OAIDiscountType &sub_type);
    bool is_sub_type_Set() const;
    bool is_sub_type_Valid() const;

    OAIDiscountTravelerType getTravelerType() const;
    void setTravelerType(const OAIDiscountTravelerType &traveler_type);
    bool is_traveler_type_Set() const;
    bool is_traveler_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_card_number;
    bool m_card_number_isSet;
    bool m_card_number_isValid;

    QString m_certificate_number;
    bool m_certificate_number_isSet;
    bool m_certificate_number_isValid;

    QString m_city_name;
    bool m_city_name_isSet;
    bool m_city_name_isValid;

    OAIDiscountType m_sub_type;
    bool m_sub_type_isSet;
    bool m_sub_type_isValid;

    OAIDiscountTravelerType m_traveler_type;
    bool m_traveler_type_isSet;
    bool m_traveler_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDiscount)

#endif // OAIDiscount_H
