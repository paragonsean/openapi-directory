/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAvailabilityOfDevicesResponse.h
 *
 * The current device availability (registered, available and maxmimum) for iPhones, iPads, iPods and Watches from Apple Developer Portal
 */

#ifndef OAIAvailabilityOfDevicesResponse_H
#define OAIAvailabilityOfDevicesResponse_H

#include <QJsonObject>

#include "OAIAvailabilityOfDevicesResponse_ipads.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAvailabilityOfDevicesResponse_ipads;

class OAIAvailabilityOfDevicesResponse : public OAIObject {
public:
    OAIAvailabilityOfDevicesResponse();
    OAIAvailabilityOfDevicesResponse(QString json);
    ~OAIAvailabilityOfDevicesResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAvailabilityOfDevicesResponse_ipads getIpads() const;
    void setIpads(const OAIAvailabilityOfDevicesResponse_ipads &ipads);
    bool is_ipads_Set() const;
    bool is_ipads_Valid() const;

    OAIAvailabilityOfDevicesResponse_ipads getIphones() const;
    void setIphones(const OAIAvailabilityOfDevicesResponse_ipads &iphones);
    bool is_iphones_Set() const;
    bool is_iphones_Valid() const;

    OAIAvailabilityOfDevicesResponse_ipads getIpods() const;
    void setIpods(const OAIAvailabilityOfDevicesResponse_ipads &ipods);
    bool is_ipods_Set() const;
    bool is_ipods_Valid() const;

    OAIAvailabilityOfDevicesResponse_ipads getWatches() const;
    void setWatches(const OAIAvailabilityOfDevicesResponse_ipads &watches);
    bool is_watches_Set() const;
    bool is_watches_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAvailabilityOfDevicesResponse_ipads m_ipads;
    bool m_ipads_isSet;
    bool m_ipads_isValid;

    OAIAvailabilityOfDevicesResponse_ipads m_iphones;
    bool m_iphones_isSet;
    bool m_iphones_isValid;

    OAIAvailabilityOfDevicesResponse_ipads m_ipods;
    bool m_ipods_isSet;
    bool m_ipods_isValid;

    OAIAvailabilityOfDevicesResponse_ipads m_watches;
    bool m_watches_isSet;
    bool m_watches_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAvailabilityOfDevicesResponse)

#endif // OAIAvailabilityOfDevicesResponse_H
