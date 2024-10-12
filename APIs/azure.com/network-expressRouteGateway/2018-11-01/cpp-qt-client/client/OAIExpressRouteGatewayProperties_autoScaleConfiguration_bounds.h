/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds.h
 *
 * Minimum and maximum number of scale units to deploy.
 */

#ifndef OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds_H
#define OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds : public OAIObject {
public:
    OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds();
    OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds(QString json);
    ~OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getMax() const;
    void setMax(const qint32 &max);
    bool is_max_Set() const;
    bool is_max_Valid() const;

    qint32 getMin() const;
    void setMin(const qint32 &min);
    bool is_min_Set() const;
    bool is_min_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_max;
    bool m_max_isSet;
    bool m_max_isValid;

    qint32 m_min;
    bool m_min_isSet;
    bool m_min_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds)

#endif // OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds_H
