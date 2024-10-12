/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApplicationProperties.h
 *
 * The properties associated with the Application.
 */

#ifndef OAIApplicationProperties_H
#define OAIApplicationProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApplicationProperties : public OAIObject {
public:
    OAIApplicationProperties();
    OAIApplicationProperties(QString json);
    ~OAIApplicationProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowUpdates() const;
    void setAllowUpdates(const bool &allow_updates);
    bool is_allow_updates_Set() const;
    bool is_allow_updates_Valid() const;

    QString getDefaultVersion() const;
    void setDefaultVersion(const QString &default_version);
    bool is_default_version_Set() const;
    bool is_default_version_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_updates;
    bool m_allow_updates_isSet;
    bool m_allow_updates_isValid;

    QString m_default_version;
    bool m_default_version_isSet;
    bool m_default_version_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties)

#endif // OAIApplicationProperties_H
