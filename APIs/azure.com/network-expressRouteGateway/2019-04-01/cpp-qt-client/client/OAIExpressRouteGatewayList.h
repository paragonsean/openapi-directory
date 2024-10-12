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
 * OAIExpressRouteGatewayList.h
 *
 * List of ExpressRoute gateways.
 */

#ifndef OAIExpressRouteGatewayList_H
#define OAIExpressRouteGatewayList_H

#include <QJsonObject>

#include "OAIExpressRouteGateway.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIExpressRouteGateway;

class OAIExpressRouteGatewayList : public OAIObject {
public:
    OAIExpressRouteGatewayList();
    OAIExpressRouteGatewayList(QString json);
    ~OAIExpressRouteGatewayList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIExpressRouteGateway> getValue() const;
    void setValue(const QList<OAIExpressRouteGateway> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIExpressRouteGateway> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpressRouteGatewayList)

#endif // OAIExpressRouteGatewayList_H
