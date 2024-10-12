/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIdentityProvider_ListByService_200_response_value_inner.h
 *
 * Identity Provider details.
 */

#ifndef OAIIdentityProvider_ListByService_200_response_value_inner_H
#define OAIIdentityProvider_ListByService_200_response_value_inner_H

#include <QJsonObject>

#include "OAIIdentityProvider_ListByService_200_response_value_inner_properties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIdentityProvider_ListByService_200_response_value_inner_properties;

class OAIIdentityProvider_ListByService_200_response_value_inner : public OAIObject {
public:
    OAIIdentityProvider_ListByService_200_response_value_inner();
    OAIIdentityProvider_ListByService_200_response_value_inner(QString json);
    ~OAIIdentityProvider_ListByService_200_response_value_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIdentityProvider_ListByService_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAIIdentityProvider_ListByService_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIdentityProvider_ListByService_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIdentityProvider_ListByService_200_response_value_inner)

#endif // OAIIdentityProvider_ListByService_200_response_value_inner_H
