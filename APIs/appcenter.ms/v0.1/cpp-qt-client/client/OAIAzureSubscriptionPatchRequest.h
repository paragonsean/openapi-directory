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
 * OAIAzureSubscriptionPatchRequest.h
 *
 * 
 */

#ifndef OAIAzureSubscriptionPatchRequest_H
#define OAIAzureSubscriptionPatchRequest_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAzureSubscriptionPatchRequest : public OAIObject {
public:
    OAIAzureSubscriptionPatchRequest();
    OAIAzureSubscriptionPatchRequest(QString json);
    ~OAIAzureSubscriptionPatchRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsBilling() const;
    void setIsBilling(const bool &is_billing);
    bool is_is_billing_Set() const;
    bool is_is_billing_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_billing;
    bool m_is_billing_isSet;
    bool m_is_billing_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAzureSubscriptionPatchRequest)

#endif // OAIAzureSubscriptionPatchRequest_H
