/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHTTPValidationError.h
 *
 * 
 */

#ifndef OAIHTTPValidationError_H
#define OAIHTTPValidationError_H

#include <QJsonObject>

#include "OAIValidationError.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIValidationError;

class OAIHTTPValidationError : public OAIObject {
public:
    OAIHTTPValidationError();
    OAIHTTPValidationError(QString json);
    ~OAIHTTPValidationError() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIValidationError> getDetail() const;
    void setDetail(const QList<OAIValidationError> &detail);
    bool is_detail_Set() const;
    bool is_detail_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIValidationError> m_detail;
    bool m_detail_isSet;
    bool m_detail_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHTTPValidationError)

#endif // OAIHTTPValidationError_H
