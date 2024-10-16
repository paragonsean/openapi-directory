/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGenerateNetworkCameraSnapshot_request.h
 *
 * 
 */

#ifndef OAIGenerateNetworkCameraSnapshot_request_H
#define OAIGenerateNetworkCameraSnapshot_request_H

#include <QJsonObject>

#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGenerateNetworkCameraSnapshot_request : public OAIObject {
public:
    OAIGenerateNetworkCameraSnapshot_request();
    OAIGenerateNetworkCameraSnapshot_request(QString json);
    ~OAIGenerateNetworkCameraSnapshot_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isFullframe() const;
    void setFullframe(const bool &fullframe);
    bool is_fullframe_Set() const;
    bool is_fullframe_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_fullframe;
    bool m_fullframe_isSet;
    bool m_fullframe_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGenerateNetworkCameraSnapshot_request)

#endif // OAIGenerateNetworkCameraSnapshot_request_H
