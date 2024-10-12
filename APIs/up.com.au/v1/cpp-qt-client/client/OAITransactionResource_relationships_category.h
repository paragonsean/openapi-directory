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
 * OAITransactionResource_relationships_category.h
 *
 * 
 */

#ifndef OAITransactionResource_relationships_category_H
#define OAITransactionResource_relationships_category_H

#include <QJsonObject>

#include "OAICategoryResource_relationships_parent_data.h"
#include "OAITransactionResource_relationships_category_links.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICategoryResource_relationships_parent_data;
class OAITransactionResource_relationships_category_links;

class OAITransactionResource_relationships_category : public OAIObject {
public:
    OAITransactionResource_relationships_category();
    OAITransactionResource_relationships_category(QString json);
    ~OAITransactionResource_relationships_category() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICategoryResource_relationships_parent_data getData() const;
    void setData(const OAICategoryResource_relationships_parent_data &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    OAITransactionResource_relationships_category_links getLinks() const;
    void setLinks(const OAITransactionResource_relationships_category_links &links);
    bool is_links_Set() const;
    bool is_links_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICategoryResource_relationships_parent_data m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAITransactionResource_relationships_category_links m_links;
    bool m_links_isSet;
    bool m_links_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITransactionResource_relationships_category)

#endif // OAITransactionResource_relationships_category_H
