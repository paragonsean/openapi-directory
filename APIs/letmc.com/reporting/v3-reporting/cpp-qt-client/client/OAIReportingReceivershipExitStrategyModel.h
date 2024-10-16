/**
 * LetMC Api V3, reporting
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-reporting
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIReportingReceivershipExitStrategyModel.h
 *
 * Helper Model - Exit Strategy
 */

#ifndef OAIReportingReceivershipExitStrategyModel_H
#define OAIReportingReceivershipExitStrategyModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIReportingReceivershipExitStrategyModel : public OAIObject {
public:
    OAIReportingReceivershipExitStrategyModel();
    OAIReportingReceivershipExitStrategyModel(QString json);
    ~OAIReportingReceivershipExitStrategyModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCompiled() const;
    void setCompiled(const QDateTime &compiled);
    bool is_compiled_Set() const;
    bool is_compiled_Valid() const;

    QString getCompiledById() const;
    void setCompiledById(const QString &compiled_by_id);
    bool is_compiled_by_id_Set() const;
    bool is_compiled_by_id_Valid() const;

    QString getDisplayCompiledById() const;
    void setDisplayCompiledById(const QString &display_compiled_by_id);
    bool is_display_compiled_by_id_Set() const;
    bool is_display_compiled_by_id_Valid() const;

    QString getExtraNotes() const;
    void setExtraNotes(const QString &extra_notes);
    bool is_extra_notes_Set() const;
    bool is_extra_notes_Valid() const;

    QString getLenderResponse() const;
    void setLenderResponse(const QString &lender_response);
    bool is_lender_response_Set() const;
    bool is_lender_response_Valid() const;

    QDateTime getLenderResponseDate() const;
    void setLenderResponseDate(const QDateTime &lender_response_date);
    bool is_lender_response_date_Set() const;
    bool is_lender_response_date_Valid() const;

    QDateTime getLockChanged() const;
    void setLockChanged(const QDateTime &lock_changed);
    bool is_lock_changed_Set() const;
    bool is_lock_changed_Valid() const;

    double getMortgageArrears() const;
    void setMortgageArrears(const double &mortgage_arrears);
    bool is_mortgage_arrears_Set() const;
    bool is_mortgage_arrears_Valid() const;

    double getMortgageBalance() const;
    void setMortgageBalance(const double &mortgage_balance);
    bool is_mortgage_balance_Set() const;
    bool is_mortgage_balance_Valid() const;

    double getMortgageCmi() const;
    void setMortgageCmi(const double &mortgage_cmi);
    bool is_mortgage_cmi_Set() const;
    bool is_mortgage_cmi_Valid() const;

    QString getRecommendation() const;
    void setRecommendation(const QString &recommendation);
    bool is_recommendation_Set() const;
    bool is_recommendation_Valid() const;

    QDateTime getReviewDate() const;
    void setReviewDate(const QDateTime &review_date);
    bool is_review_date_Set() const;
    bool is_review_date_Valid() const;

    QDateTime getSentToLender() const;
    void setSentToLender(const QDateTime &sent_to_lender);
    bool is_sent_to_lender_Set() const;
    bool is_sent_to_lender_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_compiled;
    bool m_compiled_isSet;
    bool m_compiled_isValid;

    QString m_compiled_by_id;
    bool m_compiled_by_id_isSet;
    bool m_compiled_by_id_isValid;

    QString m_display_compiled_by_id;
    bool m_display_compiled_by_id_isSet;
    bool m_display_compiled_by_id_isValid;

    QString m_extra_notes;
    bool m_extra_notes_isSet;
    bool m_extra_notes_isValid;

    QString m_lender_response;
    bool m_lender_response_isSet;
    bool m_lender_response_isValid;

    QDateTime m_lender_response_date;
    bool m_lender_response_date_isSet;
    bool m_lender_response_date_isValid;

    QDateTime m_lock_changed;
    bool m_lock_changed_isSet;
    bool m_lock_changed_isValid;

    double m_mortgage_arrears;
    bool m_mortgage_arrears_isSet;
    bool m_mortgage_arrears_isValid;

    double m_mortgage_balance;
    bool m_mortgage_balance_isSet;
    bool m_mortgage_balance_isValid;

    double m_mortgage_cmi;
    bool m_mortgage_cmi_isSet;
    bool m_mortgage_cmi_isValid;

    QString m_recommendation;
    bool m_recommendation_isSet;
    bool m_recommendation_isValid;

    QDateTime m_review_date;
    bool m_review_date_isSet;
    bool m_review_date_isValid;

    QDateTime m_sent_to_lender;
    bool m_sent_to_lender_isSet;
    bool m_sent_to_lender_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReportingReceivershipExitStrategyModel)

#endif // OAIReportingReceivershipExitStrategyModel_H
