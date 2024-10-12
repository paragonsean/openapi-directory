/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMetricSpecification_V1.h
 *
 * Metric specification version 1.
 */

#ifndef OAIMetricSpecification_V1_H
#define OAIMetricSpecification_V1_H

#include <QJsonObject>

#include "OAIMetricDimension_V1.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMetricDimension_V1;

class OAIMetricSpecification_V1 : public OAIObject {
public:
    OAIMetricSpecification_V1();
    OAIMetricSpecification_V1(QString json);
    ~OAIMetricSpecification_V1() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAggregationType() const;
    void setAggregationType(const QString &aggregation_type);
    bool is_aggregation_type_Set() const;
    bool is_aggregation_type_Valid() const;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QList<OAIMetricDimension_V1> getDimensions() const;
    void setDimensions(const QList<OAIMetricDimension_V1> &dimensions);
    bool is_dimensions_Set() const;
    bool is_dimensions_Valid() const;

    QString getDisplayDescription() const;
    void setDisplayDescription(const QString &display_description);
    bool is_display_description_Set() const;
    bool is_display_description_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    bool isFillGapWithZero() const;
    void setFillGapWithZero(const bool &fill_gap_with_zero);
    bool is_fill_gap_with_zero_Set() const;
    bool is_fill_gap_with_zero_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getResourceIdDimensionNameOverride() const;
    void setResourceIdDimensionNameOverride(const QString &resource_id_dimension_name_override);
    bool is_resource_id_dimension_name_override_Set() const;
    bool is_resource_id_dimension_name_override_Valid() const;

    QList<QString> getSupportedAggregationTypes() const;
    void setSupportedAggregationTypes(const QList<QString> &supported_aggregation_types);
    bool is_supported_aggregation_types_Set() const;
    bool is_supported_aggregation_types_Valid() const;

    QList<QString> getSupportedTimeGrainTypes() const;
    void setSupportedTimeGrainTypes(const QList<QString> &supported_time_grain_types);
    bool is_supported_time_grain_types_Set() const;
    bool is_supported_time_grain_types_Valid() const;

    QString getUnit() const;
    void setUnit(const QString &unit);
    bool is_unit_Set() const;
    bool is_unit_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_aggregation_type;
    bool m_aggregation_type_isSet;
    bool m_aggregation_type_isValid;

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QList<OAIMetricDimension_V1> m_dimensions;
    bool m_dimensions_isSet;
    bool m_dimensions_isValid;

    QString m_display_description;
    bool m_display_description_isSet;
    bool m_display_description_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    bool m_fill_gap_with_zero;
    bool m_fill_gap_with_zero_isSet;
    bool m_fill_gap_with_zero_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_resource_id_dimension_name_override;
    bool m_resource_id_dimension_name_override_isSet;
    bool m_resource_id_dimension_name_override_isValid;

    QList<QString> m_supported_aggregation_types;
    bool m_supported_aggregation_types_isSet;
    bool m_supported_aggregation_types_isValid;

    QList<QString> m_supported_time_grain_types;
    bool m_supported_time_grain_types_isSet;
    bool m_supported_time_grain_types_isValid;

    QString m_unit;
    bool m_unit_isSet;
    bool m_unit_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMetricSpecification_V1)

#endif // OAIMetricSpecification_V1_H
