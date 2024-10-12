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
 * OAISales_rule_data_rule_label_interface.h
 *
 * Interface RuleLabelInterface
 */

#ifndef OAISales_rule_data_rule_label_interface_H
#define OAISales_rule_data_rule_label_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISales_rule_data_rule_label_interface : public OAIObject {
public:
    OAISales_rule_data_rule_label_interface();
    OAISales_rule_data_rule_label_interface(QString json);
    ~OAISales_rule_data_rule_label_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getStoreId() const;
    void setStoreId(const qint32 &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    QString getStoreLabel() const;
    void setStoreLabel(const QString &store_label);
    bool is_store_label_Set() const;
    bool is_store_label_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    QString m_store_label;
    bool m_store_label_isSet;
    bool m_store_label_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISales_rule_data_rule_label_interface)

#endif // OAISales_rule_data_rule_label_interface_H
