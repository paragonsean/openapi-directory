/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBuildUpdateParameters.h
 *
 * The set of build properties that can be updated.
 */

#ifndef OAIBuildUpdateParameters_H
#define OAIBuildUpdateParameters_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBuildUpdateParameters : public OAIObject {
public:
    OAIBuildUpdateParameters();
    OAIBuildUpdateParameters(QString json);
    ~OAIBuildUpdateParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsArchiveEnabled() const;
    void setIsArchiveEnabled(const bool &is_archive_enabled);
    bool is_is_archive_enabled_Set() const;
    bool is_is_archive_enabled_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_archive_enabled;
    bool m_is_archive_enabled_isSet;
    bool m_is_archive_enabled_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuildUpdateParameters)

#endif // OAIBuildUpdateParameters_H
