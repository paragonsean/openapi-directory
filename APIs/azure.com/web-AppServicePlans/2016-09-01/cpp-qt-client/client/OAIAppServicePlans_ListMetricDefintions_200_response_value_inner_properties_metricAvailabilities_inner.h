/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner.h
 *
 * Metrics availability and retention.
 */

#ifndef OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner_H
#define OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner : public OAIObject {
public:
    OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner();
    OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner(QString json);
    ~OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRetention() const;
    void setRetention(const QString &retention);
    bool is_retention_Set() const;
    bool is_retention_Valid() const;

    QString getTimeGrain() const;
    void setTimeGrain(const QString &time_grain);
    bool is_time_grain_Set() const;
    bool is_time_grain_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_retention;
    bool m_retention_isSet;
    bool m_retention_isValid;

    QString m_time_grain;
    bool m_time_grain_isSet;
    bool m_time_grain_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner)

#endif // OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner_H
