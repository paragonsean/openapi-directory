/**
 * Football Prediction API
 * The Football Prediction API allows developers to get predictions for upcoming football (soccer) matches, results for past matches, and performance monitoring for statistical models.
 *
 * The version of the OpenAPI document: 2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_api_v2_performance_stats_get_200_response_data_accuracy.h
 *
 * 
 */

#ifndef OAI_api_v2_performance_stats_get_200_response_data_accuracy_H
#define OAI_api_v2_performance_stats_get_200_response_data_accuracy_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_v2_performance_stats_get_200_response_data_accuracy : public OAIObject {
public:
    OAI_api_v2_performance_stats_get_200_response_data_accuracy();
    OAI_api_v2_performance_stats_get_200_response_data_accuracy(QString json);
    ~OAI_api_v2_performance_stats_get_200_response_data_accuracy() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getLast14Days() const;
    void setLast14Days(const double &last_14_days);
    bool is_last_14_days_Set() const;
    bool is_last_14_days_Valid() const;

    double getLast30Days() const;
    void setLast30Days(const double &last_30_days);
    bool is_last_30_days_Set() const;
    bool is_last_30_days_Valid() const;

    double getLast7Days() const;
    void setLast7Days(const double &last_7_days);
    bool is_last_7_days_Set() const;
    bool is_last_7_days_Valid() const;

    double getYesterday() const;
    void setYesterday(const double &yesterday);
    bool is_yesterday_Set() const;
    bool is_yesterday_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_last_14_days;
    bool m_last_14_days_isSet;
    bool m_last_14_days_isValid;

    double m_last_30_days;
    bool m_last_30_days_isSet;
    bool m_last_30_days_isValid;

    double m_last_7_days;
    bool m_last_7_days_isSet;
    bool m_last_7_days_isValid;

    double m_yesterday;
    bool m_yesterday_isSet;
    bool m_yesterday_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_v2_performance_stats_get_200_response_data_accuracy)

#endif // OAI_api_v2_performance_stats_get_200_response_data_accuracy_H
