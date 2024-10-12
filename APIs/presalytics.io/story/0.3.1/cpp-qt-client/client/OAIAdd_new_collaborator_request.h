/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAdd_new_collaborator_request.h
 *
 * required subset of collaborator data to get a permission
 */

#ifndef OAIAdd_new_collaborator_request_H
#define OAIAdd_new_collaborator_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAdd_new_collaborator_request : public OAIObject {
public:
    OAIAdd_new_collaborator_request();
    OAIAdd_new_collaborator_request(QString json);
    ~OAIAdd_new_collaborator_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCollaboratorType() const;
    void setCollaboratorType(const QString &collaborator_type);
    bool is_collaborator_type_Set() const;
    bool is_collaborator_type_Valid() const;

    QString getUserEmail() const;
    void setUserEmail(const QString &user_email);
    bool is_user_email_Set() const;
    bool is_user_email_Valid() const;

    QString getUserId() const;
    void setUserId(const QString &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_collaborator_type;
    bool m_collaborator_type_isSet;
    bool m_collaborator_type_isValid;

    QString m_user_email;
    bool m_user_email_isSet;
    bool m_user_email_isValid;

    QString m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAdd_new_collaborator_request)

#endif // OAIAdd_new_collaborator_request_H
