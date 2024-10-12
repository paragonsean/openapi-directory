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
 * OAIEndpointServicesListResult.h
 *
 * Response for the ListAvailableEndpointServices API service call.
 */

#ifndef OAIEndpointServicesListResult_H
#define OAIEndpointServicesListResult_H

#include <QJsonObject>

#include "OAIEndpointServiceResult.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEndpointServiceResult;

class OAIEndpointServicesListResult : public OAIObject {
public:
    OAIEndpointServicesListResult();
    OAIEndpointServicesListResult(QString json);
    ~OAIEndpointServicesListResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIEndpointServiceResult> getValue() const;
    void setValue(const QList<OAIEndpointServiceResult> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIEndpointServiceResult> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpointServicesListResult)

#endif // OAIEndpointServicesListResult_H
