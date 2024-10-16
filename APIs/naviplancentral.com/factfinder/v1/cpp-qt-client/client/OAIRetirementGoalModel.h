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
 * OAIRetirementGoalModel.h
 *
 * 
 */

#ifndef OAIRetirementGoalModel_H
#define OAIRetirementGoalModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRetirementGoalModel : public OAIObject {
public:
    OAIRetirementGoalModel();
    OAIRetirementGoalModel(QString json);
    ~OAIRetirementGoalModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getExternalDestinationId() const;
    void setExternalDestinationId(const QString &external_destination_id);
    bool is_external_destination_id_Set() const;
    bool is_external_destination_id_Valid() const;

    qint32 getFactFinderId() const;
    void setFactFinderId(const qint32 &fact_finder_id);
    bool is_fact_finder_id_Set() const;
    bool is_fact_finder_id_Valid() const;

    QDateTime getHead1RetirementDate() const;
    void setHead1RetirementDate(const QDateTime &head1_retirement_date);
    bool is_head1_retirement_date_Set() const;
    bool is_head1_retirement_date_Valid() const;

    QDateTime getHead2RetirementDate() const;
    void setHead2RetirementDate(const QDateTime &head2_retirement_date);
    bool is_head2_retirement_date_Set() const;
    bool is_head2_retirement_date_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    qint32 m_fact_finder_id;
    bool m_fact_finder_id_isSet;
    bool m_fact_finder_id_isValid;

    QDateTime m_head1_retirement_date;
    bool m_head1_retirement_date_isSet;
    bool m_head1_retirement_date_isValid;

    QDateTime m_head2_retirement_date;
    bool m_head2_retirement_date_isSet;
    bool m_head2_retirement_date_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRetirementGoalModel)

#endif // OAIRetirementGoalModel_H
