/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICheckinNetworkSmDevices_200_response.h
 *
 * 
 */

#ifndef OAICheckinNetworkSmDevices_200_response_H
#define OAICheckinNetworkSmDevices_200_response_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICheckinNetworkSmDevices_200_response : public OAIObject {
public:
    OAICheckinNetworkSmDevices_200_response();
    OAICheckinNetworkSmDevices_200_response(QString json);
    ~OAICheckinNetworkSmDevices_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getIds() const;
    void setIds(const QList<QString> &ids);
    bool is_ids_Set() const;
    bool is_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_ids;
    bool m_ids_isSet;
    bool m_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICheckinNetworkSmDevices_200_response)

#endif // OAICheckinNetworkSmDevices_200_response_H
