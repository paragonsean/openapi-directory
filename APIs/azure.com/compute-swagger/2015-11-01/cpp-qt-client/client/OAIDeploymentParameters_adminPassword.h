/**
 * ComputeManagementConvenienceClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDeploymentParameters_adminPassword.h
 *
 * 
 */

#ifndef OAIDeploymentParameters_adminPassword_H
#define OAIDeploymentParameters_adminPassword_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDeploymentParameters_adminPassword : public OAIObject {
public:
    OAIDeploymentParameters_adminPassword();
    OAIDeploymentParameters_adminPassword(QString json);
    ~OAIDeploymentParameters_adminPassword() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeploymentParameters_adminPassword)

#endif // OAIDeploymentParameters_adminPassword_H
