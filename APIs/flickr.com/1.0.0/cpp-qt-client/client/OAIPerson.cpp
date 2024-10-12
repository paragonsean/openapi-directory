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

#include "OAIPerson.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPerson::OAIPerson(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPerson::OAIPerson() {
    this->initializeModel();
}

OAIPerson::~OAIPerson() {}

void OAIPerson::initializeModel() {

    m_can_buy_pro_isSet = false;
    m_can_buy_pro_isValid = false;

    m_cover_isSet = false;
    m_cover_isValid = false;

    m_coverphoto_isSet = false;
    m_coverphoto_isValid = false;

    m_coverphoto_farm_isSet = false;
    m_coverphoto_farm_isValid = false;

    m_coverphoto_server_isSet = false;
    m_coverphoto_server_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_disable_keyboard_shortcuts_isSet = false;
    m_disable_keyboard_shortcuts_isValid = false;

    m_expire_isSet = false;
    m_expire_isValid = false;

    m_has_stats_isSet = false;
    m_has_stats_isValid = false;

    m_iconfarm_isSet = false;
    m_iconfarm_isValid = false;

    m_iconserver_isSet = false;
    m_iconserver_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_ad_free_isSet = false;
    m_is_ad_free_isValid = false;

    m_ispro_isSet = false;
    m_ispro_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_mbox_sha1sum_isSet = false;
    m_mbox_sha1sum_isValid = false;

    m_mobileurl_isSet = false;
    m_mobileurl_isValid = false;

    m_nsid_isSet = false;
    m_nsid_isValid = false;

    m_path_alias_isSet = false;
    m_path_alias_isValid = false;

    m_photos_isSet = false;
    m_photos_isValid = false;

    m_photosurl_isSet = false;
    m_photosurl_isValid = false;

    m_profileurl_isSet = false;
    m_profileurl_isValid = false;

    m_realname_isSet = false;
    m_realname_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;

    m_unread_messages_isSet = false;
    m_unread_messages_isValid = false;

    m_user_secret_isSet = false;
    m_user_secret_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_yintl_isSet = false;
    m_yintl_isValid = false;
}

void OAIPerson::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPerson::fromJsonObject(QJsonObject json) {

    m_can_buy_pro_isValid = ::OpenAPI::fromJsonValue(m_can_buy_pro, json[QString("can_buy_pro")]);
    m_can_buy_pro_isSet = !json[QString("can_buy_pro")].isNull() && m_can_buy_pro_isValid;

    m_cover_isValid = ::OpenAPI::fromJsonValue(m_cover, json[QString("cover")]);
    m_cover_isSet = !json[QString("cover")].isNull() && m_cover_isValid;

    m_coverphoto_isValid = ::OpenAPI::fromJsonValue(m_coverphoto, json[QString("coverphoto")]);
    m_coverphoto_isSet = !json[QString("coverphoto")].isNull() && m_coverphoto_isValid;

    m_coverphoto_farm_isValid = ::OpenAPI::fromJsonValue(m_coverphoto_farm, json[QString("coverphoto_farm")]);
    m_coverphoto_farm_isSet = !json[QString("coverphoto_farm")].isNull() && m_coverphoto_farm_isValid;

    m_coverphoto_server_isValid = ::OpenAPI::fromJsonValue(m_coverphoto_server, json[QString("coverphoto_server")]);
    m_coverphoto_server_isSet = !json[QString("coverphoto_server")].isNull() && m_coverphoto_server_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_disable_keyboard_shortcuts_isValid = ::OpenAPI::fromJsonValue(m_disable_keyboard_shortcuts, json[QString("disable_keyboard_shortcuts")]);
    m_disable_keyboard_shortcuts_isSet = !json[QString("disable_keyboard_shortcuts")].isNull() && m_disable_keyboard_shortcuts_isValid;

    m_expire_isValid = ::OpenAPI::fromJsonValue(m_expire, json[QString("expire")]);
    m_expire_isSet = !json[QString("expire")].isNull() && m_expire_isValid;

    m_has_stats_isValid = ::OpenAPI::fromJsonValue(m_has_stats, json[QString("has_stats")]);
    m_has_stats_isSet = !json[QString("has_stats")].isNull() && m_has_stats_isValid;

    m_iconfarm_isValid = ::OpenAPI::fromJsonValue(m_iconfarm, json[QString("iconfarm")]);
    m_iconfarm_isSet = !json[QString("iconfarm")].isNull() && m_iconfarm_isValid;

    m_iconserver_isValid = ::OpenAPI::fromJsonValue(m_iconserver, json[QString("iconserver")]);
    m_iconserver_isSet = !json[QString("iconserver")].isNull() && m_iconserver_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_ad_free_isValid = ::OpenAPI::fromJsonValue(m_is_ad_free, json[QString("is_ad_free")]);
    m_is_ad_free_isSet = !json[QString("is_ad_free")].isNull() && m_is_ad_free_isValid;

    m_ispro_isValid = ::OpenAPI::fromJsonValue(m_ispro, json[QString("ispro")]);
    m_ispro_isSet = !json[QString("ispro")].isNull() && m_ispro_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_mbox_sha1sum_isValid = ::OpenAPI::fromJsonValue(m_mbox_sha1sum, json[QString("mbox_sha1sum")]);
    m_mbox_sha1sum_isSet = !json[QString("mbox_sha1sum")].isNull() && m_mbox_sha1sum_isValid;

    m_mobileurl_isValid = ::OpenAPI::fromJsonValue(m_mobileurl, json[QString("mobileurl")]);
    m_mobileurl_isSet = !json[QString("mobileurl")].isNull() && m_mobileurl_isValid;

    m_nsid_isValid = ::OpenAPI::fromJsonValue(m_nsid, json[QString("nsid")]);
    m_nsid_isSet = !json[QString("nsid")].isNull() && m_nsid_isValid;

    m_path_alias_isValid = ::OpenAPI::fromJsonValue(m_path_alias, json[QString("path_alias")]);
    m_path_alias_isSet = !json[QString("path_alias")].isNull() && m_path_alias_isValid;

    m_photos_isValid = ::OpenAPI::fromJsonValue(m_photos, json[QString("photos")]);
    m_photos_isSet = !json[QString("photos")].isNull() && m_photos_isValid;

    m_photosurl_isValid = ::OpenAPI::fromJsonValue(m_photosurl, json[QString("photosurl")]);
    m_photosurl_isSet = !json[QString("photosurl")].isNull() && m_photosurl_isValid;

    m_profileurl_isValid = ::OpenAPI::fromJsonValue(m_profileurl, json[QString("profileurl")]);
    m_profileurl_isSet = !json[QString("profileurl")].isNull() && m_profileurl_isValid;

    m_realname_isValid = ::OpenAPI::fromJsonValue(m_realname, json[QString("realname")]);
    m_realname_isSet = !json[QString("realname")].isNull() && m_realname_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;

    m_unread_messages_isValid = ::OpenAPI::fromJsonValue(m_unread_messages, json[QString("unread_messages")]);
    m_unread_messages_isSet = !json[QString("unread_messages")].isNull() && m_unread_messages_isValid;

    m_user_secret_isValid = ::OpenAPI::fromJsonValue(m_user_secret, json[QString("user_secret")]);
    m_user_secret_isSet = !json[QString("user_secret")].isNull() && m_user_secret_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_yintl_isValid = ::OpenAPI::fromJsonValue(m_yintl, json[QString("yintl")]);
    m_yintl_isSet = !json[QString("yintl")].isNull() && m_yintl_isValid;
}

QString OAIPerson::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPerson::asJsonObject() const {
    QJsonObject obj;
    if (m_can_buy_pro_isSet) {
        obj.insert(QString("can_buy_pro"), ::OpenAPI::toJsonValue(m_can_buy_pro));
    }
    if (m_cover.isSet()) {
        obj.insert(QString("cover"), ::OpenAPI::toJsonValue(m_cover));
    }
    if (m_coverphoto.isSet()) {
        obj.insert(QString("coverphoto"), ::OpenAPI::toJsonValue(m_coverphoto));
    }
    if (m_coverphoto_farm_isSet) {
        obj.insert(QString("coverphoto_farm"), ::OpenAPI::toJsonValue(m_coverphoto_farm));
    }
    if (m_coverphoto_server_isSet) {
        obj.insert(QString("coverphoto_server"), ::OpenAPI::toJsonValue(m_coverphoto_server));
    }
    if (m_description.isSet()) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_disable_keyboard_shortcuts.isSet()) {
        obj.insert(QString("disable_keyboard_shortcuts"), ::OpenAPI::toJsonValue(m_disable_keyboard_shortcuts));
    }
    if (m_expire_isSet) {
        obj.insert(QString("expire"), ::OpenAPI::toJsonValue(m_expire));
    }
    if (m_has_stats_isSet) {
        obj.insert(QString("has_stats"), ::OpenAPI::toJsonValue(m_has_stats));
    }
    if (m_iconfarm_isSet) {
        obj.insert(QString("iconfarm"), ::OpenAPI::toJsonValue(m_iconfarm));
    }
    if (m_iconserver_isSet) {
        obj.insert(QString("iconserver"), ::OpenAPI::toJsonValue(m_iconserver));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_ad_free_isSet) {
        obj.insert(QString("is_ad_free"), ::OpenAPI::toJsonValue(m_is_ad_free));
    }
    if (m_ispro_isSet) {
        obj.insert(QString("ispro"), ::OpenAPI::toJsonValue(m_ispro));
    }
    if (m_location.isSet()) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_mbox_sha1sum.isSet()) {
        obj.insert(QString("mbox_sha1sum"), ::OpenAPI::toJsonValue(m_mbox_sha1sum));
    }
    if (m_mobileurl.isSet()) {
        obj.insert(QString("mobileurl"), ::OpenAPI::toJsonValue(m_mobileurl));
    }
    if (m_nsid_isSet) {
        obj.insert(QString("nsid"), ::OpenAPI::toJsonValue(m_nsid));
    }
    if (m_path_alias_isSet) {
        obj.insert(QString("path_alias"), ::OpenAPI::toJsonValue(m_path_alias));
    }
    if (m_photos.isSet()) {
        obj.insert(QString("photos"), ::OpenAPI::toJsonValue(m_photos));
    }
    if (m_photosurl.isSet()) {
        obj.insert(QString("photosurl"), ::OpenAPI::toJsonValue(m_photosurl));
    }
    if (m_profileurl.isSet()) {
        obj.insert(QString("profileurl"), ::OpenAPI::toJsonValue(m_profileurl));
    }
    if (m_realname.isSet()) {
        obj.insert(QString("realname"), ::OpenAPI::toJsonValue(m_realname));
    }
    if (m_timezone.isSet()) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
    }
    if (m_unread_messages.isSet()) {
        obj.insert(QString("unread_messages"), ::OpenAPI::toJsonValue(m_unread_messages));
    }
    if (m_user_secret_isSet) {
        obj.insert(QString("user_secret"), ::OpenAPI::toJsonValue(m_user_secret));
    }
    if (m_username.isSet()) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_yintl_isSet) {
        obj.insert(QString("yintl"), ::OpenAPI::toJsonValue(m_yintl));
    }
    return obj;
}

bool OAIPerson::isCanBuyPro() const {
    return m_can_buy_pro;
}
void OAIPerson::setCanBuyPro(const bool &can_buy_pro) {
    m_can_buy_pro = can_buy_pro;
    m_can_buy_pro_isSet = true;
}

bool OAIPerson::is_can_buy_pro_Set() const{
    return m_can_buy_pro_isSet;
}

bool OAIPerson::is_can_buy_pro_Valid() const{
    return m_can_buy_pro_isValid;
}

OAICover OAIPerson::getCover() const {
    return m_cover;
}
void OAIPerson::setCover(const OAICover &cover) {
    m_cover = cover;
    m_cover_isSet = true;
}

bool OAIPerson::is_cover_Set() const{
    return m_cover_isSet;
}

bool OAIPerson::is_cover_Valid() const{
    return m_cover_isValid;
}

OAIPhotoURLs OAIPerson::getCoverphoto() const {
    return m_coverphoto;
}
void OAIPerson::setCoverphoto(const OAIPhotoURLs &coverphoto) {
    m_coverphoto = coverphoto;
    m_coverphoto_isSet = true;
}

bool OAIPerson::is_coverphoto_Set() const{
    return m_coverphoto_isSet;
}

bool OAIPerson::is_coverphoto_Valid() const{
    return m_coverphoto_isValid;
}

QString OAIPerson::getCoverphotoFarm() const {
    return m_coverphoto_farm;
}
void OAIPerson::setCoverphotoFarm(const QString &coverphoto_farm) {
    m_coverphoto_farm = coverphoto_farm;
    m_coverphoto_farm_isSet = true;
}

bool OAIPerson::is_coverphoto_farm_Set() const{
    return m_coverphoto_farm_isSet;
}

bool OAIPerson::is_coverphoto_farm_Valid() const{
    return m_coverphoto_farm_isValid;
}

QString OAIPerson::getCoverphotoServer() const {
    return m_coverphoto_server;
}
void OAIPerson::setCoverphotoServer(const QString &coverphoto_server) {
    m_coverphoto_server = coverphoto_server;
    m_coverphoto_server_isSet = true;
}

bool OAIPerson::is_coverphoto_server_Set() const{
    return m_coverphoto_server_isSet;
}

bool OAIPerson::is_coverphoto_server_Valid() const{
    return m_coverphoto_server_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getDescription() const {
    return m_description;
}
void OAIPerson::setDescription(const OAIGetFavoritesContextByID_200_response_count &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPerson::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPerson::is_description_Valid() const{
    return m_description_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getDisableKeyboardShortcuts() const {
    return m_disable_keyboard_shortcuts;
}
void OAIPerson::setDisableKeyboardShortcuts(const OAIGetFavoritesContextByID_200_response_count &disable_keyboard_shortcuts) {
    m_disable_keyboard_shortcuts = disable_keyboard_shortcuts;
    m_disable_keyboard_shortcuts_isSet = true;
}

bool OAIPerson::is_disable_keyboard_shortcuts_Set() const{
    return m_disable_keyboard_shortcuts_isSet;
}

bool OAIPerson::is_disable_keyboard_shortcuts_Valid() const{
    return m_disable_keyboard_shortcuts_isValid;
}

bool OAIPerson::isExpire() const {
    return m_expire;
}
void OAIPerson::setExpire(const bool &expire) {
    m_expire = expire;
    m_expire_isSet = true;
}

bool OAIPerson::is_expire_Set() const{
    return m_expire_isSet;
}

bool OAIPerson::is_expire_Valid() const{
    return m_expire_isValid;
}

bool OAIPerson::isHasStats() const {
    return m_has_stats;
}
void OAIPerson::setHasStats(const bool &has_stats) {
    m_has_stats = has_stats;
    m_has_stats_isSet = true;
}

bool OAIPerson::is_has_stats_Set() const{
    return m_has_stats_isSet;
}

bool OAIPerson::is_has_stats_Valid() const{
    return m_has_stats_isValid;
}

QString OAIPerson::getIconfarm() const {
    return m_iconfarm;
}
void OAIPerson::setIconfarm(const QString &iconfarm) {
    m_iconfarm = iconfarm;
    m_iconfarm_isSet = true;
}

bool OAIPerson::is_iconfarm_Set() const{
    return m_iconfarm_isSet;
}

bool OAIPerson::is_iconfarm_Valid() const{
    return m_iconfarm_isValid;
}

QString OAIPerson::getIconserver() const {
    return m_iconserver;
}
void OAIPerson::setIconserver(const QString &iconserver) {
    m_iconserver = iconserver;
    m_iconserver_isSet = true;
}

bool OAIPerson::is_iconserver_Set() const{
    return m_iconserver_isSet;
}

bool OAIPerson::is_iconserver_Valid() const{
    return m_iconserver_isValid;
}

QString OAIPerson::getId() const {
    return m_id;
}
void OAIPerson::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPerson::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPerson::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIPerson::isIsAdFree() const {
    return m_is_ad_free;
}
void OAIPerson::setIsAdFree(const bool &is_ad_free) {
    m_is_ad_free = is_ad_free;
    m_is_ad_free_isSet = true;
}

bool OAIPerson::is_is_ad_free_Set() const{
    return m_is_ad_free_isSet;
}

bool OAIPerson::is_is_ad_free_Valid() const{
    return m_is_ad_free_isValid;
}

bool OAIPerson::isIspro() const {
    return m_ispro;
}
void OAIPerson::setIspro(const bool &ispro) {
    m_ispro = ispro;
    m_ispro_isSet = true;
}

bool OAIPerson::is_ispro_Set() const{
    return m_ispro_isSet;
}

bool OAIPerson::is_ispro_Valid() const{
    return m_ispro_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getLocation() const {
    return m_location;
}
void OAIPerson::setLocation(const OAIGetFavoritesContextByID_200_response_count &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIPerson::is_location_Set() const{
    return m_location_isSet;
}

bool OAIPerson::is_location_Valid() const{
    return m_location_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getMboxSha1sum() const {
    return m_mbox_sha1sum;
}
void OAIPerson::setMboxSha1sum(const OAIGetFavoritesContextByID_200_response_count &mbox_sha1sum) {
    m_mbox_sha1sum = mbox_sha1sum;
    m_mbox_sha1sum_isSet = true;
}

bool OAIPerson::is_mbox_sha1sum_Set() const{
    return m_mbox_sha1sum_isSet;
}

bool OAIPerson::is_mbox_sha1sum_Valid() const{
    return m_mbox_sha1sum_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getMobileurl() const {
    return m_mobileurl;
}
void OAIPerson::setMobileurl(const OAIGetFavoritesContextByID_200_response_count &mobileurl) {
    m_mobileurl = mobileurl;
    m_mobileurl_isSet = true;
}

bool OAIPerson::is_mobileurl_Set() const{
    return m_mobileurl_isSet;
}

bool OAIPerson::is_mobileurl_Valid() const{
    return m_mobileurl_isValid;
}

QString OAIPerson::getNsid() const {
    return m_nsid;
}
void OAIPerson::setNsid(const QString &nsid) {
    m_nsid = nsid;
    m_nsid_isSet = true;
}

bool OAIPerson::is_nsid_Set() const{
    return m_nsid_isSet;
}

bool OAIPerson::is_nsid_Valid() const{
    return m_nsid_isValid;
}

QString OAIPerson::getPathAlias() const {
    return m_path_alias;
}
void OAIPerson::setPathAlias(const QString &path_alias) {
    m_path_alias = path_alias;
    m_path_alias_isSet = true;
}

bool OAIPerson::is_path_alias_Set() const{
    return m_path_alias_isSet;
}

bool OAIPerson::is_path_alias_Valid() const{
    return m_path_alias_isValid;
}

OAIPerson_photos OAIPerson::getPhotos() const {
    return m_photos;
}
void OAIPerson::setPhotos(const OAIPerson_photos &photos) {
    m_photos = photos;
    m_photos_isSet = true;
}

bool OAIPerson::is_photos_Set() const{
    return m_photos_isSet;
}

bool OAIPerson::is_photos_Valid() const{
    return m_photos_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getPhotosurl() const {
    return m_photosurl;
}
void OAIPerson::setPhotosurl(const OAIGetFavoritesContextByID_200_response_count &photosurl) {
    m_photosurl = photosurl;
    m_photosurl_isSet = true;
}

bool OAIPerson::is_photosurl_Set() const{
    return m_photosurl_isSet;
}

bool OAIPerson::is_photosurl_Valid() const{
    return m_photosurl_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getProfileurl() const {
    return m_profileurl;
}
void OAIPerson::setProfileurl(const OAIGetFavoritesContextByID_200_response_count &profileurl) {
    m_profileurl = profileurl;
    m_profileurl_isSet = true;
}

bool OAIPerson::is_profileurl_Set() const{
    return m_profileurl_isSet;
}

bool OAIPerson::is_profileurl_Valid() const{
    return m_profileurl_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getRealname() const {
    return m_realname;
}
void OAIPerson::setRealname(const OAIGetFavoritesContextByID_200_response_count &realname) {
    m_realname = realname;
    m_realname_isSet = true;
}

bool OAIPerson::is_realname_Set() const{
    return m_realname_isSet;
}

bool OAIPerson::is_realname_Valid() const{
    return m_realname_isValid;
}

OAIPerson_timezone OAIPerson::getTimezone() const {
    return m_timezone;
}
void OAIPerson::setTimezone(const OAIPerson_timezone &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAIPerson::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAIPerson::is_timezone_Valid() const{
    return m_timezone_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getUnreadMessages() const {
    return m_unread_messages;
}
void OAIPerson::setUnreadMessages(const OAIGetFavoritesContextByID_200_response_count &unread_messages) {
    m_unread_messages = unread_messages;
    m_unread_messages_isSet = true;
}

bool OAIPerson::is_unread_messages_Set() const{
    return m_unread_messages_isSet;
}

bool OAIPerson::is_unread_messages_Valid() const{
    return m_unread_messages_isValid;
}

QString OAIPerson::getUserSecret() const {
    return m_user_secret;
}
void OAIPerson::setUserSecret(const QString &user_secret) {
    m_user_secret = user_secret;
    m_user_secret_isSet = true;
}

bool OAIPerson::is_user_secret_Set() const{
    return m_user_secret_isSet;
}

bool OAIPerson::is_user_secret_Valid() const{
    return m_user_secret_isValid;
}

OAIGetFavoritesContextByID_200_response_count OAIPerson::getUsername() const {
    return m_username;
}
void OAIPerson::setUsername(const OAIGetFavoritesContextByID_200_response_count &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIPerson::is_username_Set() const{
    return m_username_isSet;
}

bool OAIPerson::is_username_Valid() const{
    return m_username_isValid;
}

QString OAIPerson::getYintl() const {
    return m_yintl;
}
void OAIPerson::setYintl(const QString &yintl) {
    m_yintl = yintl;
    m_yintl_isSet = true;
}

bool OAIPerson::is_yintl_Set() const{
    return m_yintl_isSet;
}

bool OAIPerson::is_yintl_Valid() const{
    return m_yintl_isValid;
}

bool OAIPerson::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_can_buy_pro_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cover.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverphoto.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverphoto_farm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverphoto_server_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_disable_keyboard_shortcuts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_expire_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_stats_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iconfarm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iconserver_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_ad_free_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ispro_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mbox_sha1sum.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mobileurl.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_nsid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_photos.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_photosurl.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_profileurl.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_realname.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_unread_messages.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_secret_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_yintl_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPerson::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
