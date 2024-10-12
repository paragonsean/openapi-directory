/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomRegistryCredentials.h
 *
 * Describes the credentials that will be used to access a custom registry during a run.
 */

#ifndef OAICustomRegistryCredentials_H
#define OAICustomRegistryCredentials_H

#include <QJsonObject>

#include "OAISecretObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISecretObject;

class OAICustomRegistryCredentials : public OAIObject {
public:
    OAICustomRegistryCredentials();
    OAICustomRegistryCredentials(QString json);
    ~OAICustomRegistryCredentials() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISecretObject getPassword() const;
    void setPassword(const OAISecretObject &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    OAISecretObject getUserName() const;
    void setUserName(const OAISecretObject &user_name);
    bool is_user_name_Set() const;
    bool is_user_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISecretObject m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    OAISecretObject m_user_name;
    bool m_user_name_isSet;
    bool m_user_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomRegistryCredentials)

#endif // OAICustomRegistryCredentials_H
