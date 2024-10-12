/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExtensions_GetMonitoringStatus_default_response.h
 *
 * Describes the format of Error response.
 */

#ifndef OAIExtensions_GetMonitoringStatus_default_response_H
#define OAIExtensions_GetMonitoringStatus_default_response_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIExtensions_GetMonitoringStatus_default_response : public OAIObject {
public:
    OAIExtensions_GetMonitoringStatus_default_response();
    OAIExtensions_GetMonitoringStatus_default_response(QString json);
    ~OAIExtensions_GetMonitoringStatus_default_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

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

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExtensions_GetMonitoringStatus_default_response)

#endif // OAIExtensions_GetMonitoringStatus_default_response_H
