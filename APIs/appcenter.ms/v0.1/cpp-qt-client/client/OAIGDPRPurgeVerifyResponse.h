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
 * OAIGDPRPurgeVerifyResponse.h
 *
 * 
 */

#ifndef OAIGDPRPurgeVerifyResponse_H
#define OAIGDPRPurgeVerifyResponse_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGDPRPurgeVerifyResponse : public OAIObject {
public:
    OAIGDPRPurgeVerifyResponse();
    OAIGDPRPurgeVerifyResponse(QString json);
    ~OAIGDPRPurgeVerifyResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGDPRPurgeVerifyResponse)

#endif // OAIGDPRPurgeVerifyResponse_H
