/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITarget.h
 *
 * for an any panel
 */

#ifndef OAITarget_H
#define OAITarget_H

#include <QJsonObject>

#include "OAIStackdriverAlignOptions.h"
#include "OAITarget_bucketAggs_inner.h"
#include "OAITarget_group_inner.h"
#include "OAITarget_metrics_inner.h"
#include "OAITarget_where_inner.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStackdriverAlignOptions;
class OAITarget_bucketAggs_inner;
class OAITarget_group_inner;
class OAITarget_metrics_inner;
class OAITarget_where_inner;

class OAITarget : public OAIObject {
public:
    OAITarget();
    OAITarget(QString json);
    ~OAITarget() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAlias() const;
    void setAlias(const QString &alias);
    bool is_alias_Set() const;
    bool is_alias_Valid() const;

    QString getAliasBy() const;
    void setAliasBy(const QString &alias_by);
    bool is_alias_by_Set() const;
    bool is_alias_by_Valid() const;

    QList<OAIStackdriverAlignOptions> getAlignOptions() const;
    void setAlignOptions(const QList<OAIStackdriverAlignOptions> &align_options);
    bool is_align_options_Set() const;
    bool is_align_options_Valid() const;

    QString getAlignmentPeriod() const;
    void setAlignmentPeriod(const QString &alignment_period);
    bool is_alignment_period_Set() const;
    bool is_alignment_period_Valid() const;

    QList<OAITarget_bucketAggs_inner> getBucketAggs() const;
    void setBucketAggs(const QList<OAITarget_bucketAggs_inner> &bucket_aggs);
    bool is_bucket_aggs_Set() const;
    bool is_bucket_aggs_Valid() const;

    QString getCrossSeriesReducer() const;
    void setCrossSeriesReducer(const QString &cross_series_reducer);
    bool is_cross_series_reducer_Set() const;
    bool is_cross_series_reducer_Valid() const;

    QString getDatasource() const;
    void setDatasource(const QString &datasource);
    bool is_datasource_Set() const;
    bool is_datasource_Valid() const;

    QMap<QString, QString> getDimensions() const;
    void setDimensions(const QMap<QString, QString> &dimensions);
    bool is_dimensions_Set() const;
    bool is_dimensions_Valid() const;

    QString getDsType() const;
    void setDsType(const QString &ds_type);
    bool is_ds_type_Set() const;
    bool is_ds_type_Valid() const;

    QString getExpr() const;
    void setExpr(const QString &expr);
    bool is_expr_Set() const;
    bool is_expr_Valid() const;

    QList<QString> getFilters() const;
    void setFilters(const QList<QString> &filters);
    bool is_filters_Set() const;
    bool is_filters_Valid() const;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QList<OAITarget_group_inner> getGroup() const;
    void setGroup(const QList<OAITarget_group_inner> &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    QList<QString> getGroupBys() const;
    void setGroupBys(const QList<QString> &group_bys);
    bool is_group_bys_Set() const;
    bool is_group_bys_Valid() const;

    bool isHide() const;
    void setHide(const bool &hide);
    bool is_hide_Set() const;
    bool is_hide_Valid() const;

    bool isInstant() const;
    void setInstant(const bool &instant);
    bool is_instant_Set() const;
    bool is_instant_Valid() const;

    QString getInterval() const;
    void setInterval(const QString &interval);
    bool is_interval_Set() const;
    bool is_interval_Valid() const;

    qint64 getIntervalFactor() const;
    void setIntervalFactor(const qint64 &interval_factor);
    bool is_interval_factor_Set() const;
    bool is_interval_factor_Valid() const;

    QString getLegendFormat() const;
    void setLegendFormat(const QString &legend_format);
    bool is_legend_format_Set() const;
    bool is_legend_format_Valid() const;

    QString getMeasurement() const;
    void setMeasurement(const QString &measurement);
    bool is_measurement_Set() const;
    bool is_measurement_Valid() const;

    QString getMetricColumn() const;
    void setMetricColumn(const QString &metric_column);
    bool is_metric_column_Set() const;
    bool is_metric_column_Valid() const;

    QString getMetricKind() const;
    void setMetricKind(const QString &metric_kind);
    bool is_metric_kind_Set() const;
    bool is_metric_kind_Valid() const;

    QString getMetricName() const;
    void setMetricName(const QString &metric_name);
    bool is_metric_name_Set() const;
    bool is_metric_name_Valid() const;

    QString getMetricType() const;
    void setMetricType(const QString &metric_type);
    bool is_metric_type_Set() const;
    bool is_metric_type_Valid() const;

    QList<OAITarget_metrics_inner> getMetrics() const;
    void setMetrics(const QList<OAITarget_metrics_inner> &metrics);
    bool is_metrics_Set() const;
    bool is_metrics_Valid() const;

    QString getRNamespace() const;
    void setRNamespace(const QString &r_namespace);
    bool is_r_namespace_Set() const;
    bool is_r_namespace_Valid() const;

    QString getPerSeriesAligner() const;
    void setPerSeriesAligner(const QString &per_series_aligner);
    bool is_per_series_aligner_Set() const;
    bool is_per_series_aligner_Valid() const;

    QString getPeriod() const;
    void setPeriod(const QString &period);
    bool is_period_Set() const;
    bool is_period_Valid() const;

    QString getProjectName() const;
    void setProjectName(const QString &project_name);
    bool is_project_name_Set() const;
    bool is_project_name_Valid() const;

    QString getQuery() const;
    void setQuery(const QString &query);
    bool is_query_Set() const;
    bool is_query_Valid() const;

    bool isRawQuery() const;
    void setRawQuery(const bool &raw_query);
    bool is_raw_query_Set() const;
    bool is_raw_query_Valid() const;

    QString getRawSql() const;
    void setRawSql(const QString &raw_sql);
    bool is_raw_sql_Set() const;
    bool is_raw_sql_Valid() const;

    QString getRefId() const;
    void setRefId(const QString &ref_id);
    bool is_ref_id_Set() const;
    bool is_ref_id_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    QList<QList<OAITarget_group_inner>> getSelect() const;
    void setSelect(const QList<QList<OAITarget_group_inner>> &select);
    bool is_select_Set() const;
    bool is_select_Valid() const;

    QList<QString> getStatistics() const;
    void setStatistics(const QList<QString> &statistics);
    bool is_statistics_Set() const;
    bool is_statistics_Valid() const;

    qint64 getStep() const;
    void setStep(const qint64 &step);
    bool is_step_Set() const;
    bool is_step_Valid() const;

    QString getTable() const;
    void setTable(const QString &table);
    bool is_table_Set() const;
    bool is_table_Valid() const;

    QString getTarget() const;
    void setTarget(const QString &target);
    bool is_target_Set() const;
    bool is_target_Valid() const;

    QString getTimeColumn() const;
    void setTimeColumn(const QString &time_column);
    bool is_time_column_Set() const;
    bool is_time_column_Valid() const;

    QString getTimeField() const;
    void setTimeField(const QString &time_field);
    bool is_time_field_Set() const;
    bool is_time_field_Valid() const;

    QString getValueType() const;
    void setValueType(const QString &value_type);
    bool is_value_type_Set() const;
    bool is_value_type_Valid() const;

    QList<OAITarget_where_inner> getWhere() const;
    void setWhere(const QList<OAITarget_where_inner> &where);
    bool is_where_Set() const;
    bool is_where_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_alias;
    bool m_alias_isSet;
    bool m_alias_isValid;

    QString m_alias_by;
    bool m_alias_by_isSet;
    bool m_alias_by_isValid;

    QList<OAIStackdriverAlignOptions> m_align_options;
    bool m_align_options_isSet;
    bool m_align_options_isValid;

    QString m_alignment_period;
    bool m_alignment_period_isSet;
    bool m_alignment_period_isValid;

    QList<OAITarget_bucketAggs_inner> m_bucket_aggs;
    bool m_bucket_aggs_isSet;
    bool m_bucket_aggs_isValid;

    QString m_cross_series_reducer;
    bool m_cross_series_reducer_isSet;
    bool m_cross_series_reducer_isValid;

    QString m_datasource;
    bool m_datasource_isSet;
    bool m_datasource_isValid;

    QMap<QString, QString> m_dimensions;
    bool m_dimensions_isSet;
    bool m_dimensions_isValid;

    QString m_ds_type;
    bool m_ds_type_isSet;
    bool m_ds_type_isValid;

    QString m_expr;
    bool m_expr_isSet;
    bool m_expr_isValid;

    QList<QString> m_filters;
    bool m_filters_isSet;
    bool m_filters_isValid;

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QList<OAITarget_group_inner> m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    QList<QString> m_group_bys;
    bool m_group_bys_isSet;
    bool m_group_bys_isValid;

    bool m_hide;
    bool m_hide_isSet;
    bool m_hide_isValid;

    bool m_instant;
    bool m_instant_isSet;
    bool m_instant_isValid;

    QString m_interval;
    bool m_interval_isSet;
    bool m_interval_isValid;

    qint64 m_interval_factor;
    bool m_interval_factor_isSet;
    bool m_interval_factor_isValid;

    QString m_legend_format;
    bool m_legend_format_isSet;
    bool m_legend_format_isValid;

    QString m_measurement;
    bool m_measurement_isSet;
    bool m_measurement_isValid;

    QString m_metric_column;
    bool m_metric_column_isSet;
    bool m_metric_column_isValid;

    QString m_metric_kind;
    bool m_metric_kind_isSet;
    bool m_metric_kind_isValid;

    QString m_metric_name;
    bool m_metric_name_isSet;
    bool m_metric_name_isValid;

    QString m_metric_type;
    bool m_metric_type_isSet;
    bool m_metric_type_isValid;

    QList<OAITarget_metrics_inner> m_metrics;
    bool m_metrics_isSet;
    bool m_metrics_isValid;

    QString m_r_namespace;
    bool m_r_namespace_isSet;
    bool m_r_namespace_isValid;

    QString m_per_series_aligner;
    bool m_per_series_aligner_isSet;
    bool m_per_series_aligner_isValid;

    QString m_period;
    bool m_period_isSet;
    bool m_period_isValid;

    QString m_project_name;
    bool m_project_name_isSet;
    bool m_project_name_isValid;

    QString m_query;
    bool m_query_isSet;
    bool m_query_isValid;

    bool m_raw_query;
    bool m_raw_query_isSet;
    bool m_raw_query_isValid;

    QString m_raw_sql;
    bool m_raw_sql_isSet;
    bool m_raw_sql_isValid;

    QString m_ref_id;
    bool m_ref_id_isSet;
    bool m_ref_id_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    QList<QList<OAITarget_group_inner>> m_select;
    bool m_select_isSet;
    bool m_select_isValid;

    QList<QString> m_statistics;
    bool m_statistics_isSet;
    bool m_statistics_isValid;

    qint64 m_step;
    bool m_step_isSet;
    bool m_step_isValid;

    QString m_table;
    bool m_table_isSet;
    bool m_table_isValid;

    QString m_target;
    bool m_target_isSet;
    bool m_target_isValid;

    QString m_time_column;
    bool m_time_column_isSet;
    bool m_time_column_isValid;

    QString m_time_field;
    bool m_time_field_isSet;
    bool m_time_field_isValid;

    QString m_value_type;
    bool m_value_type_isSet;
    bool m_value_type_isValid;

    QList<OAITarget_where_inner> m_where;
    bool m_where_isSet;
    bool m_where_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITarget)

#endif // OAITarget_H
