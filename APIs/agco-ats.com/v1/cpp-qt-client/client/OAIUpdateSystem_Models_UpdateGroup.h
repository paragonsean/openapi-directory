/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateSystem_Models_UpdateGroup.h
 *
 * 
 */

#ifndef OAIUpdateSystem_Models_UpdateGroup_H
#define OAIUpdateSystem_Models_UpdateGroup_H

#include <QJsonObject>

#include <QByteArray>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateSystem_Models_UpdateGroup : public OAIObject {
public:
    OAIUpdateSystem_Models_UpdateGroup();
    OAIUpdateSystem_Models_UpdateGroup(QString json);
    ~OAIUpdateSystem_Models_UpdateGroup() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getInventoryFrequency() const;
    void setInventoryFrequency(const qint32 &inventory_frequency);
    bool is_inventory_frequency_Set() const;
    bool is_inventory_frequency_Valid() const;

    QString getInventoryPackage() const;
    void setInventoryPackage(const QString &inventory_package);
    bool is_inventory_package_Set() const;
    bool is_inventory_package_Valid() const;

    QString getLocalizedDescription() const;
    void setLocalizedDescription(const QString &localized_description);
    bool is_localized_description_Set() const;
    bool is_localized_description_Valid() const;

    QString getLocalizedName() const;
    void setLocalizedName(const QString &localized_name);
    bool is_localized_name_Set() const;
    bool is_localized_name_Valid() const;

    qint32 getPriority() const;
    void setPriority(const qint32 &priority);
    bool is_priority_Set() const;
    bool is_priority_Valid() const;

    QString getReportField() const;
    void setReportField(const QString &report_field);
    bool is_report_field_Set() const;
    bool is_report_field_Valid() const;

    QString getUpdateType() const;
    void setUpdateType(const QString &update_type);
    bool is_update_type_Set() const;
    bool is_update_type_Valid() const;

    QString getValidatingField() const;
    void setValidatingField(const QString &validating_field);
    bool is_validating_field_Set() const;
    bool is_validating_field_Valid() const;

    QString getValueToValidate() const;
    void setValueToValidate(const QString &value_to_validate);
    bool is_value_to_validate_Set() const;
    bool is_value_to_validate_Valid() const;

    QByteArray getVersion() const;
    void setVersion(const QByteArray &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_inventory_frequency;
    bool m_inventory_frequency_isSet;
    bool m_inventory_frequency_isValid;

    QString m_inventory_package;
    bool m_inventory_package_isSet;
    bool m_inventory_package_isValid;

    QString m_localized_description;
    bool m_localized_description_isSet;
    bool m_localized_description_isValid;

    QString m_localized_name;
    bool m_localized_name_isSet;
    bool m_localized_name_isValid;

    qint32 m_priority;
    bool m_priority_isSet;
    bool m_priority_isValid;

    QString m_report_field;
    bool m_report_field_isSet;
    bool m_report_field_isValid;

    QString m_update_type;
    bool m_update_type_isSet;
    bool m_update_type_isValid;

    QString m_validating_field;
    bool m_validating_field_isSet;
    bool m_validating_field_isValid;

    QString m_value_to_validate;
    bool m_value_to_validate_isSet;
    bool m_value_to_validate_isValid;

    QByteArray m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateSystem_Models_UpdateGroup)

#endif // OAIUpdateSystem_Models_UpdateGroup_H
