/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIdentityProviderContract.h
 *
 * Identity Provider details.
 */

#ifndef OAIIdentityProviderContract_H
#define OAIIdentityProviderContract_H

#include <QJsonObject>

#include "OAIIdentityProviderContractProperties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIdentityProviderContractProperties;

class OAIIdentityProviderContract : public OAIObject {
public:
    OAIIdentityProviderContract();
    OAIIdentityProviderContract(QString json);
    ~OAIIdentityProviderContract() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIdentityProviderContractProperties getProperties() const;
    void setProperties(const OAIIdentityProviderContractProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIdentityProviderContractProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIdentityProviderContract)

#endif // OAIIdentityProviderContract_H
