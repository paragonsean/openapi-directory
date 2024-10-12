/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOperationStatus.h
 *
 * Operation status object. Operation refers to the asynchronous backend task including taking a snapshot and applying a snapshot.
 */

#ifndef OAIOperationStatus_H
#define OAIOperationStatus_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOperationStatus : public OAIObject {
public:
    OAIOperationStatus();
    OAIOperationStatus(QString json);
    ~OAIOperationStatus() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QDateTime getLastActionTime() const;
    void setLastActionTime(const QDateTime &last_action_time);
    bool is_last_action_time_Set() const;
    bool is_last_action_time_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getResourceLocation() const;
    void setResourceLocation(const QString &resource_location);
    bool is_resource_location_Set() const;
    bool is_resource_location_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QDateTime m_last_action_time;
    bool m_last_action_time_isSet;
    bool m_last_action_time_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_resource_location;
    bool m_resource_location_isSet;
    bool m_resource_location_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOperationStatus)

#endif // OAIOperationStatus_H
