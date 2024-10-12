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
 * OAIStore_data_website_interface.h
 *
 * Website interface
 */

#ifndef OAIStore_data_website_interface_H
#define OAIStore_data_website_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIStore_data_website_interface : public OAIObject {
public:
    OAIStore_data_website_interface();
    OAIStore_data_website_interface(QString json);
    ~OAIStore_data_website_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    qint32 getDefaultGroupId() const;
    void setDefaultGroupId(const qint32 &default_group_id);
    bool is_default_group_id_Set() const;
    bool is_default_group_id_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    qint32 m_default_group_id;
    bool m_default_group_id_isSet;
    bool m_default_group_id_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStore_data_website_interface)

#endif // OAIStore_data_website_interface_H
