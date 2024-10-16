/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICertificateRepresentation.h
 *
 * 
 */

#ifndef OAICertificateRepresentation_H
#define OAICertificateRepresentation_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICertificateRepresentation : public OAIObject {
public:
    OAICertificateRepresentation();
    OAICertificateRepresentation(QString json);
    ~OAICertificateRepresentation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCertificate() const;
    void setCertificate(const QString &certificate);
    bool is_certificate_Set() const;
    bool is_certificate_Valid() const;

    QString getKid() const;
    void setKid(const QString &kid);
    bool is_kid_Set() const;
    bool is_kid_Valid() const;

    QString getPrivateKey() const;
    void setPrivateKey(const QString &private_key);
    bool is_private_key_Set() const;
    bool is_private_key_Valid() const;

    QString getPublicKey() const;
    void setPublicKey(const QString &public_key);
    bool is_public_key_Set() const;
    bool is_public_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_certificate;
    bool m_certificate_isSet;
    bool m_certificate_isValid;

    QString m_kid;
    bool m_kid_isSet;
    bool m_kid_isValid;

    QString m_private_key;
    bool m_private_key_isSet;
    bool m_private_key_isValid;

    QString m_public_key;
    bool m_public_key_isSet;
    bool m_public_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICertificateRepresentation)

#endif // OAICertificateRepresentation_H
