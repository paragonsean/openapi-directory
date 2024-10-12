/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDiffDownloadResponse.h
 *
 * Backend response for a Diff download response. For details on the Scotty Diff protocol, visit http://go/scotty-diff-protocol.
 */

#ifndef OAIDiffDownloadResponse_H
#define OAIDiffDownloadResponse_H

#include <QJsonObject>

#include "OAICompositeMedia.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICompositeMedia;

class OAIDiffDownloadResponse : public OAIObject {
public:
    OAIDiffDownloadResponse();
    OAIDiffDownloadResponse(QString json);
    ~OAIDiffDownloadResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICompositeMedia getObjectLocation() const;
    void setObjectLocation(const OAICompositeMedia &object_location);
    bool is_object_location_Set() const;
    bool is_object_location_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICompositeMedia m_object_location;
    bool m_object_location_isSet;
    bool m_object_location_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDiffDownloadResponse)

#endif // OAIDiffDownloadResponse_H
