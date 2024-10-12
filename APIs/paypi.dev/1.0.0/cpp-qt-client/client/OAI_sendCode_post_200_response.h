/**
 * EmailVerify
 * OTP email verification API by PayPI. <br/><br/> EmailVerify provides a simple way to verify email addresses. We send emails ourselves taking the burden of setting up email systems and tracking codes. <br/><br/> To learn more about this API, check out [EmailVerify documentation](https://emailverify.paypi.dev/) <br/><br/>  ## Authentication All requests to the EmailVerify API must be authenticated with an API Key. To get an API key, subscribe to the EmailVerify [here](https://app.paypi.dev/subscribe/c2VydmljZTo1OGQxZDNmMy05OWQ5LTQ3ZjYtOWJkNi02OWNkMTY1OGFmOWU=).  \\ Set your `Authorization` header to `Bearer YOUR-API-KEY`.  ``` curl -H \"Content-Type: application/json\" \\ -H \"Authorization: Bearer YOUR-API-KEY\" \\ ... ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hello@paypi.dev
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_sendCode_post_200_response.h
 *
 * 
 */

#ifndef OAI_sendCode_post_200_response_H
#define OAI_sendCode_post_200_response_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_sendCode_post_200_response : public OAIObject {
public:
    OAI_sendCode_post_200_response();
    OAI_sendCode_post_200_response(QString json);
    ~OAI_sendCode_post_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isMessage() const;
    void setMessage(const bool &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_sendCode_post_200_response)

#endif // OAI_sendCode_post_200_response_H
