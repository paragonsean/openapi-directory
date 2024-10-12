/**
 * ManagementLockClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIManagementLockProperties.h
 *
 * The management lock properties.
 */

#ifndef OAIManagementLockProperties_H
#define OAIManagementLockProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIManagementLockProperties : public OAIObject {
public:
    OAIManagementLockProperties();
    OAIManagementLockProperties(QString json);
    ~OAIManagementLockProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLevel() const;
    void setLevel(const QString &level);
    bool is_level_Set() const;
    bool is_level_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_level;
    bool m_level_isSet;
    bool m_level_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIManagementLockProperties)

#endif // OAIManagementLockProperties_H
