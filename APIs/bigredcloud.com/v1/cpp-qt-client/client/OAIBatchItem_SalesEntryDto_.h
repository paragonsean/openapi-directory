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
 * OAIBatchItem_SalesEntryDto_.h
 *
 * 
 */

#ifndef OAIBatchItem_SalesEntryDto__H
#define OAIBatchItem_SalesEntryDto__H

#include <QJsonObject>

#include "OAISalesEntryDto.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISalesEntryDto;

class OAIBatchItem_SalesEntryDto_ : public OAIObject {
public:
    OAIBatchItem_SalesEntryDto_();
    OAIBatchItem_SalesEntryDto_(QString json);
    ~OAIBatchItem_SalesEntryDto_() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISalesEntryDto getItem() const;
    void setItem(const OAISalesEntryDto &item);
    bool is_item_Set() const;
    bool is_item_Valid() const;

    qint32 getOpCode() const;
    void setOpCode(const qint32 &op_code);
    bool is_op_code_Set() const;
    bool is_op_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISalesEntryDto m_item;
    bool m_item_isSet;
    bool m_item_isValid;

    qint32 m_op_code;
    bool m_op_code_isSet;
    bool m_op_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBatchItem_SalesEntryDto_)

#endif // OAIBatchItem_SalesEntryDto__H
