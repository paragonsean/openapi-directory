/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_H
#define OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner.h"
#include <QDateTime>
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner;

class OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner();
    OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner(QString json);
    ~OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner> getCounts() const;
    void setCounts(const QList<OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner> &counts);
    bool is_counts_Set() const;
    bool is_counts_Valid() const;

    QDateTime getEndTs() const;
    void setEndTs(const QDateTime &end_ts);
    bool is_end_ts_Set() const;
    bool is_end_ts_Valid() const;

    QDateTime getStartTs() const;
    void setStartTs(const QDateTime &start_ts);
    bool is_start_ts_Set() const;
    bool is_start_ts_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner> m_counts;
    bool m_counts_isSet;
    bool m_counts_isValid;

    QDateTime m_end_ts;
    bool m_end_ts_isSet;
    bool m_end_ts_isValid;

    QDateTime m_start_ts;
    bool m_start_ts_isSet;
    bool m_start_ts_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner)

#endif // OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_H
