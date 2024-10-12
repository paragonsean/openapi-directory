/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExpressRouteConnectionProperties.h
 *
 * Properties of the ExpressRouteConnection subresource.
 */

#ifndef OAIExpressRouteConnectionProperties_H
#define OAIExpressRouteConnectionProperties_H

#include <QJsonObject>

#include "OAIExpressRouteCircuitPeeringId.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIExpressRouteCircuitPeeringId;

class OAIExpressRouteConnectionProperties : public OAIObject {
public:
    OAIExpressRouteConnectionProperties();
    OAIExpressRouteConnectionProperties(QString json);
    ~OAIExpressRouteConnectionProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthorizationKey() const;
    void setAuthorizationKey(const QString &authorization_key);
    bool is_authorization_key_Set() const;
    bool is_authorization_key_Valid() const;

    OAIExpressRouteCircuitPeeringId getExpressRouteCircuitPeering() const;
    void setExpressRouteCircuitPeering(const OAIExpressRouteCircuitPeeringId &express_route_circuit_peering);
    bool is_express_route_circuit_peering_Set() const;
    bool is_express_route_circuit_peering_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    qint32 getRoutingWeight() const;
    void setRoutingWeight(const qint32 &routing_weight);
    bool is_routing_weight_Set() const;
    bool is_routing_weight_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_authorization_key;
    bool m_authorization_key_isSet;
    bool m_authorization_key_isValid;

    OAIExpressRouteCircuitPeeringId m_express_route_circuit_peering;
    bool m_express_route_circuit_peering_isSet;
    bool m_express_route_circuit_peering_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;

    qint32 m_routing_weight;
    bool m_routing_weight_isSet;
    bool m_routing_weight_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpressRouteConnectionProperties)

#endif // OAIExpressRouteConnectionProperties_H
