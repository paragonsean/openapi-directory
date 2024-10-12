/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITotpSetupResponse.h
 *
 * Contains QR code URL and OTP URI for TOTP setup
 */

#ifndef OAITotpSetupResponse_H
#define OAITotpSetupResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITotpSetupResponse : public OAIObject {
public:
    OAITotpSetupResponse();
    OAITotpSetupResponse(QString json);
    ~OAITotpSetupResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getOtpUri() const;
    void setOtpUri(const QString &otp_uri);
    bool is_otp_uri_Set() const;
    bool is_otp_uri_Valid() const;

    QString getQrCode() const;
    void setQrCode(const QString &qr_code);
    bool is_qr_code_Set() const;
    bool is_qr_code_Valid() const;

    QString getSecret() const;
    void setSecret(const QString &secret);
    bool is_secret_Set() const;
    bool is_secret_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_otp_uri;
    bool m_otp_uri_isSet;
    bool m_otp_uri_isValid;

    QString m_qr_code;
    bool m_qr_code_isSet;
    bool m_qr_code_isValid;

    QString m_secret;
    bool m_secret_isSet;
    bool m_secret_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITotpSetupResponse)

#endif // OAITotpSetupResponse_H
