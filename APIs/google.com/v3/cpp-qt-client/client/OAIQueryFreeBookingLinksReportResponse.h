/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQueryFreeBookingLinksReportResponse.h
 *
 * **DEPRECATED:** Use &#x60;QueryPropertyPerformanceReportResponse&#x60; with &#x60;PropertyPerformanceReportService&#x60; instead. Response message for FreeBookingLinksReportService.QueryFreeBookingLinksReport.
 */

#ifndef OAIQueryFreeBookingLinksReportResponse_H
#define OAIQueryFreeBookingLinksReportResponse_H

#include <QJsonObject>

#include "OAIFreeBookingLinksResult.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFreeBookingLinksResult;

class OAIQueryFreeBookingLinksReportResponse : public OAIObject {
public:
    OAIQueryFreeBookingLinksReportResponse();
    OAIQueryFreeBookingLinksReportResponse(QString json);
    ~OAIQueryFreeBookingLinksReportResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextPageToken() const;
    void setNextPageToken(const QString &next_page_token);
    bool is_next_page_token_Set() const;
    bool is_next_page_token_Valid() const;

    QList<OAIFreeBookingLinksResult> getResults() const;
    void setResults(const QList<OAIFreeBookingLinksResult> &results);
    bool is_results_Set() const;
    bool is_results_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_page_token;
    bool m_next_page_token_isSet;
    bool m_next_page_token_isValid;

    QList<OAIFreeBookingLinksResult> m_results;
    bool m_results_isSet;
    bool m_results_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQueryFreeBookingLinksReportResponse)

#endif // OAIQueryFreeBookingLinksReportResponse_H
