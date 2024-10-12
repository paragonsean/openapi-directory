/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICatalog_data_category_interface.h
 *
 * 
 */

#ifndef OAICatalog_data_category_interface_H
#define OAICatalog_data_category_interface_H

#include <QJsonObject>

#include "OAIFramework_attribute_interface.h"
#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFramework_attribute_interface;

class OAICatalog_data_category_interface : public OAIObject {
public:
    OAICatalog_data_category_interface();
    OAICatalog_data_category_interface(QString json);
    ~OAICatalog_data_category_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAvailableSortBy() const;
    void setAvailableSortBy(const QList<QString> &available_sort_by);
    bool is_available_sort_by_Set() const;
    bool is_available_sort_by_Valid() const;

    QString getChildren() const;
    void setChildren(const QString &children);
    bool is_children_Set() const;
    bool is_children_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QList<OAIFramework_attribute_interface> getCustomAttributes() const;
    void setCustomAttributes(const QList<OAIFramework_attribute_interface> &custom_attributes);
    bool is_custom_attributes_Set() const;
    bool is_custom_attributes_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIncludeInMenu() const;
    void setIncludeInMenu(const bool &include_in_menu);
    bool is_include_in_menu_Set() const;
    bool is_include_in_menu_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    qint32 getLevel() const;
    void setLevel(const qint32 &level);
    bool is_level_Set() const;
    bool is_level_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getParentId() const;
    void setParentId(const qint32 &parent_id);
    bool is_parent_id_Set() const;
    bool is_parent_id_Valid() const;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    qint32 getPosition() const;
    void setPosition(const qint32 &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getUpdatedAt() const;
    void setUpdatedAt(const QString &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_available_sort_by;
    bool m_available_sort_by_isSet;
    bool m_available_sort_by_isValid;

    QString m_children;
    bool m_children_isSet;
    bool m_children_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QList<OAIFramework_attribute_interface> m_custom_attributes;
    bool m_custom_attributes_isSet;
    bool m_custom_attributes_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_include_in_menu;
    bool m_include_in_menu_isSet;
    bool m_include_in_menu_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    qint32 m_level;
    bool m_level_isSet;
    bool m_level_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_parent_id;
    bool m_parent_id_isSet;
    bool m_parent_id_isValid;

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    qint32 m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_category_interface)

#endif // OAICatalog_data_category_interface_H
