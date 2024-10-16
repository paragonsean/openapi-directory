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
 * OAIIosAppExtensionInfo.h
 *
 * App extension information
 */

#ifndef OAIIosAppExtensionInfo_H
#define OAIIosAppExtensionInfo_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIosAppExtensionInfo : public OAIObject {
public:
    OAIIosAppExtensionInfo();
    OAIIosAppExtensionInfo(QString json);
    ~OAIIosAppExtensionInfo() override;

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

Q_DECLARE_METATYPE(OpenAPI::OAIIosAppExtensionInfo)

#endif // OAIIosAppExtensionInfo_H
