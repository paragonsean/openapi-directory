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
 * OAIDeployment.h
 *
 * Deployment operation parameters.
 */

#ifndef OAIDeployment_H
#define OAIDeployment_H

#include <QJsonObject>

#include "OAIDeploymentProperties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDeploymentProperties;

class OAIDeployment : public OAIObject {
public:
    OAIDeployment();
    OAIDeployment(QString json);
    ~OAIDeployment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIDeploymentProperties getProperties() const;
    void setProperties(const OAIDeploymentProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIDeploymentProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeployment)

#endif // OAIDeployment_H
