/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITestResultSummary.h
 *
 * Represents the summary result of a Service or API test run by Microcks. 
 */

#ifndef OAITestResultSummary_H
#define OAITestResultSummary_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITestResultSummary : public OAIObject {
public:
    OAITestResultSummary();
    OAITestResultSummary(QString json);
    ~OAITestResultSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getServiceId() const;
    void setServiceId(const QString &service_id);
    bool is_service_id_Set() const;
    bool is_service_id_Valid() const;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    qint64 getTestDate() const;
    void setTestDate(const qint64 &test_date);
    bool is_test_date_Set() const;
    bool is_test_date_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_service_id;
    bool m_service_id_isSet;
    bool m_service_id_isValid;

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;

    qint64 m_test_date;
    bool m_test_date_isSet;
    bool m_test_date_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITestResultSummary)

#endif // OAITestResultSummary_H
