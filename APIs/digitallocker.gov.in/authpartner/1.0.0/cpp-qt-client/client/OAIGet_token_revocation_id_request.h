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
 * OAIGet_token_revocation_id_request.h
 *
 * 
 */

#ifndef OAIGet_token_revocation_id_request_H
#define OAIGet_token_revocation_id_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGet_token_revocation_id_request : public OAIObject {
public:
    OAIGet_token_revocation_id_request();
    OAIGet_token_revocation_id_request(QString json);
    ~OAIGet_token_revocation_id_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getToken() const;
    void setToken(const QString &token);
    bool is_token_Set() const;
    bool is_token_Valid() const;

    QString getTokenTypeHint() const;
    void setTokenTypeHint(const QString &token_type_hint);
    bool is_token_type_hint_Set() const;
    bool is_token_type_hint_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_token;
    bool m_token_isSet;
    bool m_token_isValid;

    QString m_token_type_hint;
    bool m_token_type_hint_isSet;
    bool m_token_type_hint_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGet_token_revocation_id_request)

#endif // OAIGet_token_revocation_id_request_H
