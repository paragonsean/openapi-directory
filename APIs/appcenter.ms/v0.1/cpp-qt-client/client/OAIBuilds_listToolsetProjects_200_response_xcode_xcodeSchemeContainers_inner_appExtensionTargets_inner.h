/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner.h
 *
 * App extension information
 */

#ifndef OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner_H
#define OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner : public OAIObject {
public:
    OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner();
    OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner(QString json);
    ~OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getTargetBundleIdentifier() const;
    void setTargetBundleIdentifier(const QString &target_bundle_identifier);
    bool is_target_bundle_identifier_Set() const;
    bool is_target_bundle_identifier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_target_bundle_identifier;
    bool m_target_bundle_identifier_isSet;
    bool m_target_bundle_identifier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner)

#endif // OAIBuilds_listToolsetProjects_200_response_xcode_xcodeSchemeContainers_inner_appExtensionTargets_inner_H
