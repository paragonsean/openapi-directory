/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWebhookActivityEntry.h
 *
 * 
 */

#ifndef OAIWebhookActivityEntry_H
#define OAIWebhookActivityEntry_H

#include <QJsonObject>

#include "OAIWebhookActivityEntry_attributes.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhookActivityEntry_attributes;

class OAIWebhookActivityEntry : public OAIObject {
public:
    OAIWebhookActivityEntry();
    OAIWebhookActivityEntry(QString json);
    ~OAIWebhookActivityEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWebhookActivityEntry_attributes getAttributes() const;
    void setAttributes(const OAIWebhookActivityEntry_attributes &attributes);
    bool is_attributes_Set() const;
    bool is_attributes_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWebhookActivityEntry_attributes m_attributes;
    bool m_attributes_isSet;
    bool m_attributes_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhookActivityEntry)

#endif // OAIWebhookActivityEntry_H
