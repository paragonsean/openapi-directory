/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPageResult_SupplierQueryDto_.h
 *
 * 
 */

#ifndef OAIPageResult_SupplierQueryDto__H
#define OAIPageResult_SupplierQueryDto__H

#include <QJsonObject>

#include "OAISupplierQueryDto.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISupplierQueryDto;

class OAIPageResult_SupplierQueryDto_ : public OAIObject {
public:
    OAIPageResult_SupplierQueryDto_();
    OAIPageResult_SupplierQueryDto_(QString json);
    ~OAIPageResult_SupplierQueryDto_() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCount() const;
    void setCount(const qint64 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    QList<OAISupplierQueryDto> getItems() const;
    void setItems(const QList<OAISupplierQueryDto> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    QString getNextPageLink() const;
    void setNextPageLink(const QString &next_page_link);
    bool is_next_page_link_Set() const;
    bool is_next_page_link_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    QList<OAISupplierQueryDto> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    QString m_next_page_link;
    bool m_next_page_link_isSet;
    bool m_next_page_link_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPageResult_SupplierQueryDto_)

#endif // OAIPageResult_SupplierQueryDto__H
