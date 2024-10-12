/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWorkflow.h
 *
 * 
 */

#ifndef OAIWorkflow_H
#define OAIWorkflow_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWorkflow : public OAIObject {
public:
    OAIWorkflow();
    OAIWorkflow(QString json);
    ~OAIWorkflow() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAction() const;
    void setAction(const QString &action);
    bool is_action_Set() const;
    bool is_action_Valid() const;

    bool isActive() const;
    void setActive(const bool &active);
    bool is_active_Set() const;
    bool is_active_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getCreatedBy() const;
    void setCreatedBy(const QString &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getInput() const;
    void setInput(const QString &input);
    bool is_input_Set() const;
    bool is_input_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOwner() const;
    void setOwner(const QString &owner);
    bool is_owner_Set() const;
    bool is_owner_Valid() const;

    QString getTrigger() const;
    void setTrigger(const QString &trigger);
    bool is_trigger_Set() const;
    bool is_trigger_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action;
    bool m_action_isSet;
    bool m_action_isValid;

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_input;
    bool m_input_isSet;
    bool m_input_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_owner;
    bool m_owner_isSet;
    bool m_owner_isValid;

    QString m_trigger;
    bool m_trigger_isSet;
    bool m_trigger_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWorkflow)

#endif // OAIWorkflow_H
