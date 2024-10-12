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
 * OAIAccountResource_relationships_transactions_links.h
 *
 * 
 */

#ifndef OAIAccountResource_relationships_transactions_links_H
#define OAIAccountResource_relationships_transactions_links_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccountResource_relationships_transactions_links : public OAIObject {
public:
    OAIAccountResource_relationships_transactions_links();
    OAIAccountResource_relationships_transactions_links(QString json);
    ~OAIAccountResource_relationships_transactions_links() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRelated() const;
    void setRelated(const QString &related);
    bool is_related_Set() const;
    bool is_related_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_related;
    bool m_related_isSet;
    bool m_related_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccountResource_relationships_transactions_links)

#endif // OAIAccountResource_relationships_transactions_links_H
