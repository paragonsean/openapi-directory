/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIContactCustomFieldSchema.h
 *
 * 
 */

#ifndef OAIContactCustomFieldSchema_H
#define OAIContactCustomFieldSchema_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIContactCustomFieldSchema : public OAIObject {
public:
    OAIContactCustomFieldSchema();
    OAIContactCustomFieldSchema(QString json);
    ~OAIContactCustomFieldSchema() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    bool isRequired() const;
    void setRequired(const bool &required);
    bool is_required_Set() const;
    bool is_required_Valid() const;

    qint32 getType() const;
    void setType(const qint32 &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    bool m_required;
    bool m_required_isSet;
    bool m_required_isValid;

    qint32 m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContactCustomFieldSchema)

#endif // OAIContactCustomFieldSchema_H
