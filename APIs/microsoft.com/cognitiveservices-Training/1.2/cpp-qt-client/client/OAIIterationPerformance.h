/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIterationPerformance.h
 *
 * Represents the detailed performance data for a trained iteration
 */

#ifndef OAIIterationPerformance_H
#define OAIIterationPerformance_H

#include <QJsonObject>

#include "OAITagPerformance.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITagPerformance;

class OAIIterationPerformance : public OAIObject {
public:
    OAIIterationPerformance();
    OAIIterationPerformance(QString json);
    ~OAIIterationPerformance() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAITagPerformance> getPerTagPerformance() const;
    void setPerTagPerformance(const QList<OAITagPerformance> &per_tag_performance);
    bool is_per_tag_performance_Set() const;
    bool is_per_tag_performance_Valid() const;

    double getPrecision() const;
    void setPrecision(const double &precision);
    bool is_precision_Set() const;
    bool is_precision_Valid() const;

    double getPrecisionStdDeviation() const;
    void setPrecisionStdDeviation(const double &precision_std_deviation);
    bool is_precision_std_deviation_Set() const;
    bool is_precision_std_deviation_Valid() const;

    double getRecall() const;
    void setRecall(const double &recall);
    bool is_recall_Set() const;
    bool is_recall_Valid() const;

    double getRecallStdDeviation() const;
    void setRecallStdDeviation(const double &recall_std_deviation);
    bool is_recall_std_deviation_Set() const;
    bool is_recall_std_deviation_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAITagPerformance> m_per_tag_performance;
    bool m_per_tag_performance_isSet;
    bool m_per_tag_performance_isValid;

    double m_precision;
    bool m_precision_isSet;
    bool m_precision_isValid;

    double m_precision_std_deviation;
    bool m_precision_std_deviation_isSet;
    bool m_precision_std_deviation_isValid;

    double m_recall;
    bool m_recall_isSet;
    bool m_recall_isValid;

    double m_recall_std_deviation;
    bool m_recall_std_deviation_isSet;
    bool m_recall_std_deviation_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIterationPerformance)

#endif // OAIIterationPerformance_H
