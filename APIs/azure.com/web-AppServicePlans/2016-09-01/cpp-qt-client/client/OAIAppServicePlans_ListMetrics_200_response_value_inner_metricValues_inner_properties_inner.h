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
 * OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner.h
 *
 * Resource metric property.
 */

#ifndef OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner_H
#define OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner : public OAIObject {
public:
    OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner();
    OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner(QString json);
    ~OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner)

#endif // OAIAppServicePlans_ListMetrics_200_response_value_inner_metricValues_inner_properties_inner_H
