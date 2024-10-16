/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPerson.h
 *
 * 
 */

#ifndef OAIPerson_H
#define OAIPerson_H

#include <QJsonObject>

#include "OAICover.h"
#include "OAIGetFavoritesContextByID_200_response_count.h"
#include "OAIPerson_photos.h"
#include "OAIPerson_timezone.h"
#include "OAIPhotoURLs.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICover;
class OAIPhotoURLs;
class OAIGetFavoritesContextByID_200_response_count;
class OAIPerson_photos;
class OAIPerson_timezone;

class OAIPerson : public OAIObject {
public:
    OAIPerson();
    OAIPerson(QString json);
    ~OAIPerson() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCanBuyPro() const;
    void setCanBuyPro(const bool &can_buy_pro);
    bool is_can_buy_pro_Set() const;
    bool is_can_buy_pro_Valid() const;

    OAICover getCover() const;
    void setCover(const OAICover &cover);
    bool is_cover_Set() const;
    bool is_cover_Valid() const;

    OAIPhotoURLs getCoverphoto() const;
    void setCoverphoto(const OAIPhotoURLs &coverphoto);
    bool is_coverphoto_Set() const;
    bool is_coverphoto_Valid() const;

    QString getCoverphotoFarm() const;
    void setCoverphotoFarm(const QString &coverphoto_farm);
    bool is_coverphoto_farm_Set() const;
    bool is_coverphoto_farm_Valid() const;

    QString getCoverphotoServer() const;
    void setCoverphotoServer(const QString &coverphoto_server);
    bool is_coverphoto_server_Set() const;
    bool is_coverphoto_server_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getDescription() const;
    void setDescription(const OAIGetFavoritesContextByID_200_response_count &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getDisableKeyboardShortcuts() const;
    void setDisableKeyboardShortcuts(const OAIGetFavoritesContextByID_200_response_count &disable_keyboard_shortcuts);
    bool is_disable_keyboard_shortcuts_Set() const;
    bool is_disable_keyboard_shortcuts_Valid() const;

    bool isExpire() const;
    void setExpire(const bool &expire);
    bool is_expire_Set() const;
    bool is_expire_Valid() const;

    bool isHasStats() const;
    void setHasStats(const bool &has_stats);
    bool is_has_stats_Set() const;
    bool is_has_stats_Valid() const;

    QString getIconfarm() const;
    void setIconfarm(const QString &iconfarm);
    bool is_iconfarm_Set() const;
    bool is_iconfarm_Valid() const;

    QString getIconserver() const;
    void setIconserver(const QString &iconserver);
    bool is_iconserver_Set() const;
    bool is_iconserver_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsAdFree() const;
    void setIsAdFree(const bool &is_ad_free);
    bool is_is_ad_free_Set() const;
    bool is_is_ad_free_Valid() const;

    bool isIspro() const;
    void setIspro(const bool &ispro);
    bool is_ispro_Set() const;
    bool is_ispro_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getLocation() const;
    void setLocation(const OAIGetFavoritesContextByID_200_response_count &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getMboxSha1sum() const;
    void setMboxSha1sum(const OAIGetFavoritesContextByID_200_response_count &mbox_sha1sum);
    bool is_mbox_sha1sum_Set() const;
    bool is_mbox_sha1sum_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getMobileurl() const;
    void setMobileurl(const OAIGetFavoritesContextByID_200_response_count &mobileurl);
    bool is_mobileurl_Set() const;
    bool is_mobileurl_Valid() const;

    QString getNsid() const;
    void setNsid(const QString &nsid);
    bool is_nsid_Set() const;
    bool is_nsid_Valid() const;

    QString getPathAlias() const;
    void setPathAlias(const QString &path_alias);
    bool is_path_alias_Set() const;
    bool is_path_alias_Valid() const;

    OAIPerson_photos getPhotos() const;
    void setPhotos(const OAIPerson_photos &photos);
    bool is_photos_Set() const;
    bool is_photos_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getPhotosurl() const;
    void setPhotosurl(const OAIGetFavoritesContextByID_200_response_count &photosurl);
    bool is_photosurl_Set() const;
    bool is_photosurl_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getProfileurl() const;
    void setProfileurl(const OAIGetFavoritesContextByID_200_response_count &profileurl);
    bool is_profileurl_Set() const;
    bool is_profileurl_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getRealname() const;
    void setRealname(const OAIGetFavoritesContextByID_200_response_count &realname);
    bool is_realname_Set() const;
    bool is_realname_Valid() const;

    OAIPerson_timezone getTimezone() const;
    void setTimezone(const OAIPerson_timezone &timezone);
    bool is_timezone_Set() const;
    bool is_timezone_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getUnreadMessages() const;
    void setUnreadMessages(const OAIGetFavoritesContextByID_200_response_count &unread_messages);
    bool is_unread_messages_Set() const;
    bool is_unread_messages_Valid() const;

    QString getUserSecret() const;
    void setUserSecret(const QString &user_secret);
    bool is_user_secret_Set() const;
    bool is_user_secret_Valid() const;

    OAIGetFavoritesContextByID_200_response_count getUsername() const;
    void setUsername(const OAIGetFavoritesContextByID_200_response_count &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    QString getYintl() const;
    void setYintl(const QString &yintl);
    bool is_yintl_Set() const;
    bool is_yintl_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_can_buy_pro;
    bool m_can_buy_pro_isSet;
    bool m_can_buy_pro_isValid;

    OAICover m_cover;
    bool m_cover_isSet;
    bool m_cover_isValid;

    OAIPhotoURLs m_coverphoto;
    bool m_coverphoto_isSet;
    bool m_coverphoto_isValid;

    QString m_coverphoto_farm;
    bool m_coverphoto_farm_isSet;
    bool m_coverphoto_farm_isValid;

    QString m_coverphoto_server;
    bool m_coverphoto_server_isSet;
    bool m_coverphoto_server_isValid;

    OAIGetFavoritesContextByID_200_response_count m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIGetFavoritesContextByID_200_response_count m_disable_keyboard_shortcuts;
    bool m_disable_keyboard_shortcuts_isSet;
    bool m_disable_keyboard_shortcuts_isValid;

    bool m_expire;
    bool m_expire_isSet;
    bool m_expire_isValid;

    bool m_has_stats;
    bool m_has_stats_isSet;
    bool m_has_stats_isValid;

    QString m_iconfarm;
    bool m_iconfarm_isSet;
    bool m_iconfarm_isValid;

    QString m_iconserver;
    bool m_iconserver_isSet;
    bool m_iconserver_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_ad_free;
    bool m_is_ad_free_isSet;
    bool m_is_ad_free_isValid;

    bool m_ispro;
    bool m_ispro_isSet;
    bool m_ispro_isValid;

    OAIGetFavoritesContextByID_200_response_count m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    OAIGetFavoritesContextByID_200_response_count m_mbox_sha1sum;
    bool m_mbox_sha1sum_isSet;
    bool m_mbox_sha1sum_isValid;

    OAIGetFavoritesContextByID_200_response_count m_mobileurl;
    bool m_mobileurl_isSet;
    bool m_mobileurl_isValid;

    QString m_nsid;
    bool m_nsid_isSet;
    bool m_nsid_isValid;

    QString m_path_alias;
    bool m_path_alias_isSet;
    bool m_path_alias_isValid;

    OAIPerson_photos m_photos;
    bool m_photos_isSet;
    bool m_photos_isValid;

    OAIGetFavoritesContextByID_200_response_count m_photosurl;
    bool m_photosurl_isSet;
    bool m_photosurl_isValid;

    OAIGetFavoritesContextByID_200_response_count m_profileurl;
    bool m_profileurl_isSet;
    bool m_profileurl_isValid;

    OAIGetFavoritesContextByID_200_response_count m_realname;
    bool m_realname_isSet;
    bool m_realname_isValid;

    OAIPerson_timezone m_timezone;
    bool m_timezone_isSet;
    bool m_timezone_isValid;

    OAIGetFavoritesContextByID_200_response_count m_unread_messages;
    bool m_unread_messages_isSet;
    bool m_unread_messages_isValid;

    QString m_user_secret;
    bool m_user_secret_isSet;
    bool m_user_secret_isValid;

    OAIGetFavoritesContextByID_200_response_count m_username;
    bool m_username_isSet;
    bool m_username_isValid;

    QString m_yintl;
    bool m_yintl_isSet;
    bool m_yintl_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPerson)

#endif // OAIPerson_H
