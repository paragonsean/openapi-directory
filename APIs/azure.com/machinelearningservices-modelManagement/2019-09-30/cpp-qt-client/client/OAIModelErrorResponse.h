/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIModelErrorResponse.h
 *
 * The Model Management Service Error object.
 */

#ifndef OAIModelErrorResponse_H
#define OAIModelErrorResponse_H

#include <QJsonObject>

#include "OAIErrorDetails.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIErrorDetails;

class OAIModelErrorResponse : public OAIObject {
public:
    OAIModelErrorResponse();
    OAIModelErrorResponse(QString json);
    ~OAIModelErrorResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QList<OAIErrorDetails> getDetails() const;
    void setDetails(const QList<OAIErrorDetails> &details);
    bool is_details_Set() const;
    bool is_details_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    qint32 getStatusCode() const;
    void setStatusCode(const qint32 &status_code);
    bool is_status_code_Set() const;
    bool is_status_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QList<OAIErrorDetails> m_details;
    bool m_details_isSet;
    bool m_details_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    qint32 m_status_code;
    bool m_status_code_isSet;
    bool m_status_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIModelErrorResponse)

#endif // OAIModelErrorResponse_H
