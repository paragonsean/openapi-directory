/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHidChangePasswordRequestPayload.h
 *
 * 
 */

#ifndef OAIHidChangePasswordRequestPayload_H
#define OAIHidChangePasswordRequestPayload_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIHidChangePasswordRequestPayload : public OAIObject {
public:
    OAIHidChangePasswordRequestPayload();
    OAIHidChangePasswordRequestPayload(QString json);
    ~OAIHidChangePasswordRequestPayload() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNewPassword() const;
    void setNewPassword(const QString &new_password);
    bool is_new_password_Set() const;
    bool is_new_password_Valid() const;

    QString getOldPassword() const;
    void setOldPassword(const QString &old_password);
    bool is_old_password_Set() const;
    bool is_old_password_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_new_password;
    bool m_new_password_isSet;
    bool m_new_password_isValid;

    QString m_old_password;
    bool m_old_password_isSet;
    bool m_old_password_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHidChangePasswordRequestPayload)

#endif // OAIHidChangePasswordRequestPayload_H
