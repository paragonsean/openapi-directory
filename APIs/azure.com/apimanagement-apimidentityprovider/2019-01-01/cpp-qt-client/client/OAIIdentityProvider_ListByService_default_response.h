/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIdentityProvider_ListByService_default_response.h
 *
 * Error Response.
 */

#ifndef OAIIdentityProvider_ListByService_default_response_H
#define OAIIdentityProvider_ListByService_default_response_H

#include <QJsonObject>

#include "OAIIdentityProvider_ListByService_default_response_error.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIdentityProvider_ListByService_default_response_error;

class OAIIdentityProvider_ListByService_default_response : public OAIObject {
public:
    OAIIdentityProvider_ListByService_default_response();
    OAIIdentityProvider_ListByService_default_response(QString json);
    ~OAIIdentityProvider_ListByService_default_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIdentityProvider_ListByService_default_response_error getError() const;
    void setError(const OAIIdentityProvider_ListByService_default_response_error &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIdentityProvider_ListByService_default_response_error m_error;
    bool m_error_isSet;
    bool m_error_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIdentityProvider_ListByService_default_response)

#endif // OAIIdentityProvider_ListByService_default_response_H
