/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-10-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExpressRouteConnectionId.h
 *
 * The ID of the ExpressRouteConnection.
 */

#ifndef OAIExpressRouteConnectionId_H
#define OAIExpressRouteConnectionId_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIExpressRouteConnectionId : public OAIObject {
public:
    OAIExpressRouteConnectionId();
    OAIExpressRouteConnectionId(QString json);
    ~OAIExpressRouteConnectionId() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpressRouteConnectionId)

#endif // OAIExpressRouteConnectionId_H
