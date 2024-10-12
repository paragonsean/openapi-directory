/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetaccesstoken_id_request.h
 *
 * 
 */

#ifndef OAIGetaccesstoken_id_request_H
#define OAIGetaccesstoken_id_request_H

#include <QJsonObject>

#include "OAIAccessToken.h"
#include "OAIDeviceAccessToken.h"
#include "OAIRefreshToken.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAccessToken;
class OAIDeviceAccessToken;
class OAIRefreshToken;

class OAIGetaccesstoken_id_request : public OAIObject {
public:
    OAIGetaccesstoken_id_request();
    OAIGetaccesstoken_id_request(QString json);
    ~OAIGetaccesstoken_id_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAccessToken getGetAccessTokenUsingAuthorizationCode() const;
    void setGetAccessTokenUsingAuthorizationCode(const OAIAccessToken &get_access_token_using_authorization_code);
    bool is_get_access_token_using_authorization_code_Set() const;
    bool is_get_access_token_using_authorization_code_Valid() const;

    OAIDeviceAccessToken getGetAccessTokenUsingDeviceCodeAndOtp() const;
    void setGetAccessTokenUsingDeviceCodeAndOtp(const OAIDeviceAccessToken &get_access_token_using_device_code_and_otp);
    bool is_get_access_token_using_device_code_and_otp_Set() const;
    bool is_get_access_token_using_device_code_and_otp_Valid() const;

    OAIRefreshToken getGetAccessTokenUsingRefreshToken() const;
    void setGetAccessTokenUsingRefreshToken(const OAIRefreshToken &get_access_token_using_refresh_token);
    bool is_get_access_token_using_refresh_token_Set() const;
    bool is_get_access_token_using_refresh_token_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAccessToken m_get_access_token_using_authorization_code;
    bool m_get_access_token_using_authorization_code_isSet;
    bool m_get_access_token_using_authorization_code_isValid;

    OAIDeviceAccessToken m_get_access_token_using_device_code_and_otp;
    bool m_get_access_token_using_device_code_and_otp_isSet;
    bool m_get_access_token_using_device_code_and_otp_isValid;

    OAIRefreshToken m_get_access_token_using_refresh_token;
    bool m_get_access_token_using_refresh_token_isSet;
    bool m_get_access_token_using_refresh_token_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetaccesstoken_id_request)

#endif // OAIGetaccesstoken_id_request_H
