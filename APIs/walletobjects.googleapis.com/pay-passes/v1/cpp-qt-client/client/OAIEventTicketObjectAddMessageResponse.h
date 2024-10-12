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
 * OAIEventTicketObjectAddMessageResponse.h
 *
 * 
 */

#ifndef OAIEventTicketObjectAddMessageResponse_H
#define OAIEventTicketObjectAddMessageResponse_H

#include <QJsonObject>

#include "OAIEventTicketObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEventTicketObject;

class OAIEventTicketObjectAddMessageResponse : public OAIObject {
public:
    OAIEventTicketObjectAddMessageResponse();
    OAIEventTicketObjectAddMessageResponse(QString json);
    ~OAIEventTicketObjectAddMessageResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIEventTicketObject getResource() const;
    void setResource(const OAIEventTicketObject &resource);
    bool is_resource_Set() const;
    bool is_resource_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIEventTicketObject m_resource;
    bool m_resource_isSet;
    bool m_resource_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEventTicketObjectAddMessageResponse)

#endif // OAIEventTicketObjectAddMessageResponse_H
