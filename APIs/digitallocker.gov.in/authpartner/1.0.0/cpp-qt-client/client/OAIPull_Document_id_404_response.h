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
 * OAIPull_Document_id_404_response.h
 *
 * 
 */

#ifndef OAIPull_Document_id_404_response_H
#define OAIPull_Document_id_404_response_H

#include <QJsonObject>

#include <QJsonValue>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPull_Document_id_404_response : public OAIObject {
public:
    OAIPull_Document_id_404_response();
    OAIPull_Document_id_404_response(QString json);
    ~OAIPull_Document_id_404_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QJsonValue getError() const;
    void setError(const QJsonValue &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QJsonValue getErrorDescription() const;
    void setErrorDescription(const QJsonValue &error_description);
    bool is_error_description_Set() const;
    bool is_error_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QJsonValue m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QJsonValue m_error_description;
    bool m_error_description_isSet;
    bool m_error_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPull_Document_id_404_response)

#endif // OAIPull_Document_id_404_response_H
