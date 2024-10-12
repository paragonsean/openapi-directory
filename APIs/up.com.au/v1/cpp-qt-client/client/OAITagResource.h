/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITagResource.h
 *
 * Provides information about a tag. 
 */

#ifndef OAITagResource_H
#define OAITagResource_H

#include <QJsonObject>

#include "OAIAccountResource_relationships.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAccountResource_relationships;

class OAITagResource : public OAIObject {
public:
    OAITagResource();
    OAITagResource(QString json);
    ~OAITagResource() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIAccountResource_relationships getRelationships() const;
    void setRelationships(const OAIAccountResource_relationships &relationships);
    bool is_relationships_Set() const;
    bool is_relationships_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIAccountResource_relationships m_relationships;
    bool m_relationships_isSet;
    bool m_relationships_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITagResource)

#endif // OAITagResource_H
