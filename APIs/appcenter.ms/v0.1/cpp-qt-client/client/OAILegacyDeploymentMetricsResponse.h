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
 * OAILegacyDeploymentMetricsResponse.h
 *
 * 
 */

#ifndef OAILegacyDeploymentMetricsResponse_H
#define OAILegacyDeploymentMetricsResponse_H

#include <QJsonObject>

#include "OAILegacyDeploymentMetricsResponse_metrics_value.h"
#include <QMap>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILegacyDeploymentMetricsResponse_metrics_value;

class OAILegacyDeploymentMetricsResponse : public OAIObject {
public:
    OAILegacyDeploymentMetricsResponse();
    OAILegacyDeploymentMetricsResponse(QString json);
    ~OAILegacyDeploymentMetricsResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, OAILegacyDeploymentMetricsResponse_metrics_value> getMetrics() const;
    void setMetrics(const QMap<QString, OAILegacyDeploymentMetricsResponse_metrics_value> &metrics);
    bool is_metrics_Set() const;
    bool is_metrics_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, OAILegacyDeploymentMetricsResponse_metrics_value> m_metrics;
    bool m_metrics_isSet;
    bool m_metrics_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILegacyDeploymentMetricsResponse)

#endif // OAILegacyDeploymentMetricsResponse_H
