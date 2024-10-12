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
 * OAIEndpoint_get_users_ID_synergies_data_inner_relationship.h
 *
 * 
 */

#ifndef OAIEndpoint_get_users_ID_synergies_data_inner_relationship_H
#define OAIEndpoint_get_users_ID_synergies_data_inner_relationship_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEndpoint_get_users_ID_synergies_data_inner_relationship : public OAIObject {
public:
    OAIEndpoint_get_users_ID_synergies_data_inner_relationship();
    OAIEndpoint_get_users_ID_synergies_data_inner_relationship(QString json);
    ~OAIEndpoint_get_users_ID_synergies_data_inner_relationship() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isExistingBubbledConversation() const;
    void setExistingBubbledConversation(const bool &existing_bubbled_conversation);
    bool is_existing_bubbled_conversation_Set() const;
    bool is_existing_bubbled_conversation_Valid() const;

    bool isExistingConversation() const;
    void setExistingConversation(const bool &existing_conversation);
    bool is_existing_conversation_Set() const;
    bool is_existing_conversation_Valid() const;

    bool isMuted() const;
    void setMuted(const bool &muted);
    bool is_muted_Set() const;
    bool is_muted_Valid() const;

    bool isSkipped() const;
    void setSkipped(const bool &skipped);
    bool is_skipped_Set() const;
    bool is_skipped_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_existing_bubbled_conversation;
    bool m_existing_bubbled_conversation_isSet;
    bool m_existing_bubbled_conversation_isValid;

    bool m_existing_conversation;
    bool m_existing_conversation_isSet;
    bool m_existing_conversation_isValid;

    bool m_muted;
    bool m_muted_isSet;
    bool m_muted_isValid;

    bool m_skipped;
    bool m_skipped_isSet;
    bool m_skipped_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpoint_get_users_ID_synergies_data_inner_relationship)

#endif // OAIEndpoint_get_users_ID_synergies_data_inner_relationship_H
