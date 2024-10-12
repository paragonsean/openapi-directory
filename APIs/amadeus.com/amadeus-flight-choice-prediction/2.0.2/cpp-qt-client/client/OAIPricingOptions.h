/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPricingOptions.h
 *
 * 
 */

#ifndef OAIPricingOptions_H
#define OAIPricingOptions_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPricingOptions : public OAIObject {
public:
    OAIPricingOptions();
    OAIPricingOptions(QString json);
    ~OAIPricingOptions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getCorporateCodes() const;
    void setCorporateCodes(const QList<QString> &corporate_codes);
    bool is_corporate_codes_Set() const;
    bool is_corporate_codes_Valid() const;

    QList<QString> getFareType() const;
    void setFareType(const QList<QString> &fare_type);
    bool is_fare_type_Set() const;
    bool is_fare_type_Valid() const;

    bool isIncludedCheckedBagsOnly() const;
    void setIncludedCheckedBagsOnly(const bool &included_checked_bags_only);
    bool is_included_checked_bags_only_Set() const;
    bool is_included_checked_bags_only_Valid() const;

    bool isNoPenaltyFare() const;
    void setNoPenaltyFare(const bool &no_penalty_fare);
    bool is_no_penalty_fare_Set() const;
    bool is_no_penalty_fare_Valid() const;

    bool isNoRestrictionFare() const;
    void setNoRestrictionFare(const bool &no_restriction_fare);
    bool is_no_restriction_fare_Set() const;
    bool is_no_restriction_fare_Valid() const;

    bool isRefundableFare() const;
    void setRefundableFare(const bool &refundable_fare);
    bool is_refundable_fare_Set() const;
    bool is_refundable_fare_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_corporate_codes;
    bool m_corporate_codes_isSet;
    bool m_corporate_codes_isValid;

    QList<QString> m_fare_type;
    bool m_fare_type_isSet;
    bool m_fare_type_isValid;

    bool m_included_checked_bags_only;
    bool m_included_checked_bags_only_isSet;
    bool m_included_checked_bags_only_isValid;

    bool m_no_penalty_fare;
    bool m_no_penalty_fare_isSet;
    bool m_no_penalty_fare_isValid;

    bool m_no_restriction_fare;
    bool m_no_restriction_fare_isSet;
    bool m_no_restriction_fare_isValid;

    bool m_refundable_fare;
    bool m_refundable_fare_isSet;
    bool m_refundable_fare_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPricingOptions)

#endif // OAIPricingOptions_H
