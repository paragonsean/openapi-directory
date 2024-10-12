/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics.h
 *
 * 
 */

#ifndef OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics_H
#define OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics_H

#include <QJsonObject>

#include "OAIApi_Core_Dto_Datapoints_BrowserBaseDestinationItem.h"
#include "OAIApi_Core_Dto_Datapoints_DatapointRetargetingInfo.h"
#include "OAIApi_Core_Dto_Datapoints_MultipleDestinationItem.h"
#include "OAIApi_Core_Dto_Datapoints_UniqueDestinationItem.h"
#include "OAIApi_Core_Dto_Datapoints_UrlByLanguageItem.h"
#include "OAIApi_Core_Dto_Datapoints_UrlByNationItem.h"
#include "OAIApi_Core_Dto_Datapoints_WeightedDestinationItem.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIApi_Core_Dto_Datapoints_BrowserBaseDestinationItem;
class OAIApi_Core_Dto_Datapoints_MultipleDestinationItem;
class OAIApi_Core_Dto_Datapoints_DatapointRetargetingInfo;
class OAIApi_Core_Dto_Datapoints_UniqueDestinationItem;
class OAIApi_Core_Dto_Datapoints_UrlByLanguageItem;
class OAIApi_Core_Dto_Datapoints_UrlByNationItem;
class OAIApi_Core_Dto_Datapoints_WeightedDestinationItem;

class OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics : public OAIObject {
public:
    OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics();
    OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics(QString json);
    ~OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAppendQuery() const;
    void setAppendQuery(const bool &append_query);
    bool is_append_query_Set() const;
    bool is_append_query_Valid() const;

    OAIApi_Core_Dto_Datapoints_BrowserBaseDestinationItem getBrowserDestinationItem() const;
    void setBrowserDestinationItem(const OAIApi_Core_Dto_Datapoints_BrowserBaseDestinationItem &browser_destination_item);
    bool is_browser_destination_item_Set() const;
    bool is_browser_destination_item_Valid() const;

    QString getDestinationMode() const;
    void setDestinationMode(const QString &destination_mode);
    bool is_destination_mode_Set() const;
    bool is_destination_mode_Valid() const;

    qint32 getDomainId() const;
    void setDomainId(const qint32 &domain_id);
    bool is_domain_id_Set() const;
    bool is_domain_id_Valid() const;

    bool isEncodeUrl() const;
    void setEncodeUrl(const bool &encode_url);
    bool is_encode_url_Set() const;
    bool is_encode_url_Valid() const;

    qint64 getExpirationClicks() const;
    void setExpirationClicks(const qint64 &expiration_clicks);
    bool is_expiration_clicks_Set() const;
    bool is_expiration_clicks_Valid() const;

    QString getExpirationDate() const;
    void setExpirationDate(const QString &expiration_date);
    bool is_expiration_date_Set() const;
    bool is_expiration_date_Valid() const;

    QString getFirstUrl() const;
    void setFirstUrl(const QString &first_url);
    bool is_first_url_Set() const;
    bool is_first_url_Valid() const;

    qint32 getGoDomainId() const;
    void setGoDomainId(const qint32 &go_domain_id);
    bool is_go_domain_id_Set() const;
    bool is_go_domain_id_Valid() const;

    bool isHideUrl() const;
    void setHideUrl(const bool &hide_url);
    bool is_hide_url_Set() const;
    bool is_hide_url_Valid() const;

    QString getHideUrlTitle() const;
    void setHideUrlTitle(const QString &hide_url_title);
    bool is_hide_url_title_Set() const;
    bool is_hide_url_title_Valid() const;

    bool isIsAbTest() const;
    void setIsAbTest(const bool &is_ab_test);
    bool is_is_ab_test_Set() const;
    bool is_is_ab_test_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    bool isPauseAfterClicksExpiration() const;
    void setPauseAfterClicksExpiration(const bool &pause_after_clicks_expiration);
    bool is_pause_after_clicks_expiration_Set() const;
    bool is_pause_after_clicks_expiration_Valid() const;

    bool isPauseAfterDateExpiration() const;
    void setPauseAfterDateExpiration(const bool &pause_after_date_expiration);
    bool is_pause_after_date_expiration_Set() const;
    bool is_pause_after_date_expiration_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> getRandomDestinationItems() const;
    void setRandomDestinationItems(const QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> &random_destination_items);
    bool is_random_destination_items_Set() const;
    bool is_random_destination_items_Valid() const;

    QString getRedirectType() const;
    void setRedirectType(const QString &redirect_type);
    bool is_redirect_type_Set() const;
    bool is_redirect_type_Valid() const;

    QString getReferrerClean() const;
    void setReferrerClean(const QString &referrer_clean);
    bool is_referrer_clean_Set() const;
    bool is_referrer_clean_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_DatapointRetargetingInfo> getScripts() const;
    void setScripts(const QList<OAIApi_Core_Dto_Datapoints_DatapointRetargetingInfo> &scripts);
    bool is_scripts_Set() const;
    bool is_scripts_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> getSequentialDestinationItems() const;
    void setSequentialDestinationItems(const QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> &sequential_destination_items);
    bool is_sequential_destination_items_Set() const;
    bool is_sequential_destination_items_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> getSpilloverDestinationItems() const;
    void setSpilloverDestinationItems(const QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> &spillover_destination_items);
    bool is_spillover_destination_items_Set() const;
    bool is_spillover_destination_items_Valid() const;

    OAIApi_Core_Dto_Datapoints_UniqueDestinationItem getUniqueDestinationItem() const;
    void setUniqueDestinationItem(const OAIApi_Core_Dto_Datapoints_UniqueDestinationItem &unique_destination_item);
    bool is_unique_destination_item_Set() const;
    bool is_unique_destination_item_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    QString getUrlAfterClicksExpiration() const;
    void setUrlAfterClicksExpiration(const QString &url_after_clicks_expiration);
    bool is_url_after_clicks_expiration_Set() const;
    bool is_url_after_clicks_expiration_Valid() const;

    QString getUrlAfterDateExpiration() const;
    void setUrlAfterDateExpiration(const QString &url_after_date_expiration);
    bool is_url_after_date_expiration_Set() const;
    bool is_url_after_date_expiration_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_UrlByLanguageItem> getUrlsByLanguage() const;
    void setUrlsByLanguage(const QList<OAIApi_Core_Dto_Datapoints_UrlByLanguageItem> &urls_by_language);
    bool is_urls_by_language_Set() const;
    bool is_urls_by_language_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_UrlByNationItem> getUrlsByNation() const;
    void setUrlsByNation(const QList<OAIApi_Core_Dto_Datapoints_UrlByNationItem> &urls_by_nation);
    bool is_urls_by_nation_Set() const;
    bool is_urls_by_nation_Valid() const;

    QList<OAIApi_Core_Dto_Datapoints_WeightedDestinationItem> getWeightedDestinationItems() const;
    void setWeightedDestinationItems(const QList<OAIApi_Core_Dto_Datapoints_WeightedDestinationItem> &weighted_destination_items);
    bool is_weighted_destination_items_Set() const;
    bool is_weighted_destination_items_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_append_query;
    bool m_append_query_isSet;
    bool m_append_query_isValid;

    OAIApi_Core_Dto_Datapoints_BrowserBaseDestinationItem m_browser_destination_item;
    bool m_browser_destination_item_isSet;
    bool m_browser_destination_item_isValid;

    QString m_destination_mode;
    bool m_destination_mode_isSet;
    bool m_destination_mode_isValid;

    qint32 m_domain_id;
    bool m_domain_id_isSet;
    bool m_domain_id_isValid;

    bool m_encode_url;
    bool m_encode_url_isSet;
    bool m_encode_url_isValid;

    qint64 m_expiration_clicks;
    bool m_expiration_clicks_isSet;
    bool m_expiration_clicks_isValid;

    QString m_expiration_date;
    bool m_expiration_date_isSet;
    bool m_expiration_date_isValid;

    QString m_first_url;
    bool m_first_url_isSet;
    bool m_first_url_isValid;

    qint32 m_go_domain_id;
    bool m_go_domain_id_isSet;
    bool m_go_domain_id_isValid;

    bool m_hide_url;
    bool m_hide_url_isSet;
    bool m_hide_url_isValid;

    QString m_hide_url_title;
    bool m_hide_url_title_isSet;
    bool m_hide_url_title_isValid;

    bool m_is_ab_test;
    bool m_is_ab_test_isSet;
    bool m_is_ab_test_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    bool m_pause_after_clicks_expiration;
    bool m_pause_after_clicks_expiration_isSet;
    bool m_pause_after_clicks_expiration_isValid;

    bool m_pause_after_date_expiration;
    bool m_pause_after_date_expiration_isSet;
    bool m_pause_after_date_expiration_isValid;

    QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> m_random_destination_items;
    bool m_random_destination_items_isSet;
    bool m_random_destination_items_isValid;

    QString m_redirect_type;
    bool m_redirect_type_isSet;
    bool m_redirect_type_isValid;

    QString m_referrer_clean;
    bool m_referrer_clean_isSet;
    bool m_referrer_clean_isValid;

    QList<OAIApi_Core_Dto_Datapoints_DatapointRetargetingInfo> m_scripts;
    bool m_scripts_isSet;
    bool m_scripts_isValid;

    QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> m_sequential_destination_items;
    bool m_sequential_destination_items_isSet;
    bool m_sequential_destination_items_isValid;

    QList<OAIApi_Core_Dto_Datapoints_MultipleDestinationItem> m_spillover_destination_items;
    bool m_spillover_destination_items_isSet;
    bool m_spillover_destination_items_isValid;

    OAIApi_Core_Dto_Datapoints_UniqueDestinationItem m_unique_destination_item;
    bool m_unique_destination_item_isSet;
    bool m_unique_destination_item_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    QString m_url_after_clicks_expiration;
    bool m_url_after_clicks_expiration_isSet;
    bool m_url_after_clicks_expiration_isValid;

    QString m_url_after_date_expiration;
    bool m_url_after_date_expiration_isSet;
    bool m_url_after_date_expiration_isValid;

    QList<OAIApi_Core_Dto_Datapoints_UrlByLanguageItem> m_urls_by_language;
    bool m_urls_by_language_isSet;
    bool m_urls_by_language_isValid;

    QList<OAIApi_Core_Dto_Datapoints_UrlByNationItem> m_urls_by_nation;
    bool m_urls_by_nation_isSet;
    bool m_urls_by_nation_isValid;

    QList<OAIApi_Core_Dto_Datapoints_WeightedDestinationItem> m_weighted_destination_items;
    bool m_weighted_destination_items_isSet;
    bool m_weighted_destination_items_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics)

#endif // OAIApi_Core_Dto_Datapoints_TrackingLinkSpecifics_H
