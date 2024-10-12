/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIdentityProviderUpdateParameters.h
 *
 * Parameters supplied to update Identity Provider
 */

#ifndef OAIIdentityProviderUpdateParameters_H
#define OAIIdentityProviderUpdateParameters_H

#include <QJsonObject>

#include "OAIIdentityProviderUpdateProperties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIdentityProviderUpdateProperties;

class OAIIdentityProviderUpdateParameters : public OAIObject {
public:
    OAIIdentityProviderUpdateParameters();
    OAIIdentityProviderUpdateParameters(QString json);
    ~OAIIdentityProviderUpdateParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIdentityProviderUpdateProperties getProperties() const;
    void setProperties(const OAIIdentityProviderUpdateProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIdentityProviderUpdateProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIdentityProviderUpdateParameters)

#endif // OAIIdentityProviderUpdateParameters_H
