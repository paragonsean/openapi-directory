/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAuthenticateOKBody.h
 *
 * AuthenticateOKBody authenticate o k body
 */

#ifndef OAIAuthenticateOKBody_H
#define OAIAuthenticateOKBody_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAuthenticateOKBody : public OAIObject {
public:
    OAIAuthenticateOKBody();
    OAIAuthenticateOKBody(QString json);
    ~OAIAuthenticateOKBody() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIdentityToken() const;
    void setIdentityToken(const QString &identity_token);
    bool is_identity_token_Set() const;
    bool is_identity_token_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_identity_token;
    bool m_identity_token_isSet;
    bool m_identity_token_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAuthenticateOKBody)

#endif // OAIAuthenticateOKBody_H
