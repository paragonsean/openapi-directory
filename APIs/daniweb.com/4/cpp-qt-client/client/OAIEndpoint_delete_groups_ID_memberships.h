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
 * OAIEndpoint_delete_groups_ID_memberships.h
 *
 * 
 */

#ifndef OAIEndpoint_delete_groups_ID_memberships_H
#define OAIEndpoint_delete_groups_ID_memberships_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEndpoint_delete_groups_ID_memberships : public OAIObject {
public:
    OAIEndpoint_delete_groups_ID_memberships();
    OAIEndpoint_delete_groups_ID_memberships(QString json);
    ~OAIEndpoint_delete_groups_ID_memberships() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpoint_delete_groups_ID_memberships)

#endif // OAIEndpoint_delete_groups_ID_memberships_H
