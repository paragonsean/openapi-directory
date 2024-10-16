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
 * OAIMetrics.h
 *
 * 
 */

#ifndef OAIMetrics_H
#define OAIMetrics_H

#include <QJsonObject>

#include "OAIMetrics_response_times_inner.h"
#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMetrics_response_times_inner;

class OAIMetrics : public OAIObject {
public:
    OAIMetrics();
    OAIMetrics(QString json);
    ~OAIMetrics() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getChangesFromLastPeriod() const;
    void setChangesFromLastPeriod(const OAIObject &changes_from_last_period);
    bool is_changes_from_last_period_Set() const;
    bool is_changes_from_last_period_Valid() const;

    QString getEnvironmentUuid() const;
    void setEnvironmentUuid(const QString &environment_uuid);
    bool is_environment_uuid_Set() const;
    bool is_environment_uuid_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    QList<OAIMetrics_response_times_inner> getResponseTimes() const;
    void setResponseTimes(const QList<OAIMetrics_response_times_inner> &response_times);
    bool is_response_times_Set() const;
    bool is_response_times_Valid() const;

    OAIObject getThisTimePeriod() const;
    void setThisTimePeriod(const OAIObject &this_time_period);
    bool is_this_time_period_Set() const;
    bool is_this_time_period_Valid() const;

    QString getTimeframe() const;
    void setTimeframe(const QString &timeframe);
    bool is_timeframe_Set() const;
    bool is_timeframe_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_changes_from_last_period;
    bool m_changes_from_last_period_isSet;
    bool m_changes_from_last_period_isValid;

    QString m_environment_uuid;
    bool m_environment_uuid_isSet;
    bool m_environment_uuid_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    QList<OAIMetrics_response_times_inner> m_response_times;
    bool m_response_times_isSet;
    bool m_response_times_isValid;

    OAIObject m_this_time_period;
    bool m_this_time_period_isSet;
    bool m_this_time_period_isValid;

    QString m_timeframe;
    bool m_timeframe_isSet;
    bool m_timeframe_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMetrics)

#endif // OAIMetrics_H
