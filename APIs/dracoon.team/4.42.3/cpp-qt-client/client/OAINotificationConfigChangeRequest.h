/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINotificationConfigChangeRequest.h
 *
 * Request model for updating notification configuration
 */

#ifndef OAINotificationConfigChangeRequest_H
#define OAINotificationConfigChangeRequest_H

#include <QJsonObject>

#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINotificationConfigChangeRequest : public OAIObject {
public:
    OAINotificationConfigChangeRequest();
    OAINotificationConfigChangeRequest(QString json);
    ~OAINotificationConfigChangeRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<qint32> getChannelIds() const;
    void setChannelIds(const QList<qint32> &channel_ids);
    bool is_channel_ids_Set() const;
    bool is_channel_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<qint32> m_channel_ids;
    bool m_channel_ids_isSet;
    bool m_channel_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotificationConfigChangeRequest)

#endif // OAINotificationConfigChangeRequest_H
