/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITagPerformance.h
 *
 * Represents performance data for a particular tag in a trained iteration.
 */

#ifndef OAITagPerformance_H
#define OAITagPerformance_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITagPerformance : public OAIObject {
public:
    OAITagPerformance();
    OAITagPerformance(QString json);
    ~OAITagPerformance() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getAveragePrecision() const;
    void setAveragePrecision(const float &average_precision);
    bool is_average_precision_Set() const;
    bool is_average_precision_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    float getPrecision() const;
    void setPrecision(const float &precision);
    bool is_precision_Set() const;
    bool is_precision_Valid() const;

    float getPrecisionStdDeviation() const;
    void setPrecisionStdDeviation(const float &precision_std_deviation);
    bool is_precision_std_deviation_Set() const;
    bool is_precision_std_deviation_Valid() const;

    float getRecall() const;
    void setRecall(const float &recall);
    bool is_recall_Set() const;
    bool is_recall_Valid() const;

    float getRecallStdDeviation() const;
    void setRecallStdDeviation(const float &recall_std_deviation);
    bool is_recall_std_deviation_Set() const;
    bool is_recall_std_deviation_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    float m_average_precision;
    bool m_average_precision_isSet;
    bool m_average_precision_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    float m_precision;
    bool m_precision_isSet;
    bool m_precision_isValid;

    float m_precision_std_deviation;
    bool m_precision_std_deviation_isSet;
    bool m_precision_std_deviation_isValid;

    float m_recall;
    bool m_recall_isSet;
    bool m_recall_isValid;

    float m_recall_std_deviation;
    bool m_recall_std_deviation_isSet;
    bool m_recall_std_deviation_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITagPerformance)

#endif // OAITagPerformance_H
