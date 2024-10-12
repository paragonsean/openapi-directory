/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIssue_ListByService_200_response_value_inner.h
 *
 * Issue Contract details.
 */

#ifndef OAIIssue_ListByService_200_response_value_inner_H
#define OAIIssue_ListByService_200_response_value_inner_H

#include <QJsonObject>

#include "OAIIssue_ListByService_200_response_value_inner_properties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIssue_ListByService_200_response_value_inner_properties;

class OAIIssue_ListByService_200_response_value_inner : public OAIObject {
public:
    OAIIssue_ListByService_200_response_value_inner();
    OAIIssue_ListByService_200_response_value_inner(QString json);
    ~OAIIssue_ListByService_200_response_value_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIssue_ListByService_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAIIssue_ListByService_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIssue_ListByService_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIssue_ListByService_200_response_value_inner)

#endif // OAIIssue_ListByService_200_response_value_inner_H
