/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILongTermCareInsurancePolicyWithIdModel.h
 *
 * 
 */

#ifndef OAILongTermCareInsurancePolicyWithIdModel_H
#define OAILongTermCareInsurancePolicyWithIdModel_H

#include <QJsonObject>

#include "OAIObjectLink.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIObjectLink;

class OAILongTermCareInsurancePolicyWithIdModel : public OAIObject {
public:
    OAILongTermCareInsurancePolicyWithIdModel();
    OAILongTermCareInsurancePolicyWithIdModel(QString json);
    ~OAILongTermCareInsurancePolicyWithIdModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getBenefit() const;
    void setBenefit(const double &benefit);
    bool is_benefit_Set() const;
    bool is_benefit_Valid() const;

    qint32 getBenefitFrequency() const;
    void setBenefitFrequency(const qint32 &benefit_frequency);
    bool is_benefit_frequency_Set() const;
    bool is_benefit_frequency_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getExternalDestinationId() const;
    void setExternalDestinationId(const QString &external_destination_id);
    bool is_external_destination_id_Set() const;
    bool is_external_destination_id_Valid() const;

    qint32 getFactFinderId() const;
    void setFactFinderId(const qint32 &fact_finder_id);
    bool is_fact_finder_id_Set() const;
    bool is_fact_finder_id_Valid() const;

    qint32 getInsurancePolicyId() const;
    void setInsurancePolicyId(const qint32 &insurance_policy_id);
    bool is_insurance_policy_id_Set() const;
    bool is_insurance_policy_id_Valid() const;

    QString getInsured() const;
    void setInsured(const QString &insured);
    bool is_insured_Set() const;
    bool is_insured_Valid() const;

    QList<OAIObjectLink> getLinks() const;
    void setLinks(const QList<OAIObjectLink> &links);
    bool is_links_Set() const;
    bool is_links_Valid() const;

    double getPremium() const;
    void setPremium(const double &premium);
    bool is_premium_Set() const;
    bool is_premium_Valid() const;

    qint32 getPremiumFrequency() const;
    void setPremiumFrequency(const qint32 &premium_frequency);
    bool is_premium_frequency_Set() const;
    bool is_premium_frequency_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_benefit;
    bool m_benefit_isSet;
    bool m_benefit_isValid;

    qint32 m_benefit_frequency;
    bool m_benefit_frequency_isSet;
    bool m_benefit_frequency_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    qint32 m_fact_finder_id;
    bool m_fact_finder_id_isSet;
    bool m_fact_finder_id_isValid;

    qint32 m_insurance_policy_id;
    bool m_insurance_policy_id_isSet;
    bool m_insurance_policy_id_isValid;

    QString m_insured;
    bool m_insured_isSet;
    bool m_insured_isValid;

    QList<OAIObjectLink> m_links;
    bool m_links_isSet;
    bool m_links_isValid;

    double m_premium;
    bool m_premium_isSet;
    bool m_premium_isValid;

    qint32 m_premium_frequency;
    bool m_premium_frequency_isSet;
    bool m_premium_frequency_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILongTermCareInsurancePolicyWithIdModel)

#endif // OAILongTermCareInsurancePolicyWithIdModel_H
