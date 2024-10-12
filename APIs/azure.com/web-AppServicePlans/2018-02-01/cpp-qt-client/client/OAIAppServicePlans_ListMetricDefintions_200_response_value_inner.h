/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListMetricDefintions_200_response_value_inner.h
 *
 * Metadata for the metrics.
 */

#ifndef OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_H
#define OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_H

#include <QJsonObject>

#include "OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties;

class OAIAppServicePlans_ListMetricDefintions_200_response_value_inner : public OAIObject {
public:
    OAIAppServicePlans_ListMetricDefintions_200_response_value_inner();
    OAIAppServicePlans_ListMetricDefintions_200_response_value_inner(QString json);
    ~OAIAppServicePlans_ListMetricDefintions_200_response_value_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListMetricDefintions_200_response_value_inner)

#endif // OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_H
