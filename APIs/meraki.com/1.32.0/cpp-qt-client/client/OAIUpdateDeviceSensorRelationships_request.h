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
 * OAIUpdateDeviceSensorRelationships_request.h
 *
 * 
 */

#ifndef OAIUpdateDeviceSensorRelationships_request_H
#define OAIUpdateDeviceSensorRelationships_request_H

#include <QJsonObject>

#include "OAIUpdateDeviceSensorRelationships_request_livestream.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateDeviceSensorRelationships_request_livestream;

class OAIUpdateDeviceSensorRelationships_request : public OAIObject {
public:
    OAIUpdateDeviceSensorRelationships_request();
    OAIUpdateDeviceSensorRelationships_request(QString json);
    ~OAIUpdateDeviceSensorRelationships_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIUpdateDeviceSensorRelationships_request_livestream getLivestream() const;
    void setLivestream(const OAIUpdateDeviceSensorRelationships_request_livestream &livestream);
    bool is_livestream_Set() const;
    bool is_livestream_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIUpdateDeviceSensorRelationships_request_livestream m_livestream;
    bool m_livestream_isSet;
    bool m_livestream_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateDeviceSensorRelationships_request)

#endif // OAIUpdateDeviceSensorRelationships_request_H
