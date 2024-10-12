/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFileUploadResponse.h
 *
 * 
 */

#ifndef OAIFileUploadResponse_H
#define OAIFileUploadResponse_H

#include <QJsonObject>

#include "OAIFileUploadResponse_details.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFileUploadResponse_details;

class OAIFileUploadResponse : public OAIObject {
public:
    OAIFileUploadResponse();
    OAIFileUploadResponse(QString json);
    ~OAIFileUploadResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIFileUploadResponse_details getDetails() const;
    void setDetails(const OAIFileUploadResponse_details &details);
    bool is_details_Set() const;
    bool is_details_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIFileUploadResponse_details m_details;
    bool m_details_isSet;
    bool m_details_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFileUploadResponse)

#endif // OAIFileUploadResponse_H
