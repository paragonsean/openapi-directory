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
 * OAISalesRefundOrderV1ExecutePost_request.h
 *
 * 
 */

#ifndef OAISalesRefundOrderV1ExecutePost_request_H
#define OAISalesRefundOrderV1ExecutePost_request_H

#include <QJsonObject>

#include "OAISales_data_creditmemo_comment_creation_interface.h"
#include "OAISales_data_creditmemo_creation_arguments_interface.h"
#include "OAISales_data_creditmemo_item_creation_interface.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISales_data_creditmemo_creation_arguments_interface;
class OAISales_data_creditmemo_comment_creation_interface;
class OAISales_data_creditmemo_item_creation_interface;

class OAISalesRefundOrderV1ExecutePost_request : public OAIObject {
public:
    OAISalesRefundOrderV1ExecutePost_request();
    OAISalesRefundOrderV1ExecutePost_request(QString json);
    ~OAISalesRefundOrderV1ExecutePost_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAppendComment() const;
    void setAppendComment(const bool &append_comment);
    bool is_append_comment_Set() const;
    bool is_append_comment_Valid() const;

    OAISales_data_creditmemo_creation_arguments_interface getArguments() const;
    void setArguments(const OAISales_data_creditmemo_creation_arguments_interface &arguments);
    bool is_arguments_Set() const;
    bool is_arguments_Valid() const;

    OAISales_data_creditmemo_comment_creation_interface getComment() const;
    void setComment(const OAISales_data_creditmemo_comment_creation_interface &comment);
    bool is_comment_Set() const;
    bool is_comment_Valid() const;

    QList<OAISales_data_creditmemo_item_creation_interface> getItems() const;
    void setItems(const QList<OAISales_data_creditmemo_item_creation_interface> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    bool isNotify() const;
    void setNotify(const bool &notify);
    bool is_notify_Set() const;
    bool is_notify_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_append_comment;
    bool m_append_comment_isSet;
    bool m_append_comment_isValid;

    OAISales_data_creditmemo_creation_arguments_interface m_arguments;
    bool m_arguments_isSet;
    bool m_arguments_isValid;

    OAISales_data_creditmemo_comment_creation_interface m_comment;
    bool m_comment_isSet;
    bool m_comment_isValid;

    QList<OAISales_data_creditmemo_item_creation_interface> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    bool m_notify;
    bool m_notify_isSet;
    bool m_notify_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISalesRefundOrderV1ExecutePost_request)

#endif // OAISalesRefundOrderV1ExecutePost_request_H
