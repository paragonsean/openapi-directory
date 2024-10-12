/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIJobErrorDetails.h
 *
 * The job error information containing the list of job errors.
 */

#ifndef OAIJobErrorDetails_H
#define OAIJobErrorDetails_H

#include <QJsonObject>

#include "OAIJobErrorItem.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIJobErrorItem;

class OAIJobErrorDetails : public OAIObject {
public:
    OAIJobErrorDetails();
    OAIJobErrorDetails(QString json);
    ~OAIJobErrorDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QList<OAIJobErrorItem> getErrorDetails() const;
    void setErrorDetails(const QList<OAIJobErrorItem> &error_details);
    bool is_error_details_Set() const;
    bool is_error_details_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QList<OAIJobErrorItem> m_error_details;
    bool m_error_details_isSet;
    bool m_error_details_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIJobErrorDetails)

#endif // OAIJobErrorDetails_H
