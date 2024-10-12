/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEndpoint_get_groups_messages_ID_metadata.h
 *
 * 
 */

#ifndef OAIEndpoint_get_groups_messages_ID_metadata_H
#define OAIEndpoint_get_groups_messages_ID_metadata_H

#include <QJsonObject>

#include "OAIApi_pagination.h"
#include "OAIGroup_message_data.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGroup_message_data;
class OAIApi_pagination;

class OAIEndpoint_get_groups_messages_ID_metadata : public OAIObject {
public:
    OAIEndpoint_get_groups_messages_ID_metadata();
    OAIEndpoint_get_groups_messages_ID_metadata(QString json);
    ~OAIEndpoint_get_groups_messages_ID_metadata() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIGroup_message_data> getData() const;
    void setData(const QList<OAIGroup_message_data> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    OAIApi_pagination getPagination() const;
    void setPagination(const OAIApi_pagination &pagination);
    bool is_pagination_Set() const;
    bool is_pagination_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIGroup_message_data> m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAIApi_pagination m_pagination;
    bool m_pagination_isSet;
    bool m_pagination_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpoint_get_groups_messages_ID_metadata)

#endif // OAIEndpoint_get_groups_messages_ID_metadata_H
