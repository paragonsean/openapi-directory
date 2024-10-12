/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOfferClassAddMessageResponse.h
 *
 * 
 */

#ifndef OAIOfferClassAddMessageResponse_H
#define OAIOfferClassAddMessageResponse_H

#include <QJsonObject>

#include "OAIOfferClass.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOfferClass;

class OAIOfferClassAddMessageResponse : public OAIObject {
public:
    OAIOfferClassAddMessageResponse();
    OAIOfferClassAddMessageResponse(QString json);
    ~OAIOfferClassAddMessageResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIOfferClass getResource() const;
    void setResource(const OAIOfferClass &resource);
    bool is_resource_Set() const;
    bool is_resource_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIOfferClass m_resource;
    bool m_resource_isSet;
    bool m_resource_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOfferClassAddMessageResponse)

#endif // OAIOfferClassAddMessageResponse_H
