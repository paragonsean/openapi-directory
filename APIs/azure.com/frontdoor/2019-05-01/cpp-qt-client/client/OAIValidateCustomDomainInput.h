/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIValidateCustomDomainInput.h
 *
 * Input of the custom domain to be validated for DNS mapping.
 */

#ifndef OAIValidateCustomDomainInput_H
#define OAIValidateCustomDomainInput_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIValidateCustomDomainInput : public OAIObject {
public:
    OAIValidateCustomDomainInput();
    OAIValidateCustomDomainInput(QString json);
    ~OAIValidateCustomDomainInput() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHostName() const;
    void setHostName(const QString &host_name);
    bool is_host_name_Set() const;
    bool is_host_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_host_name;
    bool m_host_name_isSet;
    bool m_host_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIValidateCustomDomainInput)

#endif // OAIValidateCustomDomainInput_H
