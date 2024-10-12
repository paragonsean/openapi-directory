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
 * OAIEndpoint_post_messages_metadata_filters_data_inner.h
 *
 * 
 */

#ifndef OAIEndpoint_post_messages_metadata_filters_data_inner_H
#define OAIEndpoint_post_messages_metadata_filters_data_inner_H

#include <QJsonObject>

#include "OAIMessage.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMessage;

class OAIEndpoint_post_messages_metadata_filters_data_inner : public OAIObject {
public:
    OAIEndpoint_post_messages_metadata_filters_data_inner();
    OAIEndpoint_post_messages_metadata_filters_data_inner(QString json);
    ~OAIEndpoint_post_messages_metadata_filters_data_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QList<QString>> getMatchedMetadata() const;
    void setMatchedMetadata(const QMap<QString, QList<QString>> &matched_metadata);
    bool is_matched_metadata_Set() const;
    bool is_matched_metadata_Valid() const;

    OAIMessage getMessage() const;
    void setMessage(const OAIMessage &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QList<QString>> m_matched_metadata;
    bool m_matched_metadata_isSet;
    bool m_matched_metadata_isValid;

    OAIMessage m_message;
    bool m_message_isSet;
    bool m_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpoint_post_messages_metadata_filters_data_inner)

#endif // OAIEndpoint_post_messages_metadata_filters_data_inner_H
