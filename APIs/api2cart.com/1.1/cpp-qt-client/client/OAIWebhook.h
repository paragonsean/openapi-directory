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
 * OAIWebhook.h
 *
 * 
 */

#ifndef OAIWebhook_H
#define OAIWebhook_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWebhook : public OAIObject {
public:
    OAIWebhook();
    OAIWebhook(QString json);
    ~OAIWebhook() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAction() const;
    void setAction(const QString &action);
    bool is_action_Set() const;
    bool is_action_Valid() const;

    bool isActive() const;
    void setActive(const bool &active);
    bool is_active_Set() const;
    bool is_active_Valid() const;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getCallback() const;
    void setCallback(const QString &callback);
    bool is_callback_Set() const;
    bool is_callback_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getEntity() const;
    void setEntity(const QString &entity);
    bool is_entity_Set() const;
    bool is_entity_Valid() const;

    QString getFields() const;
    void setFields(const QString &fields);
    bool is_fields_Set() const;
    bool is_fields_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    QString getStoreId() const;
    void setStoreId(const QString &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    QString getUpdatedAt() const;
    void setUpdatedAt(const QString &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action;
    bool m_action_isSet;
    bool m_action_isValid;

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_callback;
    bool m_callback_isSet;
    bool m_callback_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_entity;
    bool m_entity_isSet;
    bool m_entity_isValid;

    QString m_fields;
    bool m_fields_isSet;
    bool m_fields_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    QString m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    QString m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhook)

#endif // OAIWebhook_H
