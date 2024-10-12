/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMetrics_response_times_inner.h
 *
 * 
 */

#ifndef OAIMetrics_response_times_inner_H
#define OAIMetrics_response_times_inner_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMetrics_response_times_inner : public OAIObject {
public:
    OAIMetrics_response_times_inner();
    OAIMetrics_response_times_inner(QString json);
    ~OAIMetrics_response_times_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAvgResponseTimeMs() const;
    void setAvgResponseTimeMs(const qint32 &avg_response_time_ms);
    bool is_avg_response_time_ms_Set() const;
    bool is_avg_response_time_ms_Valid() const;

    qint32 getSuccessRatio() const;
    void setSuccessRatio(const qint32 &success_ratio);
    bool is_success_ratio_Set() const;
    bool is_success_ratio_Valid() const;

    qint32 getTimestamp() const;
    void setTimestamp(const qint32 &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_avg_response_time_ms;
    bool m_avg_response_time_ms_isSet;
    bool m_avg_response_time_ms_isValid;

    qint32 m_success_ratio;
    bool m_success_ratio_isSet;
    bool m_success_ratio_isValid;

    qint32 m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMetrics_response_times_inner)

#endif // OAIMetrics_response_times_inner_H
