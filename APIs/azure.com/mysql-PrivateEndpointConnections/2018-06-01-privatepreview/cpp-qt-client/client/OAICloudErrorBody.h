/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01-privatepreview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICloudErrorBody.h
 *
 * An error response from the Batch service.
 */

#ifndef OAICloudErrorBody_H
#define OAICloudErrorBody_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICloudErrorBody : public OAIObject {
public:
    OAICloudErrorBody();
    OAICloudErrorBody(QString json);
    ~OAICloudErrorBody() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QList<OAICloudErrorBody> getDetails() const;
    void setDetails(const QList<OAICloudErrorBody> &details);
    bool is_details_Set() const;
    bool is_details_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getTarget() const;
    void setTarget(const QString &target);
    bool is_target_Set() const;
    bool is_target_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QList<OAICloudErrorBody> m_details;
    bool m_details_isSet;
    bool m_details_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_target;
    bool m_target_isSet;
    bool m_target_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICloudErrorBody)

#endif // OAICloudErrorBody_H
