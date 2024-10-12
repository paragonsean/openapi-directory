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
 * OAIEndpoint_patch_users_ID_synergies_data.h
 *
 * 
 */

#ifndef OAIEndpoint_patch_users_ID_synergies_data_H
#define OAIEndpoint_patch_users_ID_synergies_data_H

#include <QJsonObject>

#include "OAIEndpoint_patch_users_ID_synergies_data_relationship.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEndpoint_patch_users_ID_synergies_data_relationship;

class OAIEndpoint_patch_users_ID_synergies_data : public OAIObject {
public:
    OAIEndpoint_patch_users_ID_synergies_data();
    OAIEndpoint_patch_users_ID_synergies_data(QString json);
    ~OAIEndpoint_patch_users_ID_synergies_data() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIEndpoint_patch_users_ID_synergies_data_relationship getRelationship() const;
    void setRelationship(const OAIEndpoint_patch_users_ID_synergies_data_relationship &relationship);
    bool is_relationship_Set() const;
    bool is_relationship_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIEndpoint_patch_users_ID_synergies_data_relationship m_relationship;
    bool m_relationship_isSet;
    bool m_relationship_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpoint_patch_users_ID_synergies_data)

#endif // OAIEndpoint_patch_users_ID_synergies_data_H
