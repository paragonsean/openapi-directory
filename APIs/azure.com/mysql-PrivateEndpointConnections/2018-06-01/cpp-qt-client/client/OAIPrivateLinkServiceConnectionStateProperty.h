/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPrivateLinkServiceConnectionStateProperty.h
 *
 * 
 */

#ifndef OAIPrivateLinkServiceConnectionStateProperty_H
#define OAIPrivateLinkServiceConnectionStateProperty_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPrivateLinkServiceConnectionStateProperty : public OAIObject {
public:
    OAIPrivateLinkServiceConnectionStateProperty();
    OAIPrivateLinkServiceConnectionStateProperty(QString json);
    ~OAIPrivateLinkServiceConnectionStateProperty() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getActionsRequired() const;
    void setActionsRequired(const QString &actions_required);
    bool is_actions_required_Set() const;
    bool is_actions_required_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_actions_required;
    bool m_actions_required_isSet;
    bool m_actions_required_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPrivateLinkServiceConnectionStateProperty)

#endif // OAIPrivateLinkServiceConnectionStateProperty_H
