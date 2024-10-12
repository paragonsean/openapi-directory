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
 * OAIPriceMissingCountDetails.h
 *
 * The reasons that contributed to the price missing count and the total count for each reason.
 */

#ifndef OAIPriceMissingCountDetails_H
#define OAIPriceMissingCountDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPriceMissingCountDetails : public OAIObject {
public:
    OAIPriceMissingCountDetails();
    OAIPriceMissingCountDetails(QString json);
    ~OAIPriceMissingCountDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBandwidthDepletedCount() const;
    void setBandwidthDepletedCount(const QString &bandwidth_depleted_count);
    bool is_bandwidth_depleted_count_Set() const;
    bool is_bandwidth_depleted_count_Valid() const;

    QString getCacheRateMissingCount() const;
    void setCacheRateMissingCount(const QString &cache_rate_missing_count);
    bool is_cache_rate_missing_count_Set() const;
    bool is_cache_rate_missing_count_Valid() const;

    QString getItineraryBlockedCount() const;
    void setItineraryBlockedCount(const QString &itinerary_blocked_count);
    bool is_itinerary_blocked_count_Set() const;
    bool is_itinerary_blocked_count_Valid() const;

    QString getLivePricingErrorCount() const;
    void setLivePricingErrorCount(const QString &live_pricing_error_count);
    bool is_live_pricing_error_count_Set() const;
    bool is_live_pricing_error_count_Valid() const;

    QString getLivePricingNotSetupCount() const;
    void setLivePricingNotSetupCount(const QString &live_pricing_not_setup_count);
    bool is_live_pricing_not_setup_count_Set() const;
    bool is_live_pricing_not_setup_count_Valid() const;

    QString getLivePricingTimeoutCount() const;
    void setLivePricingTimeoutCount(const QString &live_pricing_timeout_count);
    bool is_live_pricing_timeout_count_Set() const;
    bool is_live_pricing_timeout_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_bandwidth_depleted_count;
    bool m_bandwidth_depleted_count_isSet;
    bool m_bandwidth_depleted_count_isValid;

    QString m_cache_rate_missing_count;
    bool m_cache_rate_missing_count_isSet;
    bool m_cache_rate_missing_count_isValid;

    QString m_itinerary_blocked_count;
    bool m_itinerary_blocked_count_isSet;
    bool m_itinerary_blocked_count_isValid;

    QString m_live_pricing_error_count;
    bool m_live_pricing_error_count_isSet;
    bool m_live_pricing_error_count_isValid;

    QString m_live_pricing_not_setup_count;
    bool m_live_pricing_not_setup_count_isSet;
    bool m_live_pricing_not_setup_count_isValid;

    QString m_live_pricing_timeout_count;
    bool m_live_pricing_timeout_count_isSet;
    bool m_live_pricing_timeout_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPriceMissingCountDetails)

#endif // OAIPriceMissingCountDetails_H
