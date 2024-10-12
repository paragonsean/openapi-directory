/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProduct_Attribute.h
 *
 * 
 */

#ifndef OAIProduct_Attribute_H
#define OAIProduct_Attribute_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProduct_Attribute : public OAIObject {
public:
    OAIProduct_Attribute();
    OAIProduct_Attribute(QString json);
    ~OAIProduct_Attribute() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getAttributeGroupId() const;
    void setAttributeGroupId(const QString &attribute_group_id);
    bool is_attribute_group_id_Set() const;
    bool is_attribute_group_id_Valid() const;

    QString getAttributeId() const;
    void setAttributeId(const QString &attribute_id);
    bool is_attribute_id_Set() const;
    bool is_attribute_id_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getLangId() const;
    void setLangId(const QString &lang_id);
    bool is_lang_id_Set() const;
    bool is_lang_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPosition() const;
    void setPosition(const qint32 &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getProductId() const;
    void setProductId(const QString &product_id);
    bool is_product_id_Set() const;
    bool is_product_id_Valid() const;

    bool isRequired() const;
    void setRequired(const bool &required);
    bool is_required_Set() const;
    bool is_required_Valid() const;

    QString getStoreId() const;
    void setStoreId(const QString &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    QString getVariantId() const;
    void setVariantId(const QString &variant_id);
    bool is_variant_id_Set() const;
    bool is_variant_id_Valid() const;

    bool isVisible() const;
    void setVisible(const bool &visible);
    bool is_visible_Set() const;
    bool is_visible_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_attribute_group_id;
    bool m_attribute_group_id_isSet;
    bool m_attribute_group_id_isValid;

    QString m_attribute_id;
    bool m_attribute_id_isSet;
    bool m_attribute_id_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_lang_id;
    bool m_lang_id_isSet;
    bool m_lang_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_product_id;
    bool m_product_id_isSet;
    bool m_product_id_isValid;

    bool m_required;
    bool m_required_isSet;
    bool m_required_isValid;

    QString m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;

    QString m_variant_id;
    bool m_variant_id_isSet;
    bool m_variant_id_isValid;

    bool m_visible;
    bool m_visible_isSet;
    bool m_visible_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProduct_Attribute)

#endif // OAIProduct_Attribute_H
