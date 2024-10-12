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
 * OAIPlatformUpdateParameters.h
 *
 * The properties for updating the platform configuration.
 */

#ifndef OAIPlatformUpdateParameters_H
#define OAIPlatformUpdateParameters_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlatformUpdateParameters : public OAIObject {
public:
    OAIPlatformUpdateParameters();
    OAIPlatformUpdateParameters(QString json);
    ~OAIPlatformUpdateParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArchitecture() const;
    void setArchitecture(const QString &architecture);
    bool is_architecture_Set() const;
    bool is_architecture_Valid() const;

    QString getOs() const;
    void setOs(const QString &os);
    bool is_os_Set() const;
    bool is_os_Valid() const;

    QString getVariant() const;
    void setVariant(const QString &variant);
    bool is_variant_Set() const;
    bool is_variant_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_architecture;
    bool m_architecture_isSet;
    bool m_architecture_isValid;

    QString m_os;
    bool m_os_isSet;
    bool m_os_isValid;

    QString m_variant;
    bool m_variant_isSet;
    bool m_variant_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlatformUpdateParameters)

#endif // OAIPlatformUpdateParameters_H
