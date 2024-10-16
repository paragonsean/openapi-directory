/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPerformanceProfile.h
 *
 * PerformanceProfile represents the performance profile that needs to be saved
 */

#ifndef OAIPerformanceProfile_H
#define OAIPerformanceProfile_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPerformanceProfile : public OAIObject {
public:
    OAIPerformanceProfile();
    OAIPerformanceProfile(QString json);
    ~OAIPerformanceProfile() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getConcurrentRequest() const;
    void setConcurrentRequest(const qint64 &concurrent_request);
    bool is_concurrent_request_Set() const;
    bool is_concurrent_request_Valid() const;

    QString getContentType() const;
    void setContentType(const QString &content_type);
    bool is_content_type_Set() const;
    bool is_content_type_Valid() const;

    OAIObject getCreatedAt() const;
    void setCreatedAt(const OAIObject &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDuration() const;
    void setDuration(const QString &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QList<QString> getEndpoints() const;
    void setEndpoints(const QList<QString> &endpoints);
    bool is_endpoints_Set() const;
    bool is_endpoints_Valid() const;

    QList<qint32> getId() const;
    void setId(const QList<qint32> &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIObject getLastRun() const;
    void setLastRun(const OAIObject &last_run);
    bool is_last_run_Set() const;
    bool is_last_run_Valid() const;

    QList<QString> getLoadGenerators() const;
    void setLoadGenerators(const QList<QString> &load_generators);
    bool is_load_generators_Set() const;
    bool is_load_generators_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint64 getQps() const;
    void setQps(const qint64 &qps);
    bool is_qps_Set() const;
    bool is_qps_Valid() const;

    QString getRequestBody() const;
    void setRequestBody(const QString &request_body);
    bool is_request_body_Set() const;
    bool is_request_body_Valid() const;

    QString getRequestCookies() const;
    void setRequestCookies(const QString &request_cookies);
    bool is_request_cookies_Set() const;
    bool is_request_cookies_Valid() const;

    QString getRequestHeaders() const;
    void setRequestHeaders(const QString &request_headers);
    bool is_request_headers_Set() const;
    bool is_request_headers_Valid() const;

    QList<qint32> getSchedule() const;
    void setSchedule(const QList<qint32> &schedule);
    bool is_schedule_Set() const;
    bool is_schedule_Valid() const;

    QString getServiceMesh() const;
    void setServiceMesh(const QString &service_mesh);
    bool is_service_mesh_Set() const;
    bool is_service_mesh_Valid() const;

    qint64 getTotalResults() const;
    void setTotalResults(const qint64 &total_results);
    bool is_total_results_Set() const;
    bool is_total_results_Valid() const;

    OAIObject getUpdatedAt() const;
    void setUpdatedAt(const OAIObject &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_concurrent_request;
    bool m_concurrent_request_isSet;
    bool m_concurrent_request_isValid;

    QString m_content_type;
    bool m_content_type_isSet;
    bool m_content_type_isValid;

    OAIObject m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QList<QString> m_endpoints;
    bool m_endpoints_isSet;
    bool m_endpoints_isValid;

    QList<qint32> m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIObject m_last_run;
    bool m_last_run_isSet;
    bool m_last_run_isValid;

    QList<QString> m_load_generators;
    bool m_load_generators_isSet;
    bool m_load_generators_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint64 m_qps;
    bool m_qps_isSet;
    bool m_qps_isValid;

    QString m_request_body;
    bool m_request_body_isSet;
    bool m_request_body_isValid;

    QString m_request_cookies;
    bool m_request_cookies_isSet;
    bool m_request_cookies_isValid;

    QString m_request_headers;
    bool m_request_headers_isSet;
    bool m_request_headers_isValid;

    QList<qint32> m_schedule;
    bool m_schedule_isSet;
    bool m_schedule_isValid;

    QString m_service_mesh;
    bool m_service_mesh_isSet;
    bool m_service_mesh_isValid;

    qint64 m_total_results;
    bool m_total_results_isSet;
    bool m_total_results_isValid;

    OAIObject m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPerformanceProfile)

#endif // OAIPerformanceProfile_H
