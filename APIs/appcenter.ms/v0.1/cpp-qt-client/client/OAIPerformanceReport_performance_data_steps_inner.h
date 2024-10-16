/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPerformanceReport_performance_data_steps_inner.h
 *
 * 
 */

#ifndef OAIPerformanceReport_performance_data_steps_inner_H
#define OAIPerformanceReport_performance_data_steps_inner_H

#include <QJsonObject>

#include "OAIPerformanceReport_performance_data_steps_inner_samples_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPerformanceReport_performance_data_steps_inner_samples_inner;

class OAIPerformanceReport_performance_data_steps_inner : public OAIObject {
public:
    OAIPerformanceReport_performance_data_steps_inner();
    OAIPerformanceReport_performance_data_steps_inner(QString json);
    ~OAIPerformanceReport_performance_data_steps_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAvgCpu() const;
    void setAvgCpu(const double &avg_cpu);
    bool is_avg_cpu_Set() const;
    bool is_avg_cpu_Valid() const;

    double getAvgMem() const;
    void setAvgMem(const double &avg_mem);
    bool is_avg_mem_Set() const;
    bool is_avg_mem_Valid() const;

    double getElapsedSecs() const;
    void setElapsedSecs(const double &elapsed_secs);
    bool is_elapsed_secs_Set() const;
    bool is_elapsed_secs_Valid() const;

    double getElapsedSecsEnd() const;
    void setElapsedSecsEnd(const double &elapsed_secs_end);
    bool is_elapsed_secs_end_Set() const;
    bool is_elapsed_secs_end_Valid() const;

    double getElapsedSecsStart() const;
    void setElapsedSecsStart(const double &elapsed_secs_start);
    bool is_elapsed_secs_start_Set() const;
    bool is_elapsed_secs_start_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIPerformanceReport_performance_data_steps_inner_samples_inner> getSamples() const;
    void setSamples(const QList<OAIPerformanceReport_performance_data_steps_inner_samples_inner> &samples);
    bool is_samples_Set() const;
    bool is_samples_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_avg_cpu;
    bool m_avg_cpu_isSet;
    bool m_avg_cpu_isValid;

    double m_avg_mem;
    bool m_avg_mem_isSet;
    bool m_avg_mem_isValid;

    double m_elapsed_secs;
    bool m_elapsed_secs_isSet;
    bool m_elapsed_secs_isValid;

    double m_elapsed_secs_end;
    bool m_elapsed_secs_end_isSet;
    bool m_elapsed_secs_end_isValid;

    double m_elapsed_secs_start;
    bool m_elapsed_secs_start_isSet;
    bool m_elapsed_secs_start_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIPerformanceReport_performance_data_steps_inner_samples_inner> m_samples;
    bool m_samples_isSet;
    bool m_samples_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPerformanceReport_performance_data_steps_inner)

#endif // OAIPerformanceReport_performance_data_steps_inner_H
